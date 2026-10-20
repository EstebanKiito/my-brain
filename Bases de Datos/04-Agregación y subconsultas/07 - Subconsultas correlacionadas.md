---
ramo: Bases de Datos
tema: Agregación y subconsultas
tags: [bd/subconsultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[05 - Consultas anidadas (IN, ALL, ANY, EXISTS)|Consultas anidadas (IN, ALL, ANY, EXISTS)]]"]
---
# Subconsultas correlacionadas

Una subconsulta correlacionada **usa atributos de la consulta externa**, así que se evalúa de nuevo para cada fila de afuera.

## Subconsultas correlacionadas
La subconsulta depende de la consulta externa: usa `p.nombre`, que cambia con cada fila de afuera.

```sql
SELECT p.nombre 
FROM Películas AS p 
WHERE p.año <> ANY (
	SELECT año
	FROM Películas
	WHERE nombre = p.nombre
)
```

> [!tip] Complemento (slides "Clase 4: SQL Avanzado")
> **Qué pregunta responde:** "nombres de películas que se repiten en años diferentes".
>
> Por cada película `p` de afuera, la subconsulta busca los años de todas las películas **con el mismo nombre** (`nombre = p.nombre`, donde `p` viene de la consulta externa). Si alguno es distinto de `p.año`, hay otra película con el mismo nombre en otro año.
>
> Con `Peliculas = {(Batman, 1989), (Batman, 2005), (Inception, 2010)}`:
> | p | años con ese nombre | `p.año <> ANY (…)` |
> |---|---|---|
> | Batman, 1989 | {1989, 2005} | verdadero (≠ 2005) |
> | Batman, 2005 | {1989, 2005} | verdadero (≠ 1989) |
> | Inception, 2010 | {2010} | falso |
>
> Resultado: Batman, dos veces (con `DISTINCT` aparece una).

> [!example] Ejemplo extra — la misma consulta con EXISTS o con GROUP BY
> ```sql
> SELECT DISTINCT p.nombre
> FROM Peliculas p
> WHERE EXISTS (SELECT * FROM Peliculas q WHERE q.nombre = p.nombre AND q.año <> p.año);
>
> SELECT nombre FROM Peliculas GROUP BY nombre HAVING COUNT(DISTINCT año) > 1;
> ```
> Ojo: una subconsulta correlacionada puede ser cara (se repite por cada fila), aunque el optimizador de PostgreSQL muchas veces la convierte en un join.

## Preguntas de repaso

1. ¿Qué hace que una subconsulta sea correlacionada?
> [!question]- Respuesta
> Que hace referencia a un atributo de la consulta externa (aquí, `p.nombre`), así que su resultado depende de la fila externa que se esté evaluando.

2. ¿Qué devuelve la consulta de esta nota?
> [!question]- Respuesta
> Los nombres de las películas que existen con el mismo nombre en más de un año distinto.

3. Escribe la misma consulta con `GROUP BY` y `HAVING`.
> [!question]- Respuesta
> `SELECT nombre FROM Peliculas GROUP BY nombre HAVING COUNT(DISTINCT año) > 1;`
