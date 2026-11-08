---
ramo: "Álgebra Lineal"
tema: "Mínimos cuadrados"
tags:
  - algebra-lineal/ortogonalidad
  - origen/complemento
prerrequisitos:
  - "[[01 - Proyección ortogonal]]"
  - "[[02 - Proceso de Gram-Schmidt y factorización QR]]"
---

# Problemas de mínimos cuadrados

En la práctica, los sistemas con más ecuaciones que incógnitas (mediciones con ruido, por ejemplo) casi nunca tienen solución. En vez de rendirse, se busca el $\mathbf x$ que deja a $A\mathbf x$ **lo más cerca posible** de $\mathbf b$. Ese es el problema de **mínimos cuadrados**, y la proyección ortogonal lo resuelve: el $A\mathbf x$ más cercano a $\mathbf b$ es la proyección de $\mathbf b$ sobre $\operatorname{Col} A$.

## Definición y geometría

> [!tip] Definición
> Si $A$ es de $m \times n$ y $\mathbf b \in \mathbb{R}^m$, una **solución de mínimos cuadrados** de $A\mathbf x = \mathbf b$ es un $\hat{\mathbf x} \in \mathbb{R}^n$ tal que
> $$\|\mathbf b - A\hat{\mathbf x}\| \leq \|\mathbf b - A\mathbf x\| \quad\text{para todo } \mathbf x \in \mathbb{R}^n .$$

El nombre viene de que $\|\mathbf b - A\mathbf x\|^2$ es una **suma de cuadrados** (de las diferencias en cada ecuación). Como $A\mathbf x$ recorre $\operatorname{Col} A$, el problema es encontrar el punto de $\operatorname{Col} A$ más cercano a $\mathbf b$, que por el teorema de la mejor aproximación es $\hat{\mathbf b} = \operatorname{proy}_{\operatorname{Col} A}\mathbf b$.

