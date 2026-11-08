---
ramo: "Introducción al Álgebra"
tema: "Técnicas de demostración e inducción"
tags:
  - intro-algebra/tecnicas-demostracion
  - origen/complemento
prerrequisitos:
  - "[[06 - Técnicas de demostración como tautologías]]"
---

# Método directo

Demostrar una afirmación de la forma "si $p$, entonces $q$" significa mostrar que $q$ se sigue de $p$ mediante pasos que preservan la verdad. El **método directo** es la forma más natural: se supone la hipótesis $p$ y se encadena una deducción hasta llegar a la tesis $q$.

## Qué es el método directo

Para probar $p \Rightarrow q$ por el método directo se parte de $p$ (la hipótesis) y, usando definiciones, axiomas y resultados ya conocidos, se deriva paso a paso la conclusión $q$. Cada paso es una implicación válida, de modo que la verdad "fluye" de $p$ a $q$.

> [!tip] Método directo
> Para demostrar $p \Rightarrow q$: **suponga $p$** y, a partir de ahí, deduzca $q$ con implicaciones válidas. Si cada paso conserva la verdad, la conclusión hereda la verdad de la hipótesis.

## Ejemplo: $a \cdot 0 = 0$

Pruebe que para todo número real $a$ se cumple $a \cdot 0 = 0$.

**Demostración.** Como $0$ es el elemento neutro de la suma, $0 + 0 = 0$, así que

$$
a \cdot 0 = a \cdot (0 + 0) = a \cdot 0 + a \cdot 0
$$

por la distributividad. Sumando el opuesto de $a \cdot 0$ a ambos lados, $a \cdot 0 - a \cdot 0 = a \cdot 0 + a \cdot 0 - a \cdot 0$, es decir, $0 = a \cdot 0$.

## Ejemplo: impar al cuadrado

Pruebe que si $n$ es un natural impar, entonces $n^2$ es de la forma $8k + 1$ con $k \ge 1$ entero.

**Demostración.** Si $n$ es impar, $n = 2m + 1$ con $m \in \mathbb{N}$. Entonces

$$
n^2 = (2m+1)^2 = 4m^2 + 4m + 1 = 4m(m+1) + 1.
$$

El producto $m(m+1)$ de dos naturales consecutivos es siempre par, así que $m(m+1) = 2k$ para algún $k \ge 1$, y por lo tanto $n^2 = 4 \cdot 2k + 1 = 8k + 1$.

> [!warning] "Suficiente" y "necesario"
> En $p \Rightarrow q$ se dice que $p$ es **condición suficiente** para $q$ (basta $p$ para tener $q$) y que $q$ es **condición necesaria** para $p$ (sin $q$ no puede darse $p$). Leer así los enunciados ayuda a reconocer la hipótesis y la tesis.

## Preguntas de repaso

> [!question]- ¿Cuál es el primer paso del método directo para probar $p \Rightarrow q$?
> Suponer la hipótesis $p$. A partir de ella se deduce, con pasos válidos, la tesis $q$.

> [!question]- En la prueba de $a \cdot 0 = 0$, ¿qué propiedad convierte $a(0+0)$ en $a\cdot 0 + a\cdot 0$?
> La distributividad del producto respecto de la suma, junto con el hecho de que $0 = 0 + 0$ (neutro aditivo).

> [!question]- ¿Por qué $m(m+1)$ es siempre par?
> Porque entre dos naturales consecutivos siempre hay uno par. Si $m$ es par, el producto lo es; si $m$ es impar, entonces $m+1$ es par.

> [!question]- Reescriba "para que una matriz sea invertible es necesario que su determinante sea no nulo" como una implicación.
> "Matriz invertible $\Rightarrow$ determinante no nulo". Lo "necesario" es la tesis: sin determinante no nulo no hay inversa.
