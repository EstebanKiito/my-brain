---
ramo: "Álgebra Lineal"
tema: "Transformaciones lineales"
tags:
  - algebra-lineal/transformaciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Transformaciones y linealidad]]"
---

# Matriz estándar de una transformación lineal

Toda transformación matricial es lineal. El resultado central de esta nota es el recíproco: **toda transformación lineal de $\mathbb{R}^n$ en $\mathbb{R}^m$ es una multiplicación por una matriz**, y esa matriz se construye mirando solo qué les pasa a los vectores $\mathbf e_1, \dots, \mathbf e_n$. Con esto, describir una rotación, una reflexión o una composición de ellas se reduce a seguir dos o tres vectores.

## El teorema

> [!tip] Teorema (matriz estándar)
> Si $T: \mathbb{R}^n \to \mathbb{R}^m$ es lineal, existe una **única** matriz $A$ de $m \times n$ tal que $T(\mathbf x) = A\mathbf x$ para todo $\mathbf x$, y es
> $$A = \big[\,T(\mathbf e_1)\ \ T(\mathbf e_2)\ \ \cdots\ \ T(\mathbf e_n)\,\big].$$
> Se llama **matriz estándar** de $T$ y se anota $[T]$.

**Demostración.** Todo $\mathbf x$ se escribe $\mathbf x = x_1\mathbf e_1 + \dots + x_n\mathbf e_n$. Por linealidad,
$$T(\mathbf x) = x_1T(\mathbf e_1) + \dots + x_nT(\mathbf e_n) = \big[T(\mathbf e_1) \cdots T(\mathbf e_n)\big]\mathbf x .$$
La unicidad sale de que $A\mathbf e_j$ es la columna $j$ de $A$, así que cualquier matriz que funcione tiene como columna $j$ a $T(\mathbf e_j)$. $\blacksquare$

**Ejemplo.** La dilatación $T(\mathbf x) = 3\mathbf x$ en $\mathbb{R}^2$ manda $\mathbf e_1 \mapsto \langle 3, 0\rangle$ y $\mathbf e_2 \mapsto \langle 0, 3\rangle$, así que $[T] = \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix}$.

## Rotaciones

Sea $T$ la rotación de $\mathbb{R}^2$ en un ángulo $\varphi$ antihorario en torno al origen (es lineal: rotar una suma es sumar las rotaciones). El vector $\mathbf e_1$, de largo 1 sobre el eje $x$, termina en $\langle \cos\varphi, \sin\varphi\rangle$. El vector $\mathbf e_2$, que está $90°$ más adelante, termina en $\langle \cos(\varphi + \tfrac\pi2), \sin(\varphi + \tfrac\pi2)\rangle = \langle -\sin\varphi, \cos\varphi\rangle$. Entonces

$$
[T] = \begin{bmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{bmatrix}.
$$

Con $\varphi = \tfrac\pi2$ se recupera $\langle x_1, x_2\rangle \mapsto \langle -x_2, x_1\rangle$.

## Catálogo de transformaciones del plano

Para cada una basta ver adónde van $\mathbf e_1$ y $\mathbf e_2$ (imaginando el cuadrado unitario que forman).

| Transformación | Matriz estándar | Qué hace con $\mathbf e_1$, $\mathbf e_2$ |
|---|---|---|
| Reflexión en el eje $x_1$ | $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ | $\mathbf e_2 \mapsto -\mathbf e_2$ |
| Reflexión en el eje $x_2$ | $\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ | $\mathbf e_1 \mapsto -\mathbf e_1$ |
| Reflexión en la recta $x_2 = x_1$ | $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ | intercambia $\mathbf e_1$ y $\mathbf e_2$ |
| Reflexión en la recta $x_2 = -x_1$ | $\begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}$ | $\mathbf e_1 \mapsto -\mathbf e_2$, $\mathbf e_2 \mapsto -\mathbf e_1$ |
| Reflexión en el origen | $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$ | invierte ambos (giro de $180°$) |
| Contracción o expansión horizontal | $\begin{bmatrix} k & 0 \\ 0 & 1 \end{bmatrix}$ | escala $\mathbf e_1$ por $k$ |
| Contracción o expansión vertical | $\begin{bmatrix} 1 & 0 \\ 0 & k \end{bmatrix}$ | escala $\mathbf e_2$ por $k$ |
| Trasquilado horizontal | $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ | $\mathbf e_2 \mapsto \langle k, 1\rangle$: el cuadrado se inclina de lado |
| Trasquilado vertical | $\begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}$ | $\mathbf e_1 \mapsto \langle 1, k\rangle$ |
| Proyección sobre el eje $x_1$ | $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ | $\mathbf e_2 \mapsto \mathbf 0$: el cuadrado se aplasta en un segmento |
| Proyección sobre el eje $x_2$ | $\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$ | $\mathbf e_1 \mapsto \mathbf 0$ |

