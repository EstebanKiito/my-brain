---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[06 - Cómo graficar una función racional]]"
---

# Ejercicios de prueba de funciones racionales

El bosquejo de una función racional es una pregunta de casi todas las interrogaciones 3 y 4 de 2020 a 2026. El puntaje se reparte entre factorizar, la tabla de signos, ceros y corte con el eje $y$, asíntota vertical, asíntota horizontal y el gráfico. Las soluciones muestran los datos que debe tener el dibujo (las pautas traen el gráfico terminado).

## Ejercicios

### 1. Dos ceros y dos asíntotas verticales (Examen, 2023-1)
Para $r(x) = \dfrac{2x^2 + 7x - 4}{x^2 + x - 2}$ determine los ceros, signos y el corte con el eje $y$; las asíntotas verticales y horizontales; y trace el gráfico.

> [!example]- Solución
> $r(x) = \dfrac{(2x - 1)(x + 4)}{(x - 1)(x + 2)}$. Ceros: $-4$ y $\tfrac{1}{2}$. Corte con el eje $y$: $r(0) = 2$. Asíntotas verticales: $x = 1$ y $x = -2$. Asíntota horizontal: $y = \tfrac{2}{1} = 2$ (mismo grado). Signos en $(-\infty, -4)$, $(-4, -2)$, $(-2, \tfrac{1}{2})$, $(\tfrac{1}{2}, 1)$, $(1, \infty)$: $+, -, +, -, +$. Es el ejemplo 3 de la clase 12: el desarrollo completo, con la tabla y la lectura del gráfico, está en [[06 - Cómo graficar una función racional|la nota del método]].

### 2. Un solo cero y grado menor abajo (I4, 2023-1)
Para $r(x) = \dfrac{x - 1}{x^2 - x - 6}$ determine ceros, signos y corte con el eje $y$; asíntotas; y grafique.

> [!example]- Solución
> $r(x) = \dfrac{x - 1}{(x - 3)(x + 2)}$. Cero: $x = 1$. Corte con el eje $y$: $r(0) = \tfrac{-1}{-6} = \tfrac{1}{6}$. Asíntotas verticales: $x = 3$ y $x = -2$. Asíntota horizontal: $y = 0$ (el grado del numerador, $1$, es menor que el del denominador, $2$).
> Signos, con puntos críticos $-2$, $1$, $3$: $-$ en $(-\infty, -2)$, $+$ en $(-2, 1)$, $-$ en $(1, 3)$ y $+$ en $(3, \infty)$. Lectura: por la izquierda baja desde $0^-$ hacia $-\infty$ en $x = -2^-$; viene desde $+\infty$ a la derecha de $-2$, cruza el eje $x$ en $1$ y baja a $-\infty$ en $x = 3^-$; a la derecha de $3$ parte desde $+\infty$ y decrece hacia $0^+$.

### 3. Con un cero que es asíntota (I4, 2025-1)
Para $f(x) = \dfrac{x^2 - 3x - 4}{2x^2 + 4x}$: (a) asíntotas verticales; (b) asíntotas horizontales; (c) grafique; (d) ¿es inyectiva?

> [!example]- Solución
> $f(x) = \dfrac{(x - 4)(x + 1)}{2x(x + 2)}$.
> (a) Asíntotas verticales: $x = 0$ y $x = -2$ (ceros del denominador que no se cancelan).
> (b) Los grados coinciden: asíntota horizontal $y = \tfrac{1}{2}$.
> (c) Ceros: $4$ y $-1$. No hay corte con el eje $y$ ($0$ no está en el dominio). Signos con puntos críticos $-2$, $-1$, $0$, $4$: $+, -, +, -, +$.
> (d) **No es inyectiva**: $f(-1) = f(4) = 0$ con $-1 \neq 4$. (También se ve con el test de la recta horizontal.)

### 4. Una raíz doble en el denominador (I3, 2022-1; I4, 2024-1)
Para $r(x) = \dfrac{5x + 20}{x^2 + 10x + 25}$: (a) asíntotas verticales; (b) asíntotas horizontales; (c) grafique; (d) ¿es inyectiva?

