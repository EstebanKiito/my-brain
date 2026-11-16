---
ramo: "Introducción al Cálculo"
tema: "Exponencial y logaritmo"
tags:
  - intro-calculo/exponencial
  - origen/complemento
prerrequisitos:
  - "[[01 - El número e y la función exponencial]]"
---

# Desigualdad fundamental y propiedades de la exponencial

Las propiedades de la exponencial que más se usan (que es positiva, que es estrictamente creciente y que por eso es inyectiva) salen de una sola desigualdad: $e^x \ge 1 + x$. Esta nota muestra cómo, y es un buen ejemplo del estilo de las demostraciones del curso.

## La desigualdad fundamental

> [!tip] Desigualdad fundamental
> Para todo $x \in \mathbb{R}$: $e^x \ge 1 + x$.

Se apoya en dos hechos que el curso prueba más adelante, en el capítulo de sucesiones:

1. **Teorema:** para todo $x \in \mathbb{R}$ y todo $n \in \mathbb{N}$, $\left(1 + \tfrac{x}{n}\right)^n \le e^x$.
2. **Desigualdad de Bernoulli** (por inducción): $(1 + t)^n \ge 1 + nt$ para $t \ge -1$ y $n \in \mathbb{N}$.

*Demostración.* Combinando ambas con $t = \tfrac{x}{n}$,
$$e^x \ge \left(1 + \frac{x}{n}\right)^n \ge 1 + n \cdot \frac{x}{n} = 1 + x. \qquad \blacksquare$$

## La exponencial es positiva

> [!tip] Positividad
> Para todo $x \in \mathbb{R}$, $e^x > 0$. En particular, la exponencial no tiene ceros.

*Demostración.* Se separa en dos casos. Si $x > -1$, entonces $1 + x > 0$ y por la desigualdad fundamental $e^x \ge 1 + x > 0$. Si $x \le -1$, se usa el **principio de Arquímedes** (los naturales no están acotados superiormente): como $-x > 0$, existe $n \in \mathbb{N}$ con $-x < n$, es decir $1 + \tfrac{x}{n} > 0$. Entonces $\left(1 + \tfrac{x}{n}\right)^n > 0$ (producto de $n$ números positivos) y $e^x \ge \left(1 + \tfrac{x}{n}\right)^n > 0$. $\blacksquare$

## Crecimiento estricto e inyectividad

> [!tip] Monotonía
> Si $x < y$, entonces $e^x < e^y$. La exponencial es **estrictamente creciente** y, por lo tanto, inyectiva.

*Demostración.* Con $e^y = e^x e^{y - x}$ y la desigualdad fundamental aplicada a $y - x$:
$$e^y = e^x e^{y - x} \ge e^x (1 + y - x) > e^x,$$
porque $e^x > 0$ y $y - x > 0$. $\blacksquare$

De la positividad y el crecimiento se deduce que el recorrido de la exponencial es $(0, \infty)$, de modo que $\exp : \mathbb{R} \to (0, \infty)$ es **biyectiva** (la sobreyectividad requiere además la continuidad, que el curso da por sentada) y admite la [[03 - Logaritmo natural y sus propiedades|inversa logarítmica]].

## Consecuencias que se usan en ejercicios

- **Ecuaciones:** $e^a = e^b \iff a = b$, y $e^x = k$ no tiene solución si $k \le 0$. Por ejemplo, de $e^x = -2$ no sale nada, porque $e^x > 0$.
- **Desigualdades:** $e^a < e^b \iff a < b$ (la exponencial conserva el orden).
- **Suma de una exponencial y su inversa:** para todo $x$, $e^x + e^{-x} \ge 2$. Con $u = e^x > 0$ equivale a $u^2 + 1 \ge 2u$, o sea $(u - 1)^2 \ge 0$. (Otra vía: sumar $e^x \ge 1 + x$ y $e^{-x} \ge 1 - x$.)

> [!warning] No confundir $e^{-x}$ con $-e^x$
> $e^{-x} = \tfrac{1}{e^x}$ es positiva y decreciente; $-e^x$ es negativa y decreciente. Se distinguen en el gráfico: una queda sobre el eje $x$ y la otra debajo.

## Preguntas de repaso

> [!question]- ¿Cómo se prueba que $e^x > 0$ para $x \le -1$ si la desigualdad fundamental no ayuda?
> Con el principio de Arquímedes se escoge $n$ tan grande que $1 + \frac{x}{n} > 0$, y se usa $e^x \ge (1 + \frac{x}{n})^n > 0$.

> [!question]- ¿De dónde sale que $e^x$ es estrictamente creciente?
> De $e^y = e^x e^{y - x} \ge e^x(1 + y - x) > e^x$ cuando $y > x$.

> [!question]- ¿Cuántas soluciones tiene $e^x = -3$ y por qué?
> Ninguna: la exponencial es siempre positiva.

> [!question]- Demuestre que $e^x + e^{-x} \ge 2$.
> Con $u = e^x > 0$, la desigualdad es $u + \frac{1}{u} \ge 2$, equivalente a $(u - 1)^2 \ge 0$, que siempre vale.
