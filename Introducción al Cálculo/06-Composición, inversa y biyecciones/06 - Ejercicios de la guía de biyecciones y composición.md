---
ramo: "Introducción al Cálculo"
tema: "Composición, inversa y biyecciones"
tags:
  - intro-calculo/inversa
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Funciones sobreyectivas y biyectivas]]"
  - "[[04 - Álgebra y composición de funciones]]"
---

# Ejercicios de la guía de biyecciones y composición

Los seis ejercicios de la Guía 5 (biyecciones) y los tres de la Guía 7 (composición de funciones). Conviene intentar cada uno antes de abrir la solución.

## Guía 5: biyecciones

### 1. Una biyección de $[0, \infty)$
Demuestre que la función $f : [0, \infty) \to [0, \infty)$ es una biyección.

> [!example]- Solución
> La guía no escribe la fórmula; el ejemplo estándar es $f(x) = x^2$. **Inyectiva:** si $x_1^2 = x_2^2$ con $x_1, x_2 \ge 0$, entonces $(x_1 - x_2)(x_1 + x_2) = 0$ y como $x_1 + x_2 \ge 0$ solo cae $x_1 = x_2$ (o ambos son $0$). **Sobreyectiva:** para todo $y \ge 0$, $x = \sqrt{y} \in [0, \infty)$ cumple $f(x) = y$.

### 2. Dos conjuntos finitos
Demuestre que no existe una biyección entre $A = \{1, 2, 3, 4\}$ y $B = \{1, 2\}$.

> [!example]- Solución
> Cualquier función $f : A \to B$ envía $4$ elementos a solo $2$ valores, de modo que dos elementos de $A$ comparten imagen (principio del palomar). Entonces $f$ no es inyectiva y no puede ser biyección.

### 3. Los cuadrados en los naturales
Demuestre que $f : \mathbb{N} \to \mathbb{N}$, $f(n) = n^2$ es inyectiva. ¿Es sobreyectiva?

> [!example]- Solución
> Si $n^2 = m^2$ con $n, m > 0$, entonces $n = m$ (la raíz positiva es única). No es sobreyectiva: $3$ (o $2$) no es el cuadrado de ningún natural.

### 4. Inyectividad en $\mathbb{R}$
Determine si $f(x) = x^2 - 2x$, $g(x) = |x|$, $h(x) = \tfrac{1}{x^2}$ y $r(x) = x^2 - 2x + 2$ son inyectivas.

> [!example]- Solución
> Ninguna lo es. $f(0) = f(2) = 0$. $g(-1) = g(1) = 1$. $h(-1) = h(1) = 1$ (con dominio $\mathbb{R} \setminus \{0\}$). $r(0) = r(2) = 2$ (su forma normal es $(x - 1)^2 + 1$, simétrica respecto de $x = 1$).

### 5. Una función por tramos
Decida si $f(x) = \begin{cases} x^2 + 1 & x \ge 0 \\ x - 1 & x < 0 \end{cases}$ es inyectiva y sobreyectiva.

> [!example]- Solución
> Para $x \ge 0$, $x^2 + 1 \in [1, \infty)$ y es inyectiva; para $x < 0$, $x - 1 \in (-\infty, -1)$ y es inyectiva. Los recorridos son disjuntos, así que $f$ es **inyectiva**. **No es sobreyectiva** sobre $\mathbb{R}$: ningún valor de $[-1, 1)$ se alcanza (por ejemplo, $f(x) = 0$ exigiría $x^2 + 1 = 0$ o $x = 1 \notin (-\infty, 0)$).

### 6. Una biyección de tipo Möbius
Sean $a, b, c, d \in \mathbb{R}$ con $c \neq 0$ y $ad \neq bc$. Demuestre que $f : \mathbb{R} \setminus \{d/c\} \to \mathbb{R} \setminus \{a/c\}$, $f(x) = \dfrac{ax - b}{cx - d}$ es biyectiva.

