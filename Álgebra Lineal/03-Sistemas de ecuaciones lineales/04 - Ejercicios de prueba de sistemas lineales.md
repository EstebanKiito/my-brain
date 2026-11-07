---
ramo: "Álgebra Lineal"
tema: "Sistemas de ecuaciones lineales"
tags:
  - algebra-lineal/sistemas
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Producto matriz-vector y ecuación vectorial]]"
---

# Ejercicios de prueba de sistemas lineales

Preguntas de interrogaciones anteriores sobre sistemas, matrices ampliadas y la relación entre $A\mathbf x = \mathbf b$ y el conjunto generado por las columnas. Las reducciones usan solo operaciones elementales; el algoritmo general se formaliza en el tema siguiente.

## Ejercicios

### 1. Resolver un sistema con matrices
Resuelva $\begin{cases} a + b + c = 2 \\ a - b + c = 6 \\ 4a + 2b + c = 3 \end{cases}$.

> [!example]- Solución
> $$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 1 & -1 & 1 & 6 \\ 4 & 2 & 1 & 3 \end{array}\right] \xrightarrow[F_3 - 4F_1]{F_2 - F_1} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & -2 & 0 & 4 \\ 0 & -2 & -3 & -5 \end{array}\right] \xrightarrow{F_3 - F_2} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & -2 & 0 & 4 \\ 0 & 0 & -3 & -9 \end{array}\right]$$
> Sustitución hacia atrás: $c = 3$, $b = -2$ y $a = 2 - b - c = 1$. Solución única $(a, b, c) = (1, -2, 3)$.

### 2. Sistemas y posiciones de planos
Asocie cada sistema a una posición de tres planos: I (se cortan en una recta), II (en un punto), III (sin punto común).
$$A: \begin{cases} x + y - z = 3 \\ x - y - z = 1 \\ 2x + y - 2z = 0 \end{cases} \quad B: \begin{cases} x + y - z = 3 \\ x - y - z = 1 \\ x + 2y - z = 4 \end{cases} \quad C: \begin{cases} x + y - z = 3 \\ x - y - z = 1 \\ x + 2y + z = 1 \end{cases}$$

> [!example]- Solución
> En los tres, $F_2 - F_1$ da $-2y = -2$, o sea $y = 1$.
> - **A:** $F_3 - 2F_1$ da $-y = -6$, o sea $y = 6$. Contradicción: **III**.
> - **B:** $F_3 - F_1$ da $y = 1$, compatible. Queda $x - z = 2$ con $z$ libre: una recta, **I**.
> - **C:** $F_3 - F_1$ da $y + 2z = -2$, así que $z = -\tfrac32$ y $x = 3 - y + z = \tfrac12$. Un punto, **II**.

### 3. V o F: consistencia por linealidad
Si $A\langle 1, 0, 1\rangle = \langle 1, 1\rangle$ y $A\langle 1, 1, 0\rangle = \langle 1, 2\rangle$, entonces $A\mathbf x = \langle 2, 3\rangle$ es consistente.

> [!example]- Solución
> **Verdadero.** $\langle 2, 3\rangle = \langle 1, 1\rangle + \langle 1, 2\rangle$, así que por linealidad $A(\langle 1, 0, 1\rangle + \langle 1, 1, 0\rangle) = A\langle 2, 1, 1\rangle = \langle 2, 3\rangle$. El vector $\langle 2, 1, 1\rangle$ es una solución.

### 4. V o F: solución para todo $\mathbf b$
Con $A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 3 & 0 \end{bmatrix}$, $A\mathbf x = \mathbf b$ tiene solución para todo $\mathbf b \in \mathbb{R}^2$.

> [!example]- Solución
> **Verdadero.** $F_2 - F_1$ da $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & -3 \end{bmatrix}$, con un pivote en cada una de las dos filas. Por el teorema de existencia, las columnas generan $\mathbb{R}^2$: ninguna fila de la ampliada puede quedar como $[0\ 0\ 0 \mid c]$.

### 5. Un vector fuera de un plano
Encuentre los $h$ tales que $\mathbf y = \langle -4, 3, h\rangle$ queda **fuera** del plano generado por $\mathbf v_1 = \langle 1, -1, -2\rangle$ y $\mathbf v_2 = \langle 5, -4, -7\rangle$.

