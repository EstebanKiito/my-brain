---
ramo: Bases de Datos
tema: Transacciones y concurrencia
tags: [bd/transacciones, bd/concurrencia, bd/sql, origen/apuntes]
prerrequisitos: ["[[04 - Lecturas sucias, no repetibles y actualización perdida|Lecturas sucias, no repetibles y actualización perdida]]", "[[11 - Locks y registros fantasma|Locks y registros fantasma]]"]
---
# Niveles de aislamiento

SQL deja elegir **cuánto aislamiento** tiene una transacción. A más aislamiento hay menos anomalías, pero también menos concurrencia. Los cuatro niveles estándar se definen por qué anomalías permiten: lecturas sucias, no repetibles y fantasmas.

## Niveles de aislamiento

![Niveles de aislamiento](adjuntos/Niveles%20de%20aislamiento.png)

> [!note]- Transcripción de la imagen
> ```sql
> SET TRANSACTION ISOLATION LEVEL Level READ ONLY
> SET TRANSACTION ISOLATION LEVEL Level READ WRITE
> ```
> | Level | Dirty Read | Unrepeatable Read | Phantom |
> |---|---|---|---|
> | SERIALIZABLE | No | No | No |
> | REPEATABLE READ | No | No | Maybe |
> | READ COMMITED | No | Maybe | Maybe |
> | READ UNCOMMITED | Maybe | Maybe | Maybe |

Según el estándar SQL (y la slide), el nivel por defecto es `SERIALIZABLE`. En PostgreSQL, en cambio, es `READ COMMITTED`, y en MySQL/InnoDB, `REPEATABLE READ`. Para fijarlo explícitamente:

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE, READ WRITE;
```

`READ WRITE` (o `READ ONLY`) es el **modo de acceso** de la transacción, no un nivel de aislamiento.

> [!tip] Complemento
> - **READ ONLY / READ WRITE** responde a la pregunta de la slide: ¿qué puedo hacer sobre las tablas en mi transacción?
> - Cada nivel corresponde a cuánto tiempo y sobre qué se mantienen los locks:
>   | Nivel | Idea |
>   |---|---|
>   | READ UNCOMMITTED | se puede leer lo no confirmado de otros |
>   | READ COMMITTED | solo se lee lo confirmado, pero cada sentencia ve el estado de ese momento |
>   | REPEATABLE READ | lo leído no cambia durante la transacción |
>   | SERIALIZABLE | equivalente a algún orden serial (sin fantasmas) |
> - En PostgreSQL, READ UNCOMMITTED se comporta como READ COMMITTED, y REPEATABLE READ tampoco tiene fantasmas (usa snapshots, MVCC). Con SERIALIZABLE, una transacción puede fallar con un error de serialización y hay que **reintentarla**.
> - Se usa al inicio de la transacción:
> ```sql
> START TRANSACTION ISOLATION LEVEL REPEATABLE READ;
> …
> COMMIT;
> ```

## Preguntas de repaso

1. ¿Qué anomalías permite READ COMMITTED?
> [!question]- Respuesta
> No permite lecturas sucias, pero sí lecturas no repetibles y fantasmas.

2. ¿Qué nivel elimina las tres anomalías?
> [!question]- Respuesta
> SERIALIZABLE.

3. ¿Cuál es el nivel por defecto en PostgreSQL?
> [!question]- Respuesta
> READ COMMITTED. El estándar SQL (y la slide) dicen SERIALIZABLE.

4. ¿Por qué no se usa siempre SERIALIZABLE?
> [!question]- Respuesta
> Porque reduce la concurrencia y el rendimiento (más bloqueos, esperas o transacciones abortadas que hay que reintentar).
