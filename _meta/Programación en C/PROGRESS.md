# Progreso de la migración — Programación en C (material de IIC2133)

Rama: `migrar/estructuras-de-datos` (compartida por Estructuras de Datos y Programación en C). Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Programación en C" --tema "<Tema>"` revisando el código de salida; al cerrar cada bloque de temas, la verificación completa de todos los ramos (el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Programación en C/`, cobertura reescrita en `verificar.py`) | `_meta/` | ✅ hecho | – | – |
| 1 | Fundamentos del lenguaje | `01-Fundamentos del lenguaje/` | ✅ hecho | 4 + índice | 4 + 0 |
| 2 | Punteros, arreglos y strings | `02-Punteros, arreglos y strings/` | ✅ hecho | 4 + índice | 13 + 0 |
| 3 | Memoria dinámica y Valgrind | `03-Memoria dinámica y Valgrind/` | ✅ hecho | 5 + índice | 21 + 0 |
| 4 | Structs | `04-Structs/` | ✅ hecho | 4 + índice | 4 + 0 |
| 5 | Módulos, compilación y depuración | `05-Módulos, compilación y depuración/` | pendiente | – | – |

## Convenciones
- Notas escritas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md): prosa reescrita, sin marcas de procedencia ni citas literales, de 60 a 120 líneas (máximo 150) y de 3 a 5 preguntas de repaso plegables.
- Prefijo `NN - ` con orden de estudio por carpeta, wikilinks con alias (`\|` dentro de tablas) e índices enlazados con ruta completa.
- `mapeo.json` lleva `"cobertura": "reescrita"`: la prueba [3] del verificador da advertencias y no errores, porque ya no se copia literal. Las pruebas [1], [2], [4] y [5] siguen siendo errores.
- **Slides:** ningún PDF entra al repo. Las útiles se convierten a PNG (`pdftoppm -r 110`), van en `adjuntos/` dentro de un callout que cita la clase y se registran con `tipo: "slide"` y `original: …pdf#page=N`.
- **Rostros:** las capturas de las cápsulas con la cámara del expositor se copian con esa esquina tapada con el color de fondo (`magick … -draw rectangle`) y se registran con `tipo: "editada"` y su `motivo`.
- **Imágenes HEIC:** se convierten a PNG con `sips` y se registran con `tipo: "convertida"`.
- **Fuentes:** Cápsulas de C (apuntes propios), las 11 páginas del CheatSheet C y el Taller introductorio (material del curso), más las guías `.md` de setup y depuración como complemento.
- **Código:** todo snippet C compila con `gcc -Wall -Wextra` en macOS y se ejecuta antes del commit.
- Las notas de `Estructuras de Datos/` enlazan a estas como prerrequisito.

## Registro

- **2026-10-16 · Fundamentos del lenguaje.** Fuentes: `capsulas` (0 a 3, con 4 diagramas del stack), `cheat00` a `cheat03` y `taller` (consejos iniciales). 4 notas; 5 programas C compilados con `gcc -Wall -Wextra` sin advertencias y ejecutados. Se conservaron los 2 videos Loom del cheatsheet (switch, funciones). Las 4 imágenes del stack tienen la cámara tapada (`editada`). Para no dejar wikilinks rotos entre commits, las notas solo enlazan hacia atrás. 2 dudas ℹ️ (`bool` en C99, `atof` en `int`).
- **Cambios a `verificar.py`** durante este tema: el tipo de imagen `editada`; las imágenes enlazadas que no vienen en el export (5 del cheatsheet) son advertencia y no error; en ramos reescritos, la búsqueda difusa de cobertura mira solo las notas del ramo (pasó de más de 10 minutos a 3 segundos).
- **2026-10-16 · Punteros, arreglos y strings.** Fuentes: `capsulas` (4 a 6, 13 imágenes; 4 con la cámara tapada), `cheat04` a `cheat06` y `taller` (punteros y paso por valor). 4 notas; 4 programas C compilados y ejecutados (la única advertencia de `-Wextra` es la que la nota usa como ejemplo). 2 imágenes renombradas sin corchetes, porque `[ ]` rompe el link Markdown. 3 dudas ℹ️.
- **2026-10-16 · Memoria dinámica y Valgrind.** Fuentes: `capsulas` (7 y 8, 21 imágenes; 4 con la cámara tapada), `cheat07`, `cheat08`, `taller` (memoria, arreglos en el heap, matrices, tips de Valgrind) y la guía AYUDAA (síntomas, comando completo). 4 imágenes renombradas para describir bien cada paso de la matriz y sin corchetes. Programas compilados y ejecutados; `leaks --atExit` de macOS confirma 0 leaks en el ejemplo correcto y 10 en el que libera solo `B`. Valgrind y ASan no corren en este entorno, así que sus salidas vienen de las capturas del curso. Las 2 imágenes del CheatSheet no están en el export (advertencia). Se conservó el video de memoria. 3 dudas ℹ️.
- **2026-10-16 · Structs.** Fuentes: `capsulas` (9, 4 imágenes, todas con la cámara tapada), `cheat09` y `taller` (structs, cuenta por valor y por puntero, lista ligada). 4 notas; 4 programas C compilados y ejecutados (`leaks` confirma 0 leaks en el patrón init/destroy) y los 3 errores de compilación citados verificados (`expected expression`, `unknown type name`, `incomplete type`). La lista ligada del taller queda como puente hacia Estructuras de Datos. 2 dudas ℹ️.
