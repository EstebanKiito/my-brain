---
ramo: "Álgebra Lineal"
tema: "Rectas, planos e hiperplanos"
tags:
  - algebra-lineal/geometria
  - origen/complemento
prerrequisitos:
  - "[[02 - Combinaciones lineales y conjunto generado]]"
  - "[[04 - Ángulo, ortogonalidad y teorema de Pitágoras]]"
---

# Rectas en el plano y en el espacio

En el colegio una recta es $y = mx + k$. Esa forma no funciona para rectas verticales ni se generaliza al espacio, donde una sola ecuación ya no describe una recta. El álgebra vectorial ofrece dos descripciones que sí funcionan: decir hacia dónde **apunta** la recta (vector director) o decir a qué es **perpendicular** (vector normal). Saber pasar de una a otra es lo central del tema.

## Forma normal en $\mathbb{R}^2$

La ecuación general de una recta en el plano es $ax + by = c$. Si $\mathbf n = \langle a, b\rangle$ y $\mathbf x = \langle x, y\rangle$, el lado izquierdo es $\mathbf n \cdot \mathbf x$. Para una recta por el origen ($c = 0$), la ecuación $\mathbf n \cdot \mathbf x = 0$ dice "los puntos de la recta son los vectores ortogonales a $\mathbf n$". Ese $\mathbf n$ es un **vector normal**.

![Recta por el origen y su vector normal](adjuntos/Recta%20por%20el%20origen%20y%20su%20vector%20normal.png)

> [!example]- Transcripción de la imagen
> La recta $\ell$ que pasa por el origen con pendiente negativa, el vector normal $\mathbf n = \langle 2, 1\rangle$ dibujado desde el origen y un vector $\mathbf x$ sobre la recta. Entre $\mathbf n$ y $\mathbf x$ se marca un ángulo recto: todo punto de $\ell$ cumple $\mathbf n \cdot \mathbf x = 0$, es decir, $2x + y = 0$.

Si la recta no pasa por el origen, se toma un punto conocido $P$, con vector posición $\mathbf p$. Un punto $X$ está en la recta si y solo si $\overrightarrow{PX} = \mathbf x - \mathbf p$ es perpendicular a $\mathbf n$:

> [!tip] Forma normal de una recta en $\mathbb{R}^2$
> $$\mathbf n \cdot (\mathbf x - \mathbf p) = 0 \qquad\Longleftrightarrow\qquad \mathbf n \cdot \mathbf x = \mathbf n \cdot \mathbf p ,$$
> con $\mathbf n \neq \mathbf 0$ normal a la recta y $\mathbf p$ un punto de ella. Expandida es la ecuación general $ax + by = c$, con $\mathbf n = \langle a, b\rangle$.

Leer el normal es inmediato: en $2x - y = 0$, los coeficientes dan $\mathbf n = \langle 2, -1\rangle$, y la forma normal es $\langle 2, -1\rangle \cdot \langle x, y\rangle = 0$.

## Forma vectorial y paramétrica

La otra descripción parte de un punto y se mueve en una dirección. Una recta por el origen con dirección $\mathbf d \neq \mathbf 0$ es $\operatorname{Gen}\{\mathbf d\}$, es decir, $\mathbf x = t\mathbf d$. Para pasar por otro punto, basta trasladarla:

> [!tip] Forma vectorial de una recta en $\mathbb{R}^n$
> $$\mathbf x = \mathbf p + t\,\mathbf d, \qquad t \in \mathbb{R},$$
> con $\mathbf p$ un punto de la recta y $\mathbf d \neq \mathbf 0$ un **vector director**. Escrita componente a componente da las **ecuaciones paramétricas**.

En $2x - y = 0$ un director es $\mathbf d = \langle 1, 2\rangle$, porque $\mathbf n \cdot \mathbf d = 2 - 2 = 0$, y la forma vectorial es $\mathbf x = t\langle 1, 2\rangle$. En $\mathbb{R}^2$, si $\mathbf n = \langle a, b\rangle$, siempre sirve $\mathbf d = \langle -b, a\rangle$ (o $\langle b, -a\rangle$).

**Ejemplo.** La recta de $\mathbb{R}^3$ que pasa por $P(1, 2, -1)$ con dirección $\mathbf d = \langle 5, -1, 3\rangle$ es

