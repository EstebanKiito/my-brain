---
ramo: "Álgebra Lineal"
tema: "Determinantes"
tags:
  - algebra-lineal/determinantes
  - origen/complemento
prerrequisitos:
  - "[[02 - Propiedades de los determinantes]]"
  - "[[02 - Matriz estándar de una transformación lineal]]"
---

# Determinante como área y volumen

El determinante tiene un significado geométrico directo: su valor absoluto es el **área** (en $\mathbb{R}^2$) o el **volumen** (en $\mathbb{R}^3$) de la figura que forman las columnas, y su signo dice si la transformación **conserva o invierte la orientación**. Esto explica de una vez por qué $\det A = 0$ significa no invertible: la transformación aplasta el espacio a una dimensión menor, y lo aplastado no se puede recuperar.

## Área y volumen

> [!tip] Teorema
> Si $A$ es de $2 \times 2$, el área del paralelogramo determinado por sus columnas es $|\det A|$. Si $A$ es de $3 \times 3$, el volumen del paralelepípedo determinado por sus columnas es $|\det A|$.

![Área del paralelogramo de dos vectores](adjuntos/%C3%81rea%20del%20paralelogramo%20de%20dos%20vectores.png)

> [!example]- Transcripción de la imagen
> El paralelogramo de lados $\langle a, b\rangle$ y $\langle c, d\rangle$, inscrito en el rectángulo de lados $a + c$ y $b + d$. Restando al rectángulo los triángulos y rectángulos de las esquinas, el área que queda es $ad - bc$, el determinante de la matriz con esas columnas.

![Volumen del paralelepípedo de tres vectores](adjuntos/Volumen%20del%20paralelep%C3%ADpedo%20de%20tres%20vectores.png)

> [!example]- Transcripción de la imagen
> Un paralelepípedo generado por tres vectores $\mathbf u$, $\mathbf v$ y $\mathbf w$ desde el origen. La altura $h$ sobre la base generada por $\mathbf v$ y $\mathbf w$ se marca con el ángulo $\theta$ entre $\mathbf u$ y la vertical. El volumen es área de la base por altura, y coincide con $|\det[\mathbf u\ \mathbf v\ \mathbf w]|$.

La idea de la demostración: los reemplazos de columna (sumar a una columna un múltiplo de otra) son **trasquilados**, que deslizan la figura sin cambiar su base ni su altura, así que no cambian el área. Con ellos se lleva la figura a un rectángulo (o caja) alineado con los ejes, cuya área es el producto de la diagonal, como el determinante.

**Ejemplo.** El paralelogramo con vértices $(-2, -2)$, $(0, 3)$, $(4, -1)$ y $(6, 4)$. Se traslada el vértice $(-2, -2)$ al origen sumando $\langle 2, 2\rangle$: los vértices pasan a $(0, 0)$, $(2, 5)$, $(6, 1)$ y $(8, 6)$. Los lados desde el origen son $\langle 2, 5\rangle$ y $\langle 6, 1\rangle$, y

$$
\text{Área} = \left|\det\begin{bmatrix} 2 & 6 \\ 5 & 1 \end{bmatrix}\right| = |2 - 30| = 28 .
$$

> [!warning] Lados, no vértices
> Las columnas de la matriz son los **lados** que salen de un mismo vértice, no los vértices. Si el paralelogramo no tiene un vértice en el origen, primero se restan coordenadas. Y hay que elegir dos lados adyacentes, no la diagonal: con vértices $P, Q, R, S$, la diagonal es la suma de los dos lados.

## Transformaciones lineales y áreas

> [!tip] Teorema
> Si $T: \mathbb{R}^2 \to \mathbb{R}^2$ tiene matriz $A$ y $S$ es un paralelogramo (o cualquier región con área),
> $$\text{área de } T(S) = |\det A| \cdot \text{área de } S .$$
> En $\mathbb{R}^3$ vale lo mismo con volúmenes.

