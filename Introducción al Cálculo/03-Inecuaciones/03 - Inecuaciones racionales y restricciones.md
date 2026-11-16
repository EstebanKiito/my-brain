---
ramo: "Introducción al Cálculo"
tema: "Inecuaciones"
tags:
  - intro-calculo/inecuaciones
  - origen/complemento
prerrequisitos:
  - "[[02 - Inecuaciones polinomiales y tabla de signos]]"
---

# Inecuaciones racionales y restricciones

Cuando la incógnita aparece en un denominador, hay una trampa que no existe en las polinomiales: no se puede "pasar multiplicando" el denominador, porque su signo es desconocido. La regla es dejar siempre un cociente comparado con $0$ y usar la tabla de signos, recordando que los ceros del denominador son **restricciones** que jamás pertenecen al conjunto solución.

## Un único cociente comparado con cero

> [!tip] Pasos
> 1. Llevar todo a un lado y **combinar en una sola fracción** (denominador común).
> 2. Factorizar numerador y denominador.
> 3. Puntos críticos: ceros del numerador (pueden incluirse si la desigualdad es $\le$ ó $\ge$) y ceros del denominador (siempre se excluyen).
> 4. Tabla de signos del cociente y elección de los intervalos.

## Ejemplo: una restricción en la frontera

$\dfrac{2x + 1}{x + 2} \le 1$. Se pasa el $1$: $\dfrac{2x + 1}{x + 2} - 1 \le 0 \iff \dfrac{(2x + 1) - (x + 2)}{x + 2} \le 0 \iff \dfrac{x - 1}{x + 2} \le 0$. Los puntos críticos son $x = 1$ (numerador) y $x = -2$ (**restricción**, porque anula el denominador).

![Tabla de signos de (x−1)/(x+2)](adjuntos/Tabla%20de%20signos%20de%20un%20cociente%20con%20una%20restricción.png)

> [!example]- Transcripción de la tabla (clase 6)
> Las filas son los factores $x + 2$ y $x - 1$ y las columnas los intervalos $(-\infty, -2)$, $(-2, 1)$ y $(1, \infty)$. Signos de $x + 2$: $-, +, +$. Signos de $x - 1$: $-, -, +$. Signos del cociente: $+, -, +$. Como se pide $\le 0$, la solución es el tramo del medio.

Se pide $\le 0$: el cociente es negativo en $(-2, 1)$ y vale $0$ en $x = 1$ (que se incluye), pero $x = -2$ no se puede incluir. Luego $S = (-2, 1]$.

## Ejemplo: tres puntos críticos y una restricción en medio

$\dfrac{x^2 - 8x + 15}{x - 4} < 0$. Factorizando, $\dfrac{(x - 3)(x - 5)}{x - 4} < 0$, con puntos críticos $3$, $4$ y $5$ y restricción $x \neq 4$.

![Tabla de signos de (x−3)(x−5)/(x−4)](adjuntos/Tabla%20de%20signos%20de%20un%20cociente%20con%20tres%20puntos%20críticos.png)

> [!example]- Transcripción de la tabla (clase 6)
> Filas $x - 3$, $x - 4$ y $x - 5$ en los intervalos $(-\infty, 3)$, $(3, 4)$, $(4, 5)$ y $(5, \infty)$. Signos de $x - 3$: $-, +, +, +$. De $x - 4$: $-, -, +, +$. De $x - 5$: $-, -, -, +$. Signos del cociente: $-, +, -, +$. Se pide $< 0$, así que valen el primer y el tercer intervalo.

La solución es $S = (-\infty, 3) \cup (4, 5)$.

## Ejemplo: raíces irracionales y cuatro factores

$3 + \dfrac{1}{x - 1} > \dfrac{1}{2x + 1}$. Se lleva a un lado y se combina:
$$\frac{3(x - 1)(2x + 1) + (2x + 1) - (x - 1)}{(x - 1)(2x + 1)} > 0 \iff \frac{6x^2 - 2x - 1}{(x - 1)(2x + 1)} > 0.$$
Las raíces del numerador son $x_{1,2} = \tfrac{1 \mp \sqrt{7}}{6}$ ($\approx -0{,}27$ y $0{,}61$), así que el numerador factoriza como $6(x - x_1)(x - x_2)$. Los puntos críticos, en orden, son $-\tfrac{1}{2},\ x_1,\ x_2,\ 1$; las restricciones, $x \neq -\tfrac{1}{2}$ y $x \neq 1$.

![Tabla de signos con cuatro factores](adjuntos/Tabla%20de%20signos%20con%20cuatro%20factores%20y%20raíces%20irracionales.png)

> [!example]- Transcripción de la tabla (clase 6)
> Cinco intervalos y cuatro factores: $x - x_1$ ($-, -, +, +, +$), $x - x_2$ ($-, -, -, +, +$), $x - 1$ ($-, -, -, -, +$) y $2x + 1$ ($-, +, +, +, +$). El cociente tiene signos $+, -, +, -, +$ en $(-\infty, -\tfrac{1}{2})$, $(-\tfrac{1}{2}, x_1)$, $(x_1, x_2)$, $(x_2, 1)$ y $(1, \infty)$.

Se pide $> 0$: $S = \left(-\infty, -\tfrac{1}{2}\right) \cup \left(\tfrac{1 - \sqrt{7}}{6}, \tfrac{1 + \sqrt{7}}{6}\right) \cup (1, \infty)$.

## Cancelar factores: la restricción sigue ahí

En $\dfrac{x^2 + 4x - 12}{x^2 - 6x + 8} \le -1$ se llega a $\dfrac{2(x - 2)(x + 1)}{(x - 4)(x - 2)} \le 0$. Cancelar $(x - 2)$ da $\dfrac{x + 1}{x - 4} \le 0$, **pero** $x = 2$ anulaba el denominador original y sigue siendo restricción: $S = [-1, 4) \setminus \{2\} = [-1, 2) \cup (2, 4)$.

> [!warning] Dos trampas de las pautas
> - Una restricción nunca entra al conjunto solución, ni siquiera cuando el punto crítico se cancela.
> - Para comparar dos fracciones, $\frac{a}{b} \ge \frac{c}{d}$ **no** equivale a $ad \ge bc$ salvo que $bd > 0$; lo seguro es restar y estudiar el signo del cociente.

## Preguntas de repaso

> [!question]- ¿Por qué no se puede multiplicar por el denominador en $\frac{x}{x - 4} < \frac{x - 4}{x}$?
> Porque $x(x - 4)$ puede ser positivo o negativo según $x$, y al multiplicar por un negativo la desigualdad cambiaría de sentido. Se resta, se combina en una fracción y se usa la tabla de signos.

> [!question]- ¿Qué puntos críticos pueden pertenecer al conjunto solución en $\frac{P}{Q} \ge 0$?
> Solo los ceros del numerador (donde el cociente vale exactamente $0$). Los ceros del denominador son restricciones y quedan fuera.

> [!question]- ¿Cómo se simplifica la solución cuando un factor aparece en numerador y denominador?
> Se cancela para resolver, pero se recuerda su cero como restricción y se saca del conjunto final: $\frac{(x-2)(x+1)}{(x-2)(x-4)} \le 0$ se reduce a $\frac{x+1}{x-4} \le 0$ con $x \neq 2$.

> [!question]- ¿Cuántos intervalos tiene la tabla si hay $n$ puntos críticos distintos?
> $n + 1$ intervalos: dos no acotados en los extremos y $n - 1$ entre ellos.
