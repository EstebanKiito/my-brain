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

## Preguntas de repaso

> [!question]- ¿Por qué una gráfica con una cúspide no es un polinomio?
> Porque la gráfica de un polinomio es suave: no tiene esquinas ni picos. Una cúspide rompe esa suavidad.

> [!question]- ¿Qué determina el comportamiento final de un polinomio?
> El grado $n$ y el signo del coeficiente principal $a_n$. Para $x \to \pm\infty$, el término $a_n x^n$ domina a los demás.

> [!question]- Describa el comportamiento final de $P(x) = 3x^5 - 2x + 1$.
> Grado $5$ (impar) y coeficiente principal $3 > 0$: cuando $x \to -\infty$, $P(x) \to -\infty$, y cuando $x \to +\infty$, $P(x) \to +\infty$.

> [!question]- ¿Qué tienen en común todos los polinomios de grado par con coeficiente principal negativo?
> Sus dos extremos caen: $P(x) \to -\infty$ tanto para $x \to -\infty$ como para $x \to +\infty$.
