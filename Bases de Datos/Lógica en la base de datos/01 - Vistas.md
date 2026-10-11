---
ramo: Bases de Datos
tema: Lógica en la base de datos
tags: [bd/logica, bd/sql, origen/apuntes]
prerrequisitos: ["[[03 - GROUP BY|GROUP BY]]", "[[08 - Subconsultas en el FROM|Subconsultas en el FROM]]"]
---
# Vistas

Una vista (`CREATE VIEW`) es una **consulta guardada con nombre** que se usa como si fuera una tabla. No guarda datos: cada vez que se consulta, se ejecuta la consulta original sobre las tablas base.

## 3. Lógica en base de datos — Vistas (mis apuntes)
**Definición y funcionamiento**
- Las vistas son consultas guardadas en la base de datos que pueden ser reutilizadas.
- No almacenan datos físicamente; se reescriben las consultas reemplazando la vista por la consulta original.

**Ventajas de usar vistas**
- **Abstracción:** Simplifican consultas grandes y evitan la repetición de consultas frecuentes.
- **Mantenibilidad:** Más fácil manejar vistas que datos duplicados o redundantes.

**Ejemplo de vistas**

```sql
CREATE VIEW PelEval AS
SELECT pelicula, director, AVG(eval) AS promedio
FROM Evaluaciones
GROUP BY pelicula, director;
```

> [!tip] Complemento — lógica en la BD y cómo se usa una vista (slides "Clase 8: Lógica en la BDD")
> **Lógica de negocio:** son todas las reglas y algoritmos que definen el sistema, dados por lo que quiere lograr la aplicación. Motores como Postgres o MySQL permiten implementar parte de esa lógica directamente en la base de datos: vistas, [[03 - Triggers|triggers]] y [[05 - Stored procedures|stored procedures]].
>
> Con la vista, la consulta frecuente "promedio de las películas de Nolan" queda corta:
> ```sql
> SELECT promedio FROM PelEval WHERE director = 'Christopher Nolan';
> ```
> **Cómo funciona:** las vistas **no son tablas físicas**. Al consultarla, el DBMS (1) reescribe la consulta reemplazando la vista por su definición en el `FROM` y (2) la ejecuta sobre las tablas originales:
> ```sql
> SELECT promedio FROM (
>   SELECT pelicula, director, AVG(eval) AS promedio
>   FROM Evaluaciones GROUP BY pelicula, director
> ) AS PelEval
> WHERE director = 'Christopher Nolan';
> ```
> - No se guarda una tabla ni se crea nada en disco: se trabaja con las tablas base.
> - **Si se actualizan los datos no hay problemas:** al agregar una evaluación, la próxima consulta a `PelEval` ya la incluye.
> - Se elimina con `DROP VIEW PelEval`; después, consultarla da error ("no such table").
> - **Desventaja:** es más lenta que tener la tabla de verdad, porque recalcula todo en cada consulta.

> [!example] Ejemplo extra — vista como capa de seguridad
> ```sql
> CREATE VIEW UsuariosPublicos AS SELECT id, username FROM Usuarios;  -- sin email ni password
> GRANT SELECT ON UsuariosPublicos TO analista;
> ```

## Preguntas de repaso

1. ¿Una vista guarda datos? ¿Qué pasa cuando se consulta?
> [!question]- Respuesta
> No. Es una consulta guardada: al consultarla, el DBMS reemplaza la vista por su definición y la ejecuta sobre las tablas base.

2. ¿Qué ventajas dan las vistas?
> [!question]- Respuesta
> Abstracción (simplifican consultas grandes y evitan repetir consultas frecuentes) y mantenibilidad (más fácil que manejar datos duplicados).

3. Si se inserta una nueva evaluación, ¿la vista `PelEval` la refleja?
> [!question]- Respuesta
> Sí, de inmediato, porque cada consulta a la vista recalcula sobre las tablas actuales.

4. ¿Cuál es la desventaja de una vista frente a una tabla?
> [!question]- Respuesta
> Es más lenta: la consulta completa se vuelve a ejecutar cada vez que se usa la vista.
