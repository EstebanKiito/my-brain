# Progreso de la migración — Estructuras de Datos (IIC2133)

Rama: `migrar/estructuras-de-datos` (compartida por Estructuras de Datos y Programación en C). Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Estructuras de Datos" --tema "<Tema>"` revisando el código de salida; al cerrar cada bloque de temas, la verificación completa de todos los ramos (el grafo es del vault completo).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Estructuras de Datos/`, cobertura reescrita en `verificar.py`) | `_meta/` | ✅ hecho | – | – |
| 1 | Análisis de algoritmos | `01-Análisis de algoritmos/` | ✅ hecho | 4 + índice | 6 + 0 |
| 2 | Estructuras lineales | `02-Estructuras lineales/` | ✅ hecho | 3 + índice | 2 + 3 |
| 3 | Ordenamiento elemental | `03-Ordenamiento elemental/` | ✅ hecho | 4 + índice | 14 + 0 |
| 4 | Mergesort | `04-Mergesort/` | pendiente | – | – |
| 5 | Quicksort | `05-Quicksort/` | pendiente | – | – |
| 6 | Heaps y colas de prioridad | `06-Heaps y colas de prioridad/` | pendiente | – | – |
| 7 | Ordenamiento lineal | `07-Ordenamiento lineal/` | pendiente | – | – |
| 8 | Árboles binarios de búsqueda | `08-Árboles binarios de búsqueda/` | pendiente | – | – |
| 9 | Árboles balanceados | `09-Árboles balanceados/` | pendiente | – | – |
| 10 | Árboles B+ | `10-Árboles B+/` | pendiente | – | – |
| 11 | Tablas de hash | `11-Tablas de hash/` | pendiente | – | – |
| 12 | Backtracking | `12-Backtracking/` | pendiente | – | – |
| 13 | Algoritmos codiciosos | `13-Algoritmos codiciosos/` | pendiente | – | – |
| 14 | Programación dinámica | `14-Programación dinámica/` | pendiente | – | – |
| 15 | Grafos y DFS | `15-Grafos y DFS/` | pendiente | – | – |
| 16 | Árboles de cobertura mínima | `16-Árboles de cobertura mínima/` | pendiente | – | – |
| 17 | Caminos más cortos | `17-Caminos más cortos/` | pendiente | – | – |
| 18 | Gestión del curso | `18-Gestión del curso/` | pendiente | – | – |

## Convenciones
- Notas escritas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md): prosa reescrita, sin marcas de procedencia ni citas literales, de 60 a 120 líneas (máximo 150) y de 3 a 5 preguntas de repaso plegables.
- Prefijo `NN - ` con orden de estudio por carpeta, wikilinks con alias (`\|` dentro de tablas) e índices enlazados con ruta completa.
- `mapeo.json` lleva `"cobertura": "reescrita"`: la prueba [3] del verificador da advertencias y no errores, porque ya no se copia literal. Las pruebas [1], [2], [4] y [5] siguen siendo errores.
- **Slides:** ningún PDF entra al repo. Las útiles se convierten a PNG (`pdftoppm -r 110`), van en `adjuntos/` dentro de un callout que cita la clase y se registran con `tipo: "slide"` y `original: …pdf#page=N`.
- **Imágenes HEIC:** se convierten a PNG con `sips` y se registran con `tipo: "convertida"`.
- **Código:** C solo donde la fuente ya trae C (listas ligadas, structs, malloc, heap de la ayudantía 3). Los algoritmos se explican con el pseudocódigo del curso más una implementación corta en Python. Todo snippet se ejecuta antes del commit (`python3`; `gcc -Wall -Wextra`).
- **Tutorial de C:** vive en `Programación en C/` (`_meta/Programación en C/`). Las notas de EDD lo enlazan como prerrequisito.
- **Tareas:** las soluciones personales (`TAREAS - RESPALDO`) no entran al vault; quedan en `aceptados`.
- **Duplicado:** las clases 10-13 de `Apuntes I2` son idénticas a las de `Apuntes` (salvo una tilde). Se mapean solo desde `apuntes`, así que el estado global de `i2` muestra esos bloques como no asignados.

## Registro

- **2026-10-16 · Análisis de algoritmos** (tema piloto, queda para revisión manual del usuario). Fuentes: `apuntes` clase 1 (desde "DEMOSTRACIÓN CON INDUCCION" hasta el nombre de selection sort) y clase 4 (dividir para conquistar y búsqueda binaria), `ayudantias` ayudantía 1 (inducción, notación asintótica, correctitud con bubble sort). Complementos: slides `class00` (algoritmo, pseudocódigo, reglas de cálculo, $T \in \Omega(M)$) y `class01` (principio de inducción, demostración de finitud). 4 notas de 83 a 101 líneas; 6 imágenes (2 GIF) con transcripción; 4 snippets Python verificados (`python3`). El resto de la clase 1 (motivación de ordenar, selection sort) queda para Ordenamiento elemental. Cobertura [3]: 81 bloques sin coincidencia textual, revisados a mano; todos los conceptos están reescritos en las notas. Sin dudas nuevas.
- **2026-10-16 · Estructuras lineales.** Fuentes: `apuntes` (inicio de la clase 6: colas FIFO, pilas LIFO, costos, 2 imágenes). Complementos: slides `class00` pp. 43, 45 y 47 (arreglo, lista en memoria, inserción) e interfaz de lista de las cápsulas de C. Lista ligada en C con `head`/`tail`/`count` (compila con `-Wall -Wextra` y `leaks` da 0); pila y cola circular en Python verificadas. Se enlaza a Programación en C y a la nota de arreglos y listas de Bases de Datos. Sin dudas nuevas.
- **2026-10-16 · Ordenamiento elemental.** Fuentes: `apuntes` (resto de la clase 1 y clase 2) y `ayudantias` (sorting de la ayudantía 1). 14 originales en 12 archivos: los GIF `SelectionSort 1` e `InsertionSort 1` son idénticos a los primeros y apuntan al mismo destino; las 2 fotos de pizarra se giraron 90° (`editada`). Python verificado: selection e insertion sort, conteo de inversiones, promedio $n(n-1)/4$ por fuerza bruta con $n = 6$ y el ejemplo de estabilidad. Erratas corregidas en el texto ("complejidad final de insertion sort O(n)" → $O(n^2)$). 1 duda ℹ️ (sumatoria de la slide). `edd_img.py` (scratchpad) ahora soporta `rotar90`. Los nombres de imagen no llevan paréntesis, porque cortan el link Markdown.
