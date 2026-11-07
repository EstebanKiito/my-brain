---
ramo: "Álgebra Lineal"
tema: "Determinantes"
tags:
  - algebra-lineal/determinantes
  - origen/complemento
prerrequisitos:
  - "[[02 - Propiedades de los determinantes]]"
---

# Regla de Cramer y fórmula de la inversa

Los determinantes permiten escribir **fórmulas cerradas** para la solución de un sistema cuadrado y para la inversa. No son el método más eficiente para calcular (escalonar es más rápido), pero son útiles cuando hay parámetros, cuando se pide una sola incógnita o una sola columna de la inversa, y en razonamientos teóricos.

## Regla de Cramer

Para $A$ de $n \times n$ y $\mathbf b \in \mathbb{R}^n$, sea $A_i(\mathbf b)$ la matriz que resulta de **reemplazar la columna $i$ de $A$ por $\mathbf b$**:

$$
A_i(\mathbf b) = [\,\mathbf a_1\ \cdots\ \mathbf b\ \cdots\ \mathbf a_n\,] .
$$

> [!tip] Teorema (regla de Cramer)
> Si $A$ es invertible, la única solución de $A\mathbf x = \mathbf b$ tiene componentes
> $$x_i = \frac{\det A_i(\mathbf b)}{\det A}, \qquad i = 1, \dots, n.$$

**Por qué funciona.** Si $A\mathbf x = \mathbf b$, entonces $A \cdot I_i(\mathbf x) = A_i(\mathbf b)$, donde $I_i(\mathbf x)$ es la identidad con su columna $i$ reemplazada por $\mathbf x$ (multiplicar $A$ por $\mathbf e_j$ da $\mathbf a_j$, y por $\mathbf x$ da $\mathbf b$). Desarrollando por la fila $i$, $\det I_i(\mathbf x) = x_i$. Por multiplicatividad, $\det A \cdot x_i = \det A_i(\mathbf b)$.

**Ejemplo.** $3x_1 - 2x_2 = 6$, $-5x_1 + 4x_2 = 8$. Con $\det A = 12 - 10 = 2$:

$$
x_1 = \frac{\begin{vmatrix} 6 & -2 \\ 8 & 4 \end{vmatrix}}{2} = \frac{40}{2} = 20, \qquad x_2 = \frac{\begin{vmatrix} 3 & 6 \\ -5 & 8 \end{vmatrix}}{2} = \frac{54}{2} = 27 .
$$

**Ejemplo con parámetro.** $3sx_1 - 2x_2 = 4$, $-6x_1 + sx_2 = 1$. $\det A = 3s^2 - 12 = 3(s - 2)(s + 2)$, así que hay solución única si y solo si $s \neq \pm 2$, y entonces

$$
x_1 = \frac{\begin{vmatrix} 4 & -2 \\ 1 & s \end{vmatrix}}{3(s^2 - 4)} = \frac{4s + 2}{3(s^2 - 4)}, \qquad x_2 = \frac{\begin{vmatrix} 3s & 4 \\ -6 & 1 \end{vmatrix}}{3(s^2 - 4)} = \frac{s + 8}{s^2 - 4}.
$$

Aquí Cramer luce: escalonar con el parámetro $s$ obligaría a dividir por expresiones con $s$.

## Matriz adjunta y fórmula de la inversa

La columna $j$ de $A^{-1}$ resuelve $A\mathbf x = \mathbf e_j$. Aplicando Cramer, su entrada $i$ es $\frac{\det A_i(\mathbf e_j)}{\det A}$, y desarrollando por la columna $i$ (donde está $\mathbf e_j$), $\det A_i(\mathbf e_j) = (-1)^{i+j}\det A_{ji} = C_{ji}$. Por eso aparecen los cofactores **transpuestos**.

> [!tip] Definición y teorema
> La **adjunta** de $A$, $\operatorname{adj} A$, es la **transpuesta de la matriz de cofactores**: su entrada $(i, j)$ es $C_{ji}$. Si $A$ es invertible,
> $$A^{-1} = \frac{1}{\det A}\operatorname{adj} A .$$

**Ejemplo.** $A = \begin{bmatrix} 2 & 1 & 3 \\ 1 & -1 & 1 \\ 1 & 4 & -2 \end{bmatrix}$ tiene cofactores $C_{11} = -2$, $C_{12} = 3$, $C_{13} = 5$, $C_{21} = 14$, $C_{22} = -7$, $C_{23} = -7$, $C_{31} = 4$, $C_{32} = 1$, $C_{33} = -3$. Desarrollando por la primera fila, $\det A = 2(-2) + 1(3) + 3(5) = 14$. Ubicando $C_{ij}$ en la posición $(j, i)$:

$$
A^{-1} = \frac{1}{14}\begin{bmatrix} -2 & 14 & 4 \\ 3 & -7 & 1 \\ 5 & -7 & -3 \end{bmatrix}.
$$

Para $2 \times 2$ se recupera la fórmula conocida: $\operatorname{adj}\begin{bmatrix} a & b \\ c & d \end{bmatrix} = \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$.

> [!tip] Determinante de la adjunta
> De $A\operatorname{adj}(A) = (\det A)I$ se obtiene, tomando determinantes, $\det A \cdot \det(\operatorname{adj} A) = (\det A)^n$, es decir,
> $$\det(\operatorname{adj} A) = (\det A)^{n - 1}$$
> si $A$ es invertible de $n \times n$.

> [!warning] Transponer los cofactores
> El error más común es poner $C_{ij}$ en la posición $(i, j)$. La adjunta lleva $C_{ij}$ en la posición $(j, i)$. Se controla multiplicando una fila de $A$ por una columna de la supuesta inversa.

## Cuándo conviene

Para matrices grandes, Cramer es muy ineficiente: cada determinante cuesta lo mismo que resolver el sistema escalonando, y Cramer necesita $n + 1$ de ellos. Conviene en sistemas de $2 \times 2$ o $3 \times 3$, con parámetros, o cuando se pide **una sola** incógnita o **una sola** columna de la inversa.

## Preguntas de repaso

> [!question]- Resuelva $4x + y = 6$, $5x + 2y = 7$ con Cramer.
> $\det A = 3$, $\det A_1 = \begin{vmatrix} 6 & 1 \\ 7 & 2 \end{vmatrix} = 5$ y $\det A_2 = \begin{vmatrix} 4 & 6 \\ 5 & 7 \end{vmatrix} = -2$. Entonces $x = \tfrac53$, $y = -\tfrac23$.

> [!question]- ¿Por qué Cramer exige que $A$ sea invertible?
> Porque divide por $\det A$. Si $\det A = 0$, el sistema tiene ninguna o infinitas soluciones y no hay una fórmula para "la" solución.

> [!question]- $A$ es de $4 \times 4$ con $\det A = 3$. ¿Cuánto vale $\det(\operatorname{adj} A)$?
> $(\det A)^{4 - 1} = 27$.

> [!question]- ¿Qué entrada de $A^{-1}$ da el cofactor $C_{23}$, dividido por $\det A$?
> La entrada $(3, 2)$, por la transposición de la adjunta.
