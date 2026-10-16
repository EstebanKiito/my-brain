# Memoria dinámica y Valgrind — índice

Cómo pedir y devolver memoria del heap, qué errores aparecen al hacerlo a mano y cómo encontrarlos con Valgrind.

Volver al [[Programación en C/_Índice|mapa de Programación en C]].

> [!note] Origen
> Basado en mis resúmenes de las cápsulas de C (secciones 7 y 8, con 21 capturas de diagramas y salidas de Valgrind) y en la parte de memoria del taller introductorio. Se completó con las páginas 7 y 8 del CheatSheet de C del curso y con la guía de resolución de problemas (síntomas, comando completo de Valgrind).

## Orden de estudio
1. [[01 - Stack frente a heap|Stack frente a heap]]: por qué no se retorna un arreglo local y cuándo usar el heap.
2. [[02 - malloc, calloc y free|malloc, calloc y free]]: pedir, inicializar y liberar bloques; matrices como arreglo de punteros a filas.
3. [[03 - Errores de memoria y memory leaks|Errores de memoria y memory leaks]]: los cinco errores clásicos y sus síntomas (*segfault*, *stack overflow*).
4. [[04 - Valgrind y detección de memory leaks|Valgrind y detección de memory leaks]]: `-g`, memcheck, leaks directos e indirectos, stack trace.
5. [[05 - Valgrind con valores no inicializados y accesos inválidos|Valgrind con valores no inicializados y accesos inválidos]]: `--track-origins` y cómo leer *invalid read/write*.

Las imágenes de esta carpeta están en `adjuntos/`.
