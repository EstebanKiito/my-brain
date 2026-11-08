---
ramo: "Álgebra Lineal"
tema: "Espacios y subespacios vectoriales"
tags:
  - algebra-lineal/espacios
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Independencia lineal y bases]]"
---

# Ejercicios de prueba de subespacios y bases

Preguntas de interrogaciones y exámenes anteriores, casi todas con el mismo esquema: demostrar que un conjunto de polinomios o matrices es subespacio y encontrarle una base. El método que más rinde es **traducir la condición a ecuaciones sobre los coeficientes**, despejar y escribir el conjunto como un generado.

## Ejercicios

### 1. Matrices triangulares superiores
¿Es $H = \left\{\begin{bmatrix} a & b \\ 0 & d \end{bmatrix} : a, b, d \in \mathbb{R}\right\}$ un subespacio de $M_{2 \times 2}$?

> [!example]- Solución
> **Sí.** $\begin{bmatrix} a & b \\ 0 & d \end{bmatrix} = a\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + b\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} + d\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$, así que $H$ es el generado de esas tres matrices, y todo generado es subespacio.

### 2. Productos con matrices diagonales
Sea $M = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ y $S = \{A \in M_{2 \times 2} : A = DM \text{ para alguna } D = \begin{bmatrix} \alpha & 0 \\ 0 & \beta \end{bmatrix}\}$. ¿Es $S$ subespacio?

> [!example]- Solución
> **Sí.** $DM = \begin{bmatrix} \alpha & 2\alpha \\ 3\beta & 4\beta \end{bmatrix} = \alpha\begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix} + \beta\begin{bmatrix} 0 & 0 \\ 3 & 4 \end{bmatrix}$. $S$ es un generado.

### 3. Polinomios con $p(1) = p(-1)$
$H = \{p \in \mathbb{P}_2 : p(1) = p(-1)\}$. (a) Pruebe que es subespacio. (b) Escríbalo como generado. (c) ¿Son LI $1 + x - x^2$, $1 + x$ y $1 - x^2$?

> [!example]- Solución
> (a) El nulo cumple $0 = 0$. Si $p, q \in H$: $(p + q)(1) = p(1) + q(1) = p(-1) + q(-1) = (p + q)(-1)$, e igual con $cp$.
> (b) Con $p = a + bx + cx^2$: $a + b + c = a - b + c$, o sea $b = 0$. $H = \{a + cx^2\} = \operatorname{Gen}\{1, x^2\}$.
> (c) $\alpha(1 + x - x^2) + \beta(1 + x) + \gamma(1 - x^2) = 0$ da $\alpha + \beta + \gamma = 0$ (constante), $\alpha + \beta = 0$ ($x$) y $-\alpha - \gamma = 0$ ($x^2$). De las dos primeras, $\gamma = 0$; luego $\alpha = 0$ y $\beta = 0$. **LI.**

### 4. Polinomios con $p(1) = p(2)$
$E = \{p \in \mathbb{P}_2 : p(1) = p(2)\}$. Pruebe que es subespacio y encuentre una base.

> [!example]- Solución
> Es subespacio por el mismo argumento que el ejercicio anterior (la condición es una igualdad lineal en $p$). Con $p = ax^2 + bx + c$: $a + b + c = 4a + 2b + c$, o sea $b = -3a$. Entonces $p = a(x^2 - 3x) + c$, y $\{x^2 - 3x, 1\}$ genera $E$. Son LI (ninguno es múltiplo del otro): **base** $\{x^2 - 3x, 1\}$.

### 5. Polinomios de $\mathbb{P}_3$ con $p(1) = p(-1)$
Encuentre una base de $H = \{p \in \mathbb{P}_3 : p(1) = p(-1)\}$.

> [!example]- Solución
> Con $p = ax^3 + bx^2 + cx + d$: $a + b + c + d = -a + b - c + d$, o sea $c = -a$. Entonces $p = a(x^3 - x) + bx^2 + d$, y una base es $\{x^3 - x, x^2, 1\}$ (LI porque tienen grados distintos).

