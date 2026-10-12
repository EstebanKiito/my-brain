---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]"]
---
# DISTINCT

`SELECT DISTINCT` elimina las filas repetidas del resultado. Hace falta porque SQL, a diferencia del álgebra relacional, trabaja con **multiconjuntos**: no quita duplicados por sí solo.

## DISTINCT: (Elimina repetidos) (mis apuntes)

```sql
SELECT DISTINCT nombre 
FROM Peliculas
```

En esta tabla, se muestran los nombres únicos de las películas presentes en la tabla "Peliculas", sin ningún nombre repetido.

| nombre |
|---|
| Interstellar |
| The Revenant |
| Harry Potter |
| The Theory of Everything |
| Inception |

> [!tip] Complemento (slides "Clase 3")
> - **"OJO: DISTINCT es un operador en sí mismo."** No es una función que se aplique a una columna: actúa sobre **la fila completa** del resultado. `SELECT DISTINCT nombre, año` elimina pares (nombre, año) repetidos, no nombres repetidos.
> - **Álgebra vs SQL:** en el álgebra, $\pi_{año}(peliculas)$ ya no tiene duplicados, porque una relación es un conjunto. En SQL, `SELECT año FROM Peliculas` devuelve 2014 dos veces; para igualar el álgebra hay que escribir `SELECT DISTINCT año`.
> - Dentro de una agregación cambia el sentido: `COUNT(DISTINCT cantidad)` cuenta valores distintos.

## Preguntas de repaso

1. ¿Por qué SQL necesita `DISTINCT` si el álgebra relacional no tiene duplicados?
> [!question]- Respuesta
> Porque SQL trabaja con multiconjuntos (bags) y no elimina duplicados automáticamente en un `SELECT`. Hay que pedirlo con `DISTINCT`.

2. ¿Qué elimina `SELECT DISTINCT nombre, año FROM Peliculas`?
> [!question]- Respuesta
> Las filas en que el par (nombre, año) se repite. Un mismo nombre puede aparecer varias veces si tiene años distintos.

3. ¿Qué devuelve `SELECT año FROM Peliculas` en la base del curso, comparado con `SELECT DISTINCT año`?
> [!question]- Respuesta
> El primero devuelve un año por película, con 2014 repetido. El segundo devuelve cada año una sola vez.
