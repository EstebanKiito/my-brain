---
ramo: "Álgebra Lineal"
tema: "Determinantes"
tags:
  - algebra-lineal/determinantes
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Regla de Cramer y fórmula de la inversa]]"
  - "[[04 - Determinante como área y volumen]]"
---

# Ejercicios de prueba de propiedades, Cramer y volúmenes

Preguntas de interrogaciones anteriores que se resuelven con las reglas del determinante (productos, inversas, múltiplos, adjunta), con la regla de Cramer y con la interpretación de área y volumen. En las de propiedades no hay que calcular ninguna matriz: basta llevar la cuenta de los factores.

## Ejercicios

### 1. Determinante de una expresión con operaciones de fila
$A$ es de $3 \times 3$ con $\det A = -3$. $B$ se obtiene sumando a la fila 3 de $A$ dos veces la fila 1, y $C$ intercambiando las filas 2 y 3 de $A$. Calcule $\det(2A^{-1}CB^T)$.

> [!example]- Solución
> $\det B = \det A = -3$ (reemplazo) y $\det C = -\det A = 3$ (intercambio). Entonces
> $$\det(2A^{-1}CB^T) = 2^3 \cdot \frac{1}{\det A} \cdot \det C \cdot \det B = 8 \cdot \left(-\tfrac13\right) \cdot 3 \cdot (-3) = 24 .$$

### 2. Despejar un determinante
$A$ y $B$ son de $5 \times 5$, $\det A = -2$ y $\det\big(2(A^{-1})^3B^T\big) = 60$. Calcule $\det(B^{-1})$.

> [!example]- Solución
> $2^5 \cdot (\det A)^{-3} \cdot \det B = 32 \cdot \left(-\tfrac18\right)\det B = -4\det B = 60$, así que $\det B = -15$ y $\det(B^{-1}) = -\tfrac{1}{15}$.

### 3. Determinante desde una ecuación y la adjunta
$A$ es de $4 \times 4$ y cumple $A^TA = -8A^{-1}$. Calcule $\det(\operatorname{adj} A)$.

> [!example]- Solución
> Tomando determinantes: $(\det A)^2 = (-8)^4 (\det A)^{-1}$, así que $(\det A)^3 = 8^4 = 4096 = 16^3$ y $\det A = 16$. Con $\det(\operatorname{adj} A) = (\det A)^{n-1}$: $16^3 = 4096$.

### 4. Una columna de la inversa con Cramer
Use Cramer para obtener la segunda columna de la inversa de $A = \begin{bmatrix} 2 & 4 & 6 \\ 4 & 5 & 6 \\ 3 & 1 & -2 \end{bmatrix}$.

> [!example]- Solución
> Es la solución de $A\mathbf x = \mathbf e_2$. $\det A = 6$. Reemplazando cada columna por $\mathbf e_2$ y desarrollando por esa columna (solo tiene un 1 en la fila 2):
> - $\det A_1(\mathbf e_2) = -\begin{vmatrix} 4 & 6 \\ 1 & -2 \end{vmatrix} = 14$;
> - $\det A_2(\mathbf e_2) = +\begin{vmatrix} 2 & 6 \\ 3 & -2 \end{vmatrix} = -22$;
> - $\det A_3(\mathbf e_2) = -\begin{vmatrix} 2 & 4 \\ 3 & 1 \end{vmatrix} = 10$.
>
> Columna: $\tfrac16\langle 14, -22, 10\rangle = \langle \tfrac73, -\tfrac{11}{3}, \tfrac53\rangle$.

### 5. Cramer con parámetro
$A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ a & 0 & 1 \end{bmatrix}$. (a) ¿Cuándo es invertible? (b) Encuentre con Cramer la segunda columna de $A^{-1}$.

