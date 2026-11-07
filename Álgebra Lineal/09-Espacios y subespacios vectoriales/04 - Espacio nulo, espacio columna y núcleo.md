---
ramo: "Álgebra Lineal"
tema: "Espacios y subespacios vectoriales"
tags:
  - algebra-lineal/espacios
  - origen/complemento
prerrequisitos:
  - "[[03 - Independencia lineal y bases]]"
  - "[[01 - Sistemas homogéneos y forma paramétrica]]"
---

# Espacio nulo, espacio columna y núcleo

Cada matriz $A$ de $m \times n$ trae consigo dos subespacios naturales: el **espacio nulo**, formado por las soluciones de $A\mathbf x = \mathbf 0$, y el **espacio columna**, formado por las combinaciones de sus columnas. El primero mide la **unicidad** (cuánto se pierde al multiplicar por $A$) y el segundo la **existencia** (qué lados derechos son alcanzables). Ambos se calculan escalonando, y se generalizan al núcleo y al rango de cualquier transformación lineal.

## Espacio nulo

> [!tip] Definición
> El **espacio nulo** de $A$ ($m \times n$) es $\operatorname{Nul} A = \{\mathbf x \in \mathbb{R}^n : A\mathbf x = \mathbf 0\}$. Es un **subespacio de $\mathbb{R}^n$**.

Es subespacio porque $A\mathbf 0 = \mathbf 0$, y si $A\mathbf u = A\mathbf v = \mathbf 0$, entonces $A(\mathbf u + \mathbf v) = \mathbf 0$ y $A(c\mathbf u) = \mathbf 0$. Está definido **implícitamente**: es fácil comprobar si un vector pertenece (multiplicar por $A$), pero para conocerlo hay que resolver.

![El espacio nulo va al vector cero](adjuntos/El%20espacio%20nulo%20va%20al%20vector%20cero.png)

> [!example]- Transcripción de la imagen
> A la izquierda, $\mathbb{R}^n$ con un subespacio marcado $\operatorname{Nul} A$ que pasa por $\mathbf 0$. Varios puntos de $\operatorname{Nul} A$ se envían, con flechas, a un único punto $\mathbf 0$ en $\mathbb{R}^m$, a la derecha.

**Ejemplo.** Con $A = \begin{bmatrix} 1 & -3 & -2 \\ -5 & 9 & 1 \end{bmatrix}$ y $\mathbf u = \langle 5, 3, -2\rangle$: $A\mathbf u = \langle 5 - 9 + 4, -25 + 27 - 2\rangle = \mathbf 0$, así que $\mathbf u \in \operatorname{Nul} A$.

**Base de $\operatorname{Nul} A$.** Se resuelve $A\mathbf x = \mathbf 0$ y se escribe la forma vectorial paramétrica. Para $A = \begin{bmatrix} -3 & 6 & -1 & 1 & -7 \\ 1 & -2 & 2 & 3 & -1 \\ 2 & -4 & 5 & 8 & -4 \end{bmatrix} \sim \begin{bmatrix} 1 & -2 & 0 & -1 & 3 \\ 0 & 0 & 1 & 2 & -2 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$:

$$
\mathbf x = x_2\begin{bmatrix}2\\1\\0\\0\\0\end{bmatrix} + x_4\begin{bmatrix}1\\0\\-2\\1\\0\end{bmatrix} + x_5\begin{bmatrix}-3\\0\\2\\0\\1\end{bmatrix}.
$$

> [!tip] Base de $\operatorname{Nul} A$
> Los vectores de la forma paramétrica (uno por variable libre) son **automáticamente LI**: cada uno tiene un 1 en la posición de su variable libre y 0 en las de las otras libres. Forman una base, y $\dim\operatorname{Nul} A$ es el **número de variables libres**.

## Espacio columna

> [!tip] Definición
> El **espacio columna** de $A = [\mathbf a_1 \cdots \mathbf a_n]$ es $\operatorname{Col} A = \operatorname{Gen}\{\mathbf a_1, \dots, \mathbf a_n\} = \{A\mathbf x : \mathbf x \in \mathbb{R}^n\}$. Es un **subespacio de $\mathbb{R}^m$**.

Está definido **explícitamente**: es fácil fabricar vectores de $\operatorname{Col} A$ (multiplicar $A$ por cualquier $\mathbf x$), pero para saber si un $\mathbf b$ dado pertenece hay que resolver $A\mathbf x = \mathbf b$. $\operatorname{Col} A = \mathbb{R}^m$ si y solo si $A\mathbf x = \mathbf b$ tiene solución para todo $\mathbf b$.

Un conjunto descrito con parámetros se escribe como espacio columna separando los parámetros: $W = \{\langle 6a - b, a + b, -7a\rangle\} = \operatorname{Col}\begin{bmatrix} 6 & -1 \\ 1 & 1 \\ -7 & 0 \end{bmatrix}$.

> [!tip] Base de $\operatorname{Col} A$
> Las **columnas pivote de $A$** forman una base de $\operatorname{Col} A$.

