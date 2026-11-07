---
ramo: "Álgebra Lineal"
tema: "Transformaciones lineales"
tags:
  - algebra-lineal/transformaciones
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Transformaciones sobreyectivas e inyectivas]]"
---

# Ejercicios de prueba de transformaciones lineales

Preguntas de interrogaciones anteriores: decidir linealidad, construir la matriz estándar a partir de datos, componer transformaciones geométricas y clasificar en inyectiva o sobre. Las inversas y los productos de matrices aparecen en el tema siguiente; aquí todo se hace con superposición y escalonamiento.

## Ejercicios

### 1. ¿Es lineal?
Determine si $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T\langle x_1, x_2\rangle = \langle x_1 - 2x_2,\ x_1 - 3,\ 2x_1 - 5x_2\rangle$, es lineal.

> [!example]- Solución
> **No.** $T(\mathbf 0) = \langle 0, -3, 0\rangle \neq \mathbf 0$, y toda transformación lineal manda el cero al cero. El término constante $-3$ la hace afín.

### 2. Fórmula a partir de dos imágenes
Encuentre $T: \mathbb{R}^2 \to \mathbb{R}^2$ lineal con $T\langle 1, 1\rangle = \langle 2, 3\rangle$ y $T\langle 1, -1\rangle = \langle 0, 5\rangle$.

> [!example]- Solución
> $\mathbf e_1 = \tfrac12(\langle 1, 1\rangle + \langle 1, -1\rangle)$ y $\mathbf e_2 = \tfrac12(\langle 1, 1\rangle - \langle 1, -1\rangle)$, así que $T(\mathbf e_1) = \langle 1, 4\rangle$ y $T(\mathbf e_2) = \langle 1, -1\rangle$. Entonces $T\langle x, y\rangle = \langle x + y,\ 4x - y\rangle$.

### 3. Matriz, inyectividad y sobreyectividad
$T: \mathbb{R}^2 \to \mathbb{R}^3$ es lineal con $T\langle 0, -2\rangle = \langle -8, 6, -2\rangle$ y $T\langle 1, 1\rangle = \langle 5, 4, 2\rangle$. (a) Dé su matriz. (b) ¿Es inyectiva? (c) ¿Es sobre?

> [!example]- Solución
> (a) $T(\mathbf e_2) = -\tfrac12T\langle 0, -2\rangle = \langle 4, -3, 1\rangle$ y $T(\mathbf e_1) = T\langle 1, 1\rangle - T(\mathbf e_2) = \langle 1, 7, 1\rangle$:
> $$[T] = \begin{bmatrix} 1 & 4 \\ 7 & -3 \\ 1 & 1 \end{bmatrix}.$$
> (b) **Sí:** las dos columnas no son paralelas, así que son LI (pivote en cada columna).
> (c) **No:** es de $3 \times 2$, con a lo más 2 pivotes para 3 filas.

### 4. Rango, inyectividad y sobreyectividad de $A\mathbf x$
$A = \begin{bmatrix} 1 & 1 \\ -2 & -1 \\ -1 & -3 \end{bmatrix}$, $\mathbf y = \langle 2, -7, 4\rangle$ y $T(\mathbf x) = A\mathbf x$. (a) Dominio y codominio. (b) ¿Está $\mathbf y$ en el rango? (c) ¿Es sobre? (d) ¿Es inyectiva?

> [!example]- Solución
> (a) Dominio $\mathbb{R}^2$, codominio $\mathbb{R}^3$.
> (b) $[A \mid \mathbf y] \sim \left[\begin{array}{cc|c} 1 & 0 & 5 \\ 0 & 1 & -3 \\ 0 & 0 & 0 \end{array}\right]$: consistente, con $\mathbf x = \langle 5, -3\rangle$. **Sí.**
> (c) **No:** 2 pivotes para 3 filas.
> (d) **Sí:** las 2 columnas son pivote (no son paralelas).

### 5. Sobre pero no inyectiva
¿Es inyectiva o sobre $T\langle x, y, z, w\rangle = \langle x + z - w,\ 2x - y - w,\ 3x + 4y - z\rangle$?

> [!example]- Solución
> $[T] = \begin{bmatrix} 1 & 0 & 1 & -1 \\ 2 & -1 & 0 & -1 \\ 3 & 4 & -1 & 0 \end{bmatrix}$, que se reduce a una matriz con pivotes en las columnas 1, 2 y 3. Hay un pivote en cada fila: **sobre**. Es de $3 \times 4$, así que la cuarta columna queda libre: **no inyectiva** (esto último se sabía sin escalonar).

