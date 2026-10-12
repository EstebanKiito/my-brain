---
ramo: Bases de Datos
tema: Definición de datos en SQL
tags: [bd/ddl, bd/sql, origen/apuntes]
prerrequisitos: ["[[03 - Llaves foráneas|Llaves foráneas]]"]
---
# INSERT e integridad referencial

`INSERT INTO` agrega tuplas a una tabla. Si la tabla tiene una llave foránea, el DBMS rechaza cualquier fila que apunte a un valor inexistente en la tabla referenciada (integridad referencial).

## 3. Insertar datos (mis apuntes)
1. `INSERT INTO Tabla(at_1,...,at_n) VALUES (v_1,...,v_n)`: Insertar una Tupla a la tabla
2. `INSERT INTO <Nombre_tabla> VALUES (v_1,...,v_n)`: Manera Resumida de insertar (Se asume el orden)

- Observacion: El siguiente codigo dará error: (NO PODEMOS CREAR UNA FILA EN QUE LA LLAVE FORANEA NO EXISTA EN LA OTRA TABLA)

```sql
CREATE TABLE R(a int, b int, PRIMARY KEY(a));
CREATE TABLE S(a int, c int, FOREIGN KEY(a) REFERENCES R, ...);
INSERT INTO R VALUES(1, 1);
INSERT INTO S VALUES(1, 2);
INSERT INTO S VALUES(2, 3); -- Esto provocará un error  ya que no existe un registro con a=2 en la tabla R.
```

| Tabla R | | Tabla S | |
|---|---|---|---|
| a | b | a | c |
| 1 | 1 | 1 | 2 |
| | | 2 | 3 |

En este ejemplo, la tabla S tiene una llave foránea que referencia a la columna 'a' de la tabla R. Como se puede observar, en la tabla S se intenta insertar un valor '2' en la columna 'a', pero no existe un valor correspondiente en la tabla R. Por lo tanto, este intento de inserción provocará un error.

> [!note] Sobre el `...`
> El `...` dentro de `CREATE TABLE S(...)` es un "etcétera" de la slide, no SQL válido. `REFERENCES R` sin columnas apunta a la llave primaria de R (`a`). La fila `(2, 3)` de la tabla S **no llega a insertarse**: es la que se intenta agregar.

> [!tip] Complemento — ejemplos completos (slides "Clase 3" y "Clase 6")
> ```sql
> -- con nombres de atributos
> INSERT INTO Peliculas(id, nombre, año, categoria, calificacion, director)
> VALUES (321351, 'V for Vendetta', 2005, 'Action', 8.2, 'James McTeigue');
>
> -- abreviado: asume el orden de creación de la tabla
> INSERT INTO Peliculas VALUES (321351, 'V for Vendetta', 2005, 'Action', 8.2, 'James McTeigue');
> ```
> - La forma con nombres de atributos es más segura: no se rompe si alguien agrega o reordena columnas, y deja que las columnas omitidas tomen su `DEFAULT` (o `NULL`).
> - Varias filas a la vez: `INSERT INTO R VALUES (1, 1), (2, 5), (3, 7);`
> - El error de PostgreSQL se ve así: `ERROR: insert or update on table "s" violates foreign key constraint … Key (a)=(2) is not present in table "r".`

## Preguntas de repaso

1. ¿Qué diferencia hay entre `INSERT INTO T(a, b) VALUES (…)` e `INSERT INTO T VALUES (…)`?
> [!question]- Respuesta
> La primera indica a qué atributos van los valores; la segunda asume el orden en que se crearon las columnas.

2. ¿Por qué falla `INSERT INTO S VALUES(2, 3)` en el ejemplo?
> [!question]- Respuesta
> Porque `S.a` es llave foránea hacia `R.a` y en R no existe ninguna tupla con `a = 2`. La base de datos no permite filas cuya llave foránea no exista en la tabla referenciada.

3. ¿Por qué conviene escribir los nombres de los atributos en un `INSERT`?
> [!question]- Respuesta
> Porque la consulta no depende del orden de las columnas y las columnas omitidas toman su valor por defecto.
