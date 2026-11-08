---
ramo: "Álgebra Lineal"
tema: "Coordenadas, dimensión y rango"
tags:
  - algebra-lineal/espacios
  - origen/complemento
prerrequisitos:
  - "[[02 - Dimensión]]"
  - "[[04 - Espacio nulo, espacio columna y núcleo]]"
---

# Espacio fila y teorema del rango

Una matriz tiene un tercer subespacio natural, generado por sus **filas**. El resultado central de este tema, el **teorema del rango**, conecta los tres: el espacio fila y el espacio columna tienen la misma dimensión, y esa dimensión sumada a la del espacio nulo da el número de columnas. Con eso, muchas preguntas sobre sistemas se responden solo con contar.

## Espacio fila

> [!tip] Definición
> Si $A$ es de $m \times n$, cada fila es un vector de $\mathbb{R}^n$. El **espacio fila** de $A$, $\operatorname{Fil} A$, es el generado por sus filas. Como las filas de $A$ son las columnas de $A^T$, $\operatorname{Fil} A = \operatorname{Col} A^T$.

> [!tip] Teorema
> Si $A \sim B$ (equivalentes por filas), entonces $\operatorname{Fil} A = \operatorname{Fil} B$. Si $B$ está en forma escalonada, sus **filas no nulas** forman una base de $\operatorname{Fil} A$.

Las operaciones de fila reemplazan filas por combinaciones de filas (y se pueden deshacer), así que no cambian el generado. Las filas no nulas de una escalonada son LI por su forma de escalera.

> [!warning] Tres subespacios, tres recetas distintas
> | Subespacio | Base |
> |---|---|
> | $\operatorname{Fil} A$ | filas no nulas de la **forma escalonada** |
> | $\operatorname{Col} A$ | columnas pivote de **$A$** (la original) |
> | $\operatorname{Nul} A$ | vectores de la forma paramétrica, desde la **FER** |
>
> Para filas se usa la escalonada porque las operaciones de fila no cambian $\operatorname{Fil}$; para columnas se usa $A$ porque sí cambian $\operatorname{Col}$.

**Ejemplo.** $A = \begin{bmatrix} -2 & -5 & 8 & 0 & -17 \\ 1 & 3 & -5 & 1 & 5 \\ 3 & 11 & -19 & 7 & 1 \\ 1 & 7 & -13 & 5 & -3 \end{bmatrix} \sim \begin{bmatrix} 1 & 3 & -5 & 1 & 5 \\ 0 & 1 & -2 & 2 & -7 \\ 0 & 0 & 0 & -4 & 20 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$.

- $\operatorname{Fil} A$: las tres filas no nulas de la escalonada.
- $\operatorname{Col} A$: los pivotes están en las columnas 1, 2 y 4, así que $\{\mathbf a_1, \mathbf a_2, \mathbf a_4\}$.
- $\operatorname{Nul} A$: la FER es $\begin{bmatrix} 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & -2 & 0 & 3 \\ 0 & 0 & 0 & 1 & -5 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$, que da la base $\{\langle -1, 2, 1, 0, 0\rangle, \langle -1, -3, 0, 5, 1\rangle\}$.

## El teorema del rango

> [!tip] Definición
> El **rango** de $A$ es $\operatorname{rango} A = \dim\operatorname{Col} A$.

> [!tip] Teorema del rango
> Para $A$ de $m \times n$, $\dim\operatorname{Col} A = \dim\operatorname{Fil} A = $ número de pivotes $= \operatorname{rango} A$, y
> $$\operatorname{rango} A + \dim\operatorname{Nul} A = n .$$

La igualdad entre columnas y filas se debe a que ambas dimensiones cuentan pivotes: los pivotes marcan las columnas pivote y también las filas no nulas de la escalonada. La fórmula es el conteo "columnas pivote más columnas libres igual a columnas". Una consecuencia es que $\operatorname{rango} A = \operatorname{rango} A^T$.

**Usos típicos.**
- $A$ de $7 \times 9$ con $\dim\operatorname{Nul} A = 2$: $\operatorname{rango} A = 9 - 2 = 7$.
- ¿Puede una $6 \times 9$ tener $\dim\operatorname{Nul} A = 2$? Daría rango 7, pero el rango es a lo más $\min(6, 9) = 6$. **No.**
- Un sistema homogéneo de 40 ecuaciones y 42 incógnitas cuyas soluciones son todas las combinaciones de dos soluciones LI: $\dim\operatorname{Nul} A = 2$, así que $\operatorname{rango} A = 40$. Entonces $\operatorname{Col} A$ es un subespacio de $\mathbb{R}^{40}$ de dimensión 40, es decir, todo $\mathbb{R}^{40}$: **cualquier** sistema no homogéneo con esos coeficientes tiene solución.

## Cuatro números de una matriz

Para $A$ de $m \times n$ con rango $r$:

| Subespacio | Vive en | Dimensión |
|---|---|---|
| $\operatorname{Col} A$ | $\mathbb{R}^m$ | $r$ |
| $\operatorname{Fil} A$ | $\mathbb{R}^n$ | $r$ |
| $\operatorname{Nul} A$ | $\mathbb{R}^n$ | $n - r$ |
| $\operatorname{Nul} A^T$ | $\mathbb{R}^m$ | $m - r$ |

## Teorema de la matriz invertible, continuación

Para $A$ de $n \times n$, son equivalentes a que $A$ sea invertible: las columnas forman una base de $\mathbb{R}^n$; $\operatorname{Col} A = \mathbb{R}^n$; $\dim\operatorname{Col} A = n$; $\operatorname{rango} A = n$; $\operatorname{Nul} A = \{\mathbf 0\}$; $\dim\operatorname{Nul} A = 0$.

## Preguntas de repaso

> [!question]- $A$ es de $7 \times 5$ con rango 2. Dé $\dim\operatorname{Nul} A$, $\dim\operatorname{Fil} A$, $\operatorname{rango} A^T$ y $\dim\operatorname{Nul} A^T$.
> $5 - 2 = 3$; $2$; $2$; y como $A^T$ es de $5 \times 7$, $7 - 2 = 5$.

> [!question]- ¿Por qué la base de $\operatorname{Fil} A$ sale de la escalonada pero la de $\operatorname{Col} A$ no?
> Porque las operaciones de fila combinan filas entre sí y no cambian su generado, pero sí cambian los vectores columna y su generado.

> [!question]- Si $A$ es de $3 \times 4$, ¿es cierto que $\operatorname{rango} A = 3$ si y solo si $\operatorname{Nul} A^T = \{\mathbf 0\}$? ¿Y si $A$ es de $4 \times 3$?
> Para $3 \times 4$, sí: $A^T$ es de $4 \times 3$ y $\dim\operatorname{Nul} A^T = 3 - \operatorname{rango} A$. Para $4 \times 3$, no: $\dim\operatorname{Nul} A^T = 4 - \operatorname{rango} A$, que con rango 3 vale 1, así que $\operatorname{Nul} A^T \neq \{\mathbf 0\}$.

> [!question]- ¿Puede una matriz de $5 \times 3$ tener espacio columna igual a $\mathbb{R}^5$?
> No. El rango es a lo más 3, así que $\operatorname{Col} A$ tiene dimensión a lo más 3, menor que 5.
