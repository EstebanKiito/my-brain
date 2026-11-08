---
ramo: "Introducción al Álgebra"
tema: "Geometría analítica: distancia, circunferencia y división de segmentos"
tags:
  - intro-algebra/geometria-analitica
  - origen/complemento
prerrequisitos:
  - "[[02 - Contraejemplos]]"
---

# Distancia entre puntos y de un punto a una recta

La **geometría analítica** estudia las figuras del plano con coordenadas y ecuaciones. Su herramienta básica es la **distancia**: entre dos puntos sale del teorema de Pitágoras, y de ella se deriva la distancia de un punto a una recta.

## Distancia entre dos puntos

Para $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$:

$$
d(P_1, P_2) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}.
$$

Es Pitágoras aplicado al triángulo rectángulo de catetos $|x_1 - x_2|$ y $|y_1 - y_2|$.

## Distancia de un punto a una recta

La distancia de $P$ a una recta $L$ es la longitud del segmento que va de $P$ a $L$ por la **perpendicular** (el punto $Q$ donde la perpendicular a $L$ por $P$ corta a $L$).

> [!tip] Distancia punto-recta
> Para la recta $L : ax + by + c = 0$ y el punto $P(x_1, y_1)$:
> $$d(P, L) = \frac{|ax_1 + by_1 + c|}{\sqrt{a^2 + b^2}}.$$

**Ejemplo.** Halle la distancia del punto de intersección de $x - y - 1 = 0$ y $x - 2y + 1 = 0$ a la recta $5x + 12y - 13 = 0$.

Resolviendo el sistema, el punto es $(3, 2)$. La distancia es

$$
\frac{|5\cdot 3 + 12\cdot 2 - 13|}{\sqrt{25 + 144}} = \frac{|15 + 24 - 13|}{13} = \frac{26}{13} = 2.
$$

> [!warning] Distancia a rectas paralelas
> Para hallar la distancia entre dos rectas paralelas se mide la distancia de un punto de una de ellas a la otra. No hay una fórmula directa que no pase por un punto.

## Área de un triángulo dado por coordenadas

La distancia punto-recta da la **altura**: se toma un lado como base (su largo con la fórmula de distancia entre puntos) y la altura es la distancia del vértice opuesto a la recta que contiene esa base.
$$\text{Área} = \tfrac{1}{2}\, d(A, B)\cdot d(C, L_{AB}).$$

**Ejemplo.** $A(-3, -2)$, $B(2, 1)$, $C(6, 5)$. La recta $AB$ tiene pendiente $\frac{3}{5}$: $L : 3x - 5y - 1 = 0$. Entonces $d(C, L) = \frac{|18 - 25 - 1|}{\sqrt{34}} = \frac{8}{\sqrt{34}}$, $d(A, B) = \sqrt{34}$ y el área es $\frac{1}{2} \cdot \sqrt{34} \cdot \frac{8}{\sqrt{34}} = 4$.

Si el triángulo viene dado por tres rectas, los vértices son las intersecciones de cada par (tres sistemas de $2 \times 2$).

## Lugares geométricos

Un **lugar geométrico** es el conjunto de puntos que cumplen una condición. Para hallar su ecuación: llamar $P(x, y)$ al punto, escribir la condición con las fórmulas de distancia, elevar al cuadrado para eliminar raíces y valores absolutos, y simplificar hasta reconocer la curva.

**Ejemplo.** Los puntos cuya distancia a $A(5, 0)$ es la mitad de su distancia a la recta $x = 20$: $\sqrt{(x-5)^2 + y^2} = \frac{1}{2}|x - 20|$. Al cuadrado, $4(x-5)^2 + 4y^2 = (x-20)^2$, que se reduce a $3x^2 + 4y^2 = 300$, es decir, $\frac{x^2}{100} + \frac{y^2}{75} = 1$: una elipse.

## Preguntas de repaso

> [!question]- ¿De dónde sale la fórmula de distancia entre dos puntos?
> Del teorema de Pitágoras: la diferencia en $x$ y en $y$ son los catetos, y la distancia es la hipotenusa.

> [!question]- ¿Qué significa "distancia de un punto a una recta"?
> La longitud del segmento que une el punto con la recta siguiendo la perpendicular (el camino más corto).

> [!question]- Calcule la distancia de $(1, 2)$ a la recta $3x + 4y - 6 = 0$.
> $\frac{|3\cdot 1 + 4\cdot 2 - 6|}{\sqrt{9 + 16}} = \frac{|3 + 8 - 6|}{5} = \frac{5}{5} = 1$.

> [!question]- ¿Por qué la fórmula usa valor absoluto en el numerador?
> Porque la distancia es siempre no negativa; el valor absoluto descarta el signo que saldría de la sustitución.
