---
ramo: "Introducción al Cálculo"
tema: "Cálculo de límites y límites infinitos"
tags:
  - intro-calculo/limites
  - origen/complemento
prerrequisitos:
  - "[[03 - Unicidad, acotación y sucesiones monótonas]]"
  - "[[06 - Ejercicios de prueba de sucesiones recursivas]]"
---

# Sucesiones recursivas y límite por punto fijo

Una sucesión definida por recurrencia, como $a_{n+1} = \tfrac{1}{2}(a_n + 6)$, no tiene fórmula explícita para $a_n$; sin embargo, su límite se calcula casi sin trabajo si se sabe que **existe**. El método es siempre el mismo: probar monotonía y cota por inducción (nota [[02 - Sucesiones acotadas y monótonas|de sucesiones acotadas y monótonas]]), concluir convergencia con el teorema de la sucesión monótona y calcular el límite pasando al límite en la recurrencia.

## El método

> [!tip] Cuatro pasos
> 1. **Cota:** probar por inducción que la sucesión está acotada (superiormente si crece, inferiormente si decrece).
> 2. **Monotonía:** probar por inducción (o con $a_{n+1} - a_n$) que es creciente o decreciente.
> 3. **Convergencia:** por el teorema, una sucesión monótona y acotada converge a un límite $L$.
> 4. **Punto fijo:** tomar límite a ambos lados de $a_{n+1} = f(a_n)$; como $a_{n+1}$ y $a_n$ tienen el mismo límite, $L = f(L)$. Se resuelve la ecuación y se **descarta** la raíz incompatible con las cotas.

El teorema garantiza que el límite existe; la ecuación $L = f(L)$ solo dice cuál es **si** existe. Plantearla sin probar antes la convergencia es un error de razonamiento (el límite supuesto puede no existir).

## Ejemplo 1: una recurrencia lineal (clase 24)

$a_1 = 2$, $a_{n+1} = \tfrac{1}{2}(a_n + 6)$. **Creciente:** $a_2 = 4 > a_1$; si $a_{k+1} > a_k$, sumando $6$ y multiplicando por $\tfrac{1}{2}$, $a_{k+2} > a_{k+1}$. **Acotada:** $a_1 < 6$ y si $a_k < 6$ entonces $a_{k+1} = \tfrac{1}{2}(a_k + 6) < \tfrac{12}{2} = 6$. **Límite:** como converge, $L = \tfrac{1}{2}(L + 6)$ y de ahí $L = 6$.

## Ejemplo 2: raíces anidadas (clase 24)

$a_1 = \sqrt{2}$, $a_{n+1} = \sqrt{2 + a_n}$. Por inducción, $a_n < 2$ y $a_n$ crece (por ser $\sqrt{2 + x}$ creciente y $a_2 > a_1$). La ecuación $L = \sqrt{2 + L}$ da $L^2 - L - 2 = 0$, es decir $L = 2$ ó $L = -1$; se descarta $-1$ porque $a_n > 0$. El límite es $2$.

## Más ejemplos de las pruebas

| Recurrencia | Cota y monotonía | Ecuación del punto fijo | Límite |
|---|---|---|---|
| $s_1 = 1$, $s_{n+1} = \sqrt{\tfrac{9 + s_n^2}{2}}$ (I8, 2026-1) | creciente, $s_n \le 3$ | $L^2 = \tfrac{9 + L^2}{2}$ | $L = 3$ |
| $s_1 = 1$, $s_{n+1} = \sqrt{72 + s_n}$ (I8, 2023-1) | estrictamente creciente, $s_n < 9$ | $L^2 = 72 + L$ | $L = 9$ ($L = -8$ se descarta) |
| $a_1 = 1$, $a_{n+1} = 3 - \tfrac{1}{a_n}$ (I7, 2025-1) | creciente, $a_n \le 3$ | $L^2 - 3L + 1 = 0$ | $L = \tfrac{3 + \sqrt{5}}{2}$ (porque $L \ge 1$) |
| $a_1 = \tfrac{5}{3}$, $a_{n+1} = (a_n - 1)^2 + 1$ (I8, 2024-1) | decreciente, $a_n \ge 1$ | $L^2 - 3L + 2 = 0$ | $L = 1$ ($L = 2$ no, pues $a_n \le \tfrac{5}{3}$) |

