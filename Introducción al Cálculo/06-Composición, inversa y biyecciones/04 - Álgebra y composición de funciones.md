---
ramo: "Introducción al Cálculo"
tema: "Composición, inversa y biyecciones"
tags:
  - intro-calculo/inversa
  - origen/complemento
prerrequisitos:
  - "[[02 - Funciones sobreyectivas y biyectivas]]"
---

# Álgebra y composición de funciones

Las funciones se pueden sumar, multiplicar, dividir y, sobre todo, **componer**: usar la salida de una como entrada de otra. La composición es la operación que da sentido a la función inversa y a casi todas las fórmulas complicadas, y exige cuidar un detalle: el dominio de la composición no es el dominio de la función "de afuera".

## Álgebra de funciones

> [!tip] Operaciones
> Para $f : A \to \mathbb{R}$ y $g : B \to \mathbb{R}$:
> - $(f \pm g)(x) = f(x) \pm g(x)$ y $(fg)(x) = f(x)g(x)$, con dominio $A \cap B$.
> - $\left(\tfrac{f}{g}\right)(x) = \tfrac{f(x)}{g(x)}$, con dominio $\{x \in A \cap B \mid g(x) \neq 0\}$.

**Ejemplo (clase 14).** $f(x) = \dfrac{x + 1}{\sqrt{x + 2}}$ (dominio $(-2, \infty)$) y $g(x) = \dfrac{x^2 - 1}{x^2 - x - 6}$ (dominio $\mathbb{R} \setminus \{-2, 3\}$). Entonces $(f + g)(2) = \tfrac{3}{2} + \tfrac{3}{-4} = \tfrac{3}{4}$. Para el cociente,
$$\frac{f}{g}(x) = \frac{x + 1}{\sqrt{x + 2}} \cdot \frac{(x - 3)(x + 2)}{(x - 1)(x + 1)} = \frac{(x - 3)\sqrt{x + 2}}{x - 1},$$
con dominio $(-2, \infty) \setminus \{-1, 1, 3\}$: se excluye $-1$ y $1$ (donde $g = 0$) y $3$ (fuera del dominio de $g$). Aunque $x + 1$ se simplifica en la fórmula, $x = -1$ sigue excluido.

## Función compuesta

> [!tip] Composición
> Si $f : A \to C$ y $g : B \to D$ cumplen $\operatorname{Rec}(f) \subseteq \operatorname{Dom}(g)$, la **composición** $g \circ f : A \to D$ es $(g \circ f)(x) = g(f(x))$: se aplica **primero $f$ y después $g$**. En general se define con el dominio
> $$\operatorname{Dom}(g \circ f) = \{\, x \in \operatorname{Dom}(f) \mid f(x) \in \operatorname{Dom}(g) \,\}.$$

La segunda forma es la importante: la composición solo existe donde la salida de $f$ cae en el dominio de $g$. Es una **condición sobre $x$**, que se resuelve con inecuaciones.

**Un ejemplo de dominio (clase 14, ejemplo 4).** $f : (-\infty, 5) \to \mathbb{R}$, $f(x) = \sqrt{x^2 + 4}$ y $g : [6, \infty) \to \mathbb{R}$, $g(x) = 2x + 3$. Entonces $x \in \operatorname{Dom}(g \circ f) \iff x < 5 \wedge \sqrt{x^2 + 4} \ge 6 \iff x < 5 \wedge x^2 \ge 32 \iff x \le -\sqrt{32}$ (la rama $x \ge \sqrt{32} \approx 5{,}66$ queda fuera de $x < 5$). $\operatorname{Dom}(g \circ f) = (-\infty, -\sqrt{32}]$ y $(g \circ f)(x) = 2\sqrt{x^2 + 4} + 3$.

**Un ejemplo de dominio con parámetro (Examen, 2023-2).** $f(x) = 3x + 2$ y $g : [-1, 1] \to \mathbb{R}$, $g(x) = \sqrt{1 - x^2}$. $x \in \operatorname{Dom}(g \circ f) \iff 3x + 2 \in [-1, 1] \iff x \in \left[-1, -\tfrac{1}{3}\right]$, y $(g \circ f)(x) = \sqrt{1 - (3x + 2)^2}$.

