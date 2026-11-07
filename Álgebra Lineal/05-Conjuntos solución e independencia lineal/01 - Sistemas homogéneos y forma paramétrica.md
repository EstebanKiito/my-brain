---
ramo: "Álgebra Lineal"
tema: "Conjuntos solución e independencia lineal"
tags:
  - algebra-lineal/sistemas
  - origen/complemento
prerrequisitos:
  - "[[03 - Existencia y unicidad de soluciones]]"
---

# Sistemas homogéneos y forma paramétrica

Los sistemas cuyo lado derecho es cero son los más simples y, a la vez, los más importantes: describen las relaciones lineales entre las columnas de una matriz y son la "parte variable" de cualquier otro sistema con la misma matriz. Su conjunto solución nunca es vacío y siempre tiene la forma de un **conjunto generado**: un punto, una recta, un plano o algo mayor, siempre pasando por el origen.

## Sistemas homogéneos

> [!tip] Definición
> Un sistema es **homogéneo** si se puede escribir como $A\mathbf x = \mathbf 0$. Siempre tiene al menos la **solución trivial** $\mathbf x = \mathbf 0$. Cualquier otra solución se llama **no trivial**.

Como siempre es consistente, la única pregunta es si la solución trivial es la única.

> [!tip] Teorema
> $A\mathbf x = \mathbf 0$ tiene una solución no trivial si y solo si el sistema tiene **al menos una variable libre**.

Es el teorema de existencia y unicidad aplicado a un sistema que siempre es consistente. Una consecuencia inmediata: si $A$ tiene más columnas que filas, hay más variables que pivotes posibles y **siempre** existen soluciones no triviales.

## Escalonar solo $A$

En un sistema homogéneo, la última columna de la ampliada es de ceros y ninguna operación de fila la cambia. Por eso basta escalonar $A$ y recordar que el lado derecho es cero.

> [!warning] Solo para sistemas homogéneos
> Si $A \sim B$, entonces $A\mathbf x = \mathbf 0$ y $B\mathbf x = \mathbf 0$ tienen las mismas soluciones. Esto **no** vale para $A\mathbf x = \mathbf b$ y $B\mathbf x = \mathbf b$ con $\mathbf b \neq \mathbf 0$: las operaciones que llevan $A$ a $B$ también cambian $\mathbf b$.

## Forma vectorial paramétrica

**Ejemplo.** ¿Tiene soluciones no triviales $\begin{cases} 3x_1 + 5x_2 - 4x_3 = 0 \\ -3x_1 - 2x_2 + 4x_3 = 0 \\ 6x_1 + x_2 - 8x_3 = 0 \end{cases}$?

$$
\begin{bmatrix} 3 & 5 & -4 \\ -3 & -2 & 4 \\ 6 & 1 & -8 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & -\frac43 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}.
$$

$x_3$ es libre, así que sí. Las ecuaciones son $x_1 = \tfrac43x_3$ y $x_2 = 0$. Escribiendo $\mathbf x$ y sacando la variable libre como factor:

$$
\mathbf x = \begin{bmatrix} \tfrac43x_3 \\ 0 \\ x_3 \end{bmatrix} = x_3\begin{bmatrix} \tfrac43 \\ 0 \\ 1 \end{bmatrix}, \qquad \text{es decir, } \{\mathbf x : A\mathbf x = \mathbf 0\} = \operatorname{Gen}\left\{\begin{bmatrix} 4 \\ 0 \\ 3 \end{bmatrix}\right\}.
$$

(Tomar $x_3 = 3t$ elimina la fracción.) Es una recta por el origen.

> [!tip] Las soluciones homogéneas son conjuntos generados
> El conjunto solución de $A\mathbf x = \mathbf 0$ siempre se puede escribir como
> $$\mathbf x = t_1\mathbf u_1 + t_2\mathbf u_2 + \dots + t_k\mathbf u_k = \operatorname{Gen}\{\mathbf u_1, \dots, \mathbf u_k\},$$
> con un vector $\mathbf u_i$ por cada variable libre. Si no hay variables libres, es $\{\mathbf 0\}$.

**Ejemplo con una sola ecuación.** $10x_1 - 3x_2 - 2x_3 = 0$ tiene una básica ($x_1$) y dos libres. De $x_1 = 0{,}3x_2 + 0{,}2x_3$:

$$
\mathbf x = x_2\begin{bmatrix} 0{,}3 \\ 1 \\ 0 \end{bmatrix} + x_3\begin{bmatrix} 0{,}2 \\ 0 \\ 1 \end{bmatrix},
$$

un plano por el origen generado por dos vectores, que es justamente el plano de normal $\langle 10, -3, -2\rangle$.

El procedimiento es siempre el mismo:

1. Llevar $A$ a FER.
2. Despejar las básicas en función de las libres.
3. Escribir $\mathbf x$ y descomponerlo como suma de "variable libre por vector".

> [!warning] Cada vector que sale tiene un $1$ en la posición de su variable libre y $0$ en las otras libres
> Eso garantiza que los vectores obtenidos no sean redundantes entre sí, y sirve como control: si dos vectores de la descomposición son paralelos, hay un error.

## Preguntas de repaso

> [!question]- ¿Por qué un sistema homogéneo de 3 ecuaciones con 4 incógnitas siempre tiene soluciones no triviales?
> Tiene a lo más 3 pivotes para 4 variables, así que queda al menos una variable libre. Como el sistema homogéneo es siempre consistente, hay infinitas soluciones.

> [!question]- Describa en forma paramétrica las soluciones de $x_1 + 2x_2 - x_3 + x_4 = 0$ en $\mathbb{R}^4$.
> $x_1 = -2x_2 + x_3 - x_4$, así que $\mathbf x = x_2\langle -2, 1, 0, 0\rangle + x_3\langle 1, 0, 1, 0\rangle + x_4\langle -1, 0, 0, 1\rangle$: un hiperplano de $\mathbb{R}^4$ generado por tres vectores.

> [!question]- V o F: si $A \sim B$, entonces $A\mathbf x = \mathbf b$ y $B\mathbf x = \mathbf b$ tienen las mismas soluciones.
> Falso. Con $A = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ y $B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ (que se obtiene con $F_2 - F_1$) y $\mathbf b = \langle 1, 0\rangle$: $A x = \mathbf b$ pide $x = 1$ y $x = 0$ (inconsistente), mientras que $Bx = \mathbf b$ da $x = 1$.

> [!question]- ¿Puede el conjunto solución de un sistema homogéneo ser una recta que no pasa por el origen?
> No. $\mathbf 0$ siempre es solución, y el conjunto solución es un conjunto generado, que siempre contiene al origen.
