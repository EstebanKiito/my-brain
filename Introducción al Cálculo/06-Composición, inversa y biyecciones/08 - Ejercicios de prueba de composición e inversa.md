---
ramo: "Introducción al Cálculo"
tema: "Composición, inversa y biyecciones"
tags:
  - intro-calculo/inversa
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Álgebra y composición de funciones]]"
  - "[[05 - Función inversa]]"
---

# Ejercicios de prueba de composición e inversa

Preguntas de interrogaciones y exámenes de 2022 a 2025 sobre dominios de composiciones, fórmulas de $f \circ g$ con funciones por tramos y cálculo de inversas con su dominio. En las pautas el dominio de la composición se razona con $x \in \operatorname{Dom}(g) \wedge g(x) \in \operatorname{Dom}(f)$, y la inversa puntúa tanto la fórmula como su dominio.

## Ejercicios

### 1. Composición con una función por tramos (I5, 2025-1)
Sean $f(x) = \begin{cases} 3x - 2 & x \le 1 \\ \dfrac{x}{x - 1} & x > 1 \end{cases}$ y $g(x) = \sqrt{x + 2}$. (a) Determine el dominio de $f \circ g$. (b) Determine una expresión para $(f \circ g)(x)$.

> [!example]- Solución
> (a) $\operatorname{Dom}(f) = \mathbb{R}$, de modo que $g(x) \in \operatorname{Dom}(f)$ siempre; solo importa $x \in \operatorname{Dom}(g)$: $\operatorname{Dom}(f \circ g) = [-2, \infty)$.
> (b) El tramo depende de si $g(x) \le 1$: $\sqrt{x + 2} \le 1 \iff x \le -1$.
> $$(f \circ g)(x) = \begin{cases} 3\sqrt{x + 2} - 2 & -2 \le x \le -1 \\ \dfrac{\sqrt{x + 2}}{\sqrt{x + 2} - 1} & x > -1 \end{cases}$$
> (en el segundo tramo $\sqrt{x + 2} > 1$, así que el denominador no se anula).

### 2. Dominio de una composición con un tramo cuadrático (I2, 2022-2; clase 14)
Sean $f : (-\infty, 5) \to \mathbb{R}$, $f(x) = \sqrt{x^2 + 4}$ y $g : [6, \infty) \to \mathbb{R}$, $g(x) = 2x + 3$. Defina $g \circ f$.

> [!example]- Solución
> $x \in \operatorname{Dom}(g \circ f) \iff x < 5 \wedge \sqrt{x^2 + 4} \ge 6 \iff x < 5 \wedge x^2 \ge 32$. Esto da $x \le -\sqrt{32} = -4\sqrt{2}$ (la rama $x \ge 4\sqrt{2} \approx 5{,}66$ no cumple $x < 5$). $\operatorname{Dom}(g \circ f) = (-\infty, -4\sqrt{2}\,]$ y $(g \circ f)(x) = 2\sqrt{x^2 + 4} + 3$.

### 3. Dominios sin construir la fórmula (Examen, 2023-2 y 2024-1)
(a) Sean $f(x) = 3x + 2$ en $\mathbb{R}$ y $g : [-1, 1] \to \mathbb{R}$, $g(x) = \sqrt{1 - x^2}$. Halle el dominio y una fórmula de $g \circ f$. (b) Si $\operatorname{Dom}(f) = [0, 2]$, halle el dominio de $g(x) = f(x^2 - 4x + 5)$.

> [!example]- Solución
> (a) $x \in \operatorname{Dom}(g \circ f) \iff 3x + 2 \in [-1, 1] \iff -1 \le x \le -\tfrac{1}{3}$. $\operatorname{Dom}(g \circ f) = \left[-1, -\tfrac{1}{3}\right]$ y $(g \circ f)(x) = \sqrt{1 - (3x + 2)^2}$.
> (b) $x \in \operatorname{Dom}(g) \iff x^2 - 4x + 5 \in [0, 2]$. Como $x^2 - 4x + 5 = (x - 2)^2 + 1 \ge 1 > 0$, solo importa $x^2 - 4x + 5 \le 2 \iff x^2 - 4x + 3 \le 0 \iff (x - 1)(x - 3) \le 0$. $\operatorname{Dom}(g) = [1, 3]$.

