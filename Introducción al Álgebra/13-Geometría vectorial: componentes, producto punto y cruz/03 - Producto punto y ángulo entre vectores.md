---
ramo: "Introducción al Álgebra"
tema: "Geometría vectorial: componentes, producto punto y cruz"
tags:
  - intro-algebra/vectores
  - origen/complemento
prerrequisitos:
  - "[[02 - Operaciones con vectores y base estándar]]"
---

# Producto punto y ángulo entre vectores

El **producto punto** combina dos vectores y devuelve un número. Su importancia está en la interpretación geométrica: ese número es proporcional al coseno del ángulo entre los vectores, así que mide cuánto "apuntan en la misma dirección".

## Producto punto

Para $\mathbf a = (a_1, a_2, a_3)$ y $\mathbf b = (b_1, b_2, b_3)$:

$$
\mathbf a \cdot \mathbf b = a_1 b_1 + a_2 b_2 + a_3 b_3.
$$

Se multiplican componentes correspondientes y se suman. El resultado es un **número real**, no un vector.

## Interpretación geométrica

> [!tip] Producto punto y ángulo
> Si $\theta$ es el ángulo entre $\mathbf a$ y $\mathbf b$ ($0 \le \theta \le \pi$):
> $$\mathbf a \cdot \mathbf b = \|\mathbf a\|\,\|\mathbf b\|\cos\theta, \qquad \cos\theta = \frac{\mathbf a \cdot \mathbf b}{\|\mathbf a\|\,\|\mathbf b\|}.$$

**Ejemplo.** Si $\|\mathbf a\| = 4$, $\|\mathbf b\| = 6$ y el ángulo entre ellos es $\pi/3$, entonces $\mathbf a \cdot \mathbf b = 4 \cdot 6 \cdot \cos(\pi/3) = 24 \cdot \tfrac12 = 12$.

## Ortogonalidad

> [!tip] Vectores ortogonales
> $\mathbf a$ y $\mathbf b$ son **ortogonales** (perpendiculares) si y solo si $\mathbf a \cdot \mathbf b = 0$. (El coseno de $\pi/2$ es $0$.)

**Ejemplo.** $(2, 6, -2) \cdot (5, -3, -4) = 10 - 18 + 8 = 0$, así que esos vectores son ortogonales.

> [!warning] El producto punto no es un vector
> $\mathbf a \cdot \mathbf b$ es un escalar. El "producto" que devuelve un vector es el producto cruz, que se ve a continuación. No mezclarlos.

## Preguntas de repaso

> [!question]- Calcule $(2, 4) \cdot (3, -1)$.
> $2 \cdot 3 + 4 \cdot (-1) = 6 - 4 = 2$.

> [!question]- ¿Cómo se halla el ángulo entre dos vectores?
> Despejando $\cos\theta = \frac{\mathbf a \cdot \mathbf b}{\|\mathbf a\|\,\|\mathbf b\|}$ y aplicando $\arccos$.

> [!question]- ¿Cuándo son ortogonales dos vectores?
> Cuando su producto punto es $0$ (el ángulo es $\pi/2$, y $\cos(\pi/2) = 0$).

> [!question]- ¿Qué significa que $\mathbf a \cdot \mathbf b > 0$?
> Que el ángulo entre ellos es agudo (coseno positivo): apuntan "más o menos" en la misma dirección.
