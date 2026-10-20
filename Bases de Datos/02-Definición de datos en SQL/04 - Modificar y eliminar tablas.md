---
ramo: Bases de Datos
tema: Definición de datos en SQL
tags: [bd/ddl, bd/sql, origen/apuntes]
prerrequisitos: ["[[02 - CREATE TABLE y llave primaria|CREATE TABLE y llave primaria]]"]
---
# Modificar y eliminar tablas

Una vez creada, una tabla se puede eliminar entera con `DROP TABLE` o cambiar su estructura con `ALTER TABLE`, agregando o quitando atributos.

## Modificar una tabla
1. `DROP TABLE <Nombre_tabla>`: elimina la tabla.
2. `ALTER TABLE <Nombre_tabla> DROP COLUMN <Atributo>`: elimina un atributo de la tabla.
3. `ALTER TABLE <Nombre_tabla> ADD COLUMN <Atributo> <tipo>`: añade un atributo a la tabla (por ejemplo, de tipo `varchar(255)`).

> [!tip] Complemento — ejemplos de la clase (slides "Clase 3")
> ```sql
> DROP TABLE Peliculas;                                   -- eliminar tabla
> ALTER TABLE Peliculas DROP COLUMN director;              -- eliminar atributo
> ALTER TABLE Peliculas ADD COLUMN productor varchar(30);  -- agregar atributo
> ```

> [!tip] Complemento — otros `ALTER TABLE` útiles en PostgreSQL (documentación oficial: https://www.postgresql.org/docs/current/sql-altertable.html)
> ```sql
> ALTER TABLE Peliculas RENAME COLUMN nombre TO titulo;
> ALTER TABLE Peliculas ALTER COLUMN calificacion SET DEFAULT 0;
> ALTER TABLE Peliculas ADD CONSTRAINT calif_valida CHECK (calificacion BETWEEN 0 AND 10);
> DROP TABLE IF EXISTS Peliculas CASCADE;  -- también borra lo que depende de ella (FK, vistas)
> ```
> - `DROP TABLE` borra la tabla **y todos sus datos**; no hay vuelta atrás fuera de una transacción.
> - Si otra tabla tiene una llave foránea hacia la que se quiere borrar, PostgreSQL da error salvo que se use `CASCADE`.
> - En un proyecto real, estos cambios se hacen con [[05 - Migraciones en Rails|migraciones]] para que todo el equipo tenga el mismo esquema.

## Preguntas de repaso

1. ¿Qué diferencia hay entre `DROP TABLE` y `ALTER TABLE … DROP COLUMN`?
> [!question]- Respuesta
> `DROP TABLE` elimina la tabla completa con todos sus datos. `ALTER TABLE … DROP COLUMN` solo quita un atributo y mantiene la tabla.

2. Agrega un atributo `productor` de tipo `varchar(30)` a `Peliculas`.
> [!question]- Respuesta
> `ALTER TABLE Peliculas ADD COLUMN productor varchar(30);`

3. ¿Qué pasa si intentas borrar una tabla referenciada por una llave foránea de otra?
> [!question]- Respuesta
> PostgreSQL da error, porque otra tabla depende de ella. Con `DROP TABLE … CASCADE` se elimina también la restricción que depende de ella.
