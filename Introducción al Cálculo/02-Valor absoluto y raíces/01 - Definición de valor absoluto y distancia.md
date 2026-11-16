---
ramo: "Introducción al Cálculo"
tema: "Valor absoluto y raíces"
tags:
  - intro-calculo/valor-absoluto
  - origen/complemento
prerrequisitos:
  - "[[04 - Cuadrados, inversos y signos del producto]]"
---

# Definición de valor absoluto y distancia

Además de operar y ordenar, el cálculo necesita **medir**: saber qué tan lejos está un número de otro. La distancia entre $x$ e $y$ es $x - y$ o $y - x$, según cuál sea positivo, y el valor absoluto es la herramienta que elige entre los dos sin tener que decidir de antemano. Es la base de toda la idea de "acercarse" que más adelante se vuelve el concepto de límite.

## Definición

> [!tip] Valor absoluto
> Para $x \in \mathbb{R}$,
> $$|x| = \begin{cases} x & \text{si } x \ge 0, \\ -x & \text{si } x < 0. \end{cases}$$

Es la distancia de $x$ a $0$. Está definido con la desigualdad $x \ge 0$ o $x < 0$, y por eso casi todas sus propiedades se demuestran separando en esos dos casos. Siempre es $\ge 0$: si $x \ge 0$, $|x| = x \ge 0$; si $x < 0$, $|x| = -x > 0$.

> [!tip] Forma con raíz
> $|x| = \sqrt{x^2}$, y por lo tanto $|x|^2 = x^2$ para todo real $x$.

Esta segunda forma es la más útil para demostrar: permite **elevar al cuadrado** para eliminar valores absolutos (cuando ambos lados son $\ge 0$). La raíz cuadrada se estudia con detalle en [[05 - Raíces cuadradas y valor absoluto|raíces cuadradas y valor absoluto]].

> [!warning] $|x|$ no es "quitar el signo menos"
> Si $x = -a$ con $a > 0$, $|x| = a$; pero si $x$ es una variable cuyo signo no se conoce, $|x|$ **no** es $x$ ni $-x$ a priori: hay que separar casos. Por ejemplo $|x - 3|$ vale $x - 3$ cuando $x \ge 3$ y $3 - x$ cuando $x < 3$.

## La distancia entre dos números

> [!tip] Distancia
> $d(x, y) = |x - y|$ es la distancia entre $x$ e $y$ en la recta.

Por ejemplo, la distancia entre $3$ y $-4$ es $|3 - (-4)| = 7$, y la distancia entre $\pi$ y $\sqrt{10}$ es $\sqrt{10} - \pi$ (positiva, porque $\sqrt{10} > \pi$). Casi nunca se escribe $d(x, y)$ en cálculo: se deja $|x - y|$, interpretado como distancia.

Cuatro propiedades resumen lo que una distancia debe cumplir:

1. $d(x, y) \ge 0$.
2. $d(x, y) = 0 \iff x = y$.
3. $d(x, y) = d(y, x)$ (simetría), porque $|y - x| = |-(x - y)| = |-1|\,|x - y| = |x - y|$.
4. $d(x, y) \le d(x, z) + d(z, y)$ (desigualdad triangular): ir de $x$ a $y$ pasando por $z$ nunca acorta el camino.

La cuarta sale de la [[02 - Propiedades del valor absoluto y desigualdad triangular|desigualdad triangular del valor absoluto]]: $|x - y| = |(x - z) + (z - y)| \le |x - z| + |z - y|$.

## Preguntas de repaso

> [!question]- ¿Por qué $|x| \ge 0$ para todo real?
> Si $x \ge 0$, $|x| = x \ge 0$. Si $x < 0$, $|x| = -x$ y $-x > 0$. En ambos casos es no negativo.

> [!question]- ¿Cuánto vale $|x - 3|$ cuando $x < 3$?
> Vale $3 - x$, porque $x - 3 < 0$ y se cambia el signo.

> [!question]- ¿Cuál es la distancia entre $-2$ y $5$, y por qué $d(x,y) = d(y,x)$?
> Es $|-2 - 5| = 7$. La simetría sale de que $|-t| = |t|$: $|y - x| = |-(x - y)| = |x - y|$.

> [!question]- ¿Qué significa geométricamente $d(x, y) \le d(x, z) + d(z, y)$?
> Que el camino directo de $x$ a $y$ no es más largo que cualquier desvío pasando por un tercer punto $z$.
