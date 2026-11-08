---
ramo: "Álgebra Lineal"
tema: "Matrices simétricas y formas cuadráticas"
tags:
  - algebra-lineal/valores-propios
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Formas cuadráticas]]"
---

# Ejercicios de prueba de matrices simétricas y formas cuadráticas

Preguntas de exámenes anteriores. Casi siempre piden clasificar una forma y eliminar el término cruzado: matriz simétrica (con la mitad del término cruzado), valores propios, vectores propios **normalizados** y $Q = \lambda_1y_1^2 + \lambda_2y_2^2$.

## Ejercicios

### 1. Diagonalización ortogonal a partir de datos
$A$ es simétrica de $3 \times 3$, $A\langle 1, 1, 1\rangle = \langle 2, 2, 2\rangle$ y $\operatorname{Nul} A = \operatorname{Gen}\{\langle 1, 1, -2\rangle, \langle 1, -2, 1\rangle, \langle 2, -1, -1\rangle\}$. Encuentre $P$ ortogonal y $D$ diagonal con $A = PDP^T$.

> [!example]- Solución
> $\langle 1, 1, 1\rangle$ es vector propio con $\lambda = 2$. El tercer generador del núcleo es la suma de los dos primeros, así que $E_0 = \operatorname{Nul} A$ tiene dimensión 2, con base $\{\langle 1, 1, -2\rangle, \langle 1, -2, 1\rangle\}$. Gram-Schmidt: $\langle 1, -2, 1\rangle - \tfrac{-3}{6}\langle 1, 1, -2\rangle = \langle \tfrac32, -\tfrac32, 0\rangle$, o $\langle 1, -1, 0\rangle$. Normalizando:
> $$P = \begin{bmatrix} \frac{1}{\sqrt3} & \frac{1}{\sqrt6} & \frac{1}{\sqrt2} \\ \frac{1}{\sqrt3} & \frac{1}{\sqrt6} & -\frac{1}{\sqrt2} \\ \frac{1}{\sqrt3} & -\frac{2}{\sqrt6} & 0 \end{bmatrix}, \qquad D = \operatorname{diag}(2, 0, 0).$$
> (De hecho $A = \tfrac23\begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$.)

### 2. Elipse sin término cruzado
$Q = 5x_1^2 - 4x_1x_2 + 5x_2^2$. (a) Diagonalice ortogonalmente su matriz. (b) Elimine el término cruzado y explique por qué $Q$ es definida positiva.

> [!example]- Solución
> (a) $A = \begin{bmatrix} 5 & -2 \\ -2 & 5 \end{bmatrix}$, con $\lambda = 3$ ($\langle 1, 1\rangle$) y $\lambda = 7$ ($\langle 1, -1\rangle$). $P = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$ y $D = \operatorname{diag}(3, 7)$.
> (b) Con $\mathbf x = P\mathbf y$: $Q = 3y_1^2 + 7y_2^2$, positiva para todo $\mathbf y \neq \mathbf 0$ porque ambos coeficientes son positivos.

### 3. Una forma definida negativa
$Q = -5x_1^2 + 4x_1x_2 - 2x_2^2$. Clasifíquela y elimine el término cruzado.

> [!example]- Solución
> $A = \begin{bmatrix} -5 & 2 \\ 2 & -2 \end{bmatrix}$: $\det(A - \lambda I) = \lambda^2 + 7\lambda + 6 = (\lambda + 1)(\lambda + 6)$. Ambos negativos: **definida negativa**. Vectores: $\lambda = -1$, $\langle 1, 2\rangle$; $\lambda = -6$, $\langle 2, -1\rangle$. Con $P = \frac{1}{\sqrt5}\begin{bmatrix} 1 & 2 \\ 2 & -1 \end{bmatrix}$: $Q = -y_1^2 - 6y_2^2$.

### 4. Una forma en tres variables
$Q = 2x_1^2 + 2x_2^2 + 4x_3^2 + 2x_1x_2$. Clasifíquela y elimine los términos cruzados.

