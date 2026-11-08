---
ramo: "Introducción al Álgebra"
tema: "Polinomios: división y algoritmo de Euclides"
tags:
  - intro-algebra/polinomios
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - División de polinomios]]"
  - "[[03 - Teorema del resto]]"
---

# Ejercicios de prueba de división de polinomios

Preguntas de interrogaciones anteriores. Las de división casi nunca piden solo dividir: piden un resto sin hacer la división, o encontrar parámetros para que la división sea exacta. Las herramientas son siempre dos: el algoritmo de la división $P = D \cdot Q + R$ con $\operatorname{grado}(R) < \operatorname{grado}(D)$ y el teorema del resto.

## Ejercicios

### 1. Tres restos del mismo polinomio
Sea $P(x) = x^4 - 2x^3 - 3x^2 + 8x - 4$. Determine el resto de dividir $P$ por (a) $x^2 - 2x + 3$, (b) $x - 1$, (c) $x - 3$.

> [!example]- Solución
> (a) Divisor de grado $2$: hay que hacer la división larga.
> $$x^4 - 2x^3 - 3x^2 + 8x - 4 = (x^2 - 2x + 3)(x^2 - 6) + (-4x + 14).$$
> El primer paso resta $x^2(x^2 - 2x + 3)$ y deja $-6x^2 + 8x - 4$; el segundo resta $-6(x^2 - 2x + 3)$ y deja $-4x + 14$, de grado menor que $2$. Resto: $-4x + 14$.
> (b) Teorema del resto: $P(1) = 1 - 2 - 3 + 8 - 4 = 0$. Resto $0$ (así que $x - 1$ es factor).
> (c) $P(3) = 81 - 54 - 27 + 24 - 4 = 20$. Con Horner: coeficientes $1, -2, -3, 8, -4$ y $c = 3$ dan $1, 1, 0, 8, \mathbf{20}$.

### 2. Resto desconocido a partir de valores
Al dividir $p(x)$ por $x^2 + 1$ se obtiene cociente $x^2 - x - 6$ y un resto $r(x)$ de grado $1$. Determine $r(x)$ si $p(-2) = 2$ y $p(3) = 1$.

> [!example]- Solución
> Con $r(x) = Ax + B$: $p(x) = (x^2 + 1)(x^2 - x - 6) + Ax + B$. El truco es que $x^2 - x - 6 = (x - 3)(x + 2)$ se anula **justo** en $-2$ y en $3$, así que en esos puntos $p$ coincide con el resto:
> $$-2A + B = 2, \qquad 3A + B = 1.$$
> Restando, $5A = -1$: $A = -\frac{1}{5}$ y $B = \frac{8}{5}$. Resto: $r(x) = -\frac{1}{5}x + \frac{8}{5}$.
>
> Con los datos $p(-2) = 3$ y $p(3) = -1$ (otra versión de la misma pregunta) sale $r(x) = -\frac{4}{5}x + \frac{7}{5}$.

### 3. Parámetros para una división exacta
Determine $a, b \in \mathbb{R}$ para que $p(x) = -x^4 + 6x^3 - 10x^2 + ax + b$ sea divisible por $x^2 - 4x + 5$.

> [!example]- Solución
> Se divide dejando $a$ y $b$ como letras:
> $$p(x) = (x^2 - 4x + 5)(-x^2 + 2x + 3) + (a + 2)x + (b - 15).$$
> Divisible significa resto nulo **como polinomio**: los dos coeficientes son cero, $a + 2 = 0$ y $b - 15 = 0$. Entonces $a = -2$, $b = 15$.

### 4. Un factor lineal con parámetro
Determine $k \in \mathbb{R}$ para que $x + 3$ sea factor de $p(x) = x^3 + kx^2 - kx + 9$.

> [!example]- Solución
> $x + 3$ es factor si y solo si el resto $p(-3)$ es $0$: $-27 + 9k + 3k + 9 = 12k - 18 = 0$, así que $k = \frac{3}{2}$.

## Preguntas de repaso

> [!question]- En el ejercicio 2, ¿por qué no hace falta conocer $p$ completo?
> Porque en $x = -2$ y $x = 3$ el producto $(x^2 + 1)(x^2 - x - 6)$ vale $0$, y $p$ coincide con el resto. Dos valores bastan para las dos incógnitas $A$ y $B$.

> [!question]- ¿Qué significa que el resto sea "el polinomio nulo"?
> Que **todos** sus coeficientes son cero. Por eso un resto $(a+2)x + (b-15)$ da dos ecuaciones, no una.

> [!question]- ¿Cuándo conviene el teorema del resto y cuándo la división larga?
> El teorema del resto, cuando el divisor es lineal $x - c$. Si el divisor tiene grado $2$ o más, hay que dividir o plantear el resto con incógnitas y evaluar en las raíces del divisor.
