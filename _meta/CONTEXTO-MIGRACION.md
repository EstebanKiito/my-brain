# Contexto para continuar la migración: Sistemas Operativos (IIC2333)

Eres un asistente que trabaja en el repo `my-brain`, un vault de Obsidian con los apuntes de la carrera (Licenciatura en Ciencia de la Computación UC). Los apuntes vienen de un export de Notion que está en `_raw/` (≈1.1 GB, en `.gitignore`, nunca se commitea). Ya hay dos ramos migrados con este flujo: **Ingeniería de Software (IIC2143)** y **Bases de Datos (IIC2413)**. El siguiente es **Sistemas Operativos (IIC2333)**. Tienes que seguir exactamente el mismo flujo y formato. Si tienes dudas, el modelo a imitar es `Bases de Datos/` junto con `_meta/Bases de Datos/`.

Objetivo del usuario: estudiar cualquier concepto abriendo **una sola nota**, sin saber en qué clase se vio. El repo tiene que funcionar sin `_raw/`.

---

## 1. Flujo de trabajo

### Estado actual
- La migración de SO **todavía no empieza**. No existen la rama, `Sistemas Operativos/` ni `_meta/Sistemas Operativos/`.
- Fuentes en `_raw/Semestre 4/Sistemas Operativos & Redes - IIC2333/`:
  - `Apuntes - SSOO IIC2333 …html` (+ carpeta con imágenes): fuente principal.
  - `RESUMEN MIDTERM SSOO …html` (+ carpeta).
  - `Ayudantías - SSOO IIC2333 …html` (+ carpeta).
  - `CLASES …html`, `Libros …html`, `Interrogaciones …html`, `Tareas …html`: fuentes de complementos o de material del curso.
  - `Apuntes - Redes IIC2333 …html`: el ramo es "SO & Redes". **Antes de empezar, pregúntale al usuario** si Redes va en el mismo ramo o en uno aparte, y qué nombre lleva la carpeta del vault (`carpeta_ramo`).

### Paso 0: infraestructura (un commit)
1. Crear la rama desde `main` actualizado: `git checkout -b migrar/sistemas-operativos`.
2. Crear `_meta/Sistemas Operativos/` con los mismos 4 archivos que `_meta/Bases de Datos/`:
   - `mapeo.json`: tiene `_descripcion`, `carpeta_ramo` y `fuentes` (alias → ruta relativa a `_raw/`). En `temas`, cada tema lleva `carpeta`, `estado` y `secciones`; cada sección indica `fuente`, `desde` (encabezado incluido) y `hasta` (encabezado excluido), y admite `por_texto` y `adjuntos`. En `aceptados` van los bloques que se omiten a propósito, cada uno con su `motivo`.
   - `imagenes.json`: lista de `{tema, tipo, original, destino, sha256}`. Para las slides, `tipo: "slide"` y `original: "…pdf#page=N"`.
   - `PROGRESS.md`: tabla `# | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides)`, una sección de Convenciones y un Registro fechado por tema (fuentes usadas, notas de complemento puro, decisiones tomadas).
   - `DUDAS.md`: una tabla por tema `Estado | Nota | Original | Duda / corrección propuesta`, con estados 🟡 abierta, ✅ resuelta e ℹ️ informativa.
3. Proponer al usuario el temario (la lista de temas y su orden) **antes** de migrar.

### Ciclo por tema (un commit por tema)
1. Leer las secciones del HTML que le corresponden al tema y registrarlas en `mapeo.json`.
2. Escribir las notas atómicas en `Sistemas Operativos/<Tema>/` (ver la sección 2), con su `_Índice.md`.
3. Copiar las imágenes a `<Tema>/adjuntos/`, registrar el sha256 en `imagenes.json` y transcribirlas.
4. Agregar los complementos (clases, libro) y marcar los errores del original (en la nota y en `DUDAS.md`).
5. Marcar el tema como `"estado": "hecho"` en `mapeo.json` y actualizar `PROGRESS.md`.
6. Verificar **todos los ramos**, porque el grafo es del vault completo:
   ```bash
   python3 _meta/verificar.py --ramo "Sistemas Operativos"
   python3 _meta/verificar.py --ramo "Bases de Datos"
   python3 _meta/verificar.py --ramo "Ingeniería de Software"
   ```
   Hace falta **0 errores** y, en lo posible, 0 advertencias. Revisa el **código de salida**: nunca encadenes `verificar … | tail && git commit`, porque el pipe siempre sale con 0.
7. Hacer el commit (ver la sección 3).

### Cierre del ramo
- El último tema es "Gestión del curso" (evaluaciones, tareas, interrogaciones) junto con el mapa final `Sistemas Operativos/_Índice.md`.
- Hay que cubrir el 100% de las fuentes: cada bloque está en una nota o en `aceptados`.
- **No hacer push ni abrir PR** sin que el usuario lo pida. Los ramos anteriores se integraron a `main` con un PR desde la rama `migrar/*`.

