---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Circuitos sumadores"
tags:
  - algoritmos/circuitos-sumadores
  - algoritmos/circuitos-logicos
  - origen/complemento
prerrequisitos:
  - "[[04 - Álgebra booleana y simplificación|Álgebra booleana y simplificación]]"
---

# Medio sumador y sumador completo

Sumar dos bits es la operación aritmética más pequeña que puede hacer un circuito. El **medio sumador** resuelve el caso de dos bits sin acarreo de entrada; el **sumador completo** agrega una entrada más para recibir el acarreo de la columna anterior y así poder encadenarse.

## Medio sumador

El medio sumador recibe dos bits, $A$ y $B$, y entrega dos salidas:

- **Suma** $S = A \oplus B$: es 1 cuando exactamente una entrada es 1.
- **Acarreo** $C = A \land B$: es 1 solo cuando ambas entradas son 1.

| $A$ | $B$ | $S$ | $C$ |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

> [!tip] La idea central
> La suma de dos bits se parece a la suma decimal: $0+0=0$, $0+1=1$, $1+0=1$ y $1+1=10_2$. El bit menos significativo es $S$ y el acarreo es $C$.

> [!warning] El medio sumador no basta para sumar números largos
> No tiene entrada de acarreo, así que no puede recibir el "1 que se lleva" de la columna anterior. Para encadenar varias columnas hace falta el sumador completo.

## Sumador completo

El sumador completo recibe tres bits: $A$, $B$ y $C_{in}$ (el acarreo que viene de la columna anterior). Entrega la suma y el acarreo de salida:

$$S = A \oplus B \oplus C_{in}$$

$$C_{out} = (A \land B) \lor \big(C_{in} \land (A \oplus B)\big)$$

| $A$ | $B$ | $C_{in}$ | $S$ | $C_{out}$ |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

La salida $C_{out}$ es 1 cuando al menos dos de las tres entradas son 1: esa es la condición para que la suma de la columna supere 1 y haya que llevar un bit a la siguiente.

## Ejemplo: $1 + 1$

Con un medio sumador, $A = 1$ y $B = 1$:

- $S = 1 \oplus 1 = 0$.
- $C = 1 \land 1 = 1$.

El resultado es $10_2$: suma 0 y acarreo 1. Es la misma regla de la suma binaria.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre el medio sumador y el sumador completo?
> El medio sumador suma dos bits y no recibe acarreo. El sumador completo recibe además $C_{in}$, el acarreo de la columna anterior, y por eso se puede encadenar.

> [!question]- ¿Por qué la suma del medio sumador es un XOR?
> Porque el XOR entrega 1 cuando exactamente una entrada es 1, que es justo el bit de suma de $0+1$ y $1+0$. En $1+1$ la suma es 0 y el 1 se va al acarreo.

> [!question]- ¿Cuándo se activa $C_{out}$ en un sumador completo?
> Cuando al menos dos de las tres entradas ($A$, $B$, $C_{in}$) son 1. En ese caso la suma de la columna es 2 o más y hay que llevar un bit.

> [!question]- ¿Cuántas filas tiene la tabla de verdad de un sumador completo?
> Ocho, porque tiene tres entradas: $2^3 = 8$ combinaciones.
