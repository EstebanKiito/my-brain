---
ramo: "Introducción al Cálculo"
tema: "Inecuaciones"
tags:
  - intro-calculo/inecuaciones
  - origen/complemento
prerrequisitos:
  - "[[03 - Vecindades e intervalos con valor absoluto]]"
---

# Intervalos y representación en la recta

Los conjuntos solución de las inecuaciones casi nunca son un punto: son tramos enteros de la recta real. Los intervalos son el lenguaje para escribirlos, y operar con ellos (unir, intersecar, quitar puntos) es el último paso de cada ejercicio. Conviene dominar su notación antes de resolver cualquier inecuación.

## La recta real y los intervalos

Los reales se representan sobre una recta horizontal con dos convenciones: si $x < y$, el punto $x$ queda a la izquierda de $y$, y el punto medio entre ambos es $\tfrac{x + y}{2}$.

> [!tip] Intervalos acotados
> Para $a \le b$:
> - **Abierto:** $(a, b) = \{x \in \mathbb{R} : a < x < b\}$.
> - **Cerrado:** $[a, b] = \{x : a \le x \le b\}$.
> - **Semiabiertos:** $(a, b] = \{x : a < x \le b\}$ y $[a, b) = \{x : a \le x < b\}$.

> [!tip] Intervalos no acotados
> $(-\infty, a] = \{x : x \le a\}$, $(-\infty, a) = \{x : x < a\}$, $[a, \infty) = \{x : a \le x\}$, $(a, \infty) = \{x : a < x\}$, y $\mathbb{R} = (-\infty, \infty)$.

Algunas observaciones útiles:

- En lugar de $(a, b)$ también se escribe $]a, b[$; los apuntes y las pautas usan ambas notaciones.
- Si $a = b$, entonces $(a, a) = (a, a] = [a, a) = \varnothing$ y $[a, a] = \{a\}$.
- $\pm\infty$ **nunca** se incluye: siempre lleva paréntesis, porque no es un número real.

## Cómo se leen en la recta

Un extremo incluido se dibuja con un punto lleno (o corchete) y uno excluido con un punto vacío (o paréntesis). Así, $[1, 4)$ es el segmento de $1$ a $4$ que contiene al $1$ pero no al $4$.

## Operar con intervalos

Las soluciones de las inecuaciones se combinan con unión e intersección; en la recta, estas operaciones se ven directamente.

> [!example]- Unión, intersección y diferencia (ejemplos)
> - $(-\infty, 1) \cap [-3, 5] = [-3, 1)$: se queda con lo que está en ambos.
> - $(-\infty, 0] \cup (0, 2) = (-\infty, 2)$: los dos tramos se pegan porque el $0$ cubre el hueco.
> - $[-1, 4) \setminus \{2\} = [-1, 2) \cup (2, 4)$: quitar un punto parte el intervalo en dos.
> - $(1, 5) \cap (6, 9) = \varnothing$: los tramos no se tocan.

> [!warning] Tres errores de escritura frecuentes
> - Escribir $x \in (2, 1)$: el extremo izquierdo debe ser menor que el derecho.
> - Unir con "$+$" en lugar de $\cup$, o escribir "$-1 < x > 3$"; se escribe $x \in (-1, \infty)$ o $x > 3$, según el caso.
> - Olvidar que una restricción del dominio (un punto donde se anula un denominador) **sale** del conjunto aunque el intervalo lo contenga.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre $[2, 5)$ y $(2, 5]$?
> En el primero el $2$ pertenece al conjunto y el $5$ no; en el segundo es al revés.

> [!question]- ¿Por qué $\infty$ siempre lleva paréntesis?
> Porque no es un número real y por tanto no puede ser elemento de un subconjunto de $\mathbb{R}$.

> [!question]- Escriba $[-1, 4) \setminus \{2\}$ como unión de intervalos.
> $[-1, 2) \cup (2, 4)$.

> [!question]- ¿Cuánto vale $(3, 3]$?
> Es el conjunto vacío: ningún real cumple $3 < x \le 3$.
