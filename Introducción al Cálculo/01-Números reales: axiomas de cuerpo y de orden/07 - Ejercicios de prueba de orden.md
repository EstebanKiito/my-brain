---
ramo: "Introducción al Cálculo"
tema: "Números reales: axiomas de cuerpo y de orden"
tags:
  - intro-calculo/numeros-reales
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Cómo demostrar desigualdades con los axiomas de orden]]"
---

# Ejercicios de prueba de orden

Preguntas de las interrogaciones 1 y 2 y de las interrogaciones 0 de 2020 a 2026. Casi todas piden **demostrar** una desigualdad "usando las propiedades de orden": la pauta puntúa el paso de pasar todo a un lado y factorizar, y luego la conclusión con la cerradura de $\mathbb{R}^+$ o con $a^2 \ge 0$. Escribir cada paso con su justificación vale tanto como el resultado.

## Ejercicios

### 1. Dos desigualdades con cuadrados (I2, 2026-1)
Demuestre, usando las propiedades de orden: (a) $\dfrac{x^2 + x + 1}{3} \ge x$ para todo $x \in \mathbb{R}$. (b) Si $a > b$ y $c > d$, entonces $(a + b)(c + d) < 2(ac + bd)$.

> [!example]- Solución
> (a) $\tfrac{x^2 + x + 1}{3} \ge x \iff x^2 + x + 1 \ge 3x \iff x^2 - 2x + 1 \ge 0 \iff (x - 1)^2 \ge 0$, que es cierto para todo real.
> (b) La diferencia es $2(ac + bd) - (a + b)(c + d) = ac + bd - ad - bc = (a - b)(c - d)$. Como $a - b > 0$ y $c - d > 0$, su producto es positivo, y la desigualdad queda probada.

### 2. $a < b$ implica $a^3 < b^3$ (I1, 2025-2)
Enuncie los axiomas de orden y, solo con ellos y las propiedades de suma y producto, demuestre que si $a < b$, entonces $a^3 < b^3$.

> [!example]- Solución
> Los axiomas son los cuatro de la [[03 - Axiomas de orden y números positivos|nota de orden]]. La pauta separa en casos según los signos ($a > 0$; $a = 0$; $a < 0$ con $b$ negativo, nulo o positivo). Una vía más corta evita los casos: $b^3 - a^3 = (b - a)(a^2 + ab + b^2)$, con $b - a > 0$, y
> $$a^2 + ab + b^2 = \frac{(2a + b)^2 + 3b^2}{4} \ge 0,$$
> que solo vale $0$ si $b = 0$ y $2a + b = 0$, es decir $a = b = 0$, lo que contradice $a < b$. Luego $a^2 + ab + b^2 > 0$ y el producto es positivo.

### 3. Inversos y diferencias (I1, 2023-1)
(a) Si $a, b > 0$ con $a \neq b$, demuestre que $(a + b)(a^{-1} + b^{-1}) > 4$. (b) Si $0 < a < b$, demuestre que $b^{-1} < a^{-1}$.

> [!example]- Solución
> (a) $(a + b)\left(\tfrac{1}{a} + \tfrac{1}{b}\right) = \tfrac{(a + b)^2}{ab}$, y restando $4$: $\tfrac{(a + b)^2 - 4ab}{ab} = \tfrac{(a - b)^2}{ab} = (a - b)^2 a^{-1} b^{-1}$. Como $a \neq b$, $(a - b)^2 > 0$; además $a^{-1}, b^{-1} > 0$. Un producto de positivos es positivo.
> (b) $a^{-1} - b^{-1} = \tfrac{b - a}{ab} = (b - a)a^{-1}b^{-1} > 0$: producto de positivos.

### 4. Hipótesis que fijan signos (I0, 2023-1 y 2020-1)
(a) Si $a < 2$ y $b > 3$, demuestre que $3a + 2b > ab + 6$. (b) Si $x \ge -3$, demuestre que $1 + 3x \le (1 + x)^3$.

> [!example]- Solución
> (a) $2 - a > 0$ y $b - 3 > 0$, luego $(2 - a)(b - 3) = 2b - 6 - ab + 3a > 0$, que reordenado es $3a + 2b > ab + 6$.
> (b) $(1 + x)^3 - (1 + 3x) = 3x^2 + x^3 = x^2(x + 3)$. Si $x = 0$ vale $0$; si no, $x^2 > 0$ y $x + 3 \ge 0$, y el producto es $\ge 0$. La hipótesis $x \ge -3$ es necesaria: con $x = -4$ queda $-11 \le -27$, falso.

