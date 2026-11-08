---
ramo: "Álgebra Lineal"
tema: "Diagonalización"
tags:
  - algebra-lineal/valores-propios
  - algebra-lineal/transformaciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Diagonalización]]"
  - "[[02 - Cambio de base en Rⁿ y en polinomios]]"
---

# Vectores propios y matriz de una transformación

La diagonalización tiene una lectura más profunda: $A$ y $D = P^{-1}AP$ son **la misma transformación vista en dos bases distintas**. Para entenderlo hace falta representar una transformación lineal cualquiera (entre polinomios, por ejemplo) con una matriz, usando coordenadas. Con esa herramienta, diagonalizar es simplemente elegir la base en que la transformación se ve más simple.

## Matriz de una transformación respecto de dos bases

> [!tip] Teorema
> Sea $T: V \to W$ lineal, con bases $\mathcal B = \{\mathbf b_1, \dots, \mathbf b_n\}$ de $V$ y $\mathcal C$ de $W$. Existe una única matriz $M$ ($m \times n$) tal que
> $$[T(\mathbf x)]_{\mathcal C} = M[\mathbf x]_{\mathcal B} \quad\text{para todo } \mathbf x \in V,$$
> y es $M = \big[\,[T(\mathbf b_1)]_{\mathcal C}\ \cdots\ [T(\mathbf b_n)]_{\mathcal C}\,\big]$. Se llama **matriz de $T$ respecto de $\mathcal B$ y $\mathcal C$**.

La receta es la misma que para la matriz estándar: aplicar $T$ a cada vector de la base de partida y escribir el resultado en coordenadas de la base de llegada.

**Ejemplo.** Si $T(\mathbf b_1) = 3\mathbf c_1 - 2\mathbf c_2 + 5\mathbf c_3$ y $T(\mathbf b_2) = 4\mathbf c_1 + 7\mathbf c_2 - \mathbf c_3$, entonces $M = \begin{bmatrix} 3 & 4 \\ -2 & 7 \\ 5 & -1 \end{bmatrix}$.

**Ejemplo.** Si $T(x_1\mathbf b_1 + x_2\mathbf b_2 + x_3\mathbf b_3) = \langle 2x_1 - 3x_2 + x_3,\ -2x_1 + 5x_3\rangle$ (con la base estándar en $\mathbb{R}^2$), la fórmula ya está en coordenadas: $M = \begin{bmatrix} 2 & -3 & 1 \\ -2 & 0 & 5 \end{bmatrix}$.

## La $\mathcal B$-matriz

Cuando $T: V \to V$ y se usa la misma base en ambos lados, la matriz se llama **$\mathcal B$-matriz** de $T$, $[T]_{\mathcal B}$, y cumple $[T(\mathbf x)]_{\mathcal B} = [T]_{\mathcal B}[\mathbf x]_{\mathcal B}$.

**Ejemplo (derivada).** $T: \mathbb{P}_2 \to \mathbb{P}_2$, $T(p) = p'$, con $\mathcal B = \{1, t, t^2\}$: $T(1) = 0$, $T(t) = 1$ y $T(t^2) = 2t$, así que
$$[T]_{\mathcal B} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{bmatrix}.$$
Para derivar $a_0 + a_1t + a_2t^2$ basta multiplicar: $[T]_{\mathcal B}\langle a_0, a_1, a_2\rangle = \langle a_1, 2a_2, 0\rangle$, que es $a_1 + 2a_2t$.

## Cambiar de base en $\mathbb{R}^n$

> [!tip] Teorema
> Si $T(\mathbf x) = A\mathbf x$ en $\mathbb{R}^n$ y $\mathcal B$ es una base con matriz $P = [\mathbf b_1 \cdots \mathbf b_n]$, entonces
> $$[T]_{\mathcal B} = P^{-1}AP .$$

Leído de derecha a izquierda: $P$ pasa de coordenadas $\mathcal B$ a estándar, $A$ aplica la transformación y $P^{-1}$ vuelve a coordenadas $\mathcal B$. Por eso **matrices similares representan la misma transformación en bases distintas**, y por eso tienen los mismos valores propios.

> [!tip] Representación diagonal
> Si $A = PDP^{-1}$ con $D$ diagonal y $\mathcal B$ es la base formada por las columnas de $P$, entonces $D = [T]_{\mathcal B}$: en la base de vectores propios, la transformación $\mathbf x \mapsto A\mathbf x$ es diagonal.

**Ejemplo.** Para $A = \begin{bmatrix} 7 & 2 \\ -4 & 1 \end{bmatrix}$ se busca una base $\mathcal B$ con $[T]_{\mathcal B}$ diagonal. Los valores propios son 5 y 3, con vectores propios $\langle 1, -1\rangle$ y $\langle 1, -2\rangle$. Con $\mathcal B = \{\langle 1, -1\rangle, \langle 1, -2\rangle\}$, $[T]_{\mathcal B} = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}$.

**En espacios abstractos** se procede igual: se calcula $[T]_{\mathcal B}$ en alguna base cómoda, se diagonaliza esa matriz y se traducen los vectores propios (que son coordenadas) de vuelta a vectores de $V$. Esos vectores forman la base en que $T$ es diagonal.

> [!warning] Los vectores propios de $[T]_{\mathcal B}$ son coordenadas
> Si $[T]_{\mathcal B}$ tiene vector propio $\langle 1, 2\rangle$ con $\mathcal B = \{1, t\}$, el vector propio de $T$ es el **polinomio** $1 + 2t$, no el vector $\langle 1, 2\rangle$.

## Preguntas de repaso

> [!question]- Encuentre la matriz de $T: \mathbb{P}_1 \to \mathbb{P}_1$, $T(a + bt) = b + at$, en la base $\{1, t\}$. ¿En qué base es diagonal?
> $T(1) = t$ y $T(t) = 1$: $[T] = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$. Sus vectores propios son $\langle 1, 1\rangle$ ($\lambda = 1$) y $\langle 1, -1\rangle$ ($\lambda = -1$), así que en la base $\{1 + t, 1 - t\}$ la matriz es $\operatorname{diag}(1, -1)$.

> [!question]- ¿Por qué matrices similares tienen los mismos valores propios, desde el punto de vista de las transformaciones?
> Porque representan la misma transformación en bases distintas, y "estirar la dirección $\mathbf v$ por $\lambda$" es una propiedad de la transformación, no de la base elegida para escribirla.

> [!question]- Si $[T]_{\mathcal B}$ es la matriz de la derivada en $\mathbb{P}_2$, ¿cuáles son sus valores propios? ¿Es diagonalizable?
> Es triangular con ceros en la diagonal: solo $\lambda = 0$, con multiplicidad 3. Pero $E_0$ son los polinomios constantes, de dimensión 1. No es diagonalizable.

> [!question]- Con $\mathcal B = \{\mathbf b_1, \mathbf b_2, \mathbf b_3\}$ y $[T]_{\mathcal B} = \begin{bmatrix} 0 & 0 & 1 \\ 2 & 1 & -2 \\ 1 & 3 & 1 \end{bmatrix}$, calcule $T(4\mathbf b_1 - 3\mathbf b_2)$.
> $[T]_{\mathcal B}\langle 4, -3, 0\rangle = \langle 0, 5, -5\rangle$, así que $T(4\mathbf b_1 - 3\mathbf b_2) = 5\mathbf b_2 - 5\mathbf b_3$.
