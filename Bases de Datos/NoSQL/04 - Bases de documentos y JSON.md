---
ramo: Bases de Datos
tema: NoSQL
tags: [bd/nosql, origen/complemento]
prerrequisitos: ["[[03 - Bases key-value y de grafos|Bases key-value y de grafos]]", "[[02 - Modelo relacional|Modelo relacional]]"]
---
# Bases de documentos y JSON

Una base de documentos es una key-value donde el valor es un **documento JSON**, agrupado en **colecciones** y con un lenguaje de consultas más poderoso. Sirve muy bien para mostrar información jerárquica, y mal para cruces complejos y datos que cambian mucho.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 14: NoSQL")
> - Especializadas en documentos: CouchDB y MongoDB guardan sus datos en documentos **JSON**. JSON no es el único estándar (también existe XML).
> - Parecidas a las key-value stores, pero el **valor es un documento**, se pueden agrupar documentos en **colecciones** y el lenguaje de consultas es mucho más poderoso.
>
> Colección `Usuarios`:
> ```json
> {
>   "uid": 1,
>   "name": "Adrian",
>   "last_name": "Soto",
>   "ocupation": "Delantero de Cobreloa",
>   "follows": [2, 3],
>   "age": 24
> }
> ```

> [!tip] Complemento — JSON (slides "Clase 14")
> - *JavaScript Object Notation*: estándar de intercambio de datos semiestructurados en la Web. Se acopla muy bien a los lenguajes de programación.
> - La base son los pares **key-value**: `{ "nombre": "Matías" }`. Los valores pueden ser números, strings (entre comillas), booleanos, arreglos, objetos o `null`.
> - Los **objetos** van entre `{}` con una cantidad arbitraria de pares. Los **arreglos** van entre `[]`:
> ```json
> { "profesores": [
>     {"nombre": "Juan", "apellido": "Reutter"},
>     {"nombre": "Cristian", "apellido": "Riveros"},
>     {"nombre": "Marcelo", "apellido": "Arenas"} ] }
> ```
> | SQL | JSON |
> |---|---|
> | esquema de datos | más flexible: no hay que respetar necesariamente un esquema |
> | lenguajes de consulta independientes del código | más tipos de datos (como arreglos), *human-readable* |

> [!tip] Complemento — ¿para qué? (slides "Clase 14")
> Guardan muchos documentos: uno por libro, uno por persona. Es **altamente jerárquico**.
>
> **Pueden verse como un caché de una BD relacional.** Con `Students(StudentID, Nombre, Carrera)`, `Courses(courseID, name, year)` y `Takes(courseID, StudentID)`, la lista de alumnos por curso exige un **join** en SQL. En una base de documentos se guarda ya preparada:
> ```json
> { "courseID": "IIC2413", "name": "Databases", "year": 2020,
>   "students": [ {"StudentID": 1, "Nombre": "Alice Cooper"},
>                 {"StudentID": 2, "Nombre": "David Bowie"} ] }
> ```
>
> | Qué hacen bien | Qué hacen mal |
> |---|---|
> | traer un libro o persona en particular | manejar información que **cambia mucho** (está duplicada) |
> | lista de alumnos de un curso, nombres de todos los cursos, cursos de David | **cruces no triviales**: "alumnos que toman IIC2413 **y** IMT3830" obliga a un nested loop join a mano (MongoDB soporta JavaScript y Python: se puede, pero no es elegante) |
> | desplegar información en la web | |
>
> **En resumen:** las BD de documentos sirven para información estática, búsquedas simples y cruces muy sencillos. Las BD SQL convienen cuando la información cambia mucho, hay que cruzar datos todo el tiempo o se necesita ACID.
>
> **BD de documentos y BASE:** varias aplicaciones acceden a distintos documentos al mismo tiempo. Están diseñadas para montar varias instancias que, en teoría, tienen la misma información y propagan los updates de forma descoordinada: **consistencia eventual** ([[02 - Consistencia eventual y BASE|BASE]]). Si dos aplicaciones acceden al mismo documento en MongoDB, pueden ver **versiones diferentes**.

## Preguntas de repaso

1. ¿En qué se parece y en qué se diferencia una base de documentos de una key-value?
> [!question]- Respuesta
> Ambas acceden por llave. En la de documentos el valor es un documento JSON estructurado, los documentos se agrupan en colecciones y se puede consultar por su contenido.

2. ¿Por qué se dice que una base de documentos puede ser un caché de una relacional?
> [!question]- Respuesta
> Porque guarda ya armado (desnormalizado) el resultado de joins frecuentes, como la lista de alumnos de cada curso, para mostrarlo sin calcularlo.

3. ¿Qué hacen mal las bases de documentos?
> [!question]- Respuesta
> Manejar información que cambia mucho (está duplicada en varios documentos) y los cruces no triviales entre colecciones.

4. ¿Cuándo preferirías SQL sobre una base de documentos?
> [!question]- Respuesta
> Cuando los datos cambian seguido, hay que cruzar información constantemente o se necesitan garantías ACID.
