---
ramo: "Álgebra Lineal"
tema: "Transformaciones lineales"
tags:
  - algebra-lineal/transformaciones
  - origen/complemento
prerrequisitos:
  - "[[03 - Producto matriz-vector y ecuación vectorial]]"
---

# Transformaciones y linealidad

Hasta ahora $A\mathbf x = \mathbf b$ se leyó como una ecuación: dado $\mathbf b$, buscar $\mathbf x$. Cambiando el punto de vista, la matriz $A$ es una **máquina** que recibe un vector $\mathbf x$ y entrega otro, $A\mathbf x$. Esa lectura convierte a las matrices en funciones entre espacios y conecta el álgebra con la geometría: rotar, reflejar, proyectar o estirar figuras son transformaciones de este tipo.

## Transformaciones

> [!tip] Definición
> Una **transformación** (o función, o mapeo) $T: \mathbb{R}^n \to \mathbb{R}^m$ asigna a cada $\mathbf x \in \mathbb{R}^n$ un vector $T(\mathbf x) \in \mathbb{R}^m$, llamado **imagen** de $\mathbf x$. $\mathbb{R}^n$ es el **dominio**, $\mathbb{R}^m$ el **codominio**, y el conjunto de todas las imágenes $\{T(\mathbf x) : \mathbf x \in \mathbb{R}^n\}$ es el **rango** (o recorrido, o imagen) de $T$.

![Dominio, codominio y rango de una transformación](adjuntos/Dominio,%20codominio%20y%20rango%20de%20una%20transformaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> A la izquierda, el dominio $\mathbb{R}^n$ con un punto $\mathbf x$. Una flecha $T$ lo lleva a $T(\mathbf x)$, dentro de un cubo que representa el codominio $\mathbb{R}^m$. Dentro del cubo, una región sombreada marca el **rango**: los puntos que efectivamente son imagen de algún $\mathbf x$. El rango puede ser más chico que el codominio.

Una **transformación matricial** es $T(\mathbf x) = A\mathbf x$ con $A$ de $m \times n$: el dominio tiene tantas dimensiones como **columnas** tiene $A$, y el codominio tantas como **filas**. Su rango es el conjunto de combinaciones lineales de las columnas, es decir, $\operatorname{Gen}$ de las columnas de $A$.

**Ejemplo.** $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T(\mathbf x) = A\mathbf x$ con $A = \begin{bmatrix} 1 & -3 \\ 3 & 5 \\ -1 & 7 \end{bmatrix}$.

- Imagen de $\mathbf u = \langle 2, -1\rangle$: $T(\mathbf u) = \langle 5, 1, -9\rangle$.
- Fórmula general: $T\langle x_1, x_2\rangle = \langle x_1 - 3x_2,\ 3x_1 + 5x_2,\ -x_1 + 7x_2\rangle$.
- ¿Hay $\mathbf x$ con $T(\mathbf x) = \mathbf b = \langle 3, 2, -5\rangle$? Escalonando $[A \mid \mathbf b]$ se obtiene $\mathbf x = \langle \tfrac32, -\tfrac12\rangle$, **una sola** (las columnas son LI).
- ¿Está $\mathbf c = \langle 3, 2, 5\rangle$ en el rango? $[A \mid \mathbf c]$ tiene pivote en la última columna: **no**.

Cada pregunta sobre $T$ es una pregunta sobre un sistema lineal.

## Transformaciones lineales

> [!tip] Definición
> $T: \mathbb{R}^n \to \mathbb{R}^m$ es **lineal** si para todo $\mathbf u, \mathbf v \in \mathbb{R}^n$ y todo escalar $c$:
> 1. $T(\mathbf u + \mathbf v) = T(\mathbf u) + T(\mathbf v)$ (preserva sumas);
> 2. $T(c\mathbf u) = cT(\mathbf u)$ (preserva múltiplos escalares).

Toda transformación matricial es lineal, por las propiedades $A(\mathbf u + \mathbf v) = A\mathbf u + A\mathbf v$ y $A(c\mathbf u) = cA\mathbf u$. Lo sorprendente (siguiente nota) es que en $\mathbb{R}^n$ también vale lo recíproco.

> [!tip] Propiedades de una transformación lineal
> - $T(\mathbf 0) = \mathbf 0$.
> - $T(c_1\mathbf u_1 + \dots + c_k\mathbf u_k) = c_1T(\mathbf u_1) + \dots + c_kT(\mathbf u_k)$ (**principio de superposición**).

La primera sale de $T(\mathbf 0) = T(0 \cdot \mathbf 0) = 0 \cdot T(\mathbf 0) = \mathbf 0$. La segunda dice que **basta conocer $T$ en unos pocos vectores** para conocerla en todas sus combinaciones.

**Ejemplo.** Si $T(\mathbf e_1) = \langle 2, 5\rangle$ y $T(\mathbf e_2) = \langle -1, 6\rangle$, entonces $T\langle 5, -3\rangle = 5T(\mathbf e_1) - 3T(\mathbf e_2) = \langle 13, 7\rangle$, y en general $T\langle x_1, x_2\rangle = \langle 2x_1 - x_2,\ 5x_1 + 6x_2\rangle$.

## Ejemplos y contraejemplos

| Transformación | ¿Lineal? | Por qué |
|---|---|---|
| $T\langle x_1, x_2, x_3\rangle = \langle x_1, x_2\rangle$ | sí | es $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}\mathbf x$ (proyección) |
| $T\langle x_1, x_2\rangle = \langle x_1 + 3x_2, x_2\rangle$ | sí | es $\begin{bmatrix} 1 & 3 \\ 0 & 1 \end{bmatrix}\mathbf x$ (trasquilado) |
| $T(\mathbf x) = r\mathbf x$ | sí | es $rI$ (contracción si $0 \leq r < 1$, dilatación si $r > 1$) |
| $T\langle x_1, x_2\rangle = \langle -x_2, x_1\rangle$ | sí | es $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}\mathbf x$ (giro de $90°$) |
| $T\langle x_1, x_2\rangle = \langle x_1 - 2x_2, x_1 - 3\rangle$ | no | $T(\mathbf 0) = \langle 0, -3\rangle \neq \mathbf 0$ |
| $T\langle x_1, x_2\rangle = \langle x_1^2, x_2\rangle$ | no | $T(2\mathbf e_1) = \langle 4, 0\rangle \neq 2T(\mathbf e_1)$ |
| $T(\mathbf x) = A\mathbf x + \mathbf b$, $\mathbf b \neq \mathbf 0$ | no | $T(\mathbf 0) = \mathbf b$ (se llama transformación **afín**) |

