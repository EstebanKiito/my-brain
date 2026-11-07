---
ramo: "Álgebra Lineal"
tema: "Conjuntos solución e independencia lineal"
tags:
  - algebra-lineal/independencia
  - origen/complemento
prerrequisitos:
  - "[[02 - Combinaciones lineales y conjunto generado]]"
  - "[[01 - Sistemas homogéneos y forma paramétrica]]"
---

# Independencia lineal

Al generar un espacio con varios vectores, algunos pueden sobrar: si uno ya es combinación de los demás, quitarlo no cambia lo que se genera. La **independencia lineal** formaliza la idea de "ningún vector sobra". Es la contraparte de la generación: generar responde **cuánto alcanzan** los vectores; la independencia, **si hay redundancia**. Juntas definirán más adelante las bases y la dimensión.

## Definición

> [!tip] Definición
> Un conjunto $\{\mathbf v_1, \dots, \mathbf v_p\}$ de $\mathbb{R}^n$ es **linealmente independiente** (LI) si la ecuación
> $$c_1\mathbf v_1 + c_2\mathbf v_2 + \dots + c_p\mathbf v_p = \mathbf 0$$
> tiene **solo** la solución trivial $c_1 = \dots = c_p = 0$. Si existe una solución no trivial, el conjunto es **linealmente dependiente** (LD), y esa ecuación con pesos no todos nulos es una **relación de dependencia lineal**.

**Ejemplo.** $\mathbf v_1 = \langle 1, 2\rangle$ y $\mathbf v_2 = \langle 3, 6\rangle$ son LD: $3\mathbf v_1 - \mathbf v_2 = \mathbf 0$.

## Cómo decidirlo: un sistema homogéneo

La ecuación de la definición es $A\mathbf c = \mathbf 0$ con $A = [\mathbf v_1 \cdots \mathbf v_p]$. Por el teorema de los sistemas homogéneos:

> [!tip] Criterio
> Las columnas de $A$ son LI $\iff$ $A\mathbf x = \mathbf 0$ tiene solo la solución trivial $\iff$ **toda columna de $A$ es columna pivote** (no hay variables libres).

**Ejemplo (LI).** $\mathbf v_1 = \langle 1, -2, 3\rangle$, $\mathbf v_2 = \langle 4, 1, 5\rangle$, $\mathbf v_3 = \langle 7, 0, 4\rangle$:

$$
\begin{bmatrix} 1 & 4 & 7 \\ -2 & 1 & 0 \\ 3 & 5 & 4 \end{bmatrix} \sim \begin{bmatrix} 1 & 4 & 7 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}.
$$

Tres pivotes en tres columnas: el conjunto es LI.

**Ejemplo (LD).** Las columnas de $A = \begin{bmatrix} 1 & 4 & 2 \\ 2 & 5 & 1 \\ 3 & 6 & 0 \end{bmatrix}$:

$$
A \sim \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}.
$$

$x_3$ es libre: son LD. Con $x_3 = 1$ se obtiene $x_1 = 2$, $x_2 = -1$, es decir, la relación $2\mathbf a_1 - \mathbf a_2 + \mathbf a_3 = \mathbf 0$, o bien $\mathbf a_3 = -2\mathbf a_1 + \mathbf a_2$.

## Casos que se deciden sin escalonar

> [!tip] Atajos
> 1. **Un vector** $\{\mathbf v\}$ es LI si y solo si $\mathbf v \neq \mathbf 0$.
> 2. **Dos vectores** son LD si y solo si uno es múltiplo del otro.
> 3. Un conjunto que **contiene al vector $\mathbf 0$** es LD ($1 \cdot \mathbf 0 = \mathbf 0$ es una relación no trivial).
> 4. Si hay **más vectores que componentes** ($p > n$), el conjunto es LD.
> 5. $\{\mathbf v_1, \dots, \mathbf v_p\}$ con $\mathbf v_1 \neq \mathbf 0$ es LD si y solo si **algún** $\mathbf v_j$ es combinación lineal de los **anteriores** $\mathbf v_1, \dots, \mathbf v_{j-1}$.

