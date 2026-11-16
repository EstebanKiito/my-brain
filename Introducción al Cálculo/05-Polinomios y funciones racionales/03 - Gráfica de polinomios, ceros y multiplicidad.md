---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones cuadráticas, forma normal y vértice]]"
---

# Gráfica de polinomios, ceros y multiplicidad

Para graficar un polinomio de grado mayor que $2$ no hay una forma tabulada, pero tres datos bastan para un bosquejo fiel: cómo se comporta en los extremos ($x \to \pm\infty$), dónde corta el eje $x$ (los ceros) y cómo se comporta el gráfico en cada cero (según su multiplicidad). El método es el mismo que usa [[05 - Gráfica de polinomios|Introducción al Álgebra]], aplicado aquí a la lectura de gráficos.

## Comportamiento final

> [!tip] Comportamiento final
> El comportamiento de $P(x) = a_n x^n + \dots + a_0$ cuando $x \to \pm\infty$ lo determinan el grado $n$ y el signo del coeficiente principal $a_n$: el término $a_n x^n$ domina a los demás.
> - $n$ **impar**, $a_n > 0$: $P \to -\infty$ cuando $x \to -\infty$ y $P \to +\infty$ cuando $x \to +\infty$ (crece de izquierda a derecha).
> - $n$ **impar**, $a_n < 0$: lo contrario (decrece de izquierda a derecha).
> - $n$ **par**, $a_n > 0$: $P \to +\infty$ en ambos extremos (forma de U).
> - $n$ **par**, $a_n < 0$: $P \to -\infty$ en ambos extremos (forma de $\cap$).

![Comportamiento final de un polinomio según grado y coeficiente principal](adjuntos/Comportamiento%20final%20de%20un%20polinomio%20según%20grado%20y%20coeficiente%20principal.png)

> [!example]- Transcripción de la figura (clase 11)
> Cuatro curvas con la parte central punteada (porque puede tener oscilaciones) y los extremos en trazo rojo. Bajo el título "P tiene grado impar": con coeficiente principal positivo, la curva sube desde abajo a la izquierda hacia arriba a la derecha ($y \to -\infty$ cuando $x \to -\infty$ y $y \to \infty$ cuando $x \to \infty$); con coeficiente negativo, baja de arriba a la izquierda hacia abajo a la derecha. Bajo "P tiene grado par": con coeficiente positivo ambos extremos suben ($y \to \infty$ en los dos lados); con coeficiente negativo ambos bajan ($y \to -\infty$).

## Ceros y multiplicidad

Un **cero** de $f$ es un $c$ con $f(c) = 0$; si $f$ es polinómica, los ceros son las soluciones de $P(x) = 0$ y el gráfico corta (o toca) el eje $x$ en $x = c$. Si el factor $(x - c)$ aparece exactamente $m$ veces en la factorización de $P$, el cero $c$ tiene **multiplicidad** $m$.

> [!tip] Forma del gráfico cerca de un cero de multiplicidad $m$
> - $m$ **impar**: el gráfico **cruza** el eje $x$ (cambia de signo). Si $m = 1$ lo cruza como una recta; si $m > 1$ (por ejemplo $3$) se aplana antes de cruzar, como $x^3$.
> - $m$ **par**: el gráfico **toca** el eje $x$ y rebota sin cruzar (no cambia de signo), como $x^2$ o $x^4$.

![Forma de la gráfica cerca de un cero según su multiplicidad](adjuntos/Forma%20de%20la%20gráfica%20cerca%20de%20un%20cero%20según%20su%20multiplicidad.png)

> [!example]- Transcripción de la figura (clase 11)
> Una tabla con dos filas. Para $m$ impar, $m > 1$: la curva cruza el eje $x$ en $c$ aplanándose, ya sea creciente (sube de izquierda a derecha) o decreciente, como $x^3$ o $-x^3$. Para $m$ par, $m > 1$: la curva toca el eje $x$ en $c$ sin cruzarlo, por arriba (forma de U, como $x^4$) o por abajo (forma de $\cap$).

