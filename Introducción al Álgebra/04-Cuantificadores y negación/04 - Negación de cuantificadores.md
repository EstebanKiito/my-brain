---
ramo: "Introducción al Álgebra"
tema: "Cuantificadores y negación"
tags:
  - intro-algebra/cuantificadores
  - origen/complemento
prerrequisitos:
  - "[[03 - Orden de los cuantificadores]]"
---

# Negación de cuantificadores

Negar un cuantificador es "cambiarlo de signo" y negar el predicado: el universal se vuelve existencial y viceversa. Con esto se niega cualquier proposición cuantificada, por muchos cuantificadores anidados que tenga.

## Las dos reglas

Para una función proposicional $p(x)$, independientemente del universo:

$$
\neg\big[(\forall x \in U)\,p(x)\big] \iff (\exists x \in U)\,\neg p(x), \qquad
\neg\big[(\exists x \in U)\,p(x)\big] \iff (\forall x \in U)\,\neg p(x).
$$

> [!tip] Negación de cuantificadores
> La negación de "todo cumple" es "alguno no cumple"; la negación de "alguno cumple" es "ninguno cumple" ($\forall x\,\neg p$). Al negar, $\forall \leftrightarrow \exists$ y el predicado se niega.

## Negar proposiciones con cuantificadores anidados

Para negar, se van "empujando" las negaciones de izquierda a derecha: cada $\forall$ se vuelve $\exists$, cada $\exists$ se vuelve $\forall$, y al final se niega el predicado.

**Ejemplo.** Niegue $(\forall x \in \mathbb{R})(\forall y \in \mathbb{R})(\exists z \in \mathbb{R})(x < z < y)$.

$$
\neg(\forall x)(\forall y)(\exists z)(x < z < y) \iff (\exists x)(\exists y)(\forall z)\,\neg(x < z < y).
$$

Como $x < z < y$ es $(x < z) \wedge (z < y)$, su negación es $(x \ge z) \vee (z \ge y)$, así que la negación es

$$
(\exists x \in \mathbb{R})(\exists y \in \mathbb{R})(\forall z \in \mathbb{R})\big[(x \ge z) \vee (z \ge y)\big].
$$

> [!warning] Negar el predicado con De Morgan
> Al llegar al predicado, hay que negarlo bien. La negación de $x < z < y$ (un "y") es un "o": $(x \ge z) \vee (z \ge y)$. Dejar el "y" es el error típico.

Si el predicado es una implicación, se usa $\neg(p \Rightarrow q) \equiv p \wedge \neg q$: la negación de $(\forall x)(x > 2 \Rightarrow x \ge 3)$ es $(\exists x)(x > 2 \wedge x < 3)$. La negación de una implicación **no** es otra implicación.

## "Escriba la negación y demuestre la proposición o su negación"

Es la pregunta de cuantificadores más común en las pruebas. Exactamente una de las dos (la proposición o su negación) es verdadera, y se demuestra esa. La forma de demostrar depende del cuantificador **de afuera** de la que se elija:

| Se quiere demostrar… | Cómo |
|---|---|
| $(\exists x)\,p(x)$ | Exhibir un **testigo** concreto y verificar $p$ en él. |
| $(\forall x)\,p(x)$ | Tomar $x$ **arbitrario** y razonar en general (por casos si hace falta). |
| $(\forall x)(\exists y)\,p(x, y)$ | Tomar $x$ arbitrario y construir $y$ **en función de $x$** (como $y = x + 1$ o $y = 3/x$). |
| $(\exists x)(\forall y)\,p(x, y)$ | Elegir un $x$ fijo y probar $p(x, y)$ para todo $y$. |

Con dominios finitos chicos (como $A = \{1, 2, 3, 4\}$) se puede revisar elemento por elemento; con dominios infinitos no.

**Ejemplo.** $(\forall x \in \mathbb{R})\big(x < 3 \vee (\exists y \in \mathbb{R})(xy = 3)\big)$. Negación: $(\exists x \in \mathbb{R})\big(x \ge 3 \wedge (\forall y \in \mathbb{R})(xy \neq 3)\big)$. La original es verdadera: dado $x$, si $x < 3$ ya está; si $x \ge 3$, entonces $x \neq 0$ y $y = 3/x$ cumple $xy = 3$.

## Preguntas de repaso

> [!question]- ¿Cuál es la negación de $(\forall x)\,p(x)$ y de $(\exists x)\,p(x)$?
> $\neg(\forall x)\,p(x) \iff (\exists x)\,\neg p(x)$ y $\neg(\exists x)\,p(x) \iff (\forall x)\,\neg p(x)$. El cuantificador cambia y el predicado se niega.

> [!question]- Niegue $(\exists x \in \mathbb{R})(x^2 = 0)$.
> $(\forall x \in \mathbb{R})(x^2 \neq 0)$.

> [!question]- ¿Qué regla se aplica para negar una proposición con tres cuantificadores?
> Se recorren de izquierda a derecha cambiando cada $\forall$ por $\exists$ y cada $\exists$ por $\forall$, y al final se niega el predicado. No hay límite de cuantificadores.

> [!question]- ¿Cuál es la negación de $(\exists!\, x)\,p(x)$?
> Que no existe tal $x$, o que existen al menos dos distintos: $\neg(\exists! x)\,p(x) \iff \neg(\exists x)\,p(x) \vee (\exists x)(\exists y)(p(x) \wedge p(y) \wedge x \neq y)$.