**Con una función por tramos (Examen, 2024-1).** Si $\operatorname{Dom}(f) = [0, 2]$ y $g(x) = f(x^2 - 4x + 5)$, entonces $x \in \operatorname{Dom}(g) \iff x^2 - 4x + 5 \in [0, 2]$. Como $x^2 - 4x + 5 = (x - 2)^2 + 1 \ge 1 > 0$, solo importa $x^2 - 4x + 5 \le 2 \iff (x - 1)(x - 3) \le 0$: $\operatorname{Dom}(g) = [1, 3]$.

## La composición no conmuta

En general $g \circ f \neq f \circ g$, y a veces solo una de las dos existe.

- $f(x) = 2x + 1$ y $g(x) = x^2$: $(g \circ f)(x) = (2x + 1)^2$ pero $(f \circ g)(x) = 2x^2 + 1$.
- $f : \mathbb{N} \to \mathbb{N}$, $f(n) = 2n$ y $g : P \to \mathbb{Z}$, $g(m) = -m$ con $P$ los naturales pares: $g \circ f(n) = -2n$ existe, pero $f \circ g$ no, porque $g(m) \in \mathbb{Z}$ no está en $\mathbb{N}$.

## Composición con funciones por tramos

Cuando $f$ está definida por tramos, hay que **traducir la condición del tramo** a una condición sobre $x$.

Sea $g(x) = -3x + 1$ y $f(x) = \begin{cases} x^2 + 5 & x < -1 \\ 1 - x & x \ge -1 \end{cases}$ (clase 14, ejemplo 5). Ambas composiciones tienen dominio $\mathbb{R}$. Para $f \circ g$, el tramo depende de si $g(x) < -1$, es decir $-3x + 1 < -1 \iff x > \tfrac{2}{3}$:
$$(f \circ g)(x) = \begin{cases} (-3x + 1)^2 + 5 = 9x^2 - 6x + 6 & x > \tfrac{2}{3} \\ 1 - (-3x + 1) = 3x & x \le \tfrac{2}{3} \end{cases}$$
Para $g \circ f$, se aplica $g$ a cada tramo de $f$:
$$(g \circ f)(x) = \begin{cases} -3(x^2 + 5) + 1 = -3x^2 - 14 & x < -1 \\ -3(1 - x) + 1 = 3x - 2 & x \ge -1 \end{cases}$$

## Composición y biyectividad

> [!tip] Composición y propiedades
> Si $g \circ f$ está bien definida: (1) si $f$ y $g$ son inyectivas, $g \circ f$ es inyectiva; (2) si $f$ y $g$ son sobreyectivas, $g \circ f$ es sobreyectiva. En particular, la composición de dos biyecciones es una biyección.

Se usa para probar inyectividad "por piezas": $f(x) = \sqrt{\tfrac{2x - 3}{x + 4}}$ es la composición de $\ell(x) = \tfrac{2x - 3}{x + 4}$ (de Möbius, inyectiva) con $h(x) = \sqrt{x}$ (inyectiva en $[0, \infty)$), luego $f$ es inyectiva en su dominio.

## Preguntas de repaso

> [!question]- ¿Cómo se halla el dominio de $g \circ f$?
> Se piden dos cosas: que $x$ esté en $\operatorname{Dom}(f)$ y que $f(x)$ esté en $\operatorname{Dom}(g)$. Se resuelve la segunda condición como una inecuación en $x$ y se intersecta con $\operatorname{Dom}(f)$.

> [!question]- Si $f(x) = \sqrt{x}$ y $g(x) = 2 - x$, ¿cuál es el dominio de $f \circ g$?
> $f(g(x)) = \sqrt{2 - x}$ exige $2 - x \ge 0$: $\operatorname{Dom}(f \circ g) = (-\infty, 2]$. En cambio $g \circ f(x) = 2 - \sqrt{x}$ tiene dominio $[0, \infty)$.

> [!question]- ¿Por qué $g \circ f$ y $f \circ g$ son distintas para $f(x) = 2x + 1$ y $g(x) = x^2$?
> $g(f(x)) = (2x + 1)^2$ y $f(g(x)) = 2x^2 + 1$: el orden en que se aplican cambia el resultado.

> [!question]- ¿Cómo se compone una función por tramos con otra?
> Se identifica para qué valores de $x$ la salida interna cae en cada tramo (resolviendo una desigualdad) y se aplica la fórmula correspondiente.
