---
ramo: "Álgebra Lineal"
tema: "Rectas, planos e hiperplanos"
tags:
  - algebra-lineal/geometria
  - origen/complemento
prerrequisitos:
  - "[[01 - Rectas en el plano y en el espacio]]"
---

# Planos en el espacio y producto cruz

La misma ecuación que en $\mathbb{R}^2$ describía una recta, $\mathbf n \cdot (\mathbf x - \mathbf p) = 0$, en $\mathbb{R}^3$ describe un **plano**: todos los puntos $X$ tales que $\overrightarrow{PX}$ es perpendicular a $\mathbf n$. Un plano, igual que una recta, admite una descripción "por la perpendicular" (normal) y otra "por las direcciones" (vectorial). El producto cruz es la herramienta para pasar de la segunda a la primera.

## Forma normal y general

> [!tip] Plano en $\mathbb{R}^3$
> Dado un punto $\mathbf p$ y un normal $\mathbf n = \langle a, b, c\rangle \neq \mathbf 0$:
> $$\mathbf n \cdot (\mathbf x - \mathbf p) = 0 \iff \mathbf n \cdot \mathbf x = \mathbf n \cdot \mathbf p \iff ax + by + cz = d, \quad d = \mathbf n \cdot \mathbf p .$$
> Los coeficientes de la ecuación general son las componentes de un normal.

![Plano determinado por un punto y un vector normal](adjuntos/Plano%20determinado%20por%20un%20punto%20y%20un%20vector%20normal.png)

> [!example]- Transcripción de la imagen
> Un plano $\mathscr P$ con un punto $P$ marcado. Desde $P$ sale hacia arriba el normal $\mathbf n$ y, dentro del plano, el vector $\mathbf x - \mathbf p$ que va de $P$ a otro punto $X$ del plano. Entre ambos se marca un ángulo recto: es la condición $\mathbf n \cdot (\mathbf x - \mathbf p) = 0$.

**Ejemplo.** El plano por $P(6, 0, 1)$ con normal $\mathbf n = \langle 1, 2, 3\rangle$ tiene forma normal $\langle 1, 2, 3\rangle \cdot (\mathbf x - \langle 6, 0, 1\rangle) = 0$ y forma general $x + 2y + 3z = 9$, porque $\mathbf n \cdot \mathbf p = 6 + 0 + 3 = 9$.

El valor de $d$ indica si el plano pasa por el origen: lo hace si y solo si $d = 0$.

## Forma vectorial y paramétrica

Un plano por el origen es el generado por dos vectores no paralelos. Trasladándolo a un punto $\mathbf p$:

> [!tip] Forma vectorial del plano
> $$\mathbf x = \mathbf p + s\,\mathbf u + t\,\mathbf v, \qquad s, t \in \mathbb{R},$$
> con $\mathbf u, \mathbf v$ **directores no paralelos** contenidos en el plano. Componente a componente son las ecuaciones paramétricas.

![Forma vectorial del plano](adjuntos/Forma%20vectorial%20del%20plano.png)

> [!example]- Transcripción de la imagen
> Un plano con un punto $P$ (vector posición $\mathbf p$ desde el origen $O$) y dos directores $\mathbf u$ y $\mathbf v$ que salen de $P$. Para llegar a un punto cualquiera $X$ del plano se avanza $s\mathbf u$ en una dirección y $t\mathbf v$ en la otra: $\mathbf x - \mathbf p = s\mathbf u + t\mathbf v$. Desde el origen, $\mathbf x = \mathbf p + s\mathbf u + t\mathbf v$.

**Ejemplo.** En el plano $x + 2y + 3z = 9$ están, además de $P(6, 0, 1)$, los puntos $(9, 0, 0)$ y $(1, 1, 2)$. Restando $P$ se obtienen los directores $\mathbf u = \langle 3, 0, -1\rangle$ y $\mathbf v = \langle -5, 1, 1\rangle$, que no son paralelos. Entonces

$$
\mathbf x = \langle 6, 0, 1\rangle + s\langle 3, 0, -1\rangle + t\langle -5, 1, 1\rangle .
$$

Comprobación: $\mathbf n \cdot \mathbf u = 3 - 3 = 0$ y $\mathbf n \cdot \mathbf v = -5 + 2 + 3 = 0$.