> [!example]- Solución
> $A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 4 \end{bmatrix}$ es diagonal por bloques: el bloque $\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$ tiene valores 3 ($\langle 1, 1\rangle$) y 1 ($\langle 1, -1\rangle$), y queda el 4 con $\mathbf e_3$. Todos positivos: **definida positiva**. Con
> $$P = \begin{bmatrix} \frac{1}{\sqrt2} & \frac{1}{\sqrt2} & 0 \\ \frac{1}{\sqrt2} & -\frac{1}{\sqrt2} & 0 \\ 0 & 0 & 1 \end{bmatrix}, \qquad Q = 3y_1^2 + y_2^2 + 4y_3^2 .$$

### 5. Una forma semidefinida
$Q = x^2 - 6xy + 9y^2$. Clasifíquela y elimine el término cruzado.

> [!example]- Solución
> $A = \begin{bmatrix} 1 & -3 \\ -3 & 9 \end{bmatrix}$ con $\det A = 0$ y traza 10: valores 0 y 10. **Semidefinida positiva** (es $(x - 3y)^2$). Vectores: $\lambda = 0$, $\langle 3, 1\rangle$; $\lambda = 10$, $\langle 1, -3\rangle$. Con $P = \frac{1}{\sqrt{10}}\begin{bmatrix} 3 & 1 \\ 1 & -3 \end{bmatrix}$: $Q = 10y_2^2$.

### 6. Parámetro para que sea definida positiva
¿Para qué $a$ es definida positiva $Q = x_1^2 + 2ax_1x_2 + x_2^2$?

> [!example]- Solución
> $A = \begin{bmatrix} 1 & a \\ a & 1 \end{bmatrix}$ tiene valores propios $1 + a$ y $1 - a$ (vectores $\langle 1, 1\rangle$ y $\langle 1, -1\rangle$). Ambos positivos si y solo si $-1 < a < 1$. (Equivalente: $\det A = 1 - a^2 > 0$ con $a_{11} = 1 > 0$.)

### 7. Tres V o F
(a) Si $A$ es simétrica y $A^2$ es definida positiva, $A$ es definida positiva. (b) Si $a, b > 0$, la forma $(a + 1)x_1^2 + 2ax_1x_2 + (a + b)x_2^2$ alcanza su mínimo absoluto en $\mathbf 0$. (c) Si $a > 1$, $\begin{bmatrix} a & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & 1 \end{bmatrix}$ es definida positiva.

> [!example]- Solución
> (a) **Falso**: $A = -I$.
> (b) **Verdadero.** $M = \begin{bmatrix} a + 1 & a \\ a & a + b \end{bmatrix}$ tiene $a + 1 > 0$ y $\det M = (a + 1)(a + b) - a^2 = ab + a + b > 0$: definida positiva. Entonces $Q(\mathbf x) > 0 = Q(\mathbf 0)$ para todo $\mathbf x \neq \mathbf 0$.
> (c) **Verdadero.** Los menores principales superiores son $a > 0$, $a^2 - 1 > 0$ y $\det = (a - 1)^2 > 0$ para $a > 1$, así que es definida positiva.

## Preguntas de repaso

> [!question]- En el ejercicio 1, ¿por qué no hizo falta ortogonalizar $\langle 1, 1, 1\rangle$ con los vectores del núcleo?
> Porque pertenece a otro espacio propio ($\lambda = 2$), y en una matriz simétrica los espacios propios distintos son ortogonales.

> [!question]- ¿Qué control rápido sirve para verificar los valores propios de una matriz de $2 \times 2$?
> La suma debe ser la traza y el producto el determinante.

> [!question]- ¿Por qué hay que **normalizar** los vectores propios para el cambio de variable?
> Para que $P$ sea ortogonal y $P^{-1} = P^T$. Así $P^TAP = D$ y la nueva forma no tiene términos cruzados; con vectores sin normalizar, $P^TAP$ quedaría diagonal pero con otros coeficientes.
