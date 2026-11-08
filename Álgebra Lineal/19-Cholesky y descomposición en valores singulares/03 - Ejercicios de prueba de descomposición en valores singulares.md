---
ramo: "Álgebra Lineal"
tema: "Cholesky y descomposición en valores singulares"
tags:
  - algebra-lineal/factorizaciones
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Descomposición en valores singulares]]"
---

# Ejercicios de prueba de descomposición en valores singulares

Preguntas de exámenes anteriores. La DVS aparece en casi todos los exámenes recientes, ya sea para calcularla o para leer información de una DVS dada. (La factorización de Cholesky no aparece en el banco de preguntas; su práctica está en la nota de teoría.)

## Ejercicios

### 1. DVS de una matriz de rango 1
Encuentre una DVS de $A = \begin{bmatrix} 4 & -2 \\ 2 & -1 \\ 0 & 0 \end{bmatrix}$.

> [!example]- Solución
> $A^TA = \begin{bmatrix} 20 & -10 \\ -10 & 5 \end{bmatrix}$, con traza 25 y determinante 0: valores propios 25 y 0. $\mathbf v_1 = \tfrac{1}{\sqrt5}\langle 2, -1\rangle$ y $\mathbf v_2 = \tfrac{1}{\sqrt5}\langle 1, 2\rangle$; $\sigma_1 = 5$.
> $\mathbf u_1 = \frac{A\mathbf v_1}{5} = \frac{1}{5\sqrt5}\langle 10, 5, 0\rangle = \tfrac{1}{\sqrt5}\langle 2, 1, 0\rangle$. Se completa con $\tfrac{1}{\sqrt5}\langle 1, -2, 0\rangle$ y $\langle 0, 0, 1\rangle$:
> $$U = \begin{bmatrix} \frac{2}{\sqrt5} & \frac{1}{\sqrt5} & 0 \\ \frac{1}{\sqrt5} & -\frac{2}{\sqrt5} & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 5 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}, \quad V = \begin{bmatrix} \frac{2}{\sqrt5} & \frac{1}{\sqrt5} \\ -\frac{1}{\sqrt5} & \frac{2}{\sqrt5} \end{bmatrix}.$$

### 2. DVS de una matriz de $3 \times 2$ de rango 2
Encuentre una DVS de $A = \begin{bmatrix} 7 & 1 \\ 0 & 0 \\ 5 & 5 \end{bmatrix}$.

> [!example]- Solución
> $A^TA = \begin{bmatrix} 74 & 32 \\ 32 & 26 \end{bmatrix}$: traza 100, determinante $1924 - 1024 = 900$, valores propios 90 y 10. $\mathbf v_1 = \tfrac{1}{\sqrt5}\langle 2, 1\rangle$ y $\mathbf v_2 = \tfrac{1}{\sqrt5}\langle -1, 2\rangle$; $\sigma_1 = 3\sqrt{10}$, $\sigma_2 = \sqrt{10}$.
> $\mathbf u_1 = \frac{A\mathbf v_1}{3\sqrt{10}} = \frac{\langle 15, 0, 15\rangle}{\sqrt5 \cdot 3\sqrt{10}} = \tfrac{1}{\sqrt2}\langle 1, 0, 1\rangle$ y $\mathbf u_2 = \frac{A\mathbf v_2}{\sqrt{10}} = \frac{\langle -5, 0, 5\rangle}{\sqrt{50}} = \tfrac{1}{\sqrt2}\langle -1, 0, 1\rangle$. Falta $\mathbf u_3 = \langle 0, 1, 0\rangle$:
> $$U = \begin{bmatrix} \frac{1}{\sqrt2} & -\frac{1}{\sqrt2} & 0 \\ 0 & 0 & 1 \\ \frac{1}{\sqrt2} & \frac{1}{\sqrt2} & 0 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 3\sqrt{10} & 0 \\ 0 & \sqrt{10} \\ 0 & 0 \end{bmatrix}, \quad V = \begin{bmatrix} \frac{2}{\sqrt5} & -\frac{1}{\sqrt5} \\ \frac{1}{\sqrt5} & \frac{2}{\sqrt5} \end{bmatrix}.$$

### 3. DVS con la diagonalización dada
Encuentre la DVS de $A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ sabiendo que $A^TA = PDP^{-1}$ con $P = \begin{bmatrix} 1 & 0 & -1 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$ y $D = \operatorname{diag}(2, 1, 0)$.

> [!example]- Solución
> Las columnas de $P$ son ortogonales; normalizándolas, $V = \begin{bmatrix} \frac{1}{\sqrt2} & 0 & -\frac{1}{\sqrt2} \\ \frac{1}{\sqrt2} & 0 & \frac{1}{\sqrt2} \\ 0 & 1 & 0 \end{bmatrix}$. $\sigma_1 = \sqrt2$ y $\sigma_2 = 1$. $\mathbf u_1 = \frac{A\mathbf v_1}{\sqrt2} = \frac{1}{\sqrt2}\cdot\frac{1}{\sqrt2}\langle 2, 0\rangle = \langle 1, 0\rangle$ y $\mathbf u_2 = A\mathbf v_2 = \langle 0, 1\rangle$:
> $$U = I_2, \qquad \Sigma = \begin{bmatrix} \sqrt2 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}.$$