El 4 se debe a que la matriz $n \times p$ tiene a lo más $n$ pivotes para $p > n$ columnas: queda una variable libre. Por ejemplo, cuatro vectores de $\mathbb{R}^3$ siempre son LD, sin importar cuáles sean.

**Ejemplos rápidos.**

- $\langle -2, 4, 6, 10\rangle$ y $\langle 3, -6, -9, 15\rangle$: el factor sería $-\tfrac32$ en las tres primeras componentes, pero $-\tfrac32 \cdot 10 = -15 \neq 15$. No son múltiplos: **LI**.
- $\langle 1, 2, 3\rangle$, $\langle 2, 4, 6\rangle$, $\langle -1, -2, 3\rangle$: el segundo es el doble del primero, **LD**.
- $\langle 2, 3, 5\rangle$, $\langle 0, 0, 0\rangle$, $\langle 1, 1, 8\rangle$: contiene al cero, **LD**.

> [!warning] LD no significa que todos los vectores sobren
> En un conjunto LD, **algún** vector es combinación de los otros, no necesariamente **cada** uno. En $\{\langle 1, 1\rangle, \langle 2, 2\rangle, \langle 1, 0\rangle\}$, el tercero no es combinación de los dos primeros (que solo generan la recta $y = x$).

> [!warning] LI y generar son cosas distintas
> Las columnas de $\begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix}$ generan $\mathbb{R}^3$ (pivote en cada fila) pero son LD (cuatro vectores en $\mathbb{R}^3$). Generar mira las **filas** con pivote; la independencia, las **columnas** con pivote.

## Independencia y unicidad

La independencia responde la pregunta de unicidad que quedó pendiente: si las columnas de $A$ son LI, $A\mathbf x = \mathbf b$ tiene **a lo más una** solución para cada $\mathbf b$. Si son LD, cualquier $\mathbf b$ alcanzable se alcanza de infinitas maneras, porque se le puede sumar una relación de dependencia.

## Preguntas de repaso

> [!question]- ¿Son LI $\langle 1, 0, 2\rangle$, $\langle 0, 1, -1\rangle$ y $\langle 2, 3, 1\rangle$?
> No: $\langle 2, 3, 1\rangle = 2\langle 1, 0, 2\rangle + 3\langle 0, 1, -1\rangle$. Al escalonar, la tercera columna no es pivote.

> [!question]- ¿Por qué cinco vectores de $\mathbb{R}^4$ son siempre LD?
> La matriz $4 \times 5$ tiene a lo más 4 pivotes, así que alguna columna no es pivote y $A\mathbf x = \mathbf 0$ tiene una variable libre, es decir, una solución no trivial.

> [!question]- Si $\{\mathbf u, \mathbf v\}$ es LI, ¿lo es $\{\mathbf u + \mathbf v, \mathbf u - \mathbf v\}$?
> Sí. De $\alpha(\mathbf u + \mathbf v) + \beta(\mathbf u - \mathbf v) = \mathbf 0$ sale $(\alpha + \beta)\mathbf u + (\alpha - \beta)\mathbf v = \mathbf 0$. Por la independencia de $\{\mathbf u, \mathbf v\}$, $\alpha + \beta = 0$ y $\alpha - \beta = 0$, así que $\alpha = \beta = 0$.

> [!question]- V o F: si las columnas de $A$ son LI, entonces $A\mathbf x = \mathbf b$ tiene solución para todo $\mathbf b$.
> Falso. Con $A = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ la columna es LI, pero $A x = \langle 0, 1\rangle$ no tiene solución. La independencia asegura unicidad, no existencia.

> [!question]- Si $\mathbf w \in \operatorname{Gen}\{\mathbf u, \mathbf v\}$, ¿qué se puede decir de $\{\mathbf u, \mathbf v, \mathbf w\}$?
> Que es LD: si $\mathbf w = a\mathbf u + b\mathbf v$, entonces $a\mathbf u + b\mathbf v - \mathbf w = \mathbf 0$ es una relación no trivial (el peso de $\mathbf w$ es $-1$).
