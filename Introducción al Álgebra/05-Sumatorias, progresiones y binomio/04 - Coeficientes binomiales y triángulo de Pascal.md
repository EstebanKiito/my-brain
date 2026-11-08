---
ramo: "Introducción al Álgebra"
tema: "Sumatorias, progresiones y binomio"
tags:
  - intro-algebra/sumatorias-binomio
  - origen/complemento
prerrequisitos:
  - "[[05 - Definiciones por inducción]]"
---

# Coeficientes binomiales y triángulo de Pascal

Los coeficientes que aparecen al desarrollar $(a + b)^n$ tienen nombre y fórmula propia. Antes de enunciar el teorema del binomio conviene conocerlos y saber calcularlos rápido.

## Factorial y coeficiente binomial

El **factorial** se define por recurrencia: $0! = 1$ y $(n+1)! = (n+1) \cdot n!$. Así $n! = 1 \cdot 2 \cdots n$.

> [!tip] Coeficiente binomial
> Para enteros $0 \le k \le n$:
> $$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}.$$
> Se lee "$n$ sobre $k$" y cuenta de cuántas formas se eligen $k$ objetos entre $n$.

Para calcularlo a mano se cancela el factorial más grande del denominador:
$$\binom{9}{4} = \frac{9!}{4!\,5!} = \frac{9 \cdot 8 \cdot 7 \cdot 6}{4 \cdot 3 \cdot 2 \cdot 1} = 126.$$

## Propiedades

> [!tip] Propiedades de los coeficientes binomiales
> - $\binom{n}{0} = \binom{n}{n} = 1$ y $\binom{n}{1} = \binom{n}{n-1} = n$.
> - **Simetría:** $\binom{n}{k} = \binom{n}{n-k}$.
> - **Regla de Pascal:** $\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}$.

La regla de Pascal se prueba sumando las fracciones con denominador común $(k+1)!\,(n-k)!$. Es la que permite construir todos los coeficientes sin factoriales.

## Triángulo de Pascal

Cada fila empieza y termina en $1$, y cada número interior es la suma de los dos que tiene arriba (regla de Pascal). La fila $n$ contiene $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}$.

| $n$ | $k=0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | | | | | | |
| 2 | 1 | 2 | 1 | | | | | |
| 3 | 1 | 3 | 3 | 1 | | | | |
| 4 | 1 | 4 | 6 | 4 | 1 | | | |
| 5 | 1 | 5 | 10 | 10 | 5 | 1 | | |
| 6 | 1 | 6 | 15 | 20 | 15 | 6 | 1 | |
| 7 | 1 | 7 | 21 | 35 | 35 | 21 | 7 | 1 |

Por ejemplo, $\binom{5}{2} = 10 = 4 + 6 = \binom{4}{1} + \binom{4}{2}$. La simetría se ve en que cada fila se lee igual de izquierda a derecha que al revés.

> [!warning] $\binom{n}{k}$ no es una fracción
> Aunque la fórmula tiene una división, el resultado siempre es un entero (la regla de Pascal lo construye sumando enteros). Si al calcular sale una fracción, hay un error de cancelación.

## Preguntas de repaso

> [!question]- Calcule $\binom{10}{4}$.
> $\frac{10 \cdot 9 \cdot 8 \cdot 7}{4 \cdot 3 \cdot 2 \cdot 1} = 210$.

> [!question]- ¿Por qué $\binom{15}{13} = \binom{15}{2}$? ¿Cuánto vale?
> Por simetría ($15 - 13 = 2$). Vale $\frac{15 \cdot 14}{2} = 105$.

> [!question]- Usando la fila $7$ del triángulo, obtenga la fila $8$.
> $1, 8, 28, 56, 70, 56, 28, 8, 1$ (cada interior es la suma de los dos de arriba).

> [!question]- ¿Cuánto suman los números de la fila $n$?
> $2^n$: es $(1 + 1)^n$ desarrollado con el teorema del binomio.
