---
ramo: "Introducción al Álgebra"
tema: "Sumatorias, progresiones y binomio"
tags:
  - intro-algebra/sumatorias-binomio
  - origen/complemento
prerrequisitos:
  - "[[04 - Coeficientes binomiales y triángulo de Pascal]]"
---

# Teorema del binomio

Desarrollar $(a + b)^n$ multiplicando $n$ veces es impracticable para $n$ grande. El teorema del binomio da el desarrollo completo de una vez, y, sobre todo, permite encontrar **un término específico** (el que tiene $x^5$, o el que no tiene $x$) sin escribir los demás.

## El teorema

> [!tip] Teorema del binomio
> Para $a, b \in \mathbb{R}$ y $n \in \mathbb{N}$:
> $$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k.$$

Se prueba por inducción sobre $n$, usando la regla de Pascal para juntar los coeficientes en el paso inductivo. Para $n = 3$ da $a^3 + 3a^2 b + 3ab^2 + b^3$, con los coeficientes de la fila $3$ del triángulo.

Casos particulares útiles:
- $(a - b)^n = \sum_{k=0}^{n} \binom{n}{k} (-1)^k a^{n-k} b^k$ (los signos alternan).
- $\sum_{k=0}^{n} \binom{n}{k} = (1+1)^n = 2^n$ y $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = (1-1)^n = 0$.

## Encontrar un término específico

En $(a + b)^n$ el término con índice $k$ es $\binom{n}{k} a^{n-k} b^k$. Para buscar el que tiene cierta potencia de $x$:

1. Escribir el término general y juntar todas las potencias de $x$ en una sola, $x^{e(k)}$.
2. Plantear $e(k) = $ la potencia buscada ($0$ si se busca el término independiente) y despejar $k$.
3. Si $k$ no es un entero entre $0$ y $n$, ese término **no existe**.

**Ejemplo.** Término independiente de $\left(x + \frac{a}{x^2}\right)^9$. El término general es
$$\binom{9}{k} x^{9-k} \left(\frac{a}{x^2}\right)^k = \binom{9}{k} a^k x^{9-3k}.$$
Se pide $9 - 3k = 0$, es decir, $k = 3$, y el término es $\binom{9}{3} a^3 = 84a^3$.

> [!warning] Las potencias negativas de $x$ cuentan
> En $\left(\frac{a}{x^2}\right)^k$ el exponente de $x$ es $-2k$, no $2k$. Juntar mal los exponentes es el error más frecuente. Otro error típico es olvidar elevar también la constante: $\left(\frac{a}{x^2}\right)^k = \frac{a^k}{x^{2k}}$.

## Producto de un polinomio por un binomio

Si la expresión es $(x^3 + 1)\left(x + \frac{a}{x^2}\right)^9$, el término independiente recibe aportes de **cada** sumando del primer factor:
- de $x^3 \cdot \binom{9}{k} a^k x^{9-3k}$, cuando $12 - 3k = 0$, o sea $k = 4$: aporta $\binom{9}{4} a^4 = 126a^4$;
- de $1 \cdot \binom{9}{k} a^k x^{9-3k}$, cuando $k = 3$: aporta $84a^3$.

Total: $126a^4 + 84a^3 = 42a^3(3a + 2)$. Si se pregunta cuándo el desarrollo **no** tiene término independiente (es decir, cuando es $0$), la respuesta es $a = 0$ o $a = -\frac{2}{3}$.

## Preguntas de repaso

> [!question]- ¿Cuántos términos tiene el desarrollo de $(a + b)^n$?
> $n + 1$, uno por cada $k = 0, 1, \dots, n$.

> [!question]- Halle el coeficiente de $x^2$ en $(1 + 2x)^5$.
> Término general $\binom{5}{k} 2^k x^k$; con $k = 2$: $\binom{5}{2} \cdot 4 = 40$.

> [!question]- ¿Tiene término independiente $\left(x^2 + \frac{1}{x}\right)^7$?
> El término general tiene $x^{14 - 3k}$; $14 - 3k = 0$ da $k = \frac{14}{3}$, que no es entero. No tiene.

> [!question]- ¿Cuánto vale $\binom{6}{0} - \binom{6}{1} + \binom{6}{2} - \dots + \binom{6}{6}$?
> $(1 - 1)^6 = 0$.
