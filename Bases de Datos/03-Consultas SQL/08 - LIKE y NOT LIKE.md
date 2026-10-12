---
ramo: Bases de Datos
tema: Consultas SQL
tags: [bd/consultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]"]
---
# LIKE y NOT LIKE

`s LIKE p` compara un string con un patrón: `%` reemplaza cualquier secuencia de caracteres y `_` exactamente uno. `NOT LIKE` deja los que **no** calzan.

## LIKE: (REGEX) (mis apuntes)

```sql
SELECT *
FROM Peliculas
WHERE name LIKE ‘%Potter%'
```

1. `%` : Cualquier otra secuencia de caracteres
2. `_` : Cualquier otro caracter (1 solamente)
3. `  ` : No otro caracter → ( correo Like ‘%@gmail.com’ )

## NOT LIKE

```sql
SELECT *
FROM Peliculas
WHERE name NOT LIKE ‘%a%'

# BUSCA TODAS LAS PELICULAS QUE NO TENGAN 'a' EN EL name
```

> [!warning] Posible error (registrado en `_meta/Bases de Datos/DUDAS.md`)
> - **Comillas:** `‘%Potter%'` y `‘%@gmail.com’` usan comillas tipográficas (‘ ’), que vienen de copiar desde la slide. PostgreSQL solo acepta comillas simples rectas: `'%Potter%'`.
> - **Comentarios:** en SQL los comentarios se escriben `-- …` (o `/* … */`), no `# …`.
> - **El punto 3** es ambiguo. Se interpreta así: si el patrón **no** termina en `%`, después del texto no puede venir ningún otro carácter. `'%@gmail.com'` calza con correos que *terminan* en `@gmail.com`.
>
> Versión que corre:
> ```sql
> SELECT * FROM Peliculas WHERE name LIKE '%Potter%';
> SELECT * FROM Peliculas WHERE name NOT LIKE '%a%';  -- películas sin 'a' en el nombre
> ```

> [!tip] Complemento (slides "Clase 3" y documentación de PostgreSQL)
> | Patrón | Calza con | No calza con |
> |---|---|---|
> | `'%Spiderman%'` | "The Amazing Spiderman 2" | "Spider-Man" |
> | `'Harry%'` | "Harry Potter" (empieza con Harry) | "The Harry" |
> | `'%@gmail.com'` | "ana@gmail.com" (termina así) | "ana@gmail.com.ar" |
> | `'_a%'` | "Batman", "Matrix" (segunda letra a) | "Avatar" |
>
> - `LIKE` distingue mayúsculas de minúsculas. En PostgreSQL existe `ILIKE` para ignorarlas.
> - No son expresiones regulares completas, aunque el título de mis apuntes diga "REGEX". Para regex, PostgreSQL ofrece `~` y `SIMILAR TO`.

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

4. ¿Por qué la consulta de mis apuntes con `‘%Potter%'` falla en PostgreSQL?
> [!question]- Respuesta
> Porque usa una comilla tipográfica (‘) en vez de la comilla simple recta ('), que es la única que delimita strings en SQL.
