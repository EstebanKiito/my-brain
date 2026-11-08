---
ramo: "Álgebra Lineal"
tema: "Valores propios complejos"
tags:
  - algebra-lineal/valores-propios
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Rotaciones escaladas y la forma PCP⁻¹]]"
---

# Ejercicios de prueba de valores propios complejos

Preguntas de interrogaciones anteriores. Casi todas piden lo mismo: factorizar $A = PCP^{-1}$ con $C = \begin{bmatrix} a & -b \\ b & a \end{bmatrix}$. La receta es fija: valores propios con la fórmula cuadrática, vector propio de $\lambda = a - bi$ con una fila de $A - \lambda I$, y $P = [\operatorname{Re}\mathbf v\ \operatorname{Im}\mathbf v]$.

## Ejercicios

### 1. Factorización con valores propios $\frac12 \pm \frac32i$
Encuentre $P$ y $C$ con $A = PCP^{-1}$ para $A = \begin{bmatrix} 1 & -5 \\ \frac12 & 0 \end{bmatrix}$.

> [!example]- Solución
> $\det(A - \lambda I) = \lambda^2 - \lambda + \tfrac52$, con raíces $\lambda = \tfrac{1 \pm \sqrt{1 - 10}}{2} = \tfrac12 \pm \tfrac32i$.
> Para $\lambda = \tfrac12 - \tfrac32i$, la primera fila de $A - \lambda I$ es $[\tfrac12 + \tfrac32i\ \ -5]$, que da $x_1 = \dfrac{5}{\frac12 + \frac32i}x_2 = (1 - 3i)x_2$. Con $x_2 = 1$: $\mathbf v = \langle 1 - 3i, 1\rangle$.
> $$P = \begin{bmatrix} 1 & -3 \\ 1 & 0 \end{bmatrix}, \qquad C = \begin{bmatrix} \frac12 & -\frac32 \\ \frac32 & \frac12 \end{bmatrix}.$$

### 2. Factorización con valores propios $1 \pm i$
Lo mismo para $A = \begin{bmatrix} 2 & -1 \\ 2 & 0 \end{bmatrix}$.

> [!example]- Solución
> $\lambda^2 - 2\lambda + 2 = 0$ da $\lambda = 1 \pm i$. Para $\lambda = 1 - i$, la primera fila de $A - \lambda I$ es $[1 + i\ \ -1]$, así que $x_2 = (1 + i)x_1$ y $\mathbf v = \langle 1, 1 + i\rangle$.
> $$P = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}, \qquad C = \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}.$$
> $C$ rota $45°$ y escala por $\sqrt2$.

### 3. Factorización con raíces irracionales
Lo mismo para $A = \begin{bmatrix} 3 & -3 \\ 1 & 1 \end{bmatrix}$.

> [!example]- Solución
> $\lambda^2 - 4\lambda + 6 = 0$ da $\lambda = 2 \pm \sqrt2\,i$. Para $\lambda = 2 - \sqrt2\,i$, la segunda fila de $A - \lambda I$ es $[1\ \ -1 + \sqrt2\,i]$, que da $x_1 = (1 - \sqrt2\,i)x_2$. Con $x_2 = 1$: $\mathbf v = \langle 1 - \sqrt2\,i, 1\rangle$.
> $$P = \begin{bmatrix} 1 & -\sqrt2 \\ 1 & 0 \end{bmatrix}, \qquad C = \begin{bmatrix} 2 & -\sqrt2 \\ \sqrt2 & 2 \end{bmatrix}.$$

### 4. Otra factorización con $1 \pm i$
Lo mismo para $A = \begin{bmatrix} 2 & 1 \\ -2 & 0 \end{bmatrix}$.

> [!example]- Solución
> $\lambda^2 - 2\lambda + 2 = 0$: $\lambda = 1 \pm i$. Para $\lambda = 1 - i$, la primera fila es $[1 + i\ \ 1]$, así que $x_2 = -(1 + i)x_1$ y $\mathbf v = \langle 1, -1 - i\rangle$.
> $$P = \begin{bmatrix} 1 & 0 \\ -1 & -1 \end{bmatrix}, \qquad C = \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}.$$
> Tiene la misma $C$ que el ejercicio 2: ambas matrices son similares (son la misma rotación escalada en bases distintas).

### 5. Construir una matriz real con un valor propio dado
Encuentre una matriz real $A$ de $2 \times 2$ con valor propio $\lambda = -2 + 2i$ y vector propio $\mathbf v = \langle 1 + i, 3i\rangle$.

> [!example]- Solución
> Se usa el teorema al revés, escribiendo $\lambda = a - bi$ con $a = -2$ y $b = -2$. $P = [\operatorname{Re}\mathbf v\ \operatorname{Im}\mathbf v] = \begin{bmatrix} 1 & 1 \\ 0 & 3 \end{bmatrix}$ y $C = \begin{bmatrix} -2 & 2 \\ -2 & -2 \end{bmatrix}$:
> $$A = PCP^{-1} = \begin{bmatrix} -4 & \frac43 \\ -6 & 0 \end{bmatrix}.$$
> Control: $A\mathbf v = \langle -4(1 + i) + 4i, -6(1 + i)\rangle = \langle -4, -6 - 6i\rangle$, y $\lambda\mathbf v = \langle (-2 + 2i)(1 + i), (-2 + 2i)3i\rangle = \langle -4, -6 - 6i\rangle$.

### 6. Valores propios de la rotación de $90°$
Encuentre los valores y vectores propios de $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ y escriba $A = PCP^{-1}$.

> [!example]- Solución
> $\lambda^2 + 1 = 0$: $\lambda = \pm i$. Para $\lambda = -i$ ($a = 0$, $b = 1$), $A + iI = \begin{bmatrix} i & -1 \\ 1 & i \end{bmatrix}$ da $x_2 = ix_1$ y $\mathbf v = \langle 1, i\rangle$. $P = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$ y $C = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = A$: la matriz ya está en forma de rotación escalada ($r = 1$, $\varphi = 90°$).

## Preguntas de repaso

> [!question]- ¿Por qué en cada ejercicio se usó una sola fila de $A - \lambda I$?
> Porque para un valor propio, $A - \lambda I$ es singular: en $2 \times 2$ sus filas son proporcionales y la otra no aporta información. Usar la otra fila da un múltiplo complejo del mismo vector.

> [!question]- ¿Cómo se verifica rápido que $P$ y $C$ son correctas?
> Comprobando $AP = PC$, que evita invertir $P$.

> [!question]- En el ejercicio 5, ¿por qué $b = -2$ y no $2$?
> Porque el teorema usa $\lambda = a - bi$: $-2 + 2i = -2 - (-2)i$. Con esa convención, $C = \begin{bmatrix} a & -b \\ b & a \end{bmatrix} = \begin{bmatrix} -2 & 2 \\ -2 & -2 \end{bmatrix}$ y $P = [\operatorname{Re}\mathbf v\ \operatorname{Im}\mathbf v]$ funcionan juntas.
