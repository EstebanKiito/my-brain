# Almacenamiento e índices — índice

Cómo guarda los datos un DBMS (disco, páginas, buffer), cómo se mide el costo de una consulta (I/O), las estructuras de datos de base (RAM, punteros, arreglos, listas, diccionarios, hash) y los índices (hash, árbol B+, clustered/unclustered).

Volver al [[Bases de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Las notas 02 a 08 parten de los apuntes del ramo («Almacenamiento y Jerarquía de Memoria» y «EDD y Almacenamiento e Índices»), con 10 imágenes transcritas. La parte de índices (09 a 13) y la nota 01 son complemento de las slides de la clase 9 (Almacenamiento y Índices), con 7 slides.

## Orden de estudio
1. [[01 - Arquitectura de un DBMS|Arquitectura de un DBMS]]: módulos y ciclo de vida de una consulta.
2. [[02 - Disco duro y páginas|Disco duro y páginas]]: sector, página, rendimiento, jerarquía de memoria.
3. [[03 - Disco, RAM y buffer pool|Disco, RAM y buffer pool]]: traer páginas a memoria.
4. [[04 - Modelo de costos de IO|Modelo de costos de I/O]]: ⌈|R|/B⌉ y el costo de una consulta.
5. [[05 - Memoria RAM y punteros|Memoria RAM y punteros]]
6. [[06 - Arreglos y listas ligadas|Arreglos y listas ligadas]]
7. [[07 - Diccionarios|Diccionarios]]: llave → valor; el problema de los RUT.
8. [[08 - Tablas de hash|Tablas de hash]]: función de hash y colisiones.
9. [[09 - Índices en bases de datos|Índices en bases de datos]]: qué son, `CREATE INDEX`, search key y data entry.
10. [[10 - Índice hash|Índice hash]]: buckets y overflow pages.
11. [[11 - Índice árbol B+|Índice árbol B+]]: búsqueda logarítmica y rangos.
12. [[12 - Índices clustered y unclustered|Índices clustered y unclustered]]: costos comparados.
13. [[13 - Índice hash vs árbol B+|Índice hash vs árbol B+]]: cuál elegir.

Las imágenes de esta carpeta están en `adjuntos/`.
