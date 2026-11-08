---
ramo: "Álgebra Lineal"
tema: "Determinantes"
tags:
  - algebra-lineal/determinantes
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Propiedades de los determinantes]]"
---

# Ejercicios de prueba de cálculo de determinantes

Preguntas de interrogaciones y exámenes anteriores donde hay que calcular un determinante, casi siempre con un parámetro, para decidir invertibilidad. La estrategia que más rinde: usar reemplazos de fila o columna para crear ceros o una matriz triangular, y factorizar el resultado.

## Ejercicios

### 1. Cofactores con parámetro
Calcule por cofactores el determinante de $A = \begin{bmatrix} \alpha & 2 & 1 \\ 2\alpha & \alpha + 5 & 4 \\ \alpha & 2 & \alpha \end{bmatrix}$ y diga para qué $\alpha$ es invertible.

> [!example]- Solución
> Por la primera fila:
> $$\det A = \alpha\big[(\alpha + 5)\alpha - 8\big] - 2\big[2\alpha^2 - 4\alpha\big] + 1\big[4\alpha - (\alpha + 5)\alpha\big] = \alpha^3 - \alpha .$$
> $\det A = \alpha(\alpha - 1)(\alpha + 1)$: invertible si y solo si $\alpha \notin \{-1, 0, 1\}$.

### 2. Otro $3 \times 3$ con parámetro
Calcule $\det B$ con $B = \begin{bmatrix} k & k & 0 \\ k^2 & 2 & k \\ 0 & k & k \end{bmatrix}$ y diga cuándo es invertible.

> [!example]- Solución
> Por la primera fila: $k(2k - k^2) - k(k^3 - 0) = 2k^2 - k^3 - k^4 = -k^2(k^2 + k - 2) = -k^2(k + 2)(k - 1)$. Invertible si y solo si $k \notin \{-2, 0, 1\}$.

### 3. Restar columnas adyacentes
Calcule $\det A$ para $A = \begin{bmatrix} a & a & a & a \\ 2 & a & a & a \\ 3 & 2 & a & a \\ 4 & 3 & 2 & a \end{bmatrix}$.

> [!example]- Solución
> Con $C_4 \to C_4 - C_3$, luego $C_3 \to C_3 - C_2$ y luego $C_2 \to C_2 - C_1$ (en ese orden, para usar siempre columnas originales), que no cambian el determinante:
> $$\det A = \begin{vmatrix} a & 0 & 0 & 0 \\ 2 & a - 2 & 0 & 0 \\ 3 & -1 & a - 2 & 0 \\ 4 & -1 & -1 & a - 2 \end{vmatrix} = a(a - 2)^3 .$$
> Invertible si y solo si $a \neq 0$ y $a \neq 2$.

### 4. Matriz de $4 \times 4$ casi triangular
¿Para qué $a$ es invertible $A = \begin{bmatrix} a & 2a & 0 & 0 \\ 0 & 1 & 0 & 3a - 1 \\ 0 & 1 & a - 1 & 2a - 1 \\ a & 2a & 0 & a \end{bmatrix}$?

> [!example]- Solución
> $F_4 - F_1$ da $[0\ 0\ 0\ a]$ y $F_3 - F_2$ da $[0\ 0\ \ a - 1\ \ -a]$. Queda triangular superior con diagonal $a, 1, a - 1, a$: $\det A = a^2(a - 1)$. Invertible si y solo si $a \neq 0$ y $a \neq 1$.

### 5. Vandermonde
Demuestre que $\begin{vmatrix} 1 & x & x^2 \\ 1 & y & y^2 \\ 1 & z & z^2 \end{vmatrix} = (y - x)(z - x)(z - y)$.

