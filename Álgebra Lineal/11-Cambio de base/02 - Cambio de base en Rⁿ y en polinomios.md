---
ramo: "Álgebra Lineal"
tema: "Cambio de base"
tags:
  - algebra-lineal/espacios
  - origen/complemento
prerrequisitos:
  - "[[01 - Matriz de cambio de coordenadas]]"
---

# Cambio de base en Rⁿ y en polinomios

La fórmula $P_{\mathcal C \leftarrow \mathcal B} = [\,[\mathbf b_1]_{\mathcal C} \cdots [\mathbf b_n]_{\mathcal C}\,]$ exige calcular $n$ vectores de coordenadas, es decir, resolver $n$ sistemas con la misma matriz. En $\mathbb{R}^n$ (y en cualquier espacio, pasando a coordenadas estándar) eso se hace de una vez con un solo escalonamiento. Esta nota da los procedimientos que se usan en los ejercicios.

## Con la base estándar

En $\mathbb{R}^n$, si $\mathcal E$ es la base estándar, las coordenadas de un vector en $\mathcal E$ son el vector mismo. Por eso

$$
P_{\mathcal E \leftarrow \mathcal B} = P_{\mathcal B} = [\,\mathbf b_1\ \cdots\ \mathbf b_n\,], \qquad \mathbf x = P_{\mathcal B}[\mathbf x]_{\mathcal B}, \qquad [\mathbf x]_{\mathcal B} = P_{\mathcal B}^{-1}\mathbf x .
$$

Ir de $\mathcal B$ a la estándar es multiplicar por la matriz con los $\mathbf b_i$ como columnas; ir al revés es resolver un sistema.

**Ejemplo.** Con $\mathbf b_1 = \langle 1, 0, 0\rangle$, $\mathbf b_2 = \langle -3, 4, 0\rangle$, $\mathbf b_3 = \langle 3, -6, 3\rangle$, se tiene $P_{\mathcal B} = \begin{bmatrix} 1 & -3 & 3 \\ 0 & 4 & -6 \\ 0 & 0 & 3 \end{bmatrix}$. Para $\mathbf x = \langle -8, 2, 3\rangle$, sustitución hacia atrás en $P_{\mathcal B}[\mathbf x]_{\mathcal B} = \mathbf x$: $\gamma = 1$, $4\beta - 6 = 2$ da $\beta = 2$, y $\alpha - 6 + 3 = -8$ da $\alpha = -5$. $[\mathbf x]_{\mathcal B} = \langle -5, 2, 1\rangle$.

## Entre dos bases de $\mathbb{R}^n$

Calcular $[\mathbf b_j]_{\mathcal C}$ es resolver $[\mathbf c_1 \cdots \mathbf c_n]\mathbf y = \mathbf b_j$. Como todos los sistemas comparten la matriz, se escalonan juntos:

> [!tip] Procedimiento
> $$\big[\,\mathbf c_1\ \cdots\ \mathbf c_n \;\big|\; \mathbf b_1\ \cdots\ \mathbf b_n\,\big] \sim \big[\,I \;\big|\; P_{\mathcal C \leftarrow \mathcal B}\,\big].$$
> A la izquierda va la base **de llegada** y a la derecha la **de partida**. Equivalentemente, $P_{\mathcal C \leftarrow \mathcal B} = P_{\mathcal C}^{-1}P_{\mathcal B}$.

**Ejemplo.** $\mathbf b_1 = \langle -9, 1\rangle$, $\mathbf b_2 = \langle -5, -1\rangle$, $\mathbf c_1 = \langle 1, -4\rangle$, $\mathbf c_2 = \langle 3, -5\rangle$:

$$
\left[\begin{array}{cc|cc} 1 & 3 & -9 & -5 \\ -4 & -5 & 1 & -1 \end{array}\right] \sim \left[\begin{array}{cc|cc} 1 & 0 & 6 & 4 \\ 0 & 1 & -5 & -3 \end{array}\right],
\qquad P_{\mathcal C \leftarrow \mathcal B} = \begin{bmatrix} 6 & 4 \\ -5 & -3 \end{bmatrix}.
$$

Comprobación: $6\mathbf c_1 - 5\mathbf c_2 = \langle 6 - 15, -24 + 25\rangle = \langle -9, 1\rangle = \mathbf b_1$.

