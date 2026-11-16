---
ramo: "Introducción al Cálculo"
tema: "Inecuaciones"
tags:
  - intro-calculo/inecuaciones
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Inecuaciones racionales y restricciones]]"
---

# Ejercicios de prueba de inecuaciones racionales

Preguntas de interrogaciones y exámenes de 2020 a 2026 que se resuelven con cocientes y tabla de signos. En las pautas el puntaje se reparte en: pasar todo a un lado y llegar a una sola fracción factorizada, hallar los puntos críticos y restricciones, armar la tabla y escribir bien el conjunto (con los extremos correctos). El error más común es incluir una restricción.

## Ejercicios

### 1. Un cociente contra 1 (Examen, 2020-1)
Resuelva $\dfrac{x^2 - 4}{x - 4} > 1$.

> [!example]- Solución
> $\dfrac{x^2 - 4}{x - 4} - 1 = \dfrac{x^2 - x}{x - 4} = \dfrac{x(x - 1)}{x - 4} > 0$. Puntos críticos $0$, $1$, $4$ (el $4$ es restricción). El cociente es negativo para $x < 0$, positivo en $(0, 1)$, negativo en $(1, 4)$ y positivo para $x > 4$. $S = (0, 1) \cup (4, \infty)$.

### 2. Un cociente contra $-1$ (I1 y Examen, 2022-1; I1, 2023-1)
Resuelva $\dfrac{x^2 + 4x - 12}{x^2 - 6x + 8} \le -1$.

> [!example]- Solución
> Se suma $1$ y se combina: $\dfrac{2x^2 - 2x - 4}{x^2 - 6x + 8} \le 0 \iff \dfrac{2(x - 2)(x + 1)}{(x - 4)(x - 2)} \le 0$. Cancelando $(x - 2)$, queda $\dfrac{x + 1}{x - 4} \le 0$ con $x \neq 2$. El cociente $\dfrac{x + 1}{x - 4}$ es $\le 0$ en $[-1, 4)$. Se excluye $x = 2$: $S = [-1, 2) \cup (2, 4)$.
>
> La pauta de 2023-1 escribe un denominador "$x^2 - 6x - 8$" en una línea intermedia; es una errata de tipeo (la factorización siguiente usa $(x - 4)(x - 2)$ y el resultado es correcto).

### 3. Dos fracciones intercambiadas (I2, 2025-1)
Resuelva $\dfrac{x}{x - 4} < \dfrac{x - 4}{x}$.

> [!example]- Solución
> $\dfrac{x}{x - 4} - \dfrac{x - 4}{x} = \dfrac{x^2 - (x - 4)^2}{x(x - 4)} = \dfrac{8(x - 2)}{x(x - 4)} < 0$. Puntos críticos $0$, $2$, $4$ (restricciones $0$ y $4$):
>
> | Intervalo | $x - 2$ | $x$ | $x - 4$ | cociente |
> |---|:-:|:-:|:-:|:-:|
> | $(-\infty, 0)$ | $-$ | $-$ | $-$ | $-$ |
> | $(0, 2)$ | $-$ | $+$ | $-$ | $+$ |
> | $(2, 4)$ | $+$ | $+$ | $-$ | $-$ |
> | $(4, \infty)$ | $+$ | $+$ | $+$ | $+$ |
>
> Se pide $< 0$: $S = (-\infty, 0) \cup (2, 4)$.

### 4. Un cociente con un cuadrado (I3, 2026-1)
Resuelva $\dfrac{x}{x - 1} \ge \dfrac{x - 1}{x - 2}$.

> [!example]- Solución
> La diferencia es $\dfrac{x(x - 2) - (x - 1)^2}{(x - 1)(x - 2)} = \dfrac{-1}{(x - 1)(x - 2)}$, porque $x^2 - 2x - (x^2 - 2x + 1) = -1$. Se pide $\ge 0$, o sea $\dfrac{1}{(x - 1)(x - 2)} \le 0$, que equivale a $(x - 1)(x - 2) < 0$ (el $0$ no se alcanza). $S = (1, 2)$.

### 5. Un factor siempre positivo (I2, 2024-1)
Resuelva $0 \le \dfrac{(x^2 + 4x + 6)(x - 3)}{x - 4}$.

> [!example]- Solución
> $x^2 + 4x + 6 = (x + 2)^2 + 2 \ge 2 > 0$, así que no afecta el signo. Queda $\dfrac{x - 3}{x - 4} \ge 0$: el numerador y el denominador tienen el mismo signo, o el numerador es cero. $x = 3$ entra y $x = 4$ es restricción. $S = (-\infty, 3] \cup (4, \infty)$.

