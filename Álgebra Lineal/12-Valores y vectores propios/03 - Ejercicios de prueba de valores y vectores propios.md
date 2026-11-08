---
ramo: "Álgebra Lineal"
tema: "Valores y vectores propios"
tags:
  - algebra-lineal/valores-propios
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Ecuación característica y similitud]]"
---

# Ejercicios de prueba de valores y vectores propios

Preguntas de interrogaciones y exámenes anteriores sobre la definición, el polinomio característico y las multiplicidades. Las demostraciones casi siempre parten de $A\mathbf v = \lambda\mathbf v$ con $\mathbf v \neq \mathbf 0$ y aplican $A$ (o $A^{-1}$) a ambos lados.

## Ejercicios

### 1. Valores propios de una matriz nilpotente
$A^3 = 0$. (a) Pruebe que si $\lambda$ es valor propio de $A$, $\lambda^3$ es valor propio de $A^3$. (b) Concluya que $0$ es el único valor propio de $A$.

> [!example]- Solución
> (a) Si $A\mathbf v = \lambda\mathbf v$ con $\mathbf v \neq \mathbf 0$: $A^2\mathbf v = A(\lambda\mathbf v) = \lambda^2\mathbf v$ y $A^3\mathbf v = \lambda^3\mathbf v$.
> (b) Como $A^3 = 0$: $\mathbf 0 = A^3\mathbf v = \lambda^3\mathbf v$ con $\mathbf v \neq \mathbf 0$, así que $\lambda^3 = 0$ y $\lambda = 0$. Además 0 sí es valor propio: $\det(A)^3 = \det(A^3) = 0$.

### 2. Un valor propio desde una ecuación matricial
$A$ es invertible y $A^4 - 7A^3 = 0$. Explique por qué 7 es valor propio de $A$.

> [!example]- Solución
> $A^3(A - 7I) = 0$. Tomando determinantes, $(\det A)^3\det(A - 7I) = 0$, y como $\det A \neq 0$, $\det(A - 7I) = 0$. Entonces 7 es raíz del polinomio característico.

### 3. Misma ecuación característica
Demuestre que $A$ y $A^T$ tienen la misma ecuación característica.

> [!example]- Solución
> $\det(A^T - \lambda I) = \det(A^T - \lambda I^T) = \det\big((A - \lambda I)^T\big) = \det(A - \lambda I)$.

### 4. Encontrar la matriz a partir de sus vectores propios
Encuentre $\alpha, \beta$ para que $A = \begin{bmatrix} 2 & 6 \\ \alpha & \beta \end{bmatrix}$ tenga como vectores propios a $\langle 3, 1\rangle$ y $\langle 2, 1\rangle$.

> [!example]- Solución
> $A\langle 3, 1\rangle = \langle 12, 3\alpha + \beta\rangle$. La primera componente fija $\lambda = 4$ (porque $12 = 4 \cdot 3$), así que $3\alpha + \beta = 4$. $A\langle 2, 1\rangle = \langle 10, 2\alpha + \beta\rangle$ fija $\lambda = 5$, así que $2\alpha + \beta = 5$. Restando, $\alpha = -1$ y $\beta = 7$.

### 5. Dimensión de un espacio propio con parámetro
Encuentre $h$ para que el espacio propio de $\lambda = 4$ de $A = \begin{bmatrix} 4 & 2 & 3 & 3 \\ 0 & 2 & h & 3 \\ 0 & 0 & 4 & 14 \\ 0 & 0 & 0 & 2 \end{bmatrix}$ tenga dimensión 2.

> [!example]- Solución
> $A - 4I = \begin{bmatrix} 0 & 2 & 3 & 3 \\ 0 & -2 & h & 3 \\ 0 & 0 & 0 & 14 \\ 0 & 0 & 0 & -2 \end{bmatrix}$. Con $F_2 + F_1$ la segunda fila queda $[0\ 0\ \ h + 3\ \ 6]$. Hay pivote en la columna 2 (fila 1) y en la columna 4 (filas 3 y 4). Si $h + 3 \neq 0$, la segunda fila da otro pivote en la columna 3 y el rango es 3; si $h = -3$, esa fila es $[0\ 0\ 0\ 6]$, proporcional a las de abajo, y el rango es 2.
> Como $\dim E_4 = 4 - \operatorname{rango}(A - 4I)$, vale 2 si y solo si $h = -3$.

### 6. Multiplicidades y vectores propios independientes
$A$ es de $6 \times 6$ con polinomio característico $(1 + \lambda)(1 - \lambda)^2(2 - \lambda)^3$. (a) ¿Por qué no hay tres vectores LI con $A\mathbf v = \mathbf v$? (b) Si $A$ fuera diagonalizable, ¿qué dimensión tendría cada espacio propio?

> [!example]- Solución
> (a) Tres vectores LI con $A\mathbf v = \mathbf v$ estarían en $E_1$, que tendría dimensión al menos 3. Pero la dimensión de un espacio propio es a lo más la multiplicidad algebraica, que para $\lambda = 1$ es 2.
> (b) Diagonalizable significa que cada espacio propio alcanza su multiplicidad: $\dim E_{-1} = 1$, $\dim E_1 = 2$ y $\dim E_2 = 3$ (suman 6).

### 7. Núcleo de una transformación definida en una base
$V$ tiene dimensión 3 y es generado por $\{\mathbf v_1, \mathbf v_2, \mathbf v_3\}$. $T: V \to V$ cumple $T(\mathbf v_1) = \mathbf v_1$, $T(\mathbf v_2) = \mathbf 0$ y $T(\mathbf v_3) = -\mathbf v_3$. Encuentre $\dim\operatorname{Nul} T$.

> [!example]- Solución
> Tres vectores que generan un espacio de dimensión 3 son una base. $T(c_1\mathbf v_1 + c_2\mathbf v_2 + c_3\mathbf v_3) = c_1\mathbf v_1 - c_3\mathbf v_3 = \mathbf 0$ si y solo si $c_1 = c_3 = 0$. Entonces $\operatorname{Nul} T = \operatorname{Gen}\{\mathbf v_2\}$ y su dimensión es 1. (En lenguaje de este tema: los $\mathbf v_i$ son vectores propios con valores 1, 0 y $-1$, y el núcleo es $E_0$.)

### 8. V o F: vectores propios independientes e invertibilidad
Toda matriz de $n \times n$ con $n$ vectores propios LI es invertible.

> [!example]- Solución
> **Falso.** $A = \begin{bmatrix} 0 & 1 \\ 0 & 1 \end{bmatrix}$ tiene los vectores propios LI $\langle 1, 0\rangle$ ($\lambda = 0$) y $\langle 1, 1\rangle$ ($\lambda = 1$), pero $\det A = 0$. Tener una base de vectores propios no impide que uno de los valores propios sea 0.

## Preguntas de repaso

> [!question]- ¿Qué técnica comparten los ejercicios 1 y 2?
> Convertir una identidad matricial en información sobre valores propios: aplicándola a un vector propio (ejercicio 1) o tomando determinantes (ejercicio 2).

> [!question]- En el ejercicio 5, ¿por qué conviene escalonar $A - 4I$ en vez de calcular el polinomio característico?
> Porque ya se sabe que 4 es valor propio (la matriz es triangular). Lo que se pide es la dimensión de $E_4 = \operatorname{Nul}(A - 4I)$, que depende del rango de $A - 4I$.

> [!question]- ¿Qué desigualdad usa el ejercicio 6?
> $1 \leq \dim E_\lambda \leq$ multiplicidad algebraica de $\lambda$, que se ve en detalle en la diagonalización.