> [!example]- Solución
> (a) Por la primera fila: $\det A = 1(1 - 0) - 1(0 - a) = 1 + a$. Invertible si y solo si $a \neq -1$.
> (b) $\det A_1(\mathbf e_2) = \begin{vmatrix} 0 & 1 & 0 \\ 1 & 1 & 1 \\ 0 & 0 & 1 \end{vmatrix} = -1$, $\det A_2(\mathbf e_2) = \begin{vmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \\ a & 0 & 1 \end{vmatrix} = 1$ y $\det A_3(\mathbf e_2) = \begin{vmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ a & 0 & 0 \end{vmatrix} = a$. Columna: $\dfrac{1}{a + 1}\langle -1, 1, a\rangle$.

### 6. Área de la imagen de un paralelogramo
$S$ es el paralelogramo de $\mathbf b_1 = \langle -2, 3\rangle$ y $\mathbf b_2 = \langle -2, 5\rangle$, y $A = \begin{bmatrix} 6 & -2 \\ -3 & 2 \end{bmatrix}$. Calcule el área de $T(S)$ con $T(\mathbf x) = A\mathbf x$.

> [!example]- Solución
> Área de $S$: $|\det[\mathbf b_1\ \mathbf b_2]| = |-10 + 6| = 4$. $|\det A| = |12 - 6| = 6$. Área de $T(S) = 6 \cdot 4 = 24$.

### 7. Volumen con parámetro
$S$ es el paralelepípedo con un vértice en el origen y vértices adyacentes $(1, 0, 2)$, $(-1, 2, 4)$ y $(-1, 1, 0)$. $T\langle x_1, x_2, x_3\rangle = \langle \alpha x_1 + x_2,\ x_1 + x_2,\ x_1 + x_2 + x_3\rangle$. ¿Para qué $\alpha$ el volumen de $T(S)$ es 4?

> [!example]- Solución
> $\text{Vol}(S) = \left|\det\begin{bmatrix} 1 & -1 & -1 \\ 0 & 2 & 1 \\ 2 & 4 & 0 \end{bmatrix}\right| = |-2| = 2$. $[T] = \begin{bmatrix} \alpha & 1 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$, y desarrollando por la tercera columna, $\det[T] = \alpha - 1$. Entonces $2|\alpha - 1| = 4$, o sea $\alpha = 3$ o $\alpha = -1$.

### 8. Volumen de un tetraedro
$S$ es el tetraedro de vértices $\mathbf 0, \mathbf e_1, \mathbf e_2, \mathbf e_3$ (volumen $\tfrac16$) y $S'$ el de vértices $\mathbf 0$, $\mathbf v_1 = \langle 1, -2, 1\rangle$, $\mathbf v_2 = \langle -1, 2, 1\rangle$, $\mathbf v_3 = \langle -1, 0, 1\rangle$. Calcule el volumen de $S'$.

> [!example]- Solución
> La transformación con matriz $A = [\mathbf v_1\ \mathbf v_2\ \mathbf v_3]$ manda $\mathbf e_i \mapsto \mathbf v_i$, así que $S' = T(S)$. $\det A = 4$, por lo que $\text{Vol}(S') = 4 \cdot \tfrac16 = \tfrac23$. El teorema vale para cualquier región, no solo paralelepípedos.

## Preguntas de repaso

> [!question]- ¿Qué tienen en común los ejercicios 1, 2 y 3?
> Todos se resuelven tomando determinantes de ambos lados y usando $\det(AB) = \det A\det B$, $\det(A^{-1}) = 1/\det A$, $\det(cA) = c^n\det A$ y $\det A^T = \det A$, sin conocer las matrices.

> [!question]- En la regla de Cramer para una columna de la inversa, ¿por qué los determinantes son fáciles?
> Porque la columna reemplazada es $\mathbf e_j$, con un solo 1. Desarrollando por esa columna, cada determinante se reduce a un cofactor de $2 \times 2$ (en matrices de $3 \times 3$).

> [!question]- ¿Cómo se ve que $S' = T(S)$ en el ejercicio 8?
> Una transformación lineal manda $\mathbf 0$ a $\mathbf 0$ y cada $\mathbf e_i$ a la columna $i$ de su matriz. Como lleva vértices a vértices y segmentos a segmentos, manda el tetraedro $S$ al tetraedro $S'$.
