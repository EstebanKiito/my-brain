# Lógica en la base de datos — índice

Lógica de negocio que puede vivir dentro del DBMS: vistas, vistas materializadas, triggers y stored procedures (PL/pgSQL), y por qué hoy se usan poco.

Volver al [[Bases de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Las notas parten de los apuntes del ramo, sección «Lógica en Base de Datos». Complementos de las slides de la clase 8 (Lógica en la BDD). La parte de la clase sobre programar con SQL (Python, SQL injection, ORM) está en el tema «Bases de datos en aplicaciones».

## Orden de estudio
1. [[01 - Vistas|Vistas]]: consultas guardadas, cómo se reescriben.
2. [[02 - Vistas materializadas|Vistas materializadas]]: resultados guardados y `REFRESH`.
3. [[03 - Triggers|Triggers]]: BEFORE/AFTER/INSTEAD OF, FOR EACH ROW/STATEMENT, NEW/OLD.
4. [[04 - Trigger para descontar stock en PLpgSQL|Trigger para descontar stock en PL/pgSQL]]: el ejemplo completo.
5. [[05 - Stored procedures|Stored procedures]]: funciones PL/pgSQL, ventajas y desventajas.
