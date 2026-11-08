---
ramo: "Álgebra Lineal"
tema: "Diagonalización"
tags:
  - algebra-lineal/transformaciones
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Vectores propios y matriz de una transformación]]"
---

# Ejercicios de prueba de matrices de transformaciones

Preguntas de interrogaciones y exámenes anteriores sobre la matriz de una transformación respecto de bases no estándar y sobre diagonalizar transformaciones en espacios de polinomios. Siempre se trabaja en tres pasos: **pasar a coordenadas**, **multiplicar por la matriz** y **volver a vectores**.

## Ejercicios

### 1. Matriz entre espacios de polinomios
$T: \mathbb{P}_2 \to \mathbb{P}_4$, $T(p) = p + 2t^2p$. (a) Calcule $T(3 - 2t + t^2)$. (b) Encuentre su matriz respecto de las bases estándar.

> [!example]- Solución
> (a) $(3 - 2t + t^2)(1 + 2t^2) = 3 - 2t + 7t^2 - 4t^3 + 2t^4$.
> (b) $T(1) = 1 + 2t^2$, $T(t) = t + 2t^3$ y $T(t^2) = t^2 + 2t^4$. Sus coordenadas en $\{1, t, t^2, t^3, t^4\}$ son las columnas:
> $$[T] = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{bmatrix}.$$

### 2. Fórmula de una transformación a partir de $[T]_{\mathcal B}$
$\mathcal B = \{\langle 1, 0, 0\rangle, \langle 1, 1, 0\rangle, \langle 1, 1, 1\rangle\}$ y $[T]_{\mathcal B} = \begin{bmatrix} 1 & 1 & 0 \\ -1 & 3 & 2 \\ 0 & 2 & -2 \end{bmatrix}$. Encuentre $T\langle x, y, z\rangle$.

> [!example]- Solución
> Cada columna da $T(\mathbf b_j)$ en coordenadas $\mathcal B$: $T(\mathbf b_1) = \mathbf b_1 - \mathbf b_2 = \langle 0, -1, 0\rangle$, $T(\mathbf b_2) = \mathbf b_1 + 3\mathbf b_2 + 2\mathbf b_3 = \langle 6, 5, 2\rangle$ y $T(\mathbf b_3) = 2\mathbf b_2 - 2\mathbf b_3 = \langle 0, 0, -2\rangle$. Como $\langle x, y, z\rangle = (x - y)\mathbf b_1 + (y - z)\mathbf b_2 + z\mathbf b_3$:
> $$T\langle x, y, z\rangle = \langle 6y - 6z,\ -x + 6y - 5z,\ 2y - 4z\rangle .$$
> (Equivalentemente, la matriz estándar es $P[T]_{\mathcal B}P^{-1}$.)

### 3. Imagen y núcleo con bases no estándar
$T: \mathbb{P}_2 \to \mathbb{R}^3$ tiene matriz $\begin{bmatrix} 1 & 2 & -1 \\ 1 & 1 & 1 \\ 2 & 1 & 4 \end{bmatrix}$ respecto de $\mathcal B = \{x^2, 1 + x, 1 - x\}$ y $\mathcal C = \{\langle 1, 0, 1\rangle, \langle 1, 1, 1\rangle, \langle 1, 0, -1\rangle\}$. (a) Calcule $T(2x^2 - 4x - 2)$. (b) Dé una base del núcleo.

> [!example]- Solución
> (a) $2x^2 - 4x - 2 = 2x^2 + a(1 + x) + b(1 - x)$ con $a + b = -2$ y $a - b = -4$: $a = -3$, $b = 1$. Coordenadas $\langle 2, -3, 1\rangle$; multiplicando, $\langle -5, 0, 5\rangle$, que en $\mathcal C$ es $-5\langle 1, 0, 1\rangle + 5\langle 1, 0, -1\rangle = \langle 0, 0, -10\rangle$.
> (b) $\operatorname{Nul}$ de la matriz es $\operatorname{Gen}\{\langle -3, 2, 1\rangle\}$, que como polinomio es $-3x^2 + 2(1 + x) + (1 - x) = -3x^2 + x + 3$. Base del núcleo: $\{-3x^2 + x + 3\}$.

### 4. Imagen, núcleo e invertibilidad desde $[T]_{\mathcal B}$
$\mathcal B = \{\langle 1, 0, 0\rangle, \langle 1, 1, 0\rangle, \langle 1, 1, -2\rangle\}$ y $[T]_{\mathcal B} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 2 \end{bmatrix}$. (a) Calcule $T\langle 2, 0, 2\rangle$. (b) Base de $\operatorname{Nul} T$. (c) ¿Es invertible?

