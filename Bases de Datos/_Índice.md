# Bases de Datos (IIC2413) — mapa del curso

Vault de estudio del ramo. Cada nota cubre **un concepto**: no hace falta saber en qué clase se vio, basta con buscar el concepto. Dentro de cada carpeta, el número del archivo indica el orden de lectura.

## Cómo están hechas las notas
- **Frontmatter:** `tema`, `tags` (`origen/apuntes` = parte de mis apuntes; `origen/complemento` = nota nueva) y `prerrequisitos` (lo que conviene leer antes).
- **Cuerpo:** primero mis apuntes; los complementos (slides de las clases 2023-2, documentación de PostgreSQL, libro de Ramakrishnan y Gehrke) siempre van en callouts `[!tip] Complemento` o `[!example]`.
- **Imágenes:** las de mis apuntes y algunas slides en PNG, todas con su transcripción en un callout plegable.
- **Errores detectados:** van en callouts `[!warning] Posible error` y quedan registrados en `_meta/Bases de Datos/DUDAS.md`.
- **Cierre:** cada nota termina con **Preguntas de repaso**, con la respuesta oculta.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Bases de Datos/Modelo relacional/_Índice\|Modelo relacional]] | DBMS, relaciones, llaves, álgebra relacional |
| [[Bases de Datos/Definición de datos en SQL/_Índice\|Definición de datos en SQL]] | CREATE/ALTER/DROP TABLE, llaves primarias y foráneas, INSERT, ON DELETE, restricciones |
| [[Bases de Datos/Consultas SQL/_Índice\|Consultas SQL]] | SELECT-FROM-WHERE, UPDATE/DELETE, joins (WHERE, INNER, OUTER), alias, ORDER BY, conjuntos, LIKE, DISTINCT |
| [[Bases de Datos/Agregación y subconsultas/_Índice\|Agregación y subconsultas]] | agregados, GROUP BY, HAVING, IN/ALL/ANY/EXISTS, correlacionadas, subconsultas en el FROM |
| [[Bases de Datos/Valores nulos/_Índice\|Valores nulos]] | NULL, lógica de tres valores, NOT IN con nulos, agregados |
| [[Bases de Datos/Diseño entidad-relación/_Índice\|Diseño entidad-relación]] | modelo E/R, multiplicidades, IsA, entidades débiles, paso a tablas |
| [[Bases de Datos/Normalización/_Índice\|Normalización]] | dependencias funcionales, 1NF–BCNF, descomposición |
| [[Bases de Datos/Lógica en la base de datos/_Índice\|Lógica en la base de datos]] | vistas, vistas materializadas, triggers, stored procedures |
| [[Bases de Datos/Transacciones y concurrencia/_Índice\|Transacciones y concurrencia]] | ACID, conflictos, schedules, grafo de precedencia, 2PL, deadlocks, aislamiento |
| [[Bases de Datos/Recuperación de fallas/_Índice\|Recuperación de fallas]] | tipos de fallas, log, undo/redo, checkpoints |
| [[Bases de Datos/Almacenamiento e índices/_Índice\|Almacenamiento e índices]] | disco, buffer, costo de I/O, estructuras de datos, índices hash y B+ |
| [[Bases de Datos/Evaluación de consultas/_Índice\|Evaluación de consultas]] | iteradores, selección, joins (NLJ, BNLJ), external merge sort |
| [[Bases de Datos/Bases de datos en aplicaciones/_Índice\|Bases de datos en aplicaciones]] | Python + SQL, SQL injection, ORMs, migraciones, N+1, Pandas |
| [[Bases de Datos/NoSQL/_Índice\|NoSQL]] | CAP, BASE, key-value, grafos, documentos, MongoDB |
| [[Bases de Datos/Privacidad de datos/_Índice\|Privacidad de datos]] | re-identificación, k-anonimato, ℓ-diversidad, privacidad diferencial |
| [[Bases de Datos/Gestión del curso/_Índice\|Gestión del curso]] | evaluación, calendario, examen, proyecto, material |

## Ruta de estudio sugerida
1. **Modelo relacional:** qué es un DBMS, cómo se guardan los datos en tablas, las llaves y el álgebra relacional.
2. **Definición de datos en SQL → Consultas SQL → Agregación y subconsultas → Valores nulos:** todo SQL, de crear tablas a consultas anidadas (materia de la I1).
3. **Diseño entidad-relación → Normalización:** modelar un problema y quitar la redundancia.
4. **Lógica en la base de datos:** vistas, triggers y procedimientos.
5. **Transacciones y concurrencia → Recuperación de fallas:** cómo se garantiza ACID (materia de la I2).
6. **Almacenamiento e índices → Evaluación de consultas:** cómo funciona el DBMS por dentro y cuánto cuesta cada consulta.
7. **Bases de datos en aplicaciones → NoSQL → Privacidad de datos:** la base de datos en el mundo real.

**Para el examen:** sigue la [[02 - Preparación del examen de Bases de Datos|preparación del examen]]. Es principalmente teórico (qué usar, para qué sirve, por qué es mejor) y pone énfasis en almacenamiento, índices, evaluación de consultas, recuperación y privacidad.

**Conexión con Ingeniería de Software:** Active Record, migraciones y asociaciones de Rails ([[04 - Modelos y Active Record|Modelos y Active Record]]), y el teorema CAP ([[04 - Escalamiento y teorema CAP|Escalamiento y teorema CAP]]).