### Reglas del entorno
- `verificar.py` usa solo la biblioteca estándar; no existe `.venv`.
- `.obsidian/` es configuración del usuario y no se commitea.
- Las slides se convierten a PNG con `pdftoppm -r 110`.

---

## 2. Formato de los contenidos migrados

### Estructura
```
Sistemas Operativos/
  _Índice.md                 ← mapa del ramo (no se numera)
  <Tema>/
    _Índice.md               ← índice del tema (no se numera)
    01 - <Concepto>.md
    02 - <Concepto>.md
    adjuntos/<nombre descriptivo>.png
```
- **Un concepto por nota**, de 150 líneas como máximo (si pasa, se divide).
- Nombres con prefijo `NN - ` según el **orden de estudio** dentro de la carpeta. Los nombres **no** pueden contener "clase N", "semana", "resumen", "i1" ni "c2". Los nombres de nota son únicos en todo el vault.

### Plantilla de nota
```markdown
---
ramo: Sistemas Operativos
tema: <Tema>
tags: [so/<tema-kebab>, origen/apuntes]          # origen/complemento si la nota es 100% nueva
prerrequisitos: ["[[01 - Procesos|Procesos]]"]   # [] si no hay
---
# <Concepto>

<Resumen de 1–2 líneas.>

## <Sección> (mis apuntes)
<Texto original CONSERVADO TAL CUAL: no se corrige ni se reescribe.>

> [!warning] Posible error (registrado en `_meta/Sistemas Operativos/DUDAS.md`)
> <Precisión o corrección.>

> [!tip] Complemento (slides "<nombre de la clase>")
> <Contenido nuevo; todo complemento va SIEMPRE dentro de un callout ([!tip] Complemento o [!example]).>

## Preguntas de repaso

1. <Pregunta>
> [!question]- Respuesta
> <Respuesta>
```
- De **3 a 5 preguntas de repaso**, cada una con la respuesta en un callout plegable `[!question]-`.
- Los pendientes del original ("seguir escribiendo…") van en un callout `[!info]`.

### Links
- Los wikilinks llevan alias sin número: `[[02 - Hilos|Hilos]]`. Dentro de una tabla se escribe `[[02 - Hilos\|Hilos]]`.
- Los índices enlazan con la ruta completa: `[[Sistemas Operativos/Procesos/_Índice|Procesos]]`.
- No puede haber notas huérfanas, links rotos, `_raw`, rutas absolutas ni URLs de Notion.
- Los links externos de los apuntes se conservan.
- Si un concepto ya existe en otro ramo, se enlaza en vez de duplicarlo. Por ejemplo, el teorema CAP de IngSoft o la memoria y los punteros de BD.

### Imágenes
- Se copian a `<Tema>/adjuntos/` con un nombre descriptivo (no "Untitled 3"). El link es Markdown relativo con `%20`: `![Descripción](adjuntos/Planificador%20round%20robin.png)`.
- Cada imagen lleva su transcripción en un callout plegable.
- Las slides de las clases **solo entran como PNG**, porque no tienen licencia: los PDF y PPTX completos no se suben. Van dentro de un callout que cita la clase y se registran como `tipo: "slide"`.
- Los datos personales (teléfonos, nombres de compañeros) se omiten y se registran en `aceptados`.

### Índices
- `_Índice.md` de cada tema: `# <Tema> — índice`, una descripción, `Volver al [[Sistemas Operativos/_Índice|mapa del ramo]].`, un callout `> [!note] Origen` (qué parte viene de los apuntes y cuál es complemento) y `## Orden de estudio` como lista numerada `[[NN - X|X]]: qué cubre`.
- `_Índice.md` del ramo: `# Sistemas Operativos (IIC2333) — mapa del curso`, una sección "Cómo están hechas las notas" (ver `Bases de Datos/_Índice.md`) y la tabla `Tema | Qué cubre`.

---

## 3. Ramas y commits

- **Rama:** `migrar/<ramo-en-kebab-case-sin-tildes>`. Para este ramo: `migrar/sistemas-operativos`. Los ejemplos existentes son `migrar/software-v2` y `migrar/bases-de-datos`. Se crea desde `main`.
- **Commits** en español, en minúscula, en imperativo de tercera persona y sin punto final:
  - Paso 0: una descripción corta del cambio de infraestructura (ej.: `verificar.py multi-ramo`, `infraestructura de Sistemas Operativos`).
  - Por tema: `migra tema <Tema>`, con el nombre exacto de la carpeta (ej.: `migra tema Planificación de procesos`).
  - Último: `migra tema Gestión del curso y mapa final del ramo`.
  - Ajustes posteriores: un verbo y su objeto (ej.: `numera las notas de Procesos de desarrollo por orden de estudio`).
- Todo commit termina con esta línea (después de una línea en blanco):
  ```
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  ```
- Un tema = un commit. No se mezclan temas y nunca se commitea con el verificador en rojo.
- Integración: un PR de la rama a `main` (`Merge pull request #N from EstebanKiito/migrar/<ramo>`), solo cuando el usuario lo pida.
