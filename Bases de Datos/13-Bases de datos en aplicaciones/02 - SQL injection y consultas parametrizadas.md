---
ramo: Bases de Datos
tema: Bases de datos en aplicaciones
tags: [bd/aplicaciones, bd/seguridad, origen/complemento]
prerrequisitos: ["[[01 - SQL desde Python con cursores|SQL desde Python con cursores]]"]
---
# SQL injection y consultas parametrizadas

Si una consulta se arma **concatenando** texto que escribe el usuario, ese texto puede traer SQL propio y la base de datos lo ejecuta: eso es **SQL injection**. Se evita con consultas **parametrizadas**, donde la librería envía los valores aparte del SQL.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 8: Lógica en la BDD")
> **Lo importante:** los usuarios de la aplicación ingresan datos y, según ese input, se consulta la base de datos.
>
> **Un ejemplo inocente…**
> ```python
> id = input("id de la película?")
> select_query = "SELECT * FROM Peliculas WHERE id=" + id
> cur.execute(select_query)
> print(cur.fetchone())
> print("Exito!")
> ```
> "Pero profesor, ¿qué tiene de malo concatenar strings para generar consultas?"
> ```
> >> id de la película? 1; DROP TABLE Peliculas; --
> ```
> La consulta que se ejecuta es `SELECT * FROM Peliculas WHERE id=1; DROP TABLE Peliculas; --`: **se borra la tabla**. El `--` comenta lo que pudiera venir después. Nos exponemos a una forma de ataque: **SQL Injection**.
>
> **SQL parametrizado:** si los parámetros de una consulta vienen del input del usuario, hay que pasarlos aparte. A esto se le llama **"sanitizar" el input**: la librería parsea y asegura los parámetros antes de pasarlos a la DB.
> ```python
> # sqlite3 usa ?   —   psycopg2 usa %s
> cur.execute("SELECT * FROM Peliculas WHERE id = ?", (id,))
> cur.execute("SELECT * FROM Peliculas WHERE id = %s", (id,))
> ```
> El valor nunca se interpreta como SQL: `1; DROP TABLE Peliculas; --` se compara literalmente con `id` y no calza con nada.

> [!example] Ejemplo extra — el clásico del login
> ```python
> q = "SELECT * FROM usuarios WHERE email = '" + email + "' AND password = '" + pw + "'"
> # con email = admin@uc.cl' --   la condición del password queda comentada
> # SELECT * FROM usuarios WHERE email = 'admin@uc.cl' --' AND password = '…'
> ```
> Reglas: **nunca** formatear SQL con `+`, f-strings ni `%` de Python sobre el input; usar siempre los parámetros de la librería o los métodos del ORM. El mismo cuidado aplica a los stored procedures con `EXECUTE` dinámico: allá también se usan `$1` y `USING` (ver [[05 - Stored procedures|Stored procedures]]).

## Preguntas de repaso

1. ¿Qué es SQL injection?
> [!question]- Respuesta
> Un ataque en que el input del usuario, concatenado en una consulta, contiene SQL que la base de datos ejecuta, como un `DROP TABLE` o una condición que evita la autenticación.

2. ¿Qué consulta se ejecuta con el input `1; DROP TABLE Peliculas; --` en el ejemplo?
> [!question]- Respuesta
> `SELECT * FROM Peliculas WHERE id=1; DROP TABLE Peliculas; --`, que además de consultar borra la tabla Peliculas.

3. ¿Cómo se evita en Python?
> [!question]- Respuesta
> Con consultas parametrizadas: `cur.execute("… WHERE id = %s", (id,))`. La librería envía el valor por separado y nunca lo interpreta como SQL.
