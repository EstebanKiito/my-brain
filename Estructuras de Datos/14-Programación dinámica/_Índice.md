# Programación dinámica — índice

Resolver optimización descomponiendo en subproblemas que se repiten y recordando sus soluciones: la recurrencia de las charlas con ganancias, memoización frente a la versión iterativa, el problema del vuelto y la comparación entre las cuatro técnicas de diseño del curso.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes de las clases de programación dinámica y comparación de técnicas (charlas con ganancias, $b(i)$, recurrencia, Opt, RecOpt, ItOpt, vuelto; 12 imágenes y una foto de pizarra). La comparación de técnicas y el caso de coloración se completaron con las slides de la clase de comparación. Todo el ejemplo (b, matriz M, asignación {1, 3, 5}, vuelto) se verificó en Python.

## Orden de estudio
1. [[01 - Subproblemas solapados y subestructura óptima|Subproblemas solapados y subestructura óptima]]: las dos condiciones, el problema de las charlas y la recurrencia $opt(j)$.
2. [[02 - Memoización y versión iterativa|Memoización y versión iterativa]]: de $O(2^n)$ a $O(n)$, cómo reconstruir la solución y la plantilla iterativa.
3. [[03 - Problema del vuelto con programación dinámica|Problema del vuelto con programación dinámica]]: la recurrencia $Z(T, k)$, el algoritmo Change y sus variantes.
4. [[04 - Comparación de técnicas de diseño|Comparación de técnicas de diseño]]: cuándo usar cada estrategia y el caso de la coloración de grafos.

Las imágenes de esta carpeta están en `adjuntos/`.
