---
ramo: "Introducción al Álgebra"
tema: "Geometría vectorial: componentes, producto punto y cruz"
tags:
  - intro-algebra/vectores
  - origen/complemento
prerrequisitos:
  - "[[03 - Producto punto y ángulo entre vectores]]"
---

# Producto cruz, paralelismo y área

El **producto cruz** solo existe en $\mathbb{R}^3$ y devuelve un **vector** perpendicular a los dos dados. Su magnitud mide el área del paralelogramo que forman, y se anula exactamente cuando los vectores son paralelos.

## Producto cruz

Para $\mathbf a = (a_1, a_2, a_3)$ y $\mathbf b = (b_1, b_2, b_3)$:

$$
\mathbf a \times \mathbf b = (a_2 b_3 - a_3 b_2,\ a_3 b_1 - a_1 b_3,\ a_1 b_2 - a_2 b_1).
$$

Se recuerda como el determinante simbólico

$$
\mathbf a \times \mathbf b =
\begin{vmatrix}
i & j & k \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3
\end{vmatrix}.
$$

**Ejemplo.** $(1, 3, 4) \times (2, 7, -5) = (3(-5) - 4(7),\ 4(2) - 1(-5),\ 1(7) - 3(2)) = (-43, 13, 1)$.

## Propiedades geométricas

> [!tip] Producto cruz: dirección y magnitud
> - $\mathbf a \times \mathbf b$ es **ortogonal** a $\mathbf a$ y a $\mathbf b$ (su dirección la da la regla de la mano derecha).
> - $\|\mathbf a \times \mathbf b\| = \|\mathbf a\|\,\|\mathbf b\|\sin\theta$.
> - $\mathbf a$ y $\mathbf b$ son **paralelos** si y solo si $\mathbf a \times \mathbf b = 0$.

El **área del paralelogramo** determinado por $\mathbf a$ y $\mathbf b$ es $\|\mathbf a \times \mathbf b\|$, y la del triángulo es su mitad.

> [!warning] El cruz es anticonmutativo
> $\mathbf a \times \mathbf b = -(\mathbf b \times \mathbf a)$: invertir el orden invierte la dirección. Además, $\mathbf a \times \mathbf a = 0$ siempre.

## Preguntas de repaso

> [!question]- ¿Qué devuelve el producto cruz: un número o un vector?
> Un **vector** (a diferencia del producto punto, que devuelve un número). Es perpendicular a ambos operandos.

> [!question]- ¿Cuándo es $\mathbf a \times \mathbf b = 0$?
> Cuando $\mathbf a$ y $\mathbf b$ son paralelos (o alguno es nulo), porque $\sin\theta = 0$.

> [!question]- ¿Cómo se calcula el área del paralelogramo entre $\mathbf a$ y $\mathbf b$?
> Como $\|\mathbf a \times \mathbf b\| = \|\mathbf a\|\,\|\mathbf b\|\sin\theta$. El triángulo con esos dos vectores tiene área la mitad.

> [!question]- ¿Por qué $\mathbf a \times \mathbf b$ es perpendicular a $\mathbf a$?
> Porque $(\mathbf a \times \mathbf b) \cdot \mathbf a = 0$ (se anula el producto punto). Es la forma algebraica de decir "perpendicular".