**Ejemplo en ambos sentidos.** Con $\mathbf b_1 = \langle 1, -3\rangle$, $\mathbf b_2 = \langle -2, 4\rangle$, $\mathbf c_1 = \langle -7, 9\rangle$, $\mathbf c_2 = \langle -5, 7\rangle$, escalonar $[\mathbf b_1\ \mathbf b_2 \mid \mathbf c_1\ \mathbf c_2]$ da $P_{\mathcal B \leftarrow \mathcal C} = \begin{bmatrix} 5 & 3 \\ 6 & 4 \end{bmatrix}$, y su inversa es
$$P_{\mathcal C \leftarrow \mathcal B} = \frac12\begin{bmatrix} 4 & -3 \\ -6 & 5 \end{bmatrix} = \begin{bmatrix} 2 & -\frac32 \\ -3 & \frac52 \end{bmatrix}.$$

## En espacios de polinomios

Se pasa todo a coordenadas en la base estándar $\{1, t, t^2, \dots\}$ y se trabaja como en $\mathbb{R}^n$.

**Ejemplo.** En $\mathbb{P}_2$, $\mathcal B = \{1 - 2t + t^2,\ 3 - 5t + 4t^2,\ 2t + 3t^2\}$ y $\mathcal C = \{1, t, t^2\}$. Las columnas de $P_{\mathcal C \leftarrow \mathcal B}$ son los coeficientes:
$$P_{\mathcal C \leftarrow \mathcal B} = \begin{bmatrix} 1 & 3 & 0 \\ -2 & -5 & 2 \\ 1 & 4 & 3 \end{bmatrix}.$$
Para $[-1 + 2t]_{\mathcal B}$ se resuelve $P_{\mathcal C \leftarrow \mathcal B}\mathbf y = \langle -1, 2, 0\rangle$, que da $\langle 5, -2, 1\rangle$.

## Recuperar una base a partir de la matriz

Si se conoce $\mathcal C$ y $P_{\mathcal C \leftarrow \mathcal B}$, la base $\mathcal B$ sale **leyendo columnas**: la columna $j$ son las coordenadas de $\mathbf b_j$ en $\mathcal C$, así que $\mathbf b_j = p_{1j}\mathbf c_1 + \dots + p_{nj}\mathbf c_n$. Si en cambio se conoce $\mathcal B$ y se busca $\mathcal C$, primero se invierte: las columnas de $P_{\mathcal B \leftarrow \mathcal C} = (P_{\mathcal C \leftarrow \mathcal B})^{-1}$ dan cada $\mathbf c_j$ en coordenadas de $\mathcal B$.

> [!warning] Leer las columnas, no las filas
> Las coordenadas de cada vector de la base de partida están en las **columnas** de la matriz de cambio. Leerlas por filas da otros vectores (los de la transpuesta), un error frecuente.

## Preguntas de repaso

> [!question]- Para obtener $P_{\mathcal C \leftarrow \mathcal B}$ escalonando, ¿qué base va a la izquierda de la barra?
> La de llegada, $\mathcal C$. Se resuelven sistemas con matriz $[\mathbf c_1 \cdots \mathbf c_n]$ y lados derechos $\mathbf b_j$.

> [!question]- En $\mathbb{R}^n$, ¿qué es $P_{\mathcal E \leftarrow \mathcal B}$ si $\mathcal E$ es la base estándar?
> La matriz $[\mathbf b_1 \cdots \mathbf b_n]$: las coordenadas estándar de un vector son sus componentes.

> [!question]- $\mathcal C = \{\mathbf v_1, \mathbf v_2, \mathbf v_3\}$ y $P_{\mathcal C \leftarrow \mathcal B} = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ -3 & 1 & 1 \end{bmatrix}$. Exprese $\mathcal B$ con los $\mathbf v_i$.
> Por columnas: $\mathbf u_1 = \mathbf v_1 - 3\mathbf v_3$, $\mathbf u_2 = \mathbf v_2 + \mathbf v_3$, $\mathbf u_3 = 2\mathbf v_1 + \mathbf v_2 + \mathbf v_3$.

> [!question]- ¿Por qué $P_{\mathcal C \leftarrow \mathcal B} = P_{\mathcal C}^{-1}P_{\mathcal B}$ en $\mathbb{R}^n$?
> Porque $\mathbf x = P_{\mathcal B}[\mathbf x]_{\mathcal B}$ y $[\mathbf x]_{\mathcal C} = P_{\mathcal C}^{-1}\mathbf x$: se pasa de $\mathcal B$ a la estándar y de la estándar a $\mathcal C$.
