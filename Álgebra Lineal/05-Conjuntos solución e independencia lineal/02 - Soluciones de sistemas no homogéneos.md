---
ramo: "Álgebra Lineal"
tema: "Conjuntos solución e independencia lineal"
tags:
  - algebra-lineal/sistemas
  - origen/complemento
prerrequisitos:
  - "[[01 - Sistemas homogéneos y forma paramétrica]]"
---

# Soluciones de sistemas no homogéneos

Cuando el lado derecho no es cero, el conjunto solución ya no pasa por el origen, pero tiene exactamente la misma **forma** que el del sistema homogéneo con la misma matriz: es una copia trasladada. Este resultado responde muchas preguntas de prueba sin escalonar nada: qué forma tiene un conjunto solución, si otro lado derecho puede dar una recta o un plano, o cómo obtener la solución a partir de datos parciales.

## El teorema de la traslación

> [!tip] Teorema
> Si $A\mathbf x = \mathbf b$ es consistente y $\mathbf p$ es **una** solución particular, entonces el conjunto solución completo es
> $$\{\mathbf p + \mathbf v_h : A\mathbf v_h = \mathbf 0\},$$
> es decir, $\mathbf p$ más todas las soluciones del sistema homogéneo.

**Demostración.** Si $A\mathbf v_h = \mathbf 0$, entonces $A(\mathbf p + \mathbf v_h) = \mathbf b + \mathbf 0 = \mathbf b$. Recíprocamente, si $A\mathbf w = \mathbf b$, entonces $A(\mathbf w - \mathbf p) = \mathbf b - \mathbf b = \mathbf 0$, así que $\mathbf w = \mathbf p + (\mathbf w - \mathbf p)$ con $\mathbf w - \mathbf p$ solución homogénea. $\blacksquare$

**Ejemplo.** Con la matriz del ejemplo homogéneo anterior y $\mathbf b = \langle 7, -1, -4\rangle$:

$$
\left[\begin{array}{ccc|c} 3 & 5 & -4 & 7 \\ -3 & -2 & 4 & -1 \\ 6 & 1 & -8 & -4 \end{array}\right] \sim \left[\begin{array}{ccc|c} 1 & 0 & -\frac43 & -1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 0 \end{array}\right]
\ \Longrightarrow\
\mathbf x = \underbrace{\begin{bmatrix} -1 \\ 2 \\ 0 \end{bmatrix}}_{\mathbf p} + x_3\underbrace{\begin{bmatrix} \tfrac43 \\ 0 \\ 1 \end{bmatrix}}_{\text{homogénea}}.
$$

Es la recta homogénea desplazada para pasar por $\mathbf p$.

![Soluciones no homogéneas como traslación de las homogéneas](adjuntos/Soluciones%20no%20homog%C3%A9neas%20como%20traslaci%C3%B3n%20de%20las%20homog%C3%A9neas.png)

> [!example]- Transcripción de la imagen
> En $\mathbb{R}^3$, dos planos paralelos: el de abajo, que pasa por el origen, es el conjunto solución de $A\mathbf x = \mathbf 0$; el de arriba es el de $A\mathbf x = \mathbf b$. Un vector $\mathbf p$ que sale del origen lleva de uno al otro: el conjunto de $A\mathbf x = \mathbf b$ es el de $A\mathbf x = \mathbf 0$ trasladado por $\mathbf p$.

> [!tip] Consecuencia clave
> Si un sistema $A\mathbf x = \mathbf b$ es consistente, el **número de parámetros** de su solución depende solo de $A$ (de sus variables libres), no de $\mathbf b$. Todos los sistemas consistentes con la misma $A$ tienen conjuntos solución paralelos y "del mismo tamaño".

## Varios lados derechos con la misma matriz

Como lo que importa es $A$, se pueden resolver varios sistemas a la vez escalonando $[A \mid \mathbf b_1 \mid \mathbf b_2 \mid \cdots]$. Con $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{bmatrix}$:

