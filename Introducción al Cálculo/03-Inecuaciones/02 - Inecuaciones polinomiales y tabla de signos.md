---
ramo: "Introducción al Cálculo"
tema: "Inecuaciones"
tags:
  - intro-calculo/inecuaciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Intervalos y representación en la recta]]"
  - "[[04 - Cuadrados, inversos y signos del producto]]"
---

# Inecuaciones polinomiales y tabla de signos

Una **inecuación** de una incógnita es una desigualdad que puede ser verdadera o falsa según el valor de $x$; resolverla es encontrar todos los reales que la hacen verdadera. Para la gran familia de inecuaciones donde todo se reduce a productos de factores lineales, existe un método mecánico y seguro: la tabla de signos.

## Los puntos críticos y el método

Para un factor lineal $ax + b$, su **punto crítico** es $x = -\tfrac{b}{a}$: el único valor donde el factor vale cero y, por tanto, donde puede cambiar de signo.

> [!tip] Método de la tabla de signos
> Para resolver $\dfrac{P(x)}{Q(x)} \;(<,\ \le,\ >,\ \ge)\; 0$ con $P$ y $Q$ productos de factores lineales:
> 1. Pasar todo a un lado y factorizar, hasta tener un lado en $0$.
> 2. Hallar los puntos críticos de cada factor.
> 3. Ordenarlos de menor a mayor: dividen la recta en intervalos.
> 4. Armar una tabla con el signo de cada factor en cada intervalo y multiplicar los signos de cada columna.
> 5. Elegir los intervalos con el signo pedido y decidir qué pasa en cada punto crítico.

Funciona porque un factor lineal tiene un solo cambio de signo (en su raíz) y el signo de un producto es el producto de los signos (teorema del signo del producto).

## Ejemplo: una cuadrática

$x^2 + x > 2$. Se pasa todo a un lado y se factoriza: $x^2 + x - 2 > 0 \iff (x + 2)(x - 1) > 0$. Los puntos críticos son $-2$ y $1$.

| | $(-\infty, -2)$ | $(-2, 1)$ | $(1, \infty)$ |
|---|:-:|:-:|:-:|
| $x + 2$ | $-$ | $+$ | $+$ |
| $x - 1$ | $-$ | $-$ | $+$ |
| producto | $+$ | $-$ | $+$ |

Se pide $> 0$, así que $S = (-\infty, -2) \cup (1, \infty)$. Los puntos críticos quedan **fuera** porque la desigualdad es estricta; con $\ge$ entrarían.

## Cuadráticas sin raíces reales

Si el discriminante $\Delta = b^2 - 4ac$ de $ax^2 + bx + c$ es negativo, el polinomio no se anula y tiene el mismo signo en todo $\mathbb{R}$: el de $a$. Esto se prueba completando cuadrados: $x^2 + bx + c = \left(x + \tfrac{b}{2}\right)^2 + \left(c - \tfrac{b^2}{4}\right)$, con segundo término positivo.

> [!tip] Factores de signo fijo
> Un factor como $x^2 + 4x + 6 = (x + 2)^2 + 2 \ge 2$ nunca es cero ni negativo: se puede **tachar** de la inecuación (sin cambiar el sentido) o ignorar en la tabla. Es lo que permite a varias pautas resolver una inecuación con un factor cuadrático en una sola línea.

Ejemplo: $x^2 - 6x + 13 > 0$ es cierta para todo real, porque $\Delta = 36 - 52 < 0$ y el coeficiente principal es positivo; $S = \mathbb{R}$.

## Cuando las raíces no son racionales

Si el polinomio no factoriza con enteros, se usan las raíces de la fórmula cuadrática como puntos críticos. En $6x^2 - 2x - 1$ las raíces son $\tfrac{1 \pm \sqrt{7}}{6}$, y la factorización es $6\left(x - \tfrac{1 - \sqrt{7}}{6}\right)\left(x - \tfrac{1 + \sqrt{7}}{6}\right)$. La tabla es igual de válida con esos puntos críticos; solo hay que ordenarlos con aproximaciones ($-0{,}27$ y $0{,}61$).

> [!warning] No multiplicar ni dividir por una expresión sin conocer su signo
> $x(x - 2) > 3x$ **no** equivale a $x - 2 > 3$: se perdería el caso $x < 0$, donde dividir por $x$ invierte el sentido. Se pasa todo a un lado, se factoriza ($x(x - 5) > 0$) y se usa la tabla.

## Preguntas de repaso

> [!question]- ¿Por qué un factor lineal puede cambiar de signo solo en su punto crítico?
> Porque $ax + b = a\left(x + \tfrac{b}{a}\right)$ es cero solo en $x = -b/a$; para $x$ a un lado de ese punto el factor $x + \tfrac{b}{a}$ es positivo y al otro lado negativo, así que $ax + b$ tiene un signo en cada lado y no puede cambiar en ningún otro lugar.

> [!question]- ¿Qué ocurre con los puntos críticos al pasar de "$>$" a "$\ge$"?
> Los que anulan el numerador pasan a pertenecer al conjunto solución. Los que anulan el denominador siguen excluidos siempre.

> [!question]- ¿Cuál es el conjunto solución de $x^2 + 3 > 0$ y de $x^2 + 3 < 0$?
> $\mathbb{R}$ y $\varnothing$, respectivamente: $x^2 + 3 \ge 3$ para todo real.

> [!question]- ¿Qué se hace con un factor $x^2 + 4x + 6$ dentro de una inecuación?
> Como $(x + 2)^2 + 2 > 0$, es siempre positivo; se puede omitir de la tabla sin alterar el sentido de la desigualdad.
