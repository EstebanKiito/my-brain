---
ramo: "Álgebra Lineal"
tema: "Conjuntos solución e independencia lineal"
tags:
  - algebra-lineal/sistemas
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Soluciones de sistemas no homogéneos]]"
---

# Ejercicios de prueba de conjuntos solución

Preguntas de interrogaciones y exámenes anteriores que se resuelven con la estructura "solución particular + soluciones homogéneas", muchas veces sin conocer la matriz. Es un tipo de pregunta que se repite casi todos los semestres.

## Ejercicios

### 1. Solución a partir de la FER y la suma de columnas
Las columnas de $A$ suman $\langle -1, -1, -3\rangle$ y su FER es $\begin{bmatrix} 1 & -1 & 0 & 0 \\ 0 & 0 & 1 & 8 \\ 0 & 0 & 0 & 0 \end{bmatrix}$. Resuelva $A\mathbf x = \langle -1, -1, -3\rangle$.

> [!example]- Solución
> **Particular:** como $A\langle 1, 1, 1, 1\rangle$ es la suma de las columnas, $\mathbf p = \langle 1, 1, 1, 1\rangle$.
> **Homogéneas:** la FER da $x_1 = x_2$ y $x_3 = -8x_4$, con $x_2, x_4$ libres: $x_2\langle 1, 1, 0, 0\rangle + x_4\langle 0, 0, -8, 1\rangle$.
> $$S = \left\{\langle 1, 1, 1, 1\rangle + x_2\langle 1, 1, 0, 0\rangle + x_4\langle 0, 0, -8, 1\rangle\right\}.$$

### 2. Particular a partir de otra combinación
$A = [\mathbf a_1\ \mathbf a_2\ \mathbf a_3\ \mathbf a_4]$ es de $2 \times 4$, equivalente por filas a $\begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}$, y $\mathbf a_1 - \mathbf a_2 + \mathbf a_3 - \mathbf a_4 = \langle 2, 2\rangle$. Resuelva $A\mathbf x = \langle 1, 1\rangle$.

> [!example]- Solución
> $A\langle 1, -1, 1, -1\rangle = \langle 2, 2\rangle$, así que por linealidad $\mathbf p = \tfrac12\langle 1, -1, 1, -1\rangle$ cumple $A\mathbf p = \langle 1, 1\rangle$.
> Homogéneas: $x_3 = 0$ y $x_1 = -x_3 - x_4 = -x_4$, con $x_2, x_4$ libres: $x_2\langle 0, 1, 0, 0\rangle + x_4\langle -1, 0, 0, 1\rangle$.
> $$S = \left\{\tfrac12\langle 1, -1, 1, -1\rangle + x_2\langle 0, 1, 0, 0\rangle + x_4\langle -1, 0, 0, 1\rangle\right\}.$$

### 3. Homogéneo y no homogéneo con la misma matriz
$A$ es de $2 \times 4$ con FER $\begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 0 & 1 & 2 \end{bmatrix}$ y columnas que suman $\langle 0, 2\rangle$. Resuelva (a) $A\mathbf x = \mathbf 0$ y (b) $A\mathbf x = \langle 0, 2\rangle$.

> [!example]- Solución
> (a) $x_1 = -x_4$, $x_3 = -2x_4$, con $x_2, x_4$ libres: $S_h = \{x_2\langle 0, 1, 0, 0\rangle + x_4\langle -1, 0, -2, 1\rangle\}$.
> (b) $\langle 1, 1, 1, 1\rangle$ es particular, así que $S = \langle 1, 1, 1, 1\rangle + S_h$.

### 4. ¿Pertenece? ¿Puede ser una recta?
$A\mathbf x = \mathbf b$ tiene solución $\{\langle 1, 0, 2, 0\rangle + t\langle -3, 1, 2, 0\rangle + s\langle 0, 0, -1, 1\rangle\}$. (a) ¿Es $\langle -5, 2, 7, -1\rangle$ solución? (b) ¿Existe $\mathbf c$ tal que $A\mathbf x = \mathbf c$ tenga como solución exactamente $\{\langle 1, 1, -1, 0\rangle + t\langle -3, 1, 2, 0\rangle\}$?

> [!example]- Solución
> (a) Hay que encontrar $t, s$ con $\langle -5, 2, 7, -1\rangle - \langle 1, 0, 2, 0\rangle = \langle -6, 2, 5, -1\rangle = t\langle -3, 1, 2, 0\rangle + s\langle 0, 0, -1, 1\rangle$. La segunda componente da $t = 2$ y la cuarta $s = -1$; la primera ($-6 = -6$) y la tercera ($5 = 4 + 1$) se cumplen. **Sí**.
> (b) **No.** Las soluciones homogéneas forman un plano ($\operatorname{Gen}$ de los dos directores, que no son paralelos). Todo $A\mathbf x = \mathbf c$ consistente tiene como solución ese plano trasladado, nunca una recta.

### 5. Construir un lado derecho
$A\mathbf x = \mathbf 0$ tiene solución $\{t\langle 1, 2, 0, -1\rangle + s\langle 2, -1, 3, 0\rangle\}$. (a) ¿Es $\mathbf w = \langle -1, 3, -6, -1\rangle$ solución de $A\mathbf x = \mathbf 0$? (b) ¿Existe $\mathbf c$ tal que $A\mathbf x = \mathbf c$ tenga solución $\{\mathbf w + t\langle 1, 2, 0, -1\rangle + s\langle 2, -1, 3, 0\rangle\}$?

