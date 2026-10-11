# Bases de Datos (IIC2413) — mapa del curso

Vault de estudio del ramo. Cada nota cubre **un concepto**: no hace falta saber en qué clase se vio, basta con buscar el concepto. Dentro de cada carpeta, el número del archivo indica el orden de lectura.

## Cómo están hechas las notas
- **Frontmatter:** `tema`, `tags` (`origen/apuntes` = parte de mis apuntes; `origen/complemento` = nota nueva) y `prerrequisitos` (lo que conviene leer antes).
- **Cuerpo:** primero mis apuntes; los complementos (slides de las clases 2023-2, documentación de PostgreSQL, conocimiento general) siempre van en callouts `[!tip] Complemento` o `[!example]`.
- **Errores detectados:** van en callouts `[!warning] Posible error` y quedan registrados en `_meta/Bases de Datos/DUDAS.md`.
- **Cierre:** cada nota termina con **Preguntas de repaso**, con la respuesta oculta.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Bases de Datos/Modelo relacional/_Índice\|Modelo relacional]] | DBMS, relaciones, llaves, álgebra relacional |
| [[Bases de Datos/Definición de datos en SQL/_Índice\|Definición de datos en SQL]] | DDL: CREATE/ALTER/DROP TABLE, llaves primarias y foráneas, INSERT, ON DELETE, restricciones |
| [[Bases de Datos/Consultas SQL/_Índice\|Consultas SQL]] | SELECT-FROM-WHERE, UPDATE/DELETE, producto cruz, joins (WHERE, INNER, OUTER), alias, ORDER BY, conjuntos, LIKE, DISTINCT |
| [[Bases de Datos/Agregación y subconsultas/_Índice\|Agregación y subconsultas]] | AVG/MIN/MAX/COUNT/SUM, GROUP BY, HAVING, IN/ALL/ANY/EXISTS, correlacionadas, subconsultas en el FROM |
| [[Bases de Datos/Valores nulos/_Índice\|Valores nulos]] | NULL, IS NULL, lógica de tres valores, NOT IN con nulos, agregados con nulos |
| [[Bases de Datos/Diseño entidad-relación/_Índice\|Diseño entidad-relación]] | Modelo E/R, multiplicidades, IsA, entidades débiles, agregación, paso a tablas, principios de diseño |

## Ruta de estudio sugerida
1. **Modelo relacional:** qué es un DBMS, cómo se guardan los datos en tablas, las llaves y el álgebra relacional.
2. **Definición de datos en SQL:** cómo se crean las tablas, sus llaves y sus restricciones.
3. **Consultas SQL:** leer y modificar datos; joins implícitos y explícitos.
4. **Agregación y subconsultas:** resumir con GROUP BY/HAVING y anidar consultas.
5. **Valores nulos:** la lógica de tres valores y sus trampas (NOT IN, agregados).
6. **Diseño entidad-relación:** modelar el problema antes de crear tablas.
