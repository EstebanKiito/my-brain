---
ramo: "Introducción al Álgebra"
tema: "Números complejos, inversas y ecuaciones trigonométricas"
tags:
  - intro-algebra/trigonometria
  - origen/complemento
prerrequisitos:
  - "[[02 - Seno y coseno en la circunferencia unitaria]]"
---

# Inversas trigonométricas

Las funciones seno, coseno y tangente no son inyectivas en todo $\mathbb{R}$, así que para invertirlas se restringe su dominio a un tramo donde sí lo sean. Las inversas resultantes, $\arcsin$, $\arccos$ y $\arctan$, devuelven un ángulo en ese tramo.

## Arcoseno, arcocoseno y arcotangente

| Función | Dominio restringido | Inversa |
|---|---|---|
| $\sin x$ | $[-\pi/2, \pi/2]$ | $\arcsin y = x \iff \sin x = y \wedge -\pi/2 \le x \le \pi/2$ |
| $\cos x$ | $[0, \pi]$ | $\arccos y = x \iff \cos x = y \wedge 0 \le x \le \pi$ |
| $\tan x$ | $(-\pi/2, \pi/2)$ | $\arctan y = x \iff \tan x = y \wedge -\pi/2 < x < \pi/2$ |

> [!tip] El rango es clave
> $\arcsin$ devuelve ángulos en $[-\pi/2, \pi/2]$, $\arccos$ en $[0, \pi]$ y $\arctan$ en $(-\pi/2, \pi/2)$. El valor de la inversa **siempre** cae en ese rango, aunque el ángulo original no estuviera ahí.

**Ejemplo.** $\arcsin(\sin(\pi/3)) = \pi/3$, pero $\arcsin(\sin(2\pi/3)) = \pi/3$, no $2\pi/3$: como $2\pi/3 \notin [-\pi/2, \pi/2]$, la inversa devuelve el ángulo de igual seno que sí está en el rango.

## Componer inversas con funciones

**Ejemplo.** Exprese $\cos(\arctan x)$ en términos de $x$. Sea $\theta = \arctan x$, así $\tan\theta = x$ y $\theta \in (-\pi/2, \pi/2)$. En ese rango el coseno es positivo, y $\cos\theta = \frac{1}{\sqrt{1 + \tan^2\theta}} = \frac{1}{\sqrt{1 + x^2}}$.

**Ejemplo.** Exprese $\sin(2\arccos x)$. Sea $\theta = \arccos x$, con $\cos\theta = x$ y $\theta \in [0,\pi]$ (donde $\sin\theta \ge 0$). Entonces $\sin(2\theta) = 2\sin\theta\cos\theta = 2x\sqrt{1 - x^2}$.

> [!warning] No "cancelar" a ciegas
> $\arcsin(\sin x) = x$ solo si $x \in [-\pi/2, \pi/2]$. Fuera de ese rango, la inversa devuelve otro ángulo con el mismo seno.

## Preguntas de repaso

> [!question]- ¿Por qué hay que restringir el dominio para definir $\arcsin$?
> Porque $\sin$ no es inyectiva en $\mathbb{R}$ (muchos ángulos comparten seno). Restringida a $[-\pi/2, \pi/2]$ sí lo es, y ahí se define su inversa.

> [!question]- ¿Cuánto vale $\arccos(\cos(-\pi/3))$?
> $\cos(-\pi/3) = 1/2$, y $\arccos(1/2) = \pi/3$ (que es el ángulo en $[0,\pi]$ con coseno $1/2$).

> [!question]- Demuestre que $\arcsin x + \arccos x = \pi/2$.
> Sea $\theta = \arcsin x$, con $\sin\theta = x$ y $\theta \in [-\pi/2, \pi/2]$. Entonces $\cos(\pi/2 - \theta) = \sin\theta = x$ y $\pi/2 - \theta \in [0, \pi]$, así que $\arccos x = \pi/2 - \theta$. Sumando, $\arcsin x + \arccos x = \pi/2$.

> [!question]- ¿Cuál es el rango de $\arctan$?
> $(-\pi/2, \pi/2)$, abierto: la tangente tiende a $\pm\infty$ en los extremos y nunca se alcanzan.
