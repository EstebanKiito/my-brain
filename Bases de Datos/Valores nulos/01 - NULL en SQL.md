---
ramo: Bases de Datos
tema: Valores nulos
tags: [bd/nulos, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - SELECT, FROM y WHERE|SELECT, FROM y WHERE]]"]
---
# NULL en SQL

`NULL` es como SQL representa la **falta de información**. No es un valor como 0 o `''`: cualquier comparación con él da *desconocido*, por eso se pregunta con `IS NULL` y no con `= NULL`.

## NULL (mis apuntes)
En sql se modela la falta de informacion mediante nulos (NULL)

En general los nulos pueden significar:
- Valor existe, pero no tengo la información
- Valor no existe (si nombre = null la información no existe)
- Ni siquiera sé si el valor existe o no

- SELECT * FROM R ≠ SELECT * FROM R WHERE R.b=3 OR R.b<>3 → (Que no sea ni 3 ni distinto a 3 NO ES NULO!!!)

```sql
SELECT * FROM R 
# <=>

SELECT * FROM R WHERE R.b = 3
UNION
SELECT * FROM R WHERE R.b <> 3
UNION
SELECT * FROM R WHERE R.b IS NULL
```

- **IS NULL:** True si es nulo
- **IS NOT NULL:** True si no es nulo

> [!warning] Posible error (registrado en `_meta/Bases de Datos/DUDAS.md`)
> - La frase "(Que no sea ni 3 ni distinto a 3 NO ES NULO!!!)" se presta a confusión. La idea de la slide es la contraria: **si `R.b` es nulo**, ni `R.b = 3` ni `R.b <> 3` son verdaderos (ambos dan *unknown*). Por eso `WHERE R.b = 3 OR R.b <> 3` **pierde las filas con `b` nulo**, y hay que agregar `UNION … WHERE R.b IS NULL` para recuperar `SELECT * FROM R`.
> - `# <=>` es una anotación ("equivale a"), no SQL: en SQL los comentarios son `--`.

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