> [!example]- Solución
> **Inyectiva:** $f(x_1) = f(x_2) \iff (ax_1 - b)(cx_2 - d) = (ax_2 - b)(cx_1 - d)$, que tras desarrollar y cancelar se reduce a $(bc - ad)(x_1 - x_2) = 0$; como $ad \neq bc$, $x_1 = x_2$. **Sobreyectiva:** para $y \neq \tfrac{a}{c}$, $x = \dfrac{dy - b}{cy - a}$ cumple $f(x) = y$ y pertenece al dominio: $x = \tfrac{d}{c}$ exigiría $c(dy - b) = d(cy - a)$, o sea $ad = bc$, una contradicción. Además $f^{-1}(y) = \dfrac{dy - b}{cy - a}$.

## Guía 7: composición

### 7. Dominios de composiciones
Si $f(x) = \sqrt{x}$ y $g(x) = \sqrt{2 - x}$, determine el dominio de (a) $f \circ g$, (b) $g \circ f$, (c) $f \circ f$ y (d) $g \circ g$.

> [!example]- Solución
> (a) $f(g(x)) = \sqrt{\sqrt{2 - x}}$ requiere $x \le 2$ (para $g$) y $\sqrt{2 - x} \ge 0$ (siempre): $(-\infty, 2]$.
> (b) $g(f(x)) = \sqrt{2 - \sqrt{x}}$ requiere $x \ge 0$ y $2 - \sqrt{x} \ge 0$, o sea $x \le 4$: $[0, 4]$.
> (c) $f(f(x)) = \sqrt[4]{x}$ requiere $x \ge 0$: $[0, \infty)$.
> (d) $g(g(x)) = \sqrt{2 - \sqrt{2 - x}}$ requiere $x \le 2$ y $\sqrt{2 - x} \le 2$, es decir $2 - x \le 4$, $x \ge -2$: $[-2, 2]$.

### 8. Descomponer una función
Sea $F(x) = \sqrt[4]{x + 9}$. Determine $f$ y $g$ con $F = f \circ g$.

> [!example]- Solución
> Por ejemplo $g(x) = x + 9$ y $f(x) = \sqrt[4]{x}$. (También sirve $g(x) = \sqrt{x + 9}$ y $f(x) = \sqrt{x}$.) La descomposición no es única.

### 9. Composiciones y dominios
Determine $f \circ g$, $g \circ f$ y sus dominios: (a) $f(x) = x^3 + 2$, $g(x) = \sqrt[3]{x}$; (b) $f(x) = x^2$, $g(x) = \sqrt{x - 3}$; (c) $f(x) = \tfrac{1}{x}$, $g(x) = 2x + 4$.

> [!example]- Solución
> (a) $f \circ g(x) = (\sqrt[3]{x})^3 + 2 = x + 2$ y $g \circ f(x) = \sqrt[3]{x^3 + 2}$, ambas con dominio $\mathbb{R}$.
> (b) $f \circ g(x) = (\sqrt{x - 3})^2 = x - 3$, pero con dominio $[3, \infty)$ (no $\mathbb{R}$: el dominio lo fija $g$). $g \circ f(x) = \sqrt{x^2 - 3}$, con dominio $(-\infty, -\sqrt{3}] \cup [\sqrt{3}, \infty)$.
> (c) $f \circ g(x) = \tfrac{1}{2x + 4}$, dominio $\mathbb{R} \setminus \{-2\}$. $g \circ f(x) = \tfrac{2}{x} + 4$, dominio $\mathbb{R} \setminus \{0\}$.

## Preguntas de repaso

> [!question]- ¿Por qué $f(x) = x^2$ restringida a $[0, \infty)$ con codominio $[0, \infty)$ es biyectiva?
> Es inyectiva (no hay dos positivos con el mismo cuadrado) y sobreyectiva (todo $y \ge 0$ es el cuadrado de $\sqrt{y}$).

> [!question]- ¿Qué falla en el ejercicio 6 si $ad = bc$?
> La función $\frac{ax - b}{cx - d}$ se reduce a una constante $\frac{a}{c}$ (hasta la restricción del dominio) y deja de ser inyectiva.

> [!question]- ¿Por qué en 9(b) $f \circ g(x) = x - 3$ no tiene dominio $\mathbb{R}$?
> Porque $x$ debe estar en $\operatorname{Dom}(g) = [3, \infty)$ antes de aplicar $f$; la fórmula simplificada $x - 3$ olvida esa restricción.
