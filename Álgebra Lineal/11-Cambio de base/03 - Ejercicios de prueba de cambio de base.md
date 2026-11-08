---
ramo: "Álgebra Lineal"
tema: "Cambio de base"
tags:
  - algebra-lineal/espacios
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Cambio de base en Rⁿ y en polinomios]]"
---

# Ejercicios de prueba de cambio de base

Preguntas de interrogaciones anteriores. Casi todas giran en torno a una sola idea: **las columnas de $P_{\mathcal C \leftarrow \mathcal B}$ son los vectores de $\mathcal B$ escritos en $\mathcal C$**. Cuando se pide la base desconocida, a veces hay que invertir primero la matriz.

## Ejercicios

### 1. Reconstruir la base de partida
$\mathbf v_1 = \langle -7, 2, 6\rangle$, $\mathbf v_2 = \langle -8, 5, 2\rangle$, $\mathbf v_3 = \langle -2, 2, 3\rangle$ y $P = \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \\ -3 & 1 & 1 \end{bmatrix}$. Encuentre $\mathcal B = \{\mathbf u_1, \mathbf u_2, \mathbf u_3\}$ tal que $P = P_{\mathcal C \leftarrow \mathcal B}$ con $\mathcal C = \{\mathbf v_1, \mathbf v_2, \mathbf v_3\}$.

> [!example]- Solución
> La columna $j$ de $P$ es $[\mathbf u_j]_{\mathcal C}$:
> - $\mathbf u_1 = \mathbf v_1 - 3\mathbf v_3 = \langle -1, -4, -3\rangle$;
> - $\mathbf u_2 = \mathbf v_2 + \mathbf v_3 = \langle -10, 7, 5\rangle$;
> - $\mathbf u_3 = 2\mathbf v_1 + \mathbf v_2 + \mathbf v_3 = \langle -24, 11, 17\rangle$.
>
> Es decir, $[\mathbf u_1\ \mathbf u_2\ \mathbf u_3] = [\mathbf v_1\ \mathbf v_2\ \mathbf v_3]\,P$.

### 2. Bases abstractas
$\mathcal B = \{\mathbf b_1, \mathbf b_2, \mathbf b_3\}$ y $\mathcal C = \{\mathbf b_1 + \mathbf b_2 + \mathbf b_3,\ \mathbf b_2 - 2\mathbf b_3,\ \mathbf b_3\}$ son bases de $\mathbb{P}_2$. (a) Encuentre $P_{\mathcal C \leftarrow \mathcal B}$. (b) Si $[1 + x - x^2]_{\mathcal C} = \langle -1, 2, 1\rangle$, encuentre $[2 + 2x - 2x^2]_{\mathcal B}$.

> [!example]- Solución
> (a) Lo fácil es escribir $\mathcal C$ en $\mathcal B$: $P_{\mathcal B \leftarrow \mathcal C} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & -2 & 1 \end{bmatrix}$. Invirtiendo (es triangular):
> $$P_{\mathcal C \leftarrow \mathcal B} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ -3 & 2 & 1 \end{bmatrix}.$$
> (b) $[1 + x - x^2]_{\mathcal B} = P_{\mathcal B \leftarrow \mathcal C}\langle -1, 2, 1\rangle = \langle -1, 1, -4\rangle$. Como $2 + 2x - 2x^2$ es el doble, por linealidad de las coordenadas: $\langle -2, 2, -8\rangle$.

### 3. Encontrar la base de llegada en $\mathbb{P}_1$
$\mathcal B = \{1 + x, 1 - 2x\}$ y $P = \begin{bmatrix} 2 & 3 \\ -1 & 1 \end{bmatrix} = P_{\mathcal C \leftarrow \mathcal B}$ con $\mathcal C = \{w_1, w_2\}$. Encuentre $w_1$ y $w_2$.

> [!example]- Solución
> Se necesitan los $w_j$ en coordenadas de $\mathcal B$, que son las columnas de $P_{\mathcal B \leftarrow \mathcal C} = P^{-1} = \tfrac15\begin{bmatrix} 1 & -3 \\ 1 & 2 \end{bmatrix}$:
> - $w_1 = \tfrac15(1 + x) + \tfrac15(1 - 2x) = \tfrac25 - \tfrac15x$;
> - $w_2 = -\tfrac35(1 + x) + \tfrac25(1 - 2x) = -\tfrac15 - \tfrac75x$.

### 4. Otra base de llegada en $\mathbb{P}_1$
$\mathcal B = \{1 - x, 2 + x\}$ y $P_{\mathcal C \leftarrow \mathcal B} = \begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}$. Encuentre $\mathcal C = \{w_1, w_2\}$.

