# Nivel de detalle y flujo de trabajo — Programación Avanzada

Referencia para retomar la migración en cualquier iteración. El tema 1 (Repaso y POO básica) fue aprobado por el usuario como **el nivel correcto**: imitar sus notas.

## Criterio de contenido
- **Orden:** el de los notebooks `.ipynb` (`Clases/Contenidos/semana-NN-*/`, por número de notebook, `bonus-*` al final de su tema). Los PDF de `Clases/2023/` y el libro solo aportan contenido extra (ejemplos, analogías, ejercicios); no cambian el orden.
- **Público:** estudiante del ramo, no experto. Poco tecnicismo: cada término nuevo en **negrita** con su explicación y el término inglés en *cursiva* si es el que se usa. Primero el problema que resuelve el concepto y su porqué, luego el mecanismo.
- **Cobertura:** cada celda de texto y de código del notebook debe quedar reflejada, reescrita (no copiada), incluidos los bonus.
- **Código:** corto, en Python 3, con su **salida esperada** en un bloque aparte. Se ejecuta con `python3` antes de commitear y la salida escrita es la real.
- **Recursos:** tablas para comparar, un Mermaid solo si aclara, analogías cotidianas, y una `[!warning]` con la trampa típica de principiante cuando exista.
- **Imágenes:** las de los notebooks se copian con nombre descriptivo (`addimg.py`), con transcripción en `[!example]-` y registro en `imagenes.json` (`tipo: "notebook"`; `"slide"` para PDF).

## Formato de cada nota (ver ESTANDAR-NOTAS.md)
- Frontmatter: `ramo`, `tema`, `tags` (`programacion/<tema>`, `origen/complemento`) y `prerrequisitos` (wikilinks sin alias).
- Estructura: `# Título`, entrada de 2-4 líneas, secciones `##`, `> [!tip]` con la regla clave, `## Preguntas de repaso` con **3 a 5** preguntas `> [!question]-` que piden explicar un porqué.
- **60–120 líneas por nota, máximo 150** (el verificador avisa). Si un notebook es largo, se divide en 2–3 notas con un título que diga qué cubre cada una. El tema 1 pasó de 4 notebooks a 10 notas.
- Nada de marcas de procedencia: «clase N», «semana», nombres de PDF, `_raw`.
- **Sin comas** en nombres de carpetas ni de notas. Nombres únicos en todo el vault.
- Cada tema lleva `_Índice.md` (descripción, volver al mapa, callout `[!note] Origen`, `## Orden de estudio`) y una fila nueva en `Programación Avanzada/_Índice.md`.

## Enlaces a otros ramos
Se escribe la nota completa en versión Python y se enlaza a la equivalente de otro ramo como lectura relacionada, sin copiar. *Introducción a la Programación* no está en `main`: no enlazar a ella hasta que se integre.

## Flujo por tema (un commit por tema)
1. Volcar el notebook a texto (celdas `[markdown]` / `[code]`) y leerlo completo; ver las slides del PDF relacionado con `pdftotext`.
2. Escribir las notas y el `_Índice.md` del tema; copiar imágenes.
3. Probar los bloques de código (los que dependen de otros bloques o de archivos previos, o que muestran un error a propósito, fallan solos y es esperable).
4. `mapeo.json` → `"estado": "hecho"`; fila del tema y entrada del Registro en `PROGRESS.md`; `DUDAS.md` si hay discrepancias reales.
5. `python3 _meta/verificar.py --ramo "Programación Avanzada" --tema "<Tema>"`: 0 errores y 0 advertencias, revisando el código de salida.
6. Commit `migra tema <Tema>` con la línea `Co-Authored-By` (los comandos `git` requieren ejecutarse fuera del sandbox).
7. Pausas de revisión con el usuario: después del tema 7 (Threading) y al cierre.

