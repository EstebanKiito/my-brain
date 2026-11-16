---
ramo: "Introducción al Cálculo"
tema: "Sumas finitas, binomio y aplicaciones financieras"
tags:
  - intro-calculo/sumas
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - El teorema del binomio y cómo hallar coeficientes]]"
  - "[[02 - Sumas telescópicas y geométricas en la práctica]]"
---

# Ejercicios de prueba de sumas, progresiones y binomio

Preguntas de la interrogación 7 y de los exámenes de 2020 a 2024. La interrogación 7 trae casi siempre tres problemas: un coeficiente del binomio, una suma que se resuelve de forma telescópica o geométrica y un problema de progresiones. La pauta puntúa por separado cada paso de la reducción.

## Ejercicios

### 1. Coeficientes del binomio (I7, 2024-1; I7, 2022-1; I7, 2020-1)
Halle (a) el coeficiente de $x^{20}$ en $\left(x^3 - \tfrac{2}{x^2}\right)^{10}$; (b) el coeficiente de $\tfrac{y^3}{x^2}$ en $\left(xy + \tfrac{2}{x^2y}\right)^{13}$; (c) el coeficiente de $x^{13}$ en $\left(x^2 + \tfrac{1}{x}\right)^{17}$.

> [!example]- Solución
> (a) Término general $\binom{10}{k}(-2)^k x^{30-5k}$. Con $30 - 5k = 20$, $k = 2$: $\binom{10}{2}\cdot 4 = 180$.
> (b) Término general $\binom{13}{k}2^k x^{13-3k}y^{13-2k}$. Se pide $13 - 3k = -2$ y $13 - 2k = 3$: ambas dan $k = 5$. Coeficiente $\binom{13}{5}\,2^5$.
> (c) Término general $\binom{17}{k}(x^{-1})^k(x^2)^{17-k} = \binom{17}{k}x^{34-3k}$. Con $34 - 3k = 13$, $k = 7$: coeficiente $\binom{17}{7}$.

### 2. Coeficientes en los exámenes (Examen, 2022-2 y 2024-1)
Halle (a) el coeficiente de $x^n$ en $(1 + x)^{2n}$; (b) el coeficiente de $x^2$ en $\left(\dfrac{x^3 + 1}{x}\right)^{10}$.

> [!example]- Solución
> (a) El término general es $\binom{2n}{k}x^k$; $x^n$ aparece con $k = n$: coeficiente $\binom{2n}{n} = \tfrac{(2n)!}{n!\,n!}$.
> (b) Es $\left(x^2 + \tfrac{1}{x}\right)^{10}$ y el término general es $\binom{10}{k}x^{20-3k}$. Con $20 - 3k = 2$, $k = 6$: coeficiente $\binom{10}{6} = 210$.

### 3. Una suma con binomio (I7, 2020-1; I3, 2023-2)
Calcule (a) $\sum_{k=0}^{n}\binom{n}{k}\tfrac{1}{2^k}$ y (b) $\sum_{k=1}^{n}k\binom{n}{k}$.

> [!example]- Solución
> (a) Es $\sum_{k=0}^{n}\binom{n}{k}1^{n-k}\left(\tfrac{1}{2}\right)^k = \left(1 + \tfrac{1}{2}\right)^n = \left(\tfrac{3}{2}\right)^n$.
> (b) $k\binom{n}{k} = \tfrac{n!}{(k-1)!(n-k)!} = n\binom{n-1}{k-1}$, de modo que la suma es $n\sum_{j=0}^{n-1}\binom{n-1}{j} = n\,2^{n-1}$.

### 4. El binomio y una suma con $\tfrac{1}{k + 1}$ (I7, 2023-1)
Use el teorema del binomio para mostrar que, para $x \neq 0$, $\dfrac{(1 + x)^{n+1} - 1}{(n + 1)x} = \sum_{k=0}^{n}\dfrac{1}{k + 1}\binom{n}{k}x^k$. (Sugerencia: $\binom{n+1}{k+1} = \tfrac{n+1}{k+1}\binom{n}{k}$.)

