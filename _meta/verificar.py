#!/usr/bin/env python3
"""Verificador de la migración de apuntes de Notion al vault de Obsidian.

Uso:
    python3 _meta/verificar.py                  # todos los temas marcados como "hecho"
    python3 _meta/verificar.py --tema "Procesos de desarrollo"
    python3 _meta/verificar.py --detalle        # muestra también los bloques cubiertos

Solo usa la biblioteca estándar. Si _raw/ no existe (por ejemplo, en un clone del
repo), las pruebas que dependen del export original (2, 3 y 4) se omiten con aviso.

Pruebas:
  1. Autocontención: sin "_raw", rutas absolutas ni URLs de Notion; todo link local existe.
  2. Imágenes: asignadas al tema / copiadas (sha256) / referenciadas.
  3. Cobertura: cada bloque de los apuntes originales del tema aparece en alguna nota.
  4. Links externos de los apuntes conservados.
  5. Grafo: wikilinks válidos, nombres únicos, sin notas huérfanas.
  +  Formato (advertencias): frontmatter, preguntas de repaso, largo, nombres, índices.
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import sys
import unicodedata
from html.parser import HTMLParser
from urllib.parse import unquote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(RAIZ, "_raw")
META = os.path.join(RAIZ, "_meta")
VAULT_RAMO = os.path.join(RAIZ, "Ingeniería de Software")

UMBRAL_TOKENS = 0.85
UMBRAL_SECUENCIA = 0.80
MAX_LINEAS = 150

errores = []
avisos = []


def error(msg):
    errores.append(msg)
    print(f"  ❌ {msg}")


def aviso(msg):
    avisos.append(msg)
    print(f"  ⚠️  {msg}")


def ok(msg):
    print(f"  ✅ {msg}")


# ---------------------------------------------------------------- normalización

def sin_tildes(texto):
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in texto if not unicodedata.combining(c))


def normalizar(texto):
    """Texto -> minúsculas, sin tildes, sin puntuación ni markdown, espacios colapsados."""
    texto = sin_tildes(texto.lower())
    texto = re.sub(r"[^a-z0-9ñ]+", " ", texto)
    return " ".join(texto.split())


def normalizar_codigo(linea):
    """Línea de código -> sin espacios y con comillas rectas."""
    linea = linea.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return re.sub(r"\s+", "", linea)


def quitar_marcas_callout(texto):
    """Quita los '>' iniciales de callouts/citas para comparar código."""
    return "\n".join(re.sub(r"^(\s*>)+\s?", "", l) for l in texto.splitlines())


# ---------------------------------------------------------------- extracción HTML

BLOQUES = {"p", "li", "pre", "tr", "h1", "h2", "h3", "h4", "blockquote", "figcaption", "summary"}


class ExtractorNotion(HTMLParser):
    """Extrae bloques (párrafo, ítem, fila, código, encabezado), imágenes y links
    del cuerpo de una página exportada de Notion, en orden de documento."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.en_cuerpo = 0
        self.pila = []          # [(tag, partes)]
        self.items = []         # dicts en orden: bloque | imagen | link
        self.ignorar = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "div" and "page-body" in (a.get("class") or ""):
            self.en_cuerpo = 1
            return
        if not self.en_cuerpo:
            return
        if tag in ("style", "script"):
            self.ignorar += 1
        if tag in BLOQUES:
            self.pila.append((tag, []))
        elif tag in ("td", "th") and self.pila:
            self.pila[-1][1].append(" | ")
        elif tag == "br" and self.pila:
            self.pila[-1][1].append("\n")
        elif tag == "img" and a.get("src"):
            self.items.append({"tipo": "imagen", "src": unquote(a["src"])})
        elif tag == "a" and a.get("href"):
            self.items.append({"tipo": "link", "href": a["href"]})

    def handle_endtag(self, tag):
        if not self.en_cuerpo:
            return
        if tag in ("style", "script"):
            self.ignorar -= 1
        if tag in BLOQUES and any(t == tag for t, _ in self.pila):
            while self.pila:
                t, partes = self.pila.pop()
                self._emitir(t, partes)
                if t == tag:
                    break

    def handle_data(self, data):
        if self.en_cuerpo and not self.ignorar and self.pila:
            self.pila[-1][1].append(data)

    def _emitir(self, tag, partes):
        texto = "".join(partes)
        if tag == "pre":
            if texto.strip():
                self.items.append({"tipo": "bloque", "clase": "codigo", "texto": texto})
            return
        texto = " ".join(texto.split())
        if tag == "tr":
            texto = texto.strip(" |")
        if not texto:
            return
        clase = {"li": "item", "tr": "fila"}.get(tag, "encabezado" if tag[0] == "h" else "parrafo")
        self.items.append({"tipo": "bloque", "clase": clase, "texto": texto})


