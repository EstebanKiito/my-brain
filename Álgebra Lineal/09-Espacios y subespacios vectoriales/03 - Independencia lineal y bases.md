---
ramo: "Álgebra Lineal"
tema: "Espacios y subespacios vectoriales"
tags:
  - algebra-lineal/espacios
  - algebra-lineal/independencia
  - origen/complemento
prerrequisitos:
  - "[[02 - Subespacios]]"
  - "[[03 - Independencia lineal]]"
---

# Independencia lineal y bases

En $\mathbb{R}^3$ los ejes coordenados permiten describir cualquier punto con tres números. Una **base** es la versión general de esos ejes: un conjunto de vectores que alcanza para generar todo el espacio (o subespacio) sin que ninguno sobre. Es la unión de las dos ideas anteriores: **generar** e **independencia lineal**.

## Independencia lineal en cualquier espacio

La definición es idéntica a la de $\mathbb{R}^n$: $\{\mathbf v_1, \dots, \mathbf v_p\} \subseteq V$ es **linealmente independiente** si $c_1\mathbf v_1 + \dots + c_p\mathbf v_p = \mathbf 0$ solo tiene la solución $c_1 = \dots = c_p = 0$, y **dependiente** si tiene otra. Valen los mismos atajos: un vector es LI si no es cero; dos son LD si uno es múltiplo del otro; un conjunto con $\mathbf 0$ es LD; y un conjunto con $\mathbf v_1 \neq \mathbf 0$ es LD si y solo si algún $\mathbf v_j$ es combinación de los anteriores.

**Ejemplo en $\mathbb{P}$.** $p_1 = 1$, $p_2 = t$, $p_3 = 4 - t$ son LD: $p_3 = 4p_1 - p_2$.

En espacios de polinomios o matrices, la ecuación $c_1\mathbf v_1 + \dots = \mathbf 0$ se resuelve **igualando coeficientes** (o entradas), lo que da un sistema homogéneo. Por ejemplo, $1 + x - x^2$, $1 + x$ y $1 - x^2$ son LI en $\mathbb{P}_2$: igualando coeficientes de $1$, $x$ y $x^2$ se obtiene un sistema cuya matriz $\begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ -1 & 0 & -1 \end{bmatrix}$ tiene determinante $1 \neq 0$, así que solo admite la solución trivial.

## Bases

> [!tip] Definición
> Sea $H$ un subespacio de $V$. Un conjunto $\mathcal B = \{\mathbf b_1, \dots, \mathbf b_p\} \subseteq V$ es una **base** de $H$ si
> 1. $\mathcal B$ es linealmente independiente, y
> 2. $H = \operatorname{Gen}\{\mathbf b_1, \dots, \mathbf b_p\}$.

**Bases estándar.**
- En $\mathbb{R}^n$: $\{\mathbf e_1, \dots, \mathbf e_n\}$, las columnas de $I_n$.
- En $\mathbb{P}_n$: $\{1, t, t^2, \dots, t^n\}$. Generan, porque todo polinomio de grado $\leq n$ es una combinación de ellos, y son LI, porque un polinomio es el polinomio nulo solo si todos sus coeficientes son cero.
- En $M_{2 \times 2}$: las cuatro matrices con un 1 en una posición y 0 en el resto.

**Columnas de una matriz invertible.** Si $A$ es de $n \times n$ e invertible, sus columnas son LI y generan $\mathbb{R}^n$ (teorema de la matriz invertible): forman una base de $\mathbb{R}^n$.

**Ejemplo.** ¿Es $\{\langle 3, 0, -6\rangle, \langle -4, 1, 7\rangle, \langle -2, 1, 5\rangle\}$ una base de $\mathbb{R}^3$? La matriz con esas columnas se escalona a una con tres pivotes (su determinante es 6). Es invertible, así que **sí**.

## Teorema del conjunto generador

> [!tip] Teorema del conjunto generador
> Sea $S = \{\mathbf v_1, \dots, \mathbf v_p\}$ y $H = \operatorname{Gen} S$.
> 1. Si algún $\mathbf v_k$ es combinación lineal de los demás, quitarlo de $S$ **no cambia** el generado.
> 2. Si $H \neq \{\mathbf 0\}$, algún subconjunto de $S$ es una base de $H$.

Para obtener una base de un generado, se van eliminando vectores redundantes hasta que el conjunto quede LI.

**Ejemplo.** $\mathbf v_1 = \langle 0, 2, -1\rangle$, $\mathbf v_2 = \langle 2, 2, 0\rangle$ y $\mathbf v_3 = \langle 6, 16, -5\rangle = 5\mathbf v_1 + 3\mathbf v_2$. Quitando $\mathbf v_3$, $H = \operatorname{Gen}\{\mathbf v_1, \mathbf v_2\}$, y como $\mathbf v_1, \mathbf v_2$ no son paralelos, $\{\mathbf v_1, \mathbf v_2\}$ es base de $H$.

## Dos miradas de una base

> [!tip] Una base es a la vez
> - un conjunto **generador lo más chico posible** (quitar cualquier vector deja de generar), y
> - un conjunto **independiente lo más grande posible** (agregar cualquier vector lo vuelve dependiente).

En $\mathbb{R}^3$:

| Conjunto | ¿LI? | ¿Genera $\mathbb{R}^3$? |
|---|---|---|
| $\langle 1, 0, 0\rangle, \langle 2, 3, 0\rangle$ | sí | no (solo el plano $z = 0$) |
| $\langle 1, 0, 0\rangle, \langle 2, 3, 0\rangle, \langle 4, 5, 6\rangle$ | sí | sí: **base** |
| los tres anteriores y $\langle 7, 8, 9\rangle$ | no | sí |

## Preguntas de repaso

> [!question]- ¿Es $\{1 + t, 1 - t, t^2\}$ una base de $\mathbb{P}_2$?
> Sí. Igualando coeficientes, tanto la independencia como la generación se reducen a sistemas con la matriz $\begin{bmatrix} 1 & 1 & 0 \\ 1 & -1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, de determinante $-2 \neq 0$. Como es invertible, $c_1(1 + t) + c_2(1 - t) + c_3t^2 = \mathbf 0$ solo tiene la solución trivial y cualquier $a + bt + ct^2$ se alcanza.

> [!question]- ¿Por qué un conjunto que genera $V$ pero es LD no es una base?
> Porque tiene vectores que sobran: alguno es combinación de los otros. Además, con un conjunto LD un mismo vector se escribe de varias formas, y una base debe dar coordenadas únicas.

> [!question]- Encuentre una base del generado por $\langle 1, 2\rangle$, $\langle 2, 4\rangle$ y $\langle 0, 1\rangle$.
> $\langle 2, 4\rangle = 2\langle 1, 2\rangle$ sobra. Quedan $\langle 1, 2\rangle$ y $\langle 0, 1\rangle$, que no son paralelos: son base, y generan todo $\mathbb{R}^2$.

> [!question]- V o F: si $\{\mathbf u, \mathbf v\}$ es LI en $\mathbb{R}^3$, es una base de $\mathbb{R}^3$.
> Falso. Dos vectores generan a lo más un plano. Es base del plano que generan, no de $\mathbb{R}^3$.