$$
\mathbf x = \begin{bmatrix}1\\2\\-1\end{bmatrix} + t\begin{bmatrix}5\\-1\\3\end{bmatrix}
\qquad\Longleftrightarrow\qquad
\begin{cases} x = 1 + 5t \\ y = 2 - t \\ z = -1 + 3t \end{cases}
$$

Ni el punto ni el director son únicos: cualquier otro punto de la recta y cualquier múltiplo no nulo de $\mathbf d$ describen la misma recta.

> [!warning] La forma normal solo describe rectas en $\mathbb{R}^2$
> En $\mathbb{R}^3$, la ecuación $\mathbf n \cdot (\mathbf x - \mathbf p) = 0$ describe todos los puntos perpendiculares a $\mathbf n$, que forman un **plano**, no una recta. Una recta en el espacio necesita la forma vectorial o **dos** ecuaciones (la intersección de dos planos). La forma vectorial, en cambio, sirve en cualquier $\mathbb{R}^n$.

## Rectas por dos puntos y rectas paralelas

Por dos puntos distintos $P$ y $Q$ pasa una única recta, con director $\overrightarrow{PQ}$: $\mathbf x = \mathbf p + t(\mathbf q - \mathbf p)$. Con $t \in [0, 1]$ se recorre el segmento $PQ$.

> [!tip] Rectas paralelas y perpendiculares
> Dos rectas distintas son **paralelas** si y solo si sus directores son paralelos (uno es múltiplo del otro). Son **perpendiculares** si y solo si se intersectan y sus directores son ortogonales.

**Ejemplo.** La recta por $R(1, 1, 0)$ paralela a la que determinan $P(-1, 5, 0)$ y $Q(2, 1, 1)$ usa el director $\overrightarrow{PQ} = \langle 3, -4, 1\rangle$:

$$
\mathbf x = \langle 1, 1, 0\rangle + t\langle 3, -4, 1\rangle .
$$

En $\mathbb{R}^3$, dos rectas pueden tener directores no paralelos y aun así **no** intersectarse: son **alabeadas** (se cruzan a distintas alturas, como dos pasos de una autopista). Por eso en el espacio "no paralelas" no implica "se cortan". La forma de decidirlo es igualar las ecuaciones vectoriales con **parámetros distintos** y resolver el sistema.

## Preguntas de repaso

> [!question]- Dé un vector normal, un director y la forma vectorial de la recta $3x + 4y = 12$.
> Normal $\langle 3, 4\rangle$; director $\langle -4, 3\rangle$ (su producto punto con el normal es cero). Un punto es $(4, 0)$, así que $\mathbf x = \langle 4, 0\rangle + t\langle -4, 3\rangle$.

> [!question]- ¿Por qué al intersectar dos rectas dadas en forma vectorial hay que usar parámetros distintos?
> Porque cada recta recorre sus puntos a su propio ritmo: el punto común puede corresponder a $t = 3$ en una y a $s = 5$ en la otra. Usar la misma letra obliga a que ambos móviles estén ahí "al mismo tiempo" y puede hacer creer que no hay intersección cuando sí la hay.

> [!question]- ¿Describen la misma recta $\mathbf x = \langle 1, 0, 2\rangle + t\langle 2, -1, 1\rangle$ y $\mathbf x = \langle 5, -2, 4\rangle + s\langle -4, 2, -2\rangle$?
> Sí. Los directores son paralelos ($\langle -4, 2, -2\rangle = -2\langle 2, -1, 1\rangle$) y el punto $\langle 5, -2, 4\rangle$ está en la primera recta con $t = 2$. Basta un punto común para que dos rectas paralelas coincidan.

> [!question]- ¿Qué tres posiciones relativas pueden tener dos rectas distintas en $\mathbb{R}^3$ y cuál no existe en $\mathbb{R}^2$?
> Paralelas, secantes (se cortan en un punto) o alabeadas (ni paralelas ni se cortan). Las alabeadas no existen en el plano: dos rectas no paralelas de $\mathbb{R}^2$ siempre se cortan.

> [!question]- V o F: la ecuación $x + y + z = 1$ describe una recta en $\mathbb{R}^3$.
> Falso. Una ecuación lineal en $\mathbb{R}^3$ describe un plano (con normal $\langle 1, 1, 1\rangle$). Para una recta hacen falta dos ecuaciones independientes o la forma vectorial.