### 4. DVS de una matriz de $4 \times 3$
Encuentre la DVS de $A = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 0 \end{bmatrix}$, sabiendo que los valores propios de $A^TA$ son 4, 2 y 0.

> [!example]- Solución
> $A^TA = \begin{bmatrix} 2 & 0 & -2 \\ 0 & 2 & 0 \\ -2 & 0 & 2 \end{bmatrix}$, con $\mathbf v_1 = \tfrac{1}{\sqrt2}\langle 1, 0, -1\rangle$ ($\lambda = 4$), $\mathbf v_2 = \langle 0, 1, 0\rangle$ ($\lambda = 2$) y $\mathbf v_3 = \tfrac{1}{\sqrt2}\langle 1, 0, 1\rangle$ ($\lambda = 0$). $\sigma_1 = 2$, $\sigma_2 = \sqrt2$.
> $\mathbf u_1 = \frac{A\mathbf v_1}{2} = \tfrac{1}{\sqrt2}\langle 1, 0, 1, 0\rangle$ y $\mathbf u_2 = \frac{A\mathbf v_2}{\sqrt2} = \tfrac{1}{\sqrt2}\langle 0, 1, 0, 1\rangle$. Se completa con $\tfrac{1}{\sqrt2}\langle 1, 0, -1, 0\rangle$ y $\tfrac{1}{\sqrt2}\langle 0, 1, 0, -1\rangle$, y $\Sigma$ es de $4 \times 3$ con diagonal $2, \sqrt2, 0$.

### 5. Leer información de una DVS dada
Sea
$$A = \underbrace{\begin{bmatrix} \frac13 & \frac{2}{\sqrt5} & -\frac{2}{\sqrt{45}} \\ -\frac23 & \frac{1}{\sqrt5} & \frac{4}{\sqrt{45}} \\ \frac23 & 0 & \frac{5}{\sqrt{45}} \end{bmatrix}}_{U}\begin{bmatrix} 3\sqrt2 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}\underbrace{\begin{bmatrix} \frac{1}{\sqrt2} & -\frac{1}{\sqrt2} \\ \frac{1}{\sqrt2} & \frac{1}{\sqrt2} \end{bmatrix}}_{V}{}^T$$
una DVS. Sin calcular $A$: (a) ¿cuál es su rango? (b) Diagonalice ortogonalmente $A^TA$ y $AA^T$. (c) Clasifique la forma cuadrática de $AA^T$. (d) Dé una base ortonormal de $\operatorname{Col} A$.

> [!example]- Solución
> (a) Un solo valor singular no nulo: rango 1.
> (b) $A^TA = V(\Sigma^T\Sigma)V^T$ con $P = V$ y $D = \operatorname{diag}(18, 0)$. $AA^T = U(\Sigma\Sigma^T)U^T$ con $P = U$ y $D = \operatorname{diag}(18, 0, 0)$.
> (c) Los valores propios de $AA^T$ son 18 y 0 (doble): **semidefinida positiva**.
> (d) La primera columna de $U$: $\left\{\langle \tfrac13, -\tfrac23, \tfrac23\rangle\right\}$.

### 6. Valores singulares y matrices ortogonales
Demuestre que si $P$ es ortogonal ($m \times m$) y $\sqrt\sigma$ es valor singular de $PA$, entonces también lo es de $A$.

> [!example]- Solución
> $(PA)^T(PA) = A^TP^TPA = A^TA$, porque $P^TP = I$. Así, $PA$ y $A$ tienen la misma matriz $A^TA$, los mismos valores propios $\sigma$ y, por lo tanto, los mismos valores singulares $\sqrt\sigma$.

## Preguntas de repaso

> [!question]- ¿Qué dos controles conviene hacer en cada DVS?
> Que $\|\mathbf u_i\| = 1$ (si no da 1, el $\sigma_i$ o el $\mathbf v_i$ están mal) y que $U\Sigma V^T$ reproduzca al menos una columna de $A$.

> [!question]- ¿Cómo se completan las columnas de $U$ que faltan?
> Con una base ortonormal de $(\operatorname{Col} A)^\perp = \operatorname{Nul} A^T$: se calcula ese espacio nulo y, si tiene dimensión mayor que 1, se ortonormaliza con Gram-Schmidt.

> [!question]- En el ejercicio 5, ¿por qué $AA^T$ es semidefinida y no definida positiva?
> Porque $A$ tiene rango 1 < 3: $AA^T$ tiene valor propio 0, y en esa dirección la forma vale cero.