En cada caso la raíz que se descarta es la que viola una cota que la sucesión ya satisface: el límite de una sucesión **hereda** las cotas ($a_n \ge m \Rightarrow L \ge m$).

## Ejemplo con la media de Newton ($\sqrt{2}$)

$a_1 = 1$, $a_{n+1} = \tfrac{1}{2}\left(a_n + \tfrac{2}{a_n}\right)$ (I9, 2020-1). Es positiva por inducción. Para $n \ge 2$, por la desigualdad entre la media aritmética y la geométrica, $a_n = \tfrac{1}{2}\left(a_{n-1} + \tfrac{2}{a_{n-1}}\right) \ge \sqrt{a_{n-1}\cdot\tfrac{2}{a_{n-1}}} = \sqrt{2}$. Además $a_n \le 2$ por inducción: $a_{n+1} \le \tfrac{1}{2}\left(2 + \tfrac{2}{\sqrt{2}}\right) = 1 + \tfrac{1}{\sqrt{2}} < 2$. La recurrencia es decreciente a partir de $a_2$ (porque $a_n^2 \ge 2$) y el punto fijo es $L = \tfrac{1}{2}\left(L + \tfrac{2}{L}\right)$, es decir $L^2 = 2$: la sucesión converge a $\sqrt{2}$. Es el método de Heron para aproximar raíces.

## Subsucesiones (Examen, 2024-1)

Si una sucesión oscila, a veces las **subsucesiones** de índices pares e impares son monótonas. Para $x_1 = 1$, $x_{n+1} = 1 + \tfrac{1}{x_n}$ se obtiene $x_{n+2} = 1 + \tfrac{1}{1 + 1/x_n} = 2 - \tfrac{1}{1 + x_n}$. Entonces $a_n = x_{2n}$ y $b_n = x_{2n+1}$ cumplen la misma recurrencia $a_{n+1} = 2 - \tfrac{1}{a_n + 1}$; por inducción $a_n$ **decrece** (con $a_1 = x_2 = 2$, $a_2 = \tfrac{5}{3}$) y está acotada por abajo por $\tfrac{3}{2}$, y $b_n$ **crece** (con $b_1 = x_3 = \tfrac{3}{2}$, $b_2 = x_5 = \tfrac{8}{5}$) y está acotada por arriba por $2$. Ambas convergen, y la ecuación $L = 2 - \tfrac{1}{1 + L}$ da $L^2 - L - 1 = 0$, de modo que las dos tienden a $L = \tfrac{1 + \sqrt{5}}{2}$ (la raíz positiva): la sucesión completa converge al número áureo.

> [!warning] Errores frecuentes
> - **Calcular el límite antes de probar que converge:** la ecuación $L = f(L)$ podría tener solución aunque la sucesión no converja.
> - **No descartar la raíz extra:** casi siempre la ecuación del punto fijo tiene dos soluciones; solo una es compatible con las cotas.
> - **Probar monotonía sin la cota:** el signo de $a_{n+1} - a_n$ depende, en general, de que $a_n$ esté en cierto rango.

## Preguntas de repaso

> [!question]- ¿Qué se obtiene de pasar al límite en $a_{n+1} = \sqrt{2 + a_n}$?
> $L = \sqrt{2 + L}$, ya que tanto $a_{n+1}$ como $a_n$ tienen límite $L$. De ahí $L^2 - L - 2 = 0$ y $L = 2$.

> [!question]- ¿Por qué hay que probar antes que la sucesión es convergente?
> Porque el paso al límite supone que $\lim a_n$ existe. Si no existe, la ecuación del punto fijo no dice nada sobre la sucesión.

> [!question]- ¿Cómo se elige entre las dos raíces de $L^2 - 3L + 2 = 0$?
> Con las cotas: si la sucesión decrece desde $\frac{5}{3}$ y es $\ge 1$, su límite está en $[1, \frac{5}{3}]$, así que $L = 1$ y no $L = 2$.

> [!question]- ¿Qué hace útil estudiar los términos pares e impares por separado?
> A veces cada subsucesión es monótona (una crece y otra decrece) aunque la sucesión completa oscile; si ambas convergen al mismo límite, la sucesión converge a él.
