---
ramo: "Álgebra Lineal"
tema: "Valores propios complejos"
tags:
  - algebra-lineal/valores-propios
  - origen/complemento
prerrequisitos:
  - "[[02 - Ecuación característica y similitud]]"
---

# Números complejos y valores propios complejos

Una rotación de $90°$ no deja ninguna dirección del plano fija: ningún vector no nulo queda sobre su misma recta. Su polinomio característico, $\lambda^2 + 1$, no tiene raíces reales. Para no perder esa información se permiten **valores propios complejos**. Lejos de ser una rareza, son la firma algebraica de las **rotaciones**: una matriz real con valores propios complejos siempre "gira" algo.

## Números complejos (lo necesario)

La **unidad imaginaria** $i$ cumple $i^2 = -1$. Un **número complejo** es $z = a + bi$ con $a, b$ reales: $a = \operatorname{Re} z$ es la **parte real** y $b = \operatorname{Im} z$ la **parte imaginaria**.

| Operación | Regla |
|---|---|
| Suma | $(a + bi) + (c + di) = (a + c) + (b + d)i$ |
| Producto | $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$, usando $i^2 = -1$ |
| Conjugado | $\overline{a + bi} = a - bi$; además $z\bar z = a^2 + b^2$ |
| División | se multiplica arriba y abajo por el conjugado del denominador |
| Módulo | $\lvert z\rvert = \sqrt{a^2 + b^2}$, la distancia de $(a, b)$ al origen |
| Argumento | $\arg z = \varphi$, el ángulo de $(a, b)$ con el eje real positivo |

Así, $z = |z|(\cos\varphi + i\sin\varphi)$: un complejo es un largo y un ángulo. Por ejemplo, $\frac{5}{\frac12 + \frac32i} = \frac{5(\frac12 - \frac32i)}{\frac14 + \frac94} = 1 - 3i$.

## Valores propios complejos

Todo lo anterior funciona con escalares complejos: $\lambda \in \mathbb{C}$ es valor propio de $A$ si $A\mathbf v = \lambda\mathbf v$ para algún $\mathbf v \in \mathbb{C}^n$ no nulo, y se encuentran igual, con $\det(A - \lambda I) = 0$ y $\operatorname{Nul}(A - \lambda I)$.

**Ejemplo (rotación de $90°$).** $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$: $\det(A - \lambda I) = \lambda^2 + 1$, así que $\lambda = \pm i$. Para $\lambda = i$, $A - iI = \begin{bmatrix} -i & -1 \\ 1 & -i \end{bmatrix}$; la primera fila da $x_2 = -ix_1$, y un vector propio es $\langle 1, -i\rangle$. Para $\lambda = -i$, $\langle 1, i\rangle$.

> [!tip] Truco para $2 \times 2$
> Si $\lambda$ es valor propio, $A - \lambda I$ es singular y sus dos filas son proporcionales (en $\mathbb{C}$). Basta usar **una sola fila**: si es $[\alpha\ \ \beta]$, un vector propio es $\langle -\beta, \alpha\rangle$ (o cualquier múltiplo complejo).

**Ejemplo.** $A = \begin{bmatrix} 0{,}5 & -0{,}6 \\ 0{,}75 & 1{,}1 \end{bmatrix}$. $\det(A - \lambda I) = \lambda^2 - 1{,}6\lambda + 1$, y $\lambda = 0{,}8 \pm 0{,}6i$. Para $\lambda = 0{,}8 - 0{,}6i$, la primera fila de $A - \lambda I$ es $[-0{,}3 + 0{,}6i\ \ -0{,}6]$, que da $(-0{,}3 + 0{,}6i)x_1 = 0{,}6x_2$. Con $x_1 = 2$: $x_2 = -1 + 2i$. Vector propio: $\langle 2, -1 + 2i\rangle$.

## Pares conjugados

> [!tip] Propiedad
> Si $A$ es una matriz **real** y $\lambda$ es un valor propio complejo con vector propio $\mathbf v$, entonces $\bar\lambda$ también es valor propio, con vector propio $\bar{\mathbf v}$.

Se ve conjugando $A\mathbf v = \lambda\mathbf v$: como $\bar A = A$, queda $A\bar{\mathbf v} = \bar\lambda\bar{\mathbf v}$. Por eso los valores propios no reales de una matriz real vienen **de a pares**, y basta calcular el vector propio de uno de ellos.

> [!warning] Una matriz real de tamaño impar siempre tiene un valor propio real
> Su polinomio característico tiene coeficientes reales y grado impar, así que tiene al menos una raíz real (las complejas vienen de a pares).

## Preguntas de repaso

> [!question]- ¿Por qué la rotación de $90°$ no tiene valores propios reales, en términos geométricos?
> Porque gira todo vector no nulo en $90°$: ningún $A\mathbf x$ queda sobre la recta de $\mathbf x$, que es lo que exige un vector propio real.

> [!question]- Calcule $(2 - 3i)(1 + i)$ y $|3 - 4i|$.
> $(2 - 3i)(1 + i) = 2 + 2i - 3i - 3i^2 = 5 - i$. $|3 - 4i| = \sqrt{9 + 16} = 5$.

> [!question]- Si $\langle 1, 1 + i\rangle$ es vector propio de una matriz real asociado a $1 - i$, ¿qué otro par valor-vector propio se conoce sin calcular?
> El conjugado: $1 + i$ con vector propio $\langle 1, 1 - i\rangle$.

> [!question]- ¿Puede una matriz real de $3 \times 3$ tener los valores propios $i$, $-i$ y $2i$?
> No. Los no reales vienen en pares conjugados, así que $2i$ exigiría también $-2i$, y serían cuatro valores propios para un polinomio de grado 3. Además debe tener al menos uno real.