### 4. Inversa de una cúbica fraccionaria (I2, 2022-2)
Sea $h : \mathbb{R} \setminus \{-1\} \to B$, $h(x) = \dfrac{x^3}{1 + x^3}$. (a) Pruebe que $h$ es inyectiva. (b) Halle la inversa. (c) ¿Cuál es el dominio de la inversa?

> [!example]- Solución
> (a) $h(x_1) = h(x_2) \iff x_1^3(1 + x_2^3) = x_2^3(1 + x_1^3) \iff x_1^3 = x_2^3 \iff x_1 = x_2$.
> (b) $y = \tfrac{x^3}{1 + x^3} \iff y(1 + x^3) = x^3 \iff x^3(1 - y) = y \iff x^3 = \tfrac{y}{1 - y}$, así que $h^{-1}(y) = \sqrt[3]{\dfrac{y}{1 - y}}$.
> (c) El dominio de $h^{-1}$ es $B = \operatorname{Rec}(h)$: $y \neq 1$ (de $x^3 = \tfrac{y}{1 - y}$ se ve que $y = 1$ no se alcanza) y $x \neq -1$ equivale a $\tfrac{y}{1 - y} \neq -1$, que siempre se cumple. $\operatorname{Dom}(h^{-1}) = \mathbb{R} \setminus \{1\}$.

### 5. Una función de Möbius con inversa (I2, 2025-2)
Sea $f(x) = \dfrac{3x - 2}{3 - 2x}$. Halle el dominio $A$ y el recorrido $B$. Demuestre que $f : A \to B$ es inyectiva (y por tanto biyectiva) y calcule la inversa.

> [!example]- Solución
> $\operatorname{Dom}(f) = A = \mathbb{R} \setminus \left\{\tfrac{3}{2}\right\}$. **Inyectiva:** $f(x) = f(z) \Rightarrow (3x - 2)(3 - 2z) = (3z - 2)(3 - 2x) \Rightarrow 9x - 6xz - 6 + 4z = 9z - 6xz - 6 + 4x \Rightarrow 5x = 5z$. **Recorrido:** $f(x) + \tfrac{3}{2} = \dfrac{5}{6 - 4x} \neq 0$ para todo $x$, así que $-\tfrac{3}{2} \notin \operatorname{Rec}(f)$; y para $y \neq -\tfrac{3}{2}$, de $(3 - 2x)y = 3x - 2$ sale $x = \dfrac{2 + 3y}{3 + 2y}$, que es distinto de $\tfrac{3}{2}$. $B = \mathbb{R} \setminus \left\{-\tfrac{3}{2}\right\}$ y $f^{-1}(y) = \dfrac{2 + 3y}{3 + 2y}$.
>
> La pauta escribe el dominio como $\left(-\infty, \tfrac{2}{3}\right) \cup \left(\tfrac{3}{2}, \infty\right)$; el denominador solo se anula en $\tfrac{3}{2}$, así que el dominio correcto es $\mathbb{R} \setminus \{\tfrac{3}{2}\}$.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 1 el dominio de $f \circ g$ es $[-2, \infty)$ y no se resuelve ninguna inecuación?
> Porque $f$ está definida en todo $\mathbb{R}$, así que $g(x) \in \operatorname{Dom}(f)$ no impone nada; solo hace falta $x \in \operatorname{Dom}(g) = [-2, \infty)$.

> [!question]- ¿Cómo se decide qué tramo de $f$ usar en $f \circ g$?
> Se traduce la condición del tramo ($g(x) \le 1$) en una condición sobre $x$ ($x \le -1$) y se aplica la fórmula correspondiente a cada región.

> [!question]- ¿Cuál es el dominio de la inversa de una biyección $f : A \to B$?
> El codominio $B$, es decir, el recorrido de $f$.

> [!question]- ¿Cómo se verifica que $f^{-1}(y) = \frac{2 + 3y}{3 + 2y}$ está bien?
> Se comprueba que $f(f^{-1}(y)) = y$: al reemplazar, $\frac{3x - 2}{3 - 2x}$ con $x = \frac{2 + 3y}{3 + 2y}$ simplifica a $y$.
