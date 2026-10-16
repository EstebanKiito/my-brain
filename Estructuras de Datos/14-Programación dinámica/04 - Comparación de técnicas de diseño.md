---
ramo: "Estructuras de Datos"
tema: "Programación dinámica"
tags:
  - edd
  - tecnicas-de-diseno
  - backtracking
  - greedy
  - programacion-dinamica
  - origen/complemento
prerrequisitos:
  - "[[03 - Problema del vuelto con programación dinámica]]"
  - "[[04 - Podas, propagación y heurísticas]]"
---

# Comparación de técnicas de diseño

El curso presenta cuatro estrategias de diseño de algoritmos: **dividir para conquistar**, **backtracking**, **algoritmos codiciosos** y **programación dinámica**. No todas resuelven los mismos problemas, y cuando varias sirven (típicamente en optimización), hay criterios para elegir. Reconocer qué estrategia pide un problema es tan importante como saber aplicarla.

## Qué pregunta hacerse

| Si el problema… | Técnica natural |
|---|---|
| Se descompone en subproblemas **disjuntos** del mismo tipo | Dividir para conquistar (mergesort, quicksort, búsqueda binaria) |
| Es asignar valores bajo restricciones (CSP) | Backtracking |
| Tiene un criterio de elección **probadamente** óptimo | Algoritmo codicioso |
| Tiene **subestructura óptima** y subproblemas que **se repiten** | Programación dinámica |

## En problemas de optimización

| Técnica | Garantía | Costo |
|---|---|---|
| Backtracking | Encuentra el óptimo, pero computando **todas** las soluciones factibles | Muy costoso en tiempo |
| Codicioso | Óptimo **solo si** la estrategia está probada | Muy eficiente en tiempo y memoria |
| Programación dinámica | Óptimo **si hay subestructura óptima** | Puede ser eficiente en tiempo y memoria (a cambio de la tabla) |

> [!tip] Cómo se relacionan
> - Backtracking **sin retroceder** y con una buena heurística es un algoritmo codicioso.
> - La programación dinámica es "backtracking que recuerda": explora las dos opciones de cada decisión, pero cada subproblema se resuelve una sola vez.
> - Dividir para conquistar con subproblemas que se solapan se vuelve programación dinámica al agregar memoización.

## Un caso: coloración de grafos

Una **$k$-coloración** de un grafo $G = (V, E)$ es una función $f: V \to \{1, \dots, k\}$ que asigna colores de modo que dos vértices unidos por una arista no tengan el mismo color. El problema **Col** pregunta si $G$ es $k$-coloreable.

- Es asignar valores (colores) bajo restricciones (vecinos distintos): es un **CSP** y se resuelve con **backtracking**. Variables: los vértices. Dominio: $\{1, \dots, k\}$. Restricción: $f(u) \ne f(v)$ para cada arista $(u, v)$.
- Comprobar si una $f$ dada es una $k$-coloración es fácil (se revisa cada arista), pero **encontrar** una puede requerir explorar muchas asignaciones.
- Un criterio codicioso ("al siguiente vértice, el menor color libre") siempre produce **alguna** coloración, pero puede usar más colores de los necesarios.

## Preguntas típicas

- **Modelar** un problema para backtracking: identificar variables, dominios y restricciones.
- Mejorar un backtracking con **poda, propagación o heurística**, a veces solo explicándolo en palabras.
- Mostrar con un **contraejemplo** que una estrategia codiciosa no es óptima.
- **Plantear la recurrencia** de una PD y el algoritmo que la implementa, y modificarla para una variante (monedas limitadas, otro criterio a optimizar).

## Preguntas de repaso

> [!question]- ¿Cuándo es preferible la programación dinámica a un algoritmo codicioso para optimizar?
> Cuando no hay un criterio codicioso probadamente óptimo, pero el problema tiene subestructura óptima. La PD garantiza el óptimo, y el algoritmo codicioso podría quedarse en un óptimo local.

> [!question]- ¿Por qué backtracking es poco conveniente para optimización?
> Porque para saber cuál es la mejor solución tiene que encontrar y comparar todas las factibles, lo que en general es exponencial.

> [!question]- ¿Qué distingue a la programación dinámica de dividir para conquistar?
> Que en PD los subproblemas se solapan y se guardan sus soluciones para no recalcularlas. En dividir para conquistar son disjuntos.

> [!question]- Modelar la $k$-coloración de un grafo como CSP.
> Variables: los vértices. Dominio de cada una: $\{1, \dots, k\}$. Restricciones: para cada arista $(u, v)$, $f(u) \ne f(v)$.
