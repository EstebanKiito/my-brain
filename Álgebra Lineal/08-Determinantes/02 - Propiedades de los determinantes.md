---
ramo: "Álgebra Lineal"
tema: "Determinantes"
tags:
  - algebra-lineal/determinantes
  - origen/complemento
prerrequisitos:
  - "[[01 - Determinante y desarrollo por cofactores]]"
  - "[[04 - Teorema de la matriz invertible]]"
---

# Propiedades de los determinantes

El secreto de los determinantes es **cómo cambian con las operaciones de fila**. Sabiendo eso, se calculan escalonando (mucho más rápido que con cofactores), se demuestra que $\det A \neq 0$ equivale a invertible y se obtienen las reglas para productos, transpuestas, inversas y múltiplos, que son la mayor parte de lo que se pregunta en las pruebas.

## Operaciones de fila

> [!tip] Teorema
> Sea $A$ cuadrada.
> 1. **Reemplazo:** si $B$ se obtiene sumando a una fila un múltiplo de otra, $\det B = \det A$.
> 2. **Intercambio:** si $B$ se obtiene intercambiando dos filas, $\det B = -\det A$.
> 3. **Escalamiento:** si $B$ se obtiene multiplicando una fila por $k$, $\det B = k\det A$.

La regla 3 se usa al revés para **sacar factores comunes** de una fila: $\begin{vmatrix} * & * & * \\ 5k & -2k & 3k \\ * & * & * \end{vmatrix} = k\begin{vmatrix} * & * & * \\ 5 & -2 & 3 \\ * & * & * \end{vmatrix}$.

**Ejemplo.**
$$
\begin{vmatrix} 1 & -4 & 2 \\ -2 & 8 & -9 \\ -1 & 7 & 0 \end{vmatrix}
\overset{\substack{F_2 + 2F_1 \\ F_3 + F_1}}{=}
\begin{vmatrix} 1 & -4 & 2 \\ 0 & 0 & -5 \\ 0 & 3 & 2 \end{vmatrix}
\overset{F_2 \leftrightarrow F_3}{=}
-\begin{vmatrix} 1 & -4 & 2 \\ 0 & 3 & 2 \\ 0 & 0 & -5 \end{vmatrix} = -(1 \cdot 3 \cdot (-5)) = 15 .
$$

> [!tip] Determinante por escalonamiento
> Si $A$ se reduce a una forma escalonada $U$ con reemplazos e intercambios, y hubo $r$ intercambios,
> $$\det A = (-1)^r\,(\text{producto de las entradas diagonales de } U).$$

No hace falta llegar a la forma escalonada completa: se puede escalonar hasta tener una fila o columna con muchos ceros y terminar con cofactores.

## Invertibilidad

> [!tip] Teorema
> Una matriz cuadrada $A$ es invertible si y solo si $\det A \neq 0$.

Si $A$ es invertible, $U$ tiene $n$ pivotes no nulos en la diagonal y su producto no es cero; si no lo es, $U$ tiene una fila de ceros y el producto es cero. Esta condición se agrega al teorema de la matriz invertible. Consecuencia: si las filas o las columnas de $A$ son LD (por ejemplo, dos filas iguales o proporcionales), $\det A = 0$.

**Ejemplo con parámetro.** $A = \begin{bmatrix} 1 - \alpha & 3 & 3 \\ -3 & -5 - \alpha & -3 \\ 3 & 3 & 1 - \alpha \end{bmatrix}$ tiene $\det A = -(\alpha - 1)(\alpha + 2)^2$, así que es invertible si y solo si $\alpha \neq 1$ y $\alpha \neq -2$.

## Transpuesta y columnas

> [!tip] Teorema
> $\det A^T = \det A$.

Por lo tanto, las **operaciones de columna** afectan al determinante igual que las de fila, y se pueden mezclar. Una columna de ceros, dos columnas iguales o columnas LD dan determinante cero.

## Producto

> [!tip] Teorema (multiplicatividad)
> Si $A$ y $B$ son de $n \times n$, $\det(AB) = (\det A)(\det B)$.

Por ejemplo, $A = \begin{bmatrix} 6 & 1 \\ 3 & 2 \end{bmatrix}$ y $B = \begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix}$ tienen $\det A = 9$, $\det B = 5$ y $\det AB = 45$.

De aquí y de las anteriores salen las reglas que más se usan:

| Expresión | Determinante ($A$ de $n \times n$) | Por qué |
|---|---|---|
| $A^k$ | $(\det A)^k$ | multiplicatividad |
| $A^{-1}$ | $\dfrac{1}{\det A}$ | $\det A \det A^{-1} = \det I = 1$ |
| $cA$ | $c^n\det A$ | se escalan las $n$ filas |
| $A^T$ | $\det A$ | transpuesta |
| $PAP^{-1}$ | $\det A$ | $\det P \cdot \det A \cdot \frac{1}{\det P}$ |

> [!warning] Lo que no vale
> - $\det(A + B) \neq \det A + \det B$ en general.
> - $\det(cA) \neq c\det A$: el factor sale **$n$ veces**. Con $A$ de $2 \times 2$ y $\det A = 5$, $\det(3A) = 9 \cdot 5 = 45$.

## Linealidad en una columna

Si se fijan todas las columnas menos la $j$-ésima, la función $\mathbf x \mapsto \det[\mathbf a_1 \cdots \mathbf x \cdots \mathbf a_n]$ es **lineal**: $T(c\mathbf x) = cT(\mathbf x)$ y $T(\mathbf u + \mathbf v) = T(\mathbf u) + T(\mathbf v)$. Esto permite separar una columna que es suma de dos. Pero el determinante **no** es lineal como función de toda la matriz.

## Preguntas de repaso

> [!question]- Si $\det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} = -6$, ¿cuánto vale $\det\begin{bmatrix} -3a & d & g - 4d \\ -3b & e & h - 4e \\ -3c & f & i - 4f \end{bmatrix}$?
> Es la transpuesta de la original con la fila 1 multiplicada por $-3$ y la fila 3 reemplazada por $F_3 - 4F_2$ (en la transpuesta, columnas). El reemplazo no cambia nada, el escalamiento multiplica por $-3$ y la transpuesta no cambia el valor: $(-3)(-6) = 18$.

> [!question]- $A$ es de $5 \times 5$ con $\det A = -2$. Calcule $\det(2A^{-1})$.
> $2^5 \cdot \tfrac{1}{-2} = -16$.

> [!question]- ¿Por qué una matriz con dos filas iguales tiene determinante cero?
> Restando una de la otra (reemplazo, no cambia el determinante) queda una fila de ceros, cuyo determinante es cero. También: las filas son LD.

> [!question]- Si $A^5 = \begin{bmatrix} 3 & 0 & s \\ 1 & -1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$, ¿para qué $s$ es invertible $A^T$?
> $\det(A^5) = 2s - 6$ y $\det(A^T) = \det A$, con $(\det A)^5 = 2s - 6$. $A^T$ es invertible si y solo si $\det A \neq 0$, o sea $s \neq 3$.
