---
ramo: "Introducción al Álgebra"
tema: "Cónicas: parábola, elipse e hipérbola"
tags:
  - intro-algebra/conicas
  - origen/complemento
prerrequisitos:
  - "[[02 - La circunferencia]]"
---

# La parábola

Una **parábola** es el conjunto de puntos que equidistan de un punto fijo (el **foco**) y de una recta fija (la **directriz**). Esa condición de "equidistar" es la que genera su ecuación y su forma.

## Ecuación de la parábola

Con el vértice en el origen y el eje sobre el eje $X$, si el foco es $F(p, 0)$ y la directriz es $x = -p$, un punto $P(x,y)$ está en la parábola cuando $d(P, F) = d(P, M)$ (con $M$ el pie de la perpendicular a la directriz):

$$
\sqrt{(x - p)^2 + y^2} = |x + p| \iff y^2 = 4px.
$$

![Parábola con foco y directriz](adjuntos/parabola%20con%20foco%20y%20directriz.png)

> [!example]- Transcripción de la imagen
> Una parábola (azul) con vértice $V$ en el origen. El foco $F(p, 0)$ está sobre el eje $X$ (a la derecha), y la directriz es la recta vertical punteada $x = -p$. Todo punto de la curva está a igual distancia del foco y de la directriz.

> [!tip] Parábola con vértice en el origen
> - $y^2 = 4px$: abre a la derecha si $p > 0$ (izquierda si $p < 0$). Foco $(p, 0)$, directriz $x = -p$.
> - $x^2 = 4py$: abre hacia arriba si $p > 0$ (abajo si $p < 0$). Foco $(0, p)$, directriz $y = -p$.

El **lado recto** es la cuerda focal perpendicular al eje, y su longitud es $\ell = |4p|$.

## Vértice desplazado

Con el vértice en $(h, k)$:

$$
(y - k)^2 = 4p(x - h) \quad \text{(eje paralelo al eje } X\text{)}, \qquad
(x - h)^2 = 4p(y - k) \quad \text{(eje paralelo al eje } Y\text{)}.
$$

**Ejemplo.** La parábola de vértice en el origen y directriz $y - 5 = 0$ (o sea $y = 5$) abre hacia abajo, con $p = -5$, así que $x^2 = -20y$.

> [!warning] El signo de $p$ da la abertura
> $p > 0$ abre hacia la derecha (o arriba); $p < 0$ hacia la izquierda (o abajo). El foco está a distancia $|p|$ del vértice, del lado al que abre.

## Preguntas de repaso

> [!question]- ¿Qué define a una parábola?
> Que cada punto equidista del foco $F$ y de la directriz. Esa condición $d(P,F) = d(P,M)$ es la que produce $y^2 = 4px$.

> [!question]- ¿Cuál es el foco y la directriz de $y^2 = 8x$?
> $4p = 8$, así que $p = 2$. Foco $(2, 0)$ y directriz $x = -2$; abre a la derecha.

> [!question]- ¿Qué es el lado recto de una parábola?
> La cuerda focal perpendicular al eje. Su longitud es $|4p|$.

> [!question]- ¿Cómo se reconoce una parábola de eje vertical?
> Porque la ecuación tiene el término al cuadrado en $x$: $(x-h)^2 = 4p(y-k)$. Si el cuadrado está en $y$, el eje es horizontal.