### 6. Restricciones que se cancelan (Examen, 2024-1)
Resuelva $\dfrac{x^2 + 2x - 15}{x^2 + 7x + 10} \ge 0$.

> [!example]- Solución
> Se factoriza: $\dfrac{(x + 5)(x - 3)}{(x + 5)(x + 2)} \ge 0$. Las restricciones son $x = -5$ y $x = -2$. Para $x \neq -5$ se cancela y queda $\dfrac{x - 3}{x + 2} \ge 0$, cierto si $x < -2$ ó $x \ge 3$. Quitando $x = -5$ (que cae en $x < -2$): $S = (-\infty, -5) \cup (-5, -2) \cup [3, \infty)$.

### 7. Una suma de fracciones (I1, 2025-2)
Resuelva $\dfrac{1}{2x - 1} + \dfrac{1}{x + 2} \ge 1$.

> [!example]- Solución
> Se lleva a un lado: $\dfrac{(x + 2) + (2x - 1) - (2x - 1)(x + 2)}{(2x - 1)(x + 2)} = \dfrac{3 - 2x^2}{(2x - 1)(x + 2)} \ge 0$. Multiplicando por $-1$ ambos lados (se invierte el sentido): $\dfrac{x^2 - \tfrac{3}{2}}{(2x - 1)(x + 2)} \le 0$. Puntos críticos: $-2$, $-\sqrt{3/2}$, $\tfrac{1}{2}$ y $\sqrt{3/2}$ ($\approx -2$, $-1{,}22$, $0{,}5$, $1{,}22$), con restricciones $-2$ y $\tfrac{1}{2}$.
>
> Signos del cociente en $(-\infty, -2)$, $(-2, -\sqrt{3/2})$, $(-\sqrt{3/2}, \tfrac{1}{2})$, $(\tfrac{1}{2}, \sqrt{3/2})$ y $(\sqrt{3/2}, \infty)$: $+,\ -,\ +,\ -,\ +$. Se pide $\le 0$:
> $$S = \left(-2, -\sqrt{3/2}\,\right] \cup \left(\tfrac{1}{2}, \sqrt{3/2}\,\right].$$

### 8. Dos ejercicios de la lista del curso (2022-1)
(a) $\dfrac{4}{x + 1} + \dfrac{5}{2x - 1} \ge 3$. (b) $\dfrac{x + 1}{x - 1} \le x + 2$.

> [!example]- Solución
> (a) Se combina: $\dfrac{4(2x - 1) + 5(x + 1) - 3(x + 1)(2x - 1)}{(x + 1)(2x - 1)} = \dfrac{-2(3x + 1)(x - 2)}{(x + 1)(2x - 1)} \ge 0$, o sea $\dfrac{(3x + 1)(x - 2)}{(x + 1)(2x - 1)} \le 0$. Puntos críticos $-1$, $-\tfrac{1}{3}$, $\tfrac{1}{2}$, $2$ (restricciones $-1$ y $\tfrac{1}{2}$). Signos: $+,\ -,\ +,\ -,\ +$. $S = \left(-1, -\tfrac{1}{3}\right] \cup \left(\tfrac{1}{2}, 2\right]$.
> (b) $\dfrac{x + 1}{x - 1} - (x + 2) = \dfrac{3 - x^2}{x - 1} \le 0 \iff \dfrac{x^2 - 3}{x - 1} \ge 0$. Puntos críticos $-\sqrt{3}$, $1$, $\sqrt{3}$ (restricción $1$). Signos: $-,\ +,\ -,\ +$. $S = [-\sqrt{3}, 1) \cup [\sqrt{3}, \infty)$.

## Preguntas de repaso

> [!question]- ¿Qué se hace con un factor que aparece arriba y abajo, como $(x + 5)$ en el ejercicio 6?
> Se cancela para resolver, pero su cero sigue siendo restricción y se saca del conjunto final.

> [!question]- ¿Por qué en el ejercicio 4 basta estudiar el signo de $(x - 1)(x - 2)$?
> Porque la diferencia de las fracciones es $\frac{-1}{(x-1)(x-2)}$, un numerador constante negativo: su signo depende solo del denominador.

> [!question]- ¿Qué error cometería quien resuelva $\frac{x}{x - 4} < \frac{x - 4}{x}$ multiplicando en cruz?
> Multiplicaría por $x(x - 4)$ sin conocer su signo, y perdería los casos en que ese producto es negativo (donde la desigualdad se invierte).
