# Definición de datos en SQL — índice

La parte DDL de SQL: crear tablas con su llave primaria, enlazarlas con llaves foráneas, modificarlas, insertar datos respetando la integridad referencial y declarar restricciones.

Volver al [[Bases de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Mis apuntes de la I1 («SQL 1»: secciones 1 a 3, «Eliminación con llaves foráneas» y «Restricción de nulos»). Complementos de las slides de las clases 3 (SQL) y 6 (Diseño de Bases de Datos II).

## Orden de estudio
1. [[01 - SQL y PostgreSQL|SQL y PostgreSQL]]: RDBMS cliente-servidor, SQL declarativo, DDL vs DML, tipos de datos.
2. [[02 - CREATE TABLE y llave primaria|CREATE TABLE y llave primaria]]: crear tablas, llave simple y compuesta, `DEFAULT`, `SERIAL`.
3. [[03 - Llaves foráneas|Llaves foráneas]]: `FOREIGN KEY … REFERENCES`, relaciones 1:N, N:M y 1:1.
4. [[04 - Modificar y eliminar tablas|Modificar y eliminar tablas]]: `DROP TABLE` y `ALTER TABLE`.
5. [[05 - INSERT e integridad referencial|INSERT e integridad referencial]]: `INSERT INTO` y el error por llave foránea inexistente.
6. [[06 - Eliminación con llaves foráneas|Eliminación con llaves foráneas]]: no permitir, `ON DELETE CASCADE`, `ON DELETE SET NULL`.
7. [[07 - Restricciones de integridad y NOT NULL|Restricciones de integridad y NOT NULL]]: `NOT NULL`, `UNIQUE`, `CHECK`, participación.
