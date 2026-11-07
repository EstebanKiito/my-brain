---
ramo: "Álgebra Lineal"
tema: "Sistemas de ecuaciones lineales"
tags:
  - algebra-lineal/sistemas
  - algebra-lineal/matrices
  - origen/complemento
prerrequisitos:
  - "[[01 - Ecuaciones lineales e intersección de planos]]"
---

# Matrices y operaciones elementales de fila

Al eliminar variables a mano, la mayor parte de lo que se escribe son nombres de variables y signos $+$ y $=$ que no cambian. Lo único que importa son los **números**. Una matriz guarda exactamente esos números en una tabla, y las manipulaciones de ecuaciones se convierten en tres operaciones mecánicas sobre filas.

## Matrices

> [!tip] Definición
> Una **matriz** de $m \times n$ es un arreglo rectangular de números reales con $m$ **filas** (horizontales) y $n$ **columnas** (verticales):
> $$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} \in M_{m\times n}(\mathbb{R}).$$
> La entrada $a_{ij}$ está en la fila $i$ y la columna $j$ (primero fila, después columna).

Por ejemplo, $A = \begin{bmatrix} 3 & -2 & 1 \\ 1 & 1 & -3 \end{bmatrix}$ es de $2 \times 3$: sus filas son $\begin{bmatrix}3 & -2 & 1\end{bmatrix}$ y $\begin{bmatrix}1 & 1 & -3\end{bmatrix}$, y sus columnas son los vectores $\langle 3, 1\rangle$, $\langle -2, 1\rangle$ y $\langle 1, -3\rangle$ de $\mathbb{R}^2$.

## Matriz de coeficientes y matriz ampliada

Al sistema
$$\begin{cases} 3x - 2y + z = 1 \\ x + y - 3z = 2 \end{cases}$$
se le asocian la **matriz de coeficientes** $A$, el **vector de términos independientes** $\mathbf b$ y la **matriz ampliada** (o aumentada):

$$
A = \begin{bmatrix} 3 & -2 & 1 \\ 1 & 1 & -3 \end{bmatrix}, \qquad \mathbf b = \begin{bmatrix}1\\2\end{bmatrix}, \qquad [A \mid \mathbf b] = \left[\begin{array}{ccc|c} 3 & -2 & 1 & 1 \\ 1 & 1 & -3 & 2 \end{array}\right].
$$

La lectura es fija: cada **fila** es una ecuación, cada **columna** (salvo la última) es una variable y la línea vertical es el signo igual. Un sistema de $m$ ecuaciones y $n$ incógnitas tiene ampliada de $m \times (n + 1)$.

> [!warning] Las variables que faltan son ceros
> Si una variable no aparece en una ecuación, su coeficiente es $0$ y hay que escribirlo. En $\begin{cases} x_2 - 4x_3 = 8 \\ 2x_1 - 3x_2 + 2x_3 = 1 \end{cases}$ la primera fila es $\begin{bmatrix} 0 & 1 & -4 & 8 \end{bmatrix}$. Olvidar ese cero desplaza toda la fila y cambia el sistema.

## Operaciones elementales de fila

> [!tip] Las tres operaciones elementales
> 1. **Intercambio:** $F_i \leftrightarrow F_j$.
> 2. **Escalamiento:** $F_i \to cF_i$, con $c \neq 0$.
> 3. **Reemplazo:** $F_i \to F_i + cF_j$, con $j \neq i$ (sumar a una fila un múltiplo de **otra**).
>
> Cada una corresponde a reemplazar el sistema por uno equivalente, así que **no alteran el conjunto solución**.

Las tres son **reversibles**, y su inversa es otra operación del mismo tipo:

| Operación | Inversa |
|---|---|
| $F_i \leftrightarrow F_j$ | el mismo intercambio |
| $F_i \to cF_i$ | $F_i \to \tfrac1c F_i$ |
| $F_i \to F_i + cF_j$ | $F_i \to F_i - cF_j$ |

