---
ramo: "Álgebra Lineal"
tema: "Álgebra de matrices, inversa y LU"
tags:
  - algebra-lineal/matrices
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Teorema de la matriz invertible]]"
---

# Ejercicios de prueba de matrices e inversas

Preguntas de interrogaciones y exámenes anteriores sobre producto de matrices, ecuaciones matriciales e inversas. La regla de oro para despejar: multiplicar por el **mismo lado** en ambos miembros y recordar que la transpuesta y la inversa de un producto **invierten el orden**.

## Ejercicios

### 1. Recuperar una matriz a partir de imágenes
$A\langle 1, 1, 0\rangle = \langle 1, 2, 0\rangle$, $A\langle 0, 0, 1\rangle = \langle -1, 0, 2\rangle$ y $A\langle 0, 1, 0\rangle = \langle 0, 3, 1\rangle$. Determine el tamaño de $A$ y la matriz.

> [!example]- Solución
> Los vectores de entrada están en $\mathbb{R}^3$ y los de salida en $\mathbb{R}^3$, así que $A$ es de $3 \times 3$. Las columnas son $A\mathbf e_j$: $A\mathbf e_3 = \langle -1, 0, 2\rangle$, $A\mathbf e_2 = \langle 0, 3, 1\rangle$ y, por linealidad, $A\mathbf e_1 = A\langle 1, 1, 0\rangle - A\mathbf e_2 = \langle 1, -1, -1\rangle$.
> $$A = \begin{bmatrix} 1 & 0 & -1 \\ -1 & 3 & 0 \\ -1 & 1 & 2 \end{bmatrix}.$$

### 2. V o F: $A - I$ invertible
Si $A$ es de $2 \times 2$ y $A - I$ es invertible, entonces $A^2 = 0$.

> [!example]- Solución
> **Falso.** $A = 2I$ cumple que $A - I = I$ es invertible, pero $A^2 = 4I \neq 0$.

### 3. Ecuación con transpuestas
Encuentre $X$ si $X^T - B^2 = (AB^T - 3X)^T$, con $A = \begin{bmatrix} -1 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & -1 \end{bmatrix}$ y $B = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$.

> [!example]- Solución
> $(AB^T - 3X)^T = BA^T - 3X^T$, así que $X^T - B^2 = BA^T - 3X^T$ y $4X^T = B^2 + BA^T$, es decir, $X = \tfrac14(B^2 + BA^T)^T$. Con $B^2 = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 2 & 1 & 1 \end{bmatrix}$ y $BA^T = \begin{bmatrix} -1 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$ ($A$ es simétrica):
> $$X = \frac14\begin{bmatrix} 0 & 2 & 1 \\ 0 & 1 & 0 \\ 2 & 1 & 1 \end{bmatrix}^T = \begin{bmatrix} 0 & 0 & \frac12 \\ \frac12 & \frac14 & \frac14 \\ \frac14 & 0 & \frac14 \end{bmatrix}.$$

### 4. Despejar con inversas y transpuestas
Con $A$ y $B$ invertibles, despeje $X$ de $(AX^{-1}B)^T = AB$.

> [!example]- Solución
> Transponiendo ambos lados: $AX^{-1}B = (AB)^T = B^TA^T$. A la izquierda por $A^{-1}$ y a la derecha por $B^{-1}$: $X^{-1} = A^{-1}B^TA^TB^{-1}$. Invirtiendo (orden inverso):
> $$X = BA^{-T}B^{-T}A, \qquad\text{con } A^{-T} = (A^{-1})^T = (A^T)^{-1}.$$

### 5. Inversa y un sistema
Sea $A = \begin{bmatrix} -6 & 2 & 1 \\ 0 & -3 & 0 \\ 1 & 0 & 0 \end{bmatrix}$. (a) Calcule $A^{-1}$. (b) Úsela para resolver $A\mathbf x = 3\mathbf e_2$.

