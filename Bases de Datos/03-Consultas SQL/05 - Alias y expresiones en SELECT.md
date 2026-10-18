---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[04 - Join con WHERE|Join con WHERE]]"]
---
# Alias y expresiones en SELECT

`AS` da un nombre corto a una tabla dentro de la consulta o un nombre a una columna calculada. En el `SELECT` también se pueden hacer operaciones, como concatenar strings con `||`.

## Alias: `AS`

```sql
SELECT P.nombre, A.nombre
FROM Peliculas AS P, Actuo_en AS Ae, Actores AS A
WHERE P.id = Ae.id_pelicula
AND A.id = Ae.id_actor;
```

## Nombramiento y operaciones

```sql
SELECT (nombre || ' dirigida por ' || director) AS creditos, año
FROM Peliculas;
```

| id | nombre | director | año |
|---|---|---|---|
| 1 | Interstellar | C. Nolan | 2014 |
| 2 | ... | ... | |

| creditos | año |
|---|---|
| Interstellar dirigida por C. Nolan | 2014 |

> [!tip] Complemento (slides "Clase 3")
> - El alias de tabla abrevia la consulta de [[04 - Join con WHERE|Join con WHERE]]. La slide advierte que alias de una letra como `p`, `ae`, `a` **no son muy recomendables**, porque restan legibilidad.
> - Hay un caso donde el alias es **obligatorio**: cuando la misma tabla aparece dos veces, como en una subconsulta sobre `Cervezas AS Cervezas2` o en un *self join*:
> ```sql
> -- pares de películas del mismo director
> SELECT p1.nombre, p2.nombre
> FROM Peliculas AS p1, Peliculas AS p2
> WHERE p1.director = p2.director AND p1.id < p2.id;
> ```
> - `||` es el operador de concatenación de strings del estándar SQL (PostgreSQL). En el `SELECT` también funcionan `+ - * /` con números: `SELECT nombre, precio * 1.19 AS precio_con_iva FROM Productos`.
> - `AS` es opcional (`FROM Peliculas P` también funciona), pero se recomienda para leer mejor la consulta.

## Preguntas de repaso

1. ¿Qué devuelve `SELECT (nombre || ' dirigida por ' || director) as creditos, año FROM Peliculas`?
> [!question]- Respuesta
> Dos columnas: `creditos`, con un string como "Interestellar dirigida por C.Nolan", y `año`.

2. ¿Para qué sirven los alias de tabla?
> [!question]- Respuesta
> Para acortar los nombres en consultas con varias tablas y para poder usar la misma tabla dos veces con nombres distintos.

3. ¿Cuándo es imprescindible un alias de tabla?
> [!question]- Respuesta
> Cuando la misma tabla aparece más de una vez en la consulta (self join o subconsulta sobre la misma tabla), para distinguir cada aparición.
