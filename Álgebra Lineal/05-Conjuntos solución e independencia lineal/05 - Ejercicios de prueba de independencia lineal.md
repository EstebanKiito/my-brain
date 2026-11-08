---
ramo: "Álgebra Lineal"
tema: "Conjuntos solución e independencia lineal"
tags:
  - algebra-lineal/independencia
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Independencia lineal]]"
---

# Ejercicios de prueba de independencia lineal

Preguntas de interrogaciones anteriores sobre generadores e independencia: demostraciones con la definición, contraejemplos y cálculos con parámetros. Las demostraciones siguen casi siempre el mismo molde: plantear una combinación igual a cero, reagrupar y usar la hipótesis.

## Ejercicios

### 1. Cambiar un generador por una combinación
V o F: si $\mathbf u, \mathbf v \in \mathbb{R}^3$, entonces $\operatorname{Gen}\{\mathbf u, \mathbf v\} = \operatorname{Gen}\{\mathbf u, \mathbf v + 5\mathbf u\}$.

> [!example]- Solución
> **Verdadero.** Todo $a\mathbf u + b\mathbf v = (a - 5b)\mathbf u + b(\mathbf v + 5\mathbf u)$ está en el segundo. Recíprocamente, $a\mathbf u + b(\mathbf v + 5\mathbf u) = (a + 5b)\mathbf u + b\mathbf v$ está en el primero. Sumar a un generador un múltiplo de otro no cambia el generado (es lo mismo que hace una operación de fila).

### 2. Demostración clásica de independencia
Demuestre que si $\{\mathbf u, \mathbf v, \mathbf w\}$ es LI, entonces $\{\mathbf u + \mathbf v,\ \mathbf u - 3\mathbf v,\ \mathbf w + 2\mathbf u\}$ también.

> [!example]- Solución
> Sea $\alpha(\mathbf u + \mathbf v) + \beta(\mathbf u - 3\mathbf v) + \gamma(\mathbf w + 2\mathbf u) = \mathbf 0$. Reagrupando:
> $$(\alpha + \beta + 2\gamma)\mathbf u + (\alpha - 3\beta)\mathbf v + \gamma\mathbf w = \mathbf 0.$$
> Como $\{\mathbf u, \mathbf v, \mathbf w\}$ es LI, los tres coeficientes son cero: $\gamma = 0$, $\alpha = 3\beta$ y $4\beta = 0$. Entonces $\alpha = \beta = \gamma = 0$.

### 3. Ortogonales y no nulos implica independientes
V o F: si $\mathbf u, \mathbf v, \mathbf w \in \mathbb{R}^n$ son no nulos y ortogonales dos a dos, entonces $\{\mathbf u, \mathbf v, \mathbf w\}$ es LI.

> [!example]- Solución
> **Verdadero.** Si $\alpha\mathbf u + \beta\mathbf v + \gamma\mathbf w = \mathbf 0$, el producto punto con $\mathbf u$ da $\alpha\|\mathbf u\|^2 + 0 + 0 = 0$, y como $\mathbf u \neq \mathbf 0$, $\alpha = 0$. Lo mismo con $\mathbf v$ y $\mathbf w$ da $\beta = \gamma = 0$. Este argumento reaparece con los conjuntos ortogonales.

### 4. Tres contraejemplos
Muestre que son falsas: (a) las columnas de $A$ son LI si $A\mathbf x = \mathbf 0$ tiene infinitas soluciones; (b) si $S$ es LD, **cada** vector de $S$ es combinación de los otros; (c) si $\{\mathbf u, \mathbf v\}$ es LI, $\{\mathbf u, \mathbf v, \mathbf w\}$ es LI para todo $\mathbf w$.

> [!example]- Solución
> (a) $A = \begin{bmatrix} 1 & 2 \\ 1 & 2 \end{bmatrix}$: $A\mathbf x = \mathbf 0$ tiene infinitas soluciones y las columnas son LD. (En realidad, infinitas soluciones implica LD siempre.)
> (b) $S = \{\langle 1, 1\rangle, \langle 2, 2\rangle, \langle 1, 0\rangle\}$ es LD, pero $\langle 1, 0\rangle$ no está en $\operatorname{Gen}\{\langle 1, 1\rangle, \langle 2, 2\rangle\}$.
> (c) $\mathbf w = \mathbf 0$, o $\mathbf w = \mathbf u$.

