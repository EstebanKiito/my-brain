---
ramo: "Introducción al Cálculo"
tema: "Composición, inversa y biyecciones"
tags:
  - intro-calculo/inversa
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Funciones sobreyectivas y biyectivas]]"
  - "[[03 - Funciones monótonas]]"
---

# Ejercicios de prueba de inyectividad, biyección y monotonía

Preguntas de las interrogaciones 5 y de los exámenes de 2022 a 2026. El esquema es casi siempre el mismo: demostrar inyectividad con $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$, calcular el recorrido por definición para decidir la sobreyectividad (o el codominio que la hace sobreyectiva) y, al final, despejar la inversa.

## Ejercicios

### 1. Recortar hasta que sea biyectiva (I5, 2026-1; I5, 2022-1)
Sea $f : \mathbb{R} \setminus \{-1, 1\} \to \mathbb{R}$, $f(x) = \dfrac{x + 1}{|x| - 1}$. (a) Demuestre que no es inyectiva ni epiyectiva. (b) Halle los mayores $A, B \subseteq \mathbb{R}$ con $f : A \to B$ biyectiva. (c) Halle $f^{-1} : B \to A$.

> [!example]- Solución
> (a) Para $x < 0$, $|x| = -x$ y $f(x) = \dfrac{x + 1}{-x - 1} = -1$ (con $x \neq -1$): constante en $(-\infty, -1) \cup (-1, 0)$, luego no inyectiva (por ejemplo $f(-2) = f(-3) = -1$). Para $x \ge 0$, $f(x) = \tfrac{x + 1}{x - 1}$. Si existiera $x$ con $f(x) = 1$, sería $x \ge 0$ y $x + 1 = x - 1$, absurdo: $1 \notin \operatorname{Rec}(f)$, no es epiyectiva.
> (b) En $[0, 1) \cup (1, \infty)$, $\tfrac{a + 1}{a - 1} = \tfrac{b + 1}{b - 1} \iff (a + 1)(b - 1) = (b + 1)(a - 1) \iff a = b$: inyectiva. Como en $(-\infty, -1) \cup (-1, 0)$ es constante, $A = [0, 1) \cup (1, \infty)$. El recorrido de $f|_A$: de $y = \tfrac{x + 1}{x - 1}$ sale $x = \tfrac{y + 1}{y - 1}$, que debe estar en $A$: $0 \le \tfrac{y + 1}{y - 1} < 1$ o $\tfrac{y + 1}{y - 1} > 1$. Esto equivale a $y \le -1$ o $y > 1$: $B = (-\infty, -1] \cup (1, \infty)$.
> (c) $f^{-1}(y) = \dfrac{y + 1}{y - 1}$ para $y \in B$.

### 2. Dominio, inyectividad, sobreyectividad e inversa (Examen, 2025-1)
Sea $f : A \to [0, 1) \cup (1, \infty)$, $f(x) = \sqrt{1 - \dfrac{2}{1 + x}}$. (a) Determine $A = \operatorname{Dom}(f)$. (b) Pruebe que es inyectiva. (c) Pruebe que es sobreyectiva. (d) Halle la inversa.

> [!example]- Solución
> (a) $1 - \tfrac{2}{1 + x} = \tfrac{x - 1}{x + 1} \ge 0$ con $x \neq -1$: $A = (-\infty, -1) \cup [1, \infty)$.
> (b) $f(a) = f(b) \Rightarrow \tfrac{a - 1}{a + 1} = \tfrac{b - 1}{b + 1} \Rightarrow (a - 1)(b + 1) = (b - 1)(a + 1) \Rightarrow a = b$.
> (c) Para $y \ge 0$: $y^2(x + 1) = x - 1 \iff x = \tfrac{1 + y^2}{1 - y^2}$ (si $y \neq \pm 1$). Ese $x$ está en $A$: si $0 \le y < 1$ es $\ge 1$, y si $y > 1$ es $< -1$. Luego $\operatorname{Rec}(f) = [0, 1) \cup (1, \infty)$, que es el codominio.
> (d) $f^{-1}(y) = \dfrac{1 + y^2}{1 - y^2}$ para $y \in [0, 1) \cup (1, \infty)$.

### 3. Mayor dominio de inyectividad y codominio sobreyectivo (I5, 2025-1)
Sea $f(x) = \sqrt{\dfrac{2x - 3}{x + 4}}$. (a) Halle el mayor $A$ donde $f$ es inyectiva. (b) Halle $B$ para que sea sobreyectiva. (c) Halle $f^{-1}$.

