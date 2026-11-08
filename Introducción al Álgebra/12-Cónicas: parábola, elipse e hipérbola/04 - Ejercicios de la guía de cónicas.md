---
ramo: "Introducción al Álgebra"
tema: "Cónicas: parábola, elipse e hipérbola"
tags:
  - intro-algebra/conicas
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[01 - La parábola]]"
  - "[[02 - La elipse]]"
  - "[[03 - La hipérbola]]"
---

# Ejercicios de la guía de cónicas

Preguntas de la guía y de las clases sobre parábolas, elipses e hipérbolas. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Parábola por su directriz
Halle la ecuación de la parábola con vértice en el origen y directriz $y - 5 = 0$.

> [!example]- Solución
> La directriz $y = 5$ está arriba del vértice, así que la parábola abre hacia abajo con $p = -5$. La ecuación es $x^2 = 4py = -20y$.

### 2. Parábola por un punto
Una parábola con vértice en el origen y eje sobre el eje $X$ pasa por $(-2, 4)$. Halle su ecuación, foco, directriz y lado recto.

> [!example]- Solución
> Como pasa por $(-2, 4)$, es $y^2 = 4px$ con $16 = 4p(-2)$, o sea $p = -2$. La ecuación es $y^2 = -8x$, el foco $(-2, 0)$, la directriz $x = 2$ y el lado recto $|4p| = 8$.

### 3. Elementos de una elipse
Determine focos, vértices y excentricidad de $16x^2 + 25y^2 = 400$.

> [!example]- Solución
> Dividiendo por $400$: $\frac{x^2}{25} + \frac{y^2}{16} = 1$, con $a = 5$, $b = 4$ y $c = \sqrt{25 - 16} = 3$. Focos $(\pm 3, 0)$, vértices $(\pm 5, 0)$ y excentricidad $e = 3/5$.

### 4. Elipse por focos y vértices
Halle la ecuación de la elipse con vértices $(\pm 4, 0)$ y focos $(\pm 3, 0)$.

> [!example]- Solución
> $a = 4$ y $c = 3$, así que $b^2 = 16 - 9 = 7$. La ecuación es $\frac{x^2}{16} + \frac{y^2}{7} = 1$.

### 5. Elementos de una hipérbola
Determine vértices, focos y asíntotas de $9x^2 - 16y^2 = 144$.

> [!example]- Solución
> Dividiendo por $144$: $\frac{x^2}{16} - \frac{y^2}{9} = 1$, con $a = 4$, $b = 3$ y $c = 5$. Vértices $(\pm 4, 0)$, focos $(\pm 5, 0)$ y asíntotas $y = \pm \tfrac34 x$.

## Preguntas de repaso

> [!question]- ¿Qué dato distingue "abre a la derecha" de "abre hacia arriba" en una parábola?
> Dónde está el cuadrado: $y^2 = 4px$ abre a la derecha/izquierda (eje horizontal); $x^2 = 4py$ abre arriba/abajo (eje vertical).

> [!question]- En una elipse, ¿qué relación hay entre $a$, $b$ y $c$?
> $b^2 = a^2 - c^2$: el semieje mayor $a$ es la hipotenusa del triángulo con catetos $b$ (semieje menor) y $c$ (semidistancia focal).

> [!question]- ¿Cómo se hallan las asíntotas de una hipérbola?
> Igualando a cero la parte izquierda de la ecuación: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 0$ da $y = \pm \frac{b}{a}x$.