> [!example]- Solución
> $F_3 \to F_3 - F_2$ y $F_2 \to F_2 - F_1$ dejan la primera columna $\langle 1, 0, 0\rangle$:
> $$\begin{vmatrix} 1 & x & x^2 \\ 0 & y - x & y^2 - x^2 \\ 0 & z - y & z^2 - y^2 \end{vmatrix} = \begin{vmatrix} y - x & (y - x)(y + x) \\ z - y & (z - y)(z + y) \end{vmatrix} = (y - x)(z - y)\begin{vmatrix} 1 & y + x \\ 1 & z + y \end{vmatrix},$$
> sacando factores comunes de cada fila. El último determinante es $(z + y) - (y + x) = z - x$.

### 6. V o F: un determinante de $n \times n$
Para todo $n \geq 2$,
$$\det\begin{bmatrix} 1 & 0 & \cdots & 0 & 1 \\ 0 & \frac12 & \cdots & 0 & 1 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \cdots & \frac{1}{n-1} & 1 \\ 1 & 1 & \cdots & 1 & \frac1n \end{bmatrix} = \frac{1}{(n-1)!}\left(\frac1n - \frac{(n - 1)n}{2}\right).$$

> [!example]- Solución
> **Verdadero.** Para anular la última fila bajo la diagonal se hace $F_n \to F_n - F_1 - 2F_2 - \dots - (n - 1)F_{n-1}$ (la fila $k$ tiene $\tfrac1k$ en la diagonal, así que se resta $k$ veces). Solo cambia la última entrada: $\tfrac1n - (1 + 2 + \dots + (n - 1)) = \tfrac1n - \tfrac{(n-1)n}{2}$. La matriz queda triangular y el determinante es $1 \cdot \tfrac12 \cdots \tfrac{1}{n-1}$ por esa entrada.

### 7. V o F: invertible para $k > 0$
Si $k > 0$, $\begin{bmatrix} k^2 & 4 & 1 \\ k & -2 & -1 \\ 1 & 1 & 1 \end{bmatrix}$ es invertible.

> [!example]- Solución
> **Verdadero.** El determinante es $k^2(-2 + 1) - 4(k + 1) + (k + 2) = -k^2 - 3k - 2 = -(k + 1)(k + 2)$. Sus raíces son $-1$ y $-2$, negativas, así que no se anula para $k > 0$.

### 8. Determinante de un producto
$A = BU$ con $B = \begin{bmatrix} -1 & 1 & 0 & 0 \\ 2 & 0 & -1 & 0 \\ 1 & -1 & 3 & 2 \\ -\frac12 & 0 & 0 & 0 \end{bmatrix}$ y $U = \begin{bmatrix} \frac19 & 0 & -1 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 3 & -8 \\ 0 & 0 & 0 & \frac17 \end{bmatrix}$. Calcule $\det(3A)$.

> [!example]- Solución
> $U$ es triangular: $\det U = \tfrac19 \cdot 1 \cdot 3 \cdot \tfrac17 = \tfrac{1}{21}$. Para $B$ se desarrolla por la fila 4 (solo $-\tfrac12$ en la posición $(4, 1)$, signo $-$): $\det B = -(-\tfrac12)\begin{vmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ -1 & 3 & 2 \end{vmatrix} = \tfrac12(-2) = -1$. Como $A$ es de $4 \times 4$:
> $$\det(3A) = 3^4\det B\det U = 81 \cdot (-1) \cdot \tfrac{1}{21} = -\tfrac{27}{7}.$$

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 3 el orden de las restas de columnas importa?
> Porque cada reemplazo debe usar una columna todavía no modificada para que el resultado sea el planeado. Empezando por la derecha, $C_4 - C_3$ usa la $C_3$ original, después $C_3 - C_2$ usa la $C_2$ original, y así.

> [!question]- ¿Qué ventaja tiene factorizar el determinante en vez de expandirlo como polinomio?
> Que las raíces se leen directamente: los valores del parámetro que hacen la matriz no invertible son los ceros de cada factor.

> [!question]- En el ejercicio 8, ¿por qué el 3 queda elevado a la cuarta?
> Porque $3A$ multiplica por 3 cada una de las 4 filas, y cada fila escalada multiplica el determinante por 3.
