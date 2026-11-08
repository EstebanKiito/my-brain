---
ramo: "Álgebra Lineal"
tema: "Matrices simétricas y formas cuadráticas"
tags:
  - algebra-lineal/valores-propios
  - origen/complemento
prerrequisitos:
  - "[[01 - Matrices simétricas y teorema espectral]]"
---

# Formas cuadráticas

Una **forma cuadrática** es un polinomio en varias variables donde todos los términos tienen grado 2, como $5x_1^2 + 3x_2^2 - x_1x_2$. Aparecen en energía, optimización (el criterio de la segunda derivada en varias variables) y en las ecuaciones de las cónicas. Los términos cruzados $x_1x_2$ son los que complican; el teorema espectral permite **eliminarlos** con un cambio de variables ortogonal, y el signo de los valores propios dice si la forma es siempre positiva, siempre negativa o mixta.

## Matriz de una forma cuadrática

> [!tip] Teorema
> Toda forma cuadrática se escribe como $Q(\mathbf x) = \mathbf x^TA\mathbf x$ con $A$ **simétrica**, la **matriz de la forma**. Los coeficientes de $x_i^2$ van en la diagonal y el coeficiente de $x_ix_j$ se **reparte por mitades** entre las posiciones $(i, j)$ y $(j, i)$.

- $\mathbf x^T\begin{bmatrix} 4 & 0 \\ 0 & 3 \end{bmatrix}\mathbf x = 4x_1^2 + 3x_2^2$.
- $\mathbf x^T\begin{bmatrix} 3 & -2 \\ -2 & 7 \end{bmatrix}\mathbf x = 3x_1^2 - 4x_1x_2 + 7x_2^2$.
- $Q = 5x_1^2 + 3x_2^2 + 2x_3^2 - x_1x_2 + 8x_2x_3$ tiene matriz $\begin{bmatrix} 5 & -\frac12 & 0 \\ -\frac12 & 3 & 4 \\ 0 & 4 & 2 \end{bmatrix}$.

> [!warning] La mitad del término cruzado
> En $-4x_1x_2$ van $-2$ en cada posición fuera de la diagonal, no $-4$. Es el error más común; se controla expandiendo $\mathbf x^TA\mathbf x$.

## Cambio de variable y ejes principales

Con $\mathbf x = P\mathbf y$ ($P$ invertible), $\mathbf x^TA\mathbf x = \mathbf y^T(P^TAP)\mathbf y$. Si $A = PDP^T$ con $P$ ortogonal, $P^TAP = D$:

> [!tip] Teorema de los ejes principales
> Si $A$ es simétrica, el cambio de variable ortogonal $\mathbf x = P\mathbf y$, con $A = PDP^T$, transforma $\mathbf x^TA\mathbf x$ en
> $$\mathbf y^TD\mathbf y = \lambda_1y_1^2 + \dots + \lambda_ny_n^2,$$
> **sin términos cruzados**. Las columnas de $P$ se llaman **ejes principales**.

**Ejemplo.** $Q = x_1^2 - 8x_1x_2 - 5x_2^2$ tiene $A = \begin{bmatrix} 1 & -4 \\ -4 & -5 \end{bmatrix}$, con valores propios $3$ y $-7$ y vectores $\langle 2, -1\rangle$ y $\langle 1, 2\rangle$. Con $P = \frac{1}{\sqrt5}\begin{bmatrix} 2 & 1 \\ -1 & 2 \end{bmatrix}$ queda $Q = 3y_1^2 - 7y_2^2$. Comprobación con $\mathbf x = \langle 2, -2\rangle$: $Q(\mathbf x) = 4 + 32 - 20 = 16$; $\mathbf y = P^T\mathbf x = \langle \tfrac{6}{\sqrt5}, -\tfrac{2}{\sqrt5}\rangle$ y $3 \cdot \tfrac{36}{5} - 7 \cdot \tfrac45 = 16$.

**Cónicas.** En dos variables, $Q(\mathbf x) = c$ suele ser una elipse o una hipérbola. En los ejes principales queda en posición estándar. Por ejemplo, $5x_1^2 - 4x_1x_2 + 5x_2^2 = 48$ tiene valores propios 3 y 7, con ejes en las direcciones $\langle 1, 1\rangle$ y $\langle -1, 1\rangle$: en las nuevas variables es $3y_1^2 + 7y_2^2 = 48$, una elipse girada $45°$.

![Elipse e hipérbola en posición estándar](adjuntos/Elipse%20e%20hip%C3%A9rbola%20en%20posici%C3%B3n%20est%C3%A1ndar.png)

