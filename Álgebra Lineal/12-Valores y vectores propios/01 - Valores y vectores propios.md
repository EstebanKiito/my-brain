---
ramo: "Álgebra Lineal"
tema: "Valores y vectores propios"
tags:
  - algebra-lineal/valores-propios
  - origen/complemento
prerrequisitos:
  - "[[04 - Espacio nulo, espacio columna y núcleo]]"
  - "[[02 - Propiedades de los determinantes]]"
---

# Valores y vectores propios

Muchos problemas obligan a multiplicar por la misma matriz una y otra vez: un modelo de población que avanza año a año, una cadena de Markov o una recurrencia. Calcular $A^{100}$ a mano es imposible en general, pero es trivial si $A$ es diagonal: basta elevar cada entrada. La idea de este tema es buscar **direcciones especiales** en las que $A$ actúa como un número, solo estirando o encogiendo. Esas direcciones son los **vectores propios**, y el factor de estiramiento es el **valor propio**.

## Definición

> [!tip] Definición
> Sea $A$ de $n \times n$. Un **vector propio** de $A$ es un vector $\mathbf x \neq \mathbf 0$ tal que
> $$A\mathbf x = \lambda\mathbf x$$
> para algún escalar $\lambda$. Un escalar $\lambda$ es un **valor propio** de $A$ si existe algún $\mathbf x \neq \mathbf 0$ con $A\mathbf x = \lambda\mathbf x$; ese $\mathbf x$ es un vector propio **asociado** a $\lambda$.

Geométricamente, $\mathbf x$ es vector propio si $A\mathbf x$ queda sobre la misma recta que $\mathbf x$: $A$ no lo gira, solo lo escala (y lo invierte si $\lambda < 0$).

![Vectores propios como direcciones que A no gira](adjuntos/Vectores%20propios%20como%20direcciones%20que%20A%20no%20gira.gif)

> [!example]- Transcripción de la animación
> Con $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$, un vector unitario $\mathbf x$ (azul) recorre el círculo unitario y la flecha $A\mathbf x$ recorre una elipse. Casi siempre $A\mathbf x$ (rojo) apunta en otra dirección que $\mathbf x$. En cuatro momentos, cuando $\mathbf x$ está sobre las rectas $y = x$ o $y = -x$, $A\mathbf x$ se vuelve verde y queda paralelo a $\mathbf x$: sobre $y = x$, $A\mathbf x = 3\mathbf x$; sobre $y = -x$, $A\mathbf x = 1\mathbf x$. Esas son las direcciones propias, con valores propios 3 y 1.

> [!warning] El vector cero no es vector propio
> $A\mathbf 0 = \lambda\mathbf 0$ vale para todo $\lambda$, así que la definición lo excluye. En cambio, el **valor propio** $\lambda = 0$ sí está permitido: significa que $A\mathbf x = \mathbf 0$ para algún $\mathbf x \neq \mathbf 0$.

**Verificar es fácil.** Con $A = \begin{bmatrix} 1 & 6 \\ 5 & 2 \end{bmatrix}$: $A\langle 6, -5\rangle = \langle -24, 20\rangle = -4\langle 6, -5\rangle$, así que $\langle 6, -5\rangle$ es vector propio con $\lambda = -4$. En cambio $A\langle 3, -2\rangle = \langle -9, 11\rangle$ no es múltiplo de $\langle 3, -2\rangle$.

## Espacio propio

$A\mathbf x = \lambda\mathbf x$ equivale a $(A - \lambda I)\mathbf x = \mathbf 0$. Por lo tanto:

> [!tip] Criterio
> $\lambda$ es valor propio de $A$ si y solo si $(A - \lambda I)\mathbf x = \mathbf 0$ tiene soluciones **no triviales**, es decir, si $A - \lambda I$ no es invertible.

> [!tip] Definición
> El **espacio propio** de $A$ asociado a $\lambda$ es $E_\lambda = \operatorname{Nul}(A - \lambda I)$: los vectores propios de $\lambda$ junto con el cero. Es un subespacio de $\mathbb{R}^n$.

**Ejemplo.** ¿Es 7 valor propio de $A = \begin{bmatrix} 1 & 6 \\ 5 & 2 \end{bmatrix}$? $A - 7I = \begin{bmatrix} -6 & 6 \\ 5 & -5 \end{bmatrix} \sim \begin{bmatrix} 1 & -1 \\ 0 & 0 \end{bmatrix}$ tiene una variable libre: sí, y $E_7 = \operatorname{Gen}\{\langle 1, 1\rangle\}$.

