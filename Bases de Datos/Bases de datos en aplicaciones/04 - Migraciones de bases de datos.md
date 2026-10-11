---
ramo: Bases de Datos
tema: Bases de datos en aplicaciones
tags: [bd/aplicaciones, origen/complemento]
prerrequisitos: ["[[03 - ORMs|ORMs]]", "[[04 - Modificar y eliminar tablas|Modificar y eliminar tablas]]"]
---
# Migraciones de bases de datos

Una migración es un cambio **versionado y reversible** del esquema: tiene un paso para aplicarlo y otro para deshacerlo. Así el esquema evoluciona junto con el código y se despliega igual en todos los ambientes.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 14: Bases de Datos y desarrollo de software")
> **El problema:** un scraper de precios de cervezas tiene el esquema
> `Cervezas(id, nombre, ibu, abv, id_marca, precio)`, `Marcas(id, nombre, país)`, `Tiendas(id, nombre)` y `Stocks(id_tienda, id_cerveza, cantidad)`.
> La jefa avisa que **el precio de una misma cerveza cambia según la tienda**. A mano habría que crear `Precios(id_cerveza, id_tienda, precio)`, copiar los precios y luego `ALTER TABLE Cervezas DROP COLUMN precio`. ¿Habrá una forma mejor?
>
> **Migraciones:** el esquema define las tablas y sus relaciones. Durante un proyecto los requerimientos cambian y el esquema también. Las migraciones permiten modificarlo a medida que cambian las necesidades.
>
> Ejemplo con *yoyo-migrations* (Python): cada `step` tiene el SQL de ida y el de vuelta.
> ```python
> # file: migrations/0002.create-prices.py
> from yoyo import step
> __depends__ = {"0001.initial-schema"}
> steps = [
>     step(
>         "CREATE TABLE Precios(id_cerveza INT NOT NULL, ...)",
>         "DROP TABLE Precios"
>     ),
>     step(
>         "ALTER TABLE Cervezas DROP COLUMN precio",
>         "ALTER TABLE Cervezas ADD precio DECIMAL(10, 2)"
>     )
> ]
> ```

> [!tip] Complemento — flujo de trabajo (slides "Clase 14")
> 1. Se crean y prueban en la **copia local** de la base de datos. Si no queda bien, se deshace la migración (**rollback**), se arregla y se vuelve a correr.
> 2. Cuando todo está bien, se suben los cambios (por ejemplo, a git).
> 3. Al lanzar una versión nueva, las migraciones pendientes se corren **automáticamente**.
> 4. Si el lanzamiento tiene problemas, se hace redeploy de la versión anterior junto con un rollback de sus migraciones.
>
> **Migraciones delicadas:** corren después del deploy, en la etapa de *release*, antes de que la versión nueva empiece a funcionar. Por eso **deben ser compatibles con la versión anterior** de la aplicación. Los cambios grandes se hacen en varias migraciones y en varios lanzamientos.
>
> **Renombrar una tabla o columna** (la versión anterior ya no podría leerla):
> 1. Crear la tabla o columna nueva con el nombre correcto.
> 2. Escribir los datos nuevos en ambas.
> 3. Copiar los datos de la antigua a la nueva.
> 4. Cambiar las lecturas a la nueva.
> 5. Cuando todo esté bien, dejar de escribir en la antigua y borrarla.
>
> **Rediseñar una base de datos:** hacer todo de nuevo suele ser la peor decisión; si se puede arreglar el modelo sin partir de 0, es preferible. Si es necesario, el proceso es como renombrar, pero mucho más largo: modelar bien algunas tablas en la base nueva, escribir los datos nuevos en ambas (cuidado con las referencias entre bases: PostgreSQL soporta llaves foráneas entre bases, los ORMs en general no), copiar los datos viejos y, cuando la nueva funciona, dejar de usar la vieja.
>
> En Rails: [[05 - Migraciones en Rails|Migraciones en Rails]] (`rails db:migrate`, `rails db:rollback`).

## Preguntas de repaso

1. ¿Qué es una migración y por qué tiene dos partes?
> [!question]- Respuesta
> Un cambio versionado del esquema. Tiene un paso para aplicarlo y otro para revertirlo (rollback), de modo que se puede deshacer si algo sale mal.

2. ¿Por qué las migraciones deben ser compatibles con la versión anterior de la aplicación?
> [!question]- Respuesta
> Porque corren antes de que la versión nueva empiece a funcionar, mientras la anterior todavía puede estar usando la base de datos.

3. ¿Cómo se renombra una columna sin romper la aplicación?
> [!question]- Respuesta
> En varios pasos: crear la nueva, escribir en ambas, copiar los datos, cambiar las lecturas a la nueva y, al final, dejar de escribir en la antigua y borrarla.
