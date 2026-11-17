---
ramo: "Matemáticas Discretas"
tema: "Aritmética modular y criptografía"
tags:
  - discretas/teoria-de-numeros
  - origen/complemento
prerrequisitos: []
---

# Divisibilidad y división con resto

Toda la aritmética modular se apoya en una sola idea: dividir enteros y quedarse con el resto. Antes de hablar de congruencias, de máximo común divisor o de criptografía hay que fijar qué significa que un número "divida" a otro y por qué siempre existe un resto único.

## La relación "divide a"

El entero $a \ne 0$ **divide** a $b$, escrito $a \mid b$, si existe $k \in \mathbb{Z}$ con $b = k \cdot a$. Es decir, $b$ es múltiplo de $a$. Por ejemplo $3 \mid 9$, $18 \mid 72$ y $2 \mid -4$, pero $7 \nmid 9$.

Propiedades que se usan sin cesar y salen directo de la definición:

- Si $c \mid a$ y $c \mid b$, entonces $c \mid (xa + yb)$ para cualesquiera enteros $x, y$ (una combinación lineal conserva la divisibilidad).
- Si $a \mid b$ y $b \mid c$, entonces $a \mid c$ (transitividad).
- Todo entero $a \neq 0$ divide a $0$, y $1$ divide a todos.

> [!tip] Divisor de 1
> Los únicos enteros que dividen a $1$ son $1$ y $-1$. Este hecho aparece al demostrar que dos números son coprimos: si un divisor común divide a $1$, solo puede ser $1$.

## División con resto

> [!tip] Teorema de la división con resto
> Dados $a, n \in \mathbb{Z}$ con $n > 0$, existen únicos $\alpha, \beta \in \mathbb{Z}$ con $a = \alpha n + \beta$ y $0 \le \beta < n$.

Aquí $\alpha = \lfloor a/n \rfloor$ es el **cuociente** y $\beta$ es el **resto**. Se escribe $\beta = a \bmod n$, y por construcción $0 \le a \bmod n < n$. La existencia sale de tomar el mayor múltiplo de $n$ que no supera a $a$; la unicidad, de que dos restos distintos en $[0, n)$ no pueden diferir en un múltiplo de $n$.

Ejemplo: $3 = 1 \cdot 2 + 1$, luego $3 \bmod 2 = 1$. Con negativos el resto sigue siendo no negativo: $-7 = (-3) \cdot 3 + 2$, así que $-7 \bmod 3 = 2$ (muchos lenguajes de programación devuelven $-1$ para `-7 % 3`; la matemática discreta usa la convención del resto no negativo).

## Una aplicación: representar números en base $b$

La división con resto permite escribir cualquier $n \ge 1$ en base $b > 1$ de manera única, $n = a_{k-1} b^{k-1} + \dots + a_1 b + a_0$ con $0 \le a_i < b$ y $a_{k-1} \ne 0$. La idea: $n = q b + r$, con $r = a_0$ el último dígito y $q < n$ el resto de los dígitos; por inducción fuerte $q$ tiene representación única, y $r$ y $q$ son únicos por el teorema anterior.

Ejemplo en base $3$: $23 = 7 \cdot 3 + 2$, $7 = 2 \cdot 3 + 1$, $2 = 0 \cdot 3 + 2$, luego $23 = 2 \cdot 3^2 + 1 \cdot 3 + 2$, es decir $212_3$. Esa misma descomposición es la que explica el criterio de divisibilidad por $3$ de [[02 - Congruencias módulo n y aritmética en Z_n]].

## Números primos

Un **primo** es un entero $p > 1$ cuyos únicos divisores positivos son $1$ y $p$. Todo $n > 1$ se factoriza en primos (inducción fuerte, ver [[03 - Inducción fuerte]]). Que esa factorización sea **única** requiere el resultado clave de [[03 - Máximo común divisor y algoritmo de Euclides]] y [[04 - Identidad de Bézout y algoritmo de Euclides extendido]]: si $p \mid ab$ entonces $p \mid a$ o $p \mid b$.

> [!warning] "Divide a" no es simétrica
> $a \mid b$ no implica $b \mid a$ (salvo $b = \pm a$), así que no es una relación de equivalencia; además $a \mid b$ es una afirmación (verdadera o falsa), mientras que $b / a$ o $b \bmod a$ son números.

## Preguntas de repaso

> [!question]- ¿Por qué si $c \mid a$ y $c \mid b$ entonces $c \mid (xa + yb)$?
> Porque $a = c k_1$ y $b = c k_2$, luego $xa + yb = c(xk_1 + yk_2)$ y $xk_1 + yk_2 \in \mathbb{Z}$.

> [!question]- ¿Cuánto vale $-7 \bmod 3$ y por qué no es $-1$?
> Vale $2$, porque $-7 = (-3) \cdot 3 + 2$ y el resto debe cumplir $0 \le r < 3$.

> [!question]- ¿Qué garantiza que el resto de la división sea único?
> Si $a = \alpha n + \beta = \gamma n + \delta$ con restos en $[0, n)$, entonces $n \mid (\beta - \delta)$ y $\lvert \beta - \delta \rvert < n$ fuerza $\beta = \delta$.

> [!question]- ¿Cómo se obtienen los dígitos de $n$ en base $b$?
> Dividiendo repetidamente por $b$: los restos sucesivos son los dígitos, empezando por el menos significativo.
