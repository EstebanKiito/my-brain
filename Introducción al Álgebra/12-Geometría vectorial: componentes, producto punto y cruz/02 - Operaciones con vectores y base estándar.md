---
ramo: "Introducción al Álgebra"
tema: "Geometría vectorial: componentes, producto punto y cruz"
tags:
  - intro-algebra/vectores
  - origen/complemento
prerrequisitos:
  - "[[01 - Vectores, componentes y longitud]]"
---

# Operaciones con vectores y base estándar

Las operaciones con vectores se hacen **componente a componente**: se suman, restan y escalan coordenadas correspondientes. Y todo vector se escribe como combinación de tres vectores base, $i$, $j$ y $k$, que apuntan en los ejes.

## Suma, resta y producto por escalar

Para $\mathbf a = (a_1, a_2, a_3)$ y $\mathbf b = (b_1, b_2, b_3)$:

$$
\mathbf a + \mathbf b = (a_1 + b_1,\ a_2 + b_2,\ a_3 + b_3), \qquad
\mathbf a - \mathbf b = (a_1 - b_1,\ a_2 - b_2,\ a_3 - b_3),
$$

$$
c\,\mathbf a = (c a_1,\ c a_2,\ c a_3).
$$

Estas operaciones cumplen las ocho reglas habituales: conmutatividad, asociatividad, vector nulo, opuesto, y las distributividades.

## La base estándar

Los tres vectores $i = (1, 0, 0)$, $j = (0, 1, 0)$ y $k = (0, 0, 1)$ tienen longitud $1$ y apuntan en los ejes positivos. Cualquier vector se descompone con ellos:

$$
\mathbf a = a_1 i + a_2 j + a_3 k.
$$

**Ejemplo.** Si $\mathbf a = i + 2j - 3k$ y $\mathbf b = 4i + 7k$, entonces $2\mathbf a + 3\mathbf b = (2 + 12)i + (4)j + (-6 + 21)k = 14i + 4j + 15k$.

## Vector unitario

> [!tip] Vector unitario
> Un **vector unitario** tiene longitud $1$. El unitario con la misma dirección de un $\mathbf a \neq 0$ es
> $$\mathbf u = \frac{1}{\|\mathbf a\|}\mathbf a = \frac{\mathbf a}{\|\mathbf a\|}.$$
> Se obtiene dividiendo cada componente por la longitud.

**Ejemplo.** El unitario en la dirección de $2i - j - 2k$ (longitud $3$) es $\tfrac{2}{3}i - \tfrac{1}{3}j - \tfrac{2}{3}k$.

> [!warning] Normalizar no cambia la dirección
> Dividir por $\|\mathbf a\|$ deja la dirección y el sentido, pero lleva la longitud a $1$. Sirve para aislar la "dirección pura" de un vector.

## Preguntas de repaso

> [!question]- Calcule $\mathbf a + \mathbf b$ con $\mathbf a = (4, 0, 3)$ y $\mathbf b = (-2, 1, 5)$.
> $(4 - 2,\ 0 + 1,\ 3 + 5) = (2, 1, 8)$.

> [!question]- Escriba $\mathbf a = (a_1, a_2, a_3)$ en la base estándar.
> $\mathbf a = a_1 i + a_2 j + a_3 k$, la combinación lineal de $i$, $j$ y $k$ con las componentes como coeficientes.

> [!question]- ¿Qué es un vector unitario y cómo se obtiene?
> Un vector de longitud $1$. Se obtiene dividiendo un vector no nulo por su longitud: $\mathbf a / \|\mathbf a\|$.

> [!question]- ¿Por qué $i$, $j$ y $k$ son especiales?
> Porque tienen longitud $1$, apuntan en los tres ejes y generan todo $\mathbb{R}^3$: cualquier vector es una combinación lineal de ellos.
