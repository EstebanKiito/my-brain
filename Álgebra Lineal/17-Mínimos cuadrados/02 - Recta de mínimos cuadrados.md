---
ramo: "Álgebra Lineal"
tema: "Mínimos cuadrados"
tags:
  - algebra-lineal/ortogonalidad
  - origen/complemento
prerrequisitos:
  - "[[01 - Problemas de mínimos cuadrados]]"
---

# Recta de mínimos cuadrados

La aplicación más común de los mínimos cuadrados es **ajustar una recta a datos**: dados puntos $(x_1, y_1), \dots, (x_n, y_n)$ que casi están alineados, encontrar la recta que mejor los representa. Es la regresión lineal de estadística, y se reduce a resolver un sistema sobredeterminado con las ecuaciones normales.

## Planteamiento

Se busca $y = \beta_0 + \beta_1x$. Si la recta pasara por todos los puntos, se cumpliría $\beta_0 + \beta_1x_j = y_j$ para cada $j$, es decir,

$$
X\boldsymbol\beta = \mathbf y, \qquad X = \begin{bmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n \end{bmatrix}, \quad \boldsymbol\beta = \begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix}, \quad \mathbf y = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix}.
$$

$X$ es la **matriz de diseño** (la columna de unos corresponde al término constante). Con más de dos puntos no alineados, el sistema es inconsistente.

> [!tip] Definición
> La **recta de mínimos cuadrados** es la que minimiza la suma de los cuadrados de los **residuos** $y_j - (\beta_0 + \beta_1x_j)$, las distancias verticales entre cada punto y la recta. Sus coeficientes son la solución de mínimos cuadrados de $X\boldsymbol\beta = \mathbf y$:
> $$X^TX\,\boldsymbol\beta = X^T\mathbf y .$$

![Recta de mínimos cuadrados y residuos](adjuntos/Recta%20de%20m%C3%ADnimos%20cuadrados%20y%20residuos.png)

> [!example]- Transcripción de la imagen
> Varios puntos de datos $(x_j, y_j)$ y la recta $y = \beta_0 + \beta_1x$. Para cada $x_j$ se marca el punto de la recta $(x_j, \beta_0 + \beta_1x_j)$ y un segmento vertical hasta el dato, rotulado "residuo". La recta de mínimos cuadrados es la que hace mínima la suma de los cuadrados de esos segmentos.

> [!tip] La forma de $X^TX$
> $$X^TX = \begin{bmatrix} n & \sum x_j \\ \sum x_j & \sum x_j^2 \end{bmatrix}, \qquad X^T\mathbf y = \begin{bmatrix} \sum y_j \\ \sum x_jy_j \end{bmatrix}.$$
> Armarlas con sumas es más rápido que multiplicar matrices.

## Ejemplo

Puntos $(2, 1)$, $(5, 2)$, $(7, 3)$, $(8, 3)$. Con $n = 4$, $\sum x_j = 22$, $\sum x_j^2 = 142$, $\sum y_j = 9$ y $\sum x_jy_j = 2 + 10 + 21 + 24 = 57$:

$$
\begin{bmatrix} 4 & 22 \\ 22 & 142 \end{bmatrix}\begin{bmatrix} \beta_0 \\ \beta_1 \end{bmatrix} = \begin{bmatrix} 9 \\ 57 \end{bmatrix} \quad\Longrightarrow\quad \beta_0 = \frac27, \quad \beta_1 = \frac{5}{14}.
$$

La recta es $y = \frac27 + \frac{5}{14}x$. Se puede usar para **predecir**: en $x = 10$, $y \approx \frac27 + \frac{50}{14} = \frac{27}{7}$.

> [!warning] El orden de las incógnitas
> Si el modelo se escribe $y = mx + n$ (pendiente primero), la matriz de diseño cambia de orden: columnas $x_j$ y luego $1$. Hay que ser consistente al leer la solución; un error típico es intercambiar pendiente e intercepto.

## Otros modelos

El mismo método sirve para cualquier modelo **lineal en los parámetros**: para una parábola $y = \beta_0 + \beta_1x + \beta_2x^2$, la matriz de diseño tiene columnas $1$, $x_j$ y $x_j^2$. Lo que importa es que los $\beta$ aparezcan linealmente, no que el gráfico sea una recta.

## Preguntas de repaso

> [!question]- ¿Por qué el residuo se mide en vertical y no perpendicular a la recta?
> Porque el modelo predice $y$ a partir de $x$: el error es la diferencia entre el $y$ observado y el predicho para el mismo $x$. Esas diferencias son las componentes de $\mathbf y - X\boldsymbol\beta$.

> [!question]- Encuentre la recta de mínimos cuadrados para $(2, 4)$, $(3, 6)$ y $(4, 5)$.
> $X^TX = \begin{bmatrix} 3 & 9 \\ 9 & 29 \end{bmatrix}$ y $X^T\mathbf y = \langle 15, 46\rangle$, de donde $\beta_0 = \tfrac72$ y $\beta_1 = \tfrac12$: $y = \tfrac72 + \tfrac12x$.

> [!question]- ¿Cuándo $X^TX$ no es invertible en un ajuste de recta?
> Cuando las columnas de $X$ son LD, es decir, cuando todos los $x_j$ son iguales. Entonces no hay una recta privilegiada (cualquier pendiente pasa por esa vertical).

> [!question]- Si los datos están exactamente sobre una recta, ¿qué entrega el método?
> Esa misma recta, con error cero: el sistema $X\boldsymbol\beta = \mathbf y$ es consistente.
