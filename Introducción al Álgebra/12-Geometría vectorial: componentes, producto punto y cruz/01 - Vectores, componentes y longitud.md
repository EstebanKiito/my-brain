---
ramo: "Introducción al Álgebra"
tema: "Geometría vectorial: componentes, producto punto y cruz"
tags:
  - intro-algebra/vectores
  - origen/complemento
prerrequisitos:
  - "[[02 - Contraejemplos]]"
---

# Vectores, componentes y longitud

Un vector se puede describir sin dibujarlo, mediante sus **componentes**: cuánto avanza en cada eje. Esa lista de números permite calcular todo (suma, longitud, ángulos) de forma algebraica, y es la puerta para trabajar en $\mathbb{R}^3$.

## Componentes de un vector

Si el punto inicial de un vector $\mathbf a$ está en el origen, su punto terminal tiene coordenadas $(a_1, a_2)$ o $(a_1, a_2, a_3)$. Esas coordenadas son las **componentes** de $\mathbf a$, y se escribe $\mathbf a = (a_1, a_2, a_3)$.

> [!tip] Vector entre dos puntos
> El vector con representación $\overrightarrow{AB}$, con $A(x_1, y_1, z_1)$ y $B(x_2, y_2, z_2)$, es
> $$\mathbf a = (x_2 - x_1,\ y_2 - y_1,\ z_2 - z_1),$$
> es decir, "coordenadas de la punta menos las de la cola".

**Ejemplo.** De $A(2, -3, 4)$ a $B(-2, 1, 1)$ el vector es $(-4, 4, -3)$.

## Longitud de un vector

La **magnitud** (o longitud) de $\mathbf a$ es la longitud de cualquiera de sus representaciones:

$$
\|\mathbf a\| = \sqrt{a_1^2 + a_2^2} \quad \text{(en }\mathbb{R}^2\text{)}, \qquad
\|\mathbf a\| = \sqrt{a_1^2 + a_2^2 + a_3^2} \quad \text{(en }\mathbb{R}^3\text{)}.
$$

Es Pitágoras generalizado: la raíz de la suma de los cuadrados de las componentes.

> [!warning] Componentes vs. magnitud
> Las componentes son números con signo (pueden ser negativos); la magnitud $\|\mathbf a\|$ es siempre no negativa. No confundir el vector $(3, -4)$ con su longitud $5$.

## Preguntas de repaso

> [!question]- ¿Qué son las componentes de un vector?
> Las coordenadas de su punto terminal cuando el punto inicial está en el origen: cuánto avanza en cada eje.

> [!question]- Halle el vector de $A(2, -3, 4)$ a $B(-2, 1, 1)$.
> $\overrightarrow{AB} = (-2 - 2,\ 1 - (-3),\ 1 - 4) = (-4, 4, -3)$.

> [!question]- ¿Cuál es la longitud de $\mathbf a = (4, 0, 3)$?
> $\|\mathbf a\| = \sqrt{16 + 0 + 9} = \sqrt{25} = 5$.

> [!question]- ¿Qué relación hay entre las componentes y la longitud?
> La longitud es la raíz de la suma de los cuadrados de las componentes (Pitágoras). La componente de un eje es cuánto se avanza en esa dirección.
