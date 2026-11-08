---
ramo: "Álgebra Lineal"
tema: "Cholesky y descomposición en valores singulares"
tags:
  - algebra-lineal/factorizaciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Matrices simétricas y teorema espectral]]"
  - "[[03 - Espacio fila y teorema del rango]]"
---

# Descomposición en valores singulares

Las matrices simétricas se diagonalizan con una matriz ortogonal. ¿Y una matriz cualquiera, incluso rectangular? No tiene valores propios en general, pero sí admite algo casi igual de bueno: la **descomposición en valores singulares** (DVS), $A = U\Sigma V^T$, con $U$ y $V$ ortogonales y $\Sigma$ "diagonal". Geométricamente dice que **toda** transformación lineal es: rotar, estirar los ejes y volver a rotar. Es la factorización más importante en aplicaciones (compresión de imágenes, análisis de datos, rango numérico).

## Máximo de una forma cuadrática

> [!tip] Teorema
> Si $A$ es simétrica y $Q(\mathbf x) = \mathbf x^TA\mathbf x$, entre los vectores con $\|\mathbf x\| = 1$ el máximo de $Q$ es el **mayor valor propio** $\lambda_1$ y el mínimo es el **menor** $\lambda_n$. Se alcanzan en los vectores propios unitarios correspondientes.

En la forma diagonal, $Q = \lambda_1y_1^2 + \dots + \lambda_ny_n^2$ con $y_1^2 + \dots + y_n^2 = 1$: lo mejor es poner todo el peso en el coeficiente más grande.

**Aplicación.** Para $A = \begin{bmatrix} 4 & 11 & 14 \\ 8 & 7 & -2 \end{bmatrix}$, ¿qué unitario $\mathbf x$ maximiza $\|A\mathbf x\|$? Como $\|A\mathbf x\|^2 = \mathbf x^T(A^TA)\mathbf x$, es el máximo de la forma de $A^TA = \begin{bmatrix} 80 & 100 & 40 \\ 100 & 170 & 140 \\ 40 & 140 & 200 \end{bmatrix}$, cuyos valores propios son 360, 90 y 0. El máximo de $\|A\mathbf x\|$ es $\sqrt{360} = 6\sqrt{10}$, en $\mathbf v_1 = \langle \tfrac13, \tfrac23, \tfrac23\rangle$.

## Valores singulares

$A^TA$ es simétrica y sus valores propios son $\geq 0$ (porque $\mathbf x^TA^TA\mathbf x = \|A\mathbf x\|^2 \geq 0$).

> [!tip] Definición
> Los **valores singulares** de $A$ ($m \times n$) son las raíces de los valores propios de $A^TA$, en orden decreciente: $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_n \geq 0$. Si $\mathbf v_i$ es un vector propio unitario de $A^TA$ para $\sigma_i^2$, entonces $\|A\mathbf v_i\| = \sigma_i$.

En el ejemplo, $\sigma_1 = 6\sqrt{10}$, $\sigma_2 = 3\sqrt{10}$ y $\sigma_3 = 0$.

> [!tip] Teorema
> Si $\{\mathbf v_1, \dots, \mathbf v_n\}$ es una base ortonormal de vectores propios de $A^TA$ ordenada como arriba, y $r$ valores singulares son no nulos, entonces $\{A\mathbf v_1, \dots, A\mathbf v_r\}$ es una **base ortogonal de $\operatorname{Col} A$** y $\operatorname{rango} A = r$.

**Teorema de la matriz invertible (conclusión).** $A$ de $n \times n$ es invertible si y solo si tiene $n$ valores singulares no nulos.

## La descomposición

> [!tip] Teorema (DVS)
> Si $A$ es de $m \times n$ con rango $r$, existen $U$ ($m \times m$) y $V$ ($n \times n$) ortogonales y $\Sigma$ ($m \times n$) con
> $$A = U\Sigma V^T, \qquad \Sigma = \begin{bmatrix} D & 0 \\ 0 & 0 \end{bmatrix}, \quad D = \operatorname{diag}(\sigma_1, \dots, \sigma_r).$$
> Las columnas de $V$ son los **vectores singulares derechos** y las de $U$ los **izquierdos**.

![Forma de la matriz Sigma](adjuntos/Forma%20de%20la%20matriz%20Sigma.png)

> [!example]- Transcripción de la imagen
> $\Sigma$ tiene en la esquina superior izquierda el bloque diagonal $D$ con los $r$ valores singulares no nulos, y ceros en el resto: $m - r$ filas y $n - r$ columnas de ceros. $\Sigma$ tiene el mismo tamaño que $A$.

