---
ramo: Bases de Datos
tema: Agregación y subconsultas
tags: [bd/subconsultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[06 - Consultas en álgebra relacional|Consultas en álgebra relacional]]", "[[05 - Consultas anidadas (IN, ALL, ANY, EXISTS)|Consultas anidadas (IN, ALL, ANY, EXISTS)]]"]
---
# Consultas monótonas en SQL

Una consulta es **monótona** si agregar datos nunca reduce su resultado. Las consultas `SELECT-FROM-WHERE` lo son; las que usan `ALL` (o `EXCEPT`, `NOT IN`, `NOT EXISTS`) no.

## Consultas monótonas (mis apuntes)
→ SELECT, FROM, WHERE: Son consultas monótonas: Es una consulta que al agregar mas datos nunca reduce el conjunto de resultados que produce

→ All No es monotona!

> [!tip] Complemento (slides "Clase 2" y "Clase 4: SQL Avanzado")
> - Definición formal en [[06 - Consultas en álgebra relacional|Consultas en álgebra relacional]]: $E$ es monótona si $I \subseteq J \Rightarrow E(I) \subseteq E(J)$.
> - Pregunta de la slide: ¿se pueden expresar las consultas con `ALL` y `ANY` usando solo `SELECT-FROM-WHERE`? Pista: SFW es monótona; **con `ANY` sí** (es monótona) y **con `ALL` no** (no es monótona).
>
> **¿Por qué `ALL` no es monótona?** "Cervezas más baratas que la Austral Calafate": si se agrega a la tabla una segunda Austral Calafate más barata, algunas cervezas que antes cumplían dejan de cumplir. El resultado **disminuye** al agregar datos.
>
> **¿Por qué `ANY` sí lo es?** "Cervezas que no son la más cara" equivale a un SFW con dos copias de la tabla:
> ```sql
> SELECT DISTINCT c1.nombre
> FROM Cervezas c1, Cervezas c2
> WHERE c1.precio < c2.precio;
> ```
> Agregar cervezas solo puede agregar parejas `(c1, c2)` que cumplan.
>
> | Monótonas | No monótonas |
> |---|---|
> | SELECT-FROM-WHERE, joins, `UNION`, `IN`, `ANY`, `EXISTS` | `ALL`, `EXCEPT`, `NOT IN`, `NOT EXISTS`, agregación (`COUNT`, `SUM`…) |

## Preguntas de repaso

1. ¿Qué es una consulta monótona?
> [!question]- Respuesta
> Una cuyo resultado nunca se achica al agregar datos a la base: si $I \subseteq J$ entonces $E(I) \subseteq E(J)$.

2. ¿Por qué una consulta con `ALL` no es monótona?
> [!question]- Respuesta
> Porque al agregar una fila a la subconsulta, la condición "menor que todos" puede dejar de cumplirse para filas que antes la cumplían, y el resultado pierde filas.

3. ¿Qué consecuencia tiene que `ALL` no sea monótona?
> [!question]- Respuesta
> Que no se puede expresar con solo SELECT-FROM-WHERE, porque toda consulta SFW es monótona. Se necesita un operador no monótono como `ALL`, `NOT EXISTS` o `EXCEPT`.
