---
ramo: "Introducción al Álgebra"
tema: "Cuantificadores y negación"
tags:
  - intro-algebra/cuantificadores
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[04 - Negación de cuantificadores]]"
---

# Ejercicios de la guía de cuantificadores

Preguntas de la guía sobre cuantificadores, orden de cuantificadores, traducción de enunciados y negación. Conviene intentar cada una antes de abrir la solución.

## Ejercicios

### 1. Valores de verdad simples
Determine si son verdaderas o falsas: a) $(\exists x \in \mathbb{R})(x^3 = 1)$; b) $(\forall x \in \mathbb{R})(x^2 = 0)$; c) $(\exists!\, x \in \mathbb{R})(x - 1 = 0)$.

> [!example]- Solución
> a) **Verdadera**: $x = 1$ cumple $1^3 = 1$.
> b) **Falsa**: $x = 1$ da $1^2 = 1 \neq 0$, un contraejemplo.
> c) **Verdadera**: la única solución de $x - 1 = 0$ es $x = 1$.

### 2. Cuantificadores sobre el alfabeto
Sobre $U = \{a, b, c, \dots, x, y, z\}$, determine el valor de verdad de a) $(\forall \alpha)(\alpha = x)$; b) $(\exists \alpha)(\alpha \neq x)$; c) $(\exists!\, \alpha)(\alpha = a)$.

> [!example]- Solución
> a) **Falsa**: solo la letra $x$ es igual a $x$; las demás no.
> b) **Verdadera**: por ejemplo, $a \neq x$.
> c) **Verdadera**: solo la letra $a$ es igual a $a$.

### 3. Traducir y negar
Traduzca al lenguaje matemático y luego niegue: "los números naturales tienen un menor elemento, pero no tienen un mayor elemento".

> [!example]- Solución
> Menor elemento: $(\exists m \in \mathbb{N})(\forall n \in \mathbb{N})(m \le n)$. No mayor elemento: $\neg(\exists M \in \mathbb{N})(\forall n \in \mathbb{N})(n \le M) \equiv (\forall M \in \mathbb{N})(\exists n \in \mathbb{N})(n > M)$. La frase completa es
> $$(\exists m \in \mathbb{N})(\forall n \in \mathbb{N})(m \le n) \;\wedge\; (\forall M \in \mathbb{N})(\exists n \in \mathbb{N})(n > M).$$
> Negando con De Morgan:
> $$(\forall m \in \mathbb{N})(\exists n \in \mathbb{N})(m > n) \;\vee\; (\exists M \in \mathbb{N})(\forall n \in \mathbb{N})(n \le M).$$

### 4. Negación del "existe único"
¿Cuál es la negación de $(\exists!\, x \in U)\,p(x)$?

> [!example]- Solución
> Como $(\exists! x)\,p(x) \iff (\exists x)\,p(x) \wedge (\forall x)(\forall y)[(p(x) \wedge p(y)) \Rightarrow x = y]$, su negación es "no existe ningún $x$, o existen al menos dos distintos":
> $$\neg(\exists! x)\,p(x) \iff \neg(\exists x)\,p(x) \;\vee\; (\exists x)(\exists y)\big(p(x) \wedge p(y) \wedge x \neq y\big).$$

### 5. Negar una proposición con "existe único"
Niegue la proposición $(\forall y \in \mathbb{R}^+)(\exists!\, x \in \mathbb{R}^+)(x^2 = y)$.

> [!example]- Solución
> Se cambia $\forall$ por $\exists$ y se niega el $(\exists!)$:
> $$(\exists y \in \mathbb{R}^+)\,\neg(\exists!\, x \in \mathbb{R}^+)(x^2 = y) \iff (\exists y \in \mathbb{R}^+)\Big[(\forall x \in \mathbb{R}^+)(x^2 \neq y) \;\vee\; (\exists x)(\exists z)(x^2 = y \wedge z^2 = y \wedge x \neq z)\Big].$$
> La proposición original es verdadera (cada $y > 0$ tiene una única raíz cuadrada positiva), así que su negación es falsa.

## Preguntas de repaso

> [!question]- ¿Qué patrón se sigue al negar una proposición con varios cuantificadores?
> Se recorren los cuantificadores de izquierda a derecha cambiando $\forall \leftrightarrow \exists$, y al final se niega el predicado (aplicando De Morgan si es un "y" o un "o").

> [!question]- ¿Cómo se traduce "no tiene mayor elemento" en símbolos?
> $\neg(\exists M)(\forall n)(n \le M)$, que equivale a $(\forall M)(\exists n)(n > M)$: para todo candidato $M$ hay un natural que lo supera.

> [!question]- ¿Qué dos maneras hay de que falle un "existe único"?
> Que no exista ningún elemento con la propiedad, o que existan dos (o más) distintos con ella. Son los dos casos de la negación de $\exists!$.
