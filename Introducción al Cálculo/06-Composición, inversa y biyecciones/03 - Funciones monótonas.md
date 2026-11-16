---
ramo: "Introducción al Cálculo"
tema: "Composición, inversa y biyecciones"
tags:
  - intro-calculo/inversa
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones inyectivas y el test de la recta horizontal]]"
---

# Funciones monótonas

Una función es **monótona** si siempre sube o siempre baja. La monotonía es la forma más práctica de probar inyectividad sin resolver ecuaciones, y se demuestra con una técnica simple: estudiar el signo de $f(x_2) - f(x_1)$ para $x_1 < x_2$.

## Definiciones

> [!tip] Crecimiento y decrecimiento
> Sea $f : A \to B$. Para todo $x_1, x_2 \in A$ con $x_1 < x_2$:
> - **estrictamente creciente** si $f(x_1) < f(x_2)$; **creciente** si $f(x_1) \le f(x_2)$;
> - **estrictamente decreciente** si $f(x_1) > f(x_2)$; **decreciente** si $f(x_1) \ge f(x_2)$;
> - **monótona** si es creciente o decreciente.

Casi todas las funciones solo son monótonas **por tramos**: por ejemplo, $x^2$ decrece en $(-\infty, 0]$ y crece en $[0, \infty)$.

> [!tip] Monotonía estricta implica inyectividad
> Si $f$ es estrictamente monótona, entonces es inyectiva.

*Demostración.* Si $f$ es estrictamente creciente y $x_1 \neq x_2$, uno es menor: digamos $x_1 < x_2$, y entonces $f(x_1) < f(x_2)$, es decir, $f(x_1) \neq f(x_2)$. El decreciente es análogo. $\blacksquare$

El recíproco es falso: una función puede ser inyectiva sin ser monótona (por ejemplo, $x \mapsto \tfrac{1}{x}$ en $\mathbb{R} \setminus \{0\}$, que decrece en cada rama pero no en todo el dominio).

## Cómo probar monotonía

El método es **restar**. Para $x_1 < x_2$ en el dominio, se calcula $f(x_2) - f(x_1)$, se factoriza el factor $(x_2 - x_1) > 0$ y se estudia el signo del resto.

**$f(x) = x + \tfrac{1}{x}$ en $[1, \infty)$ (I5, 2024-1).** Para $1 \le x_1 < x_2$:
$$f(x_2) - f(x_1) = (x_2 - x_1) + \left(\tfrac{1}{x_2} - \tfrac{1}{x_1}\right) = (x_2 - x_1)\left(1 - \tfrac{1}{x_1 x_2}\right).$$
Como $x_2 - x_1 > 0$ y $x_1 x_2 > 1$ (ambos $\ge 1$ y distintos), el segundo factor es positivo. Luego $f(x_2) > f(x_1)$: estrictamente creciente en $[1, \infty)$.

**$f(x) = \dfrac{x}{|x| + 1}$ (Examen, 2026-1).** Es impar. Para $x > y > 0$: $\tfrac{1}{x} < \tfrac{1}{y} \Rightarrow 1 + \tfrac{1}{x} < 1 + \tfrac{1}{y} \Rightarrow \tfrac{x + 1}{x} < \tfrac{y + 1}{y} \Rightarrow \tfrac{x}{x + 1} > \tfrac{y}{y + 1}$: estrictamente creciente en $(0, \infty)$ y, por imparidad, en todo $\mathbb{R}$.

## Paridad y monotonía

> [!tip] Funciones pares e impares
> $f$ es **par** si $f(-x) = f(x)$ (el gráfico es simétrico respecto del eje $y$) e **impar** si $f(-x) = -f(x)$ (simétrico respecto del origen).

Si $f$ es **impar**, la monotonía en $[0, \infty)$ se "refleja" en $(-\infty, 0]$ con el **mismo** sentido: si crece en $(0, \infty)$, crece también en todo $\mathbb{R}$. Si $f$ es **par**, el sentido se invierte entre ambos lados. Por eso las pruebas piden primero la paridad y luego la monotonía solo en $x \ge 0$.

**Ejemplo (I5, 2023-1):** $f(x) = -\dfrac{x}{(3 + x^2)^2}$ es impar. Con $x_1, x_2 \ge 0$,
$$f(x_1) - f(x_2) = -\frac{(x_1 - x_2)\big[9 - x_1 x_2(6 + x_1^2 + x_1 x_2 + x_2^2)\big]}{(3 + x_1^2)^2(3 + x_2^2)^2}.$$
Si $x_1 < x_2$ ambos en $[0, 1]$, el corchete es positivo ($9 - 1\cdot 9 > 0$ estrictamente) y la fracción con signo menos da $f(x_1) > f(x_2)$: decreciente en $[0, 1]$. Si ambos están en $[1, \infty)$, el corchete es negativo y $f(x_1) < f(x_2)$: creciente en $[1, \infty)$. Por imparidad, es decreciente en $[-1, 0]$ y creciente en $(-\infty, -1]$.

> [!warning] "Creciente" no es lo mismo que "estrictamente creciente"
> Una función constante a tramos es creciente (con $\le$) pero no estrictamente, y por tanto no es inyectiva. Las pruebas distinguen ambos casos.

## Preguntas de repaso

> [!question]- ¿Por qué una función estrictamente monótona es inyectiva?
> Porque dos entradas distintas están ordenadas ($x_1 < x_2$), y la monotonía estricta ordena sus imágenes de manera estricta, así que no pueden coincidir.

> [!question]- Si $f$ es impar y estrictamente creciente en $(0, \infty)$, ¿qué se concluye en $\mathbb{R}$?
> Que es estrictamente creciente en todo $\mathbb{R}$: en los negativos se refleja con el mismo sentido y $f(0) = 0$ conecta ambos lados.

> [!question]- ¿Qué factor siempre se puede sacar al calcular $f(x_2) - f(x_1)$ en funciones racionales?
> El factor $(x_2 - x_1)$, que es positivo por hipótesis; queda estudiar el signo del resto.

> [!question]- ¿Es $f(x) = x^3 - x$ monótona en $\mathbb{R}$?
> No: $f(-1) = f(0) = f(1) = 0$, así que no es inyectiva y por tanto tampoco estrictamente monótona.
