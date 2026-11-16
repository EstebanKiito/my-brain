---
ramo: "Introducción al Cálculo"
tema: "Sumas finitas, binomio y aplicaciones financieras"
tags:
  - intro-calculo/sumas
  - origen/complemento
prerrequisitos:
  - "[[02 - Sumas telescópicas y geométricas en la práctica]]"
---

# El teorema del binomio y cómo hallar coeficientes

Desarrollar $(a + b)^n$ multiplicando $n$ veces es impracticable. El teorema del binomio da el desarrollo completo con una fórmula, y su uso más frecuente en las pruebas es encontrar **un coeficiente específico** sin desarrollar nada. (La teoría de los coeficientes y el triángulo de Pascal también está en [[05 - Teorema del binomio|Introducción al Álgebra]].)

## El patrón

Al desarrollar las primeras potencias:
$$(a + b)^2 = a^2 + 2ab + b^2, \quad (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3, \quad (a + b)^4 = a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4.$$
Se ven tres regularidades en $(a + b)^n$: hay $n + 1$ términos; los exponentes de $a$ bajan de $n$ a $0$ mientras los de $b$ suben de $0$ a $n$; y en cada término los exponentes suman $n$. Lo que falta son los coeficientes, que forman el **triángulo de Pascal** (cada número es la suma de los dos que tiene encima):

| $n$ | coeficientes |
|---|---|
| $0$ | $1$ |
| $1$ | $1\ \ 1$ |
| $2$ | $1\ \ 2\ \ 1$ |
| $3$ | $1\ \ 3\ \ 3\ \ 1$ |
| $4$ | $1\ \ 4\ \ 6\ \ 4\ \ 1$ |
| $5$ | $1\ \ 5\ \ 10\ \ 10\ \ 5\ \ 1$ |

## Coeficientes binomiales

> [!tip] Coeficiente binomial
> Para $0 \le k \le n$: $\dbinom{n}{k} = \dfrac{n!}{k!\,(n - k)!}$. Por ejemplo, $\dbinom{5}{2} = \dfrac{5\cdot 4}{2} = 10$, $\dbinom{n}{n} = 1$ y $\dbinom{n}{1} = n$.

Los números del triángulo de Pascal son exactamente $\binom{n}{k}$ (fila $n$, posición $k$). Dos propiedades:

> [!tip] Simetría y regla de Pascal
> 1. $\dbinom{n}{k} = \dbinom{n}{n - k}$.
> 2. $\dbinom{n}{k} + \dbinom{n}{k + 1} = \dbinom{n + 1}{k + 1}$.

La simetría es inmediata de la fórmula. Para la regla de Pascal se suma con denominador común:
$$\frac{n!}{k!(n - k)!} + \frac{n!}{(k + 1)!(n - k - 1)!} = \frac{n!\,[(k + 1) + (n - k)]}{(k + 1)!(n - k)!} = \frac{(n + 1)!}{(k + 1)!(n - k)!}.$$

## El teorema

> [!tip] Teorema del binomio (Newton)
> Para $a, b \in \mathbb{R}$ y $n \in \mathbb{N}$:
> $$(a + b)^n = \sum_{k=0}^{n}\binom{n}{k}\,a^{n-k}\,b^{k}.$$

Se demuestra por **inducción** sobre $n$. Para $n = 1$ ambos lados son $a + b$. Para el paso, se multiplica $(a + b)^n$ por $(a + b)$, se separan las dos sumas resultantes, se reindexa una y se agrupan los términos de igual potencia con la regla de Pascal.

**Dos corolarios** (con $a = b = 1$ y con $a = 1$, $b = -1$): $\displaystyle\sum_{k=0}^{n}\binom{n}{k} = 2^n$ y $\displaystyle\sum_{k=0}^{n}(-1)^k\binom{n}{k} = 0$.

## Desarrollar y hallar el término general

**Desarrollo completo (clase 20): $\left(y^2 + \tfrac{1}{y}\right)^6$.** El término general es $\binom{6}{k}(y^2)^{6-k}y^{-k} = \binom{6}{k}y^{12-3k}$:
$$y^{12} + 6y^9 + 15y^6 + 20y^3 + 15 + 6y^{-3} + y^{-6}.$$

> [!tip] Método para un coeficiente
> 1. Escribir el **término general** $\binom{n}{k}a^{n-k}b^k$ y simplificar la potencia de $x$ en función de $k$.
> 2. Igualar el exponente al que se pide y **despejar $k$** (debe resultar un entero entre $0$ y $n$).
> 3. Evaluar el coeficiente $\binom{n}{k}\cdot(\text{constantes})$.

**$x^{n}$ en $(1 + x)^{2n}$ (clase 20, Examen 2022-2).** El término general es $\binom{2n}{k}x^k$, así que el exponente $n$ ocurre en $k = n$: el coeficiente es $\binom{2n}{n} = \dfrac{(2n)!}{n!\,n!}$.

**$x^{20}$ en $\left(x^3 - \tfrac{2}{x^2}\right)^{10}$ (I7, 2024-1).** El término general es $\binom{10}{k}(x^3)^{10-k}\left(-\tfrac{2}{x^2}\right)^k = \binom{10}{k}(-2)^k x^{30-5k}$. Se pide $30 - 5k = 20$, es decir $k = 2$: $\binom{10}{2}(-2)^2 = 45 \cdot 4 = 180$.

**$x^2$ en $\left(\tfrac{x^3 + 1}{x}\right)^{10}$ (Examen, 2024-1).** Es $\left(x^2 + \tfrac{1}{x}\right)^{10}$, con término general $\binom{10}{k}x^{2(10-k)}x^{-k} = \binom{10}{k}x^{20-3k}$. Con $20 - 3k = 2$, $k = 6$ y el coeficiente es $\binom{10}{6} = 210$.

**Un término con dos variables (I7, 2022-1).** En $\left(xy + \tfrac{2}{x^2y}\right)^{13}$ el término general es $\binom{13}{k}2^k x^{13-3k}y^{13-2k}$. Para $\tfrac{y^3}{x^2}$ se pide $13 - 3k = -2$ y $13 - 2k = 3$: ambas dan $k = 5$, y el coeficiente es $\binom{13}{5}2^5$.

**Un trinomio (clase 20): coeficiente de $\tfrac{1}{x^{31}}$ en $\left(x - 1 + \tfrac{1}{x^2}\right)^{20}$.** Se escribe $x - 1 + \tfrac{1}{x^2} = \tfrac{1}{x^2}\big(x^3 + (1 - x^2)\big)$, y entonces
$$\left(x - 1 + \tfrac{1}{x^2}\right)^{20} = \frac{1}{x^{40}}\sum_{k=0}^{20}\binom{20}{k}x^{3(20-k)}(1 - x^2)^k = \sum_{k=0}^{20}\sum_{\ell=0}^{k}\binom{20}{k}\binom{k}{\ell}(-1)^{\ell}x^{20-3k+2\ell}.$$
Se busca $20 - 3k + 2\ell = -31$, es decir $\ell = \tfrac{3k - 51}{2} \ge 0$ con $\ell \le k \le 20$: las únicas parejas son $(k, \ell) = (17, 0)$ y $(19, 3)$. El coeficiente es $\binom{20}{17} - \binom{20}{19}\binom{19}{3} = 1140 - 20\cdot 969 = -18240$.

## Sumas con coeficientes binomiales

Usando el teorema con valores especiales:

- $\displaystyle\sum_{k=0}^{n}\binom{n}{k}\frac{1}{2^k} = \left(1 + \tfrac{1}{2}\right)^n = \left(\tfrac{3}{2}\right)^n$ (I7, 2020-1).
- $\displaystyle\sum_{k=1}^{n}k\binom{n}{k} = n\,2^{n-1}$ (I3, 2023-2 y Guía 9): como $k\binom{n}{k} = n\binom{n-1}{k-1}$, la suma es $n\sum_{j=0}^{n-1}\binom{n-1}{j} = n\,2^{n-1}$.
- $\displaystyle\sum_{k=0}^{n}\frac{1}{k + 1}\binom{n}{k}x^k = \frac{(1 + x)^{n+1} - 1}{(n + 1)x}$ (I7, 2023-1): se usa $\tfrac{1}{k + 1}\binom{n}{k} = \tfrac{1}{n + 1}\binom{n + 1}{k + 1}$ y se aplica el teorema a $(1 + x)^{n+1}$ restando el término $k = 0$.

> [!warning] Errores frecuentes
> - Olvidar que $b^k$ incluye el **signo** y las constantes: en $(x^3 - 2/x^2)^{10}$ el factor es $(-2)^k$.
> - No reducir la potencia total de $x$ antes de buscar $k$.
> - Aceptar un $k$ no entero o fuera de $[0, n]$: entonces ese término no existe y el coeficiente es $0$.

## Preguntas de repaso

> [!question]- ¿Cuántos términos tiene $(a + b)^{12}$ y cuál es el coeficiente de $a^{10}b^2$?
> Tiene $13$ términos; el coeficiente es $\binom{12}{2} = 66$.

> [!question]- ¿Por qué $\sum_{k=0}^{n}\binom{n}{k} = 2^n$?
> Es el teorema del binomio con $a = b = 1$: $(1 + 1)^n$.

> [!question]- ¿Cuál es el sexto término del desarrollo de $(x + y)^{15}$?
> El término con $k = 5$: $\binom{15}{5}x^{10}y^5 = 3003\,x^{10}y^5$.

> [!question]- ¿Qué se concluye si al igualar exponentes sale $k = 2{,}5$?
> Que el término buscado no aparece en el desarrollo: su coeficiente es $0$.