> [!example]- Solución
> (a) La tercera componente da $3s = -6$, o sea $s = -2$; la cuarta, $-t = -1$, o sea $t = 1$. Pero la primera daría $t + 2s = -3 \neq -1$. **No.**
> (b) **Sí:** $\mathbf c = A\mathbf w$. Con ese $\mathbf c$, $\mathbf w$ es una solución particular y, por el teorema de la traslación, el conjunto solución es $\mathbf w + S_h$, que es exactamente el pedido. No importa que $\mathbf w$ no sea solución homogénea.

### 6. Leer la homogénea desde la no homogénea
$A\mathbf x = \mathbf b$ tiene solución $\{\langle 1, 2, 1, 0\rangle + t\langle -1, 1, 1, 1\rangle + s\langle 0, 0, 1, 2\rangle\}$. (a) ¿Cuál es la solución de $A\mathbf x = \mathbf 0$? (b) ¿Es $\langle 2, 4, 2, 0\rangle$ solución de $A\mathbf x = \mathbf b$? (c) ¿Existe $\mathbf c$ para el que la solución de $A\mathbf x = \mathbf c$ sea una recta?

> [!example]- Solución
> (a) $S_h = \{t\langle -1, 1, 1, 1\rangle + s\langle 0, 0, 1, 2\rangle\}$: se borra la parte particular.
> (b) La primera componente exige $1 - t = 2$, o sea $t = -1$; la segunda, $2 + t = 4$, o sea $t = 2$. Contradicción: **no**. (También: $\langle 2, 4, 2, 0\rangle = 2\mathbf p$ y $A(2\mathbf p) = 2\mathbf b \neq \mathbf b$ si $\mathbf b \neq \mathbf 0$.)
> (c) **No**: cualquier solución consistente es un plano trasladado.

### 7. Verdadero o falso
(a) Si $\mathbf w$ resuelve $A\mathbf x = \mathbf b$, existe $\mathbf q$ tal que $\mathbf w - \mathbf q$ es una solución **no nula** de $A\mathbf x = \mathbf 0$. (b) Si $A\mathbf x = \langle 1, 3, 2\rangle$ tiene infinitas soluciones, $A\mathbf x = \mathbf 0$ también.

> [!example]- Solución
> (a) **Falso.** Con $A = I_2$, la única solución de $A\mathbf x = \mathbf 0$ es $\mathbf 0$, así que no hay soluciones homogéneas no nulas.
> (b) **Verdadero.** El conjunto solución de $A\mathbf x = \mathbf b$ es $\mathbf p + S_h$; si es infinito, $S_h$ es infinito.

### 8. Columnas con relaciones conocidas
$A = [\mathbf v_1\ \mathbf v_2\ \mathbf v_3\ \mathbf v_4]$ es de $3 \times 4$ con $\{\mathbf v_1, \mathbf v_2\}$ LI, $\mathbf v_3 = \mathbf v_1 + \mathbf v_2$ y $\mathbf v_4 = \mathbf v_2 + \mathbf v_3$. (a) Resuelva $A\mathbf x = \mathbf 0$. (b) Resuelva $A\mathbf x = 2\mathbf v_1 - \mathbf v_2$. (c) ¿Qué objeto geométrico es el generado por las columnas?

> [!example]- Solución
> (a) $\mathbf v_4 = \mathbf v_1 + 2\mathbf v_2$. Las relaciones $\mathbf v_1 + \mathbf v_2 - \mathbf v_3 = \mathbf 0$ y $\mathbf v_1 + 2\mathbf v_2 - \mathbf v_4 = \mathbf 0$ dan $\langle -1, -1, 1, 0\rangle$ y $\langle -1, -2, 0, 1\rangle$ (con signo cambiado). Como $\mathbf v_1, \mathbf v_2$ son LI, las columnas 1 y 2 son pivote y las 3 y 4 libres: $S_h = \{s\langle -1, -1, 1, 0\rangle + t\langle -1, -2, 0, 1\rangle\}$.
> (b) Particular evidente: $\langle 2, -1, 0, 0\rangle$. Solución: $\langle 2, -1, 0, 0\rangle + S_h$.
> (c) $\operatorname{Gen}\{\mathbf v_1, \mathbf v_2, \mathbf v_3, \mathbf v_4\} = \operatorname{Gen}\{\mathbf v_1, \mathbf v_2\}$, un **plano por el origen** en $\mathbb{R}^3$.

## Preguntas de repaso

> [!question]- ¿Qué dos datos bastan para escribir la solución de $A\mathbf x = \mathbf b$ sin conocer $A$?
> Una solución particular (por ejemplo, de una combinación conocida de columnas que dé $\mathbf b$) y las soluciones homogéneas (que se leen de la FER o de relaciones conocidas entre columnas).

> [!question]- ¿Por qué en el ejercicio 5(b) la respuesta es sí aunque $\mathbf w$ no sea solución homogénea?
> Porque basta definir $\mathbf c = A\mathbf w$. Entonces $\mathbf w$ es solución particular de $A\mathbf x = \mathbf c$, y su conjunto solución es $\mathbf w + S_h$.

> [!question]- ¿Cómo se comprueba si un vector pertenece a un conjunto dado en forma paramétrica?
> Se resta el punto base y se plantea el sistema para los parámetros. Si las componentes "fáciles" fijan los parámetros, hay que verificar que el resto de las componentes también se cumpla.
