---
ramo: "Introducción al Álgebra"
tema: "Geometría analítica: distancia, circunferencia y división de segmentos"
tags:
  - intro-algebra/geometria-analitica
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[01 - Distancia entre puntos y de un punto a una recta]]"
  - "[[03 - Tangentes a una circunferencia]]"
---

# Ejercicios de prueba de geometría analítica

Preguntas de interrogaciones anteriores. Todo se reduce a unas pocas fórmulas (distancia entre puntos, distancia punto-recta, punto medio, pendientes perpendiculares) usadas en orden; las pautas puntúan cada paso intermedio, así que conviene dejar escrita cada recta y cada distancia antes de combinarlas.

## Ejercicios

### 1. Altura y área de un triángulo
Los vértices de un triángulo son $A(-3, -2)$, $B(2, 1)$ y $C(6, 5)$. (a) Encuentre la longitud de la altura desde $C$ al lado $AB$. (b) Calcule el área.

> [!example]- Solución
> (a) Pendiente de $AB$: $\frac{1 - (-2)}{2 - (-3)} = \frac{3}{5}$; recta $y - 1 = \frac{3}{5}(x - 2)$, o sea $L : 3x - 5y - 1 = 0$. Altura: $d(C, L) = \frac{|3 \cdot 6 - 5 \cdot 5 - 1|}{\sqrt{9 + 25}} = \frac{8}{\sqrt{34}}$.
> (b) $AB = \sqrt{5^2 + 3^2} = \sqrt{34}$, así que el área es $\frac{1}{2} \cdot \sqrt{34} \cdot \frac{8}{\sqrt{34}} = 4$.

### 2. Un triángulo definido por tres rectas
Las rectas $L_1 : x + 2y + 4 = 0$, $L_2 : x - y - 1 = 0$ y $L_3 : -x + 2y - 2 = 0$ forman el triángulo $ABC$. (a) Determine sus vértices. (b) Calcule su perímetro. (c) Calcule su área.

> [!example]- Solución
> (a) $L_1 \cap L_2$: restando, $3y + 5 = 0$, así que $A = \left(-\frac{2}{3}, -\frac{5}{3}\right)$. $L_1 \cap L_3$: sumando, $4y + 2 = 0$, así que $B = \left(-3, -\frac{1}{2}\right)$. $L_2 \cap L_3$: sumando, $y - 3 = 0$, así que $C = (4, 3)$.
> (b) $AB = \sqrt{\left(\frac{7}{3}\right)^2 + \left(\frac{7}{6}\right)^2} = \frac{7\sqrt 5}{6}$, $AC = \sqrt{\left(\frac{14}{3}\right)^2 + \left(\frac{14}{3}\right)^2} = \frac{14\sqrt 2}{3}$, $BC = \sqrt{7^2 + \left(\frac{7}{2}\right)^2} = \frac{7\sqrt 5}{2}$. Perímetro: $\frac{14}{3}\left(\sqrt 2 + \sqrt 5\right)$.
> (c) Base $AB$ (sobre $L_1$) y altura $d(C, L_1) = \frac{|4 + 6 + 4|}{\sqrt 5} = \frac{14}{\sqrt 5}$. Área: $\frac{1}{2} \cdot \frac{14}{\sqrt 5} \cdot \frac{7\sqrt 5}{6} = \frac{49}{6}$.

### 3. Circunferencia, tangente y distancia
Los extremos de un diámetro de una circunferencia son $A(2, -1)$ y $B(6, 3)$. (a) Encuentre su ecuación. (b) Encuentre la tangente en $A$. (c) ¿A qué distancia está el centro de la recta $x + y = 1$?

> [!example]- Solución
> (a) Centro en el punto medio, $C = (4, 1)$; radio $CA = \sqrt{4 + 4} = \sqrt 8$. Ecuación: $(x - 4)^2 + (y - 1)^2 = 8$.
> (b) La tangente es perpendicular al radio $CA$, de pendiente $\frac{-1 - 1}{2 - 4} = 1$; así que tiene pendiente $-1$ y pasa por $A$: $y + 1 = -(x - 2)$, es decir, $x + y = 1$.
> (c) Es la tangente de (b), así que la distancia es el radio, $\sqrt 8 = 2\sqrt 2$. (Con la fórmula: $\frac{|4 + 1 - 1|}{\sqrt 2} = 2\sqrt 2$.)

### 4. Un lugar geométrico
Encuentre la trayectoria de un punto $P(x, y)$ cuya distancia a $A(5, 0)$ es la mitad de su distancia a la recta $x = 20$, e identifique la cónica.

> [!example]- Solución
> $\sqrt{(x-5)^2 + y^2} = \frac{1}{2}|x - 20|$. Al cuadrado y multiplicando por $4$: $4x^2 - 40x + 100 + 4y^2 = x^2 - 40x + 400$, o sea $3x^2 + 4y^2 = 300$, es decir, $\frac{x^2}{100} + \frac{y^2}{75} = 1$. Es una elipse (los puntos cuya distancia a un foco es una fracción fija, menor que $1$, de su distancia a una recta).

### 5. Tres puntos colineales
Sean $O = (-1, 0)$, $A = (1, 0)$ y $B = (3, 0)$, y las semicircunferencias superiores de diámetros $OA$ y $OB$. Desde el punto medio $M$ de $AB$ se levanta la perpendicular, que corta a la circunferencia mayor en $R$; desde $M$ se traza la tangente a la circunferencia menor, con punto de tangencia $P$. (a) Halle $R$. (b) Halle $P$. (c) Pruebe que $O$, $P$ y $R$ son colineales.

> [!example]- Solución
> (a) $M = (2, 0)$. La circunferencia de diámetro $OB$ tiene centro $(1, 0)$ y radio $2$: $(x-1)^2 + y^2 = 4$. Con $x = 2$, $y^2 = 3$, así que $R = (2, \sqrt 3)$.
> (b) La de diámetro $OA$ es $x^2 + y^2 = 1$. Su centro es el origen, y la tangente en un punto $P = (p, q)$ de ella es $px + qy = 1$ (la recta por $P$ perpendicular al radio, cuya dirección es $(p, q)$). Como pasa por $M$: $2p = 1$, $p = \frac{1}{2}$, y entonces $q = \frac{\sqrt 3}{2}$.
> (c) Pendiente de $O$ a $P$: $\frac{\sqrt 3/2}{1/2 + 1} = \frac{\sqrt 3}{3}$. Pendiente de $O$ a $R$: $\frac{\sqrt 3}{2 + 1} = \frac{\sqrt 3}{3}$. Son iguales, así que los tres puntos están en una misma recta.

## Preguntas de repaso

> [!question]- ¿Por qué la tangente en $A$ es perpendicular al radio $CA$?
> Es la propiedad que define a la tangente de una circunferencia: toca en un solo punto, y ese punto es el más cercano al centro sobre la recta, así que el radio cae perpendicular.

> [!question]- Para el área de un triángulo dado por tres rectas, ¿qué base conviene elegir?
> Un lado que esté sobre una de las rectas dadas: así la altura es directamente la distancia del vértice opuesto a esa recta, sin calcular otra ecuación.

> [!question]- ¿Cómo se prueba que tres puntos son colineales?
> Mostrando que las pendientes de dos de los segmentos que comparten un punto son iguales (o que uno de los puntos satisface la ecuación de la recta por los otros dos).
