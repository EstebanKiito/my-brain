---
ramo: "Introducción al Cálculo"
tema: "Límites de sucesiones y álgebra de límites"
tags:
  - intro-calculo/limites
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Demostrar límites con la definición]]"
  - "[[05 - Teorema del sándwich y límites por acotación]]"
---

# Ejercicios de prueba de límites de sucesiones

Las interrogaciones 6 a 10 traen tres formatos de límites: **demostrar con la definición**, **calcular con álgebra de límites** (cocientes, raíces con conjugado, exponenciales) y **calcular con el teorema del sándwich**. En cada uno, la pauta puntúa el paso clave (la acotación, el conjugado, la cota por ambos lados) y la conclusión citando el teorema.

## Ejercicios

### 1. Con la definición (I6, 2026-1)
Demuestre, con la definición de límite, que (a) $\lim\dfrac{n + 1}{n - 1} = 1$ y (b) $\lim\sqrt{\dfrac{2n + 1}{n}} = \sqrt{2}$.

> [!example]- Solución
> (a) Para $n \ge 2$, $\left|\tfrac{n + 1}{n - 1} - 1\right| = \tfrac{2}{n - 1}$. Dado $\varepsilon > 0$, $\tfrac{2}{n - 1} < \varepsilon \iff n > \tfrac{2}{\varepsilon} + 1$. Por Arquímedes existe un entero $n_0 \ge 2$ con $n_0 > \tfrac{2}{\varepsilon} + 1$ y para todo $n \ge n_0$ la desigualdad vale.
> (b) $\sqrt{\tfrac{2n + 1}{n}} = \sqrt{2 + \tfrac{1}{n}}$ y $\left|\sqrt{2 + \tfrac{1}{n}} - \sqrt{2}\right| = \dfrac{1/n}{\sqrt{2 + 1/n} + \sqrt{2}} \le \dfrac{1}{n}$, porque el denominador es $\ge 2\sqrt{2} > 1$. Se elige $n_0$ con $\tfrac{1}{n_0} < \varepsilon$ y para $n \ge n_0$, $|a_n - \sqrt{2}| \le \tfrac{1}{n} < \varepsilon$.

### 2. Con la definición y acotación (I7, 2022-1; I9, 2020-1)
Demuestre con la definición que (a) $\lim\dfrac{3n^2 + 1}{n^2 + n + 1} = 3$ y (b) $\lim\dfrac{n^2}{2n^2 + n + 1} = \dfrac{1}{2}$.

> [!example]- Solución
> (a) $\left|\tfrac{3n^2 + 1}{n^2 + n + 1} - 3\right| = \tfrac{3n + 2}{n^2 + n + 1} \le \tfrac{5n}{n^2 + n} = \tfrac{5}{n + 1}$. Dado $\varepsilon > 0$, por Arquímedes existe $N > \tfrac{5}{\varepsilon} - 1$; si $n > N$, $\tfrac{5}{n + 1} < \varepsilon$.
> (b) $\left|\tfrac{n^2}{2n^2 + n + 1} - \tfrac{1}{2}\right| = \tfrac{n + 1}{2(2n^2 + n + 1)} = \tfrac{1}{n}\cdot\tfrac{1 + 1/n}{2(2 + 1/n + 1/n^2)} \le \tfrac{1}{n}$ para $n \ge 1$ (el segundo factor es $\le \tfrac{2}{4}$). Se toma $n_0$ con $\tfrac{1}{n_0} < \varepsilon$.

### 3. El signo del límite (I7, 2024-1)
Sea $\{a_n\}$ convergente con $a_n \ge 0$ para todo $n$. Demuestre que $\lim a_n \ge 0$.

> [!example]- Solución
> Sea $L = \lim a_n$ y supóngase $L < 0$. Con $\varepsilon = -L > 0$, existe $N$ tal que para $n > N$: $|a_n - L| < -L$, o sea $2L < a_n < 0$. Entonces $a_n < 0$ para $n > N$, lo que contradice $a_n \ge 0$. Luego $L \ge 0$.

### 4. Cocientes con raíces (I6, 2026-1; I6, 2025-1)
Calcule (a) $\lim\dfrac{n - 1}{n\sqrt{n} - 3}$, (b) $\lim\left(\sqrt{n^2 - n + 1} - n\right)$, (c) $\lim\dfrac{\sqrt[3]{n^2 + 1}}{n + 1}$ y (d) $\lim\left(\sqrt{n^2 + 5n + 6} - n\right)$.

