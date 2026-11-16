---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Cómo hallar el dominio de una función]]"
  - "[[03 - Cómo hallar el recorrido de una función]]"
---

# Ejercicios de prueba de dominio y recorrido

Preguntas de interrogaciones y exámenes de 2020 a 2026 que piden "el mayor dominio posible y el recorrido". Los dominios puntúan por separado cada restricción; el recorrido puntúa el planteo $y \in \operatorname{Rec}(f) \iff (\exists x)\ f(x) = y$ y la comprobación de que el $x$ obtenido está en el dominio. La pauta dice expresamente que el gráfico solo no basta cuando se pide "por definición".

## Ejercicios

### 1. Raíces anidadas (I3, 2024-1)
Determine el mayor dominio posible de $f(x) = \sqrt{\sqrt{1 - 2x} + \sqrt{\dfrac{x}{x^2 + 1}}}$.

> [!example]- Solución
> Las dos raíces interiores exigen $1 - 2x \ge 0$ (esto es, $x \le \tfrac{1}{2}$) y $\dfrac{x}{x^2 + 1} \ge 0$ (esto es, $x \ge 0$, porque $x^2 + 1 > 0$). Su intersección es $\left[0, \tfrac{1}{2}\right]$. En ella el radicando exterior es una suma de números $\ge 0$, así que la raíz exterior existe. $\operatorname{Dom}(f) = \left[0, \tfrac{1}{2}\right]$.

### 2. La función $x + \tfrac{1}{x}$ (I3, 2024-1; I3, 2025-1)
Halle el mayor dominio y el recorrido de $f(x) = x + \dfrac{1}{x}$ (y de $\dfrac{x^2 + 1}{x}$, que es la misma función).

> [!example]- Solución
> Dominio: $\mathbb{R} \setminus \{0\}$. Para el recorrido, $y \in \operatorname{Rec}(f) \iff (\exists x \neq 0)\ x + \tfrac{1}{x} = y \iff (\exists x \neq 0)\ x^2 - yx + 1 = 0$. La cuadrática tiene solución real si y solo si $\Delta = y^2 - 4 \ge 0$, es decir $|y| \ge 2$. Además $x = 0$ nunca es raíz (da $1$), luego la condición "$x \neq 0$" no restringe más. $\operatorname{Rec}(f) = (-\infty, -2] \cup [2, \infty)$.

### 3. Dominio y rango por definición (I3, 2023-1)
(a) Dominio de $f(x) = \dfrac{\sqrt{|x| - 4}}{x^2 - 16}$. (b) Rango de $f : [-4, 4] \to \mathbb{R}$, $f(x) = 5 - \sqrt{16 - x^2}$, **por definición**.

> [!example]- Solución
> (a) $|x| - 4 \ge 0$ da $x \le -4$ ó $x \ge 4$, y $x^2 \neq 16$ quita $x = \pm 4$. $\operatorname{Dom}(f) = (-\infty, -4) \cup (4, \infty)$.
> (b) $y = 5 - \sqrt{16 - x^2} \iff \sqrt{16 - x^2} = 5 - y$. Esto exige $y \le 5$, y entonces $x^2 = 16 - (5 - y)^2$, que tiene solución si y solo si $16 - (5 - y)^2 \ge 0 \iff (y - 1)(y - 9) \le 0 \iff y \in [1, 9]$. Con $y \le 5$: $y \in [1, 5]$. Y para esos $y$, $x = \pm\sqrt{16 - (5 - y)^2}$ cae en $[-4, 4]$. $\operatorname{Rec}(f) = [1, 5]$.

### 4. Recorrido de una raíz (I2, 2020-1)
Halle el dominio y el recorrido de $f(x) = \sqrt{2x - x^2}$.

> [!example]- Solución
> $\operatorname{Dom}(f) = \{x : 2x - x^2 \ge 0\} = [0, 2]$. Si $y = \sqrt{2x - x^2}$, entonces $y \ge 0$ y $x^2 - 2x + y^2 = 0$, que tiene solución si $4 - 4y^2 \ge 0 \iff -1 \le y \le 1$. Con $y \ge 0$, $y \in [0, 1]$; y para esos valores $x = 1 - \sqrt{1 - y^2} \in [0, 1]$ está en el dominio. $\operatorname{Rec}(f) = [0, 1]$.

