---
ramo: "Introducción al Cálculo"
tema: "Números reales: axiomas de cuerpo y de orden"
tags:
  - intro-calculo/numeros-reales
  - intro-calculo/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Cómo demostrar desigualdades con los axiomas de orden]]"
---

# Ejercicios de la guía de orden

Los siete ejercicios de la Guía 1 (orden). Conviene intentar cada uno antes de abrir la solución; todos se resuelven con los axiomas de orden y la cerradura de $\mathbb{R}^+$.

## Ejercicios

### 1. Desigualdad cruzada
Si $a < b$ y $c < d$, demuestre que $ad + bc < ac + bd$.

> [!example]- Solución
> Como $b - a > 0$ y $d - c > 0$, su producto es positivo por cerradura: $(b - a)(d - c) = bd - bc - ad + ac > 0$. Reordenando, $ad + bc < ac + bd$.

### 2. Un natural no supera a su cuadrado
Demuestre que $n^2 \ge n$ para todo $n \in \mathbb{N}$.

> [!example]- Solución
> Si $n = 1$, $1^2 = 1 \ge 1$. Si $n \neq 1$, entonces $n > 1$ (los naturales parten en 1), así que $n - 1 > 0$ y $n > 0$. Por cerradura, $(n - 1)n = n^2 - n > 0$, luego $n^2 > n$.

### 3. Multiplicar por un positivo
Si $x < y$ y $z > 0$, demuestre que $xz < yz$.

> [!example]- Solución
> Es el axioma O4 en esta formulación. Si se parte de la cerradura de $\mathbb{R}^+$: $y - x > 0$ y $z > 0$, luego $(y - x)z = yz - xz > 0$, es decir $xz < yz$.

### 4. Multiplicar por un negativo
Si $x < y$ y $z < 0$, demuestre que $xz > yz$.

> [!example]- Solución
> Como $z < 0$, se tiene $-z > 0$. Por el ejercicio 3, $x(-z) < y(-z)$, es decir $-xz < -yz$. Sumando $xz + yz$ a ambos lados (axioma O3) queda $yz < xz$.

### 5. El producto de las sumas
Para $a, b, c$ positivos, demuestre que $(a + b + c)(bc + ca + ab) \ge 9abc$.

> [!example]- Solución
> Expandiendo, la diferencia es $(a + b + c)(bc + ca + ab) - 9abc = c(a - b)^2 + b(a - c)^2 + a(b - c)^2 \ge 0$, porque cada término es un positivo por un cuadrado. Es estrictamente positiva si $a, b, c$ no son todos iguales.
>
> La guía escribe "$>$" sin más hipótesis, pero con $a = b = c = 1$ ambos lados valen $9$: la desigualdad estricta solo vale si no son todos iguales (ver [[05 - Cómo demostrar desigualdades con los axiomas de orden|la nota del método]]).

### 6. Una ecuación sin raíces reales
Demuestre que $x^2 + 1 = 0$ no tiene soluciones reales.

> [!example]- Solución
> Para todo real, $x^2 \ge 0$, luego $x^2 + 1 \ge 1 > 0$ y nunca vale $0$.

### 7. Suma fija
Si $a + b = 1$, demuestre que $4ab \le 1$.

> [!example]- Solución
> Se sustituye $b = 1 - a$: $1 - 4ab = 1 - 4a(1 - a) = 4a^2 - 4a + 1 = (2a - 1)^2 \ge 0$. Equivalentemente, $1 - 4ab = (a - b)^2$ cuando $a + b = 1$. La igualdad ocurre en $a = b = \tfrac{1}{2}$.

## Preguntas de repaso

> [!question]- ¿Qué ejercicio es el recíproco del 3 y qué cambia en la conclusión?
> El 4: multiplicar por un negativo. Cambia el sentido de la desigualdad, porque $-z$ es positivo y se aplica el 3 a $-z$.

> [!question]- ¿Cómo se ve que el máximo de $ab$ con $a + b = 1$ es $\tfrac{1}{4}$?
> Con $b = 1 - a$, $4ab = 1 - (2a - 1)^2 \le 1$, con igualdad solo cuando $2a - 1 = 0$, es decir $a = \tfrac{1}{2}$.

> [!question]- ¿Qué hipótesis hace falta para que la desigualdad del ejercicio 5 sea estricta?
> Que $a, b, c$ no sean todos iguales. Si $a = b = c$, los tres cuadrados valen cero y la diferencia es $0$.
