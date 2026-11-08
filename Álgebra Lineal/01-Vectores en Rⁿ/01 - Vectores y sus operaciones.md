---
ramo: "Álgebra Lineal"
tema: "Vectores en Rⁿ"
tags:
  - algebra-lineal/vectores
  - origen/complemento
prerrequisitos: []
---

# Vectores y sus operaciones

El álgebra lineal estudia objetos que se pueden **sumar** y **escalar**: desplazamientos, fuerzas, velocidades, colores RGB o las variables de un sistema de ecuaciones. El vector es el objeto básico. Tiene dos lecturas que conviene manejar a la vez: una **geométrica** (una flecha con dirección, sentido y magnitud) y una **algebraica** (una lista ordenada de números). La geometría da la intuición en el plano y el espacio, y el álgebra permite seguir trabajando en $\mathbb{R}^{n}$, donde ya no se puede dibujar.

## Dos lecturas de un vector

En $\mathbb{R}^2$ un vector es un par ordenado y en $\mathbb{R}^3$ una terna. Se escriben indistintamente en fila o en columna:

$$
\langle a, b\rangle = \begin{bmatrix} a \\ b \end{bmatrix}, \qquad \langle a, b, c\rangle = \begin{bmatrix} a \\ b \\ c \end{bmatrix}.
$$

Dibujado como flecha que parte del origen, se dice que está en **posición estándar**. Un mismo vector se puede dibujar en cualquier otro punto de partida: lo que lo define es cuánto se mueve en cada eje, no dónde empieza.

Por eso el vector que lleva del punto $A(a_1, a_2)$ al punto $B(b_1, b_2)$ es la diferencia de coordenadas, "punta menos cola":

$$
\overrightarrow{AB} = \langle b_1 - a_1,\ b_2 - a_2\rangle .
$$

Por ejemplo, de $A(2, 3)$ a $B(-1, 5)$ el desplazamiento es $\overrightarrow{AB} = \langle -3, 2\rangle$: tres unidades a la izquierda y dos hacia arriba.

![Vector entre dos puntos y vectores en posición estándar](adjuntos/Vector%20entre%20dos%20puntos%20y%20vectores%20en%20posici%C3%B3n%20est%C3%A1ndar.png)

> [!example]- Transcripción de la imagen
> - Izquierda: una flecha que va del punto $A$ al punto $B$ en el plano. Es el vector $\overrightarrow{AB}$, que no parte del origen.
> - Derecha: tres vectores $\mathbf a$, $\mathbf b$ y $\mathbf c$ que salen del origen $O$ y terminan en los puntos $A$, $B$ y $C$. Son vectores en posición estándar: cada uno coincide con las coordenadas de su punto final.

> [!tip] Vector en $\mathbb{R}^n$
> Un vector de $\mathbb{R}^n$ es una $n$-tupla de números reales $\mathbf v = \langle v_1, \dots, v_n\rangle$. Los $v_i$ son sus **componentes**, y dos vectores son **iguales** si y solo si coinciden componente a componente.

La igualdad componente a componente es lo que convierte una ecuación vectorial en varias ecuaciones escalares: $\langle x, 2y\rangle = \langle 3, 4\rangle$ dice a la vez $x = 3$ e $y = 2$. Esta idea es el puente hacia los sistemas de ecuaciones.

## Suma de vectores

La suma se define **por componentes**: si $\mathbf u = \langle u_1, \dots, u_n\rangle$ y $\mathbf v = \langle v_1, \dots, v_n\rangle$, entonces

$$
\mathbf u + \mathbf v = \langle u_1 + v_1, \dots, u_n + v_n\rangle .
$$

Solo tiene sentido si ambos vectores tienen el mismo número de componentes. Geométricamente es la **regla de punta con cola**: se dibuja $\mathbf v$ empezando en la punta de $\mathbf u$, y $\mathbf u + \mathbf v$ va desde el inicio de $\mathbf u$ hasta la punta de $\mathbf v$. Como $\mathbf u + \mathbf v = \mathbf v + \mathbf u$, el resultado es la diagonal del paralelogramo que forman $\mathbf u$ y $\mathbf v$ (**regla del paralelogramo**).

![Suma de vectores punta con cola](adjuntos/Suma%20de%20vectores%20punta%20con%20cola.png)

> [!example]- Transcripción de la imagen
> - Primer panel: dos flechas grises encadenadas, la segunda empieza donde termina la primera.
> - Segundo panel: $\mathbf u = \langle 1, 2\rangle$ (avanza 1 en $x$ y 2 en $y$) y, desde su punta, $\mathbf v = \langle 2, 2\rangle$.
> - Tercer panel: la flecha azul $\mathbf u + \mathbf v$ va del origen a la punta de $\mathbf v$ y avanza $3$ en $x$ y $4$ en $y$, es decir, $\mathbf u + \mathbf v = \langle 3, 4\rangle$.

## Multiplicación por un escalar

Si $c \in \mathbb{R}$, el **múltiplo escalar** es $c\mathbf v = \langle c v_1, \dots, c v_n\rangle$. Geométricamente estira o encoge la flecha por un factor $|c|$, y si $c < 0$ además invierte su sentido. Todos los múltiplos de un vector no nulo quedan sobre una misma recta por el origen; por eso dos vectores son **paralelos** cuando uno es múltiplo escalar del otro.

