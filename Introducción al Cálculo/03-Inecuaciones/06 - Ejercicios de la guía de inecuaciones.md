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

# Ejercicios de la guía de inecuaciones

Los nueve ejercicios de la Guía 3. Los ejercicios 3, 5, 6 y 7 son los ejemplos de las clases 6 y 7, de modo que sus tablas de signos están en las notas de [[03 - Inecuaciones racionales y restricciones|inecuaciones racionales]] y [[04 - Inecuaciones con valor absoluto|con valor absoluto]]. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. Una cuadrática
Resuelva $-2x^2 + 8x + 10 > 0$.

> [!example]- Solución
> Se divide por $-2$ (el sentido se invierte): $x^2 - 4x - 5 < 0 \iff (x - 5)(x + 1) < 0$. El producto es negativo entre las raíces: $S = (-1, 5)$.

### 2. Una raíz acotada
Resuelva $\sqrt{x^2 - 3x} \le 2$.

> [!example]- Solución
> Dominio: $x(x - 3) \ge 0 \iff x \le 0$ ó $x \ge 3$. Como ambos lados son $\ge 0$, se eleva al cuadrado: $x^2 - 3x \le 4 \iff (x - 4)(x + 1) \le 0 \iff x \in [-1, 4]$. Intersectando con el dominio, $S = [-1, 0] \cup [3, 4]$.

### 3. Dos valores absolutos
Resuelva $2|x| < |x - 1|$.

> [!example]- Solución
> Ambos lados son $\ge 0$: $4x^2 < (x - 1)^2 \iff 3x^2 + 2x - 1 < 0 \iff (x + 1)(3x - 1) < 0$. $S = \left(-1, \tfrac{1}{3}\right)$. (Tres métodos en la nota de valor absoluto.)

### 4. Valor absoluto anidado
Resuelva $\big|x^2 - |3 + 2x|\big| < 4$.

> [!example]- Solución
> El punto crítico interior es $x = -\tfrac{3}{2}$.
> - Si $x \ge -\tfrac{3}{2}$: $|3 + 2x| = 3 + 2x$ y la inecuación es $|x^2 - 2x - 3| < 4$, es decir $-4 < x^2 - 2x - 3 < 4$. La izquierda se reduce a $(x - 1)^2 > 0$, o sea $x \neq 1$. La derecha, $x^2 - 2x - 7 < 0$, da $x \in (1 - 2\sqrt{2}, 1 + 2\sqrt{2})$. Con $1 - 2\sqrt{2} \approx -1{,}83 < -\tfrac{3}{2}$, la solución en este caso es $\left[-\tfrac{3}{2}, 1\right) \cup (1, 1 + 2\sqrt{2})$.
> - Si $x < -\tfrac{3}{2}$: $|3 + 2x| = -3 - 2x$ y queda $|x^2 + 2x + 3| < 4$; como $x^2 + 2x + 3 = (x + 1)^2 + 2 > 0$, se reduce a $x^2 + 2x - 1 < 0$, o sea $x \in (-1 - \sqrt{2}, -1 + \sqrt{2})$. Con $x < -\tfrac{3}{2}$: $\left(-1 - \sqrt{2}, -\tfrac{3}{2}\right)$.
>
> Uniendo: $S = (-1 - \sqrt{2}, 1) \cup (1, 1 + 2\sqrt{2})$. El $x = 1$ queda fuera porque $|1 - 5| = 4$ no es menor que $4$.

### 5. Un cociente contra 1
Resuelva $\dfrac{2x + 1}{x + 2} \le 1$.

> [!example]- Solución
> Se reduce a $\dfrac{x - 1}{x + 2} \le 0$ con restricción $x \neq -2$. $S = (-2, 1]$.

### 6. Cociente con tres puntos críticos
Resuelva $\dfrac{x^2 - 8x + 15}{x - 4} < 0$.

> [!example]- Solución
> $\dfrac{(x - 3)(x - 5)}{x - 4} < 0$ con restricción $x \neq 4$. $S = (-\infty, 3) \cup (4, 5)$.

### 7. Una suma con fracciones
Resuelva $3 + \dfrac{1}{x - 1} > \dfrac{1}{2x + 1}$.

> [!example]- Solución
> Equivale a $\dfrac{6x^2 - 2x - 1}{(x - 1)(2x + 1)} > 0$, con raíces del numerador $\tfrac{1 \pm \sqrt{7}}{6}$ y restricciones $1$ y $-\tfrac{1}{2}$. $S = \left(-\infty, -\tfrac{1}{2}\right) \cup \left(\tfrac{1 - \sqrt{7}}{6}, \tfrac{1 + \sqrt{7}}{6}\right) \cup (1, \infty)$.

### 8. Un cociente que nunca es negativo
Resuelva $\dfrac{\sqrt{x^2 + 2}}{|x^2 + 1|} < 0$.

> [!example]- Solución
> El numerador es $\ge \sqrt{2} > 0$ y el denominador, $|x^2 + 1| = x^2 + 1 \ge 1 > 0$. El cociente es positivo para todo $x$, luego nunca es $< 0$: $S = \varnothing$.

### 9. Pasar todo a un lado
Resuelva $x^2 \le 5x - 6$.

> [!example]- Solución
> $x^2 - 5x + 6 \le 0 \iff (x - 2)(x - 3) \le 0$. $S = [2, 3]$.

## Preguntas de repaso

> [!question]- ¿Qué cambia al dividir por $-2$ en el ejercicio 1?
> El sentido de la desigualdad: de $-2(\ldots) > 0$ se pasa a $(\ldots) < 0$.

> [!question]- ¿Por qué en el ejercicio 4 el caso $x = 1$ se excluye pero $x = -\tfrac{3}{2}$ no?
> Porque en $x = 1$ la expresión vale exactamente $4$ y la desigualdad es estricta; en $x = -\tfrac{3}{2}$ vale $\tfrac{9}{4}$, que es menor que $4$ (es solo un cambio de fórmula para el valor absoluto interior).

> [!question]- ¿Cómo se ve sin cálculo que el ejercicio 8 no tiene solución?
> Un cociente de números positivos es positivo; un resultado negativo no puede aparecer.
