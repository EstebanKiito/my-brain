---
ramo: "Álgebra Lineal"
tema: "Reducción por filas"
tags:
  - algebra-lineal/sistemas
  - origen/complemento
prerrequisitos:
  - "[[02 - Matrices y operaciones elementales de fila]]"
---

# Forma escalonada y escalonada reducida

Las operaciones de fila permiten cambiar un sistema por otro equivalente, pero no dicen **hasta dónde** seguir. Las formas escalonadas son esa meta: matrices tan simples que el conjunto solución se lee directamente, de abajo hacia arriba. Además, sus **pivotes** resultan ser la información más importante que se puede extraer de una matriz.

## Forma escalonada

La **entrada principal** de una fila es su primera entrada distinta de cero, leyendo de izquierda a derecha.

> [!tip] Forma escalonada (por filas)
> Una matriz está en **forma escalonada** (FE) si:
> 1. Todas las filas no nulas están arriba de las filas nulas.
> 2. La entrada principal de cada fila está a la derecha de la entrada principal de la fila de arriba.
> 3. Todas las entradas debajo de una entrada principal son cero.

La 3 es consecuencia de la 2, pero se enuncia porque es lo que se busca al escalonar. El patrón tiene forma de escalera ($\blacksquare$ = entrada principal no nula, $*$ = cualquier número):

$$
\begin{bmatrix} \blacksquare & * & * & * \\ 0 & \blacksquare & * & * \\ 0 & 0 & 0 & \blacksquare \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

**Ejemplos.**

- $\begin{bmatrix} 2 & -3 & 2 & 1 \\ 0 & 1 & -4 & 8 \\ 0 & 0 & 0 & 5/2 \end{bmatrix}$ está en FE.
- $\begin{bmatrix} 1 & 4 & 0 \\ 0 & 0 & 0 \\ 0 & 2 & 1 \end{bmatrix}$ no lo está: hay una fila nula arriba de una no nula.
- $\begin{bmatrix} 0 & 3 & 1 \\ 2 & 0 & 5 \end{bmatrix}$ no lo está: la entrada principal de la fila 2 queda a la izquierda de la de la fila 1.

Toda matriz es equivalente por filas a **alguna** matriz escalonada, pero no a una sola: escalar una fila o sumar a una fila un múltiplo de otra de **más abajo** produce otra forma escalonada distinta.

## Forma escalonada reducida

> [!tip] Forma escalonada reducida
> Una matriz en FE está en **forma escalonada reducida** (FER) si además:
> 4. Cada entrada principal es $1$.
> 5. Cada $1$ principal es la única entrada distinta de cero de su columna.

$$
\begin{bmatrix} 1 & * & 0 & * & 0 \\ 0 & 0 & 1 & * & 0 \\ 0 & 0 & 0 & 0 & 1 \end{bmatrix}
$$

> [!tip] Teorema (unicidad de la FER)
> Toda matriz es equivalente por filas a **una única** matriz en forma escalonada reducida.

La unicidad es lo que da sentido a las definiciones que siguen: aunque dos personas escalonen de maneras distintas, llegan a la misma FER y, por lo tanto, a las mismas posiciones de los pivotes.

## Posiciones y columnas pivote

> [!tip] Definición
> Una **posición pivote** de $A$ es la posición de un $1$ principal en la FER de $A$. Una **columna pivote** es una columna de $A$ que contiene una posición pivote.

Las posiciones pivote coinciden con las de las entradas principales de **cualquier** forma escalonada de $A$. Por eso, para saber dónde están los pivotes, basta escalonar; no hace falta llegar a la FER.

**Ejemplo.** Para

$$
A = \begin{bmatrix} 0 & -3 & -6 & 4 & 9 \\ -1 & -2 & -1 & 3 & 1 \\ -2 & -3 & 0 & 3 & -1 \\ 1 & 4 & 5 & -9 & -7 \end{bmatrix},
\qquad
\operatorname{FER}(A) = \begin{bmatrix} 1 & 0 & -3 & 0 & 5 \\ 0 & 1 & 2 & 0 & -3 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}.
$$

Las columnas pivote son la 1, la 2 y la 4. Las columnas 3 y 5 no lo son.

> [!warning] Las columnas pivote se toman de $A$, no de la FER
> La FER sirve para **ubicar** los pivotes, pero las columnas pivote son las columnas originales de $A$ en esas posiciones. Las operaciones de fila cambian los vectores columna, así que las columnas de la FER (como $\mathbf e_1, \mathbf e_2, \mathbf e_3$) no generan lo mismo que las de $A$.

Las columnas no pivote se pueden leer en la FER como combinaciones de las columnas pivote. En el ejemplo, la columna 3 de la FER es $-3$ veces la primera más $2$ veces la segunda, y la misma relación vale entre las columnas de $A$: $\mathbf a_3 = -3\mathbf a_1 + 2\mathbf a_2$. Esto funciona porque las operaciones de fila no cambian las soluciones de $A\mathbf x = \mathbf 0$, que son justamente las relaciones lineales entre columnas.

## Preguntas de repaso

> [!question]- ¿Por qué la forma escalonada no es única pero la reducida sí, y qué consecuencia práctica tiene?
> En la FE se puede escalar filas o sumar múltiplos de filas inferiores sin romper la escalera, así que hay infinitas. La FER fija los pivotes en 1 y anula todo lo demás en sus columnas, y el teorema asegura que es única. En la práctica, las posiciones pivote no dependen de cómo se escalone.

> [!question]- ¿Está en FER $\begin{bmatrix} 1 & 0 & 5 & 0 \\ 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$? ¿Y $\begin{bmatrix} 1 & 3 & 0 \\ 0 & 1 & 0 \end{bmatrix}$?
> La primera sí: los pivotes son 1 y son lo único no nulo en sus columnas (el 5 y el 2 están en una columna sin pivote). La segunda no: el 3 está sobre el pivote de la columna 2.

> [!question]- ¿Cuántos pivotes puede tener como máximo una matriz de $3 \times 5$? ¿Y una de $5 \times 3$?
> Tres en ambos casos: hay a lo más un pivote por fila y uno por columna, así que el máximo es $\min(m, n)$.

> [!question]- Si la FER de $A$ es $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, ¿qué relación hay entre las columnas de $A$?
> $\mathbf a_2 = 2\mathbf a_1$. La relación entre columnas de la FER se conserva en $A$, porque ambas matrices tienen las mismas soluciones de $A\mathbf x = \mathbf 0$: el vector $\langle 2, -1, 0\rangle$ anula a las dos.
