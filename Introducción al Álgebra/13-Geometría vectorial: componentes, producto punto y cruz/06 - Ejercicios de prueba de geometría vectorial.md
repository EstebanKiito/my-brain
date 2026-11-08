---
ramo: "Introducción al Álgebra"
tema: "Geometría vectorial: componentes, producto punto y cruz"
tags:
  - intro-algebra/vectores
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Operaciones con vectores y base estándar]]"
  - "[[03 - Producto punto y ángulo entre vectores]]"
  - "[[04 - Producto cruz, paralelismo y área]]"
---

# Ejercicios de prueba de geometría vectorial

Preguntas de interrogaciones y exámenes anteriores. El producto punto da ángulos y perpendicularidad; el producto cruz da vectores normales y áreas; y las combinaciones lineales con coeficientes desconocidos resuelven los problemas de razones dentro de un triángulo.

## Ejercicios

### 1. Razón en la que se cortan dos segmentos
En el triángulo $ABC$, $D$ está en $BC$ con $BD : DC = 2 : 3$, $E$ está en $AC$ con $AE : EC = 1 : 2$, y $P$ es la intersección de $AD$ y $BE$. Determine $AP : PD$.

![Triángulo ABC con las cevianas AD y BE](adjuntos/Tri%C3%A1ngulo%20ABC%20con%20las%20cevianas%20AD%20y%20BE.png)

> [!example]- Transcripción de la figura
> Triángulo $ABC$ con $A$ abajo a la izquierda, $B$ abajo a la derecha y $C$ arriba. $D$ está sobre $BC$, más cerca de $B$; $E$ está sobre $AC$, más cerca de $A$. Los segmentos $AD$ y $BE$ se cortan en $P$.

> [!example]- Solución
> Con origen en $A$ y $\mathbf b$, $\mathbf c$ las posiciones de $B$ y $C$: $\mathbf d = \frac{3}{5}\mathbf b + \frac{2}{5}\mathbf c$ y $\mathbf e = \frac{1}{3}\mathbf c$. El punto $P$ está en $AD$, así que $\mathbf p = \lambda\mathbf d$, y en $BE$, así que $\mathbf p = \mu\mathbf b + (1 - \mu)\mathbf e$. Igualando:
> $$\left(\tfrac{3}{5}\lambda - \mu\right)\mathbf b + \left(\tfrac{2}{5}\lambda - \tfrac{1 - \mu}{3}\right)\mathbf c = \mathbf 0.$$
> Como $\mathbf b$ y $\mathbf c$ no son paralelos, ambos coeficientes son $0$: $\mu = \frac{3}{5}\lambda$ y $\frac{2}{5}\lambda + \frac{1}{5}\lambda = \frac{1}{3}$, así que $\lambda = \frac{5}{9}$ y $\mu = \frac{1}{3}$. Entonces $AP = \frac{5}{9}AD$ y $AP : PD = 5 : 4$.

### 2. Perpendicularidad y un ángulo
Sean $A = (0, 0, 0)$, $B = \left(\frac{1}{\sqrt 2}, \frac{1}{\sqrt 2}, \sqrt 2\right)$ y $C = (s, t, 0)$. Determine $s, t$ para que $AB \perp AC$ y $|AC| = 1$, y calcule $\cos\gamma$, con $\gamma$ el ángulo en $C$.

> [!example]- Solución
> $\overrightarrow{AB} \cdot \overrightarrow{AC} = \frac{s + t}{\sqrt 2} = 0$ da $t = -s$; y $s^2 + t^2 = 1$ da $s = \pm\frac{1}{\sqrt 2}$. Hay dos puntos: $C = \left(\frac{1}{\sqrt 2}, -\frac{1}{\sqrt 2}, 0\right)$ y $C = \left(-\frac{1}{\sqrt 2}, \frac{1}{\sqrt 2}, 0\right)$.
> Para el primero, $\overrightarrow{CA} = \left(-\frac{1}{\sqrt 2}, \frac{1}{\sqrt 2}, 0\right)$ y $\overrightarrow{CB} = \left(0, \sqrt 2, \sqrt 2\right)$, con producto punto $1$ y normas $1$ y $2$: $\cos\gamma = \frac{1}{2}$. El otro punto da lo mismo por simetría ($\gamma = 60^\circ$ en ambos).

