---
ramo: Bases de Datos
tema: Valores nulos
tags: [bd/nulos, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]"]
---
# NULL en SQL

`NULL` es como SQL representa la **falta de información**. No es un valor como 0 o `''`: cualquier comparación con él da *desconocido*, por eso se pregunta con `IS NULL` y no con `= NULL`.

## NULL
En SQL, la falta de información se modela con nulos (`NULL`).

En general, un nulo puede significar que:
- el valor existe, pero no se tiene la información;
- el valor no existe (por ejemplo, alguien sin segundo nombre);
- ni siquiera se sabe si el valor existe o no.

`SELECT * FROM R` **no** equivale a `SELECT * FROM R WHERE R.b = 3 OR R.b <> 3`: si `R.b` es nulo, ni `R.b = 3` ni `R.b <> 3` son verdaderos (ambos dan *unknown*), así que esas filas se pierden. Para recuperarlas hay que agregar las filas con `R.b IS NULL`:

```sql
SELECT * FROM R
-- equivale a:
SELECT * FROM R WHERE R.b = 3
UNION
SELECT * FROM R WHERE R.b <> 3
UNION
SELECT * FROM R WHERE R.b IS NULL
```

- **IS NULL:** verdadero si el valor es nulo.
- **IS NOT NULL:** verdadero si el valor no es nulo.

> [!tip] Complemento (slides "Clase 4: SQL Avanzado")
> - **Información incompleta:** en una base de datos real, muchas veces no tenemos los datos para llenar todas las columnas al agregar una fila. Otras veces, por la lógica del problema, que un campo esté vacío tiene un significado relevante (por ejemplo, "sin premios").
> - Los nulos generan **comportamientos extraños**: en comparaciones ([[02 - Lógica de tres valores|lógica de tres valores]]), en `NOT IN` ([[03 - NOT IN con nulos|NOT IN con nulos]]) y en agregados ([[04 - Agregación con nulos|Agregación con nulos]]).
> - `WHERE b = NULL` **nunca** devuelve filas: `NULL = NULL` es *unknown*, no verdadero. Siempre hay que usar `IS NULL`.
> - Para evitarlos en columnas obligatorias está la restricción `NOT NULL`: ver [[07 - Restricciones de integridad y NOT NULL|Restricciones de integridad y NOT NULL]].
> - Para reemplazar un nulo por un valor al mostrar datos: `COALESCE(b, 0)`.

## Preguntas de repaso

1. ¿Qué tres significados puede tener un NULL?
> [!question]- Respuesta
> Que el valor existe pero no se conoce; que el valor no existe; o que ni siquiera se sabe si existe.

2. ¿Por qué `SELECT * FROM R WHERE R.b = 3 OR R.b <> 3` no devuelve todas las filas de R?
> [!question]- Respuesta
> Porque en las filas con `b` nulo ambas comparaciones dan *unknown*, y el `WHERE` solo deja pasar las filas con condición verdadera. Esas filas se pierden.

3. ¿Qué devuelve `SELECT * FROM R WHERE b = NULL`?
> [!question]- Respuesta
> Ninguna fila, porque cualquier comparación con NULL (incluso `NULL = NULL`) es *unknown*. Hay que escribir `WHERE b IS NULL`.

4. ¿Cómo se escribe `SELECT * FROM R` como unión de tres consultas sobre `b`?
> [!question]- Respuesta
> `… WHERE R.b = 3 UNION … WHERE R.b <> 3 UNION … WHERE R.b IS NULL`.
