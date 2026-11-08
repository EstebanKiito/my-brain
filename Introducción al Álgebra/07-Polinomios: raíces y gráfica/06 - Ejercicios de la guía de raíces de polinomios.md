---
ramo: "Introducción al Álgebra"
tema: "Polinomios: raíces y gráfica"
tags:
  - intro-algebra/polinomios
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Teorema de los ceros racionales]]"
  - "[[04 - Número de raíces y raíces complejas]]"
---

# Ejercicios de la guía de raíces de polinomios

Preguntas de la guía del curso sobre raíces, teorema del factor, ceros racionales y raíces complejas. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Parámetros para que divida
Determine $A$ y $B$ para que $P(x) = x^4 + x^3 + Ax^2 + Bx + 30$ sea divisible por $x - 2$ y por $x + 3$.

> [!example]- Solución
> Por el teorema del factor, $P(2) = 0$ y $P(-3) = 0$. Entonces
> $$P(2) = 16 + 8 + 4A + 2B + 30 = 54 + 4A + 2B = 0 \implies 2A + B = -27,$$
> $$P(-3) = 81 - 27 + 9A - 3B + 30 = 84 + 9A - 3B = 0 \implies 3A - B = -28.$$
> Sumando ambas, $5A = -55$, así que $A = -11$; sustituyendo, $B = -5$.

### 2. Resolver una cuártica
Resuelva $2x^4 - x^3 - 11x^2 + 4x + 12 = 0$.

> [!example]- Solución
> Candidatos racionales: $p \mid 12$ y $q \mid 2$, o sea $\pm 1, \pm 2, \pm 3, \pm 4, \pm 6, \pm 12, \pm\tfrac12, \pm\tfrac32$. Evaluando, $-1$, $2$ y $-2$ son raíces. Dividiendo por $(x+1)(x-2)(x+2) = x^3 + x^2 - 4x - 4$ queda el factor $2x - 3$. Las raíces son $-1$, $2$, $-2$ y $\tfrac32$.

### 3. Resolver con raíces fraccionarias
Resuelva $4x^4 - 4x^3 - 5x^2 + x + 1 = 0$.

> [!example]- Solución
> Candidatos: $p \mid 1$ y $q \mid 4$, o sea $\pm 1, \pm\tfrac12, \pm\tfrac14$. Evaluando, $\tfrac12$ y $-\tfrac12$ son raíces, así que $4x^2 - 1$ divide. Dividiendo, $4x^4 - 4x^3 - 5x^2 + x + 1 = (4x^2 - 1)(x^2 - x - 1) = (2x-1)(2x+1)(x^2 - x - 1)$. El cuadrático da $\tfrac{1 \pm \sqrt{5}}{2}$. Raíces: $\tfrac12$, $-\tfrac12$, $\tfrac{1+\sqrt5}{2}$, $\tfrac{1-\sqrt5}{2}$.

### 4. Raíces conjugadas
Si $\alpha = 1 + i$ es raíz de $P(x) = x^3 - 4x^2 + 6x - 4$, determine las otras raíces.

> [!example]- Solución
> Como $P$ tiene coeficientes reales, $1 - i$ también es raíz. El producto $(x - (1+i))(x - (1-i)) = x^2 - 2x + 2$ divide a $P$, y dividiendo, $P(x) = (x^2 - 2x + 2)(x - 2)$. Raíces: $1 + i$, $1 - i$ y $2$.

### 5. Factorizar en irreducibles
Factorice $R(x) = x^3 + x + 10$ en polinomios irreducibles de $\mathbb{R}$.

> [!example]- Solución
> Notando que $1 + 2i$ es raíz (pues $(1+2i)^3 + (1+2i) + 10 = 0$), su conjugada $1 - 2i$ también lo es, así que $x^2 - 2x + 5$ divide a $R$. Dividiendo, $R(x) = (x + 2)(x^2 - 2x + 5)$. El cuadrático tiene discriminante $4 - 20 = -16 < 0$, así que es irreducible. Factorización: $(x + 2)(x^2 - 2x + 5)$.

## Preguntas de repaso

> [!question]- ¿Cómo se usa el teorema del factor en el ejercicio 1?
> "Divisible por $x - 2$" equivale a "2 es raíz", es decir, $P(2) = 0$. Lo mismo con $-3$. Cada condición da una ecuación en $A$ y $B$.

> [!question]- En los ejercicios 2 y 3, ¿por qué basta probar los candidatos racionales?
> Por el teorema de los ceros racionales: si hay una raíz racional, está en la lista finita de $p/q$. Encontrar una permite bajar el grado y repetir.

> [!question]- ¿Por qué una raíz compleja de un polinomio real obliga a su conjugada?
> Porque al sustituir y conjugar, $P(\overline{\alpha}) = \overline{P(\alpha)} = \overline{0} = 0$. Así las raíces no reales vienen en pares conjugados.
