---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]"]
---
# ORDER BY

`ORDER BY` ordena el resultado de una consulta por uno o más atributos, de forma ascendente (por defecto) o descendente (`DESC`).

## Ordenamiento

```sql
SELECT nombre, calificacion
FROM Peliculas
ORDER BY nombre, calificacion
```

- Ordena de forma ascendente por `nombre` (alfabéticamente); si hay empate, desempata por `calificacion`.
- En general, cada atributo del `ORDER BY` **resuelve los empates del anterior**: con `ORDER BY a, b, c`, un empate en `a` se resuelve con `b` y, si sigue empatado, con `c`.

| nombre | calificacion |
|---|---|
| Harry Potter | 8.1 |
| Inception | 8.8 |
| Interstellar | 8.6 |
| The Revenant | 8.1 |
| The Theory of Everything | 7.7 |

```sql
SELECT nombre, calificacion
FROM Peliculas
ORDER BY nombre DESC, calificacion
```

| nombre | calificacion |
|---|---|
| The Theory of Everything | 7.7 |
| The Revenant | 8.1 |
| Interstellar | 8.6 |
| Inception | 8.8 |
| Harry Potter | 8.1 |

> [!tip] Complemento
> - `DESC` afecta **solo** al atributo que lo acompaña: en `ORDER BY nombre DESC, calificacion`, `nombre` va descendente y `calificacion` ascendente (`ASC`, el default).
> - Para ver el desempate, ordena primero por calificación: `ORDER BY calificacion DESC, nombre` deja Inception (8.8), Interstellar (8.6) y luego Harry Potter y The Revenant (ambas 8.1), desempatadas alfabéticamente.
> - En PostgreSQL los `NULL` van al final en orden ascendente; se puede cambiar con `NULLS FIRST`.
> - `ORDER BY` se evalúa al final (después de `SELECT`), así que sí puede usar alias de columna. Junto con `LIMIT n` sirve para "los n mejores": `ORDER BY calificacion DESC LIMIT 3`.

## Preguntas de repaso

1. En `ORDER BY a, b, c`, ¿cómo se resuelve un empate en `a`?
> [!question]- Respuesta
> Con `b`; si también empatan en `b`, con `c`. Cada atributo desempata al anterior.

2. ¿Qué hace `ORDER BY nombre DESC, calificacion`?
> [!question]- Respuesta
> Ordena por nombre de Z a A y, ante nombres iguales, por calificación de menor a mayor.

3. ¿Cómo obtienes las 3 películas mejor calificadas?
> [!question]- Respuesta
> `SELECT nombre, calificacion FROM Peliculas ORDER BY calificacion DESC LIMIT 3;`
