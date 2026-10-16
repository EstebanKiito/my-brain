# Árboles B+ — índice

El árbol de búsqueda pensado para disco: nodos con muchas llaves, datos solo en las hojas ligadas, inserción con split y eliminación con redistribución o unsplit. Es la estructura de índice más usada en bases de datos.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes de las clases de árboles B+ (definición, índice, inserción con split, eliminación con redistribución y unsplit, eficiencia, duplicados y bulk loading; 18 imágenes de los ejemplos con $d = 2$).

## Orden de estudio
1. [[01 - Estructura de un árbol B+|Estructura de un árbol B+]]: definición de orden $d$, directorio frente a hojas, lista de hojas y por qué sirve en disco.
2. [[02 - Inserción en un árbol B+|Inserción en un árbol B+]]: el algoritmo de split, la copia frente a la subida del divisor y el ejemplo de insertar 8.
3. [[03 - Eliminación y eficiencia de un árbol B+|Eliminación y eficiencia de un árbol B+]]: redistribución, unsplit, $O(\log_{2d} n)$, duplicados y bulk loading.

Las imágenes de esta carpeta están en `adjuntos/`.
