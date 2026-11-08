---
ramo: "Álgebra Lineal"
tema: "Ortogonalidad y complemento ortogonal"
tags:
  - algebra-lineal/ortogonalidad
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Conjuntos ortogonales y matrices ortogonales]]"
---

# Ejercicios de prueba de ortogonalidad

Preguntas de exámenes e interrogaciones anteriores sobre complementos ortogonales, conjuntos ortogonales y matrices con columnas ortonormales. Para el complemento, la receta es siempre "generadores como filas y espacio nulo".

## Ejercicios

### 1. Complemento del espacio columna
Encuentre una base de $(\operatorname{Col} A)^\perp$ para $A = \begin{bmatrix} 1 & -1 & 0 & 1 \\ 2 & 2 & 2 & 0 \\ -1 & 1 & -1 & 1 \\ 2 & 2 & 1 & 2 \end{bmatrix}$.

> [!example]- Solución
> $(\operatorname{Col} A)^\perp = \operatorname{Nul} A^T$. Escalonando,
> $$A^T = \begin{bmatrix} 1 & 2 & -1 & 2 \\ -1 & 2 & 1 & 2 \\ 0 & 2 & -1 & 1 \\ 1 & 0 & 1 & 2 \end{bmatrix} \sim \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix},$$
> así que $x_1 = x_2 = x_3 = -x_4$ y una base es $\{\langle -1, -1, -1, 1\rangle\}$. Control: este vector es ortogonal a las cuatro columnas de $A$.

### 2. Complemento de un generado en $\mathbb{R}^4$
Encuentre una base de $W^\perp$ con $W = \operatorname{Gen}\{\langle 1, 1, 1, 1\rangle, \langle -1, -1, 1, -2\rangle, \langle 2, 2, -2, 2\rangle\}$.

> [!example]- Solución
> Generadores como filas: $\begin{bmatrix} 1 & 1 & 1 & 1 \\ -1 & -1 & 1 & -2 \\ 2 & 2 & -2 & 2 \end{bmatrix}$. $F_2 + F_1$ da $[0\ 0\ 2\ -1]$ y $F_3 - 2F_1$ da $[0\ 0\ -4\ 0]$; de ahí $x_3 = 0$, $x_4 = 0$ y $x_1 = -x_2$. Base: $\{\langle -1, 1, 0, 0\rangle\}$. Así, $\dim W = 3$ y $\dim W^\perp = 1$, que suman 4.

### 3. Completar a una base ortogonal de $\mathbb{R}^4$
$\mathbf v_1 = \langle 1, 2, 1, 1\rangle$ y $\mathbf v_2 = \langle 1, -1, 1, 0\rangle$. (a) Encuentre una base de $\operatorname{Gen}\{\mathbf v_1, \mathbf v_2\}^\perp$. (b) Encuentre una base ortogonal $\{\mathbf v_1, \mathbf v_2, \mathbf v_3, \mathbf v_4\}$ de $\mathbb{R}^4$.

> [!example]- Solución
> (a) $\operatorname{Nul}\begin{bmatrix} 1 & 2 & 1 & 1 \\ 1 & -1 & 1 & 0 \end{bmatrix}$: restando, $3x_2 + x_4 = 0$; con $x_3, x_4$ libres, una base es $\{\langle -1, 0, 1, 0\rangle, \langle -1, -1, 0, 3\rangle\}$.
> (b) $\mathbf v_1 \cdot \mathbf v_2 = 0$ y todo vector del complemento es ortogonal a ambos. Falta que $\mathbf v_3$ y $\mathbf v_4$ sean ortogonales entre sí: con $\mathbf v_3 = \langle -1, 0, 1, 0\rangle$, se corrige el segundo restándole su componente en $\mathbf v_3$:
> $$\mathbf v_4 = \langle -1, -1, 0, 3\rangle - \tfrac{1}{2}\langle -1, 0, 1, 0\rangle = \langle -\tfrac12, -1, -\tfrac12, 3\rangle .$$

