---
ramo: "Álgebra Lineal"
tema: "Valores propios complejos"
tags:
  - algebra-lineal/valores-propios
  - origen/complemento
prerrequisitos:
  - "[[01 - Números complejos y valores propios complejos]]"
  - "[[01 - Diagonalización]]"
---

# Rotaciones escaladas y la forma PCP⁻¹

Una matriz real de $2 \times 2$ con valores propios complejos no se puede diagonalizar con matrices reales, pero sí se puede llevar a una forma casi tan simple: una **rotación escalada**. El teorema de esta nota dice que, en una base adecuada, multiplicar por $A$ es girar un ángulo fijo y escalar por un factor fijo. Eso explica las trayectorias en espiral o en elipse de los sistemas $\mathbf x_{k+1} = A\mathbf x_k$.

## La matriz modelo

> [!tip] Teorema
> La matriz $C = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$ ($a, b$ reales, no ambos cero) tiene valores propios $\lambda = a \pm bi$. Si $r = |\lambda| = \sqrt{a^2 + b^2}$ y $\varphi = \arg(a + bi)$,
> $$C = r\begin{bmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{bmatrix}.$$
> Multiplicar por $C$ es **rotar en un ángulo $\varphi$ y luego escalar por $r$**.

Los valores propios salen de $\det(C - \lambda I) = (a - \lambda)^2 + b^2 = 0$, o sea $\lambda = a \pm bi$. La forma polar es $a = r\cos\varphi$, $b = r\sin\varphi$.

**Ejemplo.** $C = \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}$: $r = \sqrt2$ y $\varphi = \tfrac\pi4$. Multiplicar por $C$ gira $45°$ y agranda por $\sqrt2$.

## Toda $2 \times 2$ con valores propios complejos es una rotación escalada

> [!tip] Teorema
> Sea $A$ real de $2 \times 2$ con un valor propio complejo $\lambda = a - bi$ ($b \neq 0$) y vector propio $\mathbf v \in \mathbb{C}^2$. Entonces
> $$A = PCP^{-1}, \qquad P = [\,\operatorname{Re}\mathbf v\ \ \operatorname{Im}\mathbf v\,], \qquad C = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}.$$

Separando $A\mathbf v = \lambda\mathbf v$ en partes real e imaginaria se obtiene $A(\operatorname{Re}\mathbf v) = a\operatorname{Re}\mathbf v + b\operatorname{Im}\mathbf v$ y $A(\operatorname{Im}\mathbf v) = -b\operatorname{Re}\mathbf v + a\operatorname{Im}\mathbf v$, que es exactamente $AP = PC$.

> [!warning] Signos: se usa $\lambda = a - bi$
> El teorema toma el valor propio con **menos** $bi$ y su vector propio. Con $C = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$ armada con esos $a$ y $b$. Si se toma el otro valor propio con su vector, hay que ser consistente: usar $\bar{\mathbf v}$ cambia el signo de $\operatorname{Im}\mathbf v$ y de $b$ a la vez. El control seguro es verificar $AP = PC$.

**Ejemplo.** $A = \begin{bmatrix} 0{,}5 & -0{,}6 \\ 0{,}75 & 1{,}1 \end{bmatrix}$ tiene $\lambda = 0{,}8 - 0{,}6i$ con $\mathbf v = \langle 2, -1 + 2i\rangle$. Entonces $\operatorname{Re}\mathbf v = \langle 2, -1\rangle$ e $\operatorname{Im}\mathbf v = \langle 0, 2\rangle$:
$$P = \begin{bmatrix} 2 & 0 \\ -1 & 2 \end{bmatrix}, \qquad C = \begin{bmatrix} 0{,}8 & -0{,}6 \\ 0{,}6 & 0{,}8 \end{bmatrix}.$$
Como $r = \sqrt{0{,}64 + 0{,}36} = 1$, $C$ es una rotación pura (de ángulo $\varphi$ con $\cos\varphi = 0{,}8$).

## Qué significa: trayectorias

En la base $\{\operatorname{Re}\mathbf v, \operatorname{Im}\mathbf v\}$ la matriz $A$ es $C$: cada paso de $\mathbf x_{k+1} = A\mathbf x_k$ gira un ángulo $\varphi$ y escala por $r$, y $P$ solo deforma ese giro.

- Si $r = 1$, los puntos recorren una **elipse** (un círculo deformado por $P$).
- Si $r < 1$, una **espiral hacia el origen**.
- Si $r > 1$, una **espiral hacia afuera**.

![Órbitas de matrices con valores propios complejos](adjuntos/%C3%93rbitas%20de%20matrices%20con%20valores%20propios%20complejos.png)

> [!example]- Transcripción de la imagen
> Dos paneles con las iteraciones $\mathbf x_{k+1} = A\mathbf x_k$ desde un punto $\mathbf x_0$, coloreadas según $k$. Izquierda: $A = \begin{bmatrix} 0{,}5 & -0{,}6 \\ 0{,}75 & 1{,}1 \end{bmatrix}$, con $\lambda = 0{,}8 \pm 0{,}6i$ y $|\lambda| = 1$; los puntos quedan sobre una elipse y la recorren una y otra vez. Derecha: $0{,}9$ veces una rotación de $0{,}4$ radianes, con $|\lambda| = 0{,}9$; los puntos giran y se acercan al origen en espiral.

## Preguntas de repaso

> [!question]- ¿Qué hace geométricamente $C = \begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}$?
> $a = 0$, $b = 2$: $r = 2$ y $\varphi = \tfrac\pi2$. Rota $90°$ y duplica el largo.

> [!question]- Para $A = \begin{bmatrix} 2 & -1 \\ 2 & 0 \end{bmatrix}$, encuentre $P$ y $C$ con $A = PCP^{-1}$.
> $\lambda^2 - 2\lambda + 2 = 0$ da $\lambda = 1 \pm i$. Con $\lambda = 1 - i$, la primera fila de $A - \lambda I$ es $[1 + i\ \ -1]$, que da el vector $\langle 1, 1 + i\rangle$. $P = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$ y $C = \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}$.

> [!question]- ¿Cómo se sabe, solo con los valores propios, si las iteraciones $A^k\mathbf x_0$ tienden a cero?
> Si los valores propios son complejos con $|\lambda| < 1$, cada paso escala por $|\lambda|$ (en la base adecuada) y los puntos espiralan hacia el origen.

> [!question]- ¿Por qué $A = PCP^{-1}$ no contradice que $A$ no sea diagonalizable sobre los reales?
> Porque $C$ no es diagonal: es la forma más simple posible con números reales cuando no hay vectores propios reales. Sobre los complejos sí se podría diagonalizar, con $D = \operatorname{diag}(\lambda, \bar\lambda)$.