**Ejemplo.** $\lambda = 2$ es valor propio de $A = \begin{bmatrix} 4 & -1 & 6 \\ 2 & 1 & 6 \\ 2 & -1 & 8 \end{bmatrix}$. $A - 2I = \begin{bmatrix} 2 & -1 & 6 \\ 2 & -1 & 6 \\ 2 & -1 & 6 \end{bmatrix}$ tiene una sola ecuación, $2x_1 - x_2 + 6x_3 = 0$, y dos libres: $E_2 = \operatorname{Gen}\{\langle 1, 2, 0\rangle, \langle -3, 0, 1\rangle\}$, un plano.

## Propiedades

> [!tip] Valores propios de matrices triangulares
> Los valores propios de una matriz triangular son las entradas de su diagonal.

En $A - \lambda I$, triangular, las entradas diagonales son $a_{ii} - \lambda$; la matriz no es invertible exactamente cuando alguna es cero.

> [!tip] Invertibilidad
> $A$ es invertible si y solo si $0$ **no** es valor propio de $A$.

$0$ es valor propio si y solo si $A\mathbf x = \mathbf 0$ tiene soluciones no triviales, es decir, si $A$ no es invertible. Se agrega al teorema de la matriz invertible.

> [!tip] Teorema
> Vectores propios asociados a valores propios **distintos** son linealmente independientes.

Idea de la demostración: si fueran LD, se toma la primera $\mathbf v_{p+1}$ que es combinación de las anteriores, $\mathbf v_{p+1} = c_1\mathbf v_1 + \dots + c_p\mathbf v_p$. Aplicando $A$ y restando $\lambda_{p+1}$ veces la ecuación original se obtiene $\sum c_i(\lambda_i - \lambda_{p+1})\mathbf v_i = \mathbf 0$. Como los $\mathbf v_1, \dots, \mathbf v_p$ son LI y los $\lambda$ son distintos, todos los $c_i$ son cero, y entonces $\mathbf v_{p+1} = \mathbf 0$, una contradicción.

**Más relaciones útiles** (con $A\mathbf x = \lambda\mathbf x$, $\mathbf x \neq \mathbf 0$):
- $A^k\mathbf x = \lambda^k\mathbf x$: $\lambda^k$ es valor propio de $A^k$ con el mismo vector.
- Si $A$ es invertible, multiplicando por $A^{-1}$: $\mathbf x = \lambda A^{-1}\mathbf x$, así que $A^{-1}\mathbf x = \lambda^{-1}\mathbf x$ ($\lambda \neq 0$ porque $A$ es invertible).
- $A + cI$ tiene valor propio $\lambda + c$ con el mismo vector.

## Preguntas de repaso

> [!question]- ¿Por qué el espacio propio se define como $\operatorname{Nul}(A - \lambda I)$ y no solo como el conjunto de vectores propios?
> Porque el conjunto de vectores propios no contiene al cero y por eso no es subespacio. Agregándole el cero se obtiene exactamente el espacio nulo de $A - \lambda I$, que sí lo es.

> [!question]- ¿Cuáles son los valores propios de $\begin{bmatrix} 3 & 6 & -8 \\ 0 & 0 & 6 \\ 0 & 0 & 2 \end{bmatrix}$? ¿Es invertible?
> Es triangular: 3, 0 y 2. Como 0 es valor propio, no es invertible.

> [!question]- Si $\lambda$ es valor propio de $A$ invertible, demuestre que $\lambda^{-1}$ es valor propio de $A^{-1}$.
> $A\mathbf x = \lambda\mathbf x$ con $\mathbf x \neq \mathbf 0$. Como $A$ es invertible, $\lambda \neq 0$. Multiplicando por $A^{-1}$: $\mathbf x = \lambda A^{-1}\mathbf x$, o sea $A^{-1}\mathbf x = \lambda^{-1}\mathbf x$.

> [!question]- Una matriz de $3 \times 3$ tiene valores propios 1, 2 y 5. ¿Qué se puede decir de sus vectores propios?
> Tomando uno por cada valor propio, se obtienen tres vectores LI de $\mathbb{R}^3$: forman una base de $\mathbb{R}^3$.

> [!question]- ¿Cuáles son los valores y vectores propios de una reflexión en la recta $y = x$?
> Los vectores de la recta quedan fijos ($\lambda = 1$, $E_1 = \operatorname{Gen}\{\langle 1, 1\rangle\}$) y los perpendiculares se invierten ($\lambda = -1$, $E_{-1} = \operatorname{Gen}\{\langle 1, -1\rangle\}$).