> [!example]- Solución
> (a) En $[A \mid I]$: $F_1 \leftrightarrow F_3$, $F_2 \to -\tfrac13F_2$, $F_3 \to F_3 + 6F_1$ y $F_3 \to F_3 - 2F_2$ llevan la izquierda a $I$:
> $$A^{-1} = \begin{bmatrix} 0 & 0 & 1 \\ 0 & -\frac13 & 0 \\ 1 & \frac23 & 6 \end{bmatrix}.$$
> (b) $\mathbf x = A^{-1}(3\mathbf e_2) = 3 \cdot (\text{columna 2 de } A^{-1}) = \langle 0, -1, 2\rangle$.

### 6. Invertibilidad con parámetro y una columna de la inversa
$A = \begin{bmatrix} 1 & 2 & t \\ 0 & t & 1 \\ 1 & 0 & 1 \end{bmatrix}$. (a) ¿Para qué $t$ es invertible? (b) Con $t = 1$, encuentre la tercera columna de $A^{-1}$ sin calcular las otras.

> [!example]- Solución
> (a) $F_3 - F_1$ da $[0\ -2\ \ 1 - t]$. Si $t = 0$, las filas 2 y 3 son $[0\ 0\ 1]$ y $[0\ -2\ 1]$: hay tres pivotes. Si $t \neq 0$, $F_3 + \tfrac2tF_2$ da $[0\ 0\ \ 1 - t + \tfrac2t]$, y $1 - t + \tfrac2t = -\tfrac{(t - 2)(t + 1)}{t}$. Invertible si y solo si $t \neq 2$ y $t \neq -1$.
> (b) Se resuelve $A\mathbf x = \mathbf e_3$ con $t = 1$: $x_1 + 2x_2 + x_3 = 0$, $x_2 + x_3 = 0$ y $x_1 + x_3 = 1$. Sale $\langle \tfrac12, -\tfrac12, \tfrac12\rangle$.

### 7. Parámetro e inversa de $3 \times 3$
$A = \begin{bmatrix} 1 & 0 & 6 \\ -1 & 2 & 0 \\ 0 & 5 & k \end{bmatrix}$. (a) ¿Para qué $k$ es invertible? (b) Calcule $A^{-1}$ con $k = -1$.

> [!example]- Solución
> (a) $F_2 + F_1$ da $[0\ 2\ 6]$ y $F_3 - \tfrac52F_2$ da $[0\ 0\ \ k - 15]$. Invertible si y solo si $k \neq 15$.
> (b) Siguiendo con $[A \mid I]$ hasta la FER:
> $$A^{-1} = \frac{1}{32}\begin{bmatrix} 2 & -30 & 12 \\ 1 & 1 & 6 \\ 5 & 5 & -2 \end{bmatrix}.$$
> Control: la primera fila de $A$ por la primera columna de $A^{-1}$ da $\tfrac{1}{32}(2 + 0 + 30) = 1$.

### 8. V o F: solución única implica invertible
Si $A$ es de $3 \times 3$ y $A\mathbf x = \langle 1, -2, 1\rangle$ tiene solución única, entonces $A$ es invertible.

> [!example]- Solución
> **Verdadero.** Solución única significa que no hay variables libres: las 3 columnas son pivote. Como $A$ es cuadrada, tiene 3 pivotes y, por el teorema de la matriz invertible, es invertible.

## Preguntas de repaso

> [!question]- En el ejercicio 4, ¿por qué no se puede "simplificar" la $A$ de ambos lados al principio?
> Porque en $AX^{-1}B = B^TA^T$ la $A$ está a la izquierda en un lado y a la derecha en el otro. Solo se cancela multiplicando ambos lados por $A^{-1}$ **por el mismo lado**, y eso no elimina la $A^T$ de la derecha.

> [!question]- ¿Qué ventaja tiene el método del ejercicio 6(b) frente a calcular toda la inversa?
> Resuelve un solo sistema en vez de tres. La columna $j$ de $A^{-1}$ es la solución de $A\mathbf x = \mathbf e_j$.

> [!question]- En los ejercicios 6 y 7, ¿por qué alcanza con escalonar para decidir la invertibilidad?
> Porque, por el teorema de la matriz invertible, $A$ es invertible si y solo si tiene $n$ pivotes. Basta ver para qué valores del parámetro se anula el último pivote, separando el caso en que se divide por el parámetro.