> [!warning] Directores paralelos no generan un plano
> Si $\mathbf u$ y $\mathbf v$ son paralelos, $\mathbf p + s\mathbf u + t\mathbf v$ es solo una recta. Al construir un plano a partir de tres puntos, hay que verificar que no sean colineales.

## Producto cruz

Para pasar de la forma vectorial a la general se necesita un vector ortogonal a $\mathbf u$ y a $\mathbf v$ a la vez. En $\mathbb{R}^3$ hay una fórmula directa:

> [!tip] Producto cruz (solo en $\mathbb{R}^3$)
> $$\mathbf u \times \mathbf v = \langle u_2v_3 - u_3v_2,\ u_3v_1 - u_1v_3,\ u_1v_2 - u_2v_1\rangle .$$
> Es ortogonal a $\mathbf u$ y a $\mathbf v$, su norma $\|\mathbf u \times \mathbf v\| = \|\mathbf u\|\|\mathbf v\|\sin\theta$ es el área del paralelogramo que forman, y vale $\mathbf 0$ si y solo si $\mathbf u$ y $\mathbf v$ son paralelos.

Otras propiedades: $\mathbf v \times \mathbf u = -(\mathbf u \times \mathbf v)$ (no es conmutativo) y es distributivo respecto de la suma. El área de un triángulo $PQR$ es la mitad del paralelogramo: $\tfrac12\|\overrightarrow{PQ} \times \overrightarrow{PR}\|$.

**Ejemplo (de vectorial a general).** El plano $\mathbf x = t\langle 1, 2, -1\rangle + s\langle 1, 1, 0\rangle$ pasa por el origen. Su normal es

$$
\langle 1, 2, -1\rangle \times \langle 1, 1, 0\rangle = \langle 2\cdot0 - (-1)\cdot1,\ (-1)\cdot1 - 1\cdot0,\ 1\cdot1 - 2\cdot1\rangle = \langle 1, -1, -1\rangle ,
$$

así que su ecuación es $x - y - z = 0$.

Sin producto cruz se llega a lo mismo planteando $\mathbf n \cdot \mathbf u = 0$ y $\mathbf n \cdot \mathbf v = 0$ como un sistema de dos ecuaciones con tres incógnitas y eligiendo una solución no nula.

## Preguntas de repaso

> [!question]- Encuentre la ecuación general del plano que pasa por $(1, 1, 1)$, $(-1, 2, 3)$ y $(0, 1, 3)$.
> Directores $\langle -2, 1, 2\rangle$ y $\langle -1, 0, 2\rangle$. Su producto cruz es $\langle 2, 2, 1\rangle$, y con el punto $(1, 1, 1)$ se obtiene $2x + 2y + z = 5$.

> [!question]- ¿Por qué la forma vectorial de un plano necesita dos directores y la de una recta solo uno?
> Cada parámetro libre agrega una dirección de movimiento. Con uno se recorre una recta, con dos no paralelos se cubre una superficie plana. Es el mismo conteo que en $\operatorname{Gen}$: un vector genera una recta y dos no paralelos, un plano.

> [!question]- V o F: $\mathbf u \times \mathbf v = \mathbf v \times \mathbf u$.
> Falso. El producto cruz es anticonmutativo: $\mathbf v \times \mathbf u = -(\mathbf u \times \mathbf v)$. Ambos son normales al mismo plano, pero apuntan en sentidos opuestos.

> [!question]- ¿Cómo sabe, solo mirando la ecuación general, si un plano pasa por el origen y cuál es un normal?
> Pasa por el origen si y solo si el término independiente $d$ es cero. Los coeficientes de $x$, $y$ y $z$ forman un normal.

> [!question]- Calcule el área del triángulo de vértices $P(-1, 3, 1)$, $Q(0, 5, 2)$ y $R(4, 3, -1)$.
> $\overrightarrow{PQ} \times \overrightarrow{PR} = \langle 1, 2, 1\rangle \times \langle 5, 0, -2\rangle = \langle -4, 7, -10\rangle$, de norma $\sqrt{165}$. El área es $\frac{\sqrt{165}}{2}$.
