---
ramo: Bases de Datos
tema: Valores nulos
tags: [bd/nulos, bd/agregacion, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - NULL en SQL|NULL en SQL]]", "[[02 - COUNT y DISTINCT|COUNT y DISTINCT]]"]
---
# Agregación con nulos

Las funciones de agregación **ignoran los nulos**. La única excepción es `COUNT(*)`, que cuenta filas aunque tengan nulos.

## COUNT (mis apuntes)
R | A: {1,null}

SELECT COUNT(*) FROM R = 2

SELECT COUNT(R.A) FROM R = 1

- ojo!: SELECT SUM(R.A) FROM R = 1

> [!tip] Complemento (slides "Clase 4: SQL Avanzado")
> Para funciones de agregación:
> 1. Se ignoran todos los nulos.
> 2. Se calcula el valor de la agregación.
>
> La única excepción es `COUNT(*)`.
>
> | Consulta sobre `R.A = {1, null}` | Resultado | Por qué |
> |---|---|---|
> | `COUNT(*)` | 2 | cuenta filas |
> | `COUNT(R.A)` | 1 | ignora el nulo |
> | `SUM(R.A)` | 1 | suma solo el 1, no da null |
> | `AVG(R.A)` | 1 | $1/1$, no $1/2$ |
>
> - Si **todos** los valores son nulos (o la tabla está vacía), `SUM`, `AVG`, `MIN` y `MAX` devuelven `NULL`, y `COUNT(col)` devuelve 0. Para mostrar 0 se usa `COALESCE(SUM(R.A), 0)`.
> - El mismo efecto se vio en [[02 - COUNT y DISTINCT|COUNT y DISTINCT]]: `COUNT(*) = 5` vs `COUNT(cantidad) = 3`.
> - Contraste con la aritmética: `1 + NULL` es NULL, pero `SUM` de {1, NULL} es 1, porque la agregación descarta el nulo antes de sumar.

## Preguntas de repaso

1. Si `R.A = {1, null}`, ¿cuánto valen `COUNT(*)`, `COUNT(R.A)` y `SUM(R.A)`?
> [!question]- Respuesta
> 2, 1 y 1, respectivamente.

2. ¿Por qué `SUM(R.A)` da 1 y no NULL, si `1 + NULL` es NULL?
> [!question]- Respuesta
> Porque las funciones de agregación primero descartan los nulos y luego calculan; no suman el NULL.

3. ¿Cuánto vale `AVG(R.A)` con `R.A = {1, null}`?
> [!question]- Respuesta
> 1: se promedia solo sobre los valores no nulos ($1/1$).

4. ¿Qué devuelve `SUM(x)` si todos los valores de x son nulos?
> [!question]- Respuesta
> `NULL` (no 0). Con `COALESCE(SUM(x), 0)` se obtiene 0.
