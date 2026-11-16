---
ramo: "Introducción al Cálculo"
tema: "Cálculo de límites y límites infinitos"
tags:
  - intro-calculo/limites
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[01 - Sucesiones recursivas y límite por punto fijo]]"
  - "[[02 - Límites infinitos]]"
---

# Ejercicios de prueba de recurrencias y límites infinitos

Las interrogaciones 7 a 9 y los exámenes piden, para sucesiones recursivas, probar la cota y la monotonía y **concluir el límite** con la ecuación del punto fijo. Las preguntas sobre límites infinitos son más breves: una comparación o una acotación que dispare la sucesión.

## Ejercicios

### 1. Recurrencias con límite (I8, 2026-1; I8, 2023-1; I7, 2025-1; I8, 2024-1)
Calcule el límite de (a) $s_1 = 1$, $s_{n+1} = \sqrt{\tfrac{9 + s_n^2}{2}}$; (b) $s_1 = 1$, $s_{n+1} = \sqrt{72 + s_n}$; (c) $a_1 = 1$, $a_{n+1} = 3 - \tfrac{1}{a_n}$; (d) $a_1 = \tfrac{5}{3}$, $a_{n+1} = (a_n - 1)^2 + 1$, sabiendo que cada una es monótona y acotada (probado en [[06 - Ejercicios de prueba de sucesiones recursivas|el tema 08]]).

> [!example]- Solución
> Todas convergen por ser monótonas y acotadas; el límite $L$ cumple $L = f(L)$.
> (a) $L = \sqrt{\tfrac{9 + L^2}{2}} \Rightarrow L^2 = 9$; como $s_n \ge 0$, $L = 3$.
> (b) $L = \sqrt{72 + L} \Rightarrow L^2 - L - 72 = (L - 9)(L + 8) = 0$; como $s_n > 0$, $L = 9$.
> (c) $L = 3 - \tfrac{1}{L} \Rightarrow L^2 - 3L + 1 = 0 \Rightarrow L = \tfrac{3 \pm \sqrt{5}}{2}$; como $a_n \ge 1$, $L = \tfrac{3 + \sqrt{5}}{2}$.
> (d) $L = (L - 1)^2 + 1 \Rightarrow L^2 - 3L + 2 = 0 \Rightarrow L \in \{1, 2\}$; como $a_n$ decrece desde $\tfrac{5}{3} < 2$, $L = 1$. (También se ve con la fórmula $a_n = \left(\tfrac{2}{3}\right)^{2^{n-1}} + 1 \to 1$.)

### 2. La recurrencia de Newton para $\sqrt{2}$ (I9, 2020-1)
Sea $a_1 = 1$, $a_{n+1} = \tfrac{1}{2}\left(a_n + \tfrac{2}{a_n}\right)$. Demuestre que (a) $a_n > 0$, (b) $a_n \ge \sqrt{2}$ para $n \ge 2$ y (c) $a_n \le 2$ para todo $n \ge 1$. Concluya el límite.

> [!example]- Solución
> (a) Si $a_n > 0$, entonces $a_{n+1} = \tfrac{1}{2}\left(a_n + \tfrac{2}{a_n}\right) > 0$.
> (b) Para $n \ge 2$, con $a_{n-1} > 0$ y la desigualdad entre la media aritmética y la geométrica: $2a_n = a_{n-1} + \tfrac{2}{a_{n-1}} \ge 2\sqrt{a_{n-1}\cdot\tfrac{2}{a_{n-1}}} = 2\sqrt{2}$.
> (c) $a_1 = 1 \le 2$ y $a_2 = \tfrac{3}{2} \le 2$. Si $a_k \le 2$ con $k \ge 2$, por (b) $a_k \ge \sqrt{2}$ y $a_{k+1} \le \tfrac{1}{2}\left(2 + \tfrac{2}{\sqrt{2}}\right) = 1 + \tfrac{1}{\sqrt{2}} \le 2$.
> Límite: para $n \ge 2$, $a_{n+1} - a_n = \tfrac{2 - a_n^2}{2a_n} \le 0$: decreciente y acotada inferiormente por $\sqrt{2}$, converge. Con $L = \tfrac{1}{2}\left(L + \tfrac{2}{L}\right)$ resulta $L^2 = 2$ y $L = \sqrt{2}$ (porque $L \ge \sqrt{2} > 0$).

