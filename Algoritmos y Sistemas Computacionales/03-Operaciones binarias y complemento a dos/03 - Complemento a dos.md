---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Operaciones binarias y complemento a dos"
tags:
  - algoritmos/complemento-a-dos
  - algoritmos/binario
  - origen/complemento
prerrequisitos:
  - "[[02 - Representación de números negativos|Representación de números negativos]]"
---

# Complemento a dos

El **complemento a dos** es la regla que permite escribir un número negativo en binario: se invierten todos los bits y se suma 1. Esta nota muestra cómo aplicarla, cómo comprobar el resultado y hasta qué números se pueden representar con una cantidad fija de bits.

## La regla

Para obtener el negativo de un número binario de $n$ bits:

1. Se invierten todos los bits (0 pasa a 1 y 1 pasa a 0). Eso es el complemento de uno.
2. Se suma 1 al resultado.

> [!tip] La idea central
> El complemento a dos convierte la resta en una suma. Para calcular $A - B$ se suma $A$ con el complemento a dos de $B$, y el acarreo final se descarta.

## Ejemplos en 4 bits

Representar $-5$:

$$5 = 0101_2 \rightarrow \text{invertir} \rightarrow 1010_2 \rightarrow +1 \rightarrow 1011_2$$

Entonces $-5 = 1011_2$ en 4 bits.

Representar $-3$:

$$3 = 0011_2 \rightarrow \text{invertir} \rightarrow 1100_2 \rightarrow +1 \rightarrow 1101_2$$

Entonces $-3 = 1101_2$ en 4 bits.

## Ejemplo en 8 bits

Representar $-10$:

$$10 = 00001010_2 \rightarrow \text{invertir} \rightarrow 11110101_2 \rightarrow +1 \rightarrow 11110110_2$$

Entonces $-10 = 11110110_2$ en 8 bits.

La comprobación es sumar el positivo y el negativo:

```
  00001010   (10)
+ 11110110   (-10)
-----------
1 00000000   (0, se descarta el acarreo)
```

El resultado es 0, como corresponde.

## Rango de valores

Con $n$ bits en complemento a dos se pueden representar los enteros desde $-2^{n-1}$ hasta $2^{n-1} - 1$:

| Bits | Rango |
|---:|---|
| 4 | $-8$ a $7$ |
| 8 | $-128$ a $127$ |
| 16 | $-32768$ a $32767$ |

> [!warning] El caso límite de $-128$
> En 8 bits, $128 = 10000000_2$. Al invertir y sumar 1 se obtiene $10000000_2$ otra vez, que se interpreta como $-128$. Por eso $-128$ sí se puede representar, pero $+128$ no: el rango positivo llega solo hasta 127.

## Cómo leer un número negativo

Si el bit de la izquierda es 1, el número es negativo. Para saber su valor se aplica el mismo procedimiento: invertir los bits y sumar 1, y el resultado es la magnitud.

Por ejemplo, $1110_2$ en 4 bits: invertir da $0001$, sumar 1 da $0010 = 2$, así que $1110_2 = -2$.

## Preguntas de repaso

> [!question]- ¿Cuál es el complemento a dos de $0110$ en 4 bits?
> Se invierte a $1001$ y se suma 1: $1010$. Ese es $-6$ en 4 bits.

> [!question]- ¿Por qué se descarta el acarreo final al sumar un positivo y su negativo?
> Porque el resultado correcto es 0 y el acarreo representa un bit que está fuera de los $n$ bits disponibles. Al descartarlo queda $0000$.

> [!question]- ¿Cuántos números distintos se pueden representar con 8 bits en complemento a dos?
> $2^8 = 256$: 128 negativos (de $-128$ a $-1$), el cero y 127 positivos (de 1 a 127).

> [!question]- ¿Cómo se sabe si un número de 8 bits es negativo?
> Mirando el bit más significativo (el de la izquierda): si es 1, el número es negativo; si es 0, es positivo o cero.
