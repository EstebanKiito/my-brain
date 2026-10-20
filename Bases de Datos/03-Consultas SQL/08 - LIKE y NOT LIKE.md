---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]"]
---
# LIKE y NOT LIKE

`s LIKE p` compara un string con un patrón: `%` reemplaza cualquier secuencia de caracteres y `_` exactamente uno. `NOT LIKE` deja los que **no** calzan.

## LIKE: patrones de texto

```sql
SELECT *
FROM Peliculas
WHERE name LIKE '%Potter%';
```

1. `%`: cualquier secuencia de caracteres (incluso vacía).
2. `_`: exactamente un carácter cualquiera.
3. Sin comodín al final: después del texto no puede venir ningún otro carácter. Por ejemplo, `correo LIKE '%@gmail.com'` calza con los correos que **terminan** en `@gmail.com`.

## NOT LIKE

```sql
SELECT *
FROM Peliculas
WHERE name NOT LIKE '%a%';  -- películas sin 'a' en el nombre
```

> [!tip] Complemento (slides "Clase 3" y documentación de PostgreSQL)
> | Patrón | Calza con | No calza con |
> |---|---|---|
> | `'%Spiderman%'` | "The Amazing Spiderman 2" | "Spider-Man" |
> | `'Harry%'` | "Harry Potter" (empieza con Harry) | "The Harry" |
> | `'%@gmail.com'` | "ana@gmail.com" (termina así) | "ana@gmail.com.ar" |
> | `'_a%'` | "Batman", "Matrix" (segunda letra a) | "Avatar" |
>
> - `LIKE` distingue mayúsculas de minúsculas. En PostgreSQL existe `ILIKE` para ignorarlas.
> - No son expresiones regulares completas. Para regex, PostgreSQL ofrece `~` y `SIMILAR TO`.

## Preguntas de repaso

1. ¿Qué diferencia hay entre `%` y `_` en un patrón `LIKE`?
> [!question]- Respuesta
> `%` reemplaza cualquier secuencia de caracteres (incluso vacía); `_` reemplaza exactamente un carácter.

2. ¿Qué correos devuelve `WHERE correo LIKE '%@gmail.com'`?
> [!question]- Respuesta
> Los que terminan exactamente en "@gmail.com": antes puede venir cualquier cosa, pero después nada.

3. ¿Cómo encuentras las películas cuyo nombre no contiene la letra "a"?
> [!question]- Respuesta
> `SELECT * FROM Peliculas WHERE name NOT LIKE '%a%';`

4. ¿Por qué `WHERE name LIKE ‘%Potter%'` (copiado de una slide) falla en PostgreSQL?
> [!question]- Respuesta
> Porque usa una comilla tipográfica (‘) en vez de la comilla simple recta ('), que es la única que delimita strings en SQL.
