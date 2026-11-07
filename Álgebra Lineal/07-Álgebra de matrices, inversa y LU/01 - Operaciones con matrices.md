---
ramo: "Álgebra Lineal"
tema: "Álgebra de matrices, inversa y LU"
tags:
  - algebra-lineal/matrices
  - origen/complemento
prerrequisitos:
  - "[[03 - Producto matriz-vector y ecuación vectorial]]"
  - "[[02 - Matriz estándar de una transformación lineal]]"
---

# Operaciones con matrices

Las matrices empezaron como tablas de coeficientes, pero también representan transformaciones lineales. Para trabajar con ellas como objetos propios hace falta un álgebra: sumarlas, escalarlas y, sobre todo, **multiplicarlas**. El producto de matrices no se define "entrada por entrada" sino de la única forma que hace que multiplicar matrices corresponda a **componer transformaciones**. Eso explica tanto su definición como sus rarezas (no es conmutativo, no se puede cancelar).

## Vocabulario

En $A = [a_{ij}]$ de $m \times n$, las entradas $a_{11}, a_{22}, a_{33}, \dots$ forman la **diagonal principal**.

| Tipo | Definición |
|---|---|
| Matriz **cuadrada** | $m = n$ |
| Matriz **diagonal** | cuadrada, con ceros fuera de la diagonal |
| **Identidad** $I_n$ | diagonal con unos en la diagonal |
| Matriz **nula** $0$ | todas sus entradas son cero |
| **Triangular superior** | ceros bajo la diagonal principal |
| **Triangular inferior** | ceros sobre la diagonal principal |

## Suma y producto por escalar

Se hacen **entrada por entrada**, igual que con vectores. $A + B$ solo existe si $A$ y $B$ tienen el mismo tamaño. Con $A = \begin{bmatrix} 4 & 0 & 5 \\ -1 & 3 & 2 \end{bmatrix}$ y $B = \begin{bmatrix} 1 & 1 & 1 \\ 3 & 5 & 7 \end{bmatrix}$:

$$
A + B = \begin{bmatrix} 5 & 1 & 6 \\ 2 & 8 & 9 \end{bmatrix}, \qquad A - 2B = \begin{bmatrix} 2 & -2 & 3 \\ -7 & -7 & -12 \end{bmatrix},
$$

mientras que $A + C$ con $C$ de $2 \times 2$ no está definida. Valen las mismas ocho propiedades que para vectores (conmutatividad, asociatividad, neutro $0$, opuesto $-A$, distributividades, etc.).

## Producto de matrices

La idea: si $B$ transforma $\mathbf x$ en $B\mathbf x$ y luego $A$ transforma ese resultado, se quiere una matriz $AB$ que haga las dos cosas de una vez: $A(B\mathbf x) = (AB)\mathbf x$.

![Multiplicación por B y luego por A](adjuntos/Multiplicaci%C3%B3n%20por%20B%20y%20luego%20por%20A.png)

> [!example]- Transcripción de la imagen
> Tres planos en fila. Un vector $\mathbf x$ en el primero va, multiplicándolo por $B$, a $B\mathbf x$ en el segundo, y de ahí, multiplicándolo por $A$, a $A(B\mathbf x)$ en el tercero. Una flecha directa del primero al tercero indica que multiplicar por $AB$ hace el mismo recorrido de una vez.

> [!tip] Definición
> Si $A$ es de $m \times n$ y $B = [\mathbf b_1 \cdots \mathbf b_p]$ es de $n \times p$, entonces $AB$ es la matriz de $m \times p$
> $$AB = [\,A\mathbf b_1\ \ A\mathbf b_2\ \ \cdots\ \ A\mathbf b_p\,].$$
> Cada columna de $AB$ es una combinación lineal de las columnas de $A$, con pesos de la columna correspondiente de $B$.

**Tamaños.** El número de columnas de $A$ debe coincidir con el de filas de $B$: $(m \times \mathbf n)(\mathbf n \times p) = m \times p$. Si $A$ es de $3 \times 5$ y $B$ de $5 \times 2$, $AB$ es de $3 \times 2$ y $BA$ no está definido.

> [!tip] Regla fila-columna
> La entrada $(i, j)$ de $AB$ es el producto punto de la **fila $i$ de $A$** con la **columna $j$ de $B$**: $(AB)_{ij} = a_{i1}b_{1j} + \dots + a_{in}b_{nj}$. Y la fila $i$ de $AB$ es (fila $i$ de $A$)$\cdot B$.