| Lado derecho | Conjunto solución | Lectura geométrica |
|---|---|---|
| $\langle 0, 0, 0\rangle$ | $t\langle 1, -2, 1\rangle$ | tres planos que comparten una recta por el origen |
| $\langle 1, 4, 5\rangle$ | $\langle -2, 3, 0\rangle + t\langle 1, -2, 1\rangle$ | la misma recta trasladada |
| $\langle 2, 3, 0\rangle$ | vacío | los tres planos forman un prisma |

Ningún $\mathbf b$ puede dar una solución única ni un plano: si hay solución, es siempre una recta paralela a $\langle 1, -2, 1\rangle$.

## Trucos que aparecen en las pruebas

**La suma de las columnas da una solución particular.** Si $\mathbf a_1 + \dots + \mathbf a_n = \mathbf b$, entonces $\mathbf p = \langle 1, 1, \dots, 1\rangle$ resuelve $A\mathbf x = \mathbf b$, porque $A\mathbf p$ es justamente esa suma. Más en general, cualquier combinación conocida de las columnas entrega una solución particular: si $\mathbf a_1 - \mathbf a_2 = \mathbf c$, entonces $\langle 1, -1, 0, \dots\rangle$ resuelve $A\mathbf x = \mathbf c$.

**La FER da las homogéneas.** Si se conoce la FER de $A$, se conocen las soluciones de $A\mathbf x = \mathbf 0$ aunque no se conozca $A$. Juntando ambas ideas se obtiene el conjunto solución completo sin ver la matriz.

**Construir un sistema a partir de su solución.** Para que la solución sea la recta por $P(0, 1, -1)$ con dirección $\langle 1, 2, 3\rangle$, se eligen dos filas ortogonales a la dirección, como $\langle 2, -1, 0\rangle$ y $\langle 3, 0, -1\rangle$, y se toma $\mathbf b = A\mathbf p$:

$$
A = \begin{bmatrix} 2 & -1 & 0 \\ 3 & 0 & -1 \end{bmatrix}, \qquad \mathbf b = A\begin{bmatrix}0\\1\\-1\end{bmatrix} = \begin{bmatrix}-1\\1\end{bmatrix}.
$$

> [!warning] "Infinitas soluciones" no se hereda en ambos sentidos igual
> Si $A\mathbf x = \mathbf b$ tiene infinitas soluciones, $A\mathbf x = \mathbf 0$ también (mismas variables libres). Pero si $A\mathbf x = \mathbf 0$ tiene infinitas, $A\mathbf x = \mathbf b$ puede tener **ninguna**: la traslación solo existe si el sistema es consistente.

## Preguntas de repaso

> [!question]- Si $A\mathbf x = \mathbf b$ tiene como solución un plano, ¿puede $A\mathbf x = \mathbf c$ tener como solución una recta?
> No. Si $A\mathbf x = \mathbf c$ es consistente, su solución es una traslación de la homogénea, que es un plano (dos parámetros). Puede ser vacía, pero nunca una recta.

> [!question]- Las columnas de $A$ suman $\langle 3, 0, 1\rangle$ y la FER de $A$ es $\begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix}$. Resuelva $A\mathbf x = \langle 3, 0, 1\rangle$.
> Particular: $\langle 1, 1, 1\rangle$. Homogéneas: $x_1 = -2x_3$, $x_2 = x_3$, o sea $t\langle -2, 1, 1\rangle$. Solución: $\langle 1, 1, 1\rangle + t\langle -2, 1, 1\rangle$.

> [!question]- ¿Por qué la diferencia de dos soluciones de $A\mathbf x = \mathbf b$ es solución de $A\mathbf x = \mathbf 0$?
> Por linealidad: $A(\mathbf w_1 - \mathbf w_2) = A\mathbf w_1 - A\mathbf w_2 = \mathbf b - \mathbf b = \mathbf 0$.

> [!question]- V o F: la suma de dos soluciones de $A\mathbf x = \mathbf b$ es solución de $A\mathbf x = \mathbf b$.
> Falso si $\mathbf b \neq \mathbf 0$: $A(\mathbf w_1 + \mathbf w_2) = 2\mathbf b \neq \mathbf b$. Solo en el caso homogéneo la suma de soluciones es solución.
