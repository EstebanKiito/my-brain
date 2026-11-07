---
ramo: "Álgebra Lineal"
tema: "Rectas, planos e hiperplanos"
tags:
  - algebra-lineal/geometria
  - algebra-lineal/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Posición relativa, intersecciones e hiperplanos]]"
---

# Ejercicios de prueba de rectas y planos

Preguntas de interrogaciones anteriores sobre rectas, planos e hiperplanos, de menor a mayor dificultad. Casi todas combinan tres herramientas: leer normales de ecuaciones, producto cruz e igualar formas vectoriales con parámetros distintos.

## Ejercicios

### 1. Plano perpendicular a una recta
Con $A(-1, 2, 0)$, $B(3, -2, 2)$ y $C(0, 3, -1)$, encuentre la ecuación general del plano que pasa por $A$ y es perpendicular a la recta que pasa por $B$ y $C$.

> [!example]- Solución
> Si el plano es perpendicular a la recta, el director de la recta sirve como normal: $\mathbf n = \overrightarrow{BC} = \langle -3, 5, -3\rangle$. Con $d = \mathbf n \cdot A = 3 + 10 + 0 = 13$, el plano es $-3x + 5y - 3z = 13$ (o, multiplicando por $-1$, $3x - 5y + 3z = -13$).

### 2. De forma vectorial a cartesiana
Encuentre una ecuación cartesiana del plano $\{\,t\langle 1, 2, 0\rangle + s\langle 2, 1, 3\rangle + \langle 2, 1, 3\rangle : t, s \in \mathbb{R}\,\}$.

> [!example]- Solución
> Normal: $\langle 1, 2, 0\rangle \times \langle 2, 1, 3\rangle = \langle 6, -3, -3\rangle$, o más simple, $\langle 2, -1, -1\rangle$. Con el punto $(2, 1, 3)$: $d = 4 - 1 - 3 = 0$. El plano es $2x - y - z = 0$. Que pase por el origen no es casualidad: el punto base $\langle 2, 1, 3\rangle$ coincide con uno de los directores, así que $s = -1$, $t = 0$ da $\mathbf 0$.

### 3. Intersección de dos planos y de una recta con un plano
Sean $\pi_1: x + y + 2z = 1$, $\pi_2: -x + y = 2$ y $L_1$ la recta por $(0, 1, 1)$ con dirección $\langle 1, 0, 0\rangle$. (a) Encuentre la recta $L_2 = \pi_1 \cap \pi_2$. (b) Encuentre el punto $L_1 \cap \pi_1$.

> [!example]- Solución
> **(a)** Director: $\langle 1, 1, 2\rangle \times \langle -1, 1, 0\rangle = \langle -2, -2, 2\rangle$, o $\langle 1, 1, -1\rangle$. Un punto común: con $x = 0$, la segunda ecuación da $y = 2$ y la primera $2 + 2z = 1$, así que $z = -\tfrac12$. Entonces $L_2: \mathbf x = \langle 0, 2, -\tfrac12\rangle + t\langle 1, 1, -1\rangle$.
>
> **(b)** $L_1$ es $(t, 1, 1)$. En $\pi_1$: $t + 1 + 2 = 1$, así que $t = -2$ y el punto es $P_2 = (-2, 1, 1)$.

### 4. Rectas que se cortan y el plano que las contiene
$L_1: \langle 1, -1, 2\rangle + t\langle 0, 3, 1\rangle$ y $L_2: \langle 0, 2, -1\rangle + s\langle -1, 0, -4\rangle$. (a) Determine $L_1 \cap L_2$. (b) Encuentre el plano que contiene a ambas.

> [!example]- Solución
> **(a)** Igualando componentes: $1 = -s$, $-1 + 3t = 2$, $2 + t = -1 - 4s$. Las dos primeras dan $s = -1$ y $t = 1$, y la tercera se cumple ($3 = 3$). Se cortan en $(1, 2, 3)$.
>
> **(b)** Normal: $\langle 0, 3, 1\rangle \times \langle -1, 0, -4\rangle = \langle -12, -1, 3\rangle$. Con el punto $(1, 2, 3)$: $12x + y - 3z = 12 + 2 - 9 = 5$.

### 5. Rectas paralelas y el plano que las contiene
$L_1: \langle 1, -1, 2\rangle + t\langle 1, 2, -1\rangle$ y $L_2: \langle 0, 2, -1\rangle + s\langle 2, 4, -2\rangle$. (a) ¿Se intersectan? (b) Encuentre el plano que las contiene.

> [!example]- Solución
> **(a)** Los directores son paralelos ($\langle 2, 4, -2\rangle = 2\langle 1, 2, -1\rangle$), así que las rectas son paralelas o coincidentes. Para que coincidan, $\langle 0, 2, -1\rangle - \langle 1, -1, 2\rangle = \langle -1, 3, -3\rangle$ tendría que ser múltiplo de $\langle 1, 2, -1\rangle$, y no lo es ($-1 \cdot 2 \neq 3$). **No se intersectan.**
>
> **(b)** El producto cruz de los directores es $\mathbf 0$, así que no sirve. Se usa un director y el vector que une las rectas: $\langle 1, 2, -1\rangle \times \langle -1, 3, -3\rangle = \langle -3, 4, 5\rangle$. Con $(1, -1, 2)$: $3x - 4y - 5z = 3 + 4 - 10 = -3$.