### 3. El ángulo en un vértice
Para $A = (1, 3, 5)$, $B = (2, -3, 6)$ y $C = (4, 5, -3)$, determine el ángulo en $C$.

> [!example]- Solución
> $\mathbf u = \overrightarrow{CA} = (-3, -2, 8)$ y $\mathbf v = \overrightarrow{CB} = (-2, -8, 9)$. Entonces $\mathbf u \cdot \mathbf v = 6 + 16 + 72 = 94$, $\|\mathbf u\| = \sqrt{77}$ y $\|\mathbf v\| = \sqrt{149}$, así que $\theta = \arccos\frac{94}{\sqrt{77}\sqrt{149}} \approx 28{,}6^\circ$. Ojo: los dos vectores deben **salir** de $C$.

### 4. Normal unitaria a un triángulo
Encuentre un vector unitario perpendicular al triángulo con vértices $A = (1, 2, 3)$, $B = (-3, -2, 5)$ y $C = (1, 4, 1)$.

> [!example]- Solución
> $\overrightarrow{AB} = (-4, -4, 2)$ y $\overrightarrow{AC} = (0, 2, -2)$. Su producto cruz es $\mathbf w = \big((-4)(-2) - 2 \cdot 2,\ 2 \cdot 0 - (-4)(-2),\ (-4) \cdot 2 - (-4) \cdot 0\big) = (4, -8, -8)$, con $\|\mathbf w\| = 12$. Unitario: $\left(\frac{1}{3}, -\frac{2}{3}, -\frac{2}{3}\right)$ (o su opuesto).

### 5. Completar un paralelogramo
Dados $P = (0, 1, 0)$, $Q = (1, 2, -1)$ y $R = (-2, 1, 0)$, determine un punto $S$ tal que los cuatro formen un paralelogramo y calcule su área.

> [!example]- Solución
> Hay tres elecciones según qué par de puntos sea diagonal. Con $\overrightarrow{PQ} = \overrightarrow{RS}$: $S = R + (Q - P) = (-1, 2, -1)$. Las otras son $S = P + R - Q = (-3, 0, 1)$ (vértices en el orden $P, Q, R, S$) y $S = P + Q - R = (3, 2, -1)$. En todos los casos el área es el doble de la del triángulo $PQR$:
> $$\left\|\overrightarrow{PQ} \times \overrightarrow{PR}\right\| = \|(1, 1, -1) \times (-2, 0, 0)\| = \|(0, 2, 2)\| = 2\sqrt 2.$$

### 6. Cancelar en el producto cruz
Sea $\mathbf a \neq \mathbf 0$. Pruebe que si $\mathbf a \times \mathbf b = \mathbf a \times \mathbf c$, entonces $\mathbf a$ y $\mathbf b - \mathbf c$ son paralelos; y que si además $\mathbf a \cdot \mathbf b = \mathbf a \cdot \mathbf c$, entonces $\mathbf b = \mathbf c$.

> [!example]- Solución
> $\mathbf 0 = \mathbf a \times \mathbf b - \mathbf a \times \mathbf c = \mathbf a \times (\mathbf b - \mathbf c)$, y el producto cruz es nulo exactamente cuando los vectores son paralelos: $\mathbf b - \mathbf c = \lambda\mathbf a$. Si además $\mathbf a \cdot (\mathbf b - \mathbf c) = 0$, entonces $\lambda\|\mathbf a\|^2 = 0$, y como $\mathbf a \neq \mathbf 0$, $\lambda = 0$: $\mathbf b = \mathbf c$.

## Preguntas de repaso

> [!question]- ¿Por qué no se puede "cancelar" $\mathbf a$ en $\mathbf a \times \mathbf b = \mathbf a \times \mathbf c$?
> Porque solo dice que $\mathbf b - \mathbf c$ es paralelo a $\mathbf a$, no que sea cero; hace falta un dato más, como el del producto punto en el ejercicio 6.

> [!question]- ¿Qué da la norma del producto cruz de dos lados de un triángulo?
> El área del paralelogramo que generan; la del triángulo es la mitad.

> [!question]- En el ejercicio 1, ¿qué propiedad permite pasar de una ecuación vectorial a dos escalares?
> Que $\mathbf b$ y $\mathbf c$ no son paralelos: una combinación de ellos es nula solo si ambos coeficientes lo son.
