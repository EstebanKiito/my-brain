---
ramo: Bases de Datos
tema: Agregación y subconsultas
tags: [bd/agregacion, bd/sql, origen/apuntes]
prerrequisitos: ["[[01 - Funciones de agregación|Funciones de agregación]]", "[[09 - DISTINCT|DISTINCT]]"]
---
# COUNT y DISTINCT

`COUNT(*)` cuenta filas, `COUNT(columna)` cuenta solo los valores no nulos y `COUNT(DISTINCT columna)` cuenta los valores distintos. No hay que confundirlo con `SELECT DISTINCT COUNT(…)`.

## COUNT

| producto | fecha | precio | cantidad |
|---|---|---|---|
| tomates | 07/02 | 100 | 6 |
| tomates | 06/07 | 150 | |
| zapallo | 08/02 | 800 | 1 |
| zapallo | 09/07 | 1000 | |
| zapallo | 01/01 | 600 | 1 |

```sql
SELECT COUNT(*)
FROM Compra;
-- 5: cuenta todas las filas
```

```sql
SELECT COUNT(cantidad)
FROM Compra;
-- 3: cuenta solo las filas con cantidad no nula
```

### Observación
SELECT DISTINCT COUNT(cantidad) = 3  ≠  SELECT COUNT( DISTINCT cantidad ) = 2

1. **SELECT DISTINCT COUNT(cantidad):**
   Esta consulta primero cuenta **todos** los valores no nulos de la columna "cantidad", con repetidos (6, 1, 1 → 3). Después, el `DISTINCT` se aplica a las filas del resultado, que es una sola (`3`), así que no cambia nada.
2. **SELECT COUNT(DISTINCT cantidad):**
   Esta consulta primero encuentra todos los valores únicos en la columna "cantidad" y luego cuenta el número total de valores encontrados. Esto significa que si hay filas con el mismo valor de cantidad, ese valor se cuenta solo una vez: {6, 1} → 2.

> [!tip] Complemento (slides "Clase 4: SQL Avanzado")
> | Expresión | Cuenta | Resultado en `Compra` |
> |---|---|---|
> | `COUNT(*)` | filas, **incluidos los nulos** | 5 |
> | `COUNT(cantidad)` | valores no nulos de `cantidad` (con duplicados) | 3 |
> | `COUNT(DISTINCT cantidad)` | valores no nulos **distintos** | 2 |
> | `SELECT DISTINCT COUNT(cantidad)` | igual que `COUNT(cantidad)`; el DISTINCT no afecta | 3 |
>
> La slide lo resume: "`COUNT(*)` cuenta los nulos. Ojo: en ambas se cuentan los duplicados". Comentarios: en SQL son `--`, no `#`.

## Preguntas de repaso

1. ¿Por qué `COUNT(*)` da 5 y `COUNT(cantidad)` da 3?
> [!question]- Respuesta
> `COUNT(*)` cuenta todas las filas; `COUNT(cantidad)` ignora las 2 filas con `cantidad` nula.

2. ¿Cuánto vale `COUNT(DISTINCT cantidad)` y por qué?
> [!question]- Respuesta
> 2, porque los valores no nulos son 6, 1 y 1, y los distintos son {6, 1}.

3. ¿Qué hace realmente el `DISTINCT` en `SELECT DISTINCT COUNT(cantidad)`?
> [!question]- Respuesta
> Elimina filas repetidas del resultado. Como el resultado es una sola fila (3), no tiene efecto.
