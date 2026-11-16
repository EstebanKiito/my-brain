---
ramo: "Introducción al Cálculo"
tema: "Inecuaciones"
tags:
  - intro-calculo/inecuaciones
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Inecuaciones con valor absoluto]]"
  - "[[05 - Inecuaciones con raíces cuadradas]]"
---

# Ejercicios de prueba de inecuaciones con valor absoluto y raíces

Preguntas de interrogaciones y exámenes de 2022 a 2026 con valores absolutos y raíces. La pauta puntúa por separado el dominio (restricciones), la resolución en cada caso y el conjunto final; olvidar el dominio o intersectar mal con cada tramo es lo que más puntos cuesta.

## Ejercicios

### 1. Valor absoluto en un cociente (I3, 2026-1)
Resuelva (a) $\dfrac{x}{|x - 1|} \ge \dfrac{|x - 1|}{x - 2}$ y (b) $\dfrac{3 - 2x}{x^2 - |2x - 3|} \le 0$.

> [!example]- Solución
> (a) Restricciones: $x \neq 1$, $x \neq 2$. Si $x > 1$ se está en la desigualdad $\frac{x}{x - 1} \ge \frac{x - 1}{x - 2}$, que se resolvió ya: $S_2 = (1, 2)$. Si $x < 1$, $|x - 1| = -(x - 1)$ y queda $\frac{x}{x - 1} \le \frac{x - 1}{x - 2}$, la desigualdad **contraria**. Como la diferencia $\frac{-1}{(x-1)(x-2)}$ nunca es cero, es la parte de la recta que no cumple la anterior: para $x < 1$ se cumple siempre, $S_1 = (-\infty, 1)$. $S = (-\infty, 1) \cup (1, 2)$.
> (b) Punto crítico $x = \tfrac{3}{2}$, que **sí** pertenece (el numerador vale $0$ y el denominador $\tfrac{9}{4} \neq 0$). Si $x < \tfrac{3}{2}$: $|2x - 3| = 3 - 2x$ y queda $\frac{3 - 2x}{x^2 + 2x - 3} = \frac{3 - 2x}{(x + 3)(x - 1)} \le 0$; el numerador es positivo, luego $(x + 3)(x - 1) < 0$: $(-3, 1)$. Si $x > \tfrac{3}{2}$: $|2x - 3| = 2x - 3$, el denominador es $x^2 - 2x + 3 > 0$ ($\Delta < 0$) y basta $3 - 2x \le 0$: todo $x > \tfrac{3}{2}$. $S = (-3, 1) \cup \left[\tfrac{3}{2}, \infty\right)$.

### 2. Dos valores absolutos y un denominador (Examen, 2026-1)
Resuelva $\dfrac{\big||x| - |x - 2|\big|}{x^2 - 1} \le 2$.

> [!example]- Solución
> Si $x \in (-1, 1)$, el denominador es negativo y el numerador $\ge 0$, luego el cociente es $\le 0 < 2$: todo $(-1, 1)$ es solución. Fuera, $x \neq \pm 1$ y $x^2 - 1 > 0$.
> - $x < -1$: $|x| - |x - 2| = -x + (x - 2) = -2$, el numerador es $2$ y $\frac{2}{x^2 - 1} \le 2 \iff x^2 \ge 2$; con $x < -1$: $x \le -\sqrt{2}$.
> - $1 < x < 2$: $|x| - |x - 2| = 2x - 2$ y el cociente es $\frac{2}{x + 1} \le 2 \iff x \ge 0$: todo $(1, 2)$.
> - $x \ge 2$: el numerador es $2$ y de nuevo $x^2 \ge 2$: todo $[2, \infty)$.
>
> $S = (-\infty, -\sqrt{2}\,] \cup (-1, 1) \cup (1, \infty)$.

### 3. Valores absolutos de fracciones (I1, 2022-2)
Resuelva $\left|\dfrac{x + 2}{x - 6}\right| - \left|\dfrac{x - 1}{x - 3}\right| < 0$.

