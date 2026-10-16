# Mergesort — índice

El primer algoritmo de ordenación $O(n \log n)$: dividir para conquistar con merge como paso de combinación, su correctitud, el compromiso entre memoria y tiempo, y cómo se resuelve su recurrencia.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes de la clase de mergesort (merge, correctitud, complejidad con y sin memoria extra, resumen de complejidades; 6 imágenes) y en la segunda ayudantía (merge, ejercicio merge-insertion sort). La resolución de la recurrencia sale de las slides de mergesort y se verificó en Python, igual que todo el código.

## Orden de estudio
1. [[01 - Merge de dos secuencias ordenadas|Merge de dos secuencias ordenadas]]: algoritmo, correctitud por inducción y $O(n)$ con memoria extra frente a $O(n^2)$ in place.
2. [[02 - Mergesort y su recurrencia|Mergesort y su recurrencia]]: dividir para conquistar, $T(n) = 2T(n/2) + n$, memoria $O(n)$ y la variante híbrida con insertion sort.

Las imágenes de esta carpeta están en `adjuntos/`.