### 6. Rotar y después reflejar
Encuentre la matriz estándar de la transformación que primero rota $\tfrac\pi4$ antihorario y después refleja en el eje vertical.

> [!example]- Solución
> Con $c = \tfrac{\sqrt2}{2}$: $\mathbf e_1 \to \langle c, c\rangle \to \langle -c, c\rangle$ y $\mathbf e_2 \to \langle -c, c\rangle \to \langle c, c\rangle$. Entonces $[T] = \begin{bmatrix} -\tfrac{\sqrt2}{2} & \tfrac{\sqrt2}{2} \\ \tfrac{\sqrt2}{2} & \tfrac{\sqrt2}{2} \end{bmatrix}$. Es la reflexión en la recta que forma un ángulo de $\tfrac{3\pi}{8}$ con el eje $x$ (las columnas tienen largo 1 y la matriz es simétrica).

### 7. Tres pasos geométricos
Matriz estándar de: reflexión en la recta $y = x$, después rotación de $30°$ antihoraria, después reflexión en el eje $Y$.

> [!example]- Solución
> Se sigue cada vector por los tres pasos:
> - $\mathbf e_1 \to \mathbf e_2 \to \langle -\tfrac12, \tfrac{\sqrt3}{2}\rangle \to \langle \tfrac12, \tfrac{\sqrt3}{2}\rangle$;
> - $\mathbf e_2 \to \mathbf e_1 \to \langle \tfrac{\sqrt3}{2}, \tfrac12\rangle \to \langle -\tfrac{\sqrt3}{2}, \tfrac12\rangle$.
>
> $$[T] = \begin{bmatrix} \tfrac12 & -\tfrac{\sqrt3}{2} \\ \tfrac{\sqrt3}{2} & \tfrac12 \end{bmatrix},$$
> que es la rotación de $60°$: dos reflexiones y una rotación se combinan en una sola rotación.

### 8. Matriz con datos no estándar e imagen de un plano
$T: \mathbb{R}^3 \to \mathbb{R}^3$ es lineal con $T\langle 1, 0, 0\rangle = \langle 2, 7, 1\rangle$, $T\langle 1, 2, 0\rangle = \langle 6, 5, 1\rangle$ y $T\langle 1, 1, 1\rangle = \langle 6, 3, 2\rangle$. (a) Dé $[T]$. (b) Encuentre la imagen del plano $3x + 2y - z = 2$.

> [!example]- Solución
> (a) $\mathbf e_2 = \tfrac12(\langle 1, 2, 0\rangle - \mathbf e_1)$, así que $T(\mathbf e_2) = \tfrac12(\langle 6, 5, 1\rangle - \langle 2, 7, 1\rangle) = \langle 2, -1, 0\rangle$. Además $\mathbf e_3 = \langle 1, 1, 1\rangle - \mathbf e_1 - \mathbf e_2$, así que $T(\mathbf e_3) = \langle 6, 3, 2\rangle - \langle 2, 7, 1\rangle - \langle 2, -1, 0\rangle = \langle 2, -3, 1\rangle$:
> $$[T] = \begin{bmatrix} 2 & 2 & 2 \\ 7 & -1 & -3 \\ 1 & 0 & 1 \end{bmatrix}.$$
> (b) El plano en forma vectorial: punto $\langle 0, 0, -2\rangle$ y directores $\langle 1, 0, 3\rangle$, $\langle 0, 1, 2\rangle$. Su imagen es $T\langle 0, 0, -2\rangle + tT\langle 1, 0, 3\rangle + sT\langle 0, 1, 2\rangle$:
> $$\langle -4, 6, -2\rangle + t\langle 8, -2, 4\rangle + s\langle 6, -7, 2\rangle.$$
> Es un plano porque las imágenes de los directores no son paralelas ($T$ es inyectiva: su matriz tiene tres pivotes).

## Preguntas de repaso

> [!question]- ¿Qué estrategia comparten los ejercicios 2, 3 y 8?
> Expresar cada $\mathbf e_i$ como combinación de los vectores cuyas imágenes se conocen y aplicar superposición. Las columnas de $[T]$ son esas imágenes.

> [!question]- ¿Cómo se obtiene la imagen de un plano o una recta bajo una transformación lineal?
> Se escribe en forma vectorial y se aplica $T$ al punto y a cada director. Si las imágenes de los directores siguen siendo LI, la dimensión se conserva; si no, el objeto se aplasta.

> [!question]- En el ejercicio 7, ¿cómo se comprueba rápido que el resultado es una rotación?
> Sus columnas son $\langle \cos 60°, \sin 60°\rangle$ y $\langle -\sin 60°, \cos 60°\rangle$, que es exactamente la forma de la matriz de rotación.
