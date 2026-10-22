# Tópicos avanzados — índice

Herramientas avanzadas de modelamiento algorítmico, procesamiento de texto y análisis de datos en Python: coincidencia y validación de texto con expresiones regulares y el módulo `re`, representación matemática y modelamiento de grafos mediante listas y matrices de adyacencia, algoritmos de búsqueda y recorrido sobre grafos en anchura (BFS) y profundidad (DFS), computación numérica de alto rendimiento con arreglos `ndarray`, vectorización y *broadcasting* en NumPy, y manipulación y análisis de datos tabulares con `Series` y `DataFrame` en Pandas.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los cinco notebooks de la decimoquinta semana del curso (expresiones regulares, grafos y representación, búsqueda en grafos, NumPy y Pandas), complementado con las diapositivas de clases.

## Orden de estudio
1. [[01 - Expresiones regulares patrones metacaracteres y el módulo re|Expresiones regulares, patrones y el módulo re]]: metacaracteres, clases de caracteres, cuantificadores, anclas, grupos de captura y funciones del módulo `re` (`search`, `match`, `sub`).
2. [[02 - Grafos y representaciones listas y matrices de adyacencia|Grafos y representaciones: listas y matrices de adyacencia]]: vértices y aristas, grafos dirigidos vs no dirigidos, aristas ponderadas, y trade-offs espaciales entre listas de adyacencia y matrices.
3. [[03 - Búsqueda en grafos BFS en anchura y DFS en profundidad|Búsqueda en grafos: BFS en anchura y DFS en profundidad]]: prevención de ciclos con conjuntos `visitados`, búsqueda en anchura con colas (BFS y camino más corto) frente a búsqueda en profundidad con pilas o recursión (DFS).
4. [[04 - Computación numérica con NumPy ndarrays vectorización y broadcasting|Computación numérica con NumPy: ndarrays, vectorización y broadcasting]]: memoria contigua en C, tipo `ndarray`, operaciones aritméticas vectorizadas sin bucles, reglas de compatibilidad de broadcasting y reducción por ejes.
5. [[05 - Análisis y manipulación tabular de datos con Pandas|Análisis y manipulación tabular de datos con Pandas]]: estructuras `Series` y `DataFrame`, indexación con `loc` e `iloc`, filtrado booleano compuesto, transformaciones, agregaciones con `groupby()` y persistencia CSV.
