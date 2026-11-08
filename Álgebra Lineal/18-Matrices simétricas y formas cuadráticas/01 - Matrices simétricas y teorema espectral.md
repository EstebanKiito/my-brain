---
ramo: "Álgebra Lineal"
tema: "Matrices simétricas y formas cuadráticas"
tags:
  - algebra-lineal/valores-propios
  - algebra-lineal/ortogonalidad
  - origen/complemento
prerrequisitos:
  - "[[01 - Diagonalización]]"
  - "[[02 - Proceso de Gram-Schmidt y factorización QR]]"
---

# Matrices simétricas y teorema espectral

Las matrices simétricas aparecen en todas partes: matrices de covarianza, matrices $A^TA$ de mínimos cuadrados, formas cuadráticas. Y se portan mucho mejor que una matriz cualquiera: **siempre** se pueden diagonalizar, sus valores propios son reales y sus vectores propios se pueden elegir **ortogonales**. Eso permite diagonalizar con una matriz ortogonal, cuya inversa es solo su transpuesta.

## Definición

> [!tip] Definición
> $A$ es **simétrica** si $A^T = A$. Es necesariamente cuadrada; su diagonal es arbitraria y las demás entradas se repiten en espejo respecto de la diagonal: $a_{ij} = a_{ji}$.

$\begin{bmatrix} 1 & 0 \\ 0 & -3 \end{bmatrix}$ y $\begin{bmatrix} 0 & -1 & 0 \\ -1 & 5 & 8 \\ 0 & 8 & -7 \end{bmatrix}$ son simétricas; $\begin{bmatrix} 1 & -3 \\ 3 & 0 \end{bmatrix}$ no lo es (los signos no se repiten), y ninguna matriz no cuadrada lo es.

## Vectores propios ortogonales

> [!tip] Teorema
> Si $A$ es simétrica, vectores propios de **valores propios distintos** son ortogonales.

**Demostración.** Si $A\mathbf v_1 = \lambda_1\mathbf v_1$ y $A\mathbf v_2 = \lambda_2\mathbf v_2$:
$$\lambda_1\,\mathbf v_1 \cdot \mathbf v_2 = (A\mathbf v_1)^T\mathbf v_2 = \mathbf v_1^TA^T\mathbf v_2 = \mathbf v_1^TA\mathbf v_2 = \lambda_2\,\mathbf v_1 \cdot \mathbf v_2,$$
así que $(\lambda_1 - \lambda_2)\,\mathbf v_1 \cdot \mathbf v_2 = 0$, y como $\lambda_1 \neq \lambda_2$, $\mathbf v_1 \cdot \mathbf v_2 = 0$. $\blacksquare$

**Ejemplo.** $A = \begin{bmatrix} 6 & -2 & -1 \\ -2 & 6 & -1 \\ -1 & -1 & 5 \end{bmatrix}$ tiene valores propios 8, 6 y 3, con vectores propios $\langle -1, 1, 0\rangle$, $\langle -1, -1, 2\rangle$ y $\langle 1, 1, 1\rangle$: automáticamente ortogonales. Normalizándolos se obtiene $P$ con columnas ortonormales y $A = PDP^T$.

## Diagonalización ortogonal

> [!tip] Definición y teorema
> $A$ es **diagonalizable ortogonalmente** si $A = PDP^T$ con $P$ **ortogonal** ($P^{-1} = P^T$) y $D$ diagonal. Esto ocurre **si y solo si $A$ es simétrica**.

Una dirección es inmediata: si $A = PDP^T$, entonces $A^T = (P^T)^TD^TP^T = PDP^T = A$. La otra es el teorema espectral.

**Procedimiento.** Igual que diagonalizar, con un paso extra: en cada espacio propio de dimensión mayor que 1 se aplica **Gram-Schmidt** para tener vectores ortogonales; después se normaliza todo.

