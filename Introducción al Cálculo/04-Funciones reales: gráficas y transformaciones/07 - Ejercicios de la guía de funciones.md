---
ramo: "Introducción al Cálculo"
tema: "Funciones reales: gráficas y transformaciones"
tags:
  - intro-calculo/funciones
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Cómo hallar el recorrido de una función]]"
  - "[[04 - Funciones elementales y funciones por tramos]]"
---

# Ejercicios de la guía de funciones

Los tres ejercicios de la Guía 4: dominios, recorridos y gráficos de funciones por tramos. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. Dominios
Determine el dominio de (a) $f(x) = \sqrt{16 - x^2}$; (b) $f(x) = \sqrt{\dfrac{x^2 + 2}{x - 1}}$; (c) $f(x) = \dfrac{\sqrt{x^2 - 4}}{x^3 - 1}$; (d) $f(x) = \dfrac{x^5 - 4x^4 + 7x + 8}{\sqrt{(x - 8)(x + 5)}}$.

> [!example]- Solución
> (a) $16 - x^2 \ge 0 \iff -4 \le x \le 4$: $[-4, 4]$.
> (b) Como $x^2 + 2 > 0$, el cociente es $\ge 0$ exactamente cuando $x - 1 > 0$ (el denominador no puede ser $0$): $(1, \infty)$.
> (c) Se necesita $x^2 - 4 \ge 0$ (esto es, $x \le -2$ ó $x \ge 2$) y $x^3 \neq 1$, o sea $x \neq 1$, que ya no está en el conjunto anterior: $(-\infty, -2] \cup [2, \infty)$.
> (d) El numerador es un polinomio, sin restricción. La raíz exige $(x - 8)(x + 5) \ge 0$ y, por estar en el denominador, $> 0$: $x < -5$ ó $x > 8$. $(-\infty, -5) \cup (8, \infty)$.

### 2. Recorridos
Determine el recorrido de (a) $f(x) = \tfrac{1}{x}$; (b) $f(x) = 1 + \tfrac{1}{x}$; (c) $f(x) = 3x^2 + 6x + 1$; (d) $f(x) = \sqrt{2x + 8}$; (e) $f(x) = \dfrac{2x + 3}{x - 1}$.

> [!example]- Solución
> (a) $y = \tfrac{1}{x}$ se despeja como $x = \tfrac{1}{y}$, que existe si y solo si $y \neq 0$: $\mathbb{R} \setminus \{0\}$.
> (b) $y = 1 + \tfrac{1}{x} \Rightarrow x = \tfrac{1}{y - 1}$, posible si $y \neq 1$: $\mathbb{R} \setminus \{1\}$.
> (c) $f(x) = 3(x + 1)^2 - 2$: parábola que abre hacia arriba con vértice $(-1, -2)$. Recorrido $[-2, \infty)$.
> (d) Dominio $[-4, \infty)$. $y = \sqrt{2x + 8}$ exige $y \ge 0$; y para todo $y \ge 0$, $x = \tfrac{y^2 - 8}{2} \ge -4$ está en el dominio. Recorrido $[0, \infty)$.
> (e) De $y(x - 1) = 2x + 3$ resulta $x(y - 2) = y + 3$. Si $y \neq 2$, $x = \tfrac{y + 3}{y - 2}$. Si $y = 2$ la ecuación queda $0 = 5$, imposible. Recorrido $\mathbb{R} \setminus \{2\}$. (La recta $y = 2$ es la asíntota horizontal.)

### 3. Gráficos por tramos
Grafique (a) $f(x) = \begin{cases} x^2 & x < 2 \\ 4x + 5 & x \ge 2 \end{cases}$ y (b) $f(x) = \begin{cases} -x^2 & x < -2 \\ -8x - 7 & x \ge -2 \end{cases}$.

> [!example]- Solución
> (a) Hasta $x = 2$ es la parábola $y = x^2$, que llega al punto $(2, 4)$ con **punto vacío** (porque $x = 2$ no pertenece a ese tramo). Desde $x = 2$ es la recta $y = 4x + 5$, que comienza en $(2, 13)$ con punto lleno. Hay un salto de $4$ a $13$. El recorrido es $[0, \infty)$, porque el tramo parabólico ya cubre $[0, \infty)$ al tomar $x$ muy negativo.
> (b) Para $x < -2$, la parábola que abre hacia abajo $y = -x^2$, que llega a $(-2, -4)$ con punto vacío. Desde $x = -2$, la recta decreciente $y = -8x - 7$, que parte en $(-2, 9)$ con punto lleno. Salto de $-4$ a $9$. Recorrido: $(-\infty, -4) \cup (-\infty, 9] = (-\infty, 9]$.

## Preguntas de repaso

> [!question]- ¿Por qué en 1(c) no hace falta excluir $x = 1$ por el denominador?
> Porque $x = 1$ ya está excluido por la raíz: $1^2 - 4 < 0$ y la raíz no existe. Las restricciones se intersectan y la del radicando es más fuerte.

> [!question]- ¿Cómo se ve en 2(e) que $y = 2$ no pertenece al recorrido?
> Al despejar, $y = 2$ lleva a $0 = 5$: no existe $x$ con $f(x) = 2$. Es la altura hacia la que se acerca la función en el infinito, sin alcanzarla.

> [!question]- ¿Qué se marca en un extremo de tramo cuando los dos tramos no empalman?
> Punto lleno en el valor del tramo al que pertenece el extremo y punto vacío en el valor límite del otro tramo: el gráfico da un salto.
