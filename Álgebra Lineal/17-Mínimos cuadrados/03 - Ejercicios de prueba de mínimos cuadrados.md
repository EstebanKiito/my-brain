---
ramo: "Álgebra Lineal"
tema: "Mínimos cuadrados"
tags:
  - algebra-lineal/ortogonalidad
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Recta de mínimos cuadrados]]"
---

# Ejercicios de prueba de mínimos cuadrados

Preguntas de exámenes anteriores. Casi todas se resuelven con las ecuaciones normales $A^TA\mathbf x = A^T\mathbf b$; las de rectas, armando $X^TX$ con sumas.

## Ejercicios

### 1. Solución y mejor aproximación
$A = \begin{bmatrix} 1 & 2 \\ 2 & -2 \\ -1 & 1 \end{bmatrix}$ y $\mathbf b = \langle 3, -2, -4\rangle$. (a) Encuentre una solución de mínimos cuadrados. (b) Encuentre la mejor aproximación de $\mathbf b$ en $\operatorname{Col} A$.

> [!example]- Solución
> (a) $A^TA = \begin{bmatrix} 6 & -3 \\ -3 & 9 \end{bmatrix}$ y $A^T\mathbf b = \langle 3 - 4 + 4,\ 6 + 4 - 4\rangle = \langle 3, 6\rangle$. Resolviendo: $\hat{\mathbf x} = \langle 1, 1\rangle$.
> (b) $\hat{\mathbf b} = A\hat{\mathbf x} = \langle 3, 0, 0\rangle$. (El error es $\|\langle 0, -2, -4\rangle\| = 2\sqrt5$.)

### 2. Consistencia con parámetro y mínimos cuadrados
$A = \begin{bmatrix} 1 & 1 & 2 \\ \alpha & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ y $\mathbf b = \langle 1, 1, -1\rangle$. (a) ¿Para qué $\alpha$ es consistente $A\mathbf x = \mathbf b$? Resuélvalo. (b) Para los $\alpha$ que lo hacen inconsistente, encuentre todas las soluciones de mínimos cuadrados.

> [!example]- Solución
> (a) La tercera ecuación da $x_3 = -1$ y la segunda $\alpha x_1 = 1$. Si $\alpha \neq 0$: $x_1 = \tfrac1\alpha$ y $x_2 = 1 - x_1 - 2x_3 = 3 - \tfrac1\alpha$. Si $\alpha = 0$, la segunda ecuación es $0 = 1$: inconsistente.
> (b) Con $\alpha = 0$: $A^TA = \begin{bmatrix} 1 & 1 & 2 \\ 1 & 1 & 2 \\ 2 & 2 & 5 \end{bmatrix}$ y $A^T\mathbf b = \langle 1, 1, 1\rangle$. Escalonando se obtiene $x_3 = -1$ y $x_1 + x_2 = 3$:
> $$\hat{\mathbf x} = \langle 3, 0, -1\rangle + t\langle -1, 1, 0\rangle, \quad t \in \mathbb{R}.$$
> Hay infinitas porque, con $\alpha = 0$, las dos primeras columnas de $A$ son iguales.

### 3. Recta por tres puntos
Encuentre la recta de mínimos cuadrados $y = \beta_0 + \beta_1x$ para $(2, 4)$, $(3, 6)$ y $(4, 5)$.

> [!example]- Solución
> $n = 3$, $\sum x = 9$, $\sum x^2 = 29$, $\sum y = 15$ y $\sum xy = 8 + 18 + 20 = 46$. Resolviendo $\begin{bmatrix} 3 & 9 \\ 9 & 29 \end{bmatrix}\boldsymbol\beta = \begin{bmatrix} 15 \\ 46 \end{bmatrix}$: $\beta_0 = \tfrac72$ y $\beta_1 = \tfrac12$. La recta es $y = \tfrac72 + \tfrac12x$.