### 5. Un vector fuera del plano da un conjunto LI
$\mathbf y = \langle 10, 6, -4\rangle$, $\mathbf v_1 = \langle 1, 2, 1\rangle$, $\mathbf v_2 = \langle 2, 1, -4\rangle$. (a) ¿Está $\mathbf y$ en el plano generado por $\mathbf v_1$ y $\mathbf v_2$? (b) ¿Es $\{\mathbf y, \mathbf v_1, \mathbf v_2\}$ LI?

> [!example]- Solución
> (a) $\left[\begin{array}{cc|c} 1 & 2 & 10 \\ 2 & 1 & 6 \\ 1 & -4 & -4 \end{array}\right] \to [0\ \ {-3} \mid -14]$ y $[0\ \ {-6} \mid -14]$, y luego $F_3 - 2F_2$ da $[0\ 0 \mid 14]$. Inconsistente: **no está**.
> (b) **LI.** $\mathbf v_1$ y $\mathbf v_2$ no son paralelos (LI) y $\mathbf y$ no es combinación de ellos. Por el criterio de "ningún vector es combinación de los anteriores" (ordenando $\mathbf v_1, \mathbf v_2, \mathbf y$), el conjunto es LI.

### 6. Combinación de columnas y columna que sobra
$A = \begin{bmatrix} 1 & 0 & 1 & 0 \\ 0 & 2 & 2 & 0 \\ 1 & 1 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{bmatrix}$. (a) ¿Es $\mathbf b = \langle -2, 4, 1, 6\rangle$ combinación de las columnas? (b) ¿Qué columna se puede eliminar para obtener $B$ con $B\mathbf x = \mathbf 0$ de solución única?

> [!example]- Solución
> (a) En $[A \mid \mathbf b]$: $F_3 - F_1$ da $[0\ 1\ 1\ 0 \mid 3]$ y $F_3 - \tfrac12F_2$ da $[0\ 0\ 0\ 0 \mid 1]$. Inconsistente: **no**.
> (b) La columna 3 es $\mathbf a_1 + \mathbf a_2$ y es la única sin pivote. Quitándola, las tres columnas restantes son pivote, son LI, y $B\mathbf x = \mathbf 0$ solo tiene la solución trivial.

### 7. Dos generadores del mismo plano
Encuentre los $h$ tales que $\operatorname{Gen}\{\langle 2, 1, 0\rangle, \langle -6, 0, 1\rangle\} = \operatorname{Gen}\{\langle h, 2, 1\rangle, \langle 0, -6, h\rangle\}$.

> [!example]- Solución
> El primero es un plano por el origen con normal $\langle 2, 1, 0\rangle \times \langle -6, 0, 1\rangle = \langle 1, -2, 6\rangle$, es decir, $x - 2y + 6z = 0$. Los dos vectores nuevos deben estar en él: $h - 4 + 6 = 0$ y $12 + 6h = 0$, ambas dan $h = -2$. Además, con $h = -2$, $\langle -2, 2, 1\rangle$ y $\langle 0, -6, -2\rangle$ no son paralelos, así que generan todo el plano y no solo una recta. **$h = -2$.**

### 8. Una inversa por la derecha implica generar
$A$ es de $3 \times 5$ y $D$ de $5 \times 3$ con $AD = I_3$. Demuestre que las columnas de $A$ generan $\mathbb{R}^3$.

> [!example]- Solución
> Dado $\mathbf b \in \mathbb{R}^3$, sea $\mathbf x = D\mathbf b \in \mathbb{R}^5$. Entonces $A\mathbf x = (AD)\mathbf b = I_3\mathbf b = \mathbf b$. Así, $A\mathbf x = \mathbf b$ es consistente para todo $\mathbf b$, que equivale a que las columnas generen $\mathbb{R}^3$.

## Preguntas de repaso

> [!question]- ¿Cuál es el molde de las demostraciones de independencia como la del ejercicio 2?
> Plantear $\sum c_i(\text{vectores nuevos}) = \mathbf 0$, reagrupar en función de los vectores originales, usar que estos son LI para igualar cada coeficiente a cero y resolver el sistema pequeño en los $c_i$.

> [!question]- En el ejercicio 7, ¿por qué no basta con que los dos vectores nuevos estén en el plano?
> Porque si fueran paralelos, generarían solo una recta dentro del plano. Hay que verificar además que no sean múltiplos.

> [!question]- ¿Qué relación hay entre el ejercicio 8 y el teorema del pivote en cada fila?
> El ejercicio prueba que $A\mathbf x = \mathbf b$ siempre tiene solución, así que por ese teorema $A$ tiene un pivote en cada una de sus 3 filas.
