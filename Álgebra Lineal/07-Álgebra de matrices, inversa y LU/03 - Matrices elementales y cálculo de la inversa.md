---
ramo: "Álgebra Lineal"
tema: "Álgebra de matrices, inversa y LU"
tags:
  - algebra-lineal/matrices
  - origen/complemento
prerrequisitos:
  - "[[02 - Inversa de una matriz]]"
  - "[[02 - Algoritmo de reducción por filas]]"
---

# Matrices elementales y cálculo de la inversa

Para matrices de $2 \times 2$ hay fórmula para la inversa; para las demás se usa la reducción por filas. La clave es que **cada operación elemental de fila es una multiplicación por una matriz**. Con eso, escalonar se convierte en un producto de matrices, y de ahí salen el algoritmo para calcular $A^{-1}$ y la posibilidad de escribir una matriz invertible como producto de piezas simples.

## Matrices elementales

> [!tip] Definición
> Una **matriz elemental** es la que se obtiene aplicando **una sola** operación elemental de fila a la identidad.

Con $A = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}$:

| Matriz elemental | Operación sobre $I$ | Efecto de $EA$ |
|---|---|---|
| $E_1 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}$ | $F_3 \to F_3 - 4F_1$ | $\begin{bmatrix} a & b & c \\ d & e & f \\ g - 4a & h - 4b & i - 4c \end{bmatrix}$ |
| $E_2 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ | $F_1 \leftrightarrow F_2$ | $\begin{bmatrix} d & e & f \\ a & b & c \\ g & h & i \end{bmatrix}$ |
| $E_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 5 \end{bmatrix}$ | $F_3 \to 5F_3$ | $\begin{bmatrix} a & b & c \\ d & e & f \\ 5g & 5h & 5i \end{bmatrix}$ |

> [!tip] Propiedad
> Aplicar una operación de fila a una matriz $A$ de $m \times n$ da $EA$, donde $E$ es la matriz de $m \times m$ que resulta de aplicar esa misma operación a $I_m$.

Toda matriz elemental es **invertible**, y su inversa es la elemental de la operación inversa: la inversa de $E_1$ tiene $+4$ donde $E_1$ tiene $-4$; $E_2^{-1} = E_2$; $E_3^{-1}$ tiene $\tfrac15$ en la diagonal.

> [!warning] Por la izquierda, filas; por la derecha, columnas
> $EA$ opera sobre las **filas** de $A$. En cambio, $AE$ aplica la operación sobre las **columnas**. Por ejemplo, sumarle a la columna 2 cinco veces la columna 1 es $A\begin{bmatrix} 1 & 5 \\ 0 & 1 \end{bmatrix}$, con la elemental a la derecha.

## Invertible si y solo si equivalente a la identidad

Si $A$ se reduce a $I$ con operaciones $E_1, \dots, E_k$ (en ese orden), entonces

$$
E_k \cdots E_2E_1A = I .
$$

Multiplicando por las inversas, $A = E_1^{-1}E_2^{-1}\cdots E_k^{-1}$, y además $A^{-1} = E_k\cdots E_1$.

> [!tip] Teorema
> Una matriz $A$ de $n \times n$ es invertible si y solo si es equivalente por filas a $I_n$. En ese caso, la misma sucesión de operaciones que lleva $A$ a $I_n$ lleva $I_n$ a $A^{-1}$.

Consecuencia: **toda matriz invertible es producto de matrices elementales**.

## Algoritmo para calcular $A^{-1}$

> [!tip] Algoritmo
> Escalonar $[\,A \mid I\,]$ hasta la FER.
> - Si la parte izquierda llega a $I$, la derecha es $A^{-1}$: $[\,A \mid I\,] \sim [\,I \mid A^{-1}\,]$.
> - Si en la izquierda aparece una fila de ceros (menos de $n$ pivotes), $A$ no es invertible.

Por qué funciona: buscar $X$ con $AX = I$ es resolver a la vez los $n$ sistemas $A\mathbf x_j = \mathbf e_j$, uno por columna. Se escalonan todos juntos porque comparten la matriz $A$.

**Ejemplo.** $A = \begin{bmatrix} 0 & 1 & 2 \\ 1 & 0 & 3 \\ 4 & -3 & 8 \end{bmatrix}$.