def extraer(ruta_html):
    p = ExtractorNotion()
    with open(ruta_html, encoding="utf-8") as f:
        p.feed(f.read())
    # El orden de emisión es por cierre de etiqueta; un <li> que contiene encabezados
    # se emite después de ellos. Para asignar secciones basta el orden aproximado,
    # porque los rangos se definen por encabezados de nivel superior (h1/h2).
    return p.items


def seccionar(items, desde, hasta):
    """Devuelve los items entre el encabezado `desde` (incluido) y `hasta` (excluido)."""
    nd = normalizar(desde)
    nh = normalizar(hasta) if hasta else None
    dentro = False
    out = []
    for it in items:
        if it["tipo"] == "bloque" and it["clase"] == "encabezado":
            n = normalizar(it["texto"])
            if not dentro and (n == nd or n.startswith(nd)):
                dentro = True
            elif dentro and nh and (n == nh or n.startswith(nh)):
                break
        if dentro:
            out.append(it)
    if not out:
        aviso(f"No se encontró la sección '{desde}' en la fuente")
    return out


# ---------------------------------------------------------------- notas del vault

def listar_notas():
    notas = {}
    for base, dirs, files in os.walk(RAIZ):
        rel = os.path.relpath(base, RAIZ)
        if rel.startswith(("_raw", ".git", ".obsidian", ".venv")):
            dirs[:] = []
            continue
        for f in files:
            if f.endswith(".md"):
                ruta = os.path.join(base, f)
                with open(ruta, encoding="utf-8") as fh:
                    notas[ruta] = fh.read()
    return notas


def es_nota_del_ramo(ruta):
    return ruta.startswith(VAULT_RAMO + os.sep)


RE_WIKILINK = re.compile(r"(!?)\[\[([^\]|#]*)(#[^\]|]*)?(\|[^\]]*)?\]\]")
RE_MDLINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")