![Múltiplos escalares de un vector](adjuntos/M%C3%BAltiplos%20escalares%20de%20un%20vector.png)

> [!example]- Transcripción de la imagen
> Un vector azul $\mathbf v$ y, en gris, sus múltiplos $2\mathbf v$ (el doble de largo, mismo sentido), $-2\mathbf v$ (el doble de largo, sentido contrario) y $-\tfrac12\mathbf v$ (la mitad de largo, sentido contrario). Todos son paralelos a $\mathbf v$.

La resta se obtiene de las dos operaciones: $\mathbf u - \mathbf v = \mathbf u + (-1)\mathbf v$. Es justamente el vector que va de la punta de $\mathbf v$ a la punta de $\mathbf u$, lo que explica la fórmula "punta menos cola".

**Ejemplo.** Con $\mathbf u = \langle 2, -1, 3\rangle$ y $\mathbf v = \langle -1, 4, 0\rangle$:

$$
\mathbf u + \mathbf v = \langle 1, 3, 3\rangle, \qquad 2\mathbf u - \mathbf v = \langle 4, -2, 6\rangle - \langle -1, 4, 0\rangle = \langle 5, -6, 6\rangle .
$$

## Propiedades algebraicas

Para todo $\mathbf u, \mathbf v, \mathbf w \in \mathbb{R}^n$ y escalares $c, k$:

| Propiedad | Enunciado |
|---|---|
| Conmutatividad | $\mathbf u + \mathbf v = \mathbf v + \mathbf u$ |
| Asociatividad | $(\mathbf u + \mathbf v) + \mathbf w = \mathbf u + (\mathbf v + \mathbf w)$ |
| Neutro | $\mathbf 0 = \langle 0, \dots, 0\rangle$ cumple $\mathbf v + \mathbf 0 = \mathbf v$ |
| Opuesto | $\mathbf v + (-\mathbf v) = \mathbf 0$ |
| Distributividades | $c(\mathbf u + \mathbf v) = c\mathbf u + c\mathbf v$ y $(c + k)\mathbf v = c\mathbf v + k\mathbf v$ |
| Asociatividad escalar | $c(k\mathbf v) = (ck)\mathbf v$ |
| Identidad | $1\mathbf v = \mathbf v$ |

Todas se demuestran aplicando la propiedad análoga de los números reales en cada componente. Son las reglas que permiten despejar vectores como si fueran números (por ejemplo, de $2\mathbf x + \mathbf u = \mathbf v$ se obtiene $\mathbf x = \tfrac12(\mathbf v - \mathbf u)$). Más adelante, cualquier conjunto que cumpla estas ocho reglas se llamará espacio vectorial.

> [!warning] Lo que no existe
> No hay un "producto de vectores" componente a componente ni una división entre vectores. Las únicas operaciones de base son la suma y el producto por escalar. El producto punto, que se ve después, entrega un **número**, no un vector.

## Preguntas de repaso

> [!question]- ¿Por qué el vector de $A$ a $B$ se calcula como $B - A$ y no como $A - B$?
> Porque se busca el desplazamiento que, sumado al punto de partida, da el de llegada: $A + \overrightarrow{AB} = B$. Despejando, $\overrightarrow{AB} = B - A$. $A - B$ es el vector opuesto, que va de $B$ a $A$.

> [!question]- Calcule $3\mathbf u - 2\mathbf v$ con $\mathbf u = \langle 1, 0, -2\rangle$ y $\mathbf v = \langle 4, -1, 1\rangle$.
> $\langle 3, 0, -6\rangle - \langle 8, -2, 2\rangle = \langle -5, 2, -8\rangle$.

> [!question]- V o F: si $c\mathbf v = \mathbf 0$, entonces $c = 0$.
> Falso. También puede ser $\mathbf v = \mathbf 0$ con $c$ cualquiera. Lo correcto es "$c = 0$ o $\mathbf v = \mathbf 0$": si $c \neq 0$, multiplicar por $1/c$ da $\mathbf v = \mathbf 0$.

> [!question]- ¿Son paralelos $\langle 2, -6, 4\rangle$ y $\langle -1, 3, -2\rangle$? ¿Y $\langle 1, 2, 3\rangle$ y $\langle 2, 4, 5\rangle$?
> Los primeros sí: $\langle 2, -6, 4\rangle = -2\langle -1, 3, -2\rangle$. Los segundos no: el factor tendría que ser 2 por la primera componente, pero $2 \cdot 3 = 6 \neq 5$.

> [!question]- Encuentre $\mathbf x$ tal que $3\mathbf x - \langle 1, 2\rangle = \mathbf x + \langle 5, -4\rangle$. ¿Qué propiedades usó?
> $2\mathbf x = \langle 6, -2\rangle$, así que $\mathbf x = \langle 3, -1\rangle$. Se suma el opuesto a ambos lados (neutro y opuesto), se agrupa con la distributividad $(3 - 1)\mathbf x$ y se multiplica por $\tfrac12$ (asociatividad escalar e identidad).
