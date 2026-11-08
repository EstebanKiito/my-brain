---
ramo: "Introducción al Álgebra"
tema: "Cónicas: parábola, elipse e hipérbola"
tags:
  - intro-algebra/conicas
  - origen/complemento
prerrequisitos:
  - "[[02 - La elipse]]"
---

# La hipérbola

Una **hipérbola** es el lugar geométrico de los puntos cuya **diferencia** (en valor absoluto) de distancias a dos focos es constante. A diferencia de la elipse, tiene dos ramas y dos **asíntotas**, rectas a las que se aproxima sin tocarlas.

## Ecuación de la hipérbola

Con focos $(\pm c, 0)$ y diferencia de distancias $2a$:

$$
\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1, \qquad c^2 = a^2 + b^2.
$$

> [!tip] Elementos de la hipérbola
> - **Vértices:** $(\pm a, 0)$, sobre el **eje transverso** (horizontal, longitud $2a$).
> - **Focos:** $(\pm c, 0)$, con $c = \sqrt{a^2 + b^2}$.
> - **Asíntotas:** las rectas $y = \pm \tfrac{b}{a}x$, a las que las ramas se aproximan.

Si el eje transverso es vertical, la ecuación es $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$, con vértices $(0, \pm a)$ y asíntotas $y = \pm \tfrac{a}{b}x$.

**Ejemplo.** Para $9x^2 - 16y^2 = 144$, dividiendo por $144$ queda $\frac{x^2}{16} - \frac{y^2}{9} = 1$, con $a = 4$, $b = 3$ y $c = 5$. Los vértices son $(\pm 4, 0)$, los focos $(\pm 5, 0)$ y las asíntotas $y = \pm \tfrac34 x$.

## Hipérbola desplazada y forma general

Con centro en $(h, k)$ y eje transverso horizontal:

$$
\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1.
$$

La forma general es $Ax^2 + Cy^2 + Dx + Ey + F = 0$ con $AC < 0$, y representa una hipérbola o dos rectas que se cortan. Cuando las asíntotas son perpendiculares, la hipérbola se llama **equilátera**.

> [!warning] Signo menos y asíntotas
> El signo "$-$" entre los términos es lo que distingue a la hipérbola de la elipse. Las asíntotas se obtienen igualando a cero la parte de la izquierda: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 0$ da $y = \pm \tfrac{b}{a}x$.

## Preguntas de repaso

> [!question]- ¿Qué distingue a la hipérbola de la elipse?
> El signo: la elipse tiene suma de términos ($+$) y $b^2 = a^2 - c^2$; la hipérbola tiene resta ($-$) y $c^2 = a^2 + b^2$. La hipérbola tiene dos ramas y asíntotas.

> [!question]- Halle las asíntotas de $\frac{x^2}{16} - \frac{y^2}{9} = 1$.
> $y = \pm \tfrac34 x$, obtenidas igualando $\frac{x^2}{16} - \frac{y^2}{9} = 0$.

> [!question]- ¿Qué es una hipérbola equilátera?
> Una hipérbola cuyas asíntotas son perpendiculares entre sí (lo que ocurre cuando $a = b$).

> [!question]- En la forma general, ¿cómo se reconoce una hipérbola?
> Porque los coeficientes de $x^2$ e $y^2$ tienen signos opuestos ($AC < 0$).
