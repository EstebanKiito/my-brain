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

## Preguntas de repaso

> [!question]- ¿Cuál es la negación de $(\forall x)\,p(x)$ y de $(\exists x)\,p(x)$?
> $\neg(\forall x)\,p(x) \iff (\exists x)\,\neg p(x)$ y $\neg(\exists x)\,p(x) \iff (\forall x)\,\neg p(x)$. El cuantificador cambia y el predicado se niega.

> [!question]- Niegue $(\exists x \in \mathbb{R})(x^2 = 0)$.
> $(\forall x \in \mathbb{R})(x^2 \neq 0)$.

> [!question]- ¿Qué regla se aplica para negar una proposición con tres cuantificadores?
> Se recorren de izquierda a derecha cambiando cada $\forall$ por $\exists$ y cada $\exists$ por $\forall$, y al final se niega el predicado. No hay límite de cuantificadores.

> [!question]- ¿Cuál es la negación de $(\exists!\, x)\,p(x)$?
> Que no existe tal $x$, o que existen al menos dos distintos: $\neg(\exists! x)\,p(x) \iff \neg(\exists x)\,p(x) \vee (\exists x)(\exists y)(p(x) \wedge p(y) \wedge x \neq y)$.
