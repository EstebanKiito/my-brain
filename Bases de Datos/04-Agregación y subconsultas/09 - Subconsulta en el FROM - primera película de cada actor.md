---
ramo: Bases de Datos
tema: Agregación y subconsultas
tags: [bd/subconsultas, bd/agregacion, bd/sql, origen/apuntes]
prerrequisitos: ["[[08 - Subconsultas en el FROM|Subconsultas en el FROM]]"]
---
# Subconsulta en el FROM: primera película de cada actor

Segundo ejemplo de join anidado: la subconsulta une `Actuo_en` con `Peliculas` y calcula con `MIN` el año de la primera película de cada actor. Después se une con `Actores` para mostrar el nombre.

## Join anidado — Ejemplo 2 (mis apuntes)
“El nombre de cada actor junto con el año de la primera película que actuó”

```sql
SELECT Actores.nombre, agg.año 
FROM Actores, (
	SELECT Actuo_en.id_actor as id, MIN(Peliculas.año) as año 
	FROM Actuo_en, Peliculas
	WHERE Actuo_en.id_pelicula = Peliculas.id
	GROUP BY id_actor
) as agg
WHERE Actores.id = agg.id
```

Tablas `Actores` y `Actuo_en`: las mismas del [[08 - Subconsultas en el FROM|Ejemplo 1]].

| Peliculas | | |
|---|---|---|
| id | nombre | año |
| 1 | Titanic | 1997 |
| 2 | Interstellar | 2014 |
| 3 | Harry Potter and the Sorcerer's Stone | 2001 |

**SUB-CONSULTA:**

```sql
SELECT Actuo_en.id_actor as id, MIN(Peliculas.año) as año 
FROM Actuo_en, Peliculas
WHERE Actuo_en.id_pelicula = Peliculas.id
GROUP BY id_actor
```

Esta subconsulta une las tablas "Actuo_en" y "Peliculas" utilizando la condición Actuo_en.id_pelicula = Peliculas.id para obtener el año mínimo (el año más antiguo) de las películas en las que cada actor ha actuado. Devuelve dos columnas: "id" (el id del actor) y "año" (el año mínimo de las películas en las que ha actuado cada actor).

| id | año |
|---|---|
| 1 | 1997 |
| 2 | 2014 |
| 3 | 2001 |
| 4 | 2001 |

**RESULTADO FINAL:**

| nombre | año |
|---|---|
| Leonardo DiCaprio | 1997 |
| Matthew McConaughey | 2014 |
| Daniel Radcliffe | 2001 |
| Jessica Chastain | 2001 |

> [!warning] Posible error (registrado en `_meta/Bases de Datos/DUDAS.md`)
> Con la tabla `Actuo_en` del ejemplo (1→1,2,3 · 2→1 · 3→2 · 4→3), los años mínimos serían:
> | id | películas | año mínimo |
> |---|---|---|
> | 1 | Titanic, Interstellar, Harry Potter | 1997 ✅ |
> | 2 | Titanic | **1997** (no 2014) |
> | 3 | Interstellar | **2014** (no 2001) |
> | 4 | Harry Potter | 2001 ✅ |
>
> Las filas de McConaughey y Radcliffe no calzan con los datos, salvo que `Actuo_en` fuera distinta. Además, la columna se llama `pelicula_id` en la tabla y `id_pelicula` en la consulta.

> [!tip] Complemento (slides "Clase 4")
> Pregunta de la slide: **"¿Qué pasa si queremos el nombre de la película además del año?"** No se puede agregar `Peliculas.nombre` a la subconsulta, porque no está en el `GROUP BY`. Una solución es volver a unir con `Peliculas`:
> ```sql
> SELECT a.nombre, p.nombre, agg.año
> FROM Actores a, Actuo_en ae, Peliculas p, (
>   SELECT ae2.id_actor AS id, MIN(p2.año) AS año
>   FROM Actuo_en ae2, Peliculas p2
>   WHERE ae2.id_pelicula = p2.id
>   GROUP BY ae2.id_actor
> ) AS agg
> WHERE a.id = agg.id AND ae.id_actor = a.id
>   AND ae.id_pelicula = p.id AND p.año = agg.año;
> ```
> Si un actor tiene dos películas en su primer año, aparecen ambas.

## Preguntas de repaso

1. ¿Qué calcula la subconsulta de este ejemplo?
> [!question]- Respuesta
> Para cada actor, el año de su película más antigua: une Actuo_en con Peliculas, agrupa por actor y toma `MIN(año)`.

2. Según los datos de `Actuo_en`, ¿cuál debería ser el primer año de Matthew McConaughey?
> [!question]- Respuesta
> 1997, porque su única película es la 1 (Titanic). La tabla de mis apuntes dice 2014, lo que es inconsistente.

3. ¿Por qué no basta con agregar `Peliculas.nombre` al `SELECT` de la subconsulta?
> [!question]- Respuesta
> Porque no está en el `GROUP BY` ni es un agregado, y un actor tiene varias películas en su grupo. Hay que volver a unir con Peliculas usando el año mínimo.
