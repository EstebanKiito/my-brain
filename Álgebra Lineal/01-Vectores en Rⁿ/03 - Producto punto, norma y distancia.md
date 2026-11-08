---
ramo: "Álgebra Lineal"
tema: "Vectores en Rⁿ"
tags:
  - algebra-lineal/vectores
  - origen/complemento
prerrequisitos:
  - "[[01 - Vectores y sus operaciones]]"
---

# Producto punto, norma y distancia

La suma y el producto por escalar no permiten medir nada: no dicen cuánto mide un vector ni qué tan lejos están dos puntos. El **producto punto** agrega la geometría métrica. A partir de él se definen la longitud, la distancia, el ángulo y la perpendicularidad, en $\mathbb{R}^2$, en $\mathbb{R}^3$ y en cualquier $\mathbb{R}^n$.

## Producto punto

> [!tip] Definición
> Para $\mathbf u = \langle u_1, \dots, u_n\rangle$ y $\mathbf v = \langle v_1, \dots, v_n\rangle$,
> $$\mathbf u \cdot \mathbf v = u_1v_1 + u_2v_2 + \dots + u_nv_n .$$
> Solo está definido entre vectores del mismo $\mathbb{R}^n$, y el resultado es un **número**, no un vector.

**Ejemplo.** $\langle 1, 2, 3\rangle \cdot \langle -3, 5, 2\rangle = -3 + 10 + 6 = 13$.

Propiedades, para $\mathbf u, \mathbf v, \mathbf w \in \mathbb{R}^n$ y $c \in \mathbb{R}$:

1. **Conmutatividad:** $\mathbf u \cdot \mathbf v = \mathbf v \cdot \mathbf u$.
2. **Distributividad:** $\mathbf u \cdot (\mathbf v + \mathbf w) = \mathbf u \cdot \mathbf v + \mathbf u \cdot \mathbf w$.
3. **Escalares:** $c(\mathbf u \cdot \mathbf v) = (c\mathbf u) \cdot \mathbf v = \mathbf u \cdot (c\mathbf v)$.
4. **Positividad:** $\mathbf u \cdot \mathbf u \geq 0$, y $\mathbf u \cdot \mathbf u = 0$ si y solo si $\mathbf u = \mathbf 0$.

La cuarta sale de que $\mathbf u \cdot \mathbf u = u_1^2 + \dots + u_n^2$ es una suma de cuadrados. Con las tres primeras se expanden productos como si fueran productos de números:

$$
(\mathbf u + \mathbf v) \cdot (\mathbf u + \mathbf v) = \mathbf u \cdot \mathbf u + 2\,\mathbf u \cdot \mathbf v + \mathbf v \cdot \mathbf v .
$$

Esta identidad es la herramienta de casi todas las demostraciones del tema.

> [!warning] Lo que el producto punto no permite
> No se puede "simplificar" un vector: de $\mathbf u \cdot \mathbf v = \mathbf u \cdot \mathbf w$ **no** se concluye $\mathbf v = \mathbf w$. Solo se concluye $\mathbf u \cdot (\mathbf v - \mathbf w) = 0$, es decir, que $\mathbf v - \mathbf w$ es perpendicular a $\mathbf u$. Tampoco tiene sentido $(\mathbf u \cdot \mathbf v)\cdot\mathbf w$ como producto punto, porque $\mathbf u \cdot \mathbf v$ ya es un número.

## Norma

> [!tip] Definición
> La **norma** (longitud) de $\mathbf v \in \mathbb{R}^n$ es
> $$\|\mathbf v\| = \sqrt{\mathbf v \cdot \mathbf v} = \sqrt{v_1^2 + \dots + v_n^2}.$$

En $\mathbb{R}^2$ y $\mathbb{R}^3$ es el teorema de Pitágoras aplicado a las componentes; en $\mathbb{R}^n$ se toma como definición. Dos propiedades se usan todo el tiempo:

- $\|\mathbf v\| = 0$ si y solo si $\mathbf v = \mathbf 0$.
- $\|c\mathbf v\| = |c|\,\|\mathbf v\|$, porque $\sqrt{c^2(v_1^2 + \dots + v_n^2)} = |c|\sqrt{v_1^2 + \dots + v_n^2}$. El valor absoluto importa: $\|-3\mathbf v\| = 3\|\mathbf v\|$.

Una regla práctica: trabajar con $\|\mathbf v\|^2 = \mathbf v \cdot \mathbf v$ evita las raíces y permite usar la distributividad.

## Vectores unitarios y normalización

Un vector es **unitario** si su norma es 1. Todo vector no nulo tiene un unitario con su misma dirección y sentido:

$$
\mathbf u = \frac{1}{\|\mathbf v\|}\,\mathbf v ,
$$

