---
ramo: "Introducción al Álgebra"
tema: "Cuantificadores y negación"
tags:
  - intro-algebra/cuantificadores
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Orden de los cuantificadores]]"
  - "[[04 - Negación de cuantificadores]]"
---

# Ejercicios de prueba de cuantificadores

Preguntas de interrogaciones y exámenes anteriores. Casi siempre se pide **negar** y luego **decidir** cuál es verdadera, la proposición o su negación, demostrándola. En las pautas la negación y la demostración puntúan por separado: una negación correcta vale aunque se elija mal cuál es verdadera.

## Ejercicios

### 1. Negar y decidir (I)
Escriba la negación y demuestre la proposición o su negación:
(a) $(\forall x \in \mathbb{R})(x > 2 \Rightarrow x \ge 3)$. (b) $(\forall x \in \mathbb{R})\big(x < 3 \vee (\exists y \in \mathbb{R})(xy = 3)\big)$. (c) $(\exists x \in \mathbb{R})(\forall y \in \mathbb{R})(x > y \Rightarrow x^2 < y^2)$.

> [!example]- Solución
> (a) Negación: $(\exists x \in \mathbb{R})(x > 2 \wedge x < 3)$. Es la verdadera, con el testigo $x = \sqrt 5$ (o $x = 2{,}5$).
> (b) Negación: $(\exists x \in \mathbb{R})\big(x \ge 3 \wedge (\forall y \in \mathbb{R})(xy \neq 3)\big)$. La original es verdadera: si $x < 3$ se cumple la primera parte; si $x \ge 3$, entonces $x \neq 0$ y $y = 3/x$ sirve.
> (c) Negación: $(\forall x \in \mathbb{R})(\exists y \in \mathbb{R})(x > y \wedge x^2 \ge y^2)$. La original es verdadera con $x = 0$: si $0 > y$, entonces $y < 0$ y $y^2 > 0 = x^2$.

### 2. Negar y decidir (II)
Igual que el anterior: (a) $(\exists x \in \mathbb{R})(x^2 - 2x < 0)$. (b) $(\forall x \in \mathbb{N})(\forall y \in \mathbb{N})\big(x + y \text{ par} \Rightarrow (x \text{ par} \wedge y \text{ par})\big)$. (c) $(\exists x \in \mathbb{N})(\forall y \in \mathbb{R})(y^2 \ge x \vee |y| < 1)$.

> [!example]- Solución
> (a) Negación: $(\forall x \in \mathbb{R})(x^2 - 2x \ge 0)$. La original es verdadera: $x = \frac{1}{2}$ da $\frac{1}{4} - 1 = -\frac{3}{4} < 0$.
> (b) Negación: $(\exists x \in \mathbb{N})(\exists y \in \mathbb{N})\big(x + y \text{ par} \wedge (x \text{ impar} \vee y \text{ impar})\big)$. La negación es verdadera: $x = y = 1$.
> (c) Negación: $(\forall x \in \mathbb{N})(\exists y \in \mathbb{R})(y^2 < x \wedge |y| \ge 1)$. La original es verdadera con $x = 1$: si $|y| \ge 1$, entonces $y^2 \ge 1$; así que para todo $y$ vale $|y| < 1$ o $y^2 \ge 1$.

### 3. El orden importa (dominio finito)
Sean $X = \{0, 1, 2\}$, $Y = \{0, 1, 2, 3, 4\}$ y $P(x, y)$: "$x \ge y$". Determine el valor de verdad de
(a) $[(\forall x \in X)(\exists y \in Y)P(x, y)] \Rightarrow [(\exists x \in X)(\forall y \in Y)P(x, y)]$;
(b) $[(\forall y \in Y)(\exists x \in X)P(x, y)] \Rightarrow [(\exists y \in Y)(\forall x \in X)P(x, y)]$.

