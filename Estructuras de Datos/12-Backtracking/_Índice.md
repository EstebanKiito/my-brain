# Backtracking — índice

La estrategia general para problemas de satisfacción de restricciones: modelar con variables, dominios y restricciones; asignar y retroceder; recorrer grafos implícitos como un laberinto; y acelerar la búsqueda con podas, propagación y heurísticas.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes de las clases de backtracking (8 reinas, CSP, sudoku, plantilla isSolvable, complejidad, laberinto, problemas típicos; 13 imágenes y un dibujo). La sección de podas, propagación y heurísticas se completó con las slides de Backtracking II. El código (8 reinas, conteo de soluciones y laberinto) se verificó en Python.

## Orden de estudio
1. [[01 - Problemas de satisfacción de restricciones|Problemas de satisfacción de restricciones]]: la tripleta $(X, D, C)$, las 8 reinas, el sudoku y cómo modelar.
2. [[02 - Algoritmo de backtracking|Algoritmo de backtracking]]: la plantilla isSolvable, el retroceso, la complejidad $O(K^n)$ y las variantes.
3. [[03 - Backtracking como búsqueda en un laberinto|Backtracking como búsqueda en un laberinto]]: grafos implícitos, marcas de visitado y problemas típicos.
4. [[04 - Podas, propagación y heurísticas|Podas, propagación y heurísticas]]: las tres mejoras, la plantilla mejorada y el paso a un algoritmo codicioso.

Las imágenes de esta carpeta están en `adjuntos/`.
