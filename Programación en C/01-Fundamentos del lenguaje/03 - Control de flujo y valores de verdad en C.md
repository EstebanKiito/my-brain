---
ramo: "Programación en C"
tema: "Fundamentos del lenguaje"
tags:
  - c
  - control-de-flujo
  - booleanos
  - origen/complemento
prerrequisitos:
  - "[[02 - Tipos de datos, printf y casting]]"
---

# Control de flujo y valores de verdad en C

Las estructuras de control de C (`if`, `while`, `for`, `switch`) son las mismas que en cualquier lenguaje. Lo que cambia es **cómo se delimitan los bloques** y **qué cuenta como verdadero**. Ahí es donde aparecen los errores de quien viene de Python.

## Bloques: llaves y punto y coma, no indentación

En Python, la indentación define qué líneas pertenecen a un `if` o a una función. En C, la indentación **no significa nada** para el compilador: los bloques se arman con `{ }` y cada instrucción termina en `;`. Un código mal indentado compila igual, así que el orden visual depende solo de quien lo escribe.

## Valores de verdad

En C no existen `True` y `False` como tipo base. Cualquier valor se puede usar como condición: **0 es falso y todo lo demás es verdadero**. La biblioteca `<stdbool.h>` agrega el tipo `bool` y las constantes `true` (1) y `false` (0), que en el fondo siguen siendo números.

| Operador | Significado | Ejemplo con `p = 17`, `q = false` |
|---|---|---|
| `\|\|` | o lógico | `p \|\| q` → 1 |
| `&&` | y lógico | `p && q` → 0 |
| `!` | negación | `!p` → 0 |

## Las estructuras

```c
#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int n = 12, count = 0;
    for (int i = 1; i <= n; i += 1)        // for (INIT; COND; STEP)
    {
        if (n % i == 0) count += 1;        // cuenta divisores
    }
    printf("%d tiene %d divisores\n", n, count);   // 12 tiene 6 divisores

    for (int i = 0; i < 3; i += 1)
        for (int j = 0; j < 3; j += 1)
        {
            if (i == j) continue;          // salta los pares iguales
            printf("(%d,%d) ", i, j);
        }
    printf("\n");

    char jugada = 'X';
    switch (jugada)                        // evita una cadena larga de if-else
    {
        case 'O': printf("Vas segundo\n"); break;
        case 'X': printf("Vas primero\n"); break;
        default:  printf("Así no se juega\n"); break;
    }
    if (0) printf("nunca se imprime\n");   // 0 es falso
    return 0;
}
```

- **`for (INIT; COND; STEP)`** es un `while` con pasos extra: `INIT` se ejecuta una vez (declarando el tipo de la variable), `COND` se revisa antes de cada iteración y `STEP` se ejecuta al final de cada una.
- **`continue`** salta a la siguiente iteración y **`break`** sale del ciclo. Ojo: `break` solo sale del ciclo **más interno** en que está, no de todos.
- **`switch`** compara una variable con un conjunto pequeño de valores. Cada `case` debe terminar en `break`; si no, la ejecución "cae" al caso siguiente. Hay un [video del curso sobre `switch`](https://www.loom.com/share/103192e770524abc8b6b83446949f167).

> [!warning] Asignar en vez de comparar
> `if (x = 5)` no compara: asigna 5 a `x`, y como 5 es distinto de 0, la condición siempre es verdadera. La comparación es `==`. Compilar con `-Wall` hace que `gcc` avise.

## Preguntas de repaso

> [!question]- ¿Qué imprime `if (-3) printf("si");` y por qué?
> Imprime "si", porque en C cualquier valor distinto de 0 es verdadero, incluidos los negativos.

> [!question]- ¿Qué pasa si se omite el `break` de un `case` en un `switch`?
> La ejecución sigue con las instrucciones del `case` siguiente (*fall-through*), aunque su valor no coincida, hasta encontrar un `break` o el final del `switch`.

> [!question]- En dos `for` anidados, ¿de cuál sale un `break` escrito en el interno?
> Solo del `for` interno. El externo continúa con su siguiente iteración.

> [!question]- ¿Por qué en C la indentación no cambia el significado del código?
> Porque el compilador delimita los bloques con `{ }` y las instrucciones con `;`. La indentación solo ayuda a quien lee.
