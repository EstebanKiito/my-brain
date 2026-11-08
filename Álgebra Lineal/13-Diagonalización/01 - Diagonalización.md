---
ramo: "Álgebra Lineal"
tema: "Diagonalización"
tags:
  - algebra-lineal/valores-propios
  - origen/complemento
prerrequisitos:
  - "[[02 - Ecuación característica y similitud]]"
---

# Diagonalización

Una matriz diagonal es la más fácil de manejar: $D^k$ se obtiene elevando cada entrada de la diagonal, y $D\mathbf x$ solo escala cada componente. **Diagonalizar** $A$ es escribirla como $A = PDP^{-1}$ con $D$ diagonal: es decir, encontrar una base (las columnas de $P$) en la que $A$ actúa como una matriz diagonal. Esa base es una base de **vectores propios**, y no todas las matrices la tienen.

## Por qué sirve

Si $D = \begin{bmatrix} 5 & 0 \\ 0 & 3 \end{bmatrix}$, entonces $D^2 = \begin{bmatrix} 25 & 0 \\ 0 & 9 \end{bmatrix}$ y $D^k = \begin{bmatrix} 5^k & 0 \\ 0 & 3^k \end{bmatrix}$. Si $A = PDP^{-1}$, las $P^{-1}P$ intermedias se cancelan:

$$
A^k = PD^kP^{-1}.
$$

Así, una potencia enorme cuesta dos productos de matrices. Por ejemplo, si $A^2 = I$ (valores propios $\pm 1$), entonces $A^{911} = A$.

## Definición y teorema

> [!tip] Definición
> $A$ ($n \times n$) es **diagonalizable** si es similar a una matriz diagonal: $A = PDP^{-1}$ con $P$ invertible y $D$ diagonal.

> [!tip] Teorema de diagonalización
> $A$ es diagonalizable si y solo si tiene **$n$ vectores propios linealmente independientes**. En ese caso, $A = PDP^{-1}$ con
> - las columnas de $P$: $n$ vectores propios LI;
> - $D$: los valores propios correspondientes, **en el mismo orden**.

**Por qué.** $A = PDP^{-1}$ equivale a $AP = PD$. La columna $j$ de $AP$ es $A\mathbf v_j$, y la de $PD$ es $d_j\mathbf v_j$. Así, $AP = PD$ dice exactamente $A\mathbf v_j = d_j\mathbf v_j$: cada columna de $P$ es vector propio. Y $P$ es invertible si y solo si sus columnas son LI.

![Acción de una matriz diagonalizable en la base de vectores propios](adjuntos/Acci%C3%B3n%20de%20una%20matriz%20diagonalizable%20en%20la%20base%20de%20vectores%20propios.png)

> [!example]- Transcripción de la imagen
> $A = \begin{bmatrix} 1{,}5 & 0{,}5 \\ 0{,}5 & 1{,}5 \end{bmatrix}$ tiene vectores propios $\mathbf v_1$ en la dirección $\langle 1, 1\rangle$ ($\lambda = 2$) y $\mathbf v_2$ en la dirección $\langle 1, -1\rangle$ ($\lambda = 1$). A la izquierda, una cuadrícula formada por esas dos direcciones, con una celda sombreada. A la derecha, su imagen bajo $A$: las líneas paralelas a $\mathbf v_1$ se separan al doble y las paralelas a $\mathbf v_2$ no cambian. En la base $\{\mathbf v_1, \mathbf v_2\}$, $A$ solo estira; no gira ni deforma.

## Algoritmo

> [!tip] Cómo diagonalizar
> 1. Encontrar los valores propios (raíces de $\det(A - \lambda I)$).
> 2. Para cada uno, una base de $E_\lambda = \operatorname{Nul}(A - \lambda I)$.
> 3. Si en total hay $n$ vectores, $A$ es diagonalizable. Si hay menos, no lo es.
> 4. $P$ con esos vectores como columnas y $D$ con los valores propios en el mismo orden.

