---
ramo: Bases de Datos
tema: NoSQL
tags: [bd/nosql, origen/complemento]
prerrequisitos: ["[[04 - Bases de documentos y JSON|Bases de documentos y JSON]]"]
---
# Consultas en MongoDB

MongoDB organiza los datos en **servidor → bases de datos → colecciones → documentos**, y se consulta con `find`, que combina selección (filtro) y proyección (campos), más índices de texto.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 14: NoSQL")
> | Nivel | Qué es | Ejemplo |
> |---|---|---|
> | Servidor | contiene varias bases de datos | Mensajería, Compras, WikiData |
> | Base de datos | contiene colecciones relacionadas | Usuarios, Mensajes, Likes |
> | Colección | agrupación de documentos similares | Usuarios |
> | Documento | un JSON con su llave `_id` (por ejemplo, `60bfd90e002ce228636e506b`) | `{"uid": 1, "name": "Adrian", …}` |
>
> **Consultando a MongoDB:**
> ```js
> show dbs                                          // bases de datos disponibles
> use dbName                                        // usar la base dbName
> show collections                                  // colecciones de la base
> db.colName.find()                                 // todos los documentos
> db.colName.find().pretty()                        // pretty print
> db.colName.find({"name": "Adrian"})               // selección
> db.colName.find({"age": {$gte: 23}})              // selección con operador
> db.colName.find({"age": {$gte: 23}}, {"name": 1}) // selección + proyección
> ```
> Más en: http://aidanhogan.com/teaching/cc5212-1-2020/lectures/MDP2020-10.pdf
>
> **Text search:** un índice especial permite buscar texto rápidamente.
> ```js
> db.colName.createIndex({"attributeName": "text"})
> db.users.find({$text: {$search: "Delantero de Cobreloa"}})
> ```
> Más en: https://www.youtube.com/watch?v=vR97-4UG7x0

> [!example] Ejemplo extra — equivalencias con SQL
> | SQL | MongoDB |
> |---|---|
> | `SELECT * FROM users` | `db.users.find()` |
> | `SELECT * FROM users WHERE name = 'Adrian'` | `db.users.find({"name": "Adrian"})` |
> | `SELECT name FROM users WHERE age >= 23` | `db.users.find({"age": {$gte: 23}}, {"name": 1})` |
> | `INSERT INTO users VALUES (…)` | `db.users.insertOne({...})` |
> | `CREATE INDEX … ON users(name)` | `db.users.createIndex({"name": 1})` |
>
> Operadores de comparación: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`.

## Preguntas de repaso

1. ¿Cómo se organizan los datos en MongoDB?
> [!question]- Respuesta
> Un servidor tiene bases de datos, cada base tiene colecciones y cada colección agrupa documentos JSON similares.

2. Escribe la consulta para obtener solo el nombre de los usuarios con edad ≥ 23.
> [!question]- Respuesta
> `db.users.find({"age": {$gte: 23}}, {"name": 1})`: el primer argumento es la selección y el segundo la proyección.

3. ¿Cómo se busca texto eficientemente en MongoDB?
> [!question]- Respuesta
> Creando un índice de texto (`createIndex({"campo": "text"})`) y consultando con `{$text: {$search: "…"}}`.
