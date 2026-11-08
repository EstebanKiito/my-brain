---
ramo: "Álgebra Lineal"
tema: "Coordenadas, dimensión y rango"
tags:
  - algebra-lineal/espacios
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Espacio fila y teorema del rango]]"
---

# Ejercicios de prueba de coordenadas, dimensión y rango

Preguntas de interrogaciones y exámenes anteriores. Muchas son V o F que se deciden con el teorema del rango y las desigualdades de dimensión; otras piden las tres bases ($\operatorname{Nul}$, $\operatorname{Col}$, $\operatorname{Fil}$) de una matriz ya escalonada.

## Ejercicios

### 1. Coordenadas de un polinomio
$\mathcal B = \{1 + t, 1 + t^2, t + t^2\}$ es base de $\mathbb{P}_2$. Encuentre $[6 + 3t - t^2]_{\mathcal B}$.

> [!example]- Solución
> $a(1 + t) + b(1 + t^2) + c(t + t^2) = 6 + 3t - t^2$ da $a + b = 6$, $a + c = 3$ y $b + c = -1$. Sumando las tres, $a + b + c = 4$; entonces $c = -2$, $b = 1$ y $a = 5$. $[p]_{\mathcal B} = \langle 5, 1, -2\rangle$. Comprobación: $5 + 5t + 1 + t^2 - 2t - 2t^2 = 6 + 3t - t^2$.

### 2. Cuatro V o F sobre dimensión
(a) $\dim\mathbb{P}_4 = 4$. (b) Si $V = \operatorname{Gen}\{\mathbf v_1, \mathbf v_2, \mathbf v_3\}$, $\dim V = 3$. (c) Si $\{\mathbf v_1, \dots, \mathbf v_p\}$ es LI en $V$, $\dim V \leq p$. (d) Si $\{\mathbf v_1, \dots, \mathbf v_p\}$ es LD en $V$, $\dim V \leq p$.

> [!example]- Solución
> (a) **Falso**: la base $\{1, t, t^2, t^3, t^4\}$ tiene 5 elementos.
> (b) **Falso**: si $\mathbf v_1 = \mathbf v_2 = \mathbf v_3 \neq \mathbf 0$, $\dim V = 1$. Solo vale $\dim V \leq 3$.
> (c) **Falso**: es $p \leq \dim V$. $\{\mathbf e_1, \mathbf e_2\}$ es LI en $\mathbb{R}^3$.
> (d) **Falso**: $\{\langle 1, 0, 0\rangle, \langle 2, 0, 0\rangle\}$ es LD en $\mathbb{R}^3$, con $p = 2 < 3$. Un conjunto LD no da información sobre la dimensión.

### 3. Teorema del rango para $A$ y $A^T$
$A$ es de $7 \times 5$ con rango 2. Dé $\dim\operatorname{Nul} A$, $\dim\operatorname{Fil} A$, $\operatorname{rango} A^T$ y $\dim\operatorname{Nul} A^T$.

> [!example]- Solución
> $\dim\operatorname{Nul} A = 5 - 2 = 3$; $\dim\operatorname{Fil} A = 2$; $\operatorname{rango} A^T = 2$; $A^T$ es de $5 \times 7$, así que $\dim\operatorname{Nul} A^T = 7 - 2 = 5$.

### 4. Las tres bases
$A = \begin{bmatrix} 2 & 4 & -9 & 11 & -8 \\ 1 & 5 & 3 & 1 & 5 \\ -3 & -5 & 16 & -18 & 15 \\ 4 & 10 & -13 & 19 & -10 \end{bmatrix} \sim \begin{bmatrix} 1 & 3 & -2 & 4 & -1 \\ 0 & 2 & 5 & -3 & 6 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$. Dé el rango, $\dim\operatorname{Nul} A$ y bases de $\operatorname{Col} A$ y $\operatorname{Fil} A$.

> [!example]- Solución
> Dos pivotes (columnas 1 y 2): $\operatorname{rango} A = 2$ y $\dim\operatorname{Nul} A = 5 - 2 = 3$.
> $\operatorname{Col} A$: columnas 1 y 2 **de $A$**, $\{\langle 2, 1, -3, 4\rangle, \langle 4, 5, -5, 10\rangle\}$.
> $\operatorname{Fil} A$: filas no nulas **de la escalonada**, $\{\langle 1, 3, -2, 4, -1\rangle, \langle 0, 2, 5, -3, 6\rangle\}$.

### 5. $A = MR$ con $M$ invertible
$A = MR$ con $M$ invertible y $R = \begin{bmatrix} 1 & 0 & 3 & 2 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$. Encuentre bases de $\operatorname{Col} A^T$ y $\operatorname{Nul} A$.

