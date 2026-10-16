# Estructuras de Datos (IIC2133) — mapa del curso

Vault de estudio del ramo. Cada nota cubre **un concepto atómico**: basta con buscar el concepto, sin saber en qué clase se vio. Dentro de cada carpeta, el número del archivo indica el orden de lectura.

## Cómo están hechas las notas
- **Frontmatter:** `ramo`, `tema`, `tags` y `prerrequisitos` (conceptos que conviene leer antes).
- **Cuerpo:** prosa explicativa que parte por el problema que resuelve cada concepto. Los algoritmos se presentan con el pseudocódigo del curso y una implementación corta en Python; las estructuras que se programaron en C (listas ligadas, heaps) llevan su código en C.
- **Lenguaje C:** la sintaxis y el manejo de memoria están en [[Programación en C/_Índice|Programación en C]].
- **Imágenes:** diagramas de los apuntes y slides en PNG, con su transcripción en un callout plegable.
- **Cierre:** cada nota termina con preguntas de repaso con la respuesta oculta en un callout plegable.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Estructuras de Datos/01-Análisis de algoritmos/_Índice\|Análisis de algoritmos]] | Inducción, correctitud, notación O/Ω/Θ, búsqueda binaria y dividir para conquistar |
| [[Estructuras de Datos/02-Estructuras lineales/_Índice\|Estructuras lineales]] | Arreglos frente a listas ligadas, lista ligada en C, pilas y colas |
| [[Estructuras de Datos/03-Ordenamiento elemental/_Índice\|Ordenamiento elemental]] | Selection sort, insertion sort, inversiones y propiedades de los algoritmos de ordenación |
| [[Estructuras de Datos/04-Mergesort/_Índice\|Mergesort]] | Merge, mergesort, resolución de la recurrencia y compromiso memoria-tiempo |
| [[Estructuras de Datos/05-Quicksort/_Índice\|Quicksort]] | Mediana y Partition, quicksort, partition in place y correctitud, análisis de casos y mejoras |
| [[Estructuras de Datos/06-Heaps y colas de prioridad/_Índice\|Heaps y colas de prioridad]] | Colas de prioridad, heap binario en arreglo, SiftUp y SiftDown, min heap en C, BuildHeap y heapsort |
| [[Estructuras de Datos/07-Ordenamiento lineal/_Índice\|Ordenamiento lineal]] | Cota $\Omega(n \log n)$ por comparación, counting sort y radix sort LSD y MSD |
| [[Estructuras de Datos/08-Árboles binarios de búsqueda/_Índice\|Árboles binarios de búsqueda]] | Diccionarios, propiedad de ABB, búsqueda, inserción, eliminación e in-order |
| [[Estructuras de Datos/09-Árboles balanceados/_Índice\|Árboles balanceados]] | AVL y rotaciones, árboles 2-3 con split, árboles rojo-negro y su equivalencia con 2-4 |
| [[Estructuras de Datos/10-Árboles B+/_Índice\|Árboles B+]] | Árboles de orden $d$ para disco, split, redistribución, unsplit y bulk loading |
| [[Estructuras de Datos/11-Tablas de hash/_Índice\|Tablas de hash]] | Función de hash, encadenamiento, sondeo y doble hashing, factor de carga y rehashing |
| [[Estructuras de Datos/12-Backtracking/_Índice\|Backtracking]] | CSP, plantilla isSolvable, laberintos y grafos implícitos, podas, propagación y heurísticas |
| [[Estructuras de Datos/13-Algoritmos codiciosos/_Índice\|Algoritmos codiciosos]] | Paradigma de subconjuntos, plantilla Greedy, mochila fraccional y contraejemplos |
| [[Estructuras de Datos/14-Programación dinámica/_Índice\|Programación dinámica]] | Subestructura óptima, memoización, versión iterativa, vuelto y comparación de técnicas |
| [[Estructuras de Datos/15-Grafos y DFS/_Índice\|Grafos y DFS]] | Representación de grafos, DFS, ciclos, tipos de aristas, orden topológico y Kosaraju |
| [[Estructuras de Datos/16-Árboles de cobertura mínima/_Índice\|Árboles de cobertura mínima]] | MST, propiedad del corte, Kruskal con union-find y Prim con heap |
| [[Estructuras de Datos/17-Caminos más cortos/_Índice\|Caminos más cortos]] | BFS, Dijkstra, Bellman-Ford y detección de ciclos negativos |
| [[Estructuras de Datos/18-Gestión del curso/_Índice\|Gestión del curso]] | Evaluación, preparación de las interrogaciones y material del curso |

## Ruta de estudio sugerida
1. **Análisis de algoritmos → Estructuras lineales:** las herramientas para demostrar y medir, y las dos formas básicas de guardar datos. El C necesario está en [[Programación en C/_Índice|Programación en C]].
2. **Ordenamiento elemental → Mergesort → Quicksort → Heaps → Ordenamiento lineal:** de $O(n^2)$ a $O(n \log n)$ y, con información extra sobre los datos, a $O(n)$.
3. **ABB → Árboles balanceados → Árboles B+ → Tablas de hash:** diccionarios, desde el árbol simple hasta la tabla sin orden.
4. **Backtracking → Algoritmos codiciosos → Programación dinámica:** las técnicas de diseño y cuándo usar cada una.
5. **Grafos y DFS → Árboles de cobertura mínima → Caminos más cortos:** algoritmos en grafos, muchos de ellos aplicaciones de las técnicas anteriores (Prim y Dijkstra son codiciosos; Bellman-Ford es programación dinámica).
6. **Gestión del curso:** para preparar cada interrogación.