def quitar_codigo(texto):
    """Elimina bloques ``` y código inline para no analizar links dentro de código."""
    texto = re.sub(r"```.*?```", "", texto, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", texto)


# ---------------------------------------------------------------- pruebas

def prueba_autocontencion(notas):
    print("\n[1] Autocontención y links locales")
    prohibidos = [
        (r"_raw", "referencia a _raw"),
        (r"/Users/|file://|[A-Za-z]:\\\\", "ruta absoluta"),
        (r"notion\.so|notion\.site|app\.notion\.com|notion-static", "URL de Notion"),
    ]
    n_err = len(errores)
    for ruta, texto in notas.items():
        if not es_nota_del_ramo(ruta):
            continue
        rel = os.path.relpath(ruta, RAIZ)
        for patron, desc in prohibidos:
            if re.search(patron, texto):
                error(f"{rel}: contiene {desc}")
        for m in RE_MDLINK.finditer(quitar_codigo(texto)):
            destino = m.group(3)
            if re.match(r"^[a-z]+://|^mailto:|^#", destino):
                continue
            if destino.startswith("/"):
                error(f"{rel}: link con ruta absoluta '{destino}'")
                continue
            objetivo = os.path.normpath(os.path.join(os.path.dirname(ruta), unquote(destino.split("#")[0])))
            if not objetivo.startswith(RAIZ):
                error(f"{rel}: link fuera del vault '{destino}'")
            elif not os.path.exists(objetivo):
                error(f"{rel}: archivo enlazado no existe '{unquote(destino)}'")
    if len(errores) == n_err:
        ok("Sin referencias a _raw, rutas absolutas ni Notion; todos los links locales existen")


def prueba_grafo(notas):
    print("\n[5] Wikilinks, nombres únicos y notas huérfanas")
    n_err = len(errores)
    por_nombre = {}
    for ruta in notas:
        if es_nota_del_ramo(ruta):
            por_nombre.setdefault(os.path.splitext(os.path.basename(ruta))[0], []).append(ruta)
    for nombre, rutas in por_nombre.items():
        if len(rutas) > 1 and nombre != "_Índice":
            error(f"Nombre de nota repetido '{nombre}': {[os.path.relpath(r, RAIZ) for r in rutas]}")
    adjuntos = set()
    for base, _, files in os.walk(VAULT_RAMO):
        adjuntos.update(files)

    def resolver(objetivo, desde):
        objetivo = objetivo.strip().rstrip("\\")  # [[Nota\|alias]] dentro de tablas
        if not objetivo:
            return desde  # link a encabezado de la misma nota
        nombre = os.path.basename(objetivo)
        if nombre.endswith(".md"):
            nombre = nombre[:-3]
        if "/" in objetivo:
            cand = [r for r in notas if r.endswith(objetivo if objetivo.endswith(".md") else objetivo + ".md")]
            if cand:
                return cand[0]
        if nombre in por_nombre:
            if nombre == "_Índice" and "/" not in objetivo:
                return None  # ambiguo: debe usarse ruta
            return por_nombre[nombre][0]
        if nombre in adjuntos:
            return "adjunto"
        return None

    entrantes = {r: 0 for r in notas if es_nota_del_ramo(r)}
    n_links = 0
    for ruta, texto in notas.items():
        if not es_nota_del_ramo(ruta):
            continue
        for m in RE_WIKILINK.finditer(quitar_codigo(texto)):
            n_links += 1
            objetivo = m.group(2)
            destino = resolver(objetivo, ruta)
            if destino is None:
                error(f"{os.path.relpath(ruta, RAIZ)}: wikilink roto [[{objetivo}]]")
            elif destino in entrantes and destino != ruta:
                entrantes[destino] += 1
    for ruta, n in entrantes.items():
        if n == 0 and os.path.basename(ruta) != "_Índice.md":
            error(f"Nota huérfana (sin links entrantes): {os.path.relpath(ruta, RAIZ)}")
    if len(errores) == n_err:
        ok(f"{n_links} wikilinks válidos; {len(entrantes)} notas, ninguna huérfana ni repetida")


def prueba_formato(notas):
    print("\n[+] Formato (advertencias)")
    n_av = len(avisos)
    prohibidos = re.compile(r"clase\s*\d|semana|resumen|\b[ic]\d+\b", re.I)
    for ruta, texto in notas.items():
        if not es_nota_del_ramo(ruta):
            continue
        rel = os.path.relpath(ruta, RAIZ)
        partes = os.path.relpath(ruta, VAULT_RAMO).split(os.sep)
        for p in partes:
            if prohibidos.search(os.path.splitext(p)[0]):
                aviso(f"{rel}: nombre con numeración de clase o 'resumen'")
        lineas = texto.count("\n") + 1
        if lineas > MAX_LINEAS:
            aviso(f"{rel}: {lineas} líneas (> {MAX_LINEAS}); considerar dividir")
        if os.path.basename(ruta) == "_Índice.md":
            continue
        fm = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
        if not fm:
            aviso(f"{rel}: sin frontmatter")
        else:
            for clave in ("ramo", "tema", "tags", "prerrequisitos"):
                if not re.search(rf"^{clave}:", fm.group(1), re.M):
                    aviso(f"{rel}: frontmatter sin '{clave}'")
        if "## Preguntas de repaso" not in texto:
            aviso(f"{rel}: sin sección '## Preguntas de repaso'")
        else:
            n = texto.split("## Preguntas de repaso", 1)[1].count("[!question]-")
            if not 3 <= n <= 5:
                aviso(f"{rel}: {n} preguntas de repaso (se esperan 3 a 5)")
    for base, dirs, files in os.walk(VAULT_RAMO):
        dirs[:] = [d for d in dirs if d != "adjuntos"]
        if os.path.basename(base) == "adjuntos":
            continue
        if "_Índice.md" not in files:
            aviso(f"Carpeta sin _Índice.md: {os.path.relpath(base, RAIZ)}")
    if len(avisos) == n_av:
        ok("Frontmatter, preguntas de repaso, largo, nombres e índices en orden")


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 16), b""):
            h.update(bloque)
    return h.hexdigest()


