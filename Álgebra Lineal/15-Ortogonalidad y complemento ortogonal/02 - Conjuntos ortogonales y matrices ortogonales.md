---
ramo: "Álgebra Lineal"
tema: "Ortogonalidad y complemento ortogonal"
tags:
  - algebra-lineal/ortogonalidad
  - origen/complemento
prerrequisitos:
  - "[[01 - Complemento ortogonal]]"
  - "[[01 - Sistemas de coordenadas]]"
---

# Conjuntos ortogonales y matrices ortogonales

No todas las bases son igual de cómodas. En una base cualquiera, encontrar las coordenadas de un vector exige resolver un sistema; en una base **ortogonal**, cada coordenada sale con un solo producto punto, independiente de las demás. Por eso las bases ortogonales (y ortonormales) son las favoritas en geometría y en cálculo numérico, y las matrices cuyas columnas las forman (matrices ortogonales) se invierten simplemente transponiendo.

## Conjuntos ortogonales

> [!tip] Definición
> $\{\mathbf u_1, \dots, \mathbf u_p\} \subseteq \mathbb{R}^n$ es un **conjunto ortogonal** si cada par de vectores distintos es ortogonal: $\mathbf u_i \cdot \mathbf u_j = 0$ para $i \neq j$.

**Ejemplo.** $\mathbf u_1 = \langle 3, 1, 1\rangle$, $\mathbf u_2 = \langle -1, 2, 1\rangle$ y $\mathbf u_3 = \langle -\tfrac12, -2, \tfrac72\rangle$: los tres productos punto son $0$, así que es ortogonal.

> [!tip] Teorema
> Un conjunto ortogonal de vectores **no nulos** es linealmente independiente. Por lo tanto, es una base del subespacio que genera (una **base ortogonal**).

**Demostración.** Si $c_1\mathbf u_1 + \dots + c_p\mathbf u_p = \mathbf 0$, el producto punto con $\mathbf u_j$ anula todos los términos menos uno: $c_j(\mathbf u_j \cdot \mathbf u_j) = 0$. Como $\mathbf u_j \neq \mathbf 0$, $c_j = 0$. $\blacksquare$

## Coordenadas en una base ortogonal

> [!tip] Teorema
> Si $\{\mathbf u_1, \dots, \mathbf u_p\}$ es una base ortogonal de $W$ e $\mathbf y \in W$, entonces
> $$\mathbf y = c_1\mathbf u_1 + \dots + c_p\mathbf u_p \qquad\text{con}\qquad c_j = \frac{\mathbf y \cdot \mathbf u_j}{\mathbf u_j \cdot \mathbf u_j}.$$

Se obtiene con el mismo truco: el producto punto de $\mathbf y$ con $\mathbf u_j$ deja solo el término $c_j(\mathbf u_j \cdot \mathbf u_j)$.

**Ejemplo.** Con la base anterior y $\mathbf y = \langle 6, 1, -8\rangle$:
$$c_1 = \frac{18 + 1 - 8}{11} = 1, \quad c_2 = \frac{-6 + 2 - 8}{6} = -2, \quad c_3 = \frac{-3 - 2 - 28}{33/2} = -2,$$
así que $\mathbf y = \mathbf u_1 - 2\mathbf u_2 - 2\mathbf u_3$. Sin escalonar nada.

## Conjuntos ortonormales y matrices con columnas ortonormales

Un conjunto es **ortonormal** si es ortogonal y todos sus vectores son unitarios. Se obtiene normalizando cada vector de un conjunto ortogonal. En una base ortonormal, $c_j = \mathbf y \cdot \mathbf u_j$ (los denominadores valen 1). La base estándar $\{\mathbf e_1, \dots, \mathbf e_n\}$ es el ejemplo típico.

> [!tip] Teorema
> Una matriz $U$ de $m \times n$ tiene columnas ortonormales si y solo si $U^TU = I_n$.

La entrada $(i, j)$ de $U^TU$ es $\mathbf u_i \cdot \mathbf u_j$: debe ser 1 en la diagonal y 0 fuera.

> [!tip] Teorema (conservan longitudes y ángulos)
> Si $U$ tiene columnas ortonormales, para todo $\mathbf x, \mathbf y$:
> $$\|U\mathbf x\| = \|\mathbf x\|, \qquad (U\mathbf x) \cdot (U\mathbf y) = \mathbf x \cdot \mathbf y,$$
> y en particular $U\mathbf x \perp U\mathbf y$ si y solo si $\mathbf x \perp \mathbf y$.

Se demuestra con $(U\mathbf x)^T(U\mathbf y) = \mathbf x^TU^TU\mathbf y = \mathbf x^T\mathbf y$.

**Ejemplo.** $U = \begin{bmatrix} \frac{1}{\sqrt2} & \frac23 \\ \frac{1}{\sqrt2} & -\frac23 \\ 0 & \frac13 \end{bmatrix}$ cumple $U^TU = I_2$. Con $\mathbf x = \langle \sqrt2, 3\rangle$: $\|U\mathbf x\| = \|\mathbf x\| = \sqrt{2 + 9} = \sqrt{11}$, sin calcular $U\mathbf x$.

> [!tip] Definición
> Una **matriz ortogonal** es una matriz **cuadrada** con columnas ortonormales. Para ella, $U^{-1} = U^T$ (y sus filas también son ortonormales).

Las rotaciones y reflexiones del plano son matrices ortogonales. Como $\det(U^T U) = (\det U)^2 = 1$, su determinante es $\pm 1$: conservan áreas.

> [!warning] El nombre engaña
> Una "matriz ortogonal" no tiene solo columnas ortogonales: las tiene **ortonormales**, y además es cuadrada. Si las columnas son ortogonales pero no unitarias, $U^TU$ es diagonal pero no la identidad, y $U^{-1} \neq U^T$.

## Preguntas de repaso

> [!question]- ¿Por qué el teorema de independencia exige vectores no nulos?
> Porque $\mathbf 0$ es ortogonal a todo, así que un conjunto ortogonal puede contenerlo, y entonces sería LD. La demostración divide por $\mathbf u_j \cdot \mathbf u_j$, que debe ser distinto de cero.

> [!question]- Si las columnas de $A$ son ortogonales con normas $\sqrt{23}$, $\sqrt{35}$ y $\sqrt{122}$, ¿cómo se obtiene $U$ con columnas ortonormales y el mismo espacio columna?
> Dividiendo cada columna por su norma. El generado no cambia porque cada columna se escala por un número no nulo.

> [!question]- Si $U$ es de $4 \times 3$ con columnas ortonormales y $\mathbf x = \langle 4, 0, 3\rangle$, ¿cuánto vale $\|U\mathbf x\|$?
> $\|\mathbf x\| = 5$, porque $U$ conserva las normas.

> [!question]- ¿Es $UU^T = I$ si $U$ es de $4 \times 3$ con columnas ortonormales?
> No: $UU^T$ es de $4 \times 4$ con rango 3, así que no puede ser $I_4$. Es la matriz de proyección sobre $\operatorname{Col} U$ (tema siguiente). Solo para $U$ cuadrada vale $UU^T = I$.
