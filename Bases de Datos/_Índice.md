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

## Ruta de estudio sugerida
1. **Modelo relacional:** qué es un DBMS, cómo se guardan los datos en tablas, las llaves y el álgebra relacional.
2. **Definición de datos en SQL:** cómo se crean las tablas, sus llaves y sus restricciones.
3. **Consultas SQL:** leer y modificar datos; joins implícitos y explícitos.
