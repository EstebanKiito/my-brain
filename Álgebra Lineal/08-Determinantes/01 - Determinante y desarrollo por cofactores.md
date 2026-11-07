---
ramo: "Álgebra Lineal"
tema: "Determinantes"
tags:
  - algebra-lineal/determinantes
  - origen/complemento
prerrequisitos:
  - "[[02 - Inversa de una matriz]]"
---

# Determinante y desarrollo por cofactores

Para una matriz de $2 \times 2$, un solo número, $ad - bc$, dice si es invertible. El **determinante** generaliza ese número a matrices de $n \times n$: es cero exactamente cuando la matriz no es invertible, mide cómo una transformación cambia áreas y volúmenes, y permite escribir fórmulas cerradas para la inversa y para las soluciones de un sistema. Esta nota da su definición y la forma de calcularlo con cofactores.

## Motivación

Al escalonar una matriz genérica $A = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}$ suponiendo $a \neq 0$, el último pivote resulta proporcional a

$$
\Delta = a(ei - fh) - b(di - fg) + c(dh - eg),
$$

y $A$ es invertible si y solo si $\Delta \neq 0$. Cada paréntesis es el determinante $2 \times 2$ que queda al borrar la fila 1 y la columna del coeficiente. Esa estructura recursiva es la definición general.

## Definición

Para $A$ cuadrada, $A_{ij}$ denota la **submatriz** que se obtiene borrando la fila $i$ y la columna $j$. Por ejemplo, en $A = \begin{bmatrix} 1 & -2 & 5 & 0 \\ 2 & 0 & 4 & -1 \\ 3 & 1 & 0 & 7 \\ 0 & 4 & -2 & 0 \end{bmatrix}$, borrando la fila 3 y la columna 2 queda $A_{32} = \begin{bmatrix} 1 & 5 & 0 \\ 2 & 4 & -1 \\ 0 & -2 & 0 \end{bmatrix}$.

> [!tip] Definición
> Para $n = 1$, $\det[a_{11}] = a_{11}$. Para $n \geq 2$,
> $$\det A = a_{11}\det A_{11} - a_{12}\det A_{12} + \dots + (-1)^{1+n}a_{1n}\det A_{1n} = \sum_{j=1}^{n}(-1)^{1+j}a_{1j}\det A_{1j}.$$
> El número $C_{ij} = (-1)^{i+j}\det A_{ij}$ es el **cofactor** $(i, j)$, y la fórmula queda $\det A = a_{11}C_{11} + \dots + a_{1n}C_{1n}$.

También se escribe $|A|$ en vez de $\det A$. Para $n = 2$ se recupera $ad - bc$.

**Ejemplo.** $\det\begin{bmatrix} 1 & 5 & 0 \\ 2 & 4 & -1 \\ 0 & -2 & 0 \end{bmatrix} = 1\begin{vmatrix} 4 & -1 \\ -2 & 0 \end{vmatrix} - 5\begin{vmatrix} 2 & -1 \\ 0 & 0 \end{vmatrix} + 0 = 1(-2) - 5(0) = -2$.

## Cualquier fila o columna

> [!tip] Teorema (desarrollo por cofactores)
> El determinante se puede calcular desarrollando por **cualquier fila** $i$ o **cualquier columna** $j$:
> $$\det A = a_{i1}C_{i1} + \dots + a_{in}C_{in} = a_{1j}C_{1j} + \dots + a_{nj}C_{nj}.$$

Los signos $(-1)^{i+j}$ forman un tablero de ajedrez que empieza con $+$ en la esquina:

$$
\begin{bmatrix} + & - & + & \cdots \\ - & + & - & \\ + & - & + & \\ \vdots & & & \ddots \end{bmatrix}
$$

La libertad de elegir se usa para ir por la fila o columna con **más ceros**. En el ejemplo anterior, la fila 3 solo tiene una entrada no nula: $\det A = (-2)C_{32} = (-2)(-1)^{3+2}\begin{vmatrix} 1 & 0 \\ 2 & -1 \end{vmatrix} = (-2)(-1)(-1) = -2$.

**Ejemplo con muchos ceros.**

$$
\det\begin{bmatrix} 3 & -7 & 8 & 9 & -6 \\ 0 & 2 & -5 & 7 & 3 \\ 0 & 0 & 1 & 5 & 0 \\ 0 & 0 & 2 & 4 & -1 \\ 0 & 0 & 0 & -2 & 0 \end{bmatrix}
= 3\begin{vmatrix} 2 & -5 & 7 & 3 \\ 0 & 1 & 5 & 0 \\ 0 & 2 & 4 & -1 \\ 0 & 0 & -2 & 0 \end{vmatrix}
= 3 \cdot 2\begin{vmatrix} 1 & 5 & 0 \\ 2 & 4 & -1 \\ 0 & -2 & 0 \end{vmatrix} = 6 \cdot (-2) = -12 .
$$

Dos veces se desarrolló por la primera columna, que solo tenía una entrada no nula (en la posición $(1, 1)$, con signo $+$). El último determinante es el del ejemplo anterior. Con 25 cofactores posibles, el cálculo se redujo a dos pasos.

## Matrices triangulares

> [!tip] Teorema
> Si $A$ es triangular (superior o inferior), $\det A$ es el **producto de las entradas de la diagonal**.

Se ve desarrollando una y otra vez por la primera columna (o fila), que solo tiene una entrada no nula. En particular, $\det I = 1$.

> [!warning] El costo del desarrollo por cofactores
> Desarrollar por cofactores una matriz de $n \times n$ cuesta del orden de $n!$ multiplicaciones. Para $n = 25$ eso son unos $10^{25}$ productos: medio millón de años a un billón por segundo. Para matrices sin ceros, el método eficiente es escalonar (siguiente nota), que cuesta del orden de $n^3$.

## Preguntas de repaso

> [!question]- Calcule $\begin{vmatrix} 2 & 0 & 0 \\ 7 & -1 & 0 \\ 3 & 5 & 4 \end{vmatrix}$.
> Es triangular inferior: $2 \cdot (-1) \cdot 4 = -8$.

> [!question]- ¿Qué signo lleva el cofactor $C_{23}$ y por qué?
> $(-1)^{2+3} = -1$, negativo. En el tablero de signos, las posiciones con $i + j$ impar llevan $-$.

> [!question]- ¿Por qué conviene desarrollar por la fila o columna con más ceros?
> Porque cada entrada nula anula su término: no hay que calcular el determinante de esa submatriz. Con una sola entrada no nula, el determinante de $n \times n$ se reduce a uno solo de $(n - 1) \times (n - 1)$.

> [!question]- Si una matriz tiene una fila de ceros, ¿cuánto vale su determinante?
> Cero: desarrollando por esa fila, todos los términos son $0 \cdot C_{ij}$.
