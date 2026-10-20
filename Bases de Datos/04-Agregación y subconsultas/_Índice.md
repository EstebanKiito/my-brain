# Agregación y subconsultas — índice

Resumir datos con funciones de agregación y GROUP BY / HAVING, y anidar consultas: en el WHERE (IN, ALL, ANY, EXISTS), correlacionadas y en el FROM.

Volver al [[Bases de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Las notas parten de los apuntes del ramo, sección «SQL 2» (de agregación a join anidado). Complementos de las slides de la clase 4 (SQL Avanzado).

## Orden de estudio
1. [[01 - Funciones de agregación|Funciones de agregación]]: AVG, MIN, MAX, COUNT, SUM y la forma general.
2. [[02 - COUNT y DISTINCT|COUNT y DISTINCT]]: `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)`.
3. [[03 - GROUP BY|GROUP BY]]: agregar por grupos, paso a paso.
4. [[04 - HAVING|HAVING]]: filtrar grupos (vs WHERE).
5. [[05 - Consultas anidadas (IN, ALL, ANY, EXISTS)|Consultas anidadas (IN, ALL, ANY, EXISTS)]]: subconsultas en el WHERE.
6. [[06 - Consultas monótonas en SQL|Consultas monótonas en SQL]]: por qué ALL no se puede escribir con SFW.
7. [[07 - Subconsultas correlacionadas|Subconsultas correlacionadas]]: la subconsulta depende de la externa.
8. [[08 - Subconsultas en el FROM|Subconsultas en el FROM]]: tabla temporal con alias (cuenta de películas).
9. [[09 - Subconsulta en el FROM - primera película de cada actor|Subconsulta en el FROM: primera película de cada actor]]: MIN por grupo + join.