> [!example]- Solución
> (a) Se amplifica por $\tfrac{1}{n}$: $\dfrac{1 - 1/n}{\sqrt{n} - 3/n} \to \dfrac{1}{\infty} = 0$ (el numerador tiende a $1$ y el denominador crece sin cota, pues $\sqrt{n} - \tfrac{3}{n} \to \infty$).
> (b) Con el conjugado: $\dfrac{(n^2 - n + 1) - n^2}{\sqrt{n^2 - n + 1} + n} = \dfrac{-1 + 1/n}{\sqrt{1 - 1/n + 1/n^2} + 1} \to \dfrac{-1}{2}$.
> (c) $\dfrac{\sqrt[3]{(n^2 + 1)/n^3}}{1 + 1/n} = \dfrac{\sqrt[3]{1/n + 1/n^3}}{1 + 1/n} \to \dfrac{0}{1} = 0$.
> (d) Con el conjugado: $\dfrac{5n + 6}{\sqrt{n^2 + 5n + 6} + n} = \dfrac{5 + 6/n}{\sqrt{1 + 5/n + 6/n^2} + 1} \to \dfrac{5}{2}$.

### 5. Raíces y exponenciales (I8, 2022-1; I10, 2020-1)
Calcule (a) $\lim\sqrt{n}\left(\sqrt{n + 1} - \sqrt{n}\right)$, (b) $\lim\dfrac{3^{n+1} + 2^{n+1}}{3^n + 2^n}$ y (c) $\lim\left(\sqrt{n^2 + 3n + 5} - n\right)$.

> [!example]- Solución
> (a) $\sqrt{n}\cdot\dfrac{1}{\sqrt{n + 1} + \sqrt{n}} = \dfrac{1}{\sqrt{1 + 1/n} + 1} \to \dfrac{1}{2}$.
> (b) Se divide por $3^n$: $\dfrac{3 + 2(2/3)^n}{1 + (2/3)^n} \to \dfrac{3 + 0}{1 + 0} = 3$, pues $(2/3)^n \to 0$.
> (c) Con el conjugado, $\dfrac{3n + 5}{\sqrt{n^2 + 3n + 5} + n} = \dfrac{3 + 5/n}{\sqrt{1 + 3/n + 5/n^2} + 1} \to \dfrac{3}{2}$.

### 6. Con el sándwich (I7, 2026-1; I3, 2025-2)
Calcule (a) $\lim\dfrac{n - \operatorname{sen}(n)}{n^2 - 16}$, (b) $\lim\dfrac{a^{n+1} + b^{n+1}}{a^n + b^n}$ con $a > b > 0$, (c) $\lim\dfrac{\cos(n^3 + 1)}{n}$ y (d) $\lim\dfrac{n}{2^n}$.

> [!example]- Solución
> (a) Para $n \ge 5$: $\tfrac{n - \operatorname{sen}(n)}{n^2 - 16} = \tfrac{n}{n^2 - 16} - \tfrac{\operatorname{sen}(n)}{n^2 - 16}$. El primer término tiende a $0$ y, como $-\tfrac{1}{n^2 - 16} \le \tfrac{\operatorname{sen}(n)}{n^2 - 16} \le \tfrac{1}{n^2 - 16}$, el segundo también (sándwich). Resultado $0$.
> (b) $\dfrac{a^{n+1} + b^{n+1}}{a^n + b^n} = a\cdot\dfrac{1 + (b/a)^{n+1}}{1 + (b/a)^n} \to a$, porque $0 < \tfrac{b}{a} < 1$ y $(b/a)^n \to 0$.
> (c) $-\tfrac{1}{n} \le \tfrac{\cos(n^3 + 1)}{n} \le \tfrac{1}{n}$ y ambos extremos tienden a $0$: el límite es $0$.
> (d) Del binomio, $2^n \ge 1 + n + \tfrac{n(n - 1)}{2}$, de modo que $0 \le \tfrac{n}{2^n} \le \tfrac{n}{1 + n + n(n - 1)/2} \le \tfrac{2}{n - 1} \to 0$. Resultado $0$.

### 7. Una cota con senos (I8, 2023-1)
Calcule $\lim\dfrac{n + \operatorname{sen}(n\pi/2)}{2n + 1}$.

> [!example]- Solución
> Como $-1 \le \operatorname{sen}\!\left(\tfrac{n\pi}{2}\right) \le 1$, para todo $n$: $\tfrac{n - 1}{2n + 1} \le a_n \le \tfrac{n + 1}{2n + 1}$. Los dos extremos tienden a $\tfrac{1}{2}$ (por álgebra de límites), luego $\lim a_n = \tfrac{1}{2}$.

## Preguntas de repaso

> [!question]- ¿Qué se necesita para que el sándwich concluya?
> Dos sucesiones $a_n \le b_n \le c_n$ (para $n$ grande) con $\lim a_n = \lim c_n = L$; entonces $\lim b_n = L$.

> [!question]- ¿Por qué en el ejercicio 4(d) el límite no es $0$ aunque $\sqrt{n^2 + 5n + 6}$ "parezca" $n$?
> Porque la diferencia de dos términos que tienden a $\infty$ es indeterminada. Racionalizando se ve que la diferencia tiende a $\frac{5}{2}$: la parte $5n$ del radicando se acumula.

> [!question]- ¿Cómo se elige el $N$ en el ejercicio 1(a)?
> Se despeja $n > \frac{2}{\varepsilon} + 1$ y se toma, por Arquímedes, un natural mayor que ese número (con $n \ge 2$).
