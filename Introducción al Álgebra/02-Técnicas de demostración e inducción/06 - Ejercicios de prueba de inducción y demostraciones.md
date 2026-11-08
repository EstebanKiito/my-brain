---
ramo: "Introducción al Álgebra"
tema: "Técnicas de demostración e inducción"
tags:
  - intro-algebra/tecnicas-demostracion
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Plantilla de inducción y cambio de caso base]]"
---

# Ejercicios de prueba de inducción y demostraciones

Preguntas de la guía del curso y de tareas anteriores sobre inducción: divisibilidad, sumas, series geométricas, recurrencias y sumas que se colapsan. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Divisibilidad por inducción
Pruebe que $n^3 - n$ es divisible por $3$ para todo $n \in \mathbb{N}$.

> [!example]- Solución
> **Caso base** ($n=1$): $1^3 - 1 = 0$, divisible por $3$.
> **Paso inductivo:** supongamos $k^3 - k = 3m$. Entonces
> $$(k+1)^3 - (k+1) = k^3 + 3k^2 + 3k + 1 - k - 1 = (k^3 - k) + 3k^2 + 3k = 3m + 3(k^2 + k) = 3(m + k^2 + k),$$
> que es divisible por $3$.

### 2. Otra divisibilidad
Pruebe que $n^3 + 2n$ es divisible por $3$ para todo $n \in \mathbb{N}$.

> [!example]- Solución
> **Caso base** ($n=1$): $1 + 2 = 3$.
> **Paso inductivo:** supongamos $k^3 + 2k = 3m$. Entonces
> $$(k+1)^3 + 2(k+1) = k^3 + 3k^2 + 3k + 1 + 2k + 2 = (k^3 + 2k) + 3k^2 + 3k + 3 = 3(m + k^2 + k + 1).$$

### 3. Suma telescópica
Demuestre que $\displaystyle\frac{1}{1\cdot 2} + \frac{1}{2\cdot 3} + \dots + \frac{1}{n(n+1)} = \frac{n}{n+1}$ para todo $n \in \mathbb{N}$.

> [!example]- Solución
> **Caso base** ($n=1$): $\frac{1}{1\cdot 2} = \frac{1}{2} = \frac{1}{1+1}$.
> **Paso inductivo:** supongamos la igualdad para $k$ y sumemos $\frac{1}{(k+1)(k+2)}$:
> $$\frac{k}{k+1} + \frac{1}{(k+1)(k+2)} = \frac{k(k+2)+1}{(k+1)(k+2)} = \frac{k^2+2k+1}{(k+1)(k+2)} = \frac{(k+1)^2}{(k+1)(k+2)} = \frac{k+1}{k+2}.$$

### 4. Serie geométrica
Pruebe que para $x \neq 1$ y todo entero $n \ge 0$, $\displaystyle\sum_{k=0}^{n} x^k = \frac{1 - x^{n+1}}{1 - x}$.

> [!example]- Solución
> **Caso base** ($n=0$): $\sum_{k=0}^{0} x^k = 1 = \frac{1-x}{1-x}$.
> **Paso inductivo:** supongamos $\sum_{k=0}^{m} x^k = \frac{1-x^{m+1}}{1-x}$. Sumando $x^{m+1}$:
> $$\frac{1-x^{m+1}}{1-x} + x^{m+1} = \frac{1-x^{m+1} + x^{m+1}(1-x)}{1-x} = \frac{1-x^{m+1}+x^{m+1}-x^{m+2}}{1-x} = \frac{1-x^{m+2}}{1-x}.$$

### 5. Suma de cuadrados impares
Demuestre que $1^2 + 3^2 + 5^2 + \dots + (2n-1)^2 = \dfrac{n(2n-1)(2n+1)}{3}$ para todo $n \in \mathbb{N}$.

> [!example]- Solución
> **Caso base** ($n=1$): $1^2 = 1 = \frac{1\cdot 1\cdot 3}{3}$.
> **Paso inductivo:** supongamos la fórmula para $k$ y sumemos $(2(k+1)-1)^2 = (2k+1)^2$:
> $$\frac{k(2k-1)(2k+1)}{3} + (2k+1)^2 = (2k+1)\left[\frac{k(2k-1)}{3} + (2k+1)\right] = (2k+1)\frac{2k^2+5k+3}{3} = \frac{(2k+1)(2k+3)(k+1)}{3},$$
> que es $\frac{(k+1)(2(k+1)-1)(2(k+1)+1)}{3}$.

### 6. Una suma que se colapsa
Sea $x \in \mathbb{R}\setminus\{1, -1\}$. Demuestre que para todo $n \in \mathbb{N}$,
$$\sum_{j=1}^{n} \frac{2^j}{1+x^{2^j}} = \frac{2}{x^2-1} + \frac{2^{n+1}}{1-x^{2^{n+1}}}.$$

> [!example]- Solución
> **Caso base** ($n=1$): el lado izquierdo es $\frac{2}{1+x^2}$ y el derecho $\frac{2}{x^2-1} + \frac{4}{1-x^4}$. Como $\frac{4}{1-x^4} = \frac{4}{(1-x^2)(1+x^2)}$, sumando con $\frac{2}{x^2-1} = \frac{-2}{1-x^2}$ se obtiene $\frac{2}{1+x^2}$.
> **Paso inductivo:** supongamos la fórmula para $n$ y sumemos el término siguiente:
> $$S_{n+1} = \frac{2}{x^2-1} + \frac{2^{n+1}}{1-x^{2^{n+1}}} + \frac{2^{n+1}}{1+x^{2^{n+1}}}.$$
> Los dos últimos términos se combinan, pues $\frac{1}{1-y} + \frac{1}{1+y} = \frac{2}{1-y^2}$ con $y = x^{2^{n+1}}$:
> $$S_{n+1} = \frac{2}{x^2-1} + 2^{n+1}\cdot\frac{2}{1-x^{2^{n+2}}} = \frac{2}{x^2-1} + \frac{2^{n+2}}{1-x^{2^{n+2}}},$$
> que es la fórmula con $n+1$.

## Preguntas de repaso

> [!question]- ¿Qué tienen en común los ejercicios 1 y 2?
> Ambos son divisibilidad: en el paso inductivo se expande $(k+1)^3$ y se separa el término $k^3$ (que es divisible por hipótesis) del resto, que queda múltiplo de $3$ explícitamente.

> [!question]- ¿Por qué la suma del ejercicio 3 se llama "telescópica"?
> Porque cada término $\frac{1}{k(k+1)}$ se puede escribir como $\frac1k - \frac1{k+1}$, y al sumar, los términos intermedios se cancelan dejando solo $1 - \frac{1}{n+1} = \frac{n}{n+1}$.

> [!question]- En el ejercicio 6, ¿qué identidad permite combinar los dos últimos términos del paso inductivo?
> La diferencia de cuadrados: $(1-y)(1+y) = 1-y^2$, con $y = x^{2^{n+1}}$, que convierte la suma de las dos fracciones en $2/(1-x^{2^{n+2}})$.
