---
ramo: "Introducción al Álgebra"
tema: "Cónicas: parábola, elipse e hipérbola"
tags:
  - intro-algebra/conicas
  - origen/complemento
prerrequisitos:
  - "[[01 - La parábola]]"
---

# La elipse

Una **elipse** es el lugar geométrico de los puntos cuya **suma** de distancias a dos puntos fijos (los **focos**) es constante. Esa suma es $2a$, y de la relación entre $a$, $b$ y $c$ salen todos sus elementos.

## Ecuación de la elipse

Con focos $(\pm c, 0)$ y suma de distancias $2a$:

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1, \qquad b^2 = a^2 - c^2.
$$

> [!tip] Elementos de la elipse
> - **Centro:** punto medio de los focos. **Eje focal:** recta que une los focos.
> - **Vértices:** intersecciones con el eje focal, a distancia $a$ del centro (eje mayor mide $2a$).
> - **Eje menor:** mide $2b$. **Focos:** a distancia $c$ del centro, con $c = \sqrt{a^2 - b^2}$.
> - **Excentricidad:** $e = c/a < 1$ (mide cuán "achatada" está).

![Elipse con focos F1 y F2 y un punto P](adjuntos/Elipse%20con%20focos%20F1%20y%20F2%20y%20un%20punto%20P.png)

> [!example]- Transcripción de la figura
> Elipse roja centrada en el origen, más ancha que alta. Sobre el eje $x$ están los focos $F_1(-c, 0)$ y $F_2(c, 0)$. Un punto $P(x, y)$ de la elipse está unido a ambos focos con segmentos azules: la suma de sus largos es la misma para todo punto de la curva.

**Ejemplo.** Para $16x^2 + 25y^2 = 400$, dividiendo por $400$ queda $\frac{x^2}{25} + \frac{y^2}{16} = 1$, con $a = 5$, $b = 4$ y $c = 3$. Los focos son $(\pm 3, 0)$, los vértices $(\pm 5, 0)$ y la excentricidad $e = 3/5$.

## Elipse desplazada y forma general

Con centro en $(h, k)$ y eje mayor horizontal (longitud $2a$):

$$
\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1.
$$

La forma general es $Ax^2 + Cy^2 + Dx + Ey + F = 0$ con $AC > 0$ y $A \neq C$, y puede ser una elipse, un punto o el conjunto vacío.

Para decidir cuál, se **completan cuadrados** hasta llegar a $A(x - h)^2 + C(y - k)^2 = K$: si $K > 0$ (con $A, C > 0$) es elipse, si $K = 0$ es el punto $(h, k)$, y si $K < 0$ no hay puntos. Por ejemplo, $x^2 + kx + 4y^2 - 16y + 21 = 0$ queda $\left(x + \frac{k}{2}\right)^2 + 4(y - 2)^2 = \frac{k^2}{4} - 5$, y es elipse solo si $k^2 > 20$.

Si el dato son los focos y el eje mayor, el centro es el punto medio de los focos, $c$ es la mitad de su distancia, $a$ la mitad del eje mayor y $b^2 = a^2 - c^2$; el eje mayor va en la dirección en que están los focos.

> [!warning] El eje mayor va donde está $a$
> En $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ el eje mayor es horizontal (porque $a > b$). Si el mayor denominador está bajo $y$, el eje mayor es vertical. Los focos van siempre sobre el eje mayor.

## Preguntas de repaso

> [!question]- ¿Qué propiedad define a una elipse?
> Que la suma de las distancias de cada punto a los dos focos es constante e igual a $2a$ (mayor que la distancia entre los focos).

> [!question]- En $\frac{x^2}{16} + \frac{y^2}{7} = 1$, halle $a$, $b$, $c$ y los focos.
> $a = 4$, $b = \sqrt7$, $c = \sqrt{16 - 7} = 3$. Focos $(\pm 3, 0)$.

> [!question]- ¿Qué mide la excentricidad de una elipse?
> Cuánto se aleja de una circunferencia: $e = c/a$, siempre entre $0$ y $1$. Si $e = 0$ (o sea $c = 0$), la elipse es una circunferencia.

> [!question]- ¿Cómo se distingue una elipse de una circunferencia en su forma general?
> En la elipse los coeficientes de $x^2$ e $y^2$ son positivos pero **distintos** ($AC > 0$, $A \neq C$); en la circunferencia son iguales.
