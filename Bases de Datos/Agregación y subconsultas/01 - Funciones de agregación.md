---
ramo: Bases de Datos
tema: Agregación y subconsultas
tags: [bd/agregacion, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]"]
---
# Funciones de agregación

Las funciones de agregación (`AVG`, `MIN`, `MAX`, `COUNT`, `SUM`) resumen una columna completa (o cada grupo) en **un solo valor**.

## SQL 2 (mis apuntes)

| id | nombre | precio | fabricante |
|---|---|---|---|
| 1 | Corolla | 25000 | Toyota |
| 2 | Camry | 30000 | Toyota |
| 3 | Prius | 28000 | Toyota |
| 4 | Accord | 28000 | Honda |
| 5 | Civic | 22000 | Honda |

```sql
SELECT AVG(precio) as promedio
FROM Productos
WHERE fabricante = ‘Toyota’
```

Entrega el precio promedio de los productos marca Toyota

| promedio |
|---|
| 27666.67 |

1. **AVG:** Promedio de una columna
2. **MIN:** Minimo de una columna
3. **MAX:** Maximo de una columna
4. **COUNT:** Cuenta el numero de filas

> [!note] Comillas
> `‘Toyota’` tiene comillas tipográficas copiadas de la slide. En PostgreSQL va `'Toyota'` (ver DUDAS, Consultas SQL). El cálculo: $(25000 + 30000 + 28000)/3 = 27666.67$.

> [!tip] Complemento — forma general de una consulta con agregación (slides "Clase 4: SQL Avanzado")
> ```sql
> SELECT <S>
> FROM R1, …, Rn
> WHERE <Condición 1>
> GROUP BY a1, …, ak
> HAVING <Condición 2>
> ```
> - `S` puede contener atributos de `a1, …, ak` y/o agregados, **pero ningún otro atributo**. Si no, ¿qué valor mostraría para un grupo con varias filas distintas?
> - **Condición 1** usa atributos de las tablas (filtra filas). **Condición 2** es de agregación (filtra grupos).
> - **Orden de evaluación:**
> ```mermaid
> flowchart LR
>   A["FROM + WHERE<br/>(filas)"] --> B["GROUP BY<br/>(grupos)"] --> C["HAVING<br/>(filtra grupos)"] --> D["SELECT<br/>(agregados por grupo)"]
> ```
> - También existe **SUM** (suma de una columna). Sin `GROUP BY`, toda la tabla es un solo grupo y el resultado es una fila.

> [!example] Ejemplo extra — varias a la vez
> ```sql
> SELECT MIN(precio), MAX(precio), SUM(precio), COUNT(*)
> FROM Productos WHERE fabricante = 'Honda';
> -- 22000 | 28000 | 50000 | 2
> ```

## Preguntas de repaso

1. ¿Qué devuelve `SELECT AVG(precio) FROM Productos WHERE fabricante = 'Toyota'`?
> [!question]- Respuesta
> Una sola fila con el promedio del precio de los 3 Toyota: 27666.67.

2. Nombra las funciones de agregación básicas.
> [!question]- Respuesta
> `AVG` (promedio), `MIN` (mínimo), `MAX` (máximo), `COUNT` (cantidad de filas) y `SUM` (suma).

3. ¿Por qué en una consulta con `GROUP BY` el `SELECT` solo puede tener atributos del `GROUP BY` o agregados?
> [!question]- Respuesta
> Porque cada grupo produce una sola fila. Un atributo que no se agrupa podría tener varios valores dentro del grupo, y no habría uno solo que mostrar.
