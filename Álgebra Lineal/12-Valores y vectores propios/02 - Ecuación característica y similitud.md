---
ramo: "Álgebra Lineal"
tema: "Valores y vectores propios"
tags:
  - algebra-lineal/valores-propios
  - origen/complemento
prerrequisitos:
  - "[[01 - Valores y vectores propios]]"
---

# Ecuación característica y similitud

Verificar si un vector es propio es fácil, pero ¿cómo se **encuentran** los valores propios? La estrategia es buscar primero los $\lambda$, que son los números que hacen singular a $A - \lambda I$, y después sus espacios propios. Para lo primero sirve el determinante: $A - \lambda I$ es singular exactamente cuando su determinante es cero.

## Ecuación y polinomio característico

> [!tip] Teorema (ecuación característica)
> $\lambda$ es valor propio de $A$ ($n \times n$) si y solo si
> $$\det(A - \lambda I) = 0 .$$
> $\det(A - \lambda I)$ es un polinomio de grado $n$ en $\lambda$, el **polinomio característico** de $A$.

> [!tip] Procedimiento
> 1. Calcular $\det(A - \lambda I)$ y factorizarlo: sus raíces son los valores propios.
> 2. Para cada $\lambda$, resolver $(A - \lambda I)\mathbf x = \mathbf 0$: una base de las soluciones es una base de $E_\lambda$.

**Ejemplo.** $A = \begin{bmatrix} 2 & 3 \\ 3 & -6 \end{bmatrix}$.
$$\det(A - \lambda I) = (2 - \lambda)(-6 - \lambda) - 9 = \lambda^2 + 4\lambda - 21 = (\lambda + 7)(\lambda - 3).$$
- $\lambda = 3$: $A - 3I = \begin{bmatrix} -1 & 3 \\ 3 & -9 \end{bmatrix}$, así que $x_1 = 3x_2$ y $E_3 = \operatorname{Gen}\{\langle 3, 1\rangle\}$.
- $\lambda = -7$: $A + 7I = \begin{bmatrix} 9 & 3 \\ 3 & 1 \end{bmatrix}$, así que $x_2 = -3x_1$ y $E_{-7} = \operatorname{Gen}\{\langle 1, -3\rangle\}$.

**Ejemplo triangular.** Para $A = \begin{bmatrix} 5 & -2 & 6 & -1 \\ 0 & 3 & -8 & 0 \\ 0 & 0 & 5 & 4 \\ 0 & 0 & 0 & 1 \end{bmatrix}$, $\det(A - \lambda I) = (5 - \lambda)^2(3 - \lambda)(1 - \lambda)$, sin calcular nada más.

## Multiplicidad

> [!tip] Definición
> La **multiplicidad algebraica** de un valor propio es su multiplicidad como raíz del polinomio característico.

Si el polinomio característico de una matriz de $6 \times 6$ es $\lambda^6 - 4\lambda^5 - 12\lambda^4 = \lambda^4(\lambda - 6)(\lambda + 2)$, los valores propios son $0$ (multiplicidad 4), $6$ y $-2$ (multiplicidad 1). Las multiplicidades suman $n$ cuando todas las raíces son reales.

Si $\det(A - \lambda I) = (\lambda_1 - \lambda)\cdots(\lambda_n - \lambda)$, evaluando en $\lambda = 0$:

> [!tip] Consecuencia
> $\det A$ es el **producto** de los $n$ valores propios (repetidos según su multiplicidad).

Por eso $\det A = 0$ si y solo si algún valor propio es 0. (Además, la suma de los valores propios es la traza, la suma de la diagonal; sirve como control de cuentas.)

## Similitud

> [!tip] Definición
> $A$ es **similar** a $B$ si existe $P$ invertible con $P^{-1}AP = B$, o equivalentemente $A = PBP^{-1}$.

> [!tip] Teorema
> Matrices similares tienen el **mismo polinomio característico** y, por lo tanto, los mismos valores propios con las mismas multiplicidades.

**Demostración.** $B - \lambda I = P^{-1}AP - \lambda P^{-1}P = P^{-1}(A - \lambda I)P$, así que $\det(B - \lambda I) = \det P^{-1}\det(A - \lambda I)\det P = \det(A - \lambda I)$. $\blacksquare$

> [!warning] Similitud no es equivalencia por filas
> Las operaciones de fila **cambian** los valores propios: $\begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix} \sim I$ por filas, pero una tiene valor propio 2 y la otra no. Y el recíproco del teorema es falso: $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ e $I$ tienen el mismo polinomio característico pero no son similares (lo único similar a $I$ es $I$).

**Potencias con similitud.** Si $A = PDP^{-1}$, entonces $A^2 = PDP^{-1}PDP^{-1} = PD^2P^{-1}$ y en general $A^k = PD^kP^{-1}$: las $P^{-1}P$ del medio se cancelan. Con $A = \begin{bmatrix} 7 & 2 \\ -4 & 1 \end{bmatrix}$, $P = \begin{bmatrix} 1 & 1 \\ -1 & -2 \end{bmatrix}$ y $D = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}$ se cumple $A = PDP^{-1}$, y

$$
A^k = PD^kP^{-1} = \begin{bmatrix} 2 \cdot 5^k - 3^k & 5^k - 3^k \\ 2 \cdot 3^k - 2 \cdot 5^k & 2 \cdot 3^k - 5^k \end{bmatrix}.
$$

Con $k = 1$ se recupera $A$, lo que sirve de control. Esto se desarrolla en la diagonalización.

## Preguntas de repaso

> [!question]- Demuestre que $A$ y $A^T$ tienen el mismo polinomio característico.
> $\det(A^T - \lambda I) = \det\big((A - \lambda I)^T\big) = \det(A - \lambda I)$, porque $I^T = I$ y el determinante no cambia al transponer.

> [!question]- Una matriz de $3 \times 3$ tiene polinomio característico $-(\lambda - 2)^2(\lambda + 1)$. ¿Cuánto vale $\det A$? ¿Y la traza?
> $\det A = 2 \cdot 2 \cdot (-1) = -4$ y la traza es $2 + 2 - 1 = 3$.

> [!question]- Si $A$ es invertible y $A^4 - 7A^3 = 0$, ¿por qué 7 es valor propio?
> $A^3(A - 7I) = 0$, así que $(\det A)^3\det(A - 7I) = 0$. Como $\det A \neq 0$, $\det(A - 7I) = 0$, y 7 es raíz del polinomio característico.

> [!question]- ¿Por qué $A = PBP^{-1}$ implica $A^k = PB^kP^{-1}$?
> Al multiplicar $k$ copias de $PBP^{-1}$, cada $P^{-1}$ queda pegado a una $P$ y se cancela, salvo la primera $P$ y la última $P^{-1}$.