> [!example]- Solución
> Se evalúan las cuatro piezas por separado:
> - $(\forall x)(\exists y)\,x \ge y$: **V**, con $y = 0$ para todo $x$.
> - $(\exists x)(\forall y)\,x \ge y$: **F**, el mayor $x$ es $2$ y no supera a $y = 3$.
> - $(\forall y)(\exists x)\,x \ge y$: **F**, para $y = 3$ ningún $x \in X$ sirve.
> - $(\exists y)(\forall x)\,x \ge y$: **V**, con $y = 0$.
>
> (a) $V \Rightarrow F$: **falsa**. (b) $F \Rightarrow V$: **verdadera**.

### 4. $\forall\exists$ contra $\exists\forall$
Decida si son verdaderas; si una es falsa, escriba su negación y demuéstrela: (a) $(\forall x \in \mathbb{N})(\exists y \in \mathbb{N})(x \le y)$. (b) $(\exists y \in \mathbb{N})(\forall x \in \mathbb{N})(x \le y)$.

> [!example]- Solución
> (a) Verdadera: dado $x$ arbitrario, $y = x$ cumple $x \le y$.
> (b) Falsa (diría que hay un natural máximo). Negación: $(\forall y \in \mathbb{N})(\exists x \in \mathbb{N})(x > y)$, verdadera: dado $y$, el testigo $x = y + 1$ cumple $x > y$.

### 5. Deducir el valor de $p$
(a) Si $(\forall x \in U)(p \Rightarrow q(x))$ es falsa, determine el valor de verdad de $p$. (b) Si $A = \{1, 2, 3, 4\}$, determine el valor de verdad de $(\forall x \in A)(\exists y \in A)(x^2 + y \text{ es par})$.

> [!example]- Solución
> (a) Su negación es verdadera: $(\exists x \in U)\,\neg(p \Rightarrow q(x)) \equiv (\exists x \in U)(p \wedge \neg q(x))$. Si existe un $x$ con $p \wedge \neg q(x)$ verdadera, en particular $p = V$.
> (b) Verdadera, revisando cada $x$: para $x$ impar ($1$ y $3$), $x^2$ es impar y $y = 1$ da suma par ($2$ y $10$); para $x$ par ($2$ y $4$), $y = 2$ da $6$ y $18$.

### 6. Negar con una implicación dentro
Niegue $(\forall x \in A)(\exists y \in B)(x + y > 2 \Rightarrow x < 5)$.

> [!example]- Solución
> $$\neg(\forall x \in A)(\exists y \in B)(x + y > 2 \Rightarrow x < 5) \equiv (\exists x \in A)(\forall y \in B)\big(x + y > 2 \wedge x \ge 5\big).$$
> Cada cuantificador cambia y la implicación se niega como "antecedente y no consecuente".

### 7. Cuantificadores con una operación nueva
Sea $U = \mathbb{Z}$, $A = \{-3, -2, -1, 5\}$, $B$ el conjunto de los pares, y $a \star b = a + 5b$. Determine el valor de verdad de: (a) si $a, b \in B$, entonces $a \star b \in B$; (b) $(\forall x \in A)(\exists y \in U)(x + y = 0)$.

> [!example]- Solución
> (a) Verdadera: si $a = 2m$ y $b = 2n$, entonces $a \star b = 2m + 10n = 2(m + 5n)$, par.
> (b) Verdadera: para cada $x \in A$, el testigo es $y = -x \in \mathbb{Z}$ (es decir, $3, 2, 1, -5$).

## Preguntas de repaso

> [!question]- ¿Cómo se demuestra que una proposición $(\forall x)(\exists y)$ es falsa?
> Demostrando su negación $(\exists x)(\forall y)\,\neg p$: se exhibe un $x$ concreto y se prueba que **ningún** $y$ sirve para él.

> [!question]- Si $(\forall x)(\exists y)P$ es verdadera, ¿lo es $(\exists y)(\forall x)P$?
> No necesariamente: en el ejercicio 4, cada natural tiene uno mayor o igual, pero no hay uno mayor o igual que todos. La implicación válida es la contraria: $(\exists y)(\forall x) \Rightarrow (\forall x)(\exists y)$.

> [!question]- ¿Cuál es la negación de $(\forall x)(p(x) \Rightarrow q(x))$?
> $(\exists x)(p(x) \wedge \neg q(x))$: existe un caso que cumple la hipótesis y no la tesis, es decir, un contraejemplo.