que efectivamente mide $\frac{1}{\|\mathbf v\|}\|\mathbf v\| = 1$. Este proceso se llama **normalizar**.

![Normalización de un vector](adjuntos/Normalizaci%C3%B3n%20de%20un%20vector.png)

> [!example]- Transcripción de la imagen
> Un vector largo $\mathbf v$ en gris y, sobre la misma recta y con el mismo sentido, el vector azul $\frac{1}{\|\mathbf v\|}\mathbf v$, cuya longitud está marcada como $1$.

**Ejemplo.** Para $\mathbf v = \langle 2, -1, 3\rangle$: $\|\mathbf v\| = \sqrt{4 + 1 + 9} = \sqrt{14}$, así que el unitario es $\frac{1}{\sqrt{14}}\langle 2, -1, 3\rangle$. El unitario en sentido contrario es su opuesto.

Los **vectores unitarios estándar** de $\mathbb{R}^n$ son $\mathbf e_1, \dots, \mathbf e_n$, donde $\mathbf e_i$ tiene un $1$ en la posición $i$ y ceros en el resto. En $\mathbb{R}^3$:

$$
\mathbf e_1 = \begin{bmatrix}1\\0\\0\end{bmatrix},\quad \mathbf e_2 = \begin{bmatrix}0\\1\\0\end{bmatrix},\quad \mathbf e_3 = \begin{bmatrix}0\\0\\1\end{bmatrix}.
$$

Todo vector se escribe con ellos: $\langle a, b, c\rangle = a\mathbf e_1 + b\mathbf e_2 + c\mathbf e_3$, así que $\operatorname{Gen}\{\mathbf e_1, \mathbf e_2, \mathbf e_3\} = \mathbb{R}^3$.

## Distancia

> [!tip] Definición
> La **distancia** entre $\mathbf u$ y $\mathbf v$ es la norma de su diferencia: $d(\mathbf u, \mathbf v) = \|\mathbf u - \mathbf v\|$.

Corresponde a la longitud del vector que une las puntas, que es la distancia entre los puntos. Es simétrica, porque $\|\mathbf u - \mathbf v\| = \|-(\mathbf v - \mathbf u)\| = \|\mathbf v - \mathbf u\|$.

**Ejemplo.** Con $\mathbf u = \langle 2, 1, -1\rangle$ y $\mathbf v = \langle 0, 2, -2\rangle$: $\mathbf u - \mathbf v = \langle 2, -1, 1\rangle$ y $d(\mathbf u, \mathbf v) = \sqrt{4 + 1 + 1} = \sqrt 6$.

## Preguntas de repaso

> [!question]- Si $\|\mathbf u\| = 2$, $\|\mathbf v\| = 3$ y $\mathbf u \cdot \mathbf v = -1$, calcule $\|2\mathbf u - \mathbf v\|$.
> $\|2\mathbf u - \mathbf v\|^2 = 4\|\mathbf u\|^2 - 4\,\mathbf u \cdot \mathbf v + \|\mathbf v\|^2 = 16 + 4 + 9 = 29$, así que $\|2\mathbf u - \mathbf v\| = \sqrt{29}$. Se trabaja con el cuadrado para poder expandir.

> [!question]- V o F: si $\mathbf u \cdot \mathbf v = \mathbf u \cdot \mathbf w$ y $\mathbf u \neq \mathbf 0$, entonces $\mathbf v = \mathbf w$.
> Falso. Con $\mathbf u = \langle 1, 0\rangle$, $\mathbf v = \langle 0, 1\rangle$ y $\mathbf w = \langle 0, 5\rangle$ ambos productos valen 0. Solo se deduce que $\mathbf v - \mathbf w$ es perpendicular a $\mathbf u$.

> [!question]- ¿Por qué aparece $|c|$ y no $c$ en $\|c\mathbf v\| = |c|\,\|\mathbf v\|$?
> Porque la norma nunca es negativa y la raíz de $c^2$ es $|c|$. Invertir el sentido de un vector no cambia su largo.

> [!question]- Encuentre los vectores de norma 6 paralelos a $\langle 1, -2, 2\rangle$.
> Su norma es $\sqrt{1 + 4 + 4} = 3$, así que el unitario es $\tfrac13\langle 1, -2, 2\rangle$. Los buscados son $\pm 6 \cdot \tfrac13\langle 1, -2, 2\rangle = \pm\langle 2, -4, 4\rangle$.

> [!question]- ¿Qué vector es el único con $\mathbf v \cdot \mathbf v = 0$, y por qué esa propiedad es necesaria para definir la norma?
> Solo el vector cero. Gracias a eso, la única longitud nula es la del vector cero y la distancia entre dos puntos distintos es positiva. Sin la positividad, la raíz podría no existir o dos puntos distintos podrían estar a distancia cero.
