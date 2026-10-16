# Caminos más cortos — índice

Cómo encontrar la ruta más barata entre nodos de un grafo según el tipo de costos: BFS cuando todas las aristas valen lo mismo, Dijkstra con costos no negativos y Bellman-Ford cuando hay costos negativos, incluida la detección de ciclos negativos.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes del examen (clases de BFS y Dijkstra, y de Bellman-Ford; 10 imágenes y 2 fotos de pizarra). Todos los ejemplos se verificaron en Python: las distancias de BFS desde A, las distancias finales de Dijkstra desde 0, el fallo de Dijkstra con la arista −3 y Bellman-Ford con y sin ciclo negativo.

## Orden de estudio
1. [[01 - Búsqueda en amplitud (BFS)|Búsqueda en amplitud (BFS)]]: recorrer por capas con una cola FIFO, $\delta$, $\pi$ y el árbol de rutas más cortas.
2. [[02 - Algoritmo de Dijkstra|Algoritmo de Dijkstra]]: min heap por costo acumulado, colores, por qué funciona y por qué falla con costos negativos.
3. [[03 - Algoritmo de Bellman-Ford|Algoritmo de Bellman-Ford]]: $V - 1$ rondas de relajación, detección de ciclos negativos, $O(VE)$ y comparación de los tres algoritmos.

Las imágenes de esta carpeta están en `adjuntos/`.