### 6. Matrices que conmutan con una fija
$H = \{A \in M_{2 \times 2} : NA = AN\}$ con $N = \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix}$. Pruebe que es subespacio y encuentre una base.

> [!example]- Solución
> Subespacio: $N0 = 0N$; si $NA = AN$ y $NB = BN$, $N(A + B) = NA + NB = AN + BN = (A + B)N$, e igual con $cA$.
> Con $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$:
> $$NA = \begin{bmatrix} a + 2c & b + 2d \\ -a + c & -b + d \end{bmatrix}, \qquad AN = \begin{bmatrix} a - b & 2a + b \\ c - d & 2c + d \end{bmatrix}.$$
> Igualando: $2c = -b$, $2d = 2a$, $-a = -d$ y $-b = 2c$. Es decir, $d = a$ y $b = -2c$:
> $$A = a\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + c\begin{bmatrix} 0 & -2 \\ 1 & 0 \end{bmatrix}.$$
> Base: $\left\{I, \begin{bmatrix} 0 & -2 \\ 1 & 0 \end{bmatrix}\right\}$.

### 7. Matrices que anula una matriz fija
$F = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ y $H = \{A \in M_{3 \times 2} : FA = 0\}$. Pruebe que es subespacio y encuentre una base.

> [!example]- Solución
> Subespacio: $F0 = 0$, $F(A + B) = FA + FB = 0$ y $F(cA) = cFA = 0$.
> $FA = 0$ significa que **cada columna de $A$ está en $\operatorname{Nul} F$**. De $x_1 + x_2 + x_3 = 0$ y $x_3 = 0$ sale $\operatorname{Nul} F = \operatorname{Gen}\{\langle -1, 1, 0\rangle\}$. Entonces $A = \begin{bmatrix} -s & -t \\ s & t \\ 0 & 0 \end{bmatrix}$ y una base es
> $$\left\{\begin{bmatrix} -1 & 0 \\ 1 & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & -1 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}\right\}.$$

### 8. V o F: independencia de polinomios en $\mathbb{P}_3$
$\{1 - t + t^3,\ 1 + t + 2t^2 - t^3,\ 1 - t - 4t^2,\ 3t^3\}$ es LI.

> [!example]- Solución
> **Verdadero.** Se ponen los coeficientes (en el orden $1, t, t^2, t^3$) como columnas:
> $$\begin{bmatrix} 1 & 1 & 1 & 0 \\ -1 & 1 & -1 & 0 \\ 0 & 2 & -4 & 0 \\ 1 & -1 & 0 & 3 \end{bmatrix}.$$
> Desarrollando por la última columna, el determinante es $3\begin{vmatrix} 1 & 1 & 1 \\ -1 & 1 & -1 \\ 0 & 2 & -4 \end{vmatrix} = 3(-8) = -24 \neq 0$. Las columnas son LI, y por lo tanto los polinomios también.

## Preguntas de repaso

> [!question]- ¿Cuál es el procedimiento general para encontrar una base de un subespacio de polinomios definido por condiciones?
> Escribir un polinomio genérico, traducir las condiciones a ecuaciones lineales en los coeficientes, despejar unos en función de otros, sacar los coeficientes libres como factores y verificar que los polinomios que acompañan sean LI.

> [!question]- ¿Por qué en el ejercicio 7 conviene pensar columna por columna?
> Porque $FA$ tiene como columnas $F$ por cada columna de $A$. La condición $FA = 0$ se separa en dos condiciones independientes del tipo "esta columna está en $\operatorname{Nul} F$".

> [!question]- ¿Cómo se decide la independencia de polinomios o matrices sin trabajar con ellos directamente?
> Pasando a sus coeficientes (coordenadas en la base estándar) y estudiando la independencia de esos vectores de $\mathbb{R}^n$: escalonando o, si son $n$ vectores, con el determinante.
