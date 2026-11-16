---
ramo: "Introducción al Cálculo"
tema: "Sumas finitas, binomio y aplicaciones financieras"
tags:
  - intro-calculo/sumas
  - origen/complemento
prerrequisitos:
  - "[[01 - Sucesiones y formas de definirlas]]"
---

# Notación sigma y sumas de potencias

Sumar los primeros $n$ términos de una sucesión es tan frecuente que tiene su propio símbolo. La notación sigma permite escribir sumas largas en una línea y manipularlas con reglas simples; y unas pocas sumas "conocidas" resuelven la mayoría de los ejercicios. (La misma materia, con un enfoque más formal, está en [[01 - Sumatorias y sus propiedades|Introducción al Álgebra]].)

## La notación

> [!tip] Suma de los primeros términos
> $\displaystyle \sum_{k=1}^{n} a_k = a_1 + a_2 + \dots + a_n$, donde $k$ es un contador (índice) que recorre $1, 2, \ldots, n$. Se lee "la suma de $a_k$ de $k = 1$ a $k = n$". El índice es **mudo**: $\sum_{k=1}^{n} a_k = \sum_{j=1}^{n} a_j$.

Los límites pueden ser otros, y cada paso suma un término:

- $\displaystyle \sum_{k=1}^{5} k^2 = 1 + 4 + 9 + 16 + 25 = 55$.
- $\displaystyle \sum_{j=3}^{5} \frac{1}{j} = \frac{1}{3} + \frac{1}{4} + \frac{1}{5} = \frac{47}{60}$.
- $\displaystyle \sum_{i=5}^{10} i = 5 + 6 + 7 + 8 + 9 + 10 = 45$.
- $\displaystyle \sum_{i=1}^{6} 2 = 12$ (una constante se suma $6$ veces).

**Del otro lado: escribir con sigma.** $1^3 + 2^3 + \dots + 7^3 = \sum_{k=1}^{7} k^3$, y $\sqrt{3} + \sqrt{4} + \dots + \sqrt{77} = \sum_{k=3}^{77} \sqrt{k}$.

## Reglas

> [!tip] Linealidad
> Para una constante $c$:
> 1. $\sum_{k=1}^{n} a_k + \sum_{k=1}^{n} b_k = \sum_{k=1}^{n}(a_k + b_k)$.
> 2. $\sum_{k=1}^{n} c\,a_k = c \sum_{k=1}^{n} a_k$.
> 3. $\left(\sum_{k=1}^{n} a_k\right)\left(\sum_{\ell=1}^{m} b_\ell\right) = \sum_{k=1}^{n}\sum_{\ell=1}^{m} a_k b_\ell$ (distributividad).

Además, una suma que no parte en $1$ se calcula como una diferencia: $\sum_{k=m}^{n} a_k = \sum_{k=1}^{n} a_k - \sum_{k=1}^{m-1} a_k$.

> [!warning] Lo que la suma **no** respeta
> $\sum a_k b_k \neq \left(\sum a_k\right)\left(\sum b_k\right)$ y $\sum \tfrac{1}{a_k} \neq \tfrac{1}{\sum a_k}$. Y $\sum_{k=1}^{n} c = nc$, no $c$.

## La caja de herramientas

> [!tip] Sumas conocidas
> 1. $\sum_{k=1}^{n} c = nc$.
> 2. $\sum_{k=1}^{n} k = \dfrac{n(n + 1)}{2}$.
> 3. $\sum_{k=1}^{n} k^2 = \dfrac{n(n + 1)(2n + 1)}{6}$.
> 4. $\sum_{k=1}^{n} k^3 = \left(\dfrac{n(n + 1)}{2}\right)^2$.
> 5. Telescópica: $\sum_{k=m}^{n}(a_k - a_{k+1}) = a_m - a_{n+1}$.
> 6. Geométrica: $\sum_{k=0}^{n} r^k = \dfrac{1 - r^{n+1}}{1 - r}$, $r \neq 1$.

Las fórmulas 2 a 4 se prueban por inducción. Cuando una suma de $n$ términos se expresa con una fórmula simple en $n$, se dice que está en **forma cerrada**. Hay sumas que no la tienen: $1 + \tfrac{1}{2} + \dots + \tfrac{1}{n} = \sum_{k=1}^{n}\tfrac{1}{k}$ no admite una expresión simple.

## Ejemplos

**Múltiplos de $3$ menores que $100$ (Guía 9).** Son $3, 6, \ldots, 99$, es decir $3k$ con $k = 1, \ldots, 33$: $\sum_{k=1}^{33} 3k = 3\cdot\tfrac{33 \cdot 34}{2} = 1683$.

**Suma con un término alterno.** $\displaystyle\sum_{k=1}^{n}(-1)^k\, 2k^2 = (-1)^n n(n + 1)$. Se comprueba para $n = 1$: $-2$; $n = 2$: $-2 + 8 = 6$; $n = 3$: $6 - 18 = -12$. Se demuestra por inducción: $(-1)^n n(n + 1) + (-1)^{n+1}2(n + 1)^2 = (-1)^{n+1}(n + 1)\big[2(n + 1) - n\big] = (-1)^{n+1}(n + 1)(n + 2)$.

**Suma de pares.** $2 + 4 + \dots + 20 = 2(1 + 2 + \dots + 10) = 2 \cdot 55 = 110$.

## Preguntas de repaso

> [!question]- ¿Cuánto vale $\sum_{k=1}^{10}(2k + 1)$?
> $2 \cdot 55 + 10 = 120$, usando linealidad, $\sum k = 55$ y $\sum 1 = 10$.

> [!question]- ¿Cómo se calcula $\sum_{k=5}^{20} k$ con la caja de herramientas?
> Como $\sum_{k=1}^{20} k - \sum_{k=1}^{4} k = 210 - 10 = 200$.

> [!question]- ¿Es cierto que $\sum_{k=1}^{n} k^2 = \left(\sum_{k=1}^{n} k\right)^2$?
> No: para $n = 2$ da $1 + 4 = 5$ frente a $3^2 = 9$. (Lo que sí vale es la igualdad con los **cubos**.)

> [!question]- ¿Qué es una forma cerrada?
> Una expresión simple en $n$ para una suma de $n$ términos, como $\frac{n(n+1)}{2}$ para $1 + 2 + \dots + n$.
