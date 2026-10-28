---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Representación numérica"
tags:
  - algoritmos/bits
  - algoritmos/sistemas-numericos
  - origen/complemento
prerrequisitos:
  - "[[03 - Arquitectura de un computador|Arquitectura de un computador]]"
---

# Bits y sistemas posicionales

El computador no guarda números como los escribimos nosotros: guarda **bits**, cada uno con dos valores posibles, 0 o 1. Esta nota explica por qué basta con dos valores, cómo se forman números con ellos y qué significa que un sistema numérico sea **posicional**.

## Qué es un bit

Un **bit** es la unidad mínima de información: puede valer 0 o 1. Esa dualidad es cómoda porque muchos fenómenos físicos tienen dos estados fáciles de distinguir:

- un agujero en una tarjeta perforada (hay o no hay),
- un voltaje alto o bajo en un circuito,
- un campo magnético en un sentido u otro,
- presencia o ausencia de una señal.

> [!tip] La idea central
> Un bit no "significa" nada por sí solo: es un valor que se interpreta según el contexto. La misma secuencia de bits puede representar un número, una letra o una instrucción.

## Por qué binario y no decimal

Los humanos usamos diez dígitos (0 al 9) porque contamos con los dedos. El computador podría usar diez niveles de voltaje, pero sería difícil distinguirlos con precisión: el ruido haría que 7,9 se confundiera con 8. Con solo dos niveles (alto/bajo) la distinción es mucho más robusta.

> [!warning] Más bits, no más dígitos
> Para representar números más grandes no se inventan dígitos nuevos: se agregan **posiciones**. Con $n$ bits se pueden representar $2^n$ combinaciones distintas.

## Sistemas posicionales

En un sistema **posicional**, el valor de un dígito depende de la posición que ocupa. En base 10, el número 13425 es una abreviatura de:

$$13425 = 1 \times 10^4 + 3 \times 10^3 + 4 \times 10^2 + 2 \times 10^1 + 5 \times 10^0$$

La posición de la derecha vale $10^0 = 1$; la siguiente, $10^1 = 10$; la siguiente, $10^2 = 100$, y así. Cuando los dígitos se acaban (después del 9), se agrega una posición nueva.

En base 2 pasa exactamente lo mismo, pero con dos dígitos y potencias de 2:

$$101010_2 = 1 \times 2^5 + 0 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 0 \times 2^0$$

El subíndice indica la base: $101010_2$ es binario; si no se escribe nada, se asume decimal.

## La misma idea, dos bases

| Decimal | Binario | Descomposición binaria |
|---:|---:|---|
| 0 | 0 | $0 \times 2^0$ |
| 1 | 1 | $1 \times 2^0$ |
| 2 | 10 | $1 \times 2^1 + 0 \times 2^0$ |
| 3 | 11 | $1 \times 2^1 + 1 \times 2^0$ |
| 4 | 100 | $1 \times 2^2$ |
| 5 | 101 | $1 \times 2^2 + 1 \times 2^0$ |
| 8 | 1000 | $1 \times 2^3$ |
| 10 | 1010 | $1 \times 2^3 + 1 \times 2^1$ |
| 15 | 1111 | $1 \times 2^3 + 1 \times 2^2 + 1 \times 2^1 + 1 \times 2^0$ |
| 16 | 10000 | $1 \times 2^4$ |

> [!example]- Cómo leer la tabla
> La columna binaria tiene un 1 en las posiciones que se suman y un 0 en las que no. Por ejemplo, 5 se escribe 101 porque $5 = 4 + 1 = 2^2 + 2^0$. Para 10 se usa $8 + 2 = 2^3 + 2^1$, que es 1010.

## Preguntas de repaso

> [!question]- ¿Por qué un computador usa base 2 y no base 10?
> Porque distinguir dos estados físicos (voltaje alto/bajo, hay/no hay señal) es mucho más robusto que distinguir diez niveles, que el ruido podría confundir.

> [!question]- ¿Qué significa que un sistema numérico sea posicional?
> Que el valor de cada dígito depende de su posición. En base 10, el 3 de 13425 vale 3000; en binario, el 1 de 100 vale 4.

> [!question]- ¿Cuántos valores distintos se pueden representar con 4 bits?
> $2^4 = 16$ valores, desde 0000 hasta 1111 (0 a 15 en decimal).

> [!question]- ¿El número 10 binario es igual al número 10 decimal?
> No. $10_2 = 2_{10}$. El subíndice o el contexto indican la base; sin subíndice se asume decimal.
