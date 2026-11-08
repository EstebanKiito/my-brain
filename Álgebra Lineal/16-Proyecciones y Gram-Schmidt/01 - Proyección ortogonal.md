---
ramo: "Álgebra Lineal"
tema: "Proyecciones y Gram-Schmidt"
tags:
  - algebra-lineal/ortogonalidad
  - origen/complemento
prerrequisitos:
  - "[[02 - Conjuntos ortogonales y matrices ortogonales]]"
---

# Proyección ortogonal

Dado un subespacio $W$ y un vector $\mathbf y$ que no está en él, ¿cuál es el punto de $W$ más cercano a $\mathbf y$? La respuesta es la **proyección ortogonal**: la "sombra" de $\mathbf y$ sobre $W$ cuando la luz cae perpendicular. Es la herramienta central del último bloque: con ella se miden distancias a subespacios y se resuelven aproximadamente los sistemas sin solución.

## Proyección sobre una recta

Dados $\mathbf y$ y $\mathbf u \neq \mathbf 0$, se busca escribir $\mathbf y = \hat{\mathbf y} + \mathbf z$ con $\hat{\mathbf y} = \alpha\mathbf u$ y $\mathbf z \perp \mathbf u$. La condición $(\mathbf y - \alpha\mathbf u) \cdot \mathbf u = 0$ da $\alpha = \frac{\mathbf y \cdot \mathbf u}{\mathbf u \cdot \mathbf u}$:

> [!tip] Proyección sobre $\operatorname{Gen}\{\mathbf u\}$
> $$\hat{\mathbf y} = \operatorname{proy}_{\mathbf u}\mathbf y = \frac{\mathbf y \cdot \mathbf u}{\mathbf u \cdot \mathbf u}\,\mathbf u, \qquad \mathbf z = \mathbf y - \hat{\mathbf y} \perp \mathbf u .$$

**Ejemplo.** $\mathbf y = \langle 7, 6\rangle$, $\mathbf u = \langle 4, 2\rangle$: $\frac{28 + 12}{16 + 4} = 2$, así que $\hat{\mathbf y} = \langle 8, 4\rangle$ y $\mathbf z = \langle -1, 2\rangle$. Control: $\mathbf z \cdot \mathbf u = -4 + 4 = 0$.

![Proyección sobre una recta](adjuntos/Proyecci%C3%B3n%20sobre%20una%20recta.png)

> [!example]- Transcripción de la imagen
> La recta $L = \operatorname{Gen}\{\mathbf u\}$ con $\mathbf u = \langle 4, 2\rangle$, el vector $\mathbf y = \langle 7, 6\rangle$ y su proyección $\hat{\mathbf y} = \langle 8, 4\rangle$ sobre $L$. Una línea punteada une $\mathbf y$ con $\hat{\mathbf y}$ formando un ángulo recto con $L$. El vector $\mathbf y - \hat{\mathbf y} = \langle -1, 2\rangle$ aparece trasladado al origen, perpendicular a $L$.

## Teorema de la descomposición ortogonal

> [!tip] Teorema
> Sea $W$ un subespacio de $\mathbb{R}^n$. Todo $\mathbf y \in \mathbb{R}^n$ se escribe **de manera única** como
> $$\mathbf y = \hat{\mathbf y} + \mathbf z, \qquad \hat{\mathbf y} \in W,\ \mathbf z \in W^\perp .$$
> Si $\{\mathbf u_1, \dots, \mathbf u_p\}$ es una **base ortogonal** de $W$,
> $$\hat{\mathbf y} = \operatorname{proy}_W\mathbf y = \frac{\mathbf y \cdot \mathbf u_1}{\mathbf u_1 \cdot \mathbf u_1}\mathbf u_1 + \dots + \frac{\mathbf y \cdot \mathbf u_p}{\mathbf u_p \cdot \mathbf u_p}\mathbf u_p .$$

Es decir, la proyección sobre $W$ es la **suma de las proyecciones sobre cada vector de una base ortogonal**. Si $\mathbf y \in W$, $\operatorname{proy}_W\mathbf y = \mathbf y$ (es la fórmula de coordenadas), y si $\mathbf y \in W^\perp$, $\operatorname{proy}_W\mathbf y = \mathbf 0$.

![Proyección como suma de proyecciones sobre una base ortogonal](adjuntos/Proyecci%C3%B3n%20como%20suma%20de%20proyecciones%20sobre%20una%20base%20ortogonal.png)

> [!example]- Transcripción de la imagen
> En $\mathbb{R}^3$, un plano generado por los vectores ortogonales $\mathbf u_1$ y $\mathbf u_2$, y un vector $\mathbf y$ fuera de él. Se marcan $\hat{\mathbf y}_1$ (proyección de $\mathbf y$ sobre $\mathbf u_1$) y $\hat{\mathbf y}_2$ (sobre $\mathbf u_2$); su suma es $\hat{\mathbf y} = \hat{\mathbf y}_1 + \hat{\mathbf y}_2$, el pie de la perpendicular desde $\mathbf y$ al plano.

> [!warning] La base debe ser ortogonal
> Con una base cualquiera de $W$, sumar las proyecciones sobre cada vector **no** da la proyección sobre $W$: las sombras se "pisan". Si la base no es ortogonal, primero se ortogonaliza (Gram-Schmidt).

