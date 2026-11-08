---
ramo: "Introducción al Álgebra"
tema: "Geometría analítica: distancia, circunferencia y división de segmentos"
tags:
  - intro-algebra/geometria-analitica
  - origen/complemento
prerrequisitos:
  - "[[02 - La circunferencia]]"
---

# Tangentes a una circunferencia

La recta **tangente** a una circunferencia en un punto $P$ de ella es la perpendicular al radio en $P$. Según dónde esté un punto, puede haber cero, una o dos tangentes a la circunferencia que pasan por él.

## Cuántas tangentes hay

Dado un punto $P$ y una circunferencia $C$:

1. Si $P$ está **dentro** de $C$: no hay tangentes por $P$.
2. Si $P$ está **sobre** $C$: hay exactamente una tangente (la perpendicular al radio).
3. Si $P$ está **fuera** de $C$: hay exactamente dos tangentes.

> [!tip] Condición de tangencia
> Una recta es tangente a una circunferencia de centro $Q$ y radio $r$ si y solo si la distancia del centro a la recta es $r$: $d(Q, L) = r$.

## Hallar las tangentes

**Ejemplo.** Halle las tangentes desde $(1, -1)$ a $x^2 + y^2 + 2x - 6y - 6 = 0$.

La familia de rectas por $(1, -1)$ es $y + 1 = m(x - 1)$. Sustituyendo en la circunferencia queda una cuadrática en $x$; exigir que la recta sea tangente es pedir que esa cuadrática tenga **discriminante cero**, lo que da $3m^2 - 4m = 0$, es decir $m = 0$ o $m = \tfrac43$. Las tangentes son $y = -1$ y $y + 1 = \tfrac43(x - 1)$.

**Ejemplo.** Halle las tangentes de pendiente $m = 2$ a la misma circunferencia.

Se prueba con rectas $y = 2x + k$. Sustituyendo e igualando el discriminante a cero se obtiene $k^2 - 10k - 55 = 0$, o sea $k = 5 \pm 4\sqrt5$. Las tangentes son $y = 2x + 5 \pm 4\sqrt5$.

> [!warning] El discriminante mide la tangencia
> Una recta y una circunferencia pueden cortarse en 2 puntos (discriminante $>0$), ser tangentes ($=0$) o no tocarse ($<0$). Igualar el discriminante a cero es el método para exigir tangencia.

## Preguntas de repaso

> [!question]- ¿Qué es la tangente a una circunferencia en un punto de ella?
> La recta perpendicular al radio en ese punto. Es la única recta que toca la circunferencia en un solo punto.

> [!question]- ¿Cuántas tangentes pasan por un punto exterior?
> Dos. Por uno interior, ninguna; por uno sobre la circunferencia, exactamente una.

> [!question]- ¿Qué condición algebraica impone que una recta sea tangente?
> Que al sustituir la recta en la ecuación de la circunferencia, la cuadrática resultante tenga discriminante cero (una sola intersección).

> [!question]- ¿Cómo se relaciona la tangente con la distancia del centro a la recta?
> Una recta es tangente si y solo si $d(Q, L) = r$: la distancia del centro a la recta iguala al radio.
