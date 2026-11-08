---
ramo: "Introducción al Álgebra"
tema: "Polinomios: división y algoritmo de Euclides"
tags:
  - intro-algebra/polinomios
  - origen/complemento
prerrequisitos:
  - "[[01 - Polinomios, grado y coeficientes]]"
---

# División de polinomios

Así como se dividen enteros con cociente y resto, también se dividen polinomios: dado un dividendo $P$ y un divisor $D$ no nulo, existe un cociente $Q$ y un resto $R$ con $P = D \cdot Q + R$. La condición que hace único el resultado es que el resto tenga grado menor que el divisor.

## El algoritmo de la división

> [!tip] Algoritmo de la división
> Si $P, D \in \mathbb{R}[x]$ con $\operatorname{grad}(P) \ge \operatorname{grad}(D)$, existen únicos $Q, R \in \mathbb{R}[x]$ tales que
> $$P(x) = D(x) \cdot Q(x) + R(x),$$
> con $R \equiv 0$ o $0 \le \operatorname{grad}(R) < \operatorname{grad}(D)$. $Q$ es el **cociente** y $R$ el **resto**.

El procedimiento es una "división larga": se divide el término principal del dividendo por el del divisor, se multiplica y se resta, y se repite hasta que el grado de lo que queda sea menor que el del divisor.

## Un ejemplo paso a paso

Divida $P(x) = 8x^4 + 6x^2 - 3x + 1$ entre $D(x) = 2x^2 - x + 2$.

1. $8x^4 / 2x^2 = 4x^2$; se resta $4x^2 \cdot D$, y queda $4x^3 - 2x^2 - 3x + 1$.
2. $4x^3 / 2x^2 = 2x$; se resta $2x \cdot D$, y queda $-7x + 1$.
3. $-7x$ tiene grado $1 < 2 = \operatorname{grad}(D)$, así que se detiene.

Resultado: $Q(x) = 4x^2 + 2x$ y $R(x) = -7x + 1$.

> [!warning] Detenerse a tiempo
> La división termina cuando el grado del resto es **menor** que el del divisor. Seguir "dividiendo" un resto de grado menor daría fracciones, no un resto válido.

## Preguntas de repaso

> [!question]- ¿Qué condición deben cumplir el cociente y el resto en $P = D Q + R$?
> Que $R \equiv 0$ o $\operatorname{grad}(R) < \operatorname{grad}(D)$. Esa condición es la que hace únicos a $Q$ y $R$.

> [!question]- Al dividir un polinomio de grado $4$ entre uno de grado $2$, ¿qué grados puede tener el resto?
> Grado $0$ o $1$ (o ser el polinomio nulo): debe ser menor que $2$.

> [!question]- ¿Por qué el grado del cociente al dividir $P$ entre $D$ es $\operatorname{grad}(P) - \operatorname{grad}(D)$?
> Porque cada paso "baja" el grado del dividendo en el grado del divisor. Con $P$ de grado $4$ y $D$ de grado $2$, el cociente es de grado $2$.

> [!question]- En el ejemplo, ¿cuándo se detiene la división?
> Cuando lo que queda tras restar es $-7x + 1$, de grado $1$, menor que el grado $2$ del divisor. Ese es el resto.
