---
ramo: "Álgebra Lineal"
tema: "Álgebra de matrices, inversa y LU"
tags:
  - algebra-lineal/factorizaciones
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Factorización LU]]"
---

# Ejercicios de prueba de matrices elementales y LU

Preguntas de interrogaciones y exámenes anteriores sobre matrices elementales, la factorización $LU$ y su variante $PA = LU$. Es un tema mecánico, pero con trampas de orden y de signo que aparecen siempre.

## Ejercicios

### 1. V o F: operaciones por columnas
Si $B$ resulta de sumarle a la segunda columna de $A$ ($2 \times 2$) cinco veces la primera, entonces $\begin{bmatrix} 1 & 5 \\ 0 & 1 \end{bmatrix}B = A$.

> [!example]- Solución
> **Falso.** Las operaciones por columnas se hacen multiplicando **por la derecha**: $B = A\begin{bmatrix} 1 & 5 \\ 0 & 1 \end{bmatrix}$. Con $A = I$, $B = \begin{bmatrix} 1 & 5 \\ 0 & 1 \end{bmatrix}$ y $\begin{bmatrix} 1 & 5 \\ 0 & 1 \end{bmatrix}B = \begin{bmatrix} 1 & 10 \\ 0 & 1 \end{bmatrix} \neq A$.

### 2. Inversa y matriz como productos de elementales
Se sabe que $E_3E_2E_1A = I_3$ con $E_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -\frac14 \end{bmatrix}$, $E_2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}$ y $E_1 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$. Sin calcular: (a) ¿por qué $A$ es invertible? (b) Escriba $A^{-1}$ y (c) $A$ como productos de elementales.

> [!example]- Solución
> (a) $A$ se reduce a $I$ con operaciones elementales, así que es invertible (también: $E_3E_2E_1$ es una inversa por la izquierda de una matriz cuadrada).
> (b) $A^{-1} = E_3E_2E_1$.
> (c) $A = E_1^{-1}E_2^{-1}E_3^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -4 \end{bmatrix}$.

### 3. La inversa como producto de elementales
Escriba la inversa de $A = \begin{bmatrix} -6 & 2 & 1 \\ 0 & -3 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ como producto de matrices elementales.

> [!example]- Solución
> Se reduce $A$ a $I$ anotando las operaciones: $F_1 \leftrightarrow F_3$, luego $F_2 \to -\tfrac13F_2$, luego $F_3 \to F_3 + 6F_1$ (queda $[0\ 2\ 1]$) y por último $F_3 \to F_3 - 2F_2$. Con las elementales en orden de aplicación de derecha a izquierda:
> $$A^{-1} = \underbrace{\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -2 & 1 \end{bmatrix}}_{F_3 - 2F_2}\underbrace{\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 6 & 0 & 1 \end{bmatrix}}_{F_3 + 6F_1}\underbrace{\begin{bmatrix} 1 & 0 & 0 \\ 0 & -\frac13 & 0 \\ 0 & 0 & 1 \end{bmatrix}}_{-\frac13F_2}\underbrace{\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}}_{F_1 \leftrightarrow F_3}.$$

### 4. LU de una matriz de $4 \times 4$
Factorice $A = \begin{bmatrix} 3 & -7 & -2 & 2 \\ -3 & 5 & 1 & 0 \\ 6 & -4 & 0 & -5 \\ -9 & 5 & -5 & 12 \end{bmatrix}$ como $LU$.

> [!example]- Solución
> Columna 1 (pivote 3): multiplicadores $\ell_{21} = -1$, $\ell_{31} = 2$, $\ell_{41} = -3$. Quedan las filas $[0\ -2\ -1\ 2]$, $[0\ 10\ 4\ -9]$ y $[0\ -16\ -11\ 18]$.
> Columna 2 (pivote $-2$): $\ell_{32} = -5$ y $\ell_{42} = 8$. Quedan $[0\ 0\ -1\ 1]$ y $[0\ 0\ -3\ 2]$.
> Columna 3 (pivote $-1$): $\ell_{43} = 3$. Queda $[0\ 0\ 0\ -1]$.
> $$L = \begin{bmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 2 & -5 & 1 & 0 \\ -3 & 8 & 3 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} 3 & -7 & -2 & 2 \\ 0 & -2 & -1 & 2 \\ 0 & 0 & -1 & 1 \\ 0 & 0 & 0 & -1 \end{bmatrix}.$$

### 5. LU de una matriz rectangular
$A = \begin{bmatrix} 1 & -1 & 0 & 1 \\ 1 & 2 & 2 & 3 \\ 0 & 1 & -1 & 2 \end{bmatrix}$. (a) Encuentre su $LU$. (b) Encuentre $B$ escalonada y $C$ triangular inferior con $B = CA$.