![Solución de mínimos cuadrados como proyección](adjuntos/Soluci%C3%B3n%20de%20m%C3%ADnimos%20cuadrados%20como%20proyecci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> El plano $\operatorname{Col} A$ y un vector $\mathbf b$ fuera de él. Desde $\mathbf b$ baja una perpendicular hasta $A\hat{\mathbf x}$, en el plano. Otros puntos del plano, $A\mathbf x$, están unidos a $\mathbf b$ con segmentos punteados más largos. $A\hat{\mathbf x}$ es el punto de $\operatorname{Col} A$ más cercano a $\mathbf b$.

## Primera estrategia: proyectar

Calcular $\hat{\mathbf b} = \operatorname{proy}_{\operatorname{Col} A}\mathbf b$ y resolver $A\hat{\mathbf x} = \hat{\mathbf b}$ (que sí es consistente). Funciona bien si las columnas de $A$ son **ortogonales**.

**Ejemplo.** $A = \begin{bmatrix} 1 & -6 \\ 1 & -2 \\ 1 & 1 \\ 1 & 7 \end{bmatrix}$ tiene columnas ortogonales. Con $\mathbf b = \langle -1, 2, 1, 6\rangle$: $\hat{\mathbf b} = \tfrac84\mathbf a_1 + \tfrac{45}{90}\mathbf a_2$, así que $\hat{\mathbf x} = \langle 2, \tfrac12\rangle$ directamente (los coeficientes de la proyección son las componentes de $\hat{\mathbf x}$).

## Segunda estrategia: ecuaciones normales

$\hat{\mathbf x}$ es solución de mínimos cuadrados si y solo si $\mathbf b - A\hat{\mathbf x}$ es ortogonal a $\operatorname{Col} A$, es decir, a cada columna de $A$: $A^T(\mathbf b - A\hat{\mathbf x}) = \mathbf 0$.

> [!tip] Teorema (ecuaciones normales)
> Las soluciones de mínimos cuadrados de $A\mathbf x = \mathbf b$ son exactamente las soluciones de
> $$A^TA\,\mathbf x = A^T\mathbf b .$$
> Este sistema **siempre es consistente**.

**Ejemplo.** $A = \begin{bmatrix} 4 & 0 \\ 0 & 2 \\ 1 & 1 \end{bmatrix}$, $\mathbf b = \langle 2, 0, 11\rangle$. $A^TA = \begin{bmatrix} 17 & 1 \\ 1 & 5 \end{bmatrix}$ y $A^T\mathbf b = \langle 19, 11\rangle$. Resolviendo, $\hat{\mathbf x} = \langle 1, 2\rangle$.

> [!tip] Error de mínimos cuadrados
> Es la distancia $\|\mathbf b - A\hat{\mathbf x}\|$. En el ejemplo, $A\hat{\mathbf x} = \langle 4, 4, 3\rangle$ y $\|\langle -2, -4, 8\rangle\| = \sqrt{84} = 2\sqrt{21}$.

**Puede haber infinitas soluciones.** Si las columnas de $A$ son LD, $A^TA$ no es invertible y las ecuaciones normales tienen variables libres: todas dan el mismo $A\hat{\mathbf x} = \hat{\mathbf b}$, pero distintos $\hat{\mathbf x}$. Por ejemplo, con $A$ de $6 \times 4$ cuya primera columna es la suma de las otras tres, se obtiene una recta de soluciones $\hat{\mathbf x} = \hat{\mathbf x}_p + t\,\mathbf v$ con $\mathbf v \in \operatorname{Nul} A$.

> [!tip] Teorema (unicidad)
> Son equivalentes: (1) $A\mathbf x = \mathbf b$ tiene una **única** solución de mínimos cuadrados para cada $\mathbf b$; (2) las columnas de $A$ son LI; (3) $A^TA$ es invertible. En ese caso,
> $$\hat{\mathbf x} = (A^TA)^{-1}A^T\mathbf b .$$

## Tercera estrategia: QR

Si $A = QR$ (columnas LI), las ecuaciones normales se simplifican: $A^TA = R^TQ^TQR = R^TR$ y $A^T\mathbf b = R^TQ^T\mathbf b$, y como $R^T$ es invertible queda
$$R\hat{\mathbf x} = Q^T\mathbf b ,$$
un sistema **triangular** que se resuelve por sustitución hacia atrás. Es la forma más estable numéricamente.

> [!warning] $\hat{\mathbf x}$ no es lo mismo que $\hat{\mathbf b}$
> $\hat{\mathbf x} \in \mathbb{R}^n$ es la "solución" (los pesos) y $\hat{\mathbf b} = A\hat{\mathbf x} \in \mathbb{R}^m$ es la **mejor aproximación** de $\mathbf b$ en $\operatorname{Col} A$. Las pruebas suelen pedir ambas cosas por separado.

## Preguntas de repaso

> [!question]- Si $A\mathbf x = \mathbf b$ es consistente, ¿qué son sus soluciones de mínimos cuadrados?
> Sus soluciones usuales: el error mínimo es 0, porque $\mathbf b \in \operatorname{Col} A$ y $\hat{\mathbf b} = \mathbf b$.

> [!question]- ¿Por qué las ecuaciones normales siempre son consistentes?
> Porque la proyección de $\mathbf b$ sobre $\operatorname{Col} A$ siempre existe y es de la forma $A\hat{\mathbf x}$; ese $\hat{\mathbf x}$ cumple $A^T(\mathbf b - A\hat{\mathbf x}) = \mathbf 0$.

> [!question]- ¿De dónde salen las ecuaciones normales?
> De pedir que el residuo $\mathbf b - A\hat{\mathbf x}$ esté en $(\operatorname{Col} A)^\perp = \operatorname{Nul} A^T$, o sea, $A^T(\mathbf b - A\hat{\mathbf x}) = \mathbf 0$.

> [!question]- Si las columnas de $A$ son ortogonales, ¿cómo se ven $A^TA$ y la solución?
> $A^TA$ es diagonal (con $\|\mathbf a_j\|^2$ en la diagonal), así que $\hat x_j = \frac{\mathbf b \cdot \mathbf a_j}{\mathbf a_j \cdot \mathbf a_j}$: son los coeficientes de la proyección.