**Ejemplo (sí).** $A = \begin{bmatrix} 1 & 3 & 3 \\ -3 & -5 & -3 \\ 3 & 3 & 1 \end{bmatrix}$ tiene $\det(A - \lambda I) = -(\lambda - 1)(\lambda + 2)^2$, con $E_1 = \operatorname{Gen}\{\langle 1, -1, 1\rangle\}$ y $E_{-2} = \operatorname{Gen}\{\langle -1, 1, 0\rangle, \langle -1, 0, 1\rangle\}$. Hay tres vectores LI:
$$
P = \begin{bmatrix} 1 & -1 & -1 \\ -1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}, \qquad D = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & -2 \end{bmatrix}.
$$
Control rápido sin invertir $P$: comprobar $AP = PD$.

**Ejemplo (no).** $A = \begin{bmatrix} 2 & 4 & 3 \\ -4 & -6 & -3 \\ 3 & 3 & 1 \end{bmatrix}$ tiene el mismo polinomio característico, pero $E_{-2} = \operatorname{Gen}\{\langle -1, 1, 0\rangle\}$ tiene dimensión 1. Solo hay dos vectores propios LI: **no** es diagonalizable.

## Criterios

> [!tip] Teorema
> Una matriz de $n \times n$ con **$n$ valores propios distintos** es diagonalizable.

Los vectores propios de valores distintos son LI, así que uno por cada valor da los $n$ que se necesitan. Por ejemplo, $\begin{bmatrix} 5 & -8 & 1 \\ 0 & 0 & 7 \\ 0 & 0 & -2 \end{bmatrix}$ es triangular con valores propios 5, 0 y $-2$: diagonalizable sin calcular nada más. La condición es **suficiente, no necesaria** ($I$ es diagonal con un solo valor propio).

> [!tip] Teorema (caso general)
> 1. Para cada valor propio, $1 \leq \dim E_\lambda \leq$ multiplicidad algebraica de $\lambda$.
> 2. $A$ es diagonalizable si y solo si el polinomio característico se factoriza completamente en factores lineales y **$\dim E_\lambda$ es igual a la multiplicidad** de cada $\lambda$ (equivalentemente, las dimensiones de los espacios propios suman $n$).
> 3. En ese caso, juntar bases de cada $E_\lambda$ da una base de $\mathbb{R}^n$.

Así, el trabajo está en los valores propios **repetidos**: los simples siempre aportan un vector. Por ejemplo, $A = \begin{bmatrix} 5 & 0 & 0 & 0 \\ 0 & 5 & 0 & 0 \\ 1 & 4 & -3 & 0 \\ -1 & -2 & 0 & -3 \end{bmatrix}$ tiene valores propios 5 y $-3$, ambos con multiplicidad 2, y cada espacio propio resulta de dimensión 2: es diagonalizable.

> [!warning] Diagonalizable e invertible son independientes
> $\begin{bmatrix} 0 & 1 \\ 0 & 1 \end{bmatrix}$ es diagonalizable (valores propios 0 y 1, distintos) pero no invertible. $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ es invertible pero no diagonalizable ($E_1$ tiene dimensión 1). Lo primero depende de los vectores propios; lo segundo, de si 0 es valor propio.

## Preguntas de repaso

> [!question]- ¿Por qué el orden de las columnas de $P$ debe coincidir con el de la diagonal de $D$?
> Porque $AP = PD$ dice $A\mathbf v_j = d_j\mathbf v_j$ columna a columna: la entrada $d_j$ debe ser el valor propio del vector $\mathbf v_j$ que está en la columna $j$.

> [!question]- ¿Es diagonalizable $\begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}$?
> No. El único valor propio es 3, con multiplicidad 2, pero $A - 3I = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$ tiene una sola variable libre: $\dim E_3 = 1 < 2$.

> [!question]- Si $A$ es de $5 \times 5$ con 5 valores propios distintos, ¿qué se puede afirmar?
> Que es diagonalizable: un vector propio por cada valor da 5 vectores LI.

> [!question]- Calcule $A^{10}$ si $A = PDP^{-1}$ con $D = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$.
> $D^{10} = I$, así que $A^{10} = PIP^{-1} = I$.
