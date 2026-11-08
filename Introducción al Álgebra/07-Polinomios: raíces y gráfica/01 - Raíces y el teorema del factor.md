---
ramo: "Introducción al Álgebra"
tema: "Polinomios: raíces y gráfica"
tags:
  - intro-algebra/polinomios
  - origen/complemento
prerrequisitos:
  - "[[03 - Teorema del resto]]"
---

# Raíces y el teorema del factor

Una **raíz** de un polinomio es un valor que lo anula. Encontrar raíces y factorizar son la misma tarea vista desde dos lados: un número es raíz si y solo si el factor lineal correspondiente divide al polinomio. Este puente es el **teorema del factor**.

## Raíz y factor

Decimos que $\alpha \in \mathbb{R}$ es **raíz** de $P$ si $P(\alpha) = 0$. Si al dividir $P$ entre $D$ el resto es $0$, escribimos $P(x) = D(x) Q(x)$ y decimos que $D$ **divide** a $P$ (o que $D$ es **factor** de $P$), y se denota $D(x) \mid P(x)$.

> [!tip] Teorema del factor
> $\alpha$ es raíz de $P$ si y solo si $(x - \alpha) \mid P(x)$, es decir, $P(x) = (x - \alpha)\,Q(x)$. Es la versión "de factor" del teorema del resto: $P(\alpha) = 0$ equivale a resto cero.

La proposición se completa con dos hechos: si $\alpha$ es raíz, existe una **multiplicidad** $m$ (el mayor entero con $(x - \alpha)^m \mid P$), y si $\alpha_1, \dots, \alpha_k$ son raíces dos a dos distintas, entonces el producto $(x - \alpha_1)\cdots(x - \alpha_k)$ divide a $P$.

## Factorizar con el teorema del factor

**Ejemplo.** Para $P(x) = 2x^3 - x^2 - 2x + 1$, verifique que $1$, $-1$ y $\tfrac12$ son raíces y factorice.

$P(1) = 2 - 1 - 2 + 1 = 0$, $P(-1) = -2 - 1 + 2 + 1 = 0$ y $P(\tfrac12) = \tfrac{2}{8} - \tfrac14 - 1 + 1 = 0$. Como las tres raíces son distintas, $(x - 1)(x + 1)(x - \tfrac12)$ divide a $P$, y por el coeficiente principal:

$$
P(x) = 2(x - 1)(x + 1)(x - \tfrac12) = (x - 1)(x + 1)(2x - 1).
$$

> [!warning] Raíz no es lo mismo que factor
> $\alpha$ es un *número* (la raíz); $(x - \alpha)$ es un *polinomio* (el factor). Decir "$2$ es raíz de $P$" equivale a "$x - 2$ divide a $P$".

## Preguntas de repaso

> [!question]- ¿Qué dice el teorema del factor?
> $\alpha$ es raíz de $P$ (es decir, $P(\alpha) = 0$) si y solo si $(x - \alpha)$ divide a $P$. Un lado es numérico y el otro es de división.

> [!question]- ¿Cuántas raíces distintas puede tener un polinomio de grado $3$?
> A lo más $3$, porque cada raíz $\alpha$ aporta un factor $(x - \alpha)$, y el producto de $k$ factores lineales tiene grado $k$, que no puede superar el grado del polinomio.

> [!question]- Si $P(x) = (x - 1)(x + 1)(2x - 1)$, ¿cuáles son sus raíces?
> $1$, $-1$ y $\tfrac12$: son los valores que anulan cada factor.

> [!question]- ¿Qué significa que una raíz tenga multiplicidad $m$?
> Que $(x - \alpha)^m$ divide a $P$ pero $(x - \alpha)^{m+1}$ no. La raíz "cuenta" $m$ veces en la factorización.
