---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Operaciones binarias y complemento a dos"
tags:
  - algoritmos/complemento-a-dos
  - algoritmos/aritmetica
  - origen/complemento
prerrequisitos:
  - "[[03 - Complemento a dos|Complemento a dos]]"
---

# Resta y suma con complemento a dos

Restar en binario no necesita un circuito distinto: se calcula el complemento a dos del número que se resta y se suma. Esta idea es la que permite que un procesador use el mismo sumador para la suma y la resta, y explica también cuándo un resultado se desborda.

## Restar es sumar el negativo

Para calcular $A - B$:

1. Se obtiene el complemento a dos de $B$.
2. Se suma $A$ con ese resultado.
3. Se descarta el acarreo final, si lo hay.

> [!tip] La idea central
> $A - B = A + (-B)$. El complemento a dos convierte el negativo en una secuencia de bits que, sumada a $A$, da el resultado correcto.

## Ejemplo: $5 - 3$

En 4 bits, $5 = 0101$ y $3 = 0011$. El complemento a dos de 3 es $1101$ (invertir $0011$ da $1100$, más 1 es $1101$).

```
  0101   (5)
+ 1101   (-3)
------
1 0010   (2, se descarta el acarreo)
```

El resultado es $0010_2 = 2$. Correcto.

## Ejemplo: $3 - 5$

El complemento a dos de 5 es $1011$.

```
  0011   (3)
+ 1011   (-5)
------
  1110   (-2)
```

$1110$ es negativo. Para leer su magnitud: invertir $1110$ da $0001$, sumar 1 da $0010 = 2$. Por lo tanto, el resultado es $-2$. Correcto.

## Ejemplo en 8 bits

Calcular $68 - 1$. En 8 bits, $68 = 01000100$ y $1 = 00000001$. El complemento a dos de 1 es $11111111$.

```
  01000100   (68)
+ 11111111   (-1)
----------
1 01000011   (67, se descarta el acarreo)
```

El resultado es $01000011_2 = 67$.

## Acarreo y desbordamiento

> [!warning] Acarreo no es lo mismo que desbordamiento
> El **acarreo de salida** es el bit que se sale del registro y se descarta; por sí solo no indica un error. El **desbordamiento** (*overflow*) ocurre cuando el resultado no cabe en los bits disponibles y el valor queda mal.
>
> Con sumandos del mismo signo, si el resultado cambia de signo, hubo desbordamiento. Por ejemplo, en 8 bits: $127 + 1 = 01111111 + 00000001 = 10000000$, que se interpreta como $-128$. El resultado correcto (128) no cabe en 8 bits con signo.

## Preguntas de repaso

> [!question]- ¿Cómo se calcula $7 - 2$ con complemento a dos en 4 bits?
> $7 = 0111$; el complemento a dos de 2 ($0010$) es $1110$. La suma $0111 + 1110 = 1\,0101$; se descarta el acarreo y queda $0101 = 5$.

> [!question]- ¿Por qué el acarreo final se descarta?
> Porque el resultado se guarda en una cantidad fija de bits. El acarreo es un bit que queda fuera de ese registro y no forma parte del resultado.

> [!question]- ¿Cómo se detecta un desbordamiento al sumar dos números del mismo signo?
> Si el resultado tiene el signo contrario al de los sumandos, hubo desbordamiento. Por ejemplo, positivo + positivo = negativo.

> [!question]- ¿Qué ventaja tiene usar complemento a dos para restar?
> Que no hace falta un circuito restador: con el mismo sumador y el complemento a dos del sustraendo se obtiene la resta.
