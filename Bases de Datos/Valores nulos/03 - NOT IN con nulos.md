---
ramo: Bases de Datos
tema: Valores nulos
tags: [bd/nulos, bd/subconsultas, bd/sql, origen/apuntes]
prerrequisitos: ["[[02 - Lógica de tres valores|Lógica de tres valores]]", "[[05 - Consultas anidadas (IN, ALL, ANY, EXISTS)|Consultas anidadas (IN, ALL, ANY, EXISTS)]]"]
---
# NOT IN con nulos

Si la subconsulta de un `NOT IN` devuelve **algún NULL**, la condición nunca puede ser verdadera y el resultado queda **vacío**. Es la trampa más famosa de los nulos.

## Ejemplos (mis apuntes)

| R | S |
|---|---|
| A | A |
| 1 | 1 |
| 2 | 2 |
| | 3 |
| | 4 |

```sql
SELECT S.A 
FROM S
WHERE S.A NOT IN (
	SELECT R.A
	FROM R
)
```

RESULTADO: {3,4}

| R | S |
|---|---|
| A | A |
| 1 | 1 |
| 2 | 2 |
| null | 3 |
| | 4 |

```sql
SELECT S.A 
FROM S
WHERE S.A NOT IN (
	SELECT R.A
	FROM R
)
```

RESULTADO: TABLA VACIA!!!

Cuando intentas hacer la comparación S.A NOT IN (SELECT R.A FROM R), el valor NULL se maneja de manera especial. La comparación NULL NOT IN (...) se comporta como si la condición fuera desconocida. Por lo tanto, no se puede determinar si el valor NULL está presente o no en el conjunto resultante de la subconsulta. Como resultado, se devuelve una tabla vacía debido a que el resultado de la subconsulta no se puede determinar en presencia de valores NULL.

**EXPLICACION:**

```sql
3 NOT IN {1,2,null}
= NOT (3 IN {1,2,null})
= NOT (3=1 OR 3=2 OR 3 = null) 
= NOT (FALSE OR FALSE OR UNKNOWN) 
= NOT (UNKNOWN)
= UNKWNOWN

# MISMO RAZONAMIENTO PARA 4 NOT IN {1,2,null}
```

> [!tip] Complemento (slides "Clase 4: SQL Avanzado")
> - "El resultado puede ser contraintuitivo pero es correcto."
> - Para los otros valores de S: `1 NOT IN (SELECT R.A FROM R)` es **FALSE** (1 sí está), lo mismo para 2. Para 3 y 4 el resultado es **UNKNOWN**. Ninguna fila da TRUE, así que la tabla queda vacía.
> - Precisión sobre el párrafo de mis apuntes: el problema no es "NULL NOT IN (…)". Es que el NULL está **dentro** del conjunto de la subconsulta, y entonces cada comparación `3 = null` da UNKNOWN.
>
> **Cómo evitarlo:**
> ```sql
> -- 1) excluir los nulos de la subconsulta
> SELECT S.A FROM S WHERE S.A NOT IN (SELECT R.A FROM R WHERE R.A IS NOT NULL);   -- {3, 4}
>
> -- 2) usar NOT EXISTS, que no sufre este problema
> SELECT S.A FROM S WHERE NOT EXISTS (SELECT * FROM R WHERE R.A = S.A);          -- {3, 4}
> ```

## Preguntas de repaso

1. ¿Por qué el segundo ejemplo devuelve una tabla vacía?
> [!question]- Respuesta
> Porque R contiene un NULL. Para 3 y 4, `x NOT IN {1,2,null}` = NOT(FALSE OR FALSE OR UNKNOWN) = UNKNOWN, y para 1 y 2 es FALSE. Ninguna fila da TRUE.

2. Evalúa paso a paso `4 NOT IN {1, 2, null}`.
> [!question]- Respuesta
> NOT(4=1 OR 4=2 OR 4=null) = NOT(FALSE OR FALSE OR UNKNOWN) = NOT(UNKNOWN) = UNKNOWN.

3. ¿Cómo reescribes la consulta para que devuelva {3, 4} aunque R tenga nulos?
> [!question]- Respuesta
> Con `NOT EXISTS (SELECT * FROM R WHERE R.A = S.A)`, o agregando `WHERE R.A IS NOT NULL` en la subconsulta.
