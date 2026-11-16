---
ramo: "Introducción al Cálculo"
tema: "Gestión del curso"
tags:
  - intro-calculo/gestion
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[01 - Mapa de evaluaciones de Cálculo]]"
---

# Ejercicios de la tarea de 2022-1

En 2022-1 hubo una tarea de seis problemas que mezcla varios temas: una desigualdad geométrica, una inecuación con valor absoluto, una función monótona, una función definida por tramos con inversa, un límite con cociente de términos consecutivos y el método de los babilonios para $\sqrt{a}$. Es una buena preparación **integradora** del examen.

## Ejercicios

### 1. Una desigualdad del triángulo
Sean $a$, $b$ y $c$ los lados de un triángulo y $A$ su área. Demuestre que $a^2 + b^2 + c^2 \ge 4\sqrt{3}\,A$.

> [!example]- Solución
> Se toma $a$ como el lado mayor, con el triángulo apoyado en la base $a$ de extremos $B = (0, 0)$ y $C = (a, 0)$, y altura $h$ desde $A$. Sea $P$ el punto medio de la base y $x$ el desplazamiento horizontal del pie de la altura respecto de $P$. Por Pitágoras, $b^2 = \left(\tfrac{a}{2} + x\right)^2 + h^2$ y $c^2 = \left(\tfrac{a}{2} - x\right)^2 + h^2$ (con $x$ de signo adecuado). Como la altura del triángulo equilátero de lado $a$ es $\tfrac{\sqrt{3}}{2}a$, se define $y = \tfrac{\sqrt{3}}{2}a - h$, lo que le "falta" a $h$ para ser equilátero. Con $A = \tfrac{ah}{2}$:
> $$a^2 + b^2 + c^2 - 4\sqrt{3}\,A = \tfrac{3}{2}a^2 + 2x^2 + 2h^2 - 2\sqrt{3}\,ah = 2(x^2 + y^2) \ge 0.$$
> La igualdad ocurre si y solo si $x = y = 0$, es decir, si el triángulo es **equilátero**.

### 2. Una inecuación con valor absoluto
Resuelva $\left|\dfrac{|x - 2| - 3}{|x| - 1}\right| \ge 4$.

> [!example]- Solución
> Las restricciones son $x \neq \pm 1$. La inecuación equivale a $\big||x - 2| - 3\big| \ge 4\,\big||x| - 1\big|$. Los puntos críticos son $-1$, $0$, $1$, $2$ y $5$ (donde cambian de signo $x$, $|x| - 1$, $x - 2$ y $|x - 2| - 3$); se resuelve por casos:
> - $(-\infty, -1)$: $-(x - 2) - 3 \ge 4(-x - 1) \iff x \ge -\tfrac{3}{4}$: sin solución en el tramo.
> - $(-1, 0)$: la desigualdad queda $x \le -1$: sin solución.
> - $[0, 1)$: queda $x \ge \tfrac{3}{5}$: solución $\left[\tfrac{3}{5}, 1\right)$.
> - $(1, 2)$: queda $x \le \tfrac{5}{3}$: solución $\left(1, \tfrac{5}{3}\right]$.
> - $[2, 5)$ y $[5, \infty)$: quedan $x \le \tfrac{9}{5}$ y $x \le -\tfrac{1}{3}$: sin solución.
>
> $S = \left[\tfrac{3}{5}, 1\right) \cup \left(1, \tfrac{5}{3}\right]$.

### 3. Una función monótona y acotada
Sea $f : (-1, \infty) \to \mathbb{R}$, $f(x) = \dfrac{x}{1 + x}$. (a) Pruebe que es estrictamente creciente. (b) Demuestre que está acotada superiormente.

> [!example]- Solución
> (a) Para $-1 < x < y$: $f(y) - f(x) = \dfrac{y}{y + 1} - \dfrac{x}{x + 1} = \dfrac{y - x}{(x + 1)(y + 1)} > 0$, porque $y - x > 0$, $x + 1 > 0$ y $y + 1 > 0$.
> (b) Como $x < x + 1$ y $x + 1 > 0$, se divide: $\dfrac{x}{x + 1} < 1$. Luego $f(x) < 1$ para todo $x > -1$: está acotada superiormente por $1$.

### 4. Funciones inyectivas y la función $h$
Sean $f(x) = \begin{cases} 2 - x^2 & \sqrt{3} \le x \le 2 \\ 1 - \sqrt{x^2 - 4} & x \le -4 \end{cases}$ y $g(x) = \sqrt{|x^2 - 4| - 3}$, con $f = h^{-1} \circ g$. (a) Demuestre que $f$ y $g$ son inyectivas. (b) Halle $h$.

