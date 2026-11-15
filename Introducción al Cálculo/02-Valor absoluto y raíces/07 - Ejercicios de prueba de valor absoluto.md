---
ramo: "Introducción al Cálculo"
tema: "Valor absoluto y raíces"
tags:
  - intro-calculo/valor-absoluto
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Ecuaciones con valor absoluto]]"
  - "[[05 - Raíces cuadradas y valor absoluto]]"
---

# Ejercicios de prueba de valor absoluto

Preguntas de interrogaciones de 2020 a 2026 y de la lista de ejercicios del curso. Aparecen tres tipos: ecuaciones con valor absoluto (donde la pauta puntúa por separado los casos y el descarte de soluciones falsas), desigualdades que se resuelven con la triangular, y demostraciones de propiedades.

## Ejercicios

### 1. Simplificar y resolver (I2, 2025-1)
(a) Si $0 < x < 1$, determine el valor de $\dfrac{|4x + 1| - |x - 1|}{x}$. (b) Resuelva $|2x + 2| = 6x - 18$.

> [!example]- Solución
> (a) Para $x \in (0, 1)$: $4x + 1 > 0$, así que $|4x + 1| = 4x + 1$; y $x - 1 < 0$, así que $|x - 1| = 1 - x$. El cociente es $\tfrac{(4x + 1) - (1 - x)}{x} = \tfrac{5x}{x} = 5$.
> (b) Se exige $6x - 18 \ge 0$, es decir $x \ge 3$. Luego $2x + 2 = 6x - 18$ da $x = 5$, y $2x + 2 = -(6x - 18)$ da $x = 2$, que no cumple $x \ge 3$. La solución es $x = 5$.

### 2. Un cociente y un valor absoluto nulo (I2, 2026-1)
Determine el conjunto solución de (a) $\left|\dfrac{x - 1}{x + 1}\right| = \dfrac{1}{7}$ y (b) $|2x^2 + 9x + 4| \le 0$.

> [!example]- Solución
> (a) Se exige $x \neq -1$. La ecuación es $7|x - 1| = |x + 1|$. Elevando al cuadrado, $49(x - 1)^2 = (x + 1)^2$, o sea $12x^2 - 25x + 12 = 0$, con soluciones $x = \tfrac{3}{4}$ y $x = \tfrac{4}{3}$. Ambas distintas de $-1$: $S = \{\tfrac{3}{4}, \tfrac{4}{3}\}$.
> (b) Como un valor absoluto es $\ge 0$, $|2x^2 + 9x + 4| \le 0$ equivale a $2x^2 + 9x + 4 = 0$. Se factoriza $(2x + 1)(x + 4) = 0$, así que $S = \{-4, -\tfrac{1}{2}\}$.

### 3. Una desigualdad que vale siempre (I2, 2024-1)
Determine el conjunto solución de $|3x + 2| \le |x + 1| + |2x + 1|$.

> [!example]- Solución
> Como $3x + 2 = (x + 1) + (2x + 1)$, la desigualdad triangular da $|3x + 2| = |(x + 1) + (2x + 1)| \le |x + 1| + |2x + 1|$ para todo $x$. El conjunto solución es $\mathbb{R}$. (También sale por casos, con puntos críticos $-1$, $-\tfrac{1}{2}$ y $-\tfrac{2}{3}$: en cada tramo la desigualdad resulta cierta.)

### 4. Valor absoluto con una raíz (I1, 2020-1)
Resuelva $|x + 1| \le \sqrt{x^2 - 4x + 4} + 3$.

> [!example]- Solución
> $\sqrt{x^2 - 4x + 4} = \sqrt{(x - 2)^2} = |x - 2|$. La desigualdad es $|x + 1| \le |x - 2| + 3$. Pero $|x + 1| = |(x - 2) + 3| \le |x - 2| + |3| = |x - 2| + 3$ por la triangular, y vale siempre. $S = \mathbb{R}$.

### 5. Triangular inversa (I1, 2023-2)
Demuestre que $\big||x| - |y|\big| \le |x - y|$ para todo $x, y \in \mathbb{R}$.

> [!example]- Solución
> De $|x| = |(x - y) + y| \le |x - y| + |y|$ se obtiene $|x| - |y| \le |x - y|$. Intercambiando $x$ e $y$: $|y| - |x| \le |y - x| = |x - y|$. Las dos cotas, $|x| - |y| \le |x - y|$ y $-(|x| - |y|) \le |x - y|$, dicen que $\big||x| - |y|\big| \le |x - y|$.

### 6. Valor absoluto de un cociente de polinomios (I2, 2022-1)
Resuelva $\left|\dfrac{x^2 - 4x + 3}{x^2 - 2x + 1}\right| \le 1$.

> [!example]- Solución
> Se factoriza: $\tfrac{x^2 - 4x + 3}{x^2 - 2x + 1} = \tfrac{(x - 3)(x - 1)}{(x - 1)^2} = \tfrac{x - 3}{x - 1}$, con la restricción $x \neq 1$. Entonces $\left|\tfrac{x - 3}{x - 1}\right| \le 1 \iff |x - 3| \le |x - 1|$. Ambos lados son $\ge 0$, así que se eleva al cuadrado: $x^2 - 6x + 9 \le x^2 - 2x + 1 \iff 8 \le 4x \iff x \ge 2$. El conjunto solución es $[2, \infty)$ (la restricción $x \ne 1$ no lo afecta). Geométricamente, $x$ está más cerca de $3$ que de $1$.

### 7. Dos desigualdades de la lista de ejercicios (2022-1)
(a) Si $a \neq b$, resuelva $|x - a| + |b - x| > |a - b|$. (b) Resuelva $\big||x + 1| - 1\big| \ge |x|$.

> [!example]- Solución
> (a) Por la triangular, $|a - b| = |(a - x) + (x - b)| \le |x - a| + |x - b|$, con igualdad si y solo si $(a - x)(x - b) \ge 0$, o sea cuando $x$ está entre $a$ y $b$. La desigualdad es **estricta** cuando $x$ queda fuera: $x < \min\{a, b\}$ ó $x > \max\{a, b\}$.
> (b) Por tramos. Si $x \ge 0$: $|x + 1| - 1 = x$ y la desigualdad es $|x| \ge |x|$: cierta. Si $-1 \le x < 0$: $|x + 1| - 1 = x$ y $|x| \ge |x|$: cierta. Si $x < -1$: $|x + 1| - 1 = -x - 2$; para $x \le -2$ queda $-x - 2 \ge -x$, falso; para $-2 < x < -1$ queda $x + 2 \ge -x$, o sea $x \ge -1$, falso. Luego $S = [-1, \infty)$.

## Preguntas de repaso

> [!question]- ¿Qué se hace primero en una ecuación $|f| = g$ con $g$ no constante?
> Imponer $g \ge 0$, porque un valor absoluto no puede ser negativo; las soluciones de $f = \pm g$ se aceptan solo si cumplen esa condición.

> [!question]- ¿Cómo se reconoce que una desigualdad con valores absolutos "vale siempre" por la triangular?
> Cuando el interior del valor absoluto del lado izquierdo se puede escribir como suma de las expresiones de los del lado derecho, como $3x + 2 = (x + 1) + (2x + 1)$.

> [!question]- ¿Por qué $\sqrt{x^2 - 4x + 4}$ no es simplemente $x - 2$?
> Porque la raíz es no negativa: $\sqrt{(x - 2)^2} = |x - 2|$, que es $2 - x$ cuando $x < 2$.
