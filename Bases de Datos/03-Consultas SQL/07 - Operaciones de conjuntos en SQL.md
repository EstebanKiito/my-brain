---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]", "[[06 - Consultas en álgebra relacional|Consultas en álgebra relacional]]"]
---
# Operaciones de conjuntos en SQL

`UNION`, `INTERSECT` y `EXCEPT` combinan los resultados de dos consultas como conjuntos, igual que ∪, ∩ y − del álgebra relacional. `UNION ALL` mantiene los duplicados.

## UNION

```sql
SELECT nombre
FROM Actores
UNION
SELECT director
FROM Peliculas;
```

| nombre |
|---|
| A. Iñárritu |
| C. Nolan |
| D. Yates |
| J. Marsh |
| Jessica Chastain |
| Leonardo DiCaprio |
| Matthew McConaughey |
| Daniel Radcliffe |

- **EXCEPT:** diferencia del álgebra
- **UNION:** unión del álgebra
- **INTERSECT:** intersección del álgebra
- **UNION ALL:** unión que admite duplicados

> [!tip] Complemento
> - Las dos consultas deben devolver **la misma cantidad de columnas, con tipos compatibles**. El nombre de la columna del resultado sale de la primera consulta (`nombre`).
> - `UNION`, `INTERSECT` y `EXCEPT` eliminan duplicados (semántica de conjuntos). `UNION ALL` no los elimina y por eso es más rápido.
> - Ejemplos con la base del curso:
> ```sql
> -- actores que también son directores (∩)
> SELECT nombre FROM Actores
> INTERSECT
> SELECT director FROM Peliculas;
>
> -- actores que nunca han dirigido (−)
> SELECT nombre FROM Actores
> EXCEPT
> SELECT director FROM Peliculas;
> ```
> - `EXCEPT` corresponde a la diferencia, que **no es monótona**. Con él se resuelve "dirigidos por Nolan y no por Iñárritu".

## Preguntas de repaso

1. ¿Qué diferencia hay entre `UNION` y `UNION ALL`?
> [!question]- Respuesta
> `UNION` elimina las filas duplicadas del resultado; `UNION ALL` las conserva.

2. ¿Qué operador del álgebra corresponde a `EXCEPT`?
> [!question]- Respuesta
> La diferencia de conjuntos (−).

3. ¿Qué condición deben cumplir dos consultas para combinarlas con `UNION`?
> [!question]- Respuesta
> Deben devolver el mismo número de columnas, con tipos compatibles en cada posición.