> [!example]- Transcripción de la imagen
> Izquierda: la elipse $\frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} = 1$ con $a > b > 0$, de semiejes $a$ y $b$ sobre los ejes. Derecha: la hipérbola $\frac{x_1^2}{a^2} - \frac{x_2^2}{b^2} = 1$, con sus asíntotas punteadas. Ambas están en posición estándar: sin término cruzado.

![Cónicas con ejes rotados](adjuntos/C%C3%B3nicas%20con%20ejes%20rotados.png)

> [!example]- Transcripción de la imagen
> (a) La elipse $5x_1^2 - 4x_1x_2 + 5x_2^2 = 48$, girada, con los nuevos ejes $y_1$ e $y_2$ a $45°$. (b) La hipérbola $x_1^2 - 8x_1x_2 - 5x_2^2 = 16$, también girada, con sus ejes principales $y_1$ e $y_2$. El término cruzado es lo que produce el giro.

## Clasificación

> [!tip] Definición
> $Q$ es **definida positiva** si $Q(\mathbf x) > 0$ para todo $\mathbf x \neq \mathbf 0$; **definida negativa** si $Q(\mathbf x) < 0$ para todo $\mathbf x \neq \mathbf 0$; **indefinida** si toma valores positivos y negativos. Es **semidefinida positiva** (negativa) si $Q(\mathbf x) \geq 0$ ($\leq 0$) para todo $\mathbf x$.

> [!tip] Teorema
> Con $A$ simétrica, $\mathbf x^TA\mathbf x$ es definida positiva si y solo si **todos** los valores propios de $A$ son positivos; definida negativa si y solo si todos son negativos; indefinida si y solo si hay de ambos signos. (Semidefinida: todos $\geq 0$, o todos $\leq 0$.)

La razón está en la forma diagonal: $\lambda_1y_1^2 + \dots + \lambda_ny_n^2$ es siempre positiva exactamente cuando todos los $\lambda_i$ lo son. Por ejemplo, $3x_1^2 + 2x_2^2 + x_3^2 + 4x_1x_2 + 4x_2x_3$ tiene valores propios 5, 2 y $-1$: **indefinida**.

![Formas cuadráticas definida, indefinida y semidefinida](adjuntos/Formas%20cuadr%C3%A1ticas%20definida,%20indefinida%20y%20semidefinida.png)

> [!example]- Transcripción de la imagen
> Tres mapas de color de $Q(\mathbf x) = \mathbf x^TA\mathbf x$ (rojo positivo, azul negativo) con sus curvas de nivel y los ejes principales como flechas. Definida positiva ($3x^2 - 2xy + 3y^2$, $\lambda = 2, 4$): todo rojo, curvas de nivel elípticas. Indefinida ($x^2 - 8xy - 5y^2$, $\lambda = 3, -7$): zonas rojas y azules separadas por dos rectas, curvas hiperbólicas. Semidefinida positiva ($x^2 - 6xy + 9y^2$, $\lambda = 0, 10$): nunca azul, y vale cero sobre toda la recta del vector propio de $\lambda = 0$.

> [!tip] Atajo para $2 \times 2$
> Como $\det A = \lambda_1\lambda_2$ y $\operatorname{tr} A = \lambda_1 + \lambda_2$: si $\det A < 0$, es indefinida; si $\det A > 0$, es definida, con el signo de $a_{11}$ (o de la traza). (En general, una simétrica es definida positiva si y solo si todos sus menores principales superiores izquierdos son positivos.)

## Preguntas de repaso

> [!question]- ¿Para qué $a$ es definida positiva $x_1^2 + 2ax_1x_2 + x_2^2$?
> $A = \begin{bmatrix} 1 & a \\ a & 1 \end{bmatrix}$ tiene valores propios $1 \pm a$. Ambos son positivos si y solo si $|a| < 1$.

> [!question]- ¿Por qué un valor propio nulo impide que la forma sea definida?
> Porque en la dirección de su vector propio $\mathbf v$, $Q(\mathbf v) = \mathbf v^TA\mathbf v = 0$ con $\mathbf v \neq \mathbf 0$.

> [!question]- V o F: si $A$ es simétrica y $A^2$ es definida positiva, $A$ es definida positiva.
> Falso. $A = -I$ tiene $A^2 = I$ definida positiva, pero $A$ es definida negativa. Los valores propios de $A^2$ son $\lambda^2$, que pierden el signo.

> [!question]- ¿Qué curva es $3y_1^2 - 7y_2^2 = 21$?
> Una hipérbola: hay un coeficiente positivo y otro negativo (forma indefinida).
