---
ramo: "Introducción al Álgebra"
tema: "Polinomios: raíces y gráfica"
tags:
  - intro-algebra/polinomios
  - origen/complemento
prerrequisitos:
  - "[[01 - Raíces y el teorema del factor]]"
---

# Gráfica de polinomios

La gráfica de un polinomio es una curva continua y suave: no tiene huecos, esquinas ni cúspides. Su forma global, en los extremos izquierdo y derecho, queda determinada solo por el grado y el signo del coeficiente principal.

## Continuidad y suavidad

Las gráficas de polinomios de grado $0$ y $1$ son rectas, y las de grado $2$ son parábolas. A mayor grado, la gráfica puede ser más complicada, pero siempre es:

- **Continua**: sin huecos ni puntos singulares (no hay que levantar el lápiz).
- **Suave**: sin esquinas ni picos (cúspides).

> [!tip] Propiedades de la gráfica
> La gráfica de una función polinomial es continua (sin huecos) y suave (sin esquinas). Cualquier gráfica con un hueco, un salto o una cúspide **no** corresponde a un polinomio.

![Gráficas que son y no son de polinomios](adjuntos/Gr%C3%A1ficas%20que%20son%20y%20no%20son%20de%20polinomios.png)

> [!example]- Transcripción de la figura
> Cuatro gráficas sobre fondo crema. La primera tiene un salto: un tramo termina en un punto abierto ("punto singular") y la curva sigue más arriba, con otro punto abierto ("hueco"); rótulo: "No es gráfica de una función polinomial". La segunda es continua pero tiene una "esquina" (cambio brusco de dirección) y una "cúspide" (pico agudo); mismo rótulo. La tercera y la cuarta son curvas onduladas sin cortes ni puntas, marcadas "sin irregularidades y continua", con el rótulo "Gráfica de una función polinomial".

## Comportamiento final

Para $x \to \pm\infty$, el término $a_n x^n$ domina, así que el comportamiento final depende solo del grado $n$ y del signo de $a_n$:

| Grado $n$ | Coeficiente principal $a_n$ | $x \to -\infty$ | $x \to +\infty$ |
|---|---|---|---|
| par | $a_n > 0$ | $P(x) \to +\infty$ | $P(x) \to +\infty$ |
| par | $a_n < 0$ | $P(x) \to -\infty$ | $P(x) \to -\infty$ |
| impar | $a_n > 0$ | $P(x) \to -\infty$ | $P(x) \to +\infty$ |
| impar | $a_n < 0$ | $P(x) \to +\infty$ | $P(x) \to -\infty$ |

**Ejemplo.** Para $P(x) = -2x^4 + 5x^3 + 4x - 7$, el grado es $4$ (par) y el coeficiente principal es $-2 < 0$. Por lo tanto, $P(x) \to -\infty$ tanto cuando $x \to -\infty$ como cuando $x \to +\infty$: ambos extremos caen.

> [!warning] El comportamiento final no da la forma interior
> Saber que ambos extremos caen no dice cuántas vueltas da la gráfica en el medio. El comportamiento final solo fija los extremos; las raíces y los cambios de signo determinan el interior.

![Comportamiento final según grado y coeficiente principal](adjuntos/Comportamiento%20final%20seg%C3%BAn%20grado%20y%20coeficiente%20principal.png)

> [!example]- Transcripción de la figura
> Cuatro esquemas en dos grupos. "P tiene grado impar": con coeficiente principal positivo, la curva sube a la derecha ($y \to \infty$ cuando $x \to \infty$) y baja a la izquierda ($y \to -\infty$ cuando $x \to -\infty$); con coeficiente negativo, al revés. "P tiene grado par": con coeficiente positivo, ambos extremos suben; con coeficiente negativo, ambos bajan. Los extremos se dibujan con trazo continuo y la parte central punteada, para indicar que su forma no queda determinada.

## Multiplicidad y forma en cada raíz

Si $(x - c)^m$ es la mayor potencia de $x - c$ que divide a $P$, se dice que $c$ es raíz de **multiplicidad** $m$. La multiplicidad se ve en la gráfica:

| Multiplicidad de $c$ | Qué hace la gráfica en $x = c$ |
|---|---|
| impar ($1, 3, \dots$) | **cruza** el eje $x$ (el signo de $P$ cambia) |
| par ($2, 4, \dots$) | **toca** el eje y rebota (el signo no cambia) |

Con multiplicidad $3$ o más la curva se aplana al cruzar. Entre dos raíces consecutivas el signo de $P$ es constante, así que basta evaluar un punto de cada intervalo para saber si la curva está arriba o abajo.

## Armar un polinomio desde su gráfica

1. Leer las raíces y, para cada una, si cruza (multiplicidad impar, normalmente $1$) o rebota (par, normalmente $2$).
2. Ajustar las multiplicidades para que sumen el grado dado.
3. Escribir $P(x) = a\,(x - c_1)^{m_1} \cdots (x - c_k)^{m_k}$ y despejar $a$ con un punto conocido, típicamente $P(0)$.
4. Revisar el signo de $a$ contra el comportamiento final.

**Ejemplo.** Un polinomio de grado $3$ cruza el eje en $-2$, rebota en $3$ y pasa por $(0, 18)$. Entonces $P(x) = a(x + 2)(x - 3)^2$ y $P(0) = 18a = 18$, así que $a = 1$.

## Preguntas de repaso

> [!question]- ¿Por qué una gráfica con una cúspide no es un polinomio?
> Porque la gráfica de un polinomio es suave: no tiene esquinas ni picos. Una cúspide rompe esa suavidad.

> [!question]- ¿Qué determina el comportamiento final de un polinomio?
> El grado $n$ y el signo del coeficiente principal $a_n$. Para $x \to \pm\infty$, el término $a_n x^n$ domina a los demás.

> [!question]- Describa el comportamiento final de $P(x) = 3x^5 - 2x + 1$.
> Grado $5$ (impar) y coeficiente principal $3 > 0$: cuando $x \to -\infty$, $P(x) \to -\infty$, y cuando $x \to +\infty$, $P(x) \to +\infty$.

> [!question]- ¿Qué tienen en común todos los polinomios de grado par con coeficiente principal negativo?
> Sus dos extremos caen: $P(x) \to -\infty$ tanto para $x \to -\infty$ como para $x \to +\infty$.

> [!question]- ¿Qué hace la gráfica de $(x - 1)^2(x + 4)$ en $x = 1$ y en $x = -4$?
> En $x = 1$ (multiplicidad $2$) toca el eje y rebota; en $x = -4$ (multiplicidad $1$) lo cruza.
