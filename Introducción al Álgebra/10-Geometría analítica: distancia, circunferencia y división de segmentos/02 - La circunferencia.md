---
ramo: "Introducción al Álgebra"
tema: "Geometría analítica: distancia, circunferencia y división de segmentos"
tags:
  - intro-algebra/geometria-analitica
  - origen/complemento
prerrequisitos:
  - "[[01 - Distancia entre puntos y de un punto a una recta]]"
---

# La circunferencia

Una **circunferencia** es el lugar geométrico de los puntos que están a una misma distancia de un punto fijo (el centro). Esa condición de distancia constante se traduce directamente en una ecuación.

## Ecuación de la circunferencia

Si el centro es $C(h, k)$ y el radio es $r$, un punto $P(x, y)$ está en la circunferencia cuando $d(C, P) = r$:

$$
(x - h)^2 + (y - k)^2 = r^2.
$$

![Circunferencia de centro C y radio r](adjuntos/circunferencia%20de%20centro%20C%20y%20radio%20r.png)

> [!example]- Transcripción de la imagen
> Una circunferencia con centro $C(h, k)$ marcado en su interior. Un radio $r$ (en rojo) une el centro con un punto $P(x, y)$ de la circunferencia. Todos los puntos de la curva están a distancia $r$ del centro.

**Ejemplo.** La circunferencia con diámetro de extremos $A(-4, 6)$ y $B(2, 0)$ tiene centro en el punto medio $(-1, 3)$ y radio la mitad de $d(A,B) = \sqrt{72} = 6\sqrt2$, es decir $r = 3\sqrt2$. Su ecuación es $(x + 1)^2 + (y - 3)^2 = 18$.

## Forma general

Desarrollando, toda circunferencia se escribe en **forma general**

$$
x^2 + y^2 + Dx + Ey + F = 0.
$$

Completando cuadrados:

$$
\left(x + \tfrac{D}{2}\right)^2 + \left(y + \tfrac{E}{2}\right)^2 = \frac{D^2 + E^2 - 4F}{4}.
$$

> [!tip] Qué es la forma general
> El centro es $(-\tfrac{D}{2}, -\tfrac{E}{2})$ y el radio $\sqrt{D^2 + E^2 - 4F}/2$. Según el signo de $D^2 + E^2 - 4F$: positivo → circunferencia; cero → un punto; negativo → conjunto vacío.

## Preguntas de repaso

> [!question]- ¿Qué expresa la ecuación $(x-h)^2 + (y-k)^2 = r^2$?
> Que todo punto $(x,y)$ de la circunferencia está a distancia $r$ del centro $(h,k)$. Es la condición de distancia constante elevada al cuadrado.

> [!question]- ¿Cómo se pasa de la forma general al centro y al radio?
> Completando cuadrados en $x$ e $y$. El centro es $(-D/2, -E/2)$ y el radio $\sqrt{D^2 + E^2 - 4F}/2$.

> [!question]- ¿Qué representa $x^2 + y^2 + 6x - 2y + 10 = 0$?
> Completando: $(x+3)^2 + (y-1)^2 = -10 + 9 + 1 = 0$, un solo punto $(-3, 1)$ (radio cero).

> [!question]- ¿Cuándo la forma general no representa una circunferencia?
> Cuando $D^2 + E^2 - 4F \le 0$: si es cero, es un punto; si es negativo, no hay puntos (conjunto vacío).
