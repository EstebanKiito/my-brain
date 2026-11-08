---
ramo: "Álgebra Lineal"
tema: "Sistemas de ecuaciones lineales"
tags:
  - algebra-lineal/sistemas
  - algebra-lineal/matrices
  - origen/complemento
prerrequisitos:
  - "[[02 - Combinaciones lineales y conjunto generado]]"
  - "[[02 - Matrices y operaciones elementales de fila]]"
---

# Producto matriz-vector y ecuación vectorial

Un mismo sistema lineal se puede escribir de tres formas: como lista de ecuaciones, como **ecuación vectorial** (una combinación lineal de las columnas) y como **ecuación matricial** $A\mathbf x = \mathbf b$. Las tres son equivalentes, y pasar de una a otra es la herramienta más usada del curso: la primera sirve para calcular, la segunda para entender geométricamente y la tercera para razonar en abstracto.

## Producto matriz-vector

> [!tip] Definición (por columnas)
> Si $A = [\mathbf a_1\ \mathbf a_2\ \cdots\ \mathbf a_n]$ es de $m \times n$ y $\mathbf x \in \mathbb{R}^n$,
> $$A\mathbf x = x_1\mathbf a_1 + x_2\mathbf a_2 + \dots + x_n\mathbf a_n \in \mathbb{R}^m.$$
> Es la **combinación lineal de las columnas de $A$ con los pesos de $\mathbf x$**. Solo está definido si $\mathbf x$ tiene tantas componentes como columnas tiene $A$.

**Ejemplo.**
$$
\begin{bmatrix} 1 & 2 & -1 \\ 0 & -5 & 3 \end{bmatrix}\begin{bmatrix}4\\3\\7\end{bmatrix}
= 4\begin{bmatrix}1\\0\end{bmatrix} + 3\begin{bmatrix}2\\-5\end{bmatrix} + 7\begin{bmatrix}-1\\3\end{bmatrix}
= \begin{bmatrix}3\\6\end{bmatrix}.
$$

Al revés, toda combinación lineal es un producto matriz-vector: $3\mathbf v_1 - 5\mathbf v_2 + 7\mathbf v_3 = [\mathbf v_1\ \mathbf v_2\ \mathbf v_3]\begin{bmatrix}3\\-5\\7\end{bmatrix}$.

Para calcular a mano conviene la **regla fila-vector**: la entrada $i$ de $A\mathbf x$ es el producto punto entre la fila $i$ de $A$ y $\mathbf x$. En el ejemplo, $1\cdot4 + 2\cdot3 + (-1)\cdot7 = 3$ y $0\cdot4 + (-5)\cdot3 + 3\cdot7 = 6$. Las dos lecturas dan lo mismo; la de columnas explica, la de filas calcula.

> [!tip] Linealidad
> Si $A$ es de $m \times n$, $\mathbf u, \mathbf v \in \mathbb{R}^n$ y $c \in \mathbb{R}$:
> $$A(\mathbf u + \mathbf v) = A\mathbf u + A\mathbf v, \qquad A(c\mathbf u) = c(A\mathbf u).$$

Se demuestra directo con la definición por columnas y las propiedades de los vectores. Esta propiedad es la base de las transformaciones lineales y permite resolver preguntas sin conocer $A$: si $A\mathbf u = \mathbf p$ y $A\mathbf v = \mathbf q$, entonces $A(2\mathbf u - \mathbf v) = 2\mathbf p - \mathbf q$.

## Tres formas del mismo sistema

> [!tip] Equivalencias fundamentales
> Para $A = [\mathbf a_1 \cdots \mathbf a_n]$ y $\mathbf b \in \mathbb{R}^m$, estas tres afirmaciones tienen exactamente las mismas soluciones $\mathbf x$:
> 1. la ecuación matricial $A\mathbf x = \mathbf b$;
> 2. la ecuación vectorial $x_1\mathbf a_1 + \dots + x_n\mathbf a_n = \mathbf b$;
> 3. el sistema lineal cuya matriz ampliada es $[\mathbf a_1 \cdots \mathbf a_n \mid \mathbf b]$.
>
> En particular, **$A\mathbf x = \mathbf b$ tiene solución si y solo si $\mathbf b$ es combinación lineal de las columnas de $A$**, es decir, si $\mathbf b \in \operatorname{Gen}\{\mathbf a_1, \dots, \mathbf a_n\}$.