> [!example]- Solución
> $(1 + x)^{n+1} - 1 = \sum_{j=1}^{n+1}\binom{n+1}{j}x^j = \sum_{k=0}^{n}\binom{n+1}{k+1}x^{k+1}$ (se quitó el término $j = 0$ y se reindexó con $j = k + 1$). Usando $\binom{n+1}{k+1} = \tfrac{n+1}{k+1}\binom{n}{k}$:
> $$(1 + x)^{n+1} - 1 = (n + 1)\,x\sum_{k=0}^{n}\frac{1}{k + 1}\binom{n}{k}x^k,$$
> y se divide por $(n + 1)x$.

### 5. Sumas telescópicas (I7, 2023-1; Examen, 2023-1)
Calcule (a) $\sum_{k=1}^{n}(k^2 + 1)\,k!$ (sugerencia: $(k^2 + 1)k! = k(k + 1)! - (k - 1)k!$) y (b) $\sum_{k=1}^{n}\ln\!\left(1 + \tfrac{1}{k}\right)$.

> [!example]- Solución
> (a) Se verifica la sugerencia: $k(k + 1)! - (k - 1)k! = [k(k + 1) - (k - 1)]k! = (k^2 + 1)k!$. Con $a_k = (k - 1)k!$ la suma es $\sum(a_{k+1} - a_k) = a_{n+1} - a_1 = n(n + 1)! - 0 = n(n + 1)!$.
> (b) $\ln\!\left(1 + \tfrac{1}{k}\right) = \ln(k + 1) - \ln k$; con $c_k = \ln k$ la suma es $c_{n+1} - c_1 = \ln(n + 1)$.

### 6. Una suma geométrica (Examen, 2022-2)
Calcule $\sum_{k=1}^{n}\dfrac{3^{k+1}}{4^k}$.

> [!example]- Solución
> $\sum_{k=1}^{n}\tfrac{3^{k+1}}{4^k} = 3\sum_{k=1}^{n}\left(\tfrac{3}{4}\right)^k = 3\left[\tfrac{1 - (3/4)^{n+1}}{1 - 3/4} - 1\right] = 3\left[4 - 4\left(\tfrac{3}{4}\right)^{n+1} - 1\right] = 9 - 12\left(\tfrac{3}{4}\right)^{n+1}$.

### 7. Una aritmética y una geométrica (I7, 2023-1; I3, 2023-2)
(a) $\{a_n\}$ es geométrica con $a_1 = a$, $a_2 = 10$, $a_3 = c$ y $\{b_n\}$ es aritmética con $b_1 = a - 1$, $b_2 = 8$, $b_3 = c - 8$. Halle $a$ y $c$. (b) El primer, segundo y último término de una progresión aritmética son $5$, $9$ y $101$. ¿Cuántos términos tiene?

> [!example]- Solución
> (a) Geométrica: $\tfrac{10}{a} = \tfrac{c}{10}$, es decir $ac = 100$. Aritmética: $8 - (a - 1) = (c - 8) - 8$, es decir $a + c = 25$. Entonces $a^2 - 25a + 100 = 0$ y $(a, c) = (20, 5)$ ó $(5, 20)$. (La pauta escribe "$b = 20$" en el segundo caso: es $c = 20$.)
> (b) La diferencia es $d = 9 - 5 = 4$ y $5 + (m - 1)\cdot 4 = 101$ da $m = 25$.

## Preguntas de repaso

> [!question]- ¿Cómo se sabe que en el ejercicio 1(b) hay un solo valor de $k$ posible?
> Porque las dos condiciones (potencias de $x$ y de $y$) dan la misma ecuación para $k$: $13 - 3k = -2$ y $13 - 2k = 3$ coinciden en $k = 5$. Si fueran incompatibles el coeficiente sería $0$.

> [!question]- ¿Qué parte de una suma indica que es telescópica?
> Que el término general se pueda escribir como una diferencia $a_{k+1} - a_k$; con factoriales y logaritmos, suele ser $(k+1)! - k!$ o $\ln(k+1) - \ln k$.

> [!question]- ¿Por qué se resta $1$ en el ejercicio 6?
> Porque la suma geométrica estándar parte en $k = 0$, y el término $k = 0$ ($=1$) no está en la suma original.