> [!tip] Algoritmo
> 1. Diagonalizar ortogonalmente $A^TA = PDP^T$, con los valores propios en orden decreciente.
> 2. $V = P$, y $\Sigma$ con las raíces de los valores propios no nulos.
> 3. Las primeras $r$ columnas de $U$ son $\mathbf u_i = \dfrac{A\mathbf v_i}{\sigma_i}$.
> 4. Si faltan columnas de $U$, se completa con vectores ortonormales (una base ortonormal de $\operatorname{Nul} A^T = (\operatorname{Col} A)^\perp$).

**Ejemplo.** Con la $A$ de $2 \times 3$ anterior, $V = \tfrac13\begin{bmatrix} 1 & -2 & 2 \\ 2 & -1 & -2 \\ 2 & 2 & 1 \end{bmatrix}$. $A\mathbf v_1 = \langle 18, 6\rangle$ y $A\mathbf v_2 = \langle 3, -9\rangle$, así que $\mathbf u_1 = \tfrac{1}{\sqrt{10}}\langle 3, 1\rangle$ y $\mathbf u_2 = \tfrac{1}{\sqrt{10}}\langle 1, -3\rangle$:
$$A = \begin{bmatrix} \frac{3}{\sqrt{10}} & \frac{1}{\sqrt{10}} \\ \frac{1}{\sqrt{10}} & -\frac{3}{\sqrt{10}} \end{bmatrix}\begin{bmatrix} 6\sqrt{10} & 0 & 0 \\ 0 & 3\sqrt{10} & 0 \end{bmatrix}V^T .$$

**Ejemplo con columnas por completar.** $A = \begin{bmatrix} 1 & -1 \\ -2 & 2 \\ 2 & -2 \end{bmatrix}$: $A^TA = \begin{bmatrix} 9 & -9 \\ -9 & 9 \end{bmatrix}$ tiene valores 18 y 0, con $\mathbf v_1 = \tfrac{1}{\sqrt2}\langle 1, -1\rangle$ y $\mathbf v_2 = \tfrac{1}{\sqrt2}\langle 1, 1\rangle$. $\sigma_1 = 3\sqrt2$ y $\mathbf u_1 = \frac{A\mathbf v_1}{3\sqrt2} = \tfrac13\langle 1, -2, 2\rangle$. Para $\mathbf u_2, \mathbf u_3$ se toma una base ortonormal del plano $x_1 - 2x_2 + 2x_3 = 0$: $\tfrac{1}{\sqrt5}\langle 2, 1, 0\rangle$ y $\tfrac{1}{\sqrt{45}}\langle -2, 4, 5\rangle$ (Gram-Schmidt).

![Descomposición en valores singulares de una matriz 2x2](adjuntos/Descomposici%C3%B3n%20en%20valores%20singulares%20de%20una%20matriz%202x2.png)

> [!example]- Transcripción de la imagen
> $A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}$. Izquierda: el círculo unitario con los vectores singulares derechos $\mathbf v_1$ (rojo) y $\mathbf v_2$ (verde), perpendiculares. Derecha: la imagen del círculo, una elipse; $A\mathbf v_1 = \sigma_1\mathbf u_1$ es su semieje mayor ($\sigma_1 \approx 6{,}71$) y $A\mathbf v_2 = \sigma_2\mathbf u_2$ el menor ($\sigma_2 \approx 2{,}24$), también perpendiculares.

> [!warning] Valores singulares no son valores propios
> Para una matriz no simétrica, los valores singulares (raíces de los valores propios de $A^TA$) no coinciden con los valores propios de $A$, y existen aunque $A$ sea rectangular. En la figura, los valores propios de $A$ son 3 y 5, pero los singulares son $\sqrt{45}$ y $\sqrt5$.

## Preguntas de repaso

> [!question]- ¿Cómo se lee el rango de $A$ en una DVS?
> Es el número de valores singulares no nulos, es decir, de entradas no nulas en la diagonal de $\Sigma$.

> [!question]- Si $A = U\Sigma V^T$, ¿cómo se diagonalizan ortogonalmente $A^TA$ y $AA^T$?
> $A^TA = V(\Sigma^T\Sigma)V^T$ y $AA^T = U(\Sigma\Sigma^T)U^T$: los vectores singulares son sus vectores propios y los $\sigma_i^2$ sus valores propios.

> [!question]- ¿Qué columnas de $U$ forman una base ortonormal de $\operatorname{Col} A$?
> Las primeras $r$, que corresponden a valores singulares no nulos. Las restantes son una base de $(\operatorname{Col} A)^\perp$.

> [!question]- Si $P$ es ortogonal, ¿tienen $PA$ y $A$ los mismos valores singulares?
> Sí: $(PA)^T(PA) = A^TP^TPA = A^TA$, así que tienen la misma $A^TA$.
