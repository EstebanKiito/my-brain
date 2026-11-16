---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - origen/complemento
prerrequisitos:
  - "[[04 - Factorizar un polinomio con división y teorema del factor]]"
  - "[[06 - Reflexiones y transformaciones sucesivas]]"
---

# Funciones racionales y asíntotas

Una función racional es un cociente de polinomios. A diferencia de los polinomios, puede "dispararse" cerca de ciertos valores de $x$ y "estabilizarse" cuando $x$ crece mucho; esas dos conductas se describen con las asíntotas verticales y horizontales, y marcan la forma de todo el gráfico.

## Definición y dominio

> [!tip] Función racional
> Es $f(x) = \dfrac{P(x)}{Q(x)}$ con $P$ y $Q$ polinomios. Su dominio es $\operatorname{Dom}(f) = \mathbb{R} \setminus \{x : Q(x) = 0\}$.

## Asíntotas

> [!tip] Asíntota vertical
> La recta $x = a$ es una **asíntota vertical** de $y = f(x)$ si $y \to +\infty$ o $y \to -\infty$ cuando $x$ se acerca a $a$ por la derecha o por la izquierda.

![Asíntotas verticales de una función racional](adjuntos/Asíntotas%20verticales%20de%20una%20función%20racional.png)

> [!example]- Transcripción de la figura (clase 12)
> Cuatro gráficos con una recta vertical punteada $x = a$ y una curva pegada a ella. Los dos primeros muestran $y \to \infty$ cuando $x \to a^+$ (curva que baja desde arriba hacia la derecha de la recta) y $y \to \infty$ cuando $x \to a^-$ (curva que sube hacia arriba a la izquierda). Los otros dos muestran $y \to -\infty$ cuando $x \to a^+$ y $y \to -\infty$ cuando $x \to a^-$.

> [!tip] Asíntota horizontal
> La recta $y = b$ es una **asíntota horizontal** si $y \to b$ cuando $x \to \infty$ o cuando $x \to -\infty$.

![Asíntotas horizontales de una función racional](adjuntos/Asíntotas%20horizontales%20de%20una%20función%20racional.png)

> [!example]- Transcripción de la figura (clase 12)
> Dos gráficos con una recta horizontal punteada $y = b$. A la izquierda, una curva que se acerca a $y = b$ por debajo cuando $x \to \infty$. A la derecha, una curva que se acerca a $y = b$ cuando $x \to -\infty$ (con una joroba en el medio).

Los símbolos $x \to a^+$ y $x \to a^-$ indican que $x$ se acerca a $a$ desde valores mayores y menores, respectivamente.

## Cómo hallar las asíntotas

> [!tip] Teorema de las asíntotas
> Sea $r(x) = \dfrac{a_n x^n + \dots + a_0}{b_m x^m + \dots + b_0}$ con $P$ y $Q$ sin factores comunes.
> 1. **Verticales:** las rectas $x = a$ con $a$ un cero del denominador.
> 2. **Horizontal:** si $n < m$, $y = 0$; si $n = m$, $y = \dfrac{a_n}{b_m}$; si $n > m$, no hay asíntota horizontal.

La parte horizontal sale de dividir numerador y denominador por $x^m$: cuando $|x|$ es grande, $r(x) \approx \dfrac{a_n x^n}{b_m x^m}$. Si $n < m$ eso tiende a $0$; si $n = m$ queda el cociente de coeficientes principales.

> [!warning] Primero simplificar
> Si un factor $(x - a)$ aparece arriba y abajo, **no** hay asíntota vertical en $x = a$: hay un "hueco" (la función no está definida allí, pero se acerca a un valor finito). Hay que simplificar antes de aplicar el teorema.

**Ejemplo 2 (clase 12).** $r(x) = \dfrac{3x^2 - 2x - 1}{2x^2 + 3x - 2} = \dfrac{(3x + 1)(x - 1)}{(2x - 1)(x + 2)}$. El denominador se anula en $x = \tfrac{1}{2}$ y $x = -2$ (no hay factores comunes con el numerador): asíntotas verticales $x = \tfrac{1}{2}$ y $x = -2$. Los grados coinciden ($2$ y $2$), luego la asíntota horizontal es $y = \tfrac{3}{2}$.

## Funciones racionales $\dfrac{ax + b}{cx + d}$

Estas funciones se grafican a partir de $y = \tfrac{1}{x}$ con las transformaciones de las notas anteriores. Dividiendo, $\dfrac{ax + b}{cx + d} = \dfrac{a}{c} + \dfrac{k}{cx + d}$ con $k = b - \tfrac{ad}{c}$: una traslación vertical de $\tfrac{a}{c}$, una escala $k$ y una traslación horizontal por $-\tfrac{d}{c}$.

> [!example]- Ejemplo 1 (clase 12): dominio y recorrido de $r(x) = \frac{2}{x - 3}$ y $s(x) = \frac{3x + 5}{x + 2}$
> - $r(x) = 2 \cdot \tfrac{1}{x - 3}$: es $\tfrac{1}{x}$ trasladada $3$ a la derecha y alargada verticalmente por $2$. Asíntotas $x = 3$ e $y = 0$. $\operatorname{Dom}(r) = \mathbb{R} \setminus \{3\}$ y $\operatorname{Rec}(r) = \mathbb{R} \setminus \{0\}$.
> - $s(x) = \tfrac{3(x + 2) - 1}{x + 2} = 3 - \tfrac{1}{x + 2}$: $\tfrac{1}{x}$ reflejada en el eje $x$, trasladada $2$ a la izquierda y $3$ hacia arriba. Asíntotas $x = -2$ e $y = 3$. $\operatorname{Dom}(s) = \mathbb{R} \setminus \{-2\}$ y $\operatorname{Rec}(s) = \mathbb{R} \setminus \{3\}$. Corta el eje $x$ en $-\tfrac{5}{3}$ y el eje $y$ en $\tfrac{5}{2}$.

El recorrido de estas funciones omite exactamente la altura de la asíntota horizontal, $\tfrac{a}{c}$ (siempre que $ad \neq bc$): ese valor nunca se alcanza.

## Preguntas de repaso

> [!question]- ¿Qué asíntota horizontal tiene $\dfrac{3x^2 - 2x - 1}{2x^2 + 3x - 2}$ y por qué?
> $y = \tfrac{3}{2}$: numerador y denominador tienen el mismo grado y el cociente de coeficientes principales es $\tfrac{3}{2}$.

> [!question]- ¿Por qué $\dfrac{(x - 1)(x + 2)}{(x - 1)(x - 3)}$ no tiene asíntota vertical en $x = 1$?
> Porque el factor $(x - 1)$ se cancela: queda $\frac{x + 2}{x - 3}$ para $x \neq 1$. En $x = 1$ hay un hueco (no está definida), no una asíntota.

> [!question]- ¿Hay asíntota horizontal en $\dfrac{x^3}{x^2 + 1}$?
> No: el grado del numerador ($3$) supera al del denominador ($2$); la función crece sin acercarse a un valor fijo.

> [!question]- ¿Qué valor falta en el recorrido de $\frac{3x + 5}{x + 2}$?
> El $3$, que es la altura de la asíntota horizontal: $\frac{3x + 5}{x + 2} = 3 - \frac{1}{x + 2}$ nunca vale $3$.