## Receta de bosquejo

1. **Factorizar** el polinomio (ver [[04 - Factorizar un polinomio con división y teorema del factor|cómo factorizar]]).
2. **Ceros y multiplicidades**, y el corte con el eje $y$ en $P(0)$.
3. **Comportamiento final** por grado y signo de $a_n$.
4. **Signos** entre ceros: cruzan en multiplicidad impar y no cambian en multiplicidad par (se puede armar la tabla de signos con los factores).
5. Unir con una curva suave que respete todo lo anterior.

## Ejemplos

**$f(x) = x(x - 1)(x - 2)$** (clase 11): ceros $0$, $1$ y $2$, todos simples; grado $3$ y $a_n > 0$, así que va de $-\infty$ a $+\infty$ cruzando en cada cero.

**$P(x) = x^3 - 2x^2 - 4x + 8$**: factorizando por agrupación, $x^2(x - 2) - 4(x - 2) = (x - 2)(x^2 - 4) = (x - 2)^2(x + 2)$. Ceros: $-2$ (simple, cruza) y $2$ (doble, toca el eje y rebota). Corta el eje $y$ en $8$. Grado impar, $a_n > 0$: viene de $-\infty$, cruza en $-2$, sube hasta un máximo, baja hasta tocar el eje en $x = 2$ y vuelve a subir.

**$Q(x) = -2x^4 - x^3 + 3x^2$**: $-x^2(2x^2 + x - 3) = -x^2(2x + 3)(x - 1)$. Ceros: $-\tfrac{3}{2}$ (simple), $0$ (doble) y $1$ (simple). Grado par con $a_n < 0$: ambos extremos hacia $-\infty$. Entre los ceros, el signo de $-x^2(2x + 3)(x - 1)$ es: negativo para $x < -\tfrac{3}{2}$, positivo en $\left(-\tfrac{3}{2}, 0\right)$ y en $(0, 1)$ (el $0$ doble no cambia el signo), negativo para $x > 1$.

**$f(x) = x^4(x - 2)^3(x + 1)^2$**: ceros $0$ (mult. $4$, toca), $2$ (mult. $3$, cruza aplanándose) y $-1$ (mult. $2$, toca). Grado $9$ impar y $a_n = 1 > 0$: de $-\infty$ a $+\infty$. Es negativa para $x < 2$ (salvo en los ceros) y positiva para $x > 2$; en $0$ y $-1$ rebota desde abajo.

> [!warning] Lo que el bosquejo no da
> Los ceros, los signos y el comportamiento final no fijan las alturas de los máximos y mínimos locales entre dos ceros. Para un bosquejo basta con ubicarlos de forma razonable; las alturas exactas requieren más herramientas.

## Preguntas de repaso

> [!question]- ¿Qué distingue un cero simple de uno doble en el gráfico?
> En un cero simple el gráfico cruza el eje $x$ y cambia de signo. En uno doble solo lo toca y rebota, sin cambiar de signo.

> [!question]- ¿Cómo se determina el comportamiento final de $P(x) = -3x^5 + 2x$?
> El término dominante es $-3x^5$: grado impar y coeficiente negativo, así que $P \to +\infty$ cuando $x \to -\infty$ y $P \to -\infty$ cuando $x \to +\infty$.

> [!question]- ¿Cuántos ceros (contando multiplicidad) tiene $x^4(x - 2)^3(x + 1)^2$?
> $4 + 3 + 2 = 9$, igual al grado del polinomio.

> [!question]- ¿Por qué un polinomio de grado par con $a_n > 0$ tiene un mínimo absoluto pero no un máximo?
> Porque tiende a $+\infty$ en ambos extremos, así que está acotado por abajo (alcanza un mínimo) y no por arriba.