**Ejemplo.** $\begin{bmatrix} 2 & 3 \\ 1 & -5 \end{bmatrix}\begin{bmatrix} 4 & 3 & 6 \\ 1 & -2 & 3 \end{bmatrix} = \begin{bmatrix} 11 & 0 & 21 \\ -1 & 13 & -9 \end{bmatrix}$. La entrada $(1, 3)$ es $2 \cdot 6 + 3 \cdot 3 = 21$ y la $(2, 2)$ es $1 \cdot 3 + (-5)(-2) = 13$.

Propiedades (con tamaños compatibles): $A(BC) = (AB)C$, $A(B + C) = AB + AC$, $(B + C)A = BA + CA$, $r(AB) = (rA)B = A(rB)$ e $I_mA = A = AI_n$.

> [!warning] Tres reglas de los números que fallan
> 1. **No conmuta:** con $A = \begin{bmatrix} 5 & 1 \\ 3 & -2 \end{bmatrix}$ y $B = \begin{bmatrix} 2 & 0 \\ 4 & 3 \end{bmatrix}$, $AB = \begin{bmatrix} 14 & 3 \\ -2 & -6 \end{bmatrix}$ pero $BA = \begin{bmatrix} 10 & 2 \\ 29 & -2 \end{bmatrix}$. Componer en otro orden es otra transformación.
> 2. **No se cancela:** $AB = AC$ no implica $B = C$.
> 3. **Hay divisores de cero:** $AB = 0$ no implica $A = 0$ o $B = 0$; por ejemplo, $\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}^2 = 0$.
>
> Por eso, al despejar en ecuaciones matriciales hay que multiplicar **por el mismo lado** en ambos miembros y solo por matrices invertibles.

**Potencias.** Para $A$ cuadrada, $A^k = A \cdots A$ ($k$ veces) y $A^0 = I$. Cuidado con $(A + B)^2 = A^2 + AB + BA + B^2$, que no es $A^2 + 2AB + B^2$ salvo que $AB = BA$.

## Transpuesta

> [!tip] Definición
> La **transpuesta** $A^T$ de $A$ ($m \times n$) es la matriz de $n \times m$ cuyas columnas son las filas de $A$: $(A^T)_{ij} = a_{ji}$.

Por ejemplo, $\begin{bmatrix} -5 & 2 \\ 1 & -3 \\ 0 & 4 \end{bmatrix}^T = \begin{bmatrix} -5 & 1 & 0 \\ 2 & -3 & 4 \end{bmatrix}$. Propiedades:

$$
(A^T)^T = A, \qquad (A + B)^T = A^T + B^T, \qquad (rA)^T = rA^T, \qquad (AB)^T = B^TA^T .
$$

La última invierte el orden (es obligatorio por tamaños: si $A$ es $m \times n$ y $B$ es $n \times p$, $A^TB^T$ ni siquiera está definido en general). Una matriz es **simétrica** si $A^T = A$ y **antisimétrica** si $A^T = -A$.

## Preguntas de repaso

> [!question]- Si $A$ es de $4 \times 2$ y $B$ de $2 \times 4$, ¿qué tamaño tienen $AB$ y $BA$?
> $AB$ es de $4 \times 4$ y $BA$ de $2 \times 2$. Ambas existen pero ni siquiera tienen el mismo tamaño.

> [!question]- ¿Por qué el producto se define columna por columna como $A\mathbf b_j$?
> Para que $(AB)\mathbf x = A(B\mathbf x)$: multiplicar por $AB$ debe equivaler a aplicar primero $B$ y después $A$. Con esa exigencia, la columna $j$ de $AB$ tiene que ser $(AB)\mathbf e_j = A(B\mathbf e_j) = A\mathbf b_j$.

> [!question]- V o F: si $A$ y $B$ son antisimétricas de $2 \times 2$, $AB$ es antisimétrica.
> Falso. Con $A = B = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$, $AB = -I$, que es simétrica y no antisimétrica.

> [!question]- Demuestre que $AA^T$ es simétrica para cualquier $A$.
> $(AA^T)^T = (A^T)^TA^T = AA^T$, usando que la transpuesta de un producto invierte el orden.

> [!question]- Calcule la segunda fila de $AB$ con $A = \begin{bmatrix} 2 & -5 & 0 \\ -1 & 3 & -4 \\ 6 & -8 & -7 \end{bmatrix}$ y $B = \begin{bmatrix} 4 & -6 \\ 7 & 1 \\ 3 & 2 \end{bmatrix}$.
> Es la fila 2 de $A$ por $B$: $[-1\ 3\ -4]B = [-4 + 21 - 12,\ 6 + 3 - 8] = [5\ \ 1]$.