> [!warning] $T(\mathbf 0) = \mathbf 0$ es necesario pero no suficiente
> Si $T(\mathbf 0) \neq \mathbf 0$, $T$ no es lineal y no hay nada más que revisar. Pero $T(\mathbf 0) = \mathbf 0$ no prueba linealidad: $\langle x_1^2, x_2\rangle$ y $\langle |x_1|, x_2\rangle$ fijan el origen y no son lineales. Para probar que una $T$ es lineal, lo más directo es escribirla como $A\mathbf x$; para probar que no lo es, basta un contraejemplo concreto.

Las transformaciones lineales **mandan rectas en rectas (o en puntos)**: la recta $\mathbf p + t\mathbf d$ va a $T(\mathbf p) + tT(\mathbf d)$, que es una recta si $T(\mathbf d) \neq \mathbf 0$ y un solo punto si $T(\mathbf d) = \mathbf 0$. Por eso un cuadrado se transforma en un paralelogramo (posiblemente aplastado).

## Preguntas de repaso

> [!question]- Si $A$ es de $4 \times 7$, ¿cuál es el dominio y el codominio de $\mathbf x \mapsto A\mathbf x$?
> Dominio $\mathbb{R}^7$ (columnas) y codominio $\mathbb{R}^4$ (filas).

> [!question]- ¿Es lineal $T\langle x, y\rangle = \langle 2x - y,\ 3xy\rangle$?
> No. $T(2\langle 1, 1\rangle) = T\langle 2, 2\rangle = \langle 2, 12\rangle$, pero $2T\langle 1, 1\rangle = 2\langle 1, 3\rangle = \langle 2, 6\rangle$. El producto $xy$ rompe la homogeneidad.

> [!question]- Si $T$ es lineal, $T(\mathbf u) = \langle 1, 2\rangle$ y $T(\mathbf v) = \langle 0, -1\rangle$, calcule $T(3\mathbf u - 2\mathbf v)$.
> Por superposición, $3\langle 1, 2\rangle - 2\langle 0, -1\rangle = \langle 3, 8\rangle$.

> [!question]- ¿Por qué el rango de $T(\mathbf x) = A\mathbf x$ es el generado por las columnas de $A$?
> Porque $A\mathbf x = x_1\mathbf a_1 + \dots + x_n\mathbf a_n$: las imágenes son exactamente todas las combinaciones lineales de las columnas.

> [!question]- Una transformación lineal $T: \mathbb{R}^2 \to \mathbb{R}^2$ cumple $T(\mathbf d) = \mathbf 0$ para un $\mathbf d \neq \mathbf 0$. ¿Qué le pasa a la recta $\mathbf p + t\mathbf d$?
> Se aplasta en un solo punto: $T(\mathbf p + t\mathbf d) = T(\mathbf p)$ para todo $t$.