> [!example]- Solución
> $M$ es invertible, así que es producto de elementales: $A$ se obtiene de $R$ con operaciones de fila y $A \sim R$. Entonces $\operatorname{Col} A^T = \operatorname{Fil} A = \operatorname{Fil} R$, con base $\{\langle 1, 0, 3, 2\rangle, \langle 0, 1, 1, 0\rangle\}$. También $\operatorname{Nul} A = \operatorname{Nul} R$ ($A\mathbf x = \mathbf 0 \iff R\mathbf x = \mathbf 0$): $x_1 = -3x_3 - 2x_4$, $x_2 = -x_3$, con base $\{\langle -3, -1, 1, 0\rangle, \langle -2, 0, 0, 1\rangle\}$.

### 6. Base de Nul y Col sin conocer la matriz
$\dim\operatorname{Fil} A = 3$ y $A$ anula a $\langle 4, 0, 1, 2, 1\rangle$ y a $\langle -1, 2, -2, 0, 1\rangle$, con imágenes en $\mathbb{R}^3$. (a) Dé una base de $\operatorname{Nul} A$. (b) Pruebe que $\operatorname{Col} A = \mathbb{R}^3$.

> [!example]- Solución
> $A$ multiplica vectores de $\mathbb{R}^5$ y entrega vectores de $\mathbb{R}^3$: es de $3 \times 5$.
> (a) $\operatorname{rango} A = \dim\operatorname{Fil} A = 3$, así que $\dim\operatorname{Nul} A = 5 - 3 = 2$. Los dos vectores dados están en $\operatorname{Nul} A$ y no son paralelos (LI). Por el teorema de la base, forman una base de $\operatorname{Nul} A$.
> (b) $\operatorname{Col} A \subseteq \mathbb{R}^3$ y $\dim\operatorname{Col} A = 3$. Un subespacio de $\mathbb{R}^3$ de dimensión 3 es todo $\mathbb{R}^3$.

### 7. Consistencia y dimensiones
$A = \begin{bmatrix} 1 & -4 & 7 \\ 0 & 3 & -5 \\ -2 & 5 & -9 \end{bmatrix}$ y $\mathbf z = \langle a, b, c\rangle$. (a) ¿Cuándo es consistente $A\mathbf x = \mathbf z$ y cuántas soluciones tiene? (b) Dé $\dim\operatorname{Col} A$, $\dim\operatorname{Fil} A$ y $\dim\operatorname{Nul} A$.

> [!example]- Solución
> (a) $F_3 + 2F_1$ da $[0\ -3\ 5 \mid c + 2a]$ y luego $F_3 + F_2$ da $[0\ 0\ 0 \mid 2a + b + c]$. Consistente si y solo si $2a + b + c = 0$, y entonces hay **infinitas** soluciones (una variable libre).
> (b) Dos pivotes: $\dim\operatorname{Col} A = \dim\operatorname{Fil} A = 2$ y $\dim\operatorname{Nul} A = 3 - 2 = 1$.

### 8. V o F: inyectividad desde el espacio columna
$L$ es de $4 \times 2$ con $\operatorname{Col} L = \operatorname{Gen}\{\mathbf e_1, \mathbf e_4\}$. Si $L\mathbf u = L\mathbf v$, entonces $\mathbf u = \mathbf v$.

> [!example]- Solución
> **Verdadero.** $\operatorname{rango} L = \dim\operatorname{Col} L = 2$, y $L$ tiene 2 columnas, así que $\dim\operatorname{Nul} L = 0$. Entonces $L(\mathbf u - \mathbf v) = \mathbf 0$ implica $\mathbf u - \mathbf v = \mathbf 0$.

## Preguntas de repaso

> [!question]- ¿Qué herramienta resuelve casi todos los V o F de este tema?
> El teorema del rango ($\operatorname{rango} A + \dim\operatorname{Nul} A = n$) junto con $\operatorname{rango} A = \operatorname{rango} A^T \leq \min(m, n)$ y las desigualdades entre conjuntos LI, generadores y dimensión.

> [!question]- En el ejercicio 6, ¿por qué no hizo falta probar que los dos vectores generan $\operatorname{Nul} A$?
> Porque ya se sabía que $\dim\operatorname{Nul} A = 2$, y por el teorema de la base dos vectores LI en un espacio de dimensión 2 son automáticamente base.

> [!question]- ¿Por qué en el ejercicio 5 se puede leer todo desde $R$ aunque no se conozca $M$?
> Porque multiplicar por una invertible a la izquierda es hacer operaciones de fila, que no cambian $\operatorname{Fil}$ ni $\operatorname{Nul}$. (Sí cambian $\operatorname{Col}$, por eso no se pidió.)