## Composiciones paso a paso

Si $T$ consiste en aplicar varias transformaciones seguidas, se sigue a $\mathbf e_1$ y $\mathbf e_2$ por cada paso.

**Ejemplo.** Primero rotar $\tfrac\pi4$ y después reflejar en el eje vertical ($x \mapsto -x$). Con $c = \tfrac{\sqrt2}{2}$:

- $\mathbf e_1 \to \langle c, c\rangle \to \langle -c, c\rangle$;
- $\mathbf e_2 \to \langle -c, c\rangle \to \langle c, c\rangle$.

$$
[T] = \begin{bmatrix} -\tfrac{\sqrt2}{2} & \tfrac{\sqrt2}{2} \\ \tfrac{\sqrt2}{2} & \tfrac{\sqrt2}{2} \end{bmatrix}.
$$

> [!warning] El orden importa
> Reflejar primero y rotar después da otra matriz. Al seguir los vectores hay que aplicar los pasos en el orden del enunciado. Cuando se vea el producto de matrices, "primero $B$, después $A$" será $AB$, con la primera transformación a la **derecha**.

## Cuando no se conocen las imágenes de $\mathbf e_i$

Si el dato es la imagen de otros vectores, se escriben los $\mathbf e_i$ como combinación de ellos y se usa la superposición.

**Ejemplo.** $T\langle 1, 1\rangle = \langle 2, 3\rangle$ y $T\langle 1, -1\rangle = \langle 0, 5\rangle$. Como $\mathbf e_1 = \tfrac12(\langle 1, 1\rangle + \langle 1, -1\rangle)$ y $\mathbf e_2 = \tfrac12(\langle 1, 1\rangle - \langle 1, -1\rangle)$:

$$
T(\mathbf e_1) = \tfrac12(\langle 2, 3\rangle + \langle 0, 5\rangle) = \langle 1, 4\rangle, \qquad T(\mathbf e_2) = \tfrac12(\langle 2, 3\rangle - \langle 0, 5\rangle) = \langle 1, -1\rangle,
$$

y $T\langle x, y\rangle = \langle x + y,\ 4x - y\rangle$. Para que esto funcione, los vectores dados deben generar todo el dominio (si no, $T$ no queda determinada).

## Preguntas de repaso

> [!question]- Encuentre la matriz estándar de la rotación de $30°$ antihoraria.
> $\begin{bmatrix} \tfrac{\sqrt3}{2} & -\tfrac12 \\ \tfrac12 & \tfrac{\sqrt3}{2} \end{bmatrix}$, con columnas $\langle\cos 30°, \sin 30°\rangle$ y $\langle -\sin 30°, \cos 30°\rangle$.

> [!question]- ¿Por qué basta conocer $T(\mathbf e_1), \dots, T(\mathbf e_n)$ para conocer $T$ completa?
> Porque todo vector es combinación de los $\mathbf e_i$ con pesos iguales a sus componentes, y una transformación lineal respeta las combinaciones lineales.

> [!question]- Sea $T: \mathbb{R}^3 \to \mathbb{R}^2$ con $T\langle x, y, z\rangle = \langle x - z,\ 2y + z\rangle$. Dé $[T]$.
> Las columnas son $T(\mathbf e_1) = \langle 1, 0\rangle$, $T(\mathbf e_2) = \langle 0, 2\rangle$ y $T(\mathbf e_3) = \langle -1, 1\rangle$: $[T] = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 2 & 1 \end{bmatrix}$.

> [!question]- ¿Qué transformación es "reflejar en la recta $y = x$ y luego reflejar en el eje $x$"?
> $\mathbf e_1 \to \mathbf e_2 \to -\mathbf e_2$ y $\mathbf e_2 \to \mathbf e_1 \to \mathbf e_1$. La matriz $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$ es una rotación de $-90°$: dos reflexiones componen una rotación.
