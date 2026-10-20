# Evaluación de consultas — índice

Cómo ejecuta el DBMS los operadores del álgebra relacional: iteradores, selección y proyección (con y sin índice), algoritmos de join y ordenamiento externo, todo medido en I/O.

Volver al [[Bases de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Todas las notas son complemento de las slides de la clase 10 (Evaluación de consultas); el costo del external merge sort viene del libro de Ramakrishnan y Gehrke.

## Orden de estudio
1. [[01 - Algoritmos en un DBMS e iteradores|Algoritmos en un DBMS e iteradores]]: open/next/close y costo en I/O.
2. [[02 - Selección y proyección|Selección y proyección]]: sin índice, con índice, igualdad y rango.
3. [[03 - Nested loop join|Nested loop join]]: el join más simple (3,1 horas).
4. [[04 - Block nested loop join|Block nested loop join]]: usar el buffer (3,4 segundos).
5. [[05 - External merge sort|External merge sort]]: ordenar más datos que la RAM.