### 6. Trayectorias de dos drones
El dron A parte de $(1, 2, 0)$ con dirección $\langle 1, -1, 2\rangle$ y el dron B de $(9, -6, 1)$ con dirección $\langle -1, 1, 1\rangle$. (a) Escriba sus trayectorias. (b) Muestre que se cortan y encuentre el punto. (c) Si B parte desde $(a, b, c)$ con la misma dirección, ¿cuándo **no** se cortan?

> [!example]- Solución
> **(a)** $\ell_A: (1 + t,\ 2 - t,\ 2t)$ y $\ell_B: (9 - s,\ -6 + s,\ 1 + s)$.
>
> **(b)** Igualando: $1 + t = 9 - s$, $2 - t = -6 + s$, $2t = 1 + s$. De la primera, $s = 8 - t$; en la tercera, $2t = 9 - t$, así que $t = 3$ y $s = 5$. La segunda se cumple ($-1 = -1$). El punto es $(4, -1, 6)$.
>
> **(c)** Ahora $1 + t = a - s$, $2 - t = b + s$, $2t = c + s$. Sumando las dos primeras, los parámetros se cancelan y queda $3 = a + b$. Si $a + b \neq 3$ el sistema es inconsistente. Si $a + b = 3$, las ecuaciones primera y tercera determinan $t$ y $s$ (los directores no son paralelos) y siempre hay corte. **No se cortan si y solo si $a + b \neq 3$.**

### 7. Punto de un hiperplano más cercano al origen
Sea $\mathbf n \in \mathbb{R}^n$ no nulo y $H = \{\mathbf x : \mathbf x \cdot \mathbf n = s\}$. (a) Encuentre $t$ tal que $\mathbf y = t\mathbf n \in H$. (b) Muestre que si $\mathbf x \in H$, $\mathbf z = \mathbf x - \mathbf y$ es ortogonal a $\mathbf n$ y a $\mathbf y$. (c) Demuestre que $\|\mathbf y\| \leq \|\mathbf x\|$ para todo $\mathbf x \in H$.

> [!example]- Solución
> **(a)** $t\mathbf n \cdot \mathbf n = s$, así que $t = \dfrac{s}{\|\mathbf n\|^2}$.
>
> **(b)** $\mathbf z \cdot \mathbf n = \mathbf x \cdot \mathbf n - \mathbf y \cdot \mathbf n = s - s = 0$. Como $\mathbf y = t\mathbf n$, también $\mathbf z \cdot \mathbf y = t(\mathbf z \cdot \mathbf n) = 0$.
>
> **(c)** $\mathbf x = \mathbf y + \mathbf z$ con $\mathbf y \perp \mathbf z$, así que por Pitágoras $\|\mathbf x\|^2 = \|\mathbf y\|^2 + \|\mathbf z\|^2 \geq \|\mathbf y\|^2$. Interpretación: $\mathbf y$ es el punto de $H$ más cercano al origen y la distancia es $\frac{|s|}{\|\mathbf n\|}$.

### 8. Una recta por dos puntos de un plano está en el plano
Demuestre que si $A$ y $B$ están en el plano $\Pi: \mathbf n \cdot \mathbf x = d$, toda la recta $AB$ está contenida en $\Pi$.

> [!example]- Solución
> Los puntos de la recta son $P(t) = A + t(B - A) = (1 - t)A + tB$. Entonces
> $$\mathbf n \cdot P(t) = (1 - t)(\mathbf n \cdot A) + t(\mathbf n \cdot B) = (1 - t)d + td = d$$
> para todo $t$, así que cada punto de la recta cumple la ecuación del plano.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 5 no sirve el producto cruz de los directores para el normal?
> Porque los directores son paralelos y su producto cruz es $\mathbf 0$. Hace falta una segunda dirección dentro del plano, que la da el vector entre un punto de cada recta.

> [!question]- ¿Qué paso del ejercicio 6 garantiza que el sistema de tres ecuaciones con dos incógnitas tiene solución?
> Hay que comprobar la ecuación que no se usó para despejar. Con dos ecuaciones siempre se encuentran $t$ y $s$; solo si la tercera también se cumple las rectas se cortan.

> [!question]- ¿Qué relación tiene el ejercicio 7 con la fórmula de distancia de un punto a un plano?
> Es el caso del punto $Q = \mathbf 0$: $d(\mathbf 0, H) = \frac{|\mathbf n \cdot \mathbf 0 - s|}{\|\mathbf n\|} = \frac{|s|}{\|\mathbf n\|}$, y el punto más cercano está en la dirección del normal.