Es decir, **$|\det A|$ es el factor por el que $T$ multiplica todas las áreas**. Si $S$ está generado por las columnas de $B$, $T(S)$ está generado por las columnas de $AB$, y $|\det AB| = |\det A||\det B|$. Para regiones curvas se aproxima con cuadraditos, y cada uno se escala por el mismo factor.

**Ejemplo.** $S$ es el paralelogramo de $\mathbf a = \langle 1, 3\rangle$ y $\mathbf b = \langle 5, 5\rangle$, con área $|5 - 15| = 10$. Bajo $A = \begin{bmatrix} 1 & -0{,}1 \\ 0 & 2 \end{bmatrix}$, con $\det A = 2$, la imagen tiene área $2 \cdot 10 = 20$.

**Ejemplo (elipse).** La región $E: \frac{x_1^2}{a^2} + \frac{x_2^2}{b^2} \leq 1$ es la imagen del disco unitario $D$ bajo $T(\mathbf u) = \begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix}\mathbf u$: si $u_1^2 + u_2^2 \leq 1$, entonces $x_1 = au_1$ y $x_2 = bu_2$ cumplen la desigualdad de la elipse. Como el disco tiene área $\pi$, el área de la elipse es $|ab| \cdot \pi = \pi ab$.

![Círculo unitario transformado en elipse](adjuntos/C%C3%ADrculo%20unitario%20transformado%20en%20elipse.png)

> [!example]- Transcripción de la imagen
> Arriba, el disco $D$ de radio 1 en el plano $(u_1, u_2)$. Una flecha $T$ lo lleva, abajo, a la región $E$ acotada por la elipse de semiejes $a$ (sobre $x_1$) y $b$ (sobre $x_2$).

## El signo: orientación

Si $\det A > 0$, $T$ conserva la **orientación** (una figura no se ve "en espejo"); si $\det A < 0$, la invierte, como una reflexión. Si $\det A = 0$, aplasta el plano a una recta o un punto: el área de la imagen es cero y la transformación no es invertible.

![Determinante como factor de área y orientación](adjuntos/Determinante%20como%20factor%20de%20%C3%A1rea%20y%20orientaci%C3%B3n.gif)

> [!example]- Transcripción de la animación
> El cuadrado unitario con una F se transforma con $A = \begin{bmatrix} 1 & 0{,}6 \\ 0 & t \end{bmatrix}$, cuyo determinante es $t$, mientras $t$ va de $1{,}5$ a $-1{,}5$ y vuelve. Con $t > 0$ la imagen (azul) es un paralelogramo de área $t$ con la F derecha. Al acercarse $t$ a $0$ el paralelogramo se aplasta sobre el eje $x_1$ (área cero, no invertible). Con $t < 0$ la imagen (naranja) queda bajo el eje, con área $|t|$ y la F espejada: la orientación se invirtió.

## Preguntas de repaso

> [!question]- Calcule el área del triángulo de vértices $(0, 0)$, $(3, 1)$ y $(1, 4)$.
> Es la mitad del paralelogramo de $\langle 3, 1\rangle$ y $\langle 1, 4\rangle$: $\tfrac12|12 - 1| = \tfrac{11}{2}$.

> [!question]- ¿Por qué una matriz con $\det A = 0$ no puede ser invertible, en términos geométricos?
> Porque manda el cuadrado unitario a una figura de área cero: aplasta el plano a una recta o un punto. Muchos puntos distintos caen en el mismo lugar, así que no hay forma de deshacer la transformación.

> [!question]- Una transformación de $\mathbb{R}^3$ tiene $\det A = -3$. ¿Qué le hace al volumen de un cubo de lado 2?
> El cubo tiene volumen 8; su imagen tiene volumen $|-3| \cdot 8 = 24$. Además invierte la orientación.

> [!question]- ¿Cuál es el área de la imagen del cuadrado unitario bajo un trasquilado $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$?
> $|\det| = 1$: el área no cambia, aunque la forma sí. Es el mismo argumento que prueba la fórmula del área.
