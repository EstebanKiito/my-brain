---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - origen/complemento
prerrequisitos:
  - "[[05 - Funciones racionales y asíntotas]]"
  - "[[02 - Inecuaciones polinomiales y tabla de signos]]"
---

# Cómo graficar una función racional

El bosquejo de una función racional es casi mecánico: se reúnen cinco datos (factorización, cortes con los ejes, asíntotas verticales con su comportamiento lateral, asíntota horizontal y signos) y se une todo con una curva. Es una de las preguntas más repetidas de las interrogaciones 3 y 4, con puntaje por cada dato.

## Los cinco pasos

> [!tip] Método
> 1. **Factorizar** numerador y denominador (y simplificar factores comunes, anotando los huecos).
> 2. **Cortes con los ejes:** los ceros del numerador (cortes con el eje $x$) y $f(0)$ (corte con el eje $y$, si $0$ está en el dominio).
> 3. **Asíntotas verticales:** los ceros del denominador; con la **tabla de signos** se ve si $y \to +\infty$ o $-\infty$ a cada lado.
> 4. **Asíntota horizontal:** por la comparación de grados.
> 5. **Trazar** la curva respetando todo lo anterior.

La tabla de signos es la de las inecuaciones racionales: los puntos críticos son los ceros de numerador y denominador, y entre ellos el signo del cociente es el producto de los signos de los factores. Cerca de una asíntota vertical, el signo a cada lado indica hacia dónde se escapa la curva.

## Ejemplo 3 (clase 12): $r(x) = \dfrac{2x^2 + 7x - 4}{x^2 + x - 2}$

1. **Factorizar:** $r(x) = \dfrac{(2x - 1)(x + 4)}{(x - 1)(x + 2)}$.
2. **Cortes:** ceros en $x = \tfrac{1}{2}$ y $x = -4$; con el eje $y$, $r(0) = \tfrac{-4}{-2} = 2$.
3. **Asíntotas verticales:** $x = 1$ y $x = -2$.
4. **Asíntota horizontal:** mismos grados, $y = \tfrac{2}{1} = 2$.
5. **Signos** (puntos críticos $-4$, $-2$, $\tfrac{1}{2}$, $1$):

| Intervalo | $(-\infty, -4)$ | $(-4, -2)$ | $(-2, \tfrac{1}{2})$ | $(\tfrac{1}{2}, 1)$ | $(1, \infty)$ |
|---|:-:|:-:|:-:|:-:|:-:|
| $2x - 1$ | $-$ | $-$ | $-$ | $+$ | $+$ |
| $x + 4$ | $-$ | $+$ | $+$ | $+$ | $+$ |
| $x - 1$ | $-$ | $-$ | $-$ | $-$ | $+$ |
| $x + 2$ | $-$ | $-$ | $+$ | $+$ | $+$ |
| $r(x)$ | $+$ | $-$ | $+$ | $-$ | $+$ |

Lectura del gráfico: para $x < -4$ está sobre el eje $x$, cruza en $-4$ y baja hacia $-\infty$ al acercarse a $x = -2$ por la izquierda; reaparece por arriba, desde $+\infty$ a la derecha de $-2$, y baja cruzando el eje $x$ en $x = \tfrac{1}{2}$ hacia $-\infty$ en $x = 1^{-}$; a la derecha de $1$ viene desde $+\infty$ y decrece hacia la asíntota $y = 2$.

> [!tip] Una asíntota horizontal sí se puede cruzar
> Aquí $r(x) = 2 \iff 2x^2 + 7x - 4 = 2x^2 + 2x - 4 \iff x = 0$: el gráfico corta la recta $y = 2$ justo en el punto $(0, 2)$. La asíntota horizontal describe lo que ocurre cuando $|x|$ es muy grande, no impide pasar por esa altura antes. En cambio, una asíntota **vertical** nunca se cruza (la función no está definida ahí).