**Ejemplo.** $\mathbf u_1 = \langle 2, 5, -1\rangle$, $\mathbf u_2 = \langle -2, 1, 1\rangle$ (ortogonales) e $\mathbf y = \langle 1, 2, 3\rangle$:
$$\hat{\mathbf y} = \frac{9}{30}\mathbf u_1 + \frac{3}{6}\mathbf u_2 = \langle -\tfrac25, 2, \tfrac15\rangle, \qquad \mathbf z = \mathbf y - \hat{\mathbf y} = \langle \tfrac75, 0, \tfrac{14}{5}\rangle .$$
Control: $\mathbf z \cdot \mathbf u_1 = \tfrac{14}{5} - \tfrac{14}{5} = 0$ y $\mathbf z \cdot \mathbf u_2 = -\tfrac{14}{5} + \tfrac{14}{5} = 0$.

## Mejor aproximación y distancia

> [!tip] Teorema de la mejor aproximación
> $\hat{\mathbf y} = \operatorname{proy}_W\mathbf y$ es el punto de $W$ más cercano a $\mathbf y$:
> $$\|\mathbf y - \hat{\mathbf y}\| < \|\mathbf y - \mathbf v\| \quad\text{para todo } \mathbf v \in W,\ \mathbf v \neq \hat{\mathbf y}.$$
> La **distancia de $\mathbf y$ a $W$** es $\|\mathbf y - \hat{\mathbf y}\| = \|\mathbf z\|$.

**Por qué.** $\mathbf y - \mathbf v = (\mathbf y - \hat{\mathbf y}) + (\hat{\mathbf y} - \mathbf v)$, donde el primer sumando está en $W^\perp$ y el segundo en $W$. Por Pitágoras, $\|\mathbf y - \mathbf v\|^2 = \|\mathbf y - \hat{\mathbf y}\|^2 + \|\hat{\mathbf y} - \mathbf v\|^2$, que es mayor salvo que $\mathbf v = \hat{\mathbf y}$.

![Proyección ortogonal sobre un subespacio](adjuntos/Proyecci%C3%B3n%20ortogonal%20sobre%20un%20subespacio.png)

> [!example]- Transcripción de la imagen
> Un plano $W$ por el origen y un vector $\mathbf y$ sobre él. La perpendicular punteada desde $\mathbf y$ cae en $\hat{\mathbf y} \in W$, con un ángulo recto. $\hat{\mathbf y}$ es el punto del plano más cercano a $\mathbf y$.

En el ejemplo anterior, la distancia de $\mathbf y$ al plano es $\|\mathbf z\| = \sqrt{\tfrac{49}{25} + \tfrac{196}{25}} = \tfrac{7\sqrt5}{5}$.

## Con base ortonormal: la matriz de proyección

> [!tip] Teorema
> Si $\{\mathbf u_1, \dots, \mathbf u_p\}$ es una base **ortonormal** de $W$ y $U = [\mathbf u_1 \cdots \mathbf u_p]$,
> $$\operatorname{proy}_W\mathbf y = (\mathbf y \cdot \mathbf u_1)\mathbf u_1 + \dots + (\mathbf y \cdot \mathbf u_p)\mathbf u_p = UU^T\mathbf y .$$

$P = UU^T$ es la **matriz de proyección** sobre $W$. Cumple $P^2 = P$ (proyectar dos veces es lo mismo que una) y $P^T = P$. Si $W \neq \mathbb{R}^n$, $P$ **no es invertible**: tiene rango $\dim W < n$ y manda todo $W^\perp$ a cero.

## Preguntas de repaso

> [!question]- Calcule la proyección de $\langle 4, 8, 1\rangle$ sobre $W = \operatorname{Gen}\{\mathbf u_1, \mathbf u_2\}$ con $\mathbf u_1 = \tfrac13\langle 2, 1, 2\rangle$ y $\mathbf u_2 = \tfrac13\langle -2, 2, 1\rangle$.
> Es una base ortonormal: $\mathbf y \cdot \mathbf u_1 = 6$ y $\mathbf y \cdot \mathbf u_2 = 3$, así que $\hat{\mathbf y} = 6\mathbf u_1 + 3\mathbf u_2 = \langle 2, 4, 5\rangle$.

> [!question]- ¿Por qué la proyección sobre un subespacio de dimensión 1 en $\mathbb{R}^3$ no es invertible?
> Porque su matriz tiene rango 1 < 3: todo el plano perpendicular va a $\mathbf 0$, y no se puede recuperar el vector original.

> [!question]- Si $\mathbf y \in W^\perp$, ¿cuánto vale $\operatorname{proy}_W\mathbf y$ y cuál es la distancia de $\mathbf y$ a $W$?
> $\operatorname{proy}_W\mathbf y = \mathbf 0$ y la distancia es $\|\mathbf y\|$: el punto de $W$ más cercano es el origen.

> [!question]- ¿Qué es el vector $\mathbf z = \mathbf y - \hat{\mathbf y}$ en términos de $W^\perp$?
> Es la proyección de $\mathbf y$ sobre $W^\perp$. La descomposición $\mathbf y = \hat{\mathbf y} + \mathbf z$ reparte $\mathbf y$ entre $W$ y su complemento.
