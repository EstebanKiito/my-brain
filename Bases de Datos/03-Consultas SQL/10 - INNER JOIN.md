---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, bd/joins, origen/apuntes]
prerrequisitos: ["[[04 - Join con WHERE|Join con WHERE]]"]
---
# INNER JOIN

`INNER JOIN … ON` es la sintaxis explícita del join: deja solo las filas que tienen pareja en ambas tablas según la condición del `ON`. Es equivalente al join con `WHERE`, pero separa la condición de unión de los filtros.

## INNER JOIN
**Definición:** Un INNER JOIN devuelve solo las filas que tienen coincidencias en ambas tablas.

**Sintaxis:**

```sql
SELECT columns
FROM table1 INNER JOIN table2
ON table1.common_column = table2.common_column;
```

**Ejemplo:**

```sql
SELECT employees.name, departments.department_name
FROM employees INNER JOIN departments
ON employees.department_id = departments.department_id;
```

**Tablas de ejemplo:**

| employees | | | departments | |
|---|---|---|---|---|
| employee_id | name | department_id | department_id | department_name |
| 1 | John | 101 | 101 | HR |
| 2 | Alice | 102 | 102 | IT |
| 3 | Bob | 103 | 103 | Marketing |
| 4 | Eve | NULL | 104 | Sales |

**Resultado del INNER JOIN:**

| name | department_name |
|---|---|
| John | HR |
| Alice | IT |
| Bob | Marketing |

Eve no aparece (su `department_id` es NULL) y Sales tampoco (nadie trabaja ahí). Para conservarlos están los [[11 - Outer joins (LEFT, RIGHT, FULL)|outer joins]].

> [!tip] Complemento — tres formas equivalentes (slides "Clase 4: SQL Avanzado")
> ```sql
> SELECT * FROM Peliculas, Actuo_en WHERE id = id_pelicula;
> SELECT * FROM Peliculas JOIN Actuo_en ON id = id_pelicula;
> SELECT * FROM Peliculas INNER JOIN Actuo_en ON id = id_pelicula;
> ```
> `JOIN` a secas es un alias de `INNER JOIN`. La sintaxis explícita es más clara: la condición de unión va en el `ON` y los filtros en el `WHERE`.
>
> Variantes en PostgreSQL:
> - `USING (department_id)`: cuando la columna se llama igual en ambas tablas, y aparece una sola vez en el resultado.
> - `NATURAL JOIN`: une por **todas** las columnas con el mismo nombre. Es riesgoso si se agregan columnas después.

## Preguntas de repaso

1. ¿Qué filas devuelve un INNER JOIN?
> [!question]- Respuesta
> Solo las combinaciones de filas de ambas tablas que cumplen la condición del `ON`. Las filas sin pareja quedan fuera.

2. ¿Por qué Eve no aparece en el resultado?
> [!question]- Respuesta
> Porque su `department_id` es NULL, y `NULL = 101` (o cualquier valor) no es verdadero: no coincide con ningún departamento.

3. Reescribe `FROM A, B WHERE A.x = B.y` con sintaxis explícita.
> [!question]- Respuesta
> `FROM A INNER JOIN B ON A.x = B.y` (o `FROM A JOIN B ON A.x = B.y`).
