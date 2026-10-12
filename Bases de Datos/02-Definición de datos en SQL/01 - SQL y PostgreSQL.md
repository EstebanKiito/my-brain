---
ramo: Bases de Datos
tema: Definición de datos en SQL
tags: [bd/ddl, origen/complemento]
prerrequisitos: ["[[02 - Modelo relacional|Modelo relacional]]", "[[04 - Álgebra relacional|Álgebra relacional]]"]
---
# SQL y PostgreSQL

SQL (*Structured Query Language*) es el lenguaje práctico para hablar con un DBMS relacional: con él se definen las tablas (DDL) y se consultan o modifican los datos (DML). En el curso se usa con PostgreSQL.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 3: Repaso de llaves + SQL")
> **Cómo funciona un RDBMS:**
> - Es un programa que se instala en un computador (**servidor**) y se mantiene escuchando conexiones.
> - El usuario, generalmente otro programa (**cliente**), se conecta y le entrega instrucciones.
> - Ejemplo: al abrir una película en IMDb, la aplicación le manda al DBMS `SELECT name, score FROM titles WHERE title.id='tt6723592'` y recibe `Tenet | 7.4`.
>
> ```mermaid
> sequenceDiagram
>   participant C as Cliente (app web)
>   participant S as Servidor PostgreSQL
>   C->>S: SELECT name, score FROM titles WHERE …
>   S-->>C: name: Tenet, score: 7.4
> ```

> [!tip] Complemento — qué es SQL (slides "Clase 3")
> - Se usa en **todas las comunicaciones** con bases de datos relacionales: aplicaciones web, locales y móviles, análisis de datos, e incluso arquitecturas serverless.
> - Último estándar de la clase: **SQL99 (SQL3)**. Cada software implementa un "subconjunto" del estándar, con diferencias sutiles.
> - **Declarativo vs. procedural:** en SQL decimos **qué** queremos, sin detallar cómo calcularlo; el DBMS transforma la consulta en un algoritmo. En un lenguaje procedural como Java hay que indicar el procedimiento paso a paso.
>
> | Sublenguaje | Para qué | Comandos |
> |---|---|---|
> | **DDL** (definición de datos) | crear y modificar tablas, atributos y llaves | `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE` |
> | **DML** (manipulación de datos) | consultar una o más tablas; insertar, eliminar y modificar tuplas | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |

> [!tip] Complemento — PostgreSQL (PSQL) y tipos de datos (slides "Clase 3")
> - PSQL es un sistema relacional **open source** con funcionalidades avanzadas, como procedimientos almacenados y almacenamiento de JSON.
> - Se usa en el proyecto: cada grupo tiene acceso a un servidor con una base de datos a la que se conecta su aplicación. Los datos quedan en varios archivos dentro de carpetas ocultas del computador.
>
> | Tipo | Ejemplos |
> |---|---|
> | Caracteres | `char(20)` (largo fijo), `varchar(20)` (largo variable) |
> | Números | `int`, `smallint`, `float`, … (en PostgreSQL también `decimal(10,2)` y `serial`, un entero autoincremental) |
> | Tiempo y fecha | `time` (hora en formato 24 h), `date` (fecha), `timestamp` (fecha + hora) |
>
> Hay muchos más, y dependen del RDBMS. Documentación: https://www.postgresql.org/docs/current/datatype.html

> [!example] Ejemplo extra — conectarse con `psql`
> ```bash
> psql -h localhost -U usuario -d mi_base   # abrir una sesión
> \dt          -- listar tablas
> \d peliculas -- ver el esquema de una tabla
> \q           -- salir
> ```

## Preguntas de repaso

1. ¿Qué significa que SQL sea declarativo?
> [!question]- Respuesta
> Que se describe qué resultado se quiere, sin decir cómo calcularlo. El DBMS decide el algoritmo con el que ejecuta la consulta.

2. ¿Qué diferencia hay entre DDL y DML?
> [!question]- Respuesta
> DDL define la estructura: crear, modificar y eliminar tablas, atributos y llaves. DML trabaja con los datos: consultar, insertar, modificar y eliminar tuplas.

3. ¿Qué diferencia hay entre `char(20)` y `varchar(20)`?
> [!question]- Respuesta
> `char(20)` tiene largo fijo (rellena hasta 20 caracteres) y `varchar(20)` tiene largo variable, con un máximo de 20.

4. Describe la arquitectura cliente-servidor de un RDBMS.
> [!question]- Respuesta
> El DBMS corre en un servidor y escucha conexiones. Un cliente, normalmente otro programa como una app web, se conecta, le envía instrucciones SQL y recibe tablas como resultado.
