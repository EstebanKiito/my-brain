---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]", "[[04 - Álgebra relacional|Álgebra relacional]]"]
---
# Producto cruz en SQL

Cuando el `FROM` tiene varias tablas, SQL calcula su producto cartesiano: cada fila de la primera tabla combinada con cada fila de la segunda. Equivale al operador × del álgebra.

> [!note] En mis apuntes de la sección 4 había un ítem «Producto Cruz:» vacío; el contenido está en esta nota.

## PRODUCTO CRUZ: (FROM Tabla1, Tabla2) (mis apuntes)
El producto cruz (o producto cartesiano) en SQL se realiza implícitamente mediante el operador FROM cuando se especifican varias tablas. Esto genera una nueva tabla que combina cada fila de la primera tabla con cada fila de la segunda tabla.

Por ejemplo, si tenemos dos tablas, R y S:

| Tabla R | | | Tabla S | |
|---|---|---|---|---|
| a | b | | c | d |
| 1 | 2 | | 5 | 6 |
| 3 | 4 | | 7 | 8 |

Podemos realizar un producto cruz de estas dos tablas con la siguiente consulta SQL:

```sql
SELECT * FROM R, S;
```

El resultado sería una nueva tabla que combina cada fila de R con cada fila de S:

| a | b | c | d |
|---|---|---|---|
| 1 | 2 | 5 | 6 |
| 1 | 2 | 7 | 8 |
| 3 | 4 | 5 | 6 |
| 3 | 4 | 7 | 8 |

Es importante tener en cuenta que el producto cruz puede generar una gran cantidad de datos, especialmente si las tablas involucradas tienen muchas filas. En la práctica, suele ser más útil realizar un producto cruz junto con una condición (a menudo utilizando la cláusula WHERE), para limitar los resultados a las combinaciones de filas que satisfacen cierta condición.

> [!tip] Complemento (slides "Clase 3")
> Si pedimos datos de más de una tabla, la base de datos hace un producto cruz y entrega $n \times m$ filas:
> ```sql
> SELECT * FROM Peliculas, Actuo_en;
> ```
> Con 5 películas y 5 filas en `Actuo_en` son 25 filas, casi todas sin sentido (una película junto a un actor que no actuó en ella). Agregar la condición `WHERE Peliculas.id = Actuo_en.id_pelicula` lo convierte en un join: [[04 - Join con WHERE|Join con WHERE]].
>
> Sintaxis explícita equivalente: `SELECT * FROM R CROSS JOIN S;`

## Preguntas de repaso

1. ¿Cuántas filas devuelve `SELECT * FROM R, S` si R tiene 2 filas y S tiene 2?
> [!question]- Respuesta
> 2 × 2 = 4 filas: todas las combinaciones de una fila de R con una de S.

2. ¿A qué operador del álgebra relacional corresponde un `FROM` con varias tablas?
> [!question]- Respuesta
> Al producto cruz × (producto cartesiano).

3. ¿Por qué casi nunca se usa el producto cruz solo?
> [!question]- Respuesta
> Porque genera muchísimas filas (n·m) y la mayoría combina datos sin relación. Casi siempre se acompaña de una condición en el `WHERE`, y así se vuelve un join.
