---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, bd/joins, origen/apuntes]
prerrequisitos: ["[[10 - INNER JOIN|INNER JOIN]]"]
---
# Outer joins (LEFT, RIGHT, FULL)

Los outer joins hacen lo mismo que un INNER JOIN, pero además **conservan las filas sin pareja** de una o ambas tablas y completan con `NULL` las columnas de la otra tabla.

Tablas de ejemplo: `employees` y `departments` de [[10 - INNER JOIN|INNER JOIN]] (Eve no tiene departamento y Sales no tiene empleados).

## LEFT JOIN
**Definición:** Un LEFT JOIN devuelve todas las filas de la tabla de la izquierda (table1) y las filas coincidentes de la tabla de la derecha (table2). Si no hay coincidencia, se llenan con NULL.

**Ejemplo:**

```sql
SELECT employees.name, departments.department_name
FROM employees LEFT JOIN departments
ON employees.department_id = departments.department_id;
```

**Resultado del LEFT JOIN:**

| name | department_name |
|---|---|
| John | HR |
| Alice | IT |
| Bob | Marketing |
| Eve | NULL |

## RIGHT JOIN
**Definición:** Un RIGHT JOIN devuelve todas las filas de la tabla de la derecha (table2) y las filas coincidentes de la tabla de la izquierda (table1). Si no hay coincidencia, se llenan con NULL.

**Ejemplo:**

```sql
SELECT employees.name, departments.department_name
FROM employees RIGHT JOIN departments
ON employees.department_id = departments.department_id;
```

**Resultado del RIGHT JOIN:**

| name | department_name |
|---|---|
| John | HR |
| Alice | IT |
| Bob | Marketing |
| NULL | Sales |

## FULL JOIN
**Definición:** Un FULL JOIN devuelve todas las filas de ambas tablas: empareja las que coinciden y, para las que no tienen pareja, completa con NULL las columnas de la otra tabla.

**Ejemplo:**

```sql
SELECT employees.name, departments.department_name
FROM employees
FULL JOIN departments
ON employees.department_id = departments.department_id;
```

**Resultado del FULL JOIN:**

| name | department_name |
|---|---|
| John | HR |
| Alice | IT |
| Bob | Marketing |
| Eve | NULL |
| NULL | Sales |

> [!tip] Complemento — resumen (slides "Clase 4: SQL Avanzado")
> | Join | Conserva sin pareja | En el ejemplo |
> |---|---|---|
> | `R INNER JOIN S` | nada | John, Alice, Bob |
> | `R LEFT OUTER JOIN S` | las tuplas de R | + (Eve, NULL) |
> | `R RIGHT OUTER JOIN S` | las tuplas de S | + (NULL, Sales) |
> | `R FULL OUTER JOIN S` | las de R y las de S | + ambas |
>
> La palabra `OUTER` es opcional: `LEFT JOIN` = `LEFT OUTER JOIN`.
>
> **¿Para qué sirve? (ejemplo de la clase):** "ingresos totales de cada estudio".
> ```sql
> SELECT Estudio.nombre, SUM(Pelicula.ingreso)
> FROM Estudio LEFT OUTER JOIN Pelicula
> ON Estudio.titulo = Pelicula.titulo
> GROUP BY Estudio.nombre;
> ```
> Con `JOIN` normal el resultado es solo `(Warner, 428)`: MGM desaparece porque no tenemos información de sus películas. Con `LEFT OUTER JOIN` queda `(Warner, 428), (MGM, null)`.
>
> La slide recomienda **no** explicar joins con diagramas de Venn: https://blog.jooq.org/say-no-to-venn-diagrams-when-explaining-joins/

> [!example] Ejemplo extra — "anti join": empleados sin departamento
> ```sql
> SELECT e.name
> FROM employees e LEFT JOIN departments d ON e.department_id = d.department_id
> WHERE d.department_id IS NULL;   -- → Eve
> ```

## Preguntas de repaso

1. ¿Qué agrega un LEFT JOIN respecto de un INNER JOIN?
> [!question]- Respuesta
> Las filas de la tabla izquierda que no tienen pareja en la derecha, con `NULL` en las columnas de la derecha.

2. En el ejemplo, ¿qué filas tiene el FULL JOIN que no tiene el INNER JOIN?
> [!question]- Respuesta
> (Eve, NULL), porque Eve no tiene departamento, y (NULL, Sales), porque Sales no tiene empleados.

3. ¿Por qué en el ejemplo de estudios conviene un LEFT JOIN?
> [!question]- Respuesta
> Para que los estudios sin películas registradas (MGM) aparezcan en el resultado, con ingreso nulo, en vez de desaparecer.

4. ¿Cómo encuentras los departamentos sin empleados?
> [!question]- Respuesta
> `SELECT d.department_name FROM departments d LEFT JOIN employees e ON e.department_id = d.department_id WHERE e.employee_id IS NULL;` (→ Sales)