> [!example]- Solución
> $r(x) = \dfrac{5(x + 4)}{(x + 5)^2}$.
> (a) El denominador se anula en $x = -5$ y el numerador no (se anula en $-4$): no hay cancelación y $x = -5$ es asíntota vertical. Como $(x + 5)^2 > 0$ y el numerador es $-5 < 0$ cerca de $-5$, $r \to -\infty$ por ambos lados.
> (b) Grado del numerador menor que el del denominador: $y = 0$.
> (c) Cero en $x = -4$, corte con el eje $y$ en $r(0) = \tfrac{20}{25} = \tfrac{4}{5}$. Negativa para $x < -4$ (salvo en $-5$) y positiva para $x > -4$. Viene de $0^-$, se hunde hacia $-\infty$ en $x = -5$, reaparece desde $-\infty$, cruza en $-4$, sube a un máximo y baja hacia $0^+$.
> (d) No es inyectiva: $r(\sqrt{15}) = r(-\sqrt{15}) = \tfrac{1}{2}$ (de $r(x) = \tfrac{1}{2} \iff 10x + 40 = x^2 + 10x + 25 \iff x^2 = 15$).

### 5. Dos ceros y dos asíntotas, asíntota en $y = 1$ (I2, 2025-2)
Determine ceros, signos y asíntotas de $f(x) = \dfrac{x^2 + 2x - 8}{x^2 - 4x + 3}$ y bosqueje su gráfico.

> [!example]- Solución
> $f(x) = \dfrac{(x + 4)(x - 2)}{(x - 1)(x - 3)}$. Ceros: $-4$ y $2$. Asíntotas verticales: $x = 1$ y $x = 3$. Para la horizontal, dividiendo por $x^2$: $f(x) = \dfrac{1 + 2/x - 8/x^2}{1 - 4/x + 3/x^2} \to 1$ cuando $|x| \to \infty$: $y = 1$ en ambos extremos. Signos con puntos críticos $-4$, $1$, $2$, $3$: $+, -, +, -, +$. Corte con el eje $y$: $f(0) = -\tfrac{8}{3}$.

### 6. Bilineal con límites laterales (I4, 2020-1)
Esboce la gráfica de $f(x) = \dfrac{x + 2}{2x - 1}$ identificando asíntotas y límites laterales.

> [!example]- Solución
> Asíntota horizontal: mismos grados, $y = \tfrac{1}{2}$. Asíntota vertical: $x = \tfrac{1}{2}$. Cerca de $\tfrac{1}{2}$ el numerador vale $\tfrac{5}{2} > 0$ y el denominador es pequeño: $\lim_{x \to 1/2^+} f(x) = +\infty$ (denominador $0^+$) y $\lim_{x \to 1/2^-} f(x) = -\infty$ (denominador $0^-$). Cero en $x = -2$; corte con el eje $y$ en $f(0) = -2$. Esta función jamás vale $\tfrac{1}{2}$ (la ecuación daría $2x + 4 = 2x - 1$), de modo que no cruza su asíntota horizontal. Es $\dfrac{1}{2} + \dfrac{5/2}{2x - 1}$: $\tfrac{1}{x}$ alargada en factor $\tfrac{5}{4}$, trasladada $\tfrac{1}{2}$ a la derecha y $\tfrac{1}{2}$ hacia arriba.

## Preguntas de repaso

> [!question]- ¿Cómo se prueba en el ejercicio 3 que $f$ no es inyectiva sin graficar?
> Mostrando dos entradas distintas con la misma imagen: $f(-1) = 0 = f(4)$.

> [!question]- ¿Qué dos datos de una tabla de signos determinan hacia dónde se escapa la curva en una asíntota vertical?
> El signo de $r$ a la izquierda y a la derecha de la asíntota. En el ejercicio 6, a la izquierda de $\tfrac{1}{2}$ es negativo (la curva cae a $-\infty$) y a la derecha es positivo.

> [!question]- ¿Por qué en el ejercicio 4 la curva cae a $-\infty$ por ambos lados de $x = -5$?
> Porque el denominador $(x + 5)^2$ es positivo a ambos lados y el numerador es negativo cerca de $-5$ ($5(-5) + 20 = -5$): el cociente tiende a $-\infty$ desde los dos lados.
