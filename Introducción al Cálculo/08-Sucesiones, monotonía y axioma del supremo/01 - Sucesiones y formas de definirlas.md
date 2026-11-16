---
ramo: "Introducción al Cálculo"
tema: "Sucesiones, monotonía y axioma del supremo"
tags:
  - intro-calculo/sucesiones
  - origen/complemento
prerrequisitos:
  - "[[01 - El número e y la función exponencial]]"
---

# Sucesiones y formas de definirlas

Una sucesión es una lista infinita de números en un orden fijo. Es la herramienta con la que el cálculo aprende a hablar de "acercarse": el número $e$, las sumas infinitas y los límites son todos sucesiones. Antes de estudiar su comportamiento hay que saber describirlas, y hay tres maneras principales de hacerlo.

## Definición

> [!tip] Sucesión
> Una **sucesión** de números reales es una función $f : \mathbb{N} \to \mathbb{R}$ que a cada natural $n$ le asocia un real $f(n) = f_n$, el **$n$-ésimo término**. Se escribe $\{f_n\}$ o $\{f_n\}_{n \in \mathbb{N}}$ y se piensa como la lista $f_1, f_2, f_3, \ldots$

Que sea una función explica propiedades que se usarán más adelante: como $\mathbb{N}$ está ordenado, tiene sentido hablar de términos "anteriores" y "siguientes" y de si la lista sube o baja.

## Tres formas de dar una sucesión

1. **Descripción:** "la sucesión de los naturales pares" $2, 4, 6, 8, \ldots$
2. **Fórmula explícita:** el término $n$-ésimo en términos de $n$, como $x_n = 2n$. Casi siempre es lo más útil.
3. **Recursión:** se da el primer término y una regla que calcula cada uno desde los anteriores, como $x_1 = 2$ y $x_n = x_{n-1} + 2$.

La **fórmula de recursión** es preferible cuando relaciona el término con el anterior de manera simple y no hay una expresión cerrada fácil (o cuando se calcula con computador). El ejemplo clásico es el factorial: $0! = 1$, $1! = 1$ y $n! = n \cdot (n - 1)!$.

## Progresiones

> [!tip] Progresión aritmética
> Cada término se obtiene del anterior **sumando** una cantidad fija $d$ (la diferencia): $c, c + d, c + 2d, \ldots$ Su término general es $x_n = c + (n - 1)d$, o en recursión $x_1 = c$, $x_n = x_{n-1} + d$.

Ejemplo: con $c = 3$ y $d = 5$: $3, 8, 13, 18, \ldots$ y $x_n = 3 + 5(n - 1) = 5n - 2$.

> [!tip] Progresión geométrica
> Cada término se obtiene **multiplicando** por una razón fija $r$: $c, cr, cr^2, \ldots$ con $x_n = cr^{n-1}$, o en recursión $x_1 = c$, $x_n = r\,x_{n-1}$.

Ejemplo: con $c = 3$ y $r = \tfrac{1}{2}$: $3, \tfrac{3}{2}, \tfrac{3}{4}, \tfrac{3}{8}, \ldots$ y $x_n = 3\left(\tfrac{1}{2}\right)^{n-1}$. El tratamiento de sumas y recurrencias de progresiones aparece en [[03 - Progresiones aritméticas y geométricas|Introducción al Álgebra]] y se retoma en el tema de sumas finitas.

## Iteración

Una forma recursiva general es la **sucesión iterativa** de una función: dados $f : X \to \mathbb{R}$ y $c \in X$,
$$c,\ f(c),\ f(f(c)),\ f(f(f(c))),\ \ldots \qquad x_1 = c,\ \ x_n = f(x_{n-1}).$$
Si $f(x) = x + b$ el resultado es una progresión aritmética; si $f(x) = ax$ es una progresión geométrica. Por ejemplo, con $f(x) = 2x$ y $c = \tfrac{1}{2}$: $\tfrac{1}{2}, 1, 2, 4, \ldots$, es decir $x_n = \tfrac{1}{2}\cdot 2^{n-1}$. Casi todas las sucesiones recursivas de las pruebas (como $a_{n+1} = \sqrt{2 + a_n}$) son iteraciones.

## Sucesión de sumas parciales

> [!tip] Sumas parciales
> A partir de $\{x_n\}$ se construye $\{s_n\}$ sumando los términos: $s_1 = x_1$, $s_n = s_{n-1} + x_n$, es decir $s_n = x_1 + x_2 + \dots + x_n$.

**Ejemplo (clase 18).** Para $x_n = \tfrac{1}{2^n}$: $s_1 = \tfrac{1}{2}$, $s_2 = \tfrac{3}{4}$, $s_3 = \tfrac{7}{8}$, $s_4 = \tfrac{15}{16}$, y el patrón es
$$s_n = \frac{2^n - 1}{2^n} = 1 - \frac{1}{2^n}.$$
Se demuestra por inducción: $s_{n+1} = s_n + \tfrac{1}{2^{n+1}} = 1 - \tfrac{1}{2^n} + \tfrac{1}{2^{n+1}} = 1 - \tfrac{1}{2^{n+1}}$. Los términos $s_n$ crecen y se acercan a $1$ sin alcanzarlo: es el primer ejemplo de una suma infinita.

> [!warning] Sucesión no es conjunto
> $\{1, 1, 1, \ldots\}$ como sucesión tiene infinitos términos, aunque como conjunto es $\{1\}$. Y el orden importa: $1, 2, 3, \ldots$ y $2, 1, 3, \ldots$ son sucesiones distintas.

## Preguntas de repaso

> [!question]- ¿Cuál es el término general de la progresión aritmética $7, 4, 1, -2, \ldots$?
> $c = 7$ y $d = -3$, así que $x_n = 7 - 3(n - 1) = 10 - 3n$.

> [!question]- ¿Cuál es la razón de la geométrica $5, -10, 20, -40, \ldots$ y su término general?
> $r = -2$ y $x_n = 5(-2)^{n-1}$.

> [!question]- ¿Qué ventaja tiene una fórmula recursiva frente a una explícita?
> Es más simple de escribir cuando el término depende solo del anterior (factorial, iteraciones), aunque para calcular el $n$-ésimo término hay que pasar por todos los anteriores.

> [!question]- ¿Cuál es la sucesión de sumas parciales de $x_n = 1$?
> $s_n = n$: $1, 2, 3, \ldots$, que crece sin cota.