> [!example]- Solución
> (a) **$f$:** en $[\sqrt{3}, 2]$, $2 - x_1^2 = 2 - x_2^2$ implica $x_1^2 = x_2^2$ y, siendo positivos, $x_1 = x_2$; en $(-\infty, -4]$, $\sqrt{x_1^2 - 4} = \sqrt{x_2^2 - 4}$ implica $|x_1| = |x_2|$ y, siendo negativos, $x_1 = x_2$. Entre ramas, $f(x_1) = f(x_2)$ con $x_1 \in [\sqrt{3}, 2]$ y $x_2 \le -4$ exigiría $x_2^2 \in [8, 13]$, contradicción con $x_2 \le -4$ (que da $x_2^2 \ge 16$). **$g$** se inyecta de manera análoga: en $[0, 1]$ vale $\sqrt{1 - x^2}$ y en $(-\infty, -2\sqrt{2})$ vale $\sqrt{x^2 - 7}$; las igualdades entre ramas obligarían a $7 \le x_2^2 \le 8$, fuera de la rama.
> (b) De $f = h^{-1} \circ g$ resulta $h = g \circ f^{-1}$. En la rama $x \le -4$, $f(x) = 1 - \sqrt{x^2 - 4}$ tiene inversa $f^{-1}(y) = -\sqrt{(1 - y)^2 + 4}$ y entonces
> $$h(y) = g\big(f^{-1}(y)\big) = \sqrt{\big|(1 - y)^2 + 4 - 4\big| - 3} = \sqrt{(1 - y)^2 - 3}, \qquad y \le 1 - \sqrt{12}.$$
> Se verifica: $h(f(x)) = \sqrt{(x^2 - 4) - 3} = \sqrt{x^2 - 7} = g(x)$.
>
> El enunciado es inconsistente en la otra rama ($x \in [\sqrt{3}, 2]$ cae fuera del dominio de $g$, pues allí $|x^2 - 4| - 3 < 0$); la relación $f = h^{-1} \circ g$ solo tiene sentido para $x \le -4$.

### 5. La razón de términos consecutivos
Demuestre que si $x_n > 0$ y $\lim\tfrac{x_{n+1}}{x_n} = a < 1$, entonces $\lim x_n = 0$.

> [!example]- Solución
> Se elige $c$ con $a < c < 1$. Existe $N$ con $\tfrac{x_{n+1}}{x_n} \le c$ para $n \ge N$, así que $0 < x_{n+1} \le c\,x_n \le \dots \le c^{\,n - N + 1}x_N \to 0$ (porque $0 < c < 1$). Por el sándwich, $x_n \to 0$. (También: la sucesión es decreciente y acotada por $0$, converge a $b \ge 0$ y de $b \le cb$ resulta $b = 0$.) Este es el ejercicio 10 de la Guía 10, resuelto en [[06 - Ejercicios de la guía de límites de sucesiones|su nota]].

### 6. El método de los babilonios
Para $a > 0$ se toma $x_1 > 0$ y $x_{n+1} = \tfrac{1}{2}\left(x_n + \tfrac{a}{x_n}\right)$. (a) Calcule $\sqrt{11}$ con seis decimales exactos con $x_1 = 1$. (b) Demuestre que $x_n \to \sqrt{a}$.

> [!example]- Solución
> (a) Con $a = 11$: $x_2 = \tfrac{1}{2}(1 + 11) = 6$; $x_3 = \tfrac{47}{12} \approx 3{,}9167$; $x_4 = \tfrac{3793}{1128} \approx 3{,}362589$; $x_5 \approx 3{,}316939$; $x_6 \approx 3{,}316625$ y $x_7 \approx 3{,}316624790$. Como $\sqrt{11} = 3{,}31662479\ldots$, el valor $x_6 = 3{,}316624\ldots$ ya coincide hasta los seis decimales.
> (b) Es la recurrencia de Newton de la nota de [[01 - Sucesiones recursivas y límite por punto fijo|sucesiones recursivas]]: por la desigualdad entre las medias, $x_n \ge \sqrt{a}$ para $n \ge 2$; además $x_{n+1} - x_n = \tfrac{a - x_n^2}{2x_n} \le 0$, así que decrece y está acotada inferiormente: converge a un $L$ con $L = \tfrac{1}{2}\left(L + \tfrac{a}{L}\right)$, es decir $L^2 = a$ y $L = \sqrt{a}$.

## Preguntas de repaso

> [!question]- ¿En qué caso se da la igualdad en la desigualdad del ejercicio 1?
> Solo si $x = y = 0$: el triángulo es equilátero.

> [!question]- ¿Qué permite resolver el ejercicio 2 por tramos?
> Marcar los puntos donde cambian de signo las expresiones dentro de los valores absolutos ($-1, 0, 1, 2, 5$) y resolver la desigualdad sin barras en cada tramo, intersecando con el tramo.

> [!question]- ¿Por qué el ejercicio 6 converge tan rápido?
> Cada paso de Newton duplica aproximadamente el número de decimales correctos: $x_5 \approx 3{,}316939$ tiene $3$ decimales exactos y $x_6$ tiene $6$.
