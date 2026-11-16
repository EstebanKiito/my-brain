---
ramo: "Introducción al Cálculo"
tema: "Polinomios y funciones racionales"
tags:
  - intro-calculo/polinomios
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Factorizar un polinomio con división y teorema del factor]]"
  - "[[02 - Problemas de máximos y mínimos con cuadráticas]]"
---

# Ejercicios de prueba de polinomios y cuadráticas

Preguntas de interrogaciones de 2020 a 2026. La Interrogación 1 de 2025 y la de 2026 piden dividir, verificar con el teorema del resto y concluir con el teorema del factor; la de 2023 y la de 2020 piden optimización con cuadráticas y un bosquejo de un polinomio. Cada paso tiene puntaje propio, de modo que conviene mostrar la tabla de Ruffini o la división completa.

## Ejercicios

### 1. Dividir, verificar y factorizar (I1, 2025-1)
Sea $P(x) = x^5 - x^4 - 2x^3 - x^2 + x + 2$. (a) Divida por $x - 2$. (b) Verifique el resto con el teorema del resto. (c) Determine, con el teorema del factor, si $x + 1$ es factor. (d) Factorice completamente.

> [!example]- Solución
> (a) Con Ruffini ($c = 2$): coeficientes $1, 1, 0, -1, -1$ y resto $0$. Cociente $x^4 + x^3 - x - 1$, resto $0$. (b) $P(2) = 32 - 16 - 16 - 4 + 2 + 2 = 0$. (c) $P(-1) = -1 - 1 + 2 - 1 - 1 + 2 = 0$: $x + 1$ es factor. (d) $(x - 2)(x + 1) = x^2 - x - 2$ divide a $P$ con cociente $x^3 - 1 = (x - 1)(x^2 + x + 1)$. $P(x) = (x - 2)(x + 1)(x - 1)(x^2 + x + 1)$, con $x^2 + x + 1$ irreducible ($\Delta = -3 < 0$).

### 2. Dividir por un factor no mónico (I1, 2026-1)
Sea $P(x) = 4x^6 + 2x^5 - 2x^4 - 4x^3 + 3x - 1$. (a) Divida por $2x - 1$. (b) Verifique el resto con el teorema del resto. (c) Decida con el teorema del factor si $x + 1$ es factor. (d) Demuestre que $2x^4 - 2x + 1$ también es factor y dé una factorización con tres factores.

> [!example]- Solución
> (a) Cociente $Q(x) = 2x^5 + 2x^4 - 2x^2 - x + 1$ y resto $0$ (la división larga: $4x^6 \div 2x = 2x^5$, etc.). (b) $P\!\left(\tfrac{1}{2}\right) = \tfrac{1}{16} + \tfrac{1}{16} - \tfrac{1}{8} - \tfrac{1}{2} + \tfrac{3}{2} - 1 = 0$. (c) $P(-1) = 4 - 2 - 2 + 4 - 3 - 1 = 0$: sí es factor. (d) Como $2x - 1$ y $x + 1$ son factores, también lo es $(2x - 1)(x + 1) = 2x^2 + x - 1$. Dividiendo $P$ por él se obtiene $2x^4 - 2x + 1$ con resto $0$, así que $P(x) = (2x - 1)(x + 1)(2x^4 - 2x + 1)$.

### 3. Raíz y factorización completa (I1, 2026-1)
Sea $P(a) = 4a^3 + 4a^2 - 19a + 6$. (a) Verifique que $a = \tfrac{3}{2}$ es raíz. (b) Divida por $2a - 3$. (c) Factorice completamente.

> [!example]- Solución
> (a) $P\!\left(\tfrac{3}{2}\right) = \tfrac{27}{2} + 9 - \tfrac{57}{2} + 6 = 0$. (b) $4a^3 + 4a^2 - 19a + 6 = (2a - 3)(2a^2 + 5a - 2)$, resto $0$. (c) $2a^2 + 5a - 2$ tiene $\Delta = 41$ y raíces $\tfrac{-5 \pm \sqrt{41}}{4}$: $P(a) = (2a - 3)\cdot 2\left(a - \tfrac{-5 + \sqrt{41}}{4}\right)\left(a - \tfrac{-5 - \sqrt{41}}{4}\right)$.

### 4. Optimización y forma normal (I4, 2023-1)
(a) Se tienen $80$ m de cerca para un huerto rectangular con un lado en el deslinde del vecino y una división interior (en total $3$ segmentos de largo $y$ y uno de largo $x$). Plantee un problema de una incógnita para maximizar el área. (b) Escriba $f(x) = 3x^2 + \lambda x + 10$ en forma normal y halle los $\lambda$ para que su mínimo sea $-2$.

> [!example]- Solución
> (a) $3y + x = 80$ y área $A = xy$. Con $x = 80 - 3y$: maximizar $A(y) = (80 - 3y)y$ (o, con $y = \tfrac{80 - x}{3}$, $A(x) = \tfrac{x(80 - x)}{3}$). No se pide resolver.
> (b) $f(x) = 3\left(x + \tfrac{\lambda}{6}\right)^2 + 10 - \tfrac{\lambda^2}{12}$. Su mínimo es $10 - \tfrac{\lambda^2}{12}$ (en $x = -\tfrac{\lambda}{6}$). $10 - \tfrac{\lambda^2}{12} = -2 \iff \lambda^2 = 144 \iff \lambda = \pm 12$.

### 5. Bosquejo de un polinomio (I4, 2020-1)
Esboce la gráfica de $p(x) = 2x(x - 1)^3(x - 2)^2(x - 3)$.

> [!example]- Solución
> Grado $1 + 3 + 2 + 1 = 7$ (impar) y coeficiente principal $2 > 0$: $p \to -\infty$ cuando $x \to -\infty$ y $p \to +\infty$ cuando $x \to +\infty$. Ceros: $0$ (simple, cruza), $1$ (mult. $3$: cruza aplanándose), $2$ (mult. $2$: toca y rebota sin cambiar de signo) y $3$ (simple, cruza). Signos: negativo en $(-\infty, 0)$, positivo en $(0, 1)$, negativo en $(1, 3)$ (el $2$ no cambia el signo) y positivo en $(3, \infty)$. Corta el eje $y$ en $p(0) = 0$. Entonces: viene desde abajo, cruza en $0$ hacia arriba, vuelve a cruzar en $1$ hacia abajo (aplanado), toca el eje en $2$ sin cruzar y cruza en $3$ hacia arriba.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 2(d) se puede dividir por $(2x - 1)(x + 1)$?
> Porque $2x - 1$ y $x + 1$ son factores (el primero por (a) y el segundo por (c)) y tienen raíces distintas ($\tfrac{1}{2}$ y $-1$), de modo que su producto también divide a $P$.

> [!question]- ¿Qué indica que el cero $x = 2$ de $p(x)$ sea de multiplicidad $2$?
> Que el gráfico toca el eje $x$ en $2$ y rebota sin cruzarlo: el polinomio no cambia de signo allí.

> [!question]- ¿Por qué el mínimo de $3x^2 + \lambda x + 10$ no depende de signo alguno de $\lambda$?
> Porque vale $10 - \frac{\lambda^2}{12}$, que solo depende de $\lambda^2$: $\lambda = 12$ y $\lambda = -12$ dan el mismo valor mínimo.
