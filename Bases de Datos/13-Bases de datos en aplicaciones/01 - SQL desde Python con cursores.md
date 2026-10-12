---
ramo: Bases de Datos
tema: Bases de datos en aplicaciones
tags: [bd/aplicaciones, origen/complemento]
prerrequisitos: ["[[01 - SQL y PostgreSQL|SQL y PostgreSQL]]", "[[01 - Transacciones|Transacciones]]"]
---
# SQL desde Python con cursores

Para usar una base de datos desde un programa se abre una **conexión** con una librería del motor (`sqlite3`, `psycopg2`) y se ejecutan las sentencias con un **cursor**, que además recorre los resultados.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 8: Lógica en la BDD", parte "Programando con SQL")
> Hasta ahora la base de datos era un componente aislado, pero no tiene sentido si no se puede conectar a una aplicación. La forma más simple es una **librería especializada** para el motor: en Python, `sqlite3` y `psycopg2` (para Postgres).
>
> **Conexión:** la base de datos queda esperando instrucciones del programa.
> ```python
> import sqlite3
> db_connection = sqlite3.connect('some_db.db')
> # hacer cosas con la db
> db_connection.close()  # cerramos la conexión
> ```
>
> **Cursor:** objeto que ejecuta un comando SQL y representa un "puntero" al output del comando.
> ```python
> cur = db_connection.cursor()  # instanciamos el cursor
> create_query = "CREATE TABLE Peliculas(id INT, titulo VARCHAR(100));"
> insert_query = "INSERT INTO Peliculas VALUES (1, 'Minions');"
> try:
>     cur.execute(create_query)
>     cur.execute(insert_query)
> except sqlite3.OperationalError as e:
>     print(e)
> db_connection.commit()  # guardamos los cambios en disco. ¡No olvidarse antes de cerrar!
> db_connection.close()
> ```
>
> **Obtener resultados:** el cursor recorre los resultados. `fetchone()` trae uno y `fetchall()` todos (¡ojo con la memoria!). En Python el cursor además es **iterable**.
> ```python
> cur.execute("SELECT * FROM Peliculas")
> first_row = cur.fetchone()
> second_row = cur.fetchone()
>
> cur.execute("SELECT * FROM Peliculas")
> rows = cur.fetchall()
>
> cur.execute("SELECT * FROM Peliculas")
> for row in cur:
>     print(row)
> ```

> [!tip] Complemento — conexión con transacciones
> Las librerías abren una **transacción implícita** con la primera sentencia: los cambios no quedan guardados hasta `commit()`, y `rollback()` los deshace (ver [[10 - COMMIT, ROLLBACK y SAVEPOINT|COMMIT, ROLLBACK y SAVEPOINT]]). Si se cierra la conexión sin `commit()`, el `INSERT` se pierde.
>
> Con PostgreSQL:
> ```python
> import psycopg2
> conn = psycopg2.connect(host="localhost", dbname="cine", user="grupo73", password="…")
> with conn, conn.cursor() as cur:        # el with hace commit (o rollback si hay error)
>     cur.execute("SELECT titulo FROM Peliculas")
>     print(cur.fetchall())
> ```

## Preguntas de repaso

1. ¿Qué rol cumplen la conexión y el cursor?
> [!question]- Respuesta
> La conexión es el canal abierto con la base de datos. El cursor ejecuta las sentencias SQL y recorre sus resultados como un puntero.

2. ¿Qué pasa si haces un `INSERT` y cierras la conexión sin `commit()`?
> [!question]- Respuesta
> El cambio se pierde, porque la transacción implícita nunca se confirmó.

3. ¿Qué diferencia hay entre `fetchone()` y `fetchall()`, y cuál es el riesgo del segundo?
> [!question]- Respuesta
> `fetchone()` trae la siguiente fila y `fetchall()` trae todas. Con resultados muy grandes, `fetchall()` puede llenar la memoria; es mejor iterar el cursor.
