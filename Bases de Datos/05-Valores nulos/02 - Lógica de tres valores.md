---
ramo: Bases de Datos
tema: Valores nulos
tags: [bd/nulos, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - NULL en SQL|NULL en SQL]]"]
---
# Lógica de tres valores

Con nulos, SQL no usa solo verdadero/falso: toda comparación con `NULL` da **UNKNOWN**. Las operaciones aritméticas con `NULL` dan `NULL`, y el `WHERE` deja pasar **solo** las filas con condición `TRUE`.

## Operaciones con nulos

| R | S |
|---|---|
| A | B |
| 1 | 2 |
| null | 3 |

```sql
SELECT R.A + S.B
FROM R, S
```

| R.A + S.B |
|---|
| 3 |
| 4 |
| NULL |
| NULL |

Con la condición `R.A = S.B`:
1. `R.A = 1` y `S.B = 2` → FALSE.
2. `R.A = NULL` y `S.B = 2` → UNKNOWN.

> [!tip] Complemento — tablas de verdad (slides "Clase 4: SQL Avanzado")
> "Si algún argumento de una operación aritmética es nulo, el resultado es nulo." Las comparaciones con nulo dan **unknown**, que se combina así:
>
> | x | NOT x |
> |---|---|
> | true | false |
> | false | true |
> | unknown | unknown |
>
> | AND | true | false | unknown |
> |---|---|---|---|
> | **true** | true | false | unknown |
> | **false** | false | false | false |
> | **unknown** | unknown | false | unknown |
>
> | OR | true | false | unknown |
> |---|---|---|---|
> | **true** | true | true | true |
> | **false** | true | false | unknown |
> | **unknown** | true | unknown | unknown |
>
> Truco para recordarlo: piensa en unknown como "½": AND es el mínimo, OR el máximo y NOT es $1 - x$.
>
> El `WHERE` (y el `ON` de un join, y el `HAVING`) solo deja pasar `true`; descarta `false` **y** `unknown`. Un `CHECK`, en cambio, rechaza solo los `false`.

## Preguntas de repaso

1. ¿Cuánto vale `1 + NULL`? ¿Y `NULL = NULL`?
> [!question]- Respuesta
> `1 + NULL` es `NULL`. `NULL = NULL` es `UNKNOWN`, no `TRUE`.

2. ¿Cuánto valen `FALSE AND UNKNOWN` y `TRUE OR UNKNOWN`?
> [!question]- Respuesta
> `FALSE AND UNKNOWN = FALSE` y `TRUE OR UNKNOWN = TRUE`: en ambos casos el resultado ya está decidido sin importar el unknown.

3. ¿Qué hace el `WHERE` con una fila cuya condición da UNKNOWN?
> [!question]- Respuesta
> La descarta: solo pasan las filas con condición TRUE.

4. ¿Cuántas filas devuelve `SELECT R.A + S.B FROM R, S` en el ejemplo y cuáles son nulas?
> [!question]- Respuesta
> 4 filas (producto cruz 2 × 2): 3 y 4 vienen de `R.A = 1`; las dos con `R.A = null` dan null.
