# Dudas y posibles errores en los apuntes originales — Bases de Datos (IIC2413)

Criterio: el texto original **se conserva tal cual** en la nota. Al lado va un callout `> [!warning] Posible error` con la precisión o corrección, y se registra aquí para revisarlo.

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Modelo relacional
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[04 - Álgebra relacional\|Álgebra relacional]] | "Join (⨝): … combina tuplas de dos relaciones basándose en una condición de igualdad. Hay varios tipos de Join, incluyendo Inner Join, Left Outer Join…" | La igualdad describe el *equi-join*. En la clase el join admite cualquier condición: $R_1 \bowtie_{cond} R_2 = \sigma_{cond}(R_1 \times R_2)$. Los outer joins son una extensión de SQL, no del álgebra vista en clase. |
| 🟡 | [[03 - Superllaves, claves candidatas y clave primaria\|Superllaves, claves candidatas y clave primaria]] | "Superllave: Cualquier combinación de atributos que incluya una clave candidata. Por lo tanto." | La frase quedó cortada. Se propone completarla con la cita siguiente: toda clave candidata es superllave, pero no al revés. |
| ℹ️ | [[05 - Join en álgebra relacional\|Join en álgebra relacional]] | Resultado con una sola columna B | Con la condición explícita `R1.B = R2.B` el resultado tendría `R1.B` y `R2.B`. Una sola columna B corresponde al *natural join*. Se explicó en un complemento; no es un error grave. |
