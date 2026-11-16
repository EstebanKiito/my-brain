---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - origen/complemento
prerrequisitos:
  - "[[06 - Reflexiones y transformaciones sucesivas]]"
---

# Funciones cuadráticas, forma normal y vértice

Las funciones polinómicas más simples después de la recta son las cuadráticas, cuya gráfica es una parábola. Su forma normal revela de un vistazo el vértice, el eje de simetría y el valor máximo o mínimo, y se obtiene con una técnica que se usa en todo el curso: completar el cuadrado.

## Funciones polinómicas

Una **función polinómica** tiene la forma $f(x) = a_n x^n + a_{n-1}x^{n-1} + \dots + a_1 x + a_0$, con coeficientes reales; su dominio es $\mathbb{R}$ y $n$ es el **grado**. Si $n = 0$ el gráfico es una recta horizontal, si $n = 1$ una recta, si $n = 2$ una parábola; para $n > 2$ no hay una forma única. (La teoría de polinomios, con división y raíces, está en [[01 - Polinomios, grado y coeficientes|Polinomios, grado y coeficientes]].)

> [!tip] Función cuadrática
> Es $f : \mathbb{R} \to \mathbb{R}$ con $f(x) = ax^2 + bx + c$ y $a \neq 0$.

## Forma normal

> [!tip] Forma normal (o canónica)
> Completando el cuadrado, $f(x) = ax^2 + bx + c$ se escribe $f(x) = a(x - h)^2 + k$, con
> $$h = -\frac{b}{2a}, \qquad k = f(h) = c - \frac{b^2}{4a}.$$
> La gráfica es una parábola con **vértice** $(h, k)$ y eje de simetría $x = h$. Abre hacia arriba (es **convexa**) si $a > 0$ y hacia abajo (es **cóncava**) si $a < 0$.

![Parábolas con vértice en la forma normal](adjuntos/Parábolas%20con%20vértice%20en%20la%20forma%20normal.png)

> [!example]- Transcripción de la figura (clase 11)
> Dos parábolas rojas. La de la izquierda, $f(x) = ax^2 + bx + c$ con $a > 0$, abre hacia arriba y su punto más bajo, el vértice $(h, k)$, está sobre la marca $h$ del eje $x$ y a la altura $k$ del eje $y$. La de la derecha, con $a < 0$, abre hacia abajo y su vértice $(h, k)$ es el punto más alto.

Es la transformación de gráficos aplicada a $y = x^2$: $a(x - h)^2 + k$ es $x^2$ trasladada $h$ a la derecha y $k$ hacia arriba, con alargamiento vertical $|a|$ y reflexión en el eje $x$ si $a < 0$.

## Cómo completar el cuadrado

Se saca factor común $a$ de los términos con $x$, se suma y se resta el cuadrado de la mitad del coeficiente:
$$ax^2 + bx + c = a\left(x^2 + \tfrac{b}{a}x\right) + c = a\left(x + \tfrac{b}{2a}\right)^2 + c - \tfrac{b^2}{4a}.$$

> [!example]- Ejemplo 1 (clase 11): $f(x) = 2x^2 - 12x + 23$
> $2x^2 - 12x + 23 = 2(x^2 - 6x) + 23 = 2\big[(x - 3)^2 - 9\big] + 23 = 2(x - 3)^2 + 5$. Vértice $(3, 5)$; como $a = 2 > 0$, abre hacia arriba y no corta el eje $x$ (el mínimo es $5 > 0$). Corta el eje $y$ en $(0, f(0)) = (0, 23)$.

> [!example]- Ejemplo 2 (clase 11): $f(x) = 5x^2 - 30x + 49$
> $5(x^2 - 6x) + 49 = 5\big[(x - 3)^2 - 9\big] + 49 = 5(x - 3)^2 + 4$. Vértice $(3, 4)$, abre hacia arriba y el **valor mínimo** es $4$. Corta el eje $y$ en $(0, 49)$ y no corta el eje $x$ ($\Delta = 900 - 980 < 0$).

## Valor máximo o mínimo

> [!tip] Extremo de una cuadrática
> $f(x) = ax^2 + bx + c$ alcanza su extremo en $x = -\dfrac{b}{2a}$: es un **mínimo**, $f\!\left(-\tfrac{b}{2a}\right)$, si $a > 0$, y un **máximo** si $a < 0$. Por tanto el recorrido es $\left[f(-\tfrac{b}{2a}), \infty\right)$ si $a > 0$ y $\left(-\infty, f(-\tfrac{b}{2a})\right]$ si $a < 0$.

Ejemplo: el vértice de $f(x) = -6x^2 + 2x - 4$ está en $x = -\tfrac{2}{-12} = \tfrac{1}{6}$, con $f\!\left(\tfrac{1}{6}\right) = -\tfrac{6}{36} + \tfrac{2}{6} - 4 = -\tfrac{23}{6}$. Como $a < 0$, ese vértice es un máximo y el recorrido es $\left(-\infty, -\tfrac{23}{6}\right]$.

> [!warning] Dos errores frecuentes
> - Olvidar el signo: la abscisa del vértice es $-\tfrac{b}{2a}$, no $\tfrac{b}{2a}$.
> - Completar el cuadrado sin sacar antes el factor $a$ cuando $a \neq 1$: el término que se suma y resta queda multiplicado por $a$.

## Preguntas de repaso

> [!question]- ¿Por qué la abscisa del vértice de $ax^2 + bx + c$ es $-\frac{b}{2a}$?
> Al completar el cuadrado queda $a\left(x + \frac{b}{2a}\right)^2 + \text{constante}$. El cuadrado es mínimo (cero) cuando $x = -\frac{b}{2a}$, y a partir de ahí crece simétricamente a ambos lados.

> [!question]- ¿Cómo se sabe sin graficar que $2x^2 - 12x + 23$ no tiene raíces reales?
> Su forma normal es $2(x - 3)^2 + 5 \ge 5 > 0$: nunca vale cero.

> [!question]- Si $a < 0$, ¿cuál es el recorrido de la cuadrática?
> $(-\infty, k]$, donde $k = f(h)$ es el valor máximo en el vértice.

> [!question]- ¿Qué transformaciones convierten $y = x^2$ en $y = -3(x - 1)^2 + 2$?
> Traslación $1$ a la derecha, alargamiento vertical en factor $3$, reflexión en el eje $x$ y traslación $2$ hacia arriba.
