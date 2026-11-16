---
ramo: "Introducción al Cálculo"
tema: "Cálculo de límites y límites infinitos"
tags:
  - intro-calculo/limites
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[01 - Sucesiones recursivas y límite por punto fijo]]"
  - "[[03 - Límites con el número e]]"
---

# Ejercicios de la guía de recurrencias y límites con e

Cierra la Guía 10: el cálculo del **límite** de los ejercicios 1, 2, 6 y 12 (cuya monotonía y cota están en [[05 - Ejercicios de la guía de sucesiones acotadas y monótonas|el tema 08]]) y los ejercicios 8 y 13, que usan el número $e$.

## Ejercicios

### 1. Un producto de fracciones (límite)
$a_n = \dfrac{1\cdot 3\cdot 5\cdots(2n - 1)}{2\cdot 4\cdot 6\cdots 2n}$: acote su límite y calcúlelo.

> [!example]- Solución
> Es decreciente y positiva, luego converge a un $L$ con $0 \le L \le a_1 = \tfrac{1}{2}$. Para calcularlo: $a_n^2 = \prod_{k=1}^{n}\left(\tfrac{2k - 1}{2k}\right)^2 \le \prod_{k=1}^{n}\tfrac{2k - 1}{2k + 1} = \tfrac{1}{2n + 1}$, porque $\tfrac{(2k - 1)^2}{4k^2} \le \tfrac{2k - 1}{2k + 1} \iff (2k - 1)(2k + 1) \le 4k^2$ (cierto). Entonces $0 < a_n \le \tfrac{1}{\sqrt{2n + 1}} \to 0$ y, por sándwich, $L = 0$.

### 2. La recurrencia $\tfrac{a_n + 6}{2}$ (límite)
$a_1 = 2$, $a_{n+1} = \tfrac{a_n + 6}{2}$.

> [!example]- Solución
> Creciente y acotada por $6$, converge. Con $L = \tfrac{L + 6}{2}$ resulta $L = 6$.

### 6. La recurrencia $\sqrt{2 + a_n}$ (límite)
$a_1 = \sqrt{2}$, $a_{n+1} = \sqrt{2 + a_n}$.

> [!example]- Solución
> Creciente y acotada por $2$. Con $L = \sqrt{2 + L}$ y $L > 0$: $L^2 - L - 2 = 0$, $L = 2$.

### 8. Una sucesión con $e$
Decida la convergencia de $a_n = \left(\dfrac{n + 1}{n}\right)^n$.

> [!example]- Solución
> $a_n = \left(1 + \tfrac{1}{n}\right)^n$ converge a $e$ por definición.

### 12. Raíz menos $n$ (límite)
$a_n = \sqrt{n^2 + n} - n$.

> [!example]- Solución
> $a_n = \dfrac{n}{\sqrt{n^2 + n} + n} = \dfrac{1}{\sqrt{1 + 1/n} + 1}$ es creciente y menor que $\tfrac{1}{2}$. Su límite es $\dfrac{1}{1 + 1} = \dfrac{1}{2}$.

### 13. Tres límites con $e$
Calcule (a) $\lim\left(1 + \tfrac{1}{2n}\right)^n$, (b) $\lim\left(1 + \tfrac{1}{n + 1}\right)^{4n}$ y (c) $\lim\left(\dfrac{n^2 + 2n + 3}{n^2 + 2n + 1}\right)^{(n+1)^2}$.

> [!example]- Solución
> (a) $\left[\left(1 + \tfrac{1}{2n}\right)^{2n}\right]^{1/2} \to e^{1/2} = \sqrt{e}$.
> (b) Con $a_n = n + 1$: $\left[\left(1 + \tfrac{1}{n + 1}\right)^{n + 1}\right]^{4n/(n + 1)} \to e^4$, pues $\tfrac{4n}{n + 1} \to 4$.
> (c) La base es $1 + \tfrac{2}{(n + 1)^2}$. Con $a_n = \tfrac{(n + 1)^2}{2}$ el exponente es $2a_n$ y el límite es $\left[\left(1 + \tfrac{1}{a_n}\right)^{a_n}\right]^2 \to e^2$.

## Preguntas de repaso

> [!question]- ¿Por qué el límite del ejercicio 1 es $0$ y no un valor positivo?
> Porque $a_n^2 \le \frac{1}{2n + 1} \to 0$: los factores $\frac{2k - 1}{2k}$ son menores que $1$ y su producto se hace arbitrariamente pequeño.

> [!question]- ¿Cómo se ve que $\left(1 + \frac{1}{2n}\right)^n \to \sqrt{e}$?
> Es la raíz cuadrada de $\left(1 + \frac{1}{2n}\right)^{2n}$, que tiende a $e$ (con $a_n = 2n \to \infty$).

> [!question]- ¿Qué tienen en común los ejercicios 2 y 6?
> Ambas recurrencias son crecientes y acotadas, y su límite se obtiene de la ecuación del punto fijo, descartando la raíz que no cabe en las cotas.
