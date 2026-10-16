---
ramo: "Programación en C"
tema: "Fundamentos del lenguaje"
tags:
  - c
  - tipos
  - printf
  - casting
  - origen/complemento
prerrequisitos:
  - "[[01 - Estructura y compilación de un programa en C]]"
---

# Tipos de datos, printf y casting

En C, el **tipo** de una variable dice dos cosas: **cuántos bytes ocupa** en memoria y **cómo se interpretan** esos bytes. Los mismos 8 bits pueden leerse como el número 72 o como la letra `H`; el tipo es lo que decide. Por eso cada variable tiene una **dirección** (dónde está), un **tipo** (tamaño e interpretación) y un **valor**.

## Tipos básicos

| Tipo | Interpretación | Tamaño típico | En `printf` |
|---|---|---|---|
| `int` | Entero con signo | 4 bytes | `%d` o `%i` |
| `float` | Decimal | 4 bytes | `%f` |
| `double` | Decimal con más precisión | 8 bytes | `%lf` |
| `char` | Un carácter (no un string) | 1 byte | `%c` |

`sizeof(tipo)` entrega el tamaño en bytes y se imprime con `%zu`, porque retorna un tipo propio (`size_t`). Un `char` va entre **comillas simples** (`'h'`); las comillas dobles crean un string, que es otra cosa: un arreglo de `char` terminado en `'\0'`.

`printf` necesita que se le indique cómo interpretar cada valor. Los `%` cumplen el rol de las llaves de un f-string de Python: `print(f"{1} {2} {0.5}")` se escribe `printf("%i %i %f\n", 1, 2, 0.5)`. También se puede fijar la cantidad de decimales: `%.9lf` imprime un `double` con 9 decimales. Además existe `typedef`, que crea un **alias** de un tipo (`typedef int cool_int;`) y que es útil para nombres largos, sobre todo con structs.

## Casting: leer un dato como otro tipo

El tipo de una variable no cambia nunca, pero sí se puede **interpretar** su valor como otro tipo. Eso es el **casting**. Puede ser **implícito**, cuando se asigna a una variable de otro tipo, o **explícito**, cuando se escribe el tipo entre paréntesis.

```c
#include <stdio.h>

int main(void)
{
    double e = 64.79;
    char f = e;           // casting implícito: se trunca a 64
    char g = (char) e;    // casting explícito
    printf("f = %c, g = %c | f = %d, g = %d\n", f, g, f, g);
    // f = @, g = @ | f = 64, g = 64     (64 es '@' en ASCII)

    int x = 5, y = 2;
    double entera = x / y;            // división ENTERA: 2.000000
    double real = (double) x / y;     // 2.500000
    printf("%lf %lf\n", entera, real);
    return 0;
}
```

> [!warning] La división entre enteros trunca
> `5 / 2` vale `2` aunque se guarde en un `double`, porque la división se calcula entre dos `int` **antes** de asignar el resultado. Para obtener 2.5, al menos uno de los operandos tiene que ser decimal: `(double) x / y`.

## De texto a número

Todo lo que llega por consola es texto. `<stdlib.h>` trae `atoi` (*ASCII to int*) y `atof` (*ASCII to float*, que retorna un `double`) para convertirlo:

```c
int n = atoi("100");       // 100
double r = atof("3.56");   // 3.560000 (hay que guardarlo en double, no en int)
```

## Preguntas de repaso

> [!question]- ¿Qué información aporta el tipo de una variable en C, además del "tipo de dato"?
> El tamaño en bytes que ocupa en memoria y la forma de interpretar esos bytes. Por ejemplo, el byte 64 se lee como el número 64 si es `int` y como `'@'` si se imprime como `char`.

> [!question]- ¿Por qué `double c = 5 / 2;` deja `c = 2.0`?
> Porque los dos operandos son `int` y C hace la división entera antes de convertir el resultado a `double`. Basta con castear uno de ellos: `(double) 5 / 2`.

> [!question]- ¿Cuál es la diferencia entre casting implícito y explícito?
> El implícito ocurre solo al asignar un valor a una variable de otro tipo. El explícito se escribe con `(tipo)` delante del valor. El resultado es el mismo; el explícito deja clara la intención.

> [!question]- ¿Por qué no se puede guardar el resultado de `atof("3.56")` en un `int` sin perder información?
> `atof` retorna un decimal. Al asignarlo a un `int` se trunca a 3 y se pierde la parte fraccionaria.
