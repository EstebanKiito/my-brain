---
ramo: "Introducción al Cálculo"
tema: "Cálculo de límites y límites infinitos"
tags:
  - intro-calculo/limites
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Límites con el número e]]"
  - "[[04 - Cómo elegir la técnica para calcular un límite]]"
---

# Ejercicios de prueba de límites con e y límites mixtos

Preguntas de los exámenes y de las interrogaciones 7, 8 y 10 de 2020 a 2026: límites con el número $e$ y límites que combinan raíces, factoriales, logaritmos o exponenciales. La pauta puntúa por separado el paso clave (reescribir la base, acotar, racionalizar) y la conclusión.

## Ejercicios

### 1. Con el número e (I8, 2026-1; Examen, 2025-1; I7, 2025-1; Examen, 2026-1)
Calcule (a) $\left(\dfrac{3n + 1}{3n - 4}\right)^{n - 2}$, (b) $\left(\dfrac{n + 2}{n + 1}\right)^{3n}$, (c) $\left(\dfrac{n + 3}{n + 2}\right)^{5n}$ y (d) $\left(\dfrac{n^2 + 1}{3 + n^2}\right)^{n^2}$.

> [!example]- Solución
> (a) $\tfrac{3n + 1}{3n - 4} = 1 + \tfrac{5}{3n - 4} = 1 + \tfrac{1}{a_n}$ con $a_n = \tfrac{3n - 4}{5}$. El exponente es $a_n\cdot\tfrac{5(n - 2)}{3n - 4}$ y $\tfrac{5(n - 2)}{3n - 4} \to \tfrac{5}{3}$. Límite $e^{5/3}$.
> (b) $1 + \tfrac{1}{n + 1}$ con $a_n = n + 1$ y exponente $3n = 3(n + 1) - 3$: $\left[\left(1 + \tfrac{1}{n + 1}\right)^{n + 1}\right]^3\left(1 + \tfrac{1}{n + 1}\right)^{-3} \to e^3$.
> (c) $1 + \tfrac{1}{n + 2}$ con $a_n = n + 2$ y exponente $5n = 5(n + 2) - 10$: límite $e^5$.
> (d) $1 + \tfrac{-2}{3 + n^2}$ con $a_n = 3 + n^2$: $\left(1 + \tfrac{-2}{a_n}\right)^{a_n} \to e^{-2}$ y el exponente es $a_n\cdot\tfrac{n^2}{3 + n^2}$ con $\tfrac{n^2}{3 + n^2} \to 1$. Límite $e^{-2}$.

### 2. Factoriales y raíces (I8, 2026-1; Examen, 2026-1)
Calcule (a) $\lim\dfrac{n! + 3^n}{(n + 1)!}$ y (b) $\lim\dfrac{\sqrt{n^2 - n + 1} - 2n}{n + 1}$.

> [!example]- Solución
> (a) $\tfrac{n! + 3^n}{(n + 1)!} = \tfrac{1}{n + 1} + \tfrac{3^n}{(n + 1)!}$. El primer sumando tiende a $0$ y $0 < \tfrac{3^n}{(n + 1)!} \le \tfrac{3^{n+1}}{(n + 1)!} \to 0$ (límite $\tfrac{a^k}{k!} \to 0$). Resultado $0$.
> (b) Dividiendo por $n$: $\dfrac{\sqrt{1 - 1/n + 1/n^2} - 2}{1 + 1/n} \to \dfrac{1 - 2}{1} = -1$.

### 3. Raíces anidadas y un coseno (Examen, 2025-1)
Calcule (a) $\lim\left(\sqrt{n + \sqrt{n}} - \sqrt{n - \sqrt{n}}\right)$ y (b) $\lim\dfrac{3}{\sqrt{n}}\cos\!\left(\dfrac{n}{n!}\right)$.

> [!example]- Solución
> (a) Con el conjugado, $\dfrac{2\sqrt{n}}{\sqrt{n + \sqrt{n}} + \sqrt{n - \sqrt{n}}} = \dfrac{2}{\sqrt{1 + 1/\sqrt{n}} + \sqrt{1 - 1/\sqrt{n}}} \to \dfrac{2}{2} = 1$.
> (b) $-\tfrac{3}{\sqrt{n}} \le \tfrac{3}{\sqrt{n}}\cos\!\left(\tfrac{n}{n!}\right) \le \tfrac{3}{\sqrt{n}}$ y ambos extremos tienden a $0$: por el sándwich, el límite es $0$.

### 4. Una raíz $n$-ésima y un cociente de logaritmos (I10, 2020-1; Examen, 2022-2)
Calcule (a) $\lim\sqrt[n]{a^n + b^n + c^n}$ con $1 < a < b < c$ y (b) $\lim\dfrac{\ln(n + 1)}{\ln n}$.

> [!example]- Solución
> (a) $c \le \sqrt[n]{a^n + b^n + c^n} \le \sqrt[n]{3}\,c$ y $\sqrt[n]{3} \to 1$. Por sándwich, el límite es $c$.
> (b) $\dfrac{\ln(n + 1)}{\ln n} = 1 + \dfrac{\ln(1 + 1/n)}{\ln n}$; el numerador tiende a $\ln 1 = 0$ y $\ln n \to +\infty$, luego el cociente tiende a $0$ y el límite es $1$.

### 5. Un límite con logaritmo y una sucesión que diverge (Examen, 2022-1)
Si $\lim a_n = +\infty$, demuestre que $\lim\left(\sqrt{\ln(a_n + 2)} - \sqrt{\ln a_n}\right) = 0$.

> [!example]- Solución
> Se multiplica por el conjugado: $\sqrt{\ln(a_n + 2)} - \sqrt{\ln a_n} = \dfrac{\ln(a_n + 2) - \ln a_n}{\sqrt{\ln(a_n + 2)} + \sqrt{\ln a_n}} = \dfrac{\ln\!\left(1 + \tfrac{2}{a_n}\right)}{\sqrt{\ln(a_n + 2)} + \sqrt{\ln a_n}}$. El numerador tiende a $\ln 1 = 0$ (porque $\tfrac{2}{a_n} \to 0$) y el denominador tiende a $+\infty$ (porque $\ln a_n \to +\infty$). El cociente tiende a $0$.

## Preguntas de repaso

> [!question]- ¿Cómo se reconoce que una base como $\frac{3n + 1}{3n - 4}$ lleva a $e$?
> Se separa la parte entera: $\frac{3n + 1}{3n - 4} = 1 + \frac{5}{3n - 4}$. Es de la forma $1 + \frac{1}{a_n}$ con $a_n \to \infty$, y el exponente se ajusta a $a_n$ multiplicando por una sucesión convergente.

> [!question]- ¿Cuál es el truco del ejercicio 4(a)?
> Acotar por el mayor término: $c^n \le a^n + b^n + c^n \le 3c^n$, y tomar raíz $n$-ésima. Como $\sqrt[n]{3} \to 1$, el sándwich da $c$.

> [!question]- ¿Por qué en el ejercicio 3(b) no se puede usar el álgebra de límites?
> Porque $\cos\!\left(\frac{n}{n!}\right)$ no es una expresión cuyo límite se calcule directamente sin conocer el de $\frac{n}{n!}$; aquí además basta acotarlo por $1$ y usar el sándwich (el factor $\frac{3}{\sqrt{n}}$ tiende a $0$).