**Dominio y recorrido:** $\operatorname{Dom}(r) = \mathbb{R} \setminus \{-2, 1\}$. Para $y \neq 2$, la ecuación $y = r(x)$ equivale a $(y - 2)x^2 + (y - 7)x - 2y + 4 = 0$, cuyo discriminante $9y^2 - 46y + 81$ es siempre positivo (su propio discriminante es negativo), y ninguna de sus soluciones cae en $\{-2, 1\}$; el valor $y = 2$ se alcanza en $x = 0$. Por eso $\operatorname{Rec}(r) = \mathbb{R}$: los saltos de las asíntotas verticales hacen que la función tome todos los valores.

## Ejemplo 4 (clase 12): $r(x) = \dfrac{5x + 21}{x^2 + 10x + 25}$

1. **Factorizar:** $r(x) = \dfrac{5x + 21}{(x + 5)^2}$.
2. **Cortes:** cero en $x = -\tfrac{21}{5}$; $r(0) = \tfrac{21}{25}$.
3. **Asíntota vertical:** $x = -5$. Como $(x + 5)^2 > 0$ a ambos lados y el numerador vale $5(-5) + 21 = -4 < 0$ cerca de $-5$, $y \to -\infty$ por ambos lados (la curva "se hunde").
4. **Asíntota horizontal:** el grado del numerador ($1$) es menor que el del denominador ($2$): $y = 0$.
5. **Signos:** negativo para $x < -\tfrac{21}{5}$, positivo para $x > -\tfrac{21}{5}$ (con $x \neq -5$). Para $x \to -\infty$ se acerca a $0$ por debajo; para $x \to +\infty$, por encima.

**Dominio y recorrido:** $\operatorname{Dom}(r) = \mathbb{R} \setminus \{-5\}$. Despejando, $y(x + 5)^2 = 5x + 21$ da $yx^2 + (10y - 5)x + 25y - 21 = 0$ y su discriminante es $25 - 16y$, no negativo si $y \le \tfrac{25}{16}$ (con $y = 0$ alcanzado en $x = -\tfrac{21}{5}$). El máximo $\tfrac{25}{16}$ se alcanza en $x = -\tfrac{17}{5}$. $\operatorname{Rec}(r) = \left(-\infty, \tfrac{25}{16}\right]$.

## Qué esperan las pautas

El puntaje típico se reparte así: factorizar (1 punto), signos (1), ceros y corte con el eje $y$ (1), asíntotas verticales (1), asíntota horizontal (1) y el gráfico que incluya todo (2). La pauta de 2020 pide además los **límites laterales** en la asíntota vertical (por ejemplo, $y \to +\infty$ cuando $x \to \tfrac{1}{2}^+$).

> [!warning] Errores frecuentes
> - Omitir la tabla de signos: sin ella no se sabe hacia dónde se escapa la curva en cada asíntota.
> - Declarar asíntota vertical un cero del denominador que se cancela con el numerador.
> - Pensar que la curva no puede cruzar la asíntota horizontal.
> - Olvidar el corte con el eje $y$ cuando $0$ está en el dominio.

## Preguntas de repaso

> [!question]- ¿Cómo se determina hacia dónde se escapa la curva en una asíntota vertical?
> Con el signo de la función a cada lado de la asíntota, dado por la tabla de signos: si es positivo, $y \to +\infty$; si es negativo, $y \to -\infty$.

> [!question]- ¿Puede un gráfico cruzar su asíntota horizontal?
> Sí. La asíntota describe el comportamiento cuando $|x| \to \infty$; antes la función puede pasar por esa altura (como $\frac{2x^2 + 7x - 4}{x^2 + x - 2}$ en $x = 0$).

> [!question]- ¿Cuál es el cero y el corte con el eje $y$ de $\frac{5x + 21}{(x + 5)^2}$?
> El cero es $x = -\frac{21}{5}$ y el corte con el eje $y$ es $(0, \frac{21}{25})$.

> [!question]- ¿Por qué no hay corte con el eje $y$ si $x = 0$ es asíntota vertical?
> Porque $0$ no pertenece al dominio: la función no está definida en $x = 0$.