def referenciados(notas):
    refs = set()
    for ruta, texto in notas.items():
        for m in RE_MDLINK.finditer(quitar_codigo(texto)):
            destino = m.group(3)
            if not re.match(r"^[a-z]+://", destino):
                refs.add(os.path.normpath(os.path.join(os.path.dirname(ruta), unquote(destino.split("#")[0]))))
    return refs


def prueba_imagenes(tema, conf, items, imagenes, notas):
    print(f"\n[2] Imágenes — {tema}")
    n_err = len(errores)
    refs = referenciados(notas)
    originales = []
    for fuente, its in items:
        base = os.path.dirname(os.path.join(RAW, conf_fuentes[fuente]))
        for it in its:
            if it["tipo"] == "imagen" and not it["src"].startswith("http"):
                originales.append(os.path.normpath(os.path.join(base, it["src"])))
    originales = list(dict.fromkeys(originales))
    del_tema = [e for e in imagenes if e["tema"] == tema]
    por_original = {os.path.normpath(os.path.join(RAW, e["original"])): e for e in del_tema if e["tipo"] == "apuntes"}
    copiadas = referidas = 0
    for o in originales:
        e = por_original.get(o)
        if not e:
            error(f"Imagen original sin destino: {os.path.relpath(o, RAW)}")
            continue
        destino = os.path.join(RAIZ, e["destino"])
        if not os.path.exists(destino):
            error(f"Falta la copia: {e['destino']}")
            continue
        if sha256(destino) != sha256(o):
            error(f"La copia no coincide con el original (sha256): {e['destino']}")
            continue
        copiadas += 1
        if os.path.normpath(destino) in refs:
            referidas += 1
        else:
            error(f"Imagen copiada pero no referenciada: {e['destino']}")
    extra = [e for e in del_tema if e["tipo"] != "apuntes"]
    extra_ok = 0
    for e in extra:
        destino = os.path.join(RAIZ, e["destino"])
        if not os.path.exists(destino):
            error(f"Falta el adjunto de complemento: {e['destino']}")
        elif os.path.normpath(destino) not in refs:
            error(f"Adjunto de complemento no referenciado: {e['destino']}")
        else:
            extra_ok += 1
    # adjuntos en disco que nadie usa
    carpeta = os.path.join(RAIZ, conf["carpeta"], "adjuntos")
    if os.path.isdir(carpeta):
        for f in os.listdir(carpeta):
            if f.startswith("."):
                continue
            if os.path.normpath(os.path.join(carpeta, f)) not in refs:
                error(f"Adjunto sin referencias: {os.path.relpath(os.path.join(carpeta, f), RAIZ)}")
    print(f"     originales asignadas al tema: {len(originales)} | copiadas (sha256 ok): {copiadas} "
          f"| referenciadas: {referidas} | adjuntos de complemento referenciados: {extra_ok}/{len(extra)}")
    if len(errores) == n_err:
        ok("Todas las imágenes del tema están copiadas y referenciadas")


_vocab_cache = {}