### 5. Una diferencia con valor absoluto (I4, 2024-1)
Halle el mayor dominio y el recorrido de (a) $f(x) = \sqrt{|x| - x}$ y (b) $g(x) = \dfrac{1}{\sqrt{|x| - x}}$.

> [!example]- Solución
> Como $x \le |x|$, se tiene $|x| - x \ge 0$ para todo real. Además $|x| - x = 0$ si $x \ge 0$ y $= -2x$ si $x < 0$.
> (a) $\operatorname{Dom}(f) = \mathbb{R}$ y $f(x) = 0$ si $x \ge 0$, $f(x) = \sqrt{-2x}$ si $x < 0$. Para $b \ge 0$, $a = -\tfrac{b^2}{2} \le 0$ cumple $f(a) = b$. $\operatorname{Rec}(f) = [0, \infty)$.
> (b) El denominador se anula exactamente para $x \ge 0$, luego $\operatorname{Dom}(g) = (-\infty, 0)$. En ese dominio $g = \tfrac{1}{\sqrt{-2x}}$ toma todos los valores positivos (para $y > 0$, $x = -\tfrac{1}{2y^2}$). $\operatorname{Rec}(g) = (0, \infty)$.

### 6. Una raíz con una fracción (I4, 2026-1)
Determine el dominio y el recorrido de $f(x) = \sqrt{1 - \dfrac{1}{(1 + x)^2}}$.

> [!example]- Solución
> Se excluye $x = -1$. Se necesita $1 - \tfrac{1}{(1 + x)^2} \ge 0 \iff (1 + x)^2 \ge 1 \iff x^2 + 2x \ge 0 \iff x(x + 2) \ge 0$: $x \le -2$ ó $x \ge 0$. $\operatorname{Dom}(f) = (-\infty, -2] \cup [0, \infty)$.
> Recorrido: con $u = (1 + x)^2 \ge 1$, la expresión es $\sqrt{1 - \tfrac{1}{u}}$, y $1 - \tfrac{1}{u}$ crece de $0$ (en $u = 1$) hacia $1$ sin alcanzarlo. Dado $y \in [0, 1)$, $u = \tfrac{1}{1 - y^2} \ge 1$ y $x = -1 + \sqrt{u}$ está en el dominio. $\operatorname{Rec}(f) = [0, 1)$.

### 7. Un parámetro (I2, 2025-2)
Sea $a \in \mathbb{R}$ fijo y $f(x) = \sqrt{x^2 + 2x + a}$. Halle el dominio y el recorrido según $a$.

> [!example]- Solución
> Se completa el cuadrado: $x^2 + 2x + a = (x + 1)^2 + (a - 1)$.
> - **Si $a \ge 1$:** el radicando es siempre $\ge 0$; $\operatorname{Dom}(f) = \mathbb{R}$. El mínimo del radicando es $a - 1$, alcanzado en $x = -1$, y el radicando toma todos los valores $\ge a - 1$. $\operatorname{Rec}(f) = \left[\sqrt{a - 1}, \infty\right)$.
> - **Si $a < 1$:** el radicando se anula en $x = -1 \pm \sqrt{1 - a}$ y $\operatorname{Dom}(f) = \left(-\infty, -1 - \sqrt{1 - a}\right] \cup \left[-1 + \sqrt{1 - a}, \infty\right)$. En el dominio el radicando recorre todo $[0, \infty)$. $\operatorname{Rec}(f) = [0, \infty)$.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 3(b) hay que imponer $y \le 5$ además del discriminante?
> Porque $\sqrt{16 - x^2} = 5 - y$ exige que $5 - y \ge 0$. Sin eso se obtendrían valores $y \in (5, 9]$ que solo aparecen al elevar al cuadrado, pero que no están en el recorrido.

> [!question]- ¿Qué se comprueba al final de un recorrido por definición?
> Que el $x$ despejado pertenece al dominio y que realmente cumple $f(x) = y$ (y no solo la ecuación elevada al cuadrado).

> [!question]- ¿Por qué cambia el recorrido en el ejercicio 7 al pasar de $a < 1$ a $a \ge 1$?
> Porque con $a \ge 1$ el radicando tiene un mínimo positivo $a - 1$ y la raíz nunca baja de $\sqrt{a - 1}$; con $a < 1$ el radicando puede anularse y la raíz llega a $0$.