### 3. Subsucesiones pares e impares (Examen, 2024-1)
Sea $x_1 = 1$, $x_{n+1} = 1 + \tfrac{1}{x_n}$. Demuestre que $(x_{2k})$ es decreciente y acotada inferiormente, que $(x_{2k+1})$ es creciente y acotada superiormente, y que ambas convergen al mismo límite.

> [!example]- Solución
> De $x_{n+2} = 1 + \tfrac{1}{1 + 1/x_n} = 2 - \tfrac{1}{1 + x_n}$ resulta que $a_n = x_{2n}$ y $b_n = x_{2n+1}$ cumplen $a_{n+1} = 2 - \tfrac{1}{a_n + 1}$ (y lo mismo $b_n$). Con $a_1 = x_2 = 2$ y $a_2 = x_4 = \tfrac{5}{3}$; la inducción $1 \le a_{n+1} < a_n \le 2 \Rightarrow \tfrac{3}{2} \le a_{n+2} < a_{n+1} \le \tfrac{5}{3}$ prueba que $a_n$ decrece y es $\ge \tfrac{3}{2}$. Análogamente $b_n$ crece (con $b_1 = x_3 = \tfrac{3}{2}$, $b_2 = x_5 = \tfrac{8}{5}$) y está acotada por $2$. Ambas convergen, con límites en $[1, 2]$ que cumplen $L = 2 - \tfrac{1}{1 + L}$, es decir $L^2 - L - 1 = 0$, y la única raíz positiva es $L = \tfrac{1 + \sqrt{5}}{2}$. Luego los dos límites coinciden.

### 4. Una sucesión creciente positiva (Examen, 2025-1)
Sea $\{a_n\}$ de términos positivos y creciente. Demuestre que $b_n = \tfrac{1}{a_n}$ es convergente.

> [!example]- Solución
> De $0 < a_n \le a_{n+1}$ se obtiene $0 < \tfrac{1}{a_{n+1}} \le \tfrac{1}{a_n}$, es decir $0 < b_{n+1} \le b_n$: $\{b_n\}$ es **decreciente** y acotada inferiormente por $0$. Por el teorema de la sucesión monótona, converge.

### 5. Un cociente que se dispara (I9, 2024-1)
Sea $\lim a_n = 1$. Demuestre que $\lim\dfrac{a_n}{\sqrt{n + 1} - \sqrt{n}} = +\infty$.

> [!example]- Solución
> Existe $N$ con $a_n > \tfrac{1}{2}$ para $n > N$. Racionalizando, $\tfrac{1}{\sqrt{n + 1} - \sqrt{n}} = \sqrt{n + 1} + \sqrt{n} > 2\sqrt{n} > 0$. Multiplicando las dos desigualdades, para $n > N$: $\tfrac{a_n}{\sqrt{n + 1} - \sqrt{n}} > \sqrt{n}$, que tiende a $+\infty$. Por comparación, el cociente tiende a $+\infty$.

### 6. Un logaritmo que baja (Examen, 2024-1)
Calcule $\lim\ln\!\left(\dfrac{3n}{\exp(2n)}\right)$.

> [!example]- Solución
> $\ln\!\left(\tfrac{3n}{e^{2n}}\right) = \ln 3 + \ln n - 2n \le \ln 3 + (n - 1) - 2n = \ln 3 - 1 - n$ (usando $\ln n \le n - 1$). La cota superior tiende a $-\infty$, luego el límite es $-\infty$.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 1(d) no vale $L = 2$?
> Porque la sucesión decrece desde $\frac{5}{3}$ y su límite no puede superar el primer término: $L \le \frac{5}{3} < 2$.

> [!question]- ¿Cómo se usa la desigualdad $\ln n \le n - 1$ en el ejercicio 6?
> Para acotar por arriba $\ln 3 + \ln n - 2n$ por $\ln 3 - 1 - n$, que claramente tiende a $-\infty$ y arrastra a la sucesión.

> [!question]- ¿Qué se prueba primero en el ejercicio 2 antes de poder usar la desigualdad de las medias?
> Que $a_{n-1} > 0$ (parte (a)), porque la desigualdad entre la media aritmética y la geométrica exige números positivos.