> [!example]- Solución
> (a) $f = h \circ \ell$ con $\ell(x) = \tfrac{2x - 3}{x + 4}$ (Möbius, inyectiva) y $h(x) = \sqrt{x}$ (inyectiva en $[0, \infty)$); $f$ es inyectiva en todo su dominio: $\tfrac{2x - 3}{x + 4} \ge 0$ y $x \neq -4$ dan $A = (-\infty, -4) \cup \left[\tfrac{3}{2}, \infty\right)$.
> (b) $B = \operatorname{Rec}(f)$. De $y = f(x)$ con $y \ge 0$: $y^2(x + 4) = 2x - 3$, es decir $x(y^2 - 2) = -3 - 4y^2$. Si $y^2 = 2$ no hay solución. Si no, $x = \tfrac{4y^2 + 3}{2 - y^2}$, que cae en $A$ para todo $y \ge 0$, $y \neq \sqrt{2}$. $B = [0, \sqrt{2}) \cup (\sqrt{2}, \infty)$.
> (c) $f^{-1}(y) = \dfrac{4y^2 + 3}{2 - y^2}$ (la pauta usa la letra $x$ en un lado y la $y$ en el otro).

### 4. Monotonía y la sobreyectividad de una raíz con cociente (I5, 2023-1; I5, 2024-1)
(a) Muestre que $f(x) = x + \tfrac{1}{x}$ es estrictamente creciente en $[1, \infty)$. (b) Muestre que $f(x) = \dfrac{x + 3}{x - 1}$ es inyectiva en su mayor dominio. (c) Muestre que $f : (0, \infty) \to (0, \infty)$, $f(x) = \dfrac{\sqrt{1 + 4x}}{x}$ es biyectiva.

> [!example]- Solución
> (a) Para $1 \le x_1 < x_2$: $f(x_2) - f(x_1) = (x_2 - x_1)\left(1 - \tfrac{1}{x_1 x_2}\right) > 0$, pues $x_2 - x_1 > 0$ y $x_1 x_2 > 1$.
> (b) $\operatorname{Dom}(f) = \mathbb{R} \setminus \{1\}$ y $f(x) = 1 + \tfrac{4}{x - 1}$. Si $f(x_1) = f(x_2)$, entonces $\tfrac{4}{x_1 - 1} = \tfrac{4}{x_2 - 1}$ y $x_1 = x_2$.
> (c) **Inyectiva:** $f(x_1) = f(x_2)$ da $\tfrac{1 + 4x_1}{x_1^2} = \tfrac{1 + 4x_2}{x_2^2}$, que equivale a $(x_2 - x_1)(x_2 + x_1 + 4x_1 x_2) = 0$; como $x_1, x_2 > 0$, $x_2 + x_1 + 4x_1 x_2 > 0$, luego $x_1 = x_2$. **Sobreyectiva:** si $y > 0$, la ecuación $y^2 x^2 - 4x - 1 = 0$ tiene la raíz positiva $x = \tfrac{4 + \sqrt{16 + 4y^2}}{2y^2} > 0$, que cumple $f(x) = y$.

### 5. Impar, monotonía por tramos y bosquejo (I5, 2023-1)
Sea $f(x) = -\dfrac{x}{(3 + x^2)^2}$. (a) Pruebe que es impar. (b) Para $x_1, x_2 \ge 0$ pruebe que $f(x_1) - f(x_2) = -\dfrac{(x_1 - x_2)\,[\,9 - x_1 x_2(6 + x_1^2 + x_1 x_2 + x_2^2)\,]}{(3 + x_1^2)^2(3 + x_2^2)^2}$. (c) Deduzca la monotonía en $[0, 1]$ y $[1, \infty)$ y en $(-\infty, 0]$. (d) Bosqueje.

