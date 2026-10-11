---
ramo: Bases de Datos
tema: Agregación y subconsultas
tags: [bd/agregacion, bd/sql, origen/apuntes]
prerrequisitos: ["[[03 - GROUP BY|GROUP BY]]"]
---
# HAVING

`HAVING` filtra **grupos** después de agregar, usando condiciones sobre funciones de agregación. `WHERE`, en cambio, filtra **filas** antes de agrupar.

## HAVING (mis apuntes)
(Para la misma consulta anterior, pero solo para vendidos mas de 100 veces)

```sql
SELECT producto, SUM(precio*cantidad) as ventaTotal
FROM Compra
WHERE fecha > '10/01'
GROUP BY producto
HAVING SUM(cantidad) > 100
```

La cláusula WHERE se utiliza para filtrar filas antes de que se realice la agregación y el agrupamiento, mientras que la cláusula HAVING se utiliza para filtrar resultados después de que se han realizado las operaciones de agregación y agrupamiento.

En este caso específico:
- La cláusula WHERE fecha > '10/01' filtra las filas de la tabla "Compra" para incluir solo aquellas con fechas posteriores al 10 de enero.
- La cláusula GROUP BY producto agrupa las filas resultantes según el campo "producto".
- La función de agregación SUM se usa para calcular la suma del producto del precio y la cantidad para cada grupo de productos.

Ahora, la cláusula HAVING SUM(cantidad) > 100 se aplica después de la operación de agregación y agrupamiento. Esto filtra los resultados del grupo para incluir solo aquellos grupos donde la suma de la cantidad de productos vendidos es mayor que 100.

Si intentáramos incluir SUM(cantidad) > 100 en la cláusula WHERE, SQL intentaría aplicarlo antes de que se realice la agregación y el agrupamiento, lo que provocaría un error porque no se puede usar una función de agregación en la cláusula WHERE. Por lo tanto, para aplicar una condición basada en una función de agregación, como SUM, COUNT, AVG, etc., se debe utilizar la cláusula HAVING después del GROUP BY.

```mermaid
flowchart LR
  F[FROM Compra] --> W["WHERE fecha > '10/01'<br/>filtra filas"] --> G[GROUP BY producto] --> H["HAVING SUM(cantidad) > 100<br/>filtra grupos"] --> S[SELECT producto, ventaTotal]
```

> [!tip] Complemento
> - Con los datos del ejemplo, ningún grupo cumple: tomates suma 10 unidades y zapallo 3. El resultado sería **vacío**; la consulta muestra la sintaxis.
> - Una condición que **no** usa agregados conviene ponerla en el `WHERE`: descarta filas antes de agrupar y es más eficiente. Por ejemplo, `HAVING producto = 'tomates'` funciona, pero corresponde a `WHERE producto = 'tomates'`.
> - El `HAVING` puede usar un agregado que no esté en el `SELECT` (`SUM(cantidad)` no se muestra).
> - Pregunta de la slide: "¿Por qué usamos HAVING y no lo incluimos en el WHERE?". Porque el `WHERE` se evalúa por fila, antes de que existan los grupos y sus sumas.

> [!example] Ejemplo extra — fabricantes con más de 2 modelos
> ```sql
> SELECT fabricante, COUNT(*) AS modelos
> FROM Productos
> GROUP BY fabricante
> HAVING COUNT(*) > 2;     -- → Toyota | 3
> ```

## Preguntas de repaso

1. ¿Qué diferencia hay entre `WHERE` y `HAVING`?
> [!question]- Respuesta
> `WHERE` filtra filas antes de agrupar y no puede usar agregados. `HAVING` filtra grupos después de agregar y sí usa agregados.

2. ¿Por qué `WHERE SUM(cantidad) > 100` da error?
> [!question]- Respuesta
> Porque el `WHERE` se aplica fila por fila, antes de agrupar. En ese momento todavía no existe la suma de cada grupo.

3. Con los datos del ejemplo, ¿qué devuelve la consulta con `HAVING SUM(cantidad) > 100`?
> [!question]- Respuesta
> Una tabla vacía: tomates suma 10 unidades y zapallo 3, ninguno mayor que 100.

4. ¿En qué orden se evalúan WHERE, GROUP BY, HAVING y SELECT?
> [!question]- Respuesta
> FROM → WHERE → GROUP BY → HAVING → SELECT.
