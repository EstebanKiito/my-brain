---
ramo: "Introducción al Álgebra"
tema: "Cuantificadores y negación"
tags:
  - intro-algebra/cuantificadores
  - origen/complemento
prerrequisitos:
  - "[[02 - Demostrar con cuantificadores]]"
---

# Orden de los cuantificadores

Cuando una proposición tiene varios cuantificadores, **el orden importa**: $(\exists x)(\forall y)$ no dice lo mismo que $(\forall y)(\exists x)$. Cambiarlos de lugar puede convertir una afirmación verdadera en falsa.

## Qué conmuta y qué no

Para una función proposicional $p(x, y)$ con dominio $U$:

1. $(\forall x)(\forall y)\,p(x,y) \iff (\forall y)(\forall x)\,p(x,y)$: dos universales conmutan.
2. $(\exists x)(\exists y)\,p(x,y) \iff (\exists y)(\exists x)\,p(x,y)$: dos existenciales conmutan.
3. $(\exists x)(\forall y)\,p(x,y) \implies (\forall y)(\exists x)\,p(x,y)$: el "existe que sirve para todos" es más fuerte.

> [!tip] La implicación clave
> $(\exists x)(\forall y)\,p \implies (\forall y)(\exists x)\,p$. Si hay **un** $x$ que funciona para todo $y$, entonces para cada $y$ hay (ese mismo) $x$. El recíproco no vale.

> [!warning] El recíproco no vale
> $(\forall y)(\exists x)\,p$ **no** implica $(\exists x)(\forall y)\,p$. Contraejemplo con $U = \mathbb{N}$ y $p(x,y) \iff x > y$: es cierto que $(\forall y)(\exists x)(x > y)$ (dado $y$, tomo $x = y+1$), pero falso que $(\exists x)(\forall y)(x > y)$, porque ningún entero es mayor que todos.

## El orden en un ejemplo

Con $p(n, m) \iff m < n$ sobre los naturales:

- $(\forall m)(\exists n)(m < n)$ es **verdadera**: dado $m$, tomo $n = m + 1$.
- $(\exists n)(\forall m)(m < n)$ es **falsa**: ningún $n$ es mayor que todos los naturales (ni siquiera que él mismo).
- $(\forall n)(\exists m)(m < n)$ es **falsa**: para $n = 1$ no hay $m$ natural con $m < 1$.
- $(\exists m)(\forall n)(m < n)$ es **falsa**: ningún $m$ es menor que todos (ni que sí mismo).

## Otro ejemplo: el opuesto aditivo

$(\forall x \in \mathbb{R})(\exists y \in \mathbb{R})(x + y = 0)$ es **verdadera**: dado $x$, el $y = -x$ cumple. En cambio $(\exists y \in \mathbb{R})(\forall x \in \mathbb{R})(x + y = 0)$ es **falsa**: no hay un único $y$ que sea el opuesto de todos los reales a la vez.

## Preguntas de repaso

> [!question]- ¿Qué cuantificadores conmutan entre sí?
> Dos universales entre sí y dos existenciales entre sí: $(\forall x)(\forall y) \iff (\forall y)(\forall x)$ y $(\exists x)(\exists y) \iff (\exists y)(\exists x)$. Un universal y un existencial **no** conmutan en general.

> [!question]- Explique con palabras la diferencia entre $(\exists x)(\forall y)$ y $(\forall y)(\exists x)$.
> La primera dice "hay un $x$ que sirve para **todos** los $y$" (el mismo $x$). La segunda dice "para **cada** $y$ hay un $x$" (que puede depender de $y$). La primera es más fuerte.

> [!question]- Dé un contraejemplo de que $(\forall y)(\exists x)$ no implica $(\exists x)(\forall y)$.
> En $\mathbb{N}$ con $x > y$: $(\forall y)(\exists x)(x > y)$ es cierto (dado $y$, $x = y+1$), pero $(\exists x)(\forall y)(x > y)$ es falso porque ningún natural es mayor que todos.

> [!question]- ¿Por qué $(\forall n \in \mathbb{N})(\exists m \in \mathbb{N})(m < n)$ es falsa?
> Porque para $n = 1$ no existe un natural $m$ con $m < 1$: el menor natural es $1$.
