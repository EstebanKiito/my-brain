---
ramo: "Álgebra Lineal"
tema: "Coordenadas, dimensión y rango"
tags:
  - algebra-lineal/espacios
  - origen/complemento
prerrequisitos:
  - "[[01 - Sistemas de coordenadas]]"
---

# Dimensión

Un espacio vectorial puede tener muchas bases distintas, pero todas tienen **la misma cantidad de vectores**. Ese número, la **dimensión**, mide el "tamaño" del espacio: cuántos parámetros libres hacen falta para describir un vector cualquiera. Formaliza la intuición de que una recta es de dimensión 1, un plano de dimensión 2 y $\mathbb{R}^3$ de dimensión 3, y la extiende a polinomios, matrices y subespacios.

## Todas las bases tienen el mismo tamaño

> [!tip] Teorema
> Si $V$ tiene una base con $n$ vectores, entonces:
> - todo conjunto de $V$ con **más de $n$** vectores es LD;
> - ningún conjunto con **menos de $n$** vectores genera $V$.
>
> En consecuencia, **todas las bases de $V$ tienen exactamente $n$ vectores**.

La demostración pasa a coordenadas: más de $n$ vectores de $V$ dan más de $n$ vectores en $\mathbb{R}^n$, que son LD; y el isomorfismo de coordenadas conserva la dependencia.

> [!tip] Definición
> Si $V$ es generado por un conjunto finito, es de **dimensión finita** y $\dim V$ es el número de vectores de cualquier base. $\dim\{\mathbf 0\} = 0$. Si no hay un generador finito, $V$ es de **dimensión infinita**.

| Espacio | Base estándar | Dimensión |
|---|---|---|
| $\mathbb{R}^n$ | $\mathbf e_1, \dots, \mathbf e_n$ | $n$ |
| $\mathbb{P}_n$ | $1, t, \dots, t^n$ | $n + 1$ |
| $M_{m \times n}$ | matrices con un solo 1 | $mn$ |
| $\mathbb{P}$ (todos los polinomios) | $1, t, t^2, \dots$ | infinita |

> [!warning] $\dim\mathbb{P}_n = n + 1$
> $\mathbb{P}_4$ tiene dimensión 5 (la base es $1, t, t^2, t^3, t^4$), no 4. El término constante cuenta.

## Calcular la dimensión de un subespacio

Se encuentra una base y se cuentan sus vectores.

**Ejemplo.** $H = \{\langle a - 3b + 6c,\ 5a + 4d,\ b - 2c - d,\ 5d\rangle\}$. Separando por parámetros, $H = \operatorname{Gen}\{\mathbf v_1, \mathbf v_2, \mathbf v_3, \mathbf v_4\}$ con $\mathbf v_1 = \langle 1, 5, 0, 0\rangle$, $\mathbf v_2 = \langle -3, 0, 1, 0\rangle$, $\mathbf v_3 = \langle 6, 0, -2, 0\rangle$ y $\mathbf v_4 = \langle 0, 4, -1, 5\rangle$. Como $\mathbf v_3 = -2\mathbf v_2$, sobra; los otros tres son LI. $\dim H = 3$, aunque haya cuatro parámetros.

> [!warning] Parámetros no es lo mismo que dimensión
> El número de parámetros de una descripción es una **cota superior** de la dimensión. Si los vectores que acompañan a los parámetros son LD, la dimensión es menor.

**Subespacios de $\mathbb{R}^3$ por dimensión:**
- dimensión 0: solo $\{\mathbf 0\}$;
- dimensión 1: rectas por el origen;
- dimensión 2: planos por el origen;
- dimensión 3: todo $\mathbb{R}^3$.

## Teoremas sobre subespacios y bases

> [!tip] Teorema
> Si $H$ es un subespacio de $V$ (de dimensión finita), todo conjunto LI de $H$ se puede **completar** a una base de $H$. Además, $\dim H \leq \dim V$.

> [!tip] Teorema de la base
> Si $\dim V = p \geq 1$:
> - todo conjunto **LI** de exactamente $p$ vectores es una base;
> - todo conjunto de exactamente $p$ vectores que **genera** $V$ es una base.

Es un gran ahorro: si se conoce la dimensión y se tiene la cantidad justa de vectores, basta verificar **una** de las dos condiciones. Por ejemplo, tres polinomios LI de $\mathbb{P}_2$ son automáticamente una base.

## Dimensión de Nul A y Col A

> [!tip] Resultado
> $\dim\operatorname{Nul} A$ = número de **variables libres** de $A\mathbf x = \mathbf 0$. $\dim\operatorname{Col} A$ = número de **columnas pivote** de $A$.

Con $A = \begin{bmatrix} -3 & 6 & -1 & 1 & -7 \\ 1 & -2 & 2 & 3 & -1 \\ 2 & -4 & 5 & 8 & -4 \end{bmatrix}$, que tiene pivotes en las columnas 1 y 3: $\dim\operatorname{Col} A = 2$ y $\dim\operatorname{Nul} A = 3$.

## Preguntas de repaso

> [!question]- V o F: si $V$ es generado por $\{\mathbf v_1, \mathbf v_2, \mathbf v_3\}$, entonces $\dim V = 3$.
> Falso. Solo se sabe que $\dim V \leq 3$. Si los vectores son LD (por ejemplo, los tres iguales y no nulos), $\dim V$ es menor.

> [!question]- V o F: si existe un conjunto LI $\{\mathbf v_1, \dots, \mathbf v_p\}$ en $V$, entonces $\dim V \leq p$.
> Falso: es al revés. Un conjunto LI tiene a lo más $\dim V$ vectores, así que $p \leq \dim V$. Por ejemplo, $\{\mathbf e_1, \mathbf e_2\}$ es LI en $\mathbb{R}^3$, y $3 > 2$.

> [!question]- ¿Cuál es la dimensión del espacio de matrices simétricas de $2 \times 2$?
> 3. Una simétrica es $\begin{bmatrix} a & b \\ b & c \end{bmatrix} = a\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + b\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} + c\begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$, y esas tres matrices son LI.

> [!question]- ¿Por qué cuatro vectores LI de $\mathbb{R}^4$ forman automáticamente una base?
> Por el teorema de la base: $\dim\mathbb{R}^4 = 4$, y un conjunto LI con exactamente esa cantidad de vectores genera todo el espacio.