### 4. Columnas ortogonales y normas
$A = \begin{bmatrix} 3 & -1 & 3 \\ -2 & 3 & 8 \\ 1 & -3 & 7 \\ 3 & 4 & 0 \end{bmatrix}$. (a) Verifique que sus columnas son ortogonales. (b) Encuentre $U$ con columnas ortonormales y $\operatorname{Col} U = \operatorname{Col} A$. (c) Calcule $\|U\mathbf x\|$ con $\mathbf x = \langle 4, 0, 3\rangle$.

> [!example]- Solución
> (a) $\mathbf a_1 \cdot \mathbf a_2 = -3 - 6 - 3 + 12 = 0$, $\mathbf a_1 \cdot \mathbf a_3 = 9 - 16 + 7 + 0 = 0$, $\mathbf a_2 \cdot \mathbf a_3 = -3 + 24 - 21 + 0 = 0$.
> (b) Se normaliza cada columna: $\|\mathbf a_1\| = \sqrt{23}$, $\|\mathbf a_2\| = \sqrt{35}$, $\|\mathbf a_3\| = \sqrt{122}$, y $U = \left[\frac{\mathbf a_1}{\sqrt{23}}\ \ \frac{\mathbf a_2}{\sqrt{35}}\ \ \frac{\mathbf a_3}{\sqrt{122}}\right]$.
> (c) $U$ conserva normas: $\|U\mathbf x\| = \|\mathbf x\| = \sqrt{16 + 9} = 5$.

### 5. Una base ortogonal de un hiperplano
$W = \{\langle x, y, z, t\rangle : x - y - z = 0\}$. Demuestre que $\{\langle 1, 1, 0, 0\rangle, \langle 0, 0, 0, 1\rangle, \langle 1, -1, 2, 0\rangle\}$ es una base de $W$.

> [!example]- Solución
> Los tres vectores cumplen $x - y - z = 0$ ($1 - 1 - 0$, $0$, $1 + 1 - 2$), así que están en $W$. Son ortogonales dos a dos ($0$, $1 - 1 + 0 = 0$, $0$) y no nulos, así que son LI. $W$ es el espacio nulo de $[1\ -1\ -1\ 0]$, de dimensión $4 - 1 = 3$. Tres vectores LI en un espacio de dimensión 3 forman una base.

### 6. Vectores ortogonales con coordenadas no negativas
$P$ es el conjunto de vectores de $\mathbb{R}^3$ con coordenadas no negativas. (a) Si $\mathbf u, \mathbf v \in P$ son no nulos y ortogonales, al menos uno está en un plano coordenado. (b) Si $\mathbf u, \mathbf v, \mathbf w \in P$ son no nulos y mutuamente ortogonales, cada uno está sobre un eje coordenado.

> [!example]- Solución
> (a) $\mathbf u \cdot \mathbf v = u_1v_1 + u_2v_2 + u_3v_3 = 0$ es una suma de términos no negativos, así que cada $u_iv_i = 0$. Si $\mathbf u$ no tuviera coordenadas nulas, todas las de $\mathbf v$ serían cero, contradicción. Entonces alguna coordenada de $\mathbf u$ o de $\mathbf v$ es cero: está en un plano coordenado.
> (b) Si $\mathbf u$ tuviera dos coordenadas positivas, por ejemplo $u_1, u_2 > 0$, el argumento de (a) da $v_1 = v_2 = w_1 = w_2 = 0$. Entonces $\mathbf v \cdot \mathbf w = v_3w_3 = 0$ con $v_3, w_3 > 0$ (son no nulos), contradicción. Así, cada vector tiene exactamente una coordenada positiva: está sobre un eje.

## Preguntas de repaso

> [!question]- En el ejercicio 1, ¿por qué se transpone $A$ antes de calcular el espacio nulo?
> Porque se busca lo ortogonal a las **columnas** de $A$, y la receta pone los generadores como filas: las columnas de $A$ son las filas de $A^T$.

> [!question]- En el ejercicio 3, ¿por qué no basta tomar la base del complemento tal como sale?
> Porque esos dos vectores son ortogonales a $\mathbf v_1$ y $\mathbf v_2$, pero no necesariamente entre sí. Hay que ortogonalizarlos (es el primer paso de Gram-Schmidt).

> [!question]- ¿Qué ventaja tuvo saber que las columnas eran ortogonales en el ejercicio 5?
> Que la independencia sale gratis (conjunto ortogonal de no nulos), y entonces solo hay que comparar con la dimensión.
