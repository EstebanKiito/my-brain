---
ramo: "Introducción al Cálculo"
tema: "Valor absoluto y raíces"
tags:
  - intro-calculo/valor-absoluto
  - origen/complemento
prerrequisitos:
  - "[[02 - Propiedades del valor absoluto y desigualdad triangular]]"
---

# Vecindades e intervalos con valor absoluto

La desigualdad $|x - a| < \varepsilon$ dice que $x$ está a distancia menor que $\varepsilon$ de $a$. Es la forma estándar de expresar "$x$ está cerca de $a$", y se traduce en un intervalo centrado en $a$. Aprender a pasar de un lado a otro, entre valor absoluto e intervalo, es la destreza que más adelante sostiene la definición de convergencia de una sucesión.

## El intervalo centrado

> [!tip] Vecindad de radio $\varepsilon$
> Para $\varepsilon > 0$:
> $$|x - a| < \varepsilon \iff a - \varepsilon < x < a + \varepsilon \iff x \in (a - \varepsilon,\, a + \varepsilon).$$

Es la propiedad 4 del teorema de valor absoluto aplicada a $x - a$: $|x - a| < \varepsilon \iff -\varepsilon < x - a < \varepsilon$, y sumando $a$ a los tres miembros se obtiene el intervalo. Con $\le$ en lugar de $<$, el intervalo es cerrado: $[a - \varepsilon, a + \varepsilon]$.

El caso complementario es el **exterior**: $|x - a| > \varepsilon \iff x < a - \varepsilon$ ó $x > a + \varepsilon$, es decir $x \in (-\infty, a - \varepsilon) \cup (a + \varepsilon, \infty)$.

> [!example]- Representación en la recta (para $a = 1$ y $\varepsilon = 3$)
> - $|x - 1| < 3$ es el intervalo abierto $(-2, 4)$, centrado en $1$ y de radio $3$.
> - $|x - 1| = 3$ son los dos extremos, $x = -2$ y $x = 4$: los puntos a distancia exacta $3$ de $1$.
> - $|x - 1| > 3$ es la unión $(-\infty, -2) \cup (4, \infty)$.

## Del intervalo al valor absoluto

La traducción también funciona al revés. Un intervalo $(p, q)$ tiene centro $a = \tfrac{p + q}{2}$ y radio $\varepsilon = \tfrac{q - p}{2}$, así que $(p, q) = \{x : |x - a| < \varepsilon\}$. Por ejemplo, $(1, 5)$ equivale a $|x - 3| < 2$, y $[-4, 2]$ equivale a $|x + 1| \le 3$.

## Acotar usando una vecindad

A menudo se conoce $|x - a| < \varepsilon$ y se quiere acotar otra expresión. Se reemplaza $x$ por el intervalo y se opera sobre los extremos.

Si $|x - 2| < 1$, entonces $1 < x < 3$. Luego $3 < x + 2 < 5$, así que $|x + 2| < 5$, y $x^2 - 4 = (x - 2)(x + 2)$ cumple $|x^2 - 4| < 5\,|x - 2|$. Esta cadena (acotar un factor con la vecindad, el otro con $|x - 2|$) se repite en las demostraciones de límites.

> [!warning] El orden de los pasos
> $|x - a| < \varepsilon$ **no** es lo mismo que $x < a + \varepsilon$: falta la cota inferior $x > a - \varepsilon$. Para la versión con $>$ pasa lo contrario, se necesitan los dos lados con "ó".

## Equidistancia

$|x - a| = |x - b|$ dice que $x$ está a la misma distancia de $a$ que de $b$: es el punto medio $x = \tfrac{a + b}{2}$ (si $a \neq b$). Y $|x - a| < |x - b|$ dice que $x$ está más cerca de $a$ que de $b$, lo que describe una semirrecta limitada por el punto medio.

## Preguntas de repaso

> [!question]- ¿Cómo se escribe $|x + 3| \le 2$ como intervalo?
> Como $|x - (-3)| \le 2$, es el intervalo cerrado $[-5, -1]$, centrado en $-3$ y de radio $2$.

> [!question]- ¿Qué desigualdad con valor absoluto describe el intervalo $(-1, 7)$?
> Centro $\tfrac{-1 + 7}{2} = 3$ y radio $4$: $|x - 3| < 4$.

> [!question]- Si $|x - 2| < 1$, ¿qué cota se obtiene para $|x + 2|$?
> De $1 < x < 3$ sale $3 < x + 2 < 5$, luego $|x + 2| < 5$.

> [!question]- ¿Qué describe $|x - a| < |x - b|$ para $a < b$?
> Los $x$ más cercanos a $a$ que a $b$: la semirrecta $x < \tfrac{a + b}{2}$.