> [!example]- Solución
> $\mathbf y \in \operatorname{Gen}\{\mathbf v_1, \mathbf v_2\}$ si y solo si $[\mathbf v_1\ \mathbf v_2 \mid \mathbf y]$ es consistente:
> $$\left[\begin{array}{cc|c} 1 & 5 & -4 \\ -1 & -4 & 3 \\ -2 & -7 & h \end{array}\right] \xrightarrow[F_3 + 2F_1]{F_2 + F_1} \left[\begin{array}{cc|c} 1 & 5 & -4 \\ 0 & 1 & -1 \\ 0 & 3 & h - 8 \end{array}\right] \xrightarrow{F_3 - 3F_2} \left[\begin{array}{cc|c} 1 & 5 & -4 \\ 0 & 1 & -1 \\ 0 & 0 & h - 5 \end{array}\right]$$
> Es inconsistente si y solo si $h - 5 \neq 0$. Queda fuera del plano para $h \neq 5$.

### 6. Un vector que nunca está en el generado
¿Para qué $h$ está $\mathbf v_3 = \langle 2, -5, h\rangle$ en $\operatorname{Gen}\{\mathbf v_1, \mathbf v_2\}$, con $\mathbf v_1 = \langle 1, -3, -5\rangle$ y $\mathbf v_2 = \langle -3, 9, 15\rangle$?

> [!example]- Solución
> $\left[\begin{array}{cc|c} 1 & -3 & 2 \\ -3 & 9 & -5 \\ -5 & 15 & h \end{array}\right] \xrightarrow[F_3 + 5F_1]{F_2 + 3F_1} \left[\begin{array}{cc|c} 1 & -3 & 2 \\ 0 & 0 & 1 \\ 0 & 0 & h + 10 \end{array}\right]$. La segunda fila dice $0 = 1$ sin importar $h$: **para ningún $h$**. Geométricamente, $\mathbf v_2 = -3\mathbf v_1$, así que el generado es solo una recta, y $\mathbf v_3$ no es múltiplo de $\mathbf v_1$ (por las dos primeras componentes).

### 7. Condiciones sobre $\mathbf b$
Sea $A = \begin{bmatrix} 1 & 3 & 2 & 1 \\ 0 & 1 & 4 & 2 \\ 0 & 3 & 2 & 5 \\ 3 & 6 & 9 & 12 \\ 2 & 4 & 6 & 8 \end{bmatrix}$. ¿De qué tamaño es $\mathbf x$ en $A\mathbf x = \mathbf b$, y qué condición debe cumplir $\mathbf b$ para que sea consistente?

> [!example]- Solución
> $A$ tiene 4 columnas, así que $\mathbf x \in \mathbb{R}^4$. Las filas 4 y 5 son $3\mathbf r$ y $2\mathbf r$ con $\mathbf r = [1\ 2\ 3\ 4]$, así que $2F_4 - 3F_5$ anula la fila 5 de $A$ y en la ampliada deja $[0\ 0\ 0\ 0 \mid 2b_4 - 3b_5]$. Las filas 1 a 4 escalonan con cuatro pivotes, así que no aparece otra restricción. Consistente si y solo si $2b_4 = 3b_5$.

### 8. Tres planos que se cortan en una recta
¿Qué deben cumplir $a, b$ para que $x + y + z = 1$, $x + 2y + 3z = 2$ y $2x + ay + bz = 3$ se corten en una recta? Dé la recta.

> [!example]- Solución
> Las dos primeras ecuaciones ya se cortan en una recta: restándolas, $y + 2z = 1$, y $x = 1 - y - z = z$. Con $z = t$: $(t,\ 1 - 2t,\ t)$. El tercer plano debe contener esa recta: $2t + a(1 - 2t) + bt = 3$ para todo $t$, o sea $a = 3$ (término constante) y $2 - 2a + b = 0$, es decir $b = 4$ (coeficiente de $t$). Con $a = 3$, $b = 4$ la recta es $x = t$, $y = 1 - 2t$, $z = t$.

## Preguntas de repaso

> [!question]- ¿Qué tienen en común los ejercicios 5, 6 y 7?
> Los tres preguntan si un vector está en un conjunto generado. Se responden escalonando la ampliada y exigiendo que no aparezca una fila $[0 \cdots 0 \mid c]$ con $c \neq 0$.

> [!question]- En el ejercicio 8, ¿por qué exigir que la recta esté en el tercer plano "para todo $t$" da dos ecuaciones?
> Porque un polinomio en $t$ es cero para todo $t$ solo si todos sus coeficientes son cero: el término constante y el coeficiente de $t$ dan una condición cada uno.

> [!question]- ¿Qué diferencia hay entre escalonar $A$ y escalonar $[A \mid \mathbf b]$ al estudiar consistencia?
> Escalonar $A$ dice si hay solución **para todo** $\mathbf b$ (pivote en cada fila). Escalonar la ampliada dice si hay solución **para ese** $\mathbf b$ en particular, y qué condiciones debe cumplir.