> [!example]- Solución
> (a) $\ell_{21} = 1$ deja $[0\ 3\ 2\ 2]$; $\ell_{31} = 0$; $\ell_{32} = \tfrac13$ deja $[0\ 0\ -\tfrac53\ \tfrac43]$.
> $$L = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & \frac13 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} 1 & -1 & 0 & 1 \\ 0 & 3 & 2 & 2 \\ 0 & 0 & -\frac53 & \frac43 \end{bmatrix}.$$
> (b) De $A = LU$ sale $L^{-1}A = U$: $B = U$ y $C = L^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ \frac13 & -\frac13 & 1 \end{bmatrix}$.

### 6. Dos V o F sobre LU
(a) Si $[a_1]$ y $\begin{bmatrix} a_1 & a_2 \\ a_4 & a_5 \end{bmatrix}$ son invertibles, $A = \begin{bmatrix} a_1 & a_2 & a_3 \\ a_4 & a_5 & a_6 \\ a_7 & a_8 & a_9 \end{bmatrix}$ tiene LU. (b) Si $A = LU$ con $L = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 3 & 1 \end{bmatrix}$, la primera entrada de la tercera fila de $A$ es cero.

> [!example]- Solución
> (a) **Verdadero.** $a_1 \neq 0$ es el primer pivote. Después de eliminar, el segundo pivote es $a_5 - \tfrac{a_4}{a_1}a_2 = \tfrac{a_1a_5 - a_2a_4}{a_1} \neq 0$. No hace falta intercambiar filas para los dos primeros pivotes, y el tercero no necesita intercambio (o la fila queda en ceros). Solo se usan reemplazos hacia abajo.
> (b) **Verdadero.** $a_{31} = \ell_{31}u_{11} + \ell_{32}u_{21} + \ell_{33}u_{31} = 0 + 3 \cdot 0 + 1 \cdot 0 = 0$, porque $U$ es escalonada.

### 7. $PA = LU$ a partir de las elementales
Al aplicar a $A$ las operaciones $E_1 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, luego $E_2 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -\frac12 & 0 & 1 \end{bmatrix}$ y luego $E_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & \frac12 & 1 \end{bmatrix}$ se obtiene $U = \begin{bmatrix} 2 & 3 & 2 \\ 0 & 1 & -1 \\ 0 & 0 & -\frac52 \end{bmatrix}$. Encuentre la factorización $PA = LU$.

> [!example]- Solución
> $E_3E_2(E_1A) = U$. $E_1$ es un intercambio, así que $P = E_1$, y $PA = (E_3E_2)^{-1}U = E_2^{-1}E_3^{-1}U$:
> $$L = E_2^{-1}E_3^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ \frac12 & -\frac12 & 1 \end{bmatrix}.$$
> Las inversas cambian el signo de los multiplicadores y se colocan en su lugar.

### 8. Resolver con $PA = LU$
Con $P = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}$, $L = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & -1 & 1 \end{bmatrix}$, $U = \begin{bmatrix} 1 & 1 & 1 \\ 0 & -1 & 1 \\ 0 & 0 & 2 \end{bmatrix}$ y $PA = LU$, resuelva $A\mathbf x = \mathbf e_2$.

> [!example]- Solución
> Multiplicando por $P$: $LU\mathbf x = P\mathbf e_2$, y $P\mathbf e_2$ es la segunda columna de $P$, o sea $\mathbf e_1$.
> - $L\mathbf y = \mathbf e_1$: $y_1 = 1$, $y_2 = 0$, $y_3 = -2y_1 + y_2 = -2$.
> - $U\mathbf x = \mathbf y$: $2x_3 = -2$, así que $x_3 = -1$; $-x_2 + x_3 = 0$, así que $x_2 = -1$; $x_1 + x_2 + x_3 = 1$, así que $x_1 = 3$.
>
> $\mathbf x = \langle 3, -1, -1\rangle$.

## Preguntas de repaso

> [!question]- En el ejercicio 7, ¿por qué el intercambio va en $P$ y no en $L$?
> Porque $L$ debe ser triangular inferior con unos en la diagonal, y una permutación no lo es. Se aplica primero a $A$ (reordenando filas) y el resto de la reducción ya no necesita intercambios.

> [!question]- ¿Cuál es el error más frecuente al armar $L$ y cómo se evita?
> Poner los multiplicadores con el signo cambiado. Si la operación es $F_i \to F_i - \ell F_j$, en $L$ va $+\ell$. Se controla multiplicando $LU$ y comparando con $A$.

> [!question]- ¿En qué orden se escriben las elementales para obtener $A^{-1}$?
> De derecha a izquierda en el orden en que se aplicaron: la primera operación queda pegada a la derecha. Para $A$ se usan las inversas en el orden opuesto.
