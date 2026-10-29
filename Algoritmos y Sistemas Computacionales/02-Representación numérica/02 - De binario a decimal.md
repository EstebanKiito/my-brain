---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Representación numérica"
tags:
  - algoritmos/binario
  - algoritmos/conversiones
  - origen/complemento
prerrequisitos:
  - "[[01 - Bits y sistemas posicionales|Bits y sistemas posicionales]]"
---

# De binario a decimal

Convertir un número binario a decimal es sumar las potencias de 2 que marcan sus bits en 1. Es la operación inversa de escribir un número en base 2 y la base de casi todo lo que viene después: complemento a dos, hexadecimal y operaciones aritméticas.

## El método

Se numera la posición de cada bit de derecha a izquierda, empezando en 0. El bit de la posición $k$ aporta $s_k \times 2^k$, donde $s_k$ es 0 o 1. El valor decimal es la suma de todos los aportes:

$$\sum_{k=0}^{n-1} s_k \times 2^k$$

> [!tip] Regla práctica
> Escribe encima de cada bit las potencias de 2 —1, 2, 4, 8, 16, 32…— y suma solo las que tienen un 1 debajo. El bit de la derecha siempre vale 1 ($2^0$), no 2.

## Ejemplo paso a paso

Convertir $(100110101)_2$ a decimal. Primero se etiquetan las posiciones de derecha a izquierda:

| Posición | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bit | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
| Potencia | $2^8$ | $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| Aporte | 256 | 0 | 0 | 32 | 16 | 0 | 4 | 0 | 1 |

Los bits en 1 están en las posiciones 8, 5, 4, 2 y 0:

$$1 \times 2^8 + 1 \times 2^5 + 1 \times 2^4 + 1 \times 2^2 + 1 \times 2^0 = 256 + 32 + 16 + 4 + 1 = 309$$

Por lo tanto, $(100110101)_2 = 309_{10}$.

## Más ejemplos

| Binario | Potencias que se suman | Decimal |
|---|---|---:|
| $1101_2$ | $8 + 4 + 1$ | 13 |
| $1011011_2$ | $64 + 16 + 8 + 2 + 1$ | 91 |
| $101010_2$ | $32 + 8 + 2$ | 42 |

Para comprobar, se puede hacer el camino inverso: 13 en binario es 1101, 91 es 1011011 y 42 es 101010.

> [!warning] Los errores típicos
> - Empezar a contar las posiciones en 1 en vez de 0: el bit de la derecha vale 1, no 2.
> - Olvidar que un 0 también ocupa una posición: en 101, el 0 del medio es $2^1$, no $2^0$.
> - Sumar todas las potencias en vez de solo las que tienen un 1.

## Preguntas de repaso

> [!question]- ¿Cuál es el valor decimal de $1011_2$?
> $8 + 2 + 1 = 11$. Los bits en 1 están en las posiciones 3, 1 y 0.

> [!question]- ¿Por qué el bit de la derecha vale 1 y no 2?
> Porque su posición es 0 y $2^0 = 1$. La posición 1 vale $2^1 = 2$.

> [!question]- ¿Cómo se convierte rápido un binario que tiene un solo 1?
> Es una potencia de 2: si el 1 está en la posición $k$, el valor es $2^k$. Por ejemplo, $10000_2 = 2^4 = 16$.

> [!question]- ¿Qué relación tiene este método con la definición de sistema posicional?
> Es la misma definición aplicada a base 2: cada bit se multiplica por la potencia de la base según su posición y se suman los resultados.