**Ejemplo con un valor repetido.** $A = \begin{bmatrix} 3 & -2 & 4 \\ -2 & 6 & 2 \\ 4 & 2 & 3 \end{bmatrix}$ tiene $\lambda = 7$ (doble) y $\lambda = -2$.
- $E_7 = \operatorname{Gen}\{\langle 1, 0, 1\rangle, \langle -1, 2, 0\rangle\}$, que no son ortogonales. Gram-Schmidt: $\langle -1, 2, 0\rangle + \tfrac12\langle 1, 0, 1\rangle = \langle -\tfrac12, 2, \tfrac12\rangle$, o escalado $\langle -1, 4, 1\rangle$.
- $E_{-2} = \operatorname{Gen}\{\langle -2, -1, 2\rangle\}$, ortogonal a los dos anteriores.

$$
P = \begin{bmatrix} \frac{1}{\sqrt2} & -\frac{1}{\sqrt{18}} & -\frac23 \\ 0 & \frac{4}{\sqrt{18}} & -\frac13 \\ \frac{1}{\sqrt2} & \frac{1}{\sqrt{18}} & \frac23 \end{bmatrix}, \qquad D = \operatorname{diag}(7, 7, -2).
$$

## Teorema espectral

> [!tip] Teorema espectral (matrices simétricas)
> Si $A$ es simétrica de $n \times n$:
> 1. tiene $n$ valores propios **reales**, contando multiplicidades;
> 2. la dimensión de cada espacio propio es igual a la multiplicidad del valor propio;
> 3. los espacios propios son mutuamente ortogonales;
> 4. $A$ es diagonalizable ortogonalmente.

> [!warning] Lo que no hay que hacer en los ejercicios
> Con una matriz simétrica nunca hace falta verificar si es diagonalizable: siempre lo es. Lo que sí hay que hacer es ortogonalizar dentro de cada espacio propio repetido; los vectores de espacios distintos ya son ortogonales.

## Descomposición espectral

Si $A = PDP^T$ con columnas $\mathbf u_1, \dots, \mathbf u_n$ y valores propios $\lambda_1, \dots, \lambda_n$, multiplicando por columnas y filas:

> [!tip] Descomposición espectral
> $$A = \lambda_1\mathbf u_1\mathbf u_1^T + \lambda_2\mathbf u_2\mathbf u_2^T + \dots + \lambda_n\mathbf u_n\mathbf u_n^T .$$
> Cada $\mathbf u_j\mathbf u_j^T$ es la matriz de proyección sobre $\operatorname{Gen}\{\mathbf u_j\}$: $A$ se descompone en proyecciones ponderadas por sus valores propios.

**Ejemplo.** $A = \begin{bmatrix} 7 & 2 \\ 2 & 4 \end{bmatrix}$ tiene $\lambda = 8$ con $\mathbf u_1 = \tfrac{1}{\sqrt5}\langle 2, 1\rangle$ y $\lambda = 3$ con $\mathbf u_2 = \tfrac{1}{\sqrt5}\langle -1, 2\rangle$:
$$A = 8\cdot\frac15\begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} + 3\cdot\frac15\begin{bmatrix} 1 & -2 \\ -2 & 4 \end{bmatrix}.$$

## Preguntas de repaso

> [!question]- ¿Por qué $A^TA$ es siempre diagonalizable ortogonalmente?
> Porque es simétrica: $(A^TA)^T = A^T(A^T)^T = A^TA$.

> [!question]- Diagonalice ortogonalmente $C = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.
> Valores propios 0 y 2, con vectores $\langle 1, -1\rangle$ y $\langle 1, 1\rangle$. $P = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$ y $D = \operatorname{diag}(0, 2)$.

> [!question]- En una matriz simétrica, ¿hay que aplicar Gram-Schmidt a todos los vectores propios juntos?
> No: solo dentro de cada espacio propio de dimensión mayor que 1. Los de espacios distintos ya son ortogonales por el teorema.

> [!question]- ¿Qué tiene de especial $P$ en $A = PDP^T$ frente a $A = PDP^{-1}$?
> Es ortogonal, así que su inversa es su transpuesta y no hay que invertirla.