### 5. Multiplicar desigualdades y MA-MG (I1, 2024-1)
(a) Si $0 < x < y$ y $0 < w < z$, demuestre que $xw < yz$. (b) Si $a, b, c > 0$, demuestre que $8abc \le (a + b)(b + c)(c + a)$.

> [!example]- Solución
> (a) Por O4 con el positivo $w$: $xw < yw$. Por O4 con el positivo $y$: $yw < yz$. Por transitividad, $xw < yz$.
> (b) Por la desigualdad entre medias, $\sqrt{ab} \le \tfrac{a+b}{2}$, $\sqrt{bc} \le \tfrac{b+c}{2}$, $\sqrt{ca} \le \tfrac{c+a}{2}$, todas con ambos lados positivos. Multiplicando con (a) (con $\le$ en lugar de $<$): $abc \le \tfrac{(a+b)(b+c)(c+a)}{8}$. Directamente: la diferencia es $a(b - c)^2 + b(c - a)^2 + c(a - b)^2 \ge 0$.

### 6. Mayores que 1 y un mínimo (I1, 2025-1)
(a) Si $a > 1$ y $b > 1$, pruebe que $ab + 1 > a + b$. (b) Si $x > 0$, demuestre que $x + \tfrac{9}{x} \ge 6$.

> [!example]- Solución
> (a) $ab + 1 - a - b = (a - 1)(b - 1) > 0$, por ser producto de dos positivos. (La pauta multiplica $a > 1$ por $b - 1 > 0$ y suma términos.)
> (b) $x + \tfrac{9}{x} - 6 = \tfrac{x^2 - 6x + 9}{x} = \tfrac{(x - 3)^2}{x} \ge 0$, con igualdad solo en $x = 3$.

### 7. Una desigualdad en la circunferencia (I1, 2022-2)
Si $a^2 + b^2 = 1$ y $c^2 + d^2 = 1$, demuestre que $ac + bd \le 1$.

> [!example]- Solución
> $(a - c)^2 + (b - d)^2 \ge 0$ se expande en $(a^2 + b^2) + (c^2 + d^2) - 2(ac + bd) \ge 0$. Con las hipótesis, $2 - 2(ac + bd) \ge 0$, o sea $ac + bd \le 1$.

### 8. Promedio de productos (I1, 2022-1)
Si $0 < a < b$ y $0 < c < d$, demuestre que $\tfrac{a + b}{2} \cdot \tfrac{c + d}{2} < \tfrac{ac + bd}{2}$.

> [!example]- Solución
> $\tfrac{ac + bd}{2} - \tfrac{(a + b)(c + d)}{4} = \tfrac{2ac + 2bd - ac - ad - bc - bd}{4} = \tfrac{(a - b)(c - d)}{4}$. Como $a - b < 0$ y $c - d < 0$, el producto de dos negativos es positivo, y la diferencia es positiva.

### 9. Sumar desigualdades (I1, 2023-2)
Si $x < y$ y $z < r$, demuestre que $x + z < y + r$.

> [!example]- Solución
> Por monotonía de la suma, $x + z < y + z$ y $y + z < y + r$; por transitividad, $x + z < y + r$.

## Preguntas de repaso

> [!question]- ¿Qué paso comparten casi todas las soluciones de esta nota?
> Pasar todo a un lado, factorizar o completar cuadrados y concluir con el signo conocido de cada factor (cuadrados no negativos o números positivos por hipótesis).

> [!question]- ¿Por qué en el ejercicio 4(b) hace falta la hipótesis $x \ge -3$?
> Porque la diferencia es $x^2(x + 3)$ y su signo depende de $x + 3$. Si $x < -3$ el factor es negativo y la diferencia es negativa para todo $x \neq 0$.

> [!question]- ¿Cómo se explica que "multiplicar desigualdades" funcione en 5(a) y 8?
> En 5(a) todos los números son positivos, así que se aplica O4 dos veces. En el ejercicio 8 se evita multiplicar desigualdades: se calcula la diferencia y se estudia su signo, que sí es positivo por ser producto de dos negativos.
