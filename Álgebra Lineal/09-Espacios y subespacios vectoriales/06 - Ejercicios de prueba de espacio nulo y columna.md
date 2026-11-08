---
ramo: "Álgebra Lineal"
tema: "Espacios y subespacios vectoriales"
tags:
  - algebra-lineal/espacios
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Espacio nulo, espacio columna y núcleo]]"
---

# Ejercicios de prueba de espacio nulo y columna

Preguntas de interrogaciones y exámenes anteriores sobre $\operatorname{Nul} A$, $\operatorname{Col} A$ y el núcleo y rango de transformaciones. Se repiten dos ideas: pertenecer a $\operatorname{Nul}$ se **comprueba** multiplicando, y pertenecer a $\operatorname{Col}$ se **resuelve** escalonando.

## Ejercicios

### 1. ¿Pertenece a Nul? ¿Pertenece a Col?
$A = \begin{bmatrix} 2 & 4 & -2 & 1 \\ -2 & -5 & 7 & 3 \\ 3 & 7 & -8 & 6 \end{bmatrix}$, $\mathbf u = \langle 3, -2, -1, 0\rangle$ y $\mathbf v = \langle 3, -1, 3\rangle$. (a) ¿$\mathbf u \in \operatorname{Nul} A$? (b) ¿$\mathbf v \in \operatorname{Col} A$?

> [!example]- Solución
> (a) $A\mathbf u = \langle 6 - 8 + 2,\ -6 + 10 - 7,\ 9 - 14 + 8\rangle = \langle 0, -3, 3\rangle \neq \mathbf 0$. **No.**
> (b) Escalonando, $A$ tiene pivotes en las columnas 1, 2 y 4: tres pivotes en tres filas, así que $\operatorname{Col} A = \mathbb{R}^3$. **Sí**, y sin resolver nada.

### 2. Bases de Nul y Col
$A = \begin{bmatrix} -2 & 4 & -2 & -4 \\ 2 & -6 & -3 & 1 \\ -3 & 8 & 2 & -3 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 6 & 5 \\ 0 & 2 & 5 & 3 \\ 0 & 0 & 0 & 0 \end{bmatrix}$. Encuentre bases de $\operatorname{Nul} A$ y $\operatorname{Col} A$.

> [!example]- Solución
> **Nul:** $x_1 = -6x_3 - 5x_4$ y $x_2 = -\tfrac52x_3 - \tfrac32x_4$, con $x_3, x_4$ libres. Base: $\{\langle -6, -\tfrac52, 1, 0\rangle, \langle -5, -\tfrac32, 0, 1\rangle\}$.
> **Col:** las columnas pivote son la 1 y la 2. Base: $\{\langle -2, 2, -3\rangle, \langle 4, -6, 8\rangle\}$, tomadas de $A$, no de la forma escalonada.

### 3. Una matriz con espacio columna dado
Encuentre $A$ con $\operatorname{Col} A = \{\langle b - c,\ 2b - 5d,\ b - 3c + 3d,\ -c + d\rangle : b, c, d \in \mathbb{R}\}$.

> [!example]- Solución
> Se separa por parámetros: $b\langle 1, 2, 1, 0\rangle + c\langle -1, 0, -3, -1\rangle + d\langle 0, -5, 3, 1\rangle$. Esos vectores son las columnas:
> $$A = \begin{bmatrix} 1 & -1 & 0 \\ 2 & 0 & -5 \\ 1 & -3 & 3 \\ 0 & -1 & 1 \end{bmatrix}.$$

### 4. Columnas dadas en términos de una base
$\{\mathbf u_1, \mathbf u_2, \mathbf u_3\}$ es LI en $\mathbb{R}^3$ y $A = [\mathbf u_2\ \ \mathbf u_2 - \mathbf u_3\ \ \mathbf u_3\ \ \mathbf u_1 + 4\mathbf u_2]$. Encuentre bases de $\operatorname{Col} A$ y $\operatorname{Nul} A$.