> [!example]- Solución
> Restricciones: $x \neq 6$, $x \neq 3$. Con $A = \frac{x + 2}{x - 6}$ y $B = \frac{x - 1}{x - 3}$, $|A| < |B| \iff A^2 < B^2 \iff (A - B)(A + B) < 0$. Se calcula $A - B = \frac{6(x - 2)}{(x - 6)(x - 3)}$ y $A + B = \frac{2x(x - 4)}{(x - 6)(x - 3)}$. Luego
> $$(A - B)(A + B) = \frac{12\,x(x - 2)(x - 4)}{(x - 6)^2(x - 3)^2} < 0 \iff x(x - 2)(x - 4) < 0,$$
> pues los cuadrados son positivos. Esto vale en $(-\infty, 0) \cup (2, 4)$. Quitando la restricción $x = 3$: $S = (-\infty, 0) \cup (2, 3) \cup (3, 4)$.
>
> La pauta entrega $(-\infty, 0) \cup (2, 4)$, que incluye $x = 3$, valor donde la expresión original no está definida.

### 4. Suma de valores absolutos (I1, 2025-2)
Resuelva $3 < |x + 1| + |x - 1|$.

> [!example]- Solución
> Puntos críticos $-1$ y $1$.
> - $x < -1$: $(-1 - x) + (1 - x) = -2x > 3 \iff x < -\tfrac{3}{2}$.
> - $-1 \le x < 1$: $(x + 1) + (1 - x) = 2 > 3$, falso.
> - $x \ge 1$: $(x + 1) + (x - 1) = 2x > 3 \iff x > \tfrac{3}{2}$.
>
> $S = \left(-\infty, -\tfrac{3}{2}\right) \cup \left(\tfrac{3}{2}, \infty\right)$: los puntos cuya suma de distancias a $-1$ y a $1$ supera $3$.

### 5. Valor absoluto y radicales (I2, 2023-1)
Resuelva (a) $|x^2 - 2x| - 5x + 8 > |x^2 - 3x + 4|$ y (b) $\sqrt{3 - 3x} \le \sqrt{21 + 4x - x^2}$.

> [!example]- Solución
> (a) $x^2 - 3x + 4$ tiene discriminante $-7 < 0$ y es siempre positivo, así que $|x^2 - 3x + 4| = x^2 - 3x + 4$. Además $x^2 - 2x = x(x - 2)$ es $\ge 0$ si $x \le 0$ ó $x \ge 2$, y negativa en $(0, 2)$. En $(-\infty, 0] \cup [2, \infty)$: $x^2 - 2x - 5x + 8 > x^2 - 3x + 4 \iff x < 1$; queda $(-\infty, 0]$. En $(0, 2)$: $-(x^2 - 2x) - 5x + 8 > x^2 - 3x + 4 \iff x^2 < 2$; queda $(0, \sqrt{2})$. $S = (-\infty, \sqrt{2})$.
> (b) Dominio: $3 - 3x \ge 0$ ($x \le 1$) y $21 + 4x - x^2 = -(x - 7)(x + 3) \ge 0$ ($x \in [-3, 7]$): $[-3, 1]$. Elevando, $3 - 3x \le 21 + 4x - x^2 \iff (x - 9)(x + 2) \le 0 \iff x \in [-2, 9]$. $S = [-2, 1]$.

### 6. Radicales (I1, 2023-2)
Resuelva (a) $\sqrt{(x + 2)(x + 3)} < \sqrt{2}$ y (b) $\dfrac{|x^2 - 3|\sqrt{2x - 2}}{x^2 - x - 2} \ge 0$.

