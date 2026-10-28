---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Circuitos sumadores"
tags:
  - algoritmos/comparadores
  - algoritmos/circuitos-logicos
  - origen/complemento
prerrequisitos:
  - "[[02 - Sumador de varios bits y restador|Sumador de varios bits y restador]]"
---

# Comparadores y enabler

Además de sumar, un computador necesita comparar números y decidir si deja pasar una señal. El **comparador** dice si un número es mayor, menor o igual que otro; el **enabler** (habilitador) permite encender o apagar una salida según una señal de control.

## Comparador de 1 bit

Un comparador de 1 bit recibe $A$ y $B$ y entrega tres salidas:

- $A > B = A \land \neg B$: es 1 solo cuando $A = 1$ y $B = 0$.
- $A < B = \neg A \land B$: es 1 solo cuando $A = 0$ y $B = 1$.
- $A = B = \neg(A \oplus B)$: es 1 cuando ambos son iguales.

| $A$ | $B$ | $A > B$ | $A = B$ | $A < B$ |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 0 |

## Comparador de 2 bits

Para comparar $A = A_1A_0$ con $B = B_1B_0$ se compara primero el bit más significativo. $A$ es mayor que $B$ si:

- $A_1 > B_1$, o
- $A_1 = B_1$ y $A_0 > B_0$.

En álgebra booleana:

$$A > B = (A_1 \land \neg B_1) \lor \big((A_1 = B_1) \land (A_0 \land \neg B_0)\big)$$

La idea se repite para $A < B$ y $A = B$, y se puede extender a cualquier cantidad de bits comparando de izquierda a derecha.

> [!tip] La idea central
> Se compara desde el bit más significativo hacia la derecha. El primer bit distinto decide; si son iguales, se mira el siguiente.

## Enabler

Un **enabler** es un componente que deja pasar una señal solo cuando una entrada de control $E$ está en 1. Su comportamiento es:

| $E$ | $A_0$ | $A_0'$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Es decir, $A_0' = E \land A_0$. Se implementa con una compuerta AND entre la señal y el control.

Para varias señales se usa un enabler de varios bits: un AND por cada bit, todos controlados por la misma señal $E$. Así se habilita o deshabilita un bus completo.

> [!warning] Deshabilitar no es lo mismo que borrar
> Cuando $E = 0$, la salida del enabler es 0, pero la señal de entrada sigue existiendo. El enabler solo decide si esa señal pasa o no; no modifica el valor original.

## Preguntas de repaso

> [!question]- ¿Cómo se expresa $A > B$ en un comparador de 1 bit?
> Como $A \land \neg B$: $A$ debe ser 1 y $B$ debe ser 0.

> [!question]- ¿Qué se compara primero en un comparador de 2 bits?
> El bit más significativo ($A_1$ con $B_1$). Si son distintos, ese bit decide; si son iguales, se compara el siguiente.

> [!question]- ¿Qué hace un enabler cuando $E = 1$?
> Deja pasar la señal de entrada: la salida es igual a la entrada. Cuando $E = 0$, la salida es 0.

> [!question]- ¿Cómo se implementa un enabler de 1 bit?
> Con una compuerta AND entre la entrada $A_0$ y la señal de control $E$: $A_0' = E \land A_0$.