**Ejemplo.** Sean $\mathbf a_1 = \langle 3, 1\rangle$, $\mathbf a_2 = \langle -2, 1\rangle$, $\mathbf a_3 = \langle 1, -3\rangle$ y $\mathbf b = \langle 1, 2\rangle$. ¿Está $\mathbf b$ en $\operatorname{Gen}\{\mathbf a_1, \mathbf a_2, \mathbf a_3\}$? La matriz ampliada $[\mathbf a_1\ \mathbf a_2\ \mathbf a_3 \mid \mathbf b]$ es la del sistema que ya se resolvió, con solución $\langle 1 + t, 1 + 2t, t\rangle$. Así que sí, y de infinitas maneras: con $t = 0$, $\mathbf b = \mathbf a_1 + \mathbf a_2$; con $t = 1$, $\mathbf b = 2\mathbf a_1 + 3\mathbf a_2 + \mathbf a_3$.

La pregunta de existencia ("¿hay solución?") es una pregunta sobre el conjunto generado por las columnas. La de unicidad ("¿cuántas?") depende de si las columnas tienen redundancias; eso se estudia con la independencia lineal.

## ¿Cuándo hay solución para todo $\mathbf b$?

Una pregunta frecuente es si $A\mathbf x = \mathbf b$ es consistente **para cualquier** $\mathbf b$, es decir, si las columnas de $A$ generan todo $\mathbb{R}^m$.

> [!tip] Teorema
> Para $A$ de $m \times n$, son equivalentes:
> 1. $A\mathbf x = \mathbf b$ tiene solución para todo $\mathbf b \in \mathbb{R}^m$.
> 2. Todo $\mathbf b \in \mathbb{R}^m$ es combinación lineal de las columnas de $A$.
> 3. Las columnas de $A$ generan $\mathbb{R}^m$.
> 4. $A$ tiene una **posición pivote en cada fila**.

La condición 4 se verifica escalonando **solo $A$**, no la ampliada (las posiciones pivote se definen en la nota de formas escalonadas). Si alguna fila de la forma escalonada de $A$ queda en ceros, existe un $\mathbf b$ que produce en esa fila $[0 \cdots 0 \mid c]$ con $c \neq 0$, y para ese $\mathbf b$ no hay solución.

> [!warning] Más filas que columnas
> Si $A$ tiene más filas que columnas ($m > n$), hay como mucho $n$ pivotes, que no alcanzan para las $m$ filas. Entonces **nunca** genera $\mathbb{R}^m$: $n$ vectores no pueden generar un espacio de mayor dimensión. Por ejemplo, dos vectores de $\mathbb{R}^3$ generan a lo más un plano.

## Preguntas de repaso

> [!question]- ¿Qué tamaño debe tener $\mathbf x$ para que $A\mathbf x$ esté definido si $A$ es de $5 \times 4$, y en qué espacio vive $A\mathbf x$?
> $\mathbf x \in \mathbb{R}^4$ (una componente por columna) y $A\mathbf x \in \mathbb{R}^5$ (una componente por fila).

> [!question]- Si $A\langle 1, 0, 1\rangle = \langle 1, 1\rangle$ y $A\langle 1, 1, 0\rangle = \langle 1, 2\rangle$, ¿es consistente $A\mathbf x = \langle 2, 3\rangle$?
> Sí. Por linealidad, $A\langle 2, 1, 1\rangle = A\langle 1, 0, 1\rangle + A\langle 1, 1, 0\rangle = \langle 2, 3\rangle$, así que $\mathbf x = \langle 2, 1, 1\rangle$ es solución. No hace falta conocer $A$.

> [!question]- ¿Por qué la existencia de solución de $A\mathbf x = \mathbf b$ es una pregunta sobre $\operatorname{Gen}$ de las columnas?
> Porque $A\mathbf x$ es, por definición, una combinación lineal de las columnas con pesos $x_i$. Pedir $A\mathbf x = \mathbf b$ es pedir que $\mathbf b$ sea una de esas combinaciones.

> [!question]- V o F: si $A$ es de $3 \times 4$, entonces $A\mathbf x = \mathbf b$ tiene solución para todo $\mathbf b \in \mathbb{R}^3$.
> Falso en general. Hace falta un pivote en cada una de las 3 filas. Por ejemplo, si todas las columnas de $A$ son iguales, generan solo una recta. Tener más columnas que filas lo hace posible, pero no lo garantiza.

> [!question]- Calcule $\begin{bmatrix} 2 & 0 & -1 \\ 1 & 3 & 4 \end{bmatrix}\begin{bmatrix}1\\-1\\2\end{bmatrix}$ de las dos maneras.
> Por columnas: $1\langle 2, 1\rangle - 1\langle 0, 3\rangle + 2\langle -1, 4\rangle = \langle 0, 6\rangle$. Por filas: $2 - 0 - 2 = 0$ y $1 - 3 + 8 = 6$.