> [!example]- Solución
> Las columnas generan $\operatorname{Gen}\{\mathbf u_1, \mathbf u_2, \mathbf u_3\} = \mathbb{R}^3$ ($\mathbf u_2$, $\mathbf u_3 = \mathbf a_1 - \mathbf a_2$ y $\mathbf u_1 = \mathbf a_4 - 4\mathbf a_1$ se recuperan). La única relación es $\mathbf a_3 = \mathbf a_1 - \mathbf a_2$, así que las columnas pivote son la 1, la 2 y la 4: base de $\operatorname{Col} A$, $\{\mathbf u_2, \mathbf u_2 - \mathbf u_3, \mathbf u_1 + 4\mathbf u_2\}$ (o $\{\mathbf u_1, \mathbf u_2, \mathbf u_3\}$).
> La relación $\mathbf a_1 - \mathbf a_2 - \mathbf a_3 = \mathbf 0$ da $\operatorname{Nul} A = \operatorname{Gen}\{\langle 1, -1, -1, 0\rangle\}$.

### 5. V o F: $\operatorname{Col} A \subseteq \operatorname{Nul}(A - I)$
Si $A$ es cuadrada y $\operatorname{Col} A \subseteq \operatorname{Nul}(A - I)$, entonces $A^2 = A$.

> [!example]- Solución
> **Verdadero.** Cada columna $\mathbf a_j$ de $A$ está en $\operatorname{Col} A$, por lo tanto en $\operatorname{Nul}(A - I)$: $(A - I)\mathbf a_j = \mathbf 0$. Esas son las columnas de $(A - I)A$, así que $(A - I)A = 0$, es decir, $A^2 = A$.

### 6. V o F: matrices idempotentes
Si $A^2 = A$, entonces $\operatorname{Col} A \cap \operatorname{Nul} A = \{\mathbf 0\}$.

> [!example]- Solución
> **Verdadero.** Si $\mathbf b$ está en ambos, $\mathbf b = A\mathbf x$ para algún $\mathbf x$ y $A\mathbf b = \mathbf 0$. Entonces $\mathbf 0 = A\mathbf b = A^2\mathbf x = A\mathbf x = \mathbf b$.

### 7. Núcleo y rango de una evaluación
$T: \mathbb{P}_2 \to \mathbb{R}^3$, $T(p) = \langle p(0), p(1), p(0)\rangle$. Encuentre bases del núcleo y del rango.

> [!example]- Solución
> Con $p = ax^2 + bx + c$: $T(p) = \langle c,\ a + b + c,\ c\rangle$.
> **Núcleo:** $c = 0$ y $a + b = 0$: $p = a(x^2 - x)$. Base: $\{x^2 - x\}$.
> **Rango:** $\langle c, a + b + c, c\rangle = c\langle 1, 0, 1\rangle + (a + b + c)\langle 0, 1, 0\rangle$, y ambos coeficientes toman cualquier valor. Base: $\{\langle 1, 0, 1\rangle, \langle 0, 1, 0\rangle\}$.

### 8. Núcleo de $A \mapsto BA$
$T: M_{2 \times 2} \to M_{2 \times 2}$, $T(A) = BA$ con $B = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}$. Pruebe que es lineal y encuentre su núcleo.

> [!example]- Solución
> Lineal: $B(A_1 + A_2) = BA_1 + BA_2$ y $B(cA) = cBA$.
> Núcleo: $\det B = 1 \neq 0$, así que $B$ es invertible y $BA = 0$ implica $A = B^{-1}0 = 0$. El núcleo es $\{0\}$ ($T$ es inyectiva).

## Preguntas de repaso

> [!question]- En el ejercicio 1(b), ¿qué atajo evitó resolver un sistema?
> Que $A$ tiene un pivote en cada fila: entonces $\operatorname{Col} A$ es todo $\mathbb{R}^3$ y cualquier vector de $\mathbb{R}^3$ pertenece.

> [!question]- ¿Qué técnica usan los ejercicios 5 y 6?
> Pasar de afirmaciones sobre subespacios a afirmaciones sobre vectores concretos: "las columnas están en..." o "existe $\mathbf x$ con $\mathbf b = A\mathbf x$", y luego usar la hipótesis algebraica ($A^2 = A$, etc.).

> [!question]- ¿Cómo se obtiene el rango de una transformación en $\mathbb{P}_2$?
> Se aplica $T$ a un polinomio genérico, se separa el resultado por parámetros y se toman los vectores que acompañan a cada parámetro. Si quedan dependientes, se eliminan los que sobran.