> [!example]- Solución
> (a) $\langle 2, 0, 2\rangle = 2\mathbf b_1 + \mathbf b_2 - \mathbf b_3$ (se resuelve el sistema triangular). $[T]_{\mathcal B}\langle 2, 1, -1\rangle = \langle 1, 0, 1\rangle$, así que $T\langle 2, 0, 2\rangle = \mathbf b_1 + \mathbf b_3 = \langle 2, 1, -2\rangle$.
> (b) La tercera fila de $[T]_{\mathcal B}$ es la suma de las dos primeras; $\operatorname{Nul}[T]_{\mathcal B} = \operatorname{Gen}\{\langle -1, -1, 1\rangle\}$, que corresponde a $-\mathbf b_1 - \mathbf b_2 + \mathbf b_3 = \langle -1, 0, -2\rangle$.
> (c) **No**: tiene núcleo no trivial ($\det[T]_{\mathcal B} = 0$).

### 5. Matriz de una transformación en $\mathbb{P}_2$ y diagonalizabilidad
$T: \mathbb{P}_2 \to \mathbb{P}_2$ cumple $T(x^2) = x$, $T(x - 1) = x + 1$ y $T(1) = 2$. (a) Calcule $T(x)$. (b) Encuentre $[T]_E$ con $E = \{x^2, x, 1\}$. (c) ¿Es diagonalizable?

> [!example]- Solución
> (a) $T(x) = T((x - 1) + 1) = (x + 1) + 2 = x + 3$.
> (b) Coordenadas en $\{x^2, x, 1\}$: $T(x^2) = x \to \langle 0, 1, 0\rangle$, $T(x) = x + 3 \to \langle 0, 1, 3\rangle$, $T(1) = 2 \to \langle 0, 0, 2\rangle$:
> $$[T]_E = \begin{bmatrix} 0 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 3 & 2 \end{bmatrix}.$$
> (c) **Sí**: es triangular inferior con valores propios $0, 1, 2$, distintos.

### 6. Una base que diagonaliza en $\mathbb{P}_1$
$[T]_{\mathcal B} = \begin{bmatrix} 1 & 1 \\ -2 & 4 \end{bmatrix}$ con $\mathcal B = \{1, t\}$. (a) Encuentre $T(a + bt)$. (b) Encuentre una base $\mathcal C$ con $[T]_{\mathcal C}$ diagonal.

> [!example]- Solución
> (a) $[T]_{\mathcal B}\langle a, b\rangle = \langle a + b, -2a + 4b\rangle$: $T(a + bt) = (a + b) + (-2a + 4b)t$.
> (b) $\det([T]_{\mathcal B} - \lambda I) = \lambda^2 - 5\lambda + 6 = (\lambda - 2)(\lambda - 3)$. Vectores propios: $\langle 1, 1\rangle$ para 2 y $\langle 1, 2\rangle$ para 3, que son los polinomios $1 + t$ y $1 + 2t$. Con $\mathcal C = \{1 + t, 1 + 2t\}$, $[T]_{\mathcal C} = \operatorname{diag}(2, 3)$.

### 7. Una base de polinomios propios en $\mathbb{P}_2$
$T(ax^2 + bx + c) = (a + 3b + 3c)x^2 + (-3a - 5b - 3c)x + (3a + 3b + c)$ con $\mathcal B = \{x^2, x, 1\}$. (a) Calcule $T(x^2 - x + 1)$. (b) Encuentre $[T]_{\mathcal B}$. (c) Encuentre una base $\mathcal C$ con $[T]_{\mathcal C}$ diagonal.

> [!example]- Solución
> (a) Con $a = 1$, $b = -1$, $c = 1$: $(1 - 3 + 3)x^2 + (-3 + 5 - 3)x + (3 - 3 + 1) = x^2 - x + 1$. Es un vector propio con $\lambda = 1$.
> (b) $[T]_{\mathcal B} = \begin{bmatrix} 1 & 3 & 3 \\ -3 & -5 & -3 \\ 3 & 3 & 1 \end{bmatrix}$ (coeficientes de $a$, $b$, $c$ por columnas).
> (c) Es la matriz diagonalizada en la teoría: $\lambda = 1$ con $\langle 1, -1, 1\rangle$ y $\lambda = -2$ con $\langle -1, 1, 0\rangle$ y $\langle -1, 0, 1\rangle$. Traducidos a polinomios: $\mathcal C = \{x^2 - x + 1,\ -x^2 + x,\ -x^2 + 1\}$, y $[T]_{\mathcal C} = \operatorname{diag}(1, -2, -2)$.

## Preguntas de repaso

> [!question]- ¿Cuál es el error más común al usar $[T]_{\mathcal B}^{\mathcal C}$?
> Olvidar traducir: el resultado de multiplicar son **coordenadas en $\mathcal C$**, no el vector. Hay que combinar los vectores de $\mathcal C$ con esos pesos.

> [!question]- En el ejercicio 4(b), ¿por qué el vector del núcleo no es $\langle -1, -1, 1\rangle$?
> Porque ese vector son coordenadas en $\mathcal B$. El vector de $\mathbb{R}^3$ es $-\mathbf b_1 - \mathbf b_2 + \mathbf b_3$.

> [!question]- ¿Qué relación hay entre diagonalizar $[T]_{\mathcal B}$ y encontrar una base que diagonaliza $T$?
> Los vectores propios de $[T]_{\mathcal B}$ son las coordenadas en $\mathcal B$ de los vectores propios de $T$. Traducidos de vuelta a $V$, forman la base buscada.