La reversibilidad es lo que garantiza la equivalencia: toda solución del sistema original es solución del nuevo y, deshaciendo la operación, toda solución del nuevo es solución del original. Por eso se exige $c \neq 0$ al escalar: multiplicar por $0$ borra una ecuación y no se puede deshacer.

Dos matrices son **equivalentes por filas** ($A \sim B$) si una se obtiene de la otra con una sucesión de operaciones elementales.

> [!tip] Consecuencia
> Si las matrices ampliadas de dos sistemas son equivalentes por filas, los sistemas tienen el mismo conjunto solución.

El recíproco es **falso**: $\left[\begin{array}{ccc|c} 2 & -3 & 5 & 1 \\ 0 & 0 & 4 & -2 \end{array}\right]$ y la misma matriz con una fila de ceros agregada tienen las mismas soluciones, pero no pueden ser equivalentes por filas porque ni siquiera tienen el mismo tamaño. Algo parecido ocurre con dos sistemas inconsistentes cualesquiera: tienen el mismo conjunto solución (vacío) sin tener por qué ser equivalentes.

## Ejemplo: resolver con operaciones de fila

$$
\left[\begin{array}{ccc|c} 3 & -2 & 1 & 1 \\ 1 & 1 & -3 & 2 \end{array}\right]
\xrightarrow{F_1 \leftrightarrow F_2}
\left[\begin{array}{ccc|c} 1 & 1 & -3 & 2 \\ 3 & -2 & 1 & 1 \end{array}\right]
\xrightarrow{F_2 \to F_2 - 3F_1}
\left[\begin{array}{ccc|c} 1 & 1 & -3 & 2 \\ 0 & -5 & 10 & -5 \end{array}\right]
$$

$$
\xrightarrow{F_2 \to -\frac15 F_2}
\left[\begin{array}{ccc|c} 1 & 1 & -3 & 2 \\ 0 & 1 & -2 & 1 \end{array}\right]
\xrightarrow{F_1 \to F_1 - F_2}
\left[\begin{array}{ccc|c} 1 & 0 & -1 & 1 \\ 0 & 1 & -2 & 1 \end{array}\right].
$$

La última matriz dice $x - z = 1$ e $y - 2z = 1$, es decir, $x = 1 + z$, $y = 1 + 2z$, con $z$ libre: la misma recta de la nota anterior. Cada flecha es la versión matricial de un paso de eliminación.

## Preguntas de repaso

> [!question]- ¿Por qué no se permite la operación $F_i \to 0 \cdot F_i$?
> Porque no es reversible: borra la información de esa ecuación. El sistema nuevo podría tener más soluciones que el original, así que ya no sería equivalente.

> [!question]- Escriba la matriz ampliada de $\begin{cases} x_1 + 2x_3 = 5 \\ x_2 - x_1 = 0 \\ 3x_3 = x_2 - 1 \end{cases}$.
> Primero se ordenan las variables y se pasan todas a la izquierda: $\left[\begin{array}{ccc|c} 1 & 0 & 2 & 5 \\ -1 & 1 & 0 & 0 \\ 0 & -1 & 3 & -1 \end{array}\right]$.

> [!question]- ¿Cuál es la operación inversa de $F_3 \to F_3 - 4F_1$, y por qué la operación $F_1 \to F_1 + 2F_1$ no es un reemplazo válido?
> La inversa es $F_3 \to F_3 + 4F_1$. $F_1 \to F_1 + 2F_1$ es en realidad $F_1 \to 3F_1$, un escalamiento; el reemplazo exige sumar un múltiplo de **otra** fila. Con $F_1 \to F_1 - F_1$ se borraría la fila sin poder recuperarla.

> [!question]- V o F: si dos sistemas tienen el mismo conjunto solución, sus matrices ampliadas son equivalentes por filas.
> Falso. Basta con que tengan distinto número de ecuaciones (por ejemplo, uno con una ecuación repetida), o dos sistemas inconsistentes sin relación entre sí. La implicación correcta va en el otro sentido.