> [!example]- Solución
> (a) $f(-x) = \dfrac{x}{(3 + x^2)^2} = -f(x)$.
> (b) $f(x_1) - f(x_2) = -\dfrac{x_1(3 + x_2^2)^2 - x_2(3 + x_1^2)^2}{(3 + x_1^2)^2(3 + x_2^2)^2}$, y el numerador es $9(x_1 - x_2) - 6x_1x_2(x_1 - x_2) - x_1x_2(x_1^3 - x_2^3)$; al usar $x_1^3 - x_2^3 = (x_1 - x_2)(x_1^2 + x_1x_2 + x_2^2)$ se factoriza $(x_1 - x_2)[\ldots]$.
> (c) Si $0 \le x_1 < x_2 \le 1$, el corchete es positivo (cota $9 - 1 \cdot 9 > 0$) y $x_1 - x_2 < 0$; entonces $f(x_1) - f(x_2) > 0$: **estrictamente decreciente** en $[0, 1]$. Si $1 \le x_1 < x_2$ el corchete es negativo y resulta $f(x_1) < f(x_2)$: **estrictamente creciente** en $[1, \infty)$. Por ser impar, es decreciente en $[-1, 0]$ y creciente en $(-\infty, -1]$.
> (d) Sin asíntotas verticales; la asíntota horizontal es $y = 0$; el único corte con los ejes es el origen. Desde el origen el gráfico baja hasta un mínimo en $x = 1$, donde vale $-\tfrac{1}{16}$, y luego sube acercándose a $0$ por debajo; la mitad izquierda se obtiene por simetría impar (máximo en $x = -1$, con valor $\tfrac{1}{16}$).

### 6. Una función impar y biyectiva (Examen, 2026-1)
Sea $f(x) = \dfrac{x}{|x| + 1}$. (a) Dominio, ceros y paridad. (b) Pruebe que es estrictamente creciente. (c) Pruebe que $-1 < f(x) < 1$. (d) Halle los mayores $A, B$ con $f : A \to B$ biyectiva y la inversa.

> [!example]- Solución
> (a) $\operatorname{Dom}(f) = \mathbb{R}$ (el denominador es $\ge 1$). El único cero es $x = 0$. Es impar: $f(-x) = \tfrac{-x}{|x| + 1} = -f(x)$.
> (b) Por imparidad basta $x > y > 0$: $\tfrac{1}{x} < \tfrac{1}{y} \Rightarrow \tfrac{x + 1}{x} < \tfrac{y + 1}{y} \Rightarrow \tfrac{x}{x + 1} > \tfrac{y}{y + 1}$, o sea $f(x) > f(y)$.
> (c) Para $x \ge 0$: $0 \le \tfrac{x}{x + 1} < 1$. Para $x < 0$ se usa la imparidad: $-1 < f(x) \le 0$.
> (d) Es inyectiva por ser estrictamente creciente en $\mathbb{R}$, y por (c) su recorrido está en $(-1, 1)$. Todo $y \in [0, 1)$ tiene la preimagen $x = \tfrac{y}{1 - y} \ge 0$ y todo $y \in (-1, 0)$ la preimagen $x = \tfrac{y}{1 + y} < 0$. $A = \mathbb{R}$, $B = (-1, 1)$ y $f^{-1}(y) = \dfrac{y}{1 - |y|}$.

### 7. Biyecciones entre conjuntos de números (I2, 2023-2)
(a) Demuestre que $f : \mathbb{N} \to \mathbb{N}$, $f(n) = n^2$ es inyectiva. ¿Es sobreyectiva? (b) Construya una biyección $\mathbb{N} \to \mathbb{Z}$.

> [!example]- Solución
> (a) Es inyectiva ($n^2 = m^2$ con $n, m > 0$ implica $n = m$) y no sobreyectiva ($3$ no es un cuadrado). (b) $f(n) = \tfrac{n}{2}$ si $n$ es par y $f(n) = -\tfrac{n - 1}{2}$ si $n$ es impar. Los pares van a los enteros positivos ($f(2k) = k$) y los impares a los no positivos ($f(2k + 1) = -k$, con $f(1) = 0$): es inyectiva (distinto signo o distintos $n$) y sobreyectiva (para $k > 0$, $f(2k) = k$; para $k \le 0$, $f(1 - 2k) = k$).

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 1 se recorta el dominio a $[0, 1) \cup (1, \infty)$?
> Porque en los negativos $f$ es constante igual a $-1$, lo que rompe la inyectividad. En $[0, 1) \cup (1, \infty)$ la función es el cociente inyectivo $\frac{x + 1}{x - 1}$.

> [!question]- ¿Cómo se concluye en el ejercicio 6 que $B = (-1, 1)$ y no todo $\mathbb{R}$?
> Porque $\frac{x}{|x| + 1}$ queda siempre entre $-1$ y $1$ (estrictamente): ningún valor fuera de $(-1, 1)$ se alcanza, y todos los de dentro sí.

> [!question]- ¿Qué se necesita comprobar al despejar $x$ en el ejercicio 3(b)?
> Que el $x$ obtenido, $\frac{4y^2 + 3}{2 - y^2}$, pertenece a $A$ y que $y^2 = 2$ no tiene solución. Eso determina que el recorrido omita $\sqrt{2}$.