def ventana_mejor(tokens_bloque, tokens_nota):
    """Mejor ventana de la nota por solapamiento de tokens; devuelve (fraccion, texto).
    Un token ausente se empareja con el más parecido de la nota (erratas corregidas,
    p. ej. 'improvistos' -> 'imprevistos')."""
    n = len(tokens_bloque)
    if n == 0 or not tokens_nota:
        return 0.0, ""
    clave = id(tokens_nota)
    if clave not in _vocab_cache:
        _vocab_cache[clave] = set(tokens_nota)
    vocab_nota = _vocab_cache[clave]
    tokens_bloque = [
        t if t in vocab_nota or len(t) < 5
        else (difflib.get_close_matches(t, vocab_nota, n=1, cutoff=0.8) or [t])[0]
        for t in tokens_bloque
    ]
    largo = n + max(3, n // 2)
    objetivo = {}
    for t in tokens_bloque:
        objetivo[t] = objetivo.get(t, 0) + 1
    mejor, mejor_span = 0.0, ""
    vocab = set(objetivo)
    for i, t in enumerate(tokens_nota):
        if t not in vocab:
            continue
        ventana = tokens_nota[i:i + largo]
        cuenta = {}
        ultimo = 0
        for j, w in enumerate(ventana):
            if w in objetivo and cuenta.get(w, 0) < objetivo[w]:
                cuenta[w] = cuenta.get(w, 0) + 1
                ultimo = j
        hit = sum(cuenta.values()) / n
        # la ventana se recorta al último token coincidente y, a igual cantidad de
        # coincidencias, se prefiere el tramo más corto, para que la similitud de
        # secuencia no se diluya con palabras ajenas
        if hit > mejor or (hit == mejor and ultimo + 1 < len(mejor_span.split())):
            mejor, mejor_span = hit, " ".join(ventana[:ultimo + 1])
    return mejor, mejor_span


def umbral_tokens(n):
    """Fracción mínima de tokens: en bloques cortos se tolera una palabra distinta."""
    if n < 4:
        return 1.0
    return min(UMBRAL_TOKENS, (n - 1) / n)


def prueba_cobertura(tema, items, notas_tema, notas_todas, aceptados, detalle):
    print(f"\n[3] Cobertura de contenido — {tema}")
    n_err = len(errores)
    aceptados = [a for a in aceptados if normalizar(a.get("texto", ""))]
    corp = {r: normalizar(t) for r, t in notas_todas.items()}
    toks = {r: c.split() for r, c in corp.items()}
    codigo = {r: normalizar_codigo(quitar_marcas_callout(t)) for r, t in notas_todas.items()}
    orden = list(notas_tema) + [r for r in notas_todas if r not in notas_tema]
    stats = {"exacto": 0, "reformulado": 0, "aceptado": 0, "no": 0}
    for fuente, its in items:
        for it in its:
            if it["tipo"] != "bloque":
                continue
            texto = it["texto"]
            if it["clase"] == "codigo":
                lineas = [normalizar_codigo(l) for l in texto.splitlines() if l.strip()]
                faltan = [l for l, n in zip([l for l in texto.splitlines() if l.strip()], lineas)
                          if not any(n in codigo[r] for r in orden)]
                if not faltan:
                    stats["exacto"] += 1
                    continue
                if any(normalizar(texto).find(normalizar(a["texto"])) >= 0 for a in aceptados if a["fuente"] == fuente):
                    stats["aceptado"] += 1
                    continue
                stats["no"] += 1
                error(f"[{fuente}] código no cubierto ({len(faltan)}/{len(lineas)} líneas faltan): "
                      f"{faltan[0].strip()[:90]!r}")
                continue
            if it["clase"] == "encabezado":
                # "A) Cascada", "1. Modelo Espiral:", "→ Modelo Agile": el enumerador es estructura
                texto = re.sub(r"^\s*(→\s*)?(([A-Za-z]|\d+(\.\d+)*)[\.\)]\s+)?", "", texto)
            n = normalizar(texto)
            if not n:
                continue
            donde = next((r for r in orden if n in corp[r]), None)
            if donde:
                stats["exacto"] += 1
                if detalle:
                    print(f"     = {texto[:70]!r} → {os.path.basename(donde)}")
                continue
            if any(normalizar(a["texto"]) in n or n in normalizar(a["texto"]) for a in aceptados if a["fuente"] == fuente):
                stats["aceptado"] += 1
                continue
            tb = n.split()
            mejor = (0.0, 0.0, None)
            for r in orden:
                frac, vent = ventana_mejor(tb, toks[r])
                if frac >= umbral_tokens(len(tb)):
                    sim = difflib.SequenceMatcher(None, n, vent).ratio()
                    if (frac, sim) > mejor[:2]:
                        mejor = (frac, sim, r)
                elif frac > mejor[0]:
                    mejor = (frac, 0.0, r)
            if mejor[0] >= umbral_tokens(len(tb)) and mejor[1] >= UMBRAL_SECUENCIA:
                stats["reformulado"] += 1
                if detalle:
                    print(f"     ≈ {texto[:70]!r} → {os.path.basename(mejor[2])} "
                          f"(tokens {mejor[0]:.0%}, similitud {mejor[1]:.0%})")
                continue
            stats["no"] += 1
            pista = f" (mejor candidato: {os.path.basename(mejor[2])}, tokens {mejor[0]:.0%})" if mejor[2] else ""
            error(f"[{fuente}] {it['clase']} no cubierto: {texto[:110]!r}{pista}")
    total = sum(stats.values())
    print(f"     bloques: {total} | exactos: {stats['exacto']} | reformulados: {stats['reformulado']} "
          f"| aceptados sin destino: {stats['aceptado']} | NO cubiertos: {stats['no']}")
    if len(errores) == n_err:
        ok("Todo el contenido original del tema aparece en las notas")


def prueba_links_externos(tema, items, notas_todas, aceptados):
    print(f"\n[4] Links externos — {tema}")
    n_err = len(errores)
    texto = "\n".join(notas_todas.values())
    total = 0
    for fuente, its in items:
        for it in its:
            if it["tipo"] != "link" or not it["href"].startswith("http"):
                continue
            href = it["href"]
            if any(a.get("link") == href for a in aceptados):
                continue
            total += 1
            if href not in texto and unquote(href) not in texto:
                error(f"[{fuente}] link externo perdido: {href}")
    if len(errores) == n_err:
        ok(f"{total} links externos conservados")


# ---------------------------------------------------------------- main

def main():
    global conf_fuentes
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tema", help="verificar solo este tema")
    ap.add_argument("--detalle", action="store_true", help="listar también bloques cubiertos")
    args = ap.parse_args()

    with open(os.path.join(META, "mapeo.json"), encoding="utf-8") as f:
        mapeo = json.load(f)
    with open(os.path.join(META, "imagenes.json"), encoding="utf-8") as f:
        imagenes = json.load(f)
    conf_fuentes = mapeo["fuentes"]
    aceptados = mapeo.get("aceptados", [])
    notas = listar_notas()

    if args.tema:
        if args.tema not in mapeo["temas"]:
            sys.exit(f"Tema desconocido: {args.tema}. Opciones: {', '.join(mapeo['temas'])}")
        temas = [args.tema]
    else:
        temas = [t for t, c in mapeo["temas"].items() if c.get("estado") == "hecho"]

    print(f"Vault: {RAIZ}")
    print(f"Temas a verificar: {', '.join(temas) or '(ninguno marcado como hecho)'}")
    prueba_autocontencion(notas)

    hay_raw = os.path.isdir(RAW)
    if not hay_raw:
        aviso("No existe _raw/: se omiten las pruebas 2, 3 y 4 (dependen del export original)")
    cache = {}
    asignados = {}
    for tema in temas:
        conf = mapeo["temas"][tema]
        carpeta = os.path.join(RAIZ, conf["carpeta"])
        notas_tema = {r: t for r, t in notas.items() if r.startswith(carpeta + os.sep)}
        print(f"\n=== Tema: {tema} ({len(notas_tema)} notas) ===")
        if not notas_tema:
            error(f"El tema no tiene notas en {conf['carpeta']}")
        if not hay_raw:
            continue
        items = []
        for sec in conf["secciones"]:
            fuente = sec["fuente"]
            if fuente not in cache:
                cache[fuente] = extraer(os.path.join(RAW, conf_fuentes[fuente]))
            its = seccionar(cache[fuente], sec["desde"], sec.get("hasta"))
            items.append((fuente, its))
            asignados.setdefault(fuente, set()).update(id(i) for i in its)
        prueba_imagenes(tema, conf, items, imagenes, notas)
        prueba_cobertura(tema, items, notas_tema, notas, aceptados, args.detalle)
        prueba_links_externos(tema, items, notas, aceptados)

    prueba_grafo(notas)
    prueba_formato(notas)

    if hay_raw and not args.tema:
        print("\n[i] Estado global de las fuentes")
        for fuente, ruta in conf_fuentes.items():
            if fuente not in cache:
                cache[fuente] = extraer(os.path.join(RAW, ruta))
            bloques = [i for i in cache[fuente] if i["tipo"] == "bloque"]
            hechos = len([i for i in bloques if id(i) in asignados.get(fuente, set())])
            links = [i for i in cache[fuente] if i["tipo"] == "link"]
            if bloques:
                estado = f"{hechos}/{len(bloques)} bloques en temas hechos"
            elif links:
                estado = f"sin bloques de texto (solo {len(links)} enlaces; ver Material del curso)"
            else:
                estado = "vacía (sin destino)"
            print(f"     {fuente}: {estado}")

    print("\n" + "=" * 60)
    print(f"Resultado: {len(errores)} errores, {len(avisos)} advertencias")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
