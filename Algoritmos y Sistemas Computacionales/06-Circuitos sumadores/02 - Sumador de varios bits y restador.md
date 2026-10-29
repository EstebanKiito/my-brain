---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Circuitos sumadores"
tags:
  - algoritmos/circuitos-sumadores
  - algoritmos/binario
  - origen/complemento
prerrequisitos:
  - "[[01 - Medio sumador y sumador completo|Medio sumador y sumador completo]]"
---

# Sumador de varios bits y restador

Un sumador completo resuelve una columna. Para sumar números de varios bits se encadenan varios sumadores completos, pasando el acarreo de una columna a la siguiente. Con la misma estructura, invirtiendo un operando, también se puede restar.

## Sumar dos números de 2 bits

Si $A = A_1A_0$ y $B = B_1B_0$, el resultado puede necesitar 3 bits: $S = S_2S_1S_0$. La columna de la derecha suma $A_0 + B_0$; la de la izquierda suma $A_1 + B_1$ más el acarreo que venga de la derecha.

| $A$ | $B$ | $A + B$ |
|---|---|---|
| 00 | 00 | 000 |
| 01 | 01 | 010 |
| 10 | 10 | 100 |
| 11 | 11 | 110 |

Por ejemplo, $10_2 + 11_2 = 101_2$: se suma la columna de la derecha ($0+1=1$) y la de la izquierda ($1+1=10$), que produce el bit $S_2$.

## El sumador de 4 bits

Para sumar números de 4 bits se conectan cuatro sumadores completos en cadena:

- El sumador de la columna 0 recibe $A_0$, $B_0$ y $C_{in} = 0$.
- Su $C_{out}$ entra como $C_{in}$ del sumador de la columna 1.
- Así hasta la columna 3, cuyo $C_{out}$ es el acarreo final del resultado.

El acarreo "viaja" de derecha a izquierda. Ese recorrido se llama **propagación del acarreo** y es lo que hace que un sumador de muchos bits sea más lento que uno de pocos.

> [!tip] La idea central
> Un sumador de $n$ bits es una cadena de $n$ sumadores completos. Cada uno resuelve una columna y le pasa el acarreo al siguiente.

## Buses

Cuando un circuito maneja varios bits a la vez, el diagrama se simplifica dibujando una sola línea gruesa con un número: el **bus**. Un bus de 4 bits representa cuatro cables en paralelo, uno por bit. Así, un sumador de 4 bits se dibuja como un bloque con entradas de 4 bits y salidas de 4 bits.

## Restar con el mismo sumador

Restar $A - B$ es sumar $A$ con el complemento a dos de $B$. El complemento a dos se obtiene invirtiendo los bits de $B$ y sumando 1. En el circuito, eso se hace con:

- una compuerta NOT en cada bit de $B$;
- el acarreo de entrada $C_{in} = 1$ del primer sumador.

El resultado es $A + (-B)$ y el acarreo final se descarta, tal como en la resta con complemento a dos.

![Restador de 4 bits: se invierten los bits de B y se suma 1 con el acarreo de entrada](adjuntos/Restador%20de%204%20bits.png)

> [!example]- Transcripción de la imagen
> - Entradas $A_3A_2A_1A_0$ y $B_3B_2B_1B_0$.
> - Cada bit de $B$ pasa por una compuerta NOT (los triángulos).
> - El acarreo de entrada del sumador vale 1.
> - El bloque central es un sumador de 4 bits; las salidas son $S_3S_2S_1S_0$ y $C_{out}$.

## Ejemplo: $7 - 3$

En 4 bits, $7 = 0111$ y $3 = 0011$. El complemento a dos de 3 es $1101$.

$$0111 + 1101 = 1\,0100$$

Se descarta el acarreo final y queda $0100_2 = 4$. Correcto.

> [!warning] El acarreo final no siempre es un error
> Al restar con complemento a dos, el acarreo final se descarta. No confundirlo con un desbordamiento: el desbordamiento ocurre cuando el resultado no cabe en los bits disponibles, no cuando sobra un acarreo.

## Preguntas de repaso

> [!question]- ¿Cómo se encadenan dos sumadores completos?
> La salida $C_{out}$ del primero se conecta a la entrada $C_{in}$ del segundo. Así el acarreo de una columna pasa a la siguiente.

> [!question]- ¿Por qué un sumador de 4 bits necesita cuatro sumadores completos?
> Porque cada sumador completo resuelve una columna. Para sumar dos números de 4 bits hay cuatro columnas.

> [!question]- ¿Qué se hace para restar con un sumador?
> Se invierten los bits del sustraendo, se suma 1 (con $C_{in} = 1$) y se suma al minuendo. El acarreo final se descarta.

> [!question]- ¿Qué es un bus en un diagrama de circuitos?
> Una línea que representa varios bits en paralelo. Se anota con el número de bits que transporta.