> [!example]- Solución
> (a) Dominio: $(x + 2)(x + 3) \ge 0 \iff x \le -3$ ó $x \ge -2$. Luego $(x + 2)(x + 3) < 2 \iff x^2 + 5x + 4 < 0 \iff (x + 4)(x + 1) < 0 \iff x \in (-4, -1)$. $S = (-4, -3] \cup [-2, -1)$.
> (b) Dominio: $x \ge 1$ y $x \ne 2$ (el denominador $(x - 2)(x + 1)$). El numerador es $\ge 0$ y vale $0$ solo en $x = 1$ ($\sqrt{0}$) y $x = \sqrt{3}$ ($|x^2 - 3| = 0$), donde el denominador no es cero: ambos son soluciones. Si el numerador es positivo, hace falta denominador positivo: $x > 2$. $S = \{1, \sqrt{3}\} \cup (2, \infty)$.
>
> La pauta entrega $\{1, 3\} \cup (2, \infty)$; el "$3$" es un $\sqrt{3}$ que se perdió al extraer el texto (el $3$ ya pertenece a $(2, \infty)$).

### 7. Raíces contra valor absoluto (I3, 2025-1)
Resuelva $\sqrt{x + 3} > \sqrt{|x - 2|}$.

> [!example]- Solución
> Dominio: $x \ge -3$. Se compara $x + 3 > |x - 2|$. Si $x \le 2$: $x + 3 > 2 - x \iff x > -\tfrac{1}{2}$, es decir $\left(-\tfrac{1}{2}, 2\right]$. Si $x > 2$: $x + 3 > x - 2$ siempre. La unión es $\left(-\tfrac{1}{2}, \infty\right)$, que ya está en el dominio. $S = \left(-\tfrac{1}{2}, \infty\right)$.

### 8. Tres ejercicios de la lista del curso (2022-1)
(a) $\dfrac{\big||x - 1| - 2\big|}{2 + |x|} \ge 1$. (b) $\sqrt{4 - |x + 1|} \le 1$. (c) $\sqrt{2x^2 + x + 3} > 1 - x$.

> [!example]- Solución
> (a) El denominador es positivo, luego equivale a $\big||x - 1| - 2\big| \ge 2 + |x|$, es decir $|x - 1| - 2 \ge 2 + |x|$ ó $|x - 1| - 2 \le -2 - |x|$. La primera dice $|x - 1| \ge 4 + |x|$, imposible porque $|x - 1| \le |x| + 1$. La segunda dice $|x - 1| + |x| \le 0$, que exige $x = 0$ y $x = 1$ a la vez. $S = \varnothing$.
> (b) Dominio: $|x + 1| \le 4$, o sea $x \in [-5, 3]$. Ambos lados son $\ge 0$: $4 - |x + 1| \le 1 \iff |x + 1| \ge 3 \iff x \le -4$ ó $x \ge 2$. $S = [-5, -4] \cup [2, 3]$.
> (c) El radicando $2x^2 + x + 3$ tiene $\Delta = -23 < 0$ y es siempre positivo. Si $x > 1$, $1 - x < 0$ y la desigualdad es cierta. Si $x \le 1$, se eleva al cuadrado: $2x^2 + x + 3 > 1 - 2x + x^2 \iff (x + 1)(x + 2) > 0 \iff x < -2$ ó $x > -1$; con $x \le 1$: $(-\infty, -2) \cup (-1, 1]$. $S = (-\infty, -2) \cup (-1, \infty)$.

## Preguntas de repaso

> [!question]- ¿Qué pasa si se olvida el dominio en $\sqrt{3 - 3x} \le \sqrt{21 + 4x - x^2}$?
> La solución de la cuadrática, $[-2, 9]$, incluiría valores como $x = 5$, que anulan la primera raíz (radicando negativo). El dominio $[-3, 1]$ recorta el resultado a $[-2, 1]$.

> [!question]- ¿Por qué en el ejercicio 3 conviene $A^2 < B^2$ en lugar de dividir las dos fracciones?
> Porque $|A| < |B|$ equivale a $(A - B)(A + B) < 0$ y evita dividir por $B$, que puede anularse. Además las restricciones del enunciado se leen directo de los denominadores.

> [!question]- ¿Cómo se usa la desigualdad triangular en el ejercicio 8(a)?
> $|x - 1| \le |x| + 1$ impide $|x - 1| \ge 4 + |x|$, así que esa rama no tiene solución sin tener que partir en casos.
