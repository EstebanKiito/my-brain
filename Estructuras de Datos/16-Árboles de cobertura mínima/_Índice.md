# Árboles de cobertura mínima — índice

Conectar todos los nodos de un grafo no dirigido con el menor costo total: la definición de MST, la propiedad del corte que justifica las estrategias codiciosas, y los algoritmos de Kruskal (con conjuntos disjuntos) y Prim (con un heap).

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> En mis apuntes solo queda registrado que se vio Kruskal. El contenido sale de las slides de las clases de MST con Kruskal y con Prim, de las que se usan 6 como imagen. Ambos algoritmos se implementaron en Python sobre el grafo de las slides y entregan el mismo MST de costo 204.

## Orden de estudio
1. [[01 - Árboles de cobertura mínima y cortes|Árboles de cobertura mínima y cortes]]: definición, aplicaciones, cortes y la propiedad que justifica a Kruskal y Prim.
2. [[02 - Kruskal y conjuntos disjuntos|Kruskal y conjuntos disjuntos]]: el bosque que converge, union-find con compresión de rutas y $O(E \log V)$.
3. [[03 - Algoritmo de Prim|Algoritmo de Prim]]: el árbol que crece, DecreaseKey en el heap, correctitud y $O(E \log V)$.

Las imágenes de esta carpeta están en `adjuntos/`.