$$
\left[\begin{array}{ccc|ccc} 0 & 1 & 2 & 1 & 0 & 0 \\ 1 & 0 & 3 & 0 & 1 & 0 \\ 4 & -3 & 8 & 0 & 0 & 1 \end{array}\right]
\xrightarrow[F_3 - 4F_1]{F_1 \leftrightarrow F_2}
\left[\begin{array}{ccc|ccc} 1 & 0 & 3 & 0 & 1 & 0 \\ 0 & 1 & 2 & 1 & 0 & 0 \\ 0 & -3 & -4 & 0 & -4 & 1 \end{array}\right]
\xrightarrow[\frac12 F_3]{F_3 + 3F_2}
\left[\begin{array}{ccc|ccc} 1 & 0 & 3 & 0 & 1 & 0 \\ 0 & 1 & 2 & 1 & 0 & 0 \\ 0 & 0 & 1 & \frac32 & -2 & \frac12 \end{array}\right]
$$

Con $F_2 - 2F_3$ y $F_1 - 3F_3$:

$$
A^{-1} = \begin{bmatrix} -\frac92 & 7 & -\frac32 \\ -2 & 4 & -1 \\ \frac32 & -2 & \frac12 \end{bmatrix}.
$$

**Una sola columna de la inversa.** Si solo se pide la columna $j$ de $A^{-1}$, basta resolver $A\mathbf x = \mathbf e_j$, sin calcular el resto.

## Escribir una matriz como producto de elementales

Se escalona $A$ hasta $I$ anotando cada operación. Por ejemplo, $A = \begin{bmatrix} 2 & 3 \\ 1 & 3 \end{bmatrix}$:

1. $F_1 \to \tfrac12F_1$: $\begin{bmatrix} 1 & \frac32 \\ 1 & 3 \end{bmatrix}$, con $E_1 = \begin{bmatrix} \frac12 & 0 \\ 0 & 1 \end{bmatrix}$.
2. $F_2 \to F_2 - F_1$: $\begin{bmatrix} 1 & \frac32 \\ 0 & \frac32 \end{bmatrix}$, con $E_2 = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}$.
3. $F_2 \to \tfrac23F_2$: $\begin{bmatrix} 1 & \frac32 \\ 0 & 1 \end{bmatrix}$, con $E_3 = \begin{bmatrix} 1 & 0 \\ 0 & \frac23 \end{bmatrix}$.
4. $F_1 \to F_1 - \tfrac32F_2$: $I$, con $E_4 = \begin{bmatrix} 1 & -\frac32 \\ 0 & 1 \end{bmatrix}$.

Entonces $A^{-1} = E_4E_3E_2E_1$ y

$$
A = E_1^{-1}E_2^{-1}E_3^{-1}E_4^{-1} = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & \frac32 \end{bmatrix}\begin{bmatrix} 1 & \frac32 \\ 0 & 1 \end{bmatrix}.
$$

La descomposición no es única: otro orden de operaciones da otros factores.

## Preguntas de repaso

> [!question]- ¿Qué matriz elemental de $3 \times 3$ intercambia las filas 2 y 3, y cuál es su inversa?
> $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$, que es su propia inversa: intercambiar dos veces deja todo igual.

> [!question]- Si $E_3E_2E_1A = I$, ¿en qué orden aparecen las inversas al escribir $A$?
> $A = E_1^{-1}E_2^{-1}E_3^{-1}$: se multiplica a la izquierda por $E_3^{-1}$, luego por $E_2^{-1}$ y luego por $E_1^{-1}$, y el orden queda invertido.

> [!question]- ¿Cómo se detecta en el algoritmo $[A \mid I]$ que $A$ no es invertible?
> Si al escalonar la parte izquierda aparece una fila de ceros, $A$ tiene menos de $n$ pivotes y no puede llegar a $I$.

> [!question]- Encuentre la tercera columna de $A^{-1}$ para $A = \begin{bmatrix} 1 & 2 & 1 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{bmatrix}$ sin calcular el resto.
> Se resuelve $A\mathbf x = \mathbf e_3$: $x_1 + 2x_2 + x_3 = 0$, $x_2 + x_3 = 0$ y $x_1 + x_3 = 1$. De la segunda, $x_2 = -x_3$; en la primera, $x_1 = x_3$; en la tercera, $2x_3 = 1$. Columna: $\langle \tfrac12, -\tfrac12, \tfrac12\rangle$.
