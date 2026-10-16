# Dudas y posibles errores en los apuntes originales — Programación en C (material de IIC2133)

Criterio (ESTANDAR-NOTAS): las erratas se corrigen en la nota sin comentarlas. Aquí solo quedan las dudas reales de contenido y las discrepancias entre apuntes, material de clase y conocimiento general (la nota sigue al material de clase).

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Fundamentos del lenguaje
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[03 - Control de flujo y valores de verdad en C\|Control de flujo y valores de verdad en C]] | CheatSheet: "`<stdbool.h>` hace `typedef int bool`" | Desde C99, `bool` es una macro de `_Bool`, un tipo entero que solo guarda 0 o 1 (`(bool) 17` vale 1, mientras que `(int) 17` vale 17). La nota dice solo que `true` y `false` son 1 y 0. |
| ℹ️ | [[02 - Tipos de datos, printf y casting\|Tipos de datos, printf y casting]] | CheatSheet: `char var[] = '100'; int number = atof(var);` | Las comillas simples son para un solo `char`, así que el string es `"100"`. Además, `atof` retorna `double`, y guardarlo en un `int` trunca el valor. La nota usa la forma correcta. |
