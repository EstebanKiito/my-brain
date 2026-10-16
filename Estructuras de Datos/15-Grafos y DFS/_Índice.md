# Grafos y DFS — índice

Grafos dirigidos para modelar relaciones, cómo representarlos, y la búsqueda en profundidad como base de varios algoritmos: detección de ciclos, clasificación de aristas, orden topológico y componentes fuertemente conectadas (Kosaraju).

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Mis apuntes de estas clases son muy breves (qué es un grafo, DFS en el torpedo, Kosaraju). El contenido sale de las slides de las clases de grafos y de DFS y aplicaciones, de las que se usan 7 como imagen. Todos los ejemplos se verificaron en Python: los tiempos de DFS coinciden con la figura, el orden topológico es 0, 1, 3, 2, 4, 6, 5 y Kosaraju da las 4 componentes.

## Orden de estudio
1. [[01 - Grafos y su representación|Grafos y su representación]]: el proyecto con requisitos, grafos dirigidos y no dirigidos, lista y matriz de adyacencias.
2. [[02 - Detección de ciclos y búsqueda en profundidad|Detección de ciclos y búsqueda en profundidad]]: Posteriors, colores blanco/gris/negro y DFS en $O(V + E)$.
3. [[03 - Tiempos de DFS y tipos de aristas|Tiempos de DFS y tipos de aristas]]: tiempos de inicio y término, intervalos anidados y aristas de árbol, hacia atrás, hacia adelante y cruzadas.
4. [[04 - Orden topológico|Orden topológico]]: definición, por qué sirve el término decreciente y TopSort.
5. [[05 - Componentes fuertemente conectadas y Kosaraju|Componentes fuertemente conectadas y Kosaraju]]: CFC, grafo de componentes, grafo transpuesto y el algoritmo.

Las imágenes de esta carpeta están en `adjuntos/`.
