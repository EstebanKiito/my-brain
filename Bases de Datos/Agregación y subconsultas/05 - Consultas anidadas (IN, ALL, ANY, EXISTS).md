---
ramo: Bases de Datos
tema: Agregación y subconsultas
tags: [bd/subconsultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]", "[[05 - Alias y expresiones en SELECT|Alias y expresiones en SELECT]]"]
---
# Consultas anidadas (IN, ALL, ANY, EXISTS)

Una consulta anidada usa el resultado de una **subconsulta** dentro de la condición del `WHERE`. Si la subconsulta devuelve un conjunto, se compara con `IN`, `ALL`, `ANY` o `EXISTS`.

## Consultas anidadas (mis apuntes)
Bandas(nombre, vocalista, ...)
Estudiantes_UC(nombre, ...)
Toco_en(nombre_banda, nombre_festival)

```sql
SELECT Bandas.nombre
FROM Bandas, Estudiantes_UC
WHERE Bandas.vocalista = Estudiantes_UC.nombre 
AND Bandas.nombre IN (
	SELECT Toco_en.nombre_banda
	FROM Toco_en
	WHERE Toco_en.nombre_festival = ‘Lollapalooza’
)
```

Comprobamos que Bandas.nombre esté dentro del listado de bandas que han tocado en Lollapalooza.

1. **IN :** forma abreviada de escribir una condición comúnmente utilizada para verificar si un valor está presente en un conjunto de resultados.
    - Por ejemplo, si deseas verificar si el valor de una subconsulta está presente en un conjunto de resultados, puedes usar s IN R. Si el valor devuelto por la subconsulta está presente en el conjunto de resultados, la condición será verdadera; de lo contrario, será falsa.
2. **> ALL:** Esta condición se utiliza para verificar si un valor escalar devuelto por una subconsulta es mayor que TODOS los valores devueltos por otra consulta.
    - Por ejemplo, si deseas verificar si un valor es mayor que todos los valores devueltos por una subconsulta, puedes usar s > ALL R. Si el valor es mayor que todos los valores devueltos por la subconsulta, la condición será verdadera; de lo contrario, será falsa.
3. **> ANY:** Esta condición se utiliza para verificar si un valor escalar devuelto por una subconsulta es mayor que al menos uno de los valores devueltos por otra consulta.
    - Por ejemplo, si deseas verificar si un valor es mayor que al menos uno de los valores devueltos por una subconsulta, puedes usar s > ANY R. Si el valor es mayor que al menos uno de los valores devueltos por la subconsulta, la condición será verdadera; de lo contrario, será falsa.
4. **EXISTS:** Esta condición se utiliza para verificar si la subconsulta devuelve algún resultado o no.
    - Si la subconsulta devuelve algún resultado, la condición EXISTS R será verdadera; de lo contrario, será falsa.
    - Se utiliza comúnmente en combinación con una cláusula WHERE para filtrar filas basadas en la existencia de resultados en una subconsulta.

### ALL
1. Cervezas más baratas que la Austral Calafate

```sql
SELECT Cervezas.nombre 
FROM Cervezas
WHERE Cervezas.precio < ALL (
	SELECT Cervezas2.precio
	FROM Cervezas AS Cervezas2
	WHERE Cervezas2.nombre = ‘Austral Calafate’
)
```

### ANY
1. Cervezas que no son la mas cara

```sql
SELECT Cervezas.nombre 
FROM Cervezas
WHERE Cervezas.precio < ANY (
	SELECT Cervezas2.precio
	FROM Cervezas AS Cervezas2 
)
```

> [!tip] Complemento (slides "Clase 4: SQL Avanzado")
> - Si la subconsulta devuelve **un escalar**, se usan los comparadores típicos (`=`, `<`, …). Si devuelve un conjunto, se agrega un operador: `s IN R`, `s > ALL R`, `s > ANY R`, `EXISTS R`. `ALL` y `ANY` no están disponibles en SQLite.
> - Se puede usar cualquier comparador con `ALL`/`ANY`: `< ALL` significa "menor que todos" y `< ANY` "menor que al menos uno". "No es la más cara" = existe alguna más cara = `precio < ANY (precios)`.
> - Las comillas `‘…’` son tipográficas; en PostgreSQL van `'Lollapalooza'`.
> - **La misma consulta se puede escribir de varias formas**, todas equivalentes: con `IN`, con un join a `Toco_en` + `DISTINCT`, o con `INTERSECT`. Por ser SQL declarativo es difícil predecir cuál rinde mejor; en la práctica importa más **reducir el número de consultas** a la base de datos.

> [!example] Ejemplo extra — EXISTS (bandas que alguna vez tocaron en un festival)
> ```sql
> SELECT b.nombre
> FROM Bandas AS b
> WHERE EXISTS (SELECT * FROM Toco_en t WHERE t.nombre_banda = b.nombre);
> ```
> `NOT EXISTS` da las que nunca han tocado. Ojo: con `NOT IN` y nulos el resultado puede quedar vacío (ver «NOT IN con nulos», en Valores nulos).

## Preguntas de repaso

1. ¿Qué hace `s IN (subconsulta)`?
> [!question]- Respuesta
> Es verdadero si el valor `s` está en el conjunto que devuelve la subconsulta.

2. ¿Qué diferencia hay entre `precio < ALL (…)` y `precio < ANY (…)`?
> [!question]- Respuesta
> `< ALL` exige ser menor que todos los valores de la subconsulta. `< ANY` basta con ser menor que al menos uno.

3. ¿Cómo encuentras las cervezas que no son la más cara?
> [!question]- Respuesta
> Con las que tienen un precio menor que el de al menos otra cerveza: `WHERE precio < ANY (SELECT precio FROM Cervezas)`.

4. ¿Cuándo es verdadero `EXISTS R`?
> [!question]- Respuesta
> Cuando la subconsulta R devuelve al menos una fila.
