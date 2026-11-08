---
ramo: "Introducción al Álgebra"
tema: "Polinomios: raíces y gráfica"
tags:
  - intro-algebra/polinomios
  - origen/complemento
prerrequisitos:
  - "[[01 - Raíces y el teorema del factor]]"
---

# Teorema de los ceros racionales

Para un polinomio con coeficientes enteros, las raíces racionales no son arbitrarias: si $p/q$ es una raíz (en forma irreducible), entonces $p$ divide al coeficiente constante y $q$ divide al coeficiente principal. Esto reduce la búsqueda a una lista finita de candidatos.

## El teorema

> [!tip] Teorema de los ceros racionales
> Si $P(x) = a_n x^n + \dots + a_0 \in \mathbb{Z}[x]$ y $\alpha = p/q$ es una raíz racional con $p$ y $q$ sin factores comunes, entonces $p \mid a_0$ y $q \mid a_n$.

Los candidatos se obtienen tomando $p$ entre los divisores de $a_0$ y $q$ entre los divisores de $a_n$, y luego se evalúa cada uno.

## Encontrar las raíces

**Ejemplo.** Para $P(x) = 2x^3 - 7x^2 + 2$, liste las posibles raíces racionales y encuéntrelas.

Los divisores de $a_0 = 2$ son $\pm 1, \pm 2$, y los de $a_n = 2$ también $\pm 1, \pm 2$. Los candidatos son $\pm 1, \pm 2, \pm \tfrac12$. Evaluando, $P(-\tfrac12) = -\tfrac14 - \tfrac74 + 2 = 0$, así que $-\tfrac12$ es raíz. Dividiendo, $P(x) = (2x + 1)(x^2 - 4x + 2)$, y el cuadrático tiene discriminante $16 - 8 = 8 > 0$, con raíces $2 \pm \sqrt{2}$.

Las raíces son $-\tfrac12$, $2 + \sqrt{2}$ y $2 - \sqrt{2}$: solo **una** es racional.

> [!warning] El teorema da candidatos, no garantiza raíces
> La lista de $p/q$ es de *candidatos*: puede que ninguno sea raíz (entonces el polinomio no tiene raíces racionales), o que existan raíces irracionales o complejas fuera de la lista.

## Preguntas de repaso

> [!question]- ¿Cómo se construye la lista de posibles raíces racionales?
> Se toman $p$ entre los divisores del coeficiente constante $a_0$ y $q$ entre los divisores del coeficiente principal $a_n$, y se forman todos los $p/q$ (con signo). Luego se evalúa cada candidato.

> [!question]- ¿Por qué $q \mid a_n$ y no solo $p \mid a_0$?
> Porque la raíz es $p/q$: al sustituir y multiplicar por $q^n$, aparece $q^n$ en el término principal, lo que obliga a que $q$ divida a $a_n$ (y a que $p$ divida a $a_0$).

> [!question]- ¿Qué pasa si ningún candidato es raíz?
> El polinomio no tiene raíces racionales (aunque puede tenerlas irracionales o complejas). El teorema no dice que existan raíces racionales, solo acota cuáles podrían ser.

> [!question]- Resuelva $2x^3 - 7x^2 + 2 = 0$.
> Las raíces son $-\tfrac12$, $2 + \sqrt{2}$ y $2 - \sqrt{2}$: una racional y dos irracionales.