> [!example]- Solución
> $P^{-1} = \tfrac15\begin{bmatrix} 1 & 2 \\ -2 & 1 \end{bmatrix}$. Sus columnas:
> - $w_1 = \tfrac15(1 - x) - \tfrac25(2 + x) = -\tfrac35 - \tfrac35x$;
> - $w_2 = \tfrac25(1 - x) + \tfrac15(2 + x) = \tfrac45 - \tfrac15x$.

### 5. Base de llegada en $\mathbb{P}_2$
$\mathcal B = \{x^2 + 1, x - 2, 2x + 1\}$ y $P_{\mathcal C \leftarrow \mathcal B} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 0 \\ 1 & 1 & 2 \end{bmatrix}$. Encuentre $\mathcal C$.

> [!example]- Solución
> $P_{\mathcal B \leftarrow \mathcal C} = (P_{\mathcal C \leftarrow \mathcal B})^{-1} = \begin{bmatrix} 2 & -1 & -1 \\ 0 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix}$. Por columnas:
> - $\mathbf c_1 = 2(x^2 + 1) - (2x + 1) = 2x^2 - 2x + 1$;
> - $\mathbf c_2 = -(x^2 + 1) + (x - 2) = -x^2 + x - 3$;
> - $\mathbf c_3 = -(x^2 + 1) + (2x + 1) = -x^2 + 2x$.

### 6. Coordenadas y matriz entre dos bases de $\mathbb{P}_2$
$\mathcal B = \{1 + t^2,\ t - 3t^2,\ 1 + t - 3t^2\}$ y $\mathcal C = \{1 + t, 1 - t, t^2\}$. (a) Encuentre $[2 + 2t - 4t^2]_{\mathcal B}$. (b) Encuentre $P_{\mathcal C \leftarrow \mathcal B}$.

> [!example]- Solución
> (a) $a(1 + t^2) + b(t - 3t^2) + c(1 + t - 3t^2)$: constante $a + c = 2$, $t$: $b + c = 2$, $t^2$: $a - 3b - 3c = -4$. Con $a = 2 - c$ y $b = 2 - c$: $2 - c - 6 + 3c - 3c = -4$, o sea $c = 0$. Resultado: $\langle 2, 2, 0\rangle$.
> (b) Se escalona $[\mathbf c_1\ \mathbf c_2\ \mathbf c_3 \mid \mathbf b_1\ \mathbf b_2\ \mathbf b_3]$ en coordenadas estándar:
> $$\left[\begin{array}{ccc|ccc} 1 & 1 & 0 & 1 & 0 & 1 \\ 1 & -1 & 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 1 & -3 & -3 \end{array}\right] \sim \left[\begin{array}{ccc|ccc} 1 & 0 & 0 & \frac12 & \frac12 & 1 \\ 0 & 1 & 0 & \frac12 & -\frac12 & 0 \\ 0 & 0 & 1 & 1 & -3 & -3 \end{array}\right].$$
> $P_{\mathcal C \leftarrow \mathcal B}$ es el bloque derecho.

### 7. Matriz hacia la base estándar y una ecuación para las coordenadas
$\mathcal B = \{1 + t, 1 + t^2, t + t^2\}$ en $\mathbb{P}_2$. (a) Encuentre la matriz de cambio de $\mathcal B$ a la base canónica. (b) Úsela para escribir una ecuación cuya solución sean las coordenadas de $6 + 3t - t^2$ en $\mathcal B$, y resuélvala.

> [!example]- Solución
> (a) Las columnas son los coeficientes: $P = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}$.
> (b) $P\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 6 \\ 3 \\ -1 \end{bmatrix}$, cuya solución es $\langle 5, 1, -2\rangle$.

## Preguntas de repaso

> [!question]- En los ejercicios 3, 4 y 5, ¿por qué hay que invertir $P$?
> Porque $P_{\mathcal C \leftarrow \mathcal B}$ tiene en sus columnas a $\mathcal B$ escrita en $\mathcal C$, pero lo que se necesita es $\mathcal C$ escrita en $\mathcal B$ (la base conocida). Esas columnas están en $P_{\mathcal B \leftarrow \mathcal C} = P^{-1}$.

> [!question]- En el ejercicio 1 no hubo que invertir. ¿Por qué?
> Porque la base conocida era la de llegada, $\mathcal C$, y se buscaba la de partida: sus coordenadas en $\mathcal C$ ya estaban en las columnas de $P$.

> [!question]- ¿Qué propiedad permite pasar de las coordenadas de $p$ a las de $2p$ sin recalcular?
> La linealidad del mapa de coordenadas: $[c\,p]_{\mathcal B} = c[p]_{\mathcal B}$.
