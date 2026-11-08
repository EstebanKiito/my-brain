---
ramo: "Álgebra Lineal"
tema: "Ortogonalidad y complemento ortogonal"
tags:
  - algebra-lineal/ortogonalidad
  - origen/complemento
prerrequisitos:
  - "[[04 - Ángulo, ortogonalidad y teorema de Pitágoras]]"
  - "[[03 - Espacio fila y teorema del rango]]"
---

# Complemento ortogonal

El último bloque del curso vuelve a la geometría del producto punto, ahora aplicada a subespacios. La pregunta motora es práctica: si un sistema $A\mathbf x = \mathbf b$ no tiene solución, ¿cuál es el $\mathbf x$ que **más se acerca**? Para responderla hace falta saber qué es "perpendicular a un subespacio" y cómo proyectar sobre él. Esta nota define el primer concepto: el **complemento ortogonal**.

## Repaso en notación matricial

El producto punto se escribe también como producto de matrices: $\mathbf u \cdot \mathbf v = \mathbf u^T\mathbf v$. La norma es $\|\mathbf v\| = \sqrt{\mathbf v^T\mathbf v}$, la distancia $d(\mathbf u, \mathbf v) = \|\mathbf u - \mathbf v\|$, y $\mathbf u, \mathbf v$ son **ortogonales** si $\mathbf u^T\mathbf v = 0$, lo que por Pitágoras equivale a $\|\mathbf u + \mathbf v\|^2 = \|\mathbf u\|^2 + \|\mathbf v\|^2$.

## Definición

> [!tip] Definición
> Si $W$ es un subespacio de $\mathbb{R}^n$, su **complemento ortogonal** es
> $$W^\perp = \{\mathbf z \in \mathbb{R}^n : \mathbf z \cdot \mathbf w = 0 \text{ para todo } \mathbf w \in W\},$$
> el conjunto de vectores ortogonales a **todo** $W$.

![Complemento ortogonal de un plano](adjuntos/Complemento%20ortogonal%20de%20un%20plano.png)

> [!example]- Transcripción de la imagen
> Un plano $W$ que pasa por el origen y la recta $L$ perpendicular a él por el origen. Un vector $\mathbf w$ en el plano y un vector $\mathbf z$ en la recta forman un ángulo recto. Todo vector de $L$ es ortogonal a todo vector de $W$: $L = W^\perp$ y $W = L^\perp$.

> [!tip] Propiedades
> 1. $\mathbf x \in W^\perp$ si y solo si $\mathbf x$ es ortogonal a cada vector de un **conjunto generador** de $W$.
> 2. $W^\perp$ es un subespacio de $\mathbb{R}^n$.
> 3. $\dim W + \dim W^\perp = n$, y $(W^\perp)^\perp = W$.

La propiedad 1 es la que hace calculable el complemento: si $\mathbf x$ es ortogonal a $\mathbf w_1, \dots, \mathbf w_p$, es ortogonal a cualquier combinación de ellos (por distributividad). No hay que revisar los infinitos vectores de $W$, solo los generadores.

## Cálculo: un espacio nulo

> [!tip] Teorema
> Para $A$ de $m \times n$:
> $$(\operatorname{Fil} A)^\perp = \operatorname{Nul} A, \qquad (\operatorname{Col} A)^\perp = \operatorname{Nul} A^T .$$

La primera es la regla fila-vector: $A\mathbf x = \mathbf 0$ dice que $\mathbf x$ tiene producto punto cero con cada fila de $A$, o sea, con un generador de $\operatorname{Fil} A$. La segunda es la primera aplicada a $A^T$.

> [!tip] Receta
> Para encontrar $W^\perp$ con $W = \operatorname{Gen}\{\mathbf w_1, \dots, \mathbf w_p\}$: poner los $\mathbf w_i$ **como filas** de una matriz y calcular su espacio nulo.

**Ejemplo.** $W = \operatorname{Gen}\{\langle 1, 1, 1, 1\rangle, \langle -1, -1, 1, -2\rangle, \langle 2, 2, -2, 2\rangle\}$. El espacio nulo de la matriz con esas filas es $\operatorname{Gen}\{\langle -1, 1, 0, 0\rangle\}$: $W$ tiene dimensión 3 y $W^\perp$ es una recta en $\mathbb{R}^4$.

**Ejemplo con $\operatorname{Col} A$.** Para $(\operatorname{Col} A)^\perp$ se calcula $\operatorname{Nul} A^T$: se transpone y se escalona. Con $A = \begin{bmatrix} 1 & -1 & 0 & 1 \\ 2 & 2 & 2 & 0 \\ -1 & 1 & -1 & 1 \\ 2 & 2 & 1 & 2 \end{bmatrix}$, $A^T$ se reduce a una FER con tres pivotes y $x_4$ libre, y $(\operatorname{Col} A)^\perp = \operatorname{Gen}\{\langle -1, -1, -1, 1\rangle\}$.

> [!warning] Filas, no columnas
> Para $W^\perp$ los generadores van como **filas** (la condición es $\mathbf w_i^T\mathbf x = 0$). Ponerlos como columnas y calcular $\operatorname{Nul}$ da otra cosa: las relaciones de dependencia entre los generadores.

## Los cuatro subespacios, otra vez

Con esto, los cuatro subespacios de una matriz quedan emparejados de a dos y ortogonales:

| En $\mathbb{R}^n$ | En $\mathbb{R}^m$ |
|---|---|
| $\operatorname{Fil} A \perp \operatorname{Nul} A$, dimensiones $r$ y $n - r$ | $\operatorname{Col} A \perp \operatorname{Nul} A^T$, dimensiones $r$ y $m - r$ |

## Preguntas de repaso

> [!question]- ¿Qué es $W^\perp$ si $W$ es el plano $x + 2y - z = 0$ de $\mathbb{R}^3$?
> La recta generada por el normal, $\operatorname{Gen}\{\langle 1, 2, -1\rangle\}$: es exactamente el conjunto de vectores perpendiculares a todo el plano.

> [!question]- ¿Por qué basta verificar la ortogonalidad con los generadores de $W$?
> Porque si $\mathbf x \cdot \mathbf w_i = 0$ para cada generador, entonces $\mathbf x \cdot (c_1\mathbf w_1 + \dots + c_p\mathbf w_p) = c_1 \cdot 0 + \dots + c_p \cdot 0 = 0$ para cualquier vector de $W$.

> [!question]- Si $W$ es un subespacio de $\mathbb{R}^7$ de dimensión 4, ¿qué dimensión tiene $W^\perp$?
> $7 - 4 = 3$.

> [!question]- ¿Cuál es el único vector que está en $W$ y en $W^\perp$ a la vez?
> El cero: si $\mathbf x$ está en ambos, $\mathbf x \cdot \mathbf x = 0$, así que $\mathbf x = \mathbf 0$.
