---
ramo: Bases de Datos
tema: Agregación y subconsultas
tags: [bd/agregacion, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - Funciones de agregación|Funciones de agregación]]"]
---
# GROUP BY

`GROUP BY` separa las filas en grupos que comparten los mismos valores de ciertos atributos y aplica la agregación **a cada grupo por separado**, dejando una fila por grupo.

## GROUP BY

| producto | fecha | precio | cantidad |
|---|---|---|---|
| tomates | 07/02 | 100 | 6 |
| tomates | 06/07 | 150 | 4 |
| zapallo | 08/02 | 800 | 1 |
| zapallo | 09/07 | 1000 | 2 |
| zapallo | 01/01 | 600 | 1 |

```sql
SELECT producto, SUM(precio*cantidad) as ventaTotal
FROM Compra
WHERE fecha > DATE '2024-01-10'  -- fecha es de tipo date
GROUP BY producto;
```

1) **FROM y WHERE:**

| producto | fecha | precio | cantidad |
|---|---|---|---|
| tomates | 07/02 | 100 | 6 |
| tomates | 06/07 | 150 | 4 |
| zapallo | 08/02 | 800 | 1 |
| zapallo | 09/07 | 1000 | 2 |

2) **GROUP BY:**

| producto | fecha | precio | cantidad |
|---|---|---|---|
| tomates | 07/02 | 100 | 6 |
| | 06/07 | 150 | 4 |
| zapallo | 08/02 | 800 | 1 |
| | 09/07 | 1000 | 2 |

3) **Ejecutar proyección:**

| producto | ventaTotal |
|---|---|
| tomates | 1200 |
| zapallo | 2800 |

> [!tip] Complemento — las cuentas y la regla (slides "Clase 4")
> - tomates: $100 \cdot 6 + 150 \cdot 4 = 600 + 600 = 1200$; zapallo: $800 \cdot 1 + 1000 \cdot 2 = 2800$. La fila (zapallo, 01/01) queda fuera por el `WHERE`.
> - La consulta: (1) computa los resultados según el `FROM` y el `WHERE`, (2) agrupa según los atributos del `GROUP BY` y (3) aplica la agregación a cada grupo, independientemente.
> - En el `SELECT` solo pueden ir los atributos agrupados (`producto`) y agregados (`SUM(…)`). `SELECT producto, fecha … GROUP BY producto` da error: un grupo tiene varias fechas.
>
> Otro ejemplo de la clase: `SELECT fabricante, COUNT(fabricante) FROM Productos WHERE año > 2012 GROUP BY fabricante`.

## Preguntas de repaso

1. ¿Cuáles son los tres pasos con que se evalúa la consulta de ventas?
> [!question]- Respuesta
> (1) `FROM` + `WHERE` filtran filas; (2) `GROUP BY producto` forma un grupo por producto; (3) se calcula `SUM(precio*cantidad)` en cada grupo y se proyecta.

2. ¿Por qué tomates suma 1200?
> [!question]- Respuesta
> Porque $100 \cdot 6 + 150 \cdot 4 = 1200$.

3. ¿Por qué falla `SELECT producto, fecha, SUM(precio) FROM Compra GROUP BY producto`?
> [!question]- Respuesta
> Porque `fecha` no está en el `GROUP BY` ni dentro de un agregado, y cada grupo tiene varias fechas: no hay un solo valor que mostrar.

4. ¿Qué problema tiene `WHERE fecha > '10/01'` si `fecha` es texto?
> [!question]- Respuesta
> Compara strings carácter a carácter, no fechas. `'07/02'` queda antes que `'10/01'`, así que el filtro no hace lo que se espera.