### 4. Recta con pendiente negativa
Encuentre la recta $y = \alpha + \beta x$ para $(2, 3)$, $(3, 2)$, $(5, 1)$ y $(6, 0)$.

> [!example]- Solución
> $n = 4$, $\sum x = 16$, $\sum x^2 = 74$, $\sum y = 6$ y $\sum xy = 6 + 6 + 5 + 0 = 17$. El sistema $\begin{bmatrix} 4 & 16 \\ 16 & 74 \end{bmatrix}\begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \begin{bmatrix} 6 \\ 17 \end{bmatrix}$ tiene determinante $296 - 256 = 40$, y por Cramer $\alpha = \frac{6 \cdot 74 - 16 \cdot 17}{40} = \frac{43}{10}$ y $\beta = \frac{4 \cdot 17 - 16 \cdot 6}{40} = -\frac{7}{10}$. La recta es $y = \tfrac{43}{10} - \tfrac{7}{10}x$.

### 5. Recta con la pendiente primero
Encuentre la recta $y = mx + n$ más cercana a $(1, 1)$, $(2, 2)$ y $(3, 4)$.

> [!example]- Solución
> Con incógnitas en el orden $(m, n)$, la matriz es $A = \begin{bmatrix} 1 & 1 \\ 2 & 1 \\ 3 & 1 \end{bmatrix}$, así que $A^TA = \begin{bmatrix} 14 & 6 \\ 6 & 3 \end{bmatrix}$ y $A^T\mathbf b = \langle 1 + 4 + 12, 7\rangle = \langle 17, 7\rangle$. El determinante es $42 - 36 = 6$: $m = \frac{17 \cdot 3 - 6 \cdot 7}{6} = \frac32$ y $n = \frac{14 \cdot 7 - 6 \cdot 17}{6} = -\frac23$. La recta es $y = \tfrac32x - \tfrac23$.

### 6. Un modelo para estimar
Se registran $(x, y) = (0, 1), (1, 1), (2, 2), (3, 2)$, con $x$ el número de sesiones e $y$ el puntaje. (a) Plantee $A\mathbf x = \mathbf b$ para $y = mx + c$. (b) Encuentre la recta de mínimos cuadrados. (c) Estime el puntaje con 4 sesiones.

> [!example]- Solución
> (a) Con incógnitas $(c, m)$: $A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}$ y $\mathbf b = \langle 1, 1, 2, 2\rangle$.
> (b) $A^TA = \begin{bmatrix} 4 & 6 \\ 6 & 14 \end{bmatrix}$ y $A^T\mathbf b = \langle 6, 11\rangle$. Determinante $56 - 36 = 20$: $c = \frac{6 \cdot 14 - 6 \cdot 11}{20} = \frac{9}{10}$ y $m = \frac{4 \cdot 11 - 6 \cdot 6}{20} = \frac25$. La recta es $y = \tfrac25x + \tfrac{9}{10}$.
> (c) $y(4) = \tfrac85 + \tfrac{9}{10} = \tfrac52$.

## Preguntas de repaso

> [!question]- En el ejercicio 2, ¿cómo se anticipa que habrá infinitas soluciones de mínimos cuadrados?
> Con $\alpha = 0$ las columnas 1 y 2 de $A$ son iguales (LD), así que $A^TA$ no es invertible y las ecuaciones normales tienen una variable libre.

> [!question]- ¿Qué ventaja tiene Cramer para resolver las ecuaciones normales de una recta?
> El sistema es de $2 \times 2$ y simétrico, así que Cramer da cada coeficiente con dos determinantes pequeños y sin fracciones intermedias.

> [!question]- ¿Qué hay que revisar al leer la solución de un ajuste $y = mx + n$?
> El orden de las columnas de la matriz de diseño: la primera componente de $\hat{\mathbf x}$ corresponde a la primera columna. Con $[x_j\ 1]$ sale primero la pendiente; con $[1\ x_j]$, primero el intercepto.
