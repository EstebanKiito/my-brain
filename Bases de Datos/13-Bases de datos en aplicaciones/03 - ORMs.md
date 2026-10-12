---
ramo: Bases de Datos
tema: Bases de datos en aplicaciones
tags: [bd/aplicaciones, origen/complemento]
prerrequisitos: ["[[02 - SQL injection y consultas parametrizadas|SQL injection y consultas parametrizadas]]", "[[03 - Llaves foráneas|Llaves foráneas]]"]
---
# ORMs

Un **ORM** (*Object Relational Mapping*) asocia cada tabla a una **clase** del código (un *modelo*) y cada fila a un objeto. Así se trabaja con objetos y métodos en vez de escribir SQL a mano, aunque por debajo se sigue ejecutando SQL.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 8: Lógica en la BDD")
> - Es un **patrón de diseño** muy adoptado en desarrollo web, mediante librerías incluidas en los frameworks.
> - Fundamentalmente, cada **tabla** de la DB tiene una **clase** (POO) en el código de la aplicación.
> - Nacen de la necesidad de aprovechar la programación orientada a objetos manteniendo el esquema relacional que guarda los datos por debajo. Proporcionan una **capa de abstracción** sobre la base de datos.
>
> **Ejemplos:** Active Record (Ruby on Rails), el ORM de Django (Python), Sequelize (JavaScript/Node). Existen para casi todos los lenguajes y frameworks.
>
> | Concepto del ORM | Qué es | En la BD |
> |---|---|---|
> | **Modelo** | clase que hereda de la clase base del ORM; atributos de instancia = columnas; métodos para manejar los datos y métodos de clase para consultas simples | tabla |
> | **Migración** | "script" que traduce código a `CREATE`, `ALTER` o `DROP TABLE`. Algunos ORMs la generan desde el modelo o por consola; lo complejo (restricciones) suele escribirse a mano. Cada migración es un cambio pequeño del esquema | cambio de esquema |
> | **Asociación** | relaciona modelos como las tablas (1:N, N:N, 1:1): `deposit.monkey`, `monkey.deposits` | llaves foráneas |
>
> Migración de ejemplo de la clase (el SQL que genera):
> ```sql
> CREATE TABLE deposits(
>   id SERIAL,
>   amount int,
>   monkey_id int NOT NULL,
>   created_at date,
>   updated_at date,
>   PRIMARY KEY (id),
>   FOREIGN KEY(monkey_id) REFERENCES monkeys(id)
> );
> ```
>
> En Rails todo esto se vio en [[04 - Modelos y Active Record|Modelos y Active Record]], [[05 - Migraciones en Rails|Migraciones en Rails]] y [[08 - Asociaciones en Active Record|Asociaciones en Active Record]].

> [!tip] Complemento — conclusiones de la clase
> - Los ORMs agregan una capa por encima de la DB, pero **por debajo se sigue escribiendo SQL**, y eso es lo que finalmente se ejecuta.
> - La base de datos es un componente clave de cada aplicación: si no entendemos las consultas que hace el ORM, "estamos ciegos a lo que estamos programando".
> - Con consultas simples el ORM parece facilitar la vida, pero apenas se ponen complejas "dan ganas de volver a SQL".
> - Estamos **agregando una capa más de complejidad** al sistema.
> - **Conclusión:** usar un ORM aporta mucho valor, pero no podemos olvidarnos de SQL. Además, los ORMs parametrizan las consultas, lo que protege de SQL injection.

## Preguntas de repaso

1. ¿Qué es un ORM y qué relación establece?
> [!question]- Respuesta
> Una librería que mapea cada tabla a una clase (modelo) y cada fila a un objeto, para trabajar con la base de datos desde la programación orientada a objetos.

2. ¿Qué son los modelos, las migraciones y las asociaciones de un ORM?
> [!question]- Respuesta
> Los modelos son las clases que representan tablas. Las migraciones son scripts que cambian el esquema (CREATE/ALTER/DROP). Las asociaciones relacionan modelos según las llaves foráneas (1:N, N:N, 1:1).

3. ¿Por qué igual hay que saber SQL si se usa un ORM?
> [!question]- Respuesta
> Porque el ORM genera y ejecuta SQL. Sin entenderlo no se puede saber qué consultas se hacen, optimizarlas ni escribir las complejas.