Las columnas no pivote son combinaciones de las pivote (las relaciones se leen en la FER), así que sobran; y las columnas pivote son LI porque las de la FER lo son. Por ejemplo, si $A = \begin{bmatrix} 1 & 4 & 0 & 2 & -1 \\ 3 & 12 & 1 & 5 & 5 \\ 2 & 8 & 1 & 3 & 2 \\ 5 & 20 & 2 & 8 & 8 \end{bmatrix}$ tiene pivotes en las columnas 1, 3 y 5, una base de $\operatorname{Col} A$ es $\{\mathbf a_1, \mathbf a_3, \mathbf a_5\}$.

> [!warning] Las columnas de $A$, no las de la forma escalonada
> Las operaciones de fila **cambian** el espacio columna. La forma escalonada solo dice **cuáles** columnas son pivote; la base se toma de las columnas **originales** de $A$.

## Dos universos distintos

| $\operatorname{Nul} A$ | $\operatorname{Col} A$ |
|---|---|
| subespacio de $\mathbb{R}^n$ (columnas) | subespacio de $\mathbb{R}^m$ (filas) |
| definido implícitamente | definido explícitamente |
| pertenecer: calcular $A\mathbf v$ | pertenecer: resolver $A\mathbf x = \mathbf v$ |
| $\{\mathbf 0\}$ si y solo si $\mathbf x \mapsto A\mathbf x$ es inyectiva | $\mathbb{R}^m$ si y solo si $\mathbf x \mapsto A\mathbf x$ es sobre |

Con $A = \begin{bmatrix} 2 & 4 & -2 & 1 \\ -2 & -5 & 7 & 3 \\ 3 & 7 & -8 & 6 \end{bmatrix}$: $\operatorname{Nul} A \subseteq \mathbb{R}^4$ y $\operatorname{Col} A \subseteq \mathbb{R}^3$. El vector $\langle 3, -1, 3\rangle$ (de $\mathbb{R}^3$) podría estar en $\operatorname{Col} A$, pero jamás en $\operatorname{Nul} A$.

## Núcleo y rango de una transformación

> [!tip] Definición
> Para una transformación lineal $T: V \to W$, el **núcleo** es $\{\mathbf u \in V : T(\mathbf u) = \mathbf 0\}$ (subespacio de $V$) y el **rango** o imagen es $\{T(\mathbf x) : \mathbf x \in V\}$ (subespacio de $W$). Si $T(\mathbf x) = A\mathbf x$, son $\operatorname{Nul} A$ y $\operatorname{Col} A$.

![Núcleo y rango de una transformación](adjuntos/N%C3%BAcleo%20y%20rango%20de%20una%20transformaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> El dominio $V$ con un subespacio marcado "núcleo", cuyos puntos van todos a $\mathbf 0$ en $W$. Otros puntos del dominio van a puntos de una recta marcada "rango" en $W$. Leyendas: "El núcleo es un subespacio de $V$" y "El rango es un subespacio de $W$".

**Ejemplo.** $T: \mathbb{P}_3 \to \mathbb{R}^2$, $T(p) = \langle p(0),\ p(1) - p(-1)\rangle$. Con $p = a + bt + ct^2 + dt^3$: $T(p) = \langle a,\ 2b + 2d\rangle$. El rango es todo $\mathbb{R}^2$ ($a$ y $2b + 2d$ toman cualquier valor). El núcleo pide $a = 0$ y $b = -d$: $p = ct^2 + d(t^3 - t)$, es decir, $\operatorname{Gen}\{t^2, t^3 - t\}$.

**Ejemplo (derivada).** $D(f) = f'$ de las funciones derivables en $[a, b]$ a las continuas: el núcleo son las funciones constantes y el rango son todas las continuas (toda función continua tiene primitiva).

## Preguntas de repaso

> [!question]- Si $A$ es de $3 \times 7$, ¿de qué espacios son subespacios $\operatorname{Nul} A$ y $\operatorname{Col} A$?
> $\operatorname{Nul} A \subseteq \mathbb{R}^7$ (vectores que se multiplican por $A$) y $\operatorname{Col} A \subseteq \mathbb{R}^3$ (vectores que resultan del producto).

> [!question]- ¿Por qué la base de $\operatorname{Col} A$ se toma de $A$ y no de su forma escalonada?
> Porque las operaciones de fila cambian los vectores columna y su generado. Por ejemplo, la FER puede tener todas sus columnas con última componente 0 aunque $A$ no.

> [!question]- Si $\operatorname{Col} B \subseteq \operatorname{Nul} A$, ¿qué se puede decir de $AB$?
> Que $AB = 0$: cada columna $\mathbf b_j$ de $B$ está en $\operatorname{Col} B$, por lo tanto en $\operatorname{Nul} A$, y la columna $j$ de $AB$ es $A\mathbf b_j = \mathbf 0$.

> [!question]- ¿Cuántos vectores tiene una base de $\operatorname{Nul} A$ si $A$ es de $4 \times 6$ con 4 pivotes?
> $6 - 4 = 2$, uno por variable libre.
