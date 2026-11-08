---
ramo: "Introducción al Álgebra"
tema: "Polinomios: división y algoritmo de Euclides"
tags:
  - intro-algebra/polinomios
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[03 - Teorema del resto]]"
---

# Ejercicios de la guía de división de polinomios

Preguntas de la guía del curso y de tareas anteriores sobre división de polinomios y el teorema del resto. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Dividir entre un lineal
Divida $6x^2 - 26x + 12$ entre $x - 4$ e indique cociente y resto.

> [!example]- Solución
> $6x^2 / x = 6x$; se resta $6x(x-4) = 6x^2 - 24x$ y queda $-2x + 12$. Luego $-2x / x = -2$; se resta $-2(x-4) = -2x + 8$ y queda $4$. Por lo tanto $6x^2 - 26x + 12 = (x-4)(6x-2) + 4$: cociente $6x - 2$, resto $4$.

### 2. División larga completa
Divida $8x^4 + 6x^2 - 3x + 1$ entre $2x^2 - x + 2$.

> [!example]- Solución
> $8x^4/2x^2 = 4x^2$; al restar queda $4x^3 - 2x^2 - 3x + 1$. $4x^3/2x^2 = 2x$; al restar queda $-7x + 1$. Como su grado $1 < 2$, el proceso termina: $Q(x) = 4x^2 + 2x$, $R(x) = -7x + 1$.

### 3. Dividir con resto no nulo
Divida $3x^4 - 6x^3 + 3x^2 - x + 2$ entre $x^2 - 2x + 3$.

> [!example]- Solución
> $3x^4/x^2 = 3x^2$; al restar queda $-6x^2 - x + 2$. $-6x^2/x^2 = -6$; al restar queda $-13x + 20$. Como su grado $1 < 2$, $Q(x) = 3x^2 - 6$ y $R(x) = -13x + 20$. El grado del cociente es $4 - 2 = 2$ y el resto tiene grado $1$.

### 4. Resto por dos métodos
Para $P(x) = 5x^3 - 8x^2 - x + 7$, determine el resto de dividir entre $x - 2$ por división larga y por el teorema del resto.

> [!example]- Solución
> Por el teorema del resto, $P(2) = 5 \cdot 8 - 8 \cdot 4 - 2 + 7 = 13$. La división larga da el mismo resto constante $13$.

### 5. Parámetro para que divida
Determine $c$ para que $q(x) = x^2 + c$ divida a $p(x) = 2x^3 - x^2 + 6x - 3$.

> [!example]- Solución
> Dividiendo $2x^3 - x^2 + 6x - 3$ entre $x^2 + c$:
> $2x^3/x^2 = 2x$; se resta $2x(x^2 + c) = 2x^3 + 2cx$ y queda $-x^2 + (6 - 2c)x - 3$. Luego $-x^2/x^2 = -1$; se resta $-1(x^2 + c) = -x^2 - c$ y queda $(6 - 2c)x + (c - 3)$.
> Para que $q$ divida a $p$ el resto debe ser $0$, o sea $(6 - 2c)x + (c - 3) = 0$ para todo $x$, lo que exige $6 - 2c = 0$ y $c - 3 = 0$. Ambos dan $c = 3$.

## Preguntas de repaso

> [!question]- ¿Cuándo un divisor divide exactamente a un polinomio?
> Cuando el resto de la división es el polinomio nulo. Si el divisor es $x - c$, equivale a $P(c) = 0$.

> [!question]- En el ejercicio 5, ¿por qué el resto $(6-2c)x + (c-3)$ debe ser el polinomio nulo?
> Porque "dividir" significa resto cero. Un polinomio es nulo solo si todos sus coeficientes son cero, lo que da dos ecuaciones: $6 - 2c = 0$ y $c - 3 = 0$, ambas con $c = 3$.

> [!question]- ¿Qué relación hay entre el teorema del resto y encontrar raíces?
> El teorema dice que el resto de dividir entre $x - c$ es $P(c)$. Si ese resto es $0$, entonces $P(c) = 0$, es decir, $c$ es raíz de $P$.
