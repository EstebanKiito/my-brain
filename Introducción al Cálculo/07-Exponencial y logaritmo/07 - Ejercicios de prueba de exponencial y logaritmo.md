---
ramo: "Introducción al Cálculo"
tema: "Exponencial y logaritmo"
tags:
  - intro-calculo/exponencial
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Ecuaciones exponenciales y logarítmicas]]"
---

# Ejercicios de prueba de exponencial y logaritmo

Preguntas de interrogaciones y exámenes de 2022 a 2026. Aparecen cuatro formatos: ecuaciones, modelos de crecimiento y enfriamiento, demostración de desigualdades con la exponencial y funciones con $\ln$ y $\exp$ cuya inversa se pide. En los modelos la pauta da puntaje por cada constante del modelo.

## Ejercicios

### 1. Ecuaciones exponenciales (I3, 2023-2; I6, 2022-1)
Resuelva (a) $e^{2x} - e^x - 6 = 0$ y (b) $5^x - 25^x = -6$.

> [!example]- Solución
> (a) Con $u = e^x$: $u^2 - u - 6 = (u - 3)(u + 2) = 0$. $e^x = -2$ es imposible; $e^x = 3$ da $x = \ln 3$.
> (b) $25^x = (5^x)^2$; con $u = 5^x$: $u - u^2 = -6 \iff (u - 3)(u + 2) = 0$. $5^x = -2$ es imposible y $5^x = 3$ da $x = \dfrac{\ln 3}{\ln 5}$.

### 2. Ecuaciones logarítmicas (I3, 2023-2; Examen, 2026-1)
Resuelva (a) $\log(x + 1) - \log(x - 1) = 2$ (con $\log = \log_{10}$); (b) $e^x + e^{-x} = 3$; (c) $\log_x a + \log_{x^2} b = c$ con $a, b, c > 0$.

> [!example]- Solución
> (a) $\log\dfrac{x + 1}{x - 1} = 2 \iff \dfrac{x + 1}{x - 1} = 100 \iff 99x = 101$, $x = \tfrac{101}{99} > 1$, así que ambos argumentos son positivos. $x = \tfrac{101}{99}$.
> (b) Multiplicando por $e^x$: $e^{2x} - 3e^x + 1 = 0$, $e^x = \tfrac{3 \pm \sqrt{5}}{2}$ (ambos positivos): $x = \ln\tfrac{3 + \sqrt{5}}{2}$ ó $x = \ln\tfrac{3 - \sqrt{5}}{2}$ (opuestas).
> (c) Se requiere $x > 0$, $x \neq 1$. $\dfrac{\ln a}{\ln x} + \dfrac{\ln b}{2\ln x} = c \iff \ln x = \dfrac{2\ln a + \ln b}{2c}$, o sea $x = (a^2 b)^{1/(2c)}$, válida si $a^2 b \neq 1$ (si $a^2 b = 1$ daría $x = 1$ y no hay solución).

### 3. Crecimiento exponencial (I6, 2022-1)
Una población sigue $N(t) = N_0 e^{0{,}1t}$. ¿En cuánto tiempo se triplica?

> [!example]- Solución
> $3N_0 = N_0 e^{0{,}1t} \Rightarrow 0{,}1t = \ln 3 \Rightarrow t = \dfrac{\ln 3}{0{,}1} = 10\ln 3 \approx 10{,}99$ unidades de tiempo.

### 4. Ley de enfriamiento y hora de una muerte (I3, 2022-2)
La temperatura de un cuerpo en un ambiente a temperatura $C$ sigue $T = f(t) = ae^{-kt} + C$. A las 15:00 el forense mide $30^\circ$C, una hora después $28^\circ$C, y el departamento está a $20^\circ$C. Suponiendo $37^\circ$C en el momento de la muerte, ¿a qué hora murió la persona?

> [!example]- Solución
> Con $t = 0$ a las 15:00: $C = 20$ y $f(0) = a + 20 = 30$, luego $a = 10$. Con $f(1) = 28$: $10e^{-k} + 20 = 28 \Rightarrow e^{-k} = \tfrac{4}{5}$, de modo que $f(t) = 10\left(\tfrac{4}{5}\right)^t + 20$. La muerte ocurrió cuando $f(t) = 37$: $\left(\tfrac{4}{5}\right)^t = \tfrac{17}{10}$, y
> $$t = \frac{\ln(17/10)}{\ln(4/5)} \approx -2{,}378 \text{ horas}.$$
> El signo negativo indica que fue **antes** de las 15:00: unas $2{,}38$ horas antes, es decir alrededor de las 12:37.

### 5. Una desigualdad con exponenciales (I5, 2022-1)
Demuestre que $e^x + e^{-x} \ge 2$ para todo $x \in \mathbb{R}$.

> [!example]- Solución
> Como $e^x > 0$, la desigualdad equivale (multiplicando por $e^x$) a $e^{2x} + 1 \ge 2e^x$, es decir $e^{2x} - 2e^x + 1 = (e^x - 1)^2 \ge 0$, que siempre es cierto. Otra vía: sumar las desigualdades fundamentales $e^x \ge 1 + x$ y $e^{-x} \ge 1 - x$.

### 6. Una función con $\ln$ y $\exp$ (Examen, 2025-1)
Sea $g(x) = \ln(1 + e^x)$. (a) Halle el dominio. (b) Pruebe que es inyectiva. (c) Halle el conjunto $B$ para que $g : A \to B$ sea sobreyectiva. (d) Defina la inversa.

> [!example]- Solución
> (a) $1 + e^x > 0$ siempre, luego $A = \mathbb{R}$.
> (b) Si $g(a) = g(b)$, por la inyectividad de $\ln$ queda $1 + e^a = 1 + e^b$ y por la de $\exp$, $a = b$.
> (c) $y \in \operatorname{Rec}(g) \iff (\exists x)\ e^y = 1 + e^x \iff e^x = e^y - 1$, que tiene solución si y solo si $e^y - 1 > 0$, o sea $y > 0$. $B = (0, \infty)$.
> (d) De $x = \ln(e^y - 1)$: $g^{-1} : (0, \infty) \to \mathbb{R}$, $g^{-1}(x) = \ln(e^x - 1)$.

## Preguntas de repaso

> [!question]- ¿Cómo se interpreta el tiempo negativo del ejercicio 4?
> El instante en que $f(t) = 37$ ocurre antes del momento en que se tomó la primera medición ($t = 0$), así que la muerte fue anterior a las 15:00.

> [!question]- ¿Por qué en el ejercicio 6 el recorrido es $(0, \infty)$ y no $\mathbb{R}$?
> Porque $1 + e^x > 1$ y $\ln$ de un número mayor que $1$ es positivo; $g$ nunca toma valores $\le 0$.

> [!question]- ¿Qué paso comparten los ejercicios 1(a) y 2(b)?
> El cambio de variable $u = e^x$, que convierte la ecuación en una cuadrática en $u$ y permite descartar los valores $u \le 0$.
