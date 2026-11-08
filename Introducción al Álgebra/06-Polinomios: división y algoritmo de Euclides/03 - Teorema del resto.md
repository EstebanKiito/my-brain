---
ramo: "Introducción al Álgebra"
tema: "Polinomios: división y algoritmo de Euclides"
tags:
  - intro-algebra/polinomios
  - origen/complemento
prerrequisitos:
  - "[[02 - División de polinomios]]"
---

# Teorema del resto

Dividir entre un polinomio lineal $x - c$ es tan frecuente que conviene un atajo: el resto de esa división no requiere hacer la división, porque es simplemente $P(c)$. Este hecho es el **teorema del resto**, y además conecta con el estudio de las raíces.

## El teorema del resto

> [!tip] Teorema del resto
> El resto de dividir $P(x)$ entre $x - c$ es la constante $P(c)$.

**Por qué funciona.** Por el algoritmo de la división, $P(x) = (x - c)\,Q(x) + R$, donde $R$ es constante (grado menor que $1$). Evaluando en $x = c$: $P(c) = (c - c)\,Q(c) + R = 0 + R = R$.

## Ejemplos

**Ejemplo.** Halle el resto de dividir $P(x) = 5x^3 - 8x^2 - x + 7$ entre $x - 2$.

Por el teorema del resto, el resto es $P(2) = 5 \cdot 8 - 8 \cdot 4 - 2 + 7 = 40 - 32 - 2 + 7 = 13$. Haciendo la división larga se obtiene el mismo resto.

**Ejemplo.** Halle el resto de dividir $P(x) = 2x^{2021} - 5x^{2020} + 3x + 2$ entre $x + 1$.

Como $x + 1 = x - (-1)$, se evalúa en $c = -1$:

$$
P(-1) = 2(-1)^{2021} - 5(-1)^{2020} + 3(-1) + 2 = -2 - 5 - 3 + 2 = -8.
$$

> [!warning] Cuidado con el signo de $c$
> Para dividir entre $x + 1$ se evalúa en $c = -1$, no en $+1$: el teorema usa $x - c$, así que $x + 1 = x - (-1)$.

## División sintética (esquema de Horner)

Para dividir entre $x - c$ y obtener también el **cociente**, hay un atajo que trabaja solo con los coeficientes. Se escriben los coeficientes de $P$ (con ceros para las potencias que faltan), se baja el primero y, en cada paso, se multiplica por $c$ el último número obtenido y se suma al coeficiente siguiente. El último número es el resto; los anteriores, los coeficientes del cociente.

**Ejemplo.** $P(x) = x^4 - 2x^3 - 3x^2 + 8x - 4$ entre $x - 3$:

| | $1$ | $-2$ | $-3$ | $8$ | $-4$ |
|---|---|---|---|---|---|
| $\times 3$ | | $3$ | $3$ | $0$ | $24$ |
| | $1$ | $1$ | $0$ | $8$ | $\mathbf{20}$ |

Cociente $x^3 + x^2 + 8$ y resto $20$, que coincide con $P(3) = 20$.

## Resto de dividir por un polinomio de grado mayor

El teorema del resto solo sirve para divisores lineales. Si el divisor $D$ tiene grado $2$, el resto tiene grado a lo más $1$ y se escribe con incógnitas: $P(x) = D(x)\,Q(x) + Ax + B$. Evaluando en las raíces de $D$ el término $D(x)Q(x)$ se anula, y quedan ecuaciones para $A$ y $B$.

**Ejemplo.** Resto de dividir $x^{100}$ entre $x^2 - 1$. Se escribe $x^{100} = (x^2 - 1)Q(x) + Ax + B$. En $x = 1$: $1 = A + B$; en $x = -1$: $1 = -A + B$. Entonces $A = 0$, $B = 1$ y el resto es $1$, sin hacer ninguna división.

> [!tip] La idea en una línea
> Escribir $P = D \cdot Q + R$ con $R$ de coeficientes desconocidos y evaluar donde algún factor se anula. Sirve también cuando el dato es el cociente y lo que se conoce son valores de $P$.

## Preguntas de repaso

> [!question]- ¿Por qué el resto de dividir entre $x - c$ es constante?
> Porque el divisor tiene grado $1$, y el resto debe tener grado menor que $1$, es decir, grado $0$ (constante) o ser nulo.

> [!question]- Demuestre el teorema del resto.
> De $P(x) = (x - c)Q(x) + R$ con $R$ constante, se evalúa en $x = c$: $P(c) = (c - c)Q(c) + R = R$.

> [!question]- Halle el resto de dividir $x^3 - 4x + 1$ entre $x - 1$.
> $P(1) = 1 - 4 + 1 = -2$. El resto es $-2$.

> [!question]- ¿Cuándo es $x - c$ un factor de $P(x)$, es decir, $P(x) = (x - c)Q(x)$?
> Cuando el resto es cero, o sea, cuando $P(c) = 0$. Es el puente con el concepto de raíz, que se estudia en el tema siguiente.

> [!question]- ¿Qué grado puede tener el resto de dividir por $x^2 + 1$?
> A lo más $1$: el resto se escribe $Ax + B$ (con $A = 0$ si resulta constante).
