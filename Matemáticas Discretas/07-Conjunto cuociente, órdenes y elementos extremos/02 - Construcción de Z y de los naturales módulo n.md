---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Conjunto cuociente y particiones]]"
---

# Construcción de Z y de los naturales módulo n

La aplicación más importante de los cuocientes es **fabricar conjuntos nuevos**: se toma un conjunto conocido, se calcula su cuociente por una equivalencia, se nombran las clases y se definen operaciones sobre ellas usando las del conjunto original. Así se obtienen los naturales módulo $n$ y también los enteros a partir de los naturales.

## Naturales módulo n

Con $\equiv_4$ sobre $\mathbb{N}$, el conjunto $\mathbb{N}_4 = \mathbb{N}/{\equiv_4} = \{[0],[1],[2],[3]\}$ se dota de operaciones que trabajan con representantes:

$$[i] +_4 [j] = [i+j], \qquad [i] \cdot_4 [j] = [i \cdot j].$$

Por ejemplo, $[3] +_4 [2] = [5] = [1]$, $[1] +_4 [3] = [4] = [0]$ y $[2] \cdot_4 [3] = [6] = [2]$. Si se renombra $[k]$ como $k$, queda $\mathbb{N}_4 = \{0,1,2,3\}$ con $+$ y $\cdot$ "con reloj de cuatro horas":

| $+$ | 0 | 1 | 2 | 3 | | $\cdot$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 1 | 2 | 3 | | **0** | 0 | 0 | 0 | 0 |
| **1** | 1 | 2 | 3 | 0 | | **1** | 0 | 1 | 2 | 3 |
| **2** | 2 | 3 | 0 | 1 | | **2** | 0 | 2 | 0 | 2 |
| **3** | 3 | 0 | 1 | 2 | | **3** | 0 | 3 | 2 | 1 |

> [!warning] La operación no debe depender del representante
> $[i+j]$ debe dar la misma clase aunque se cambie $i$ por otro elemento de $[i]$. Con $+_4$ y $\cdot_4$ esto se cumple; si se definiera una operación que mirara el representante (por ejemplo "$[i]$ elevado a $i$"), el resultado no estaría bien definido.

## Los enteros como cuociente de pares

Los naturales no tienen resta, pero un par $(m,n)$ puede leerse como "la diferencia $m-n$". Dos pares representan el mismo número si tienen la misma diferencia, lo que se escribe sin restar:

$$(m,n) \mathrel{\downarrow} (r,s) \iff m + s = n + r.$$

Es de equivalencia: refleja ($m+n = n+m$), simétrica (se intercambian los lados) y transitiva (de $m+s = n+r$ y $r+u = s+t$ se obtiene $m+u = n+t$). Sus clases son las **diagonales** de $\mathbb{N}\times\mathbb{N}$.

![Cuadrícula de pares de naturales](adjuntos/Pares%20de%20naturales%20coloreados%20por%20diagonales.png)

> [!example]- Transcripción de la imagen
> Una cuadrícula de pares $(a,b)$ con $a$ hacia la derecha y $b$ hacia arriba, cuyas filas inferiores muestran $(0,0),(1,0),(2,0),\dots$. Cada diagonal que sube hacia la derecha tiene un solo tono: la diagonal principal $(0,0),(1,1),(2,2),\dots$ aparece marcada con borde, y las diagonales vecinas en tonos más oscuros o claros.

![Diagonales como clases de equivalencia](adjuntos/Partición%20de%20N%20por%20N%20inducida%20por%20la%20relación%20de%20pares.png)

> [!example]- Transcripción de la imagen
> Los puntos de $\mathbb{N}\times\mathbb{N}$ con círculos alargados sobre cada diagonal. A la derecha están las clases $[(0,0)]$, $[(0,1)]$, $[(0,2)]$, $\dots$ (diagonales sobre la principal) y arriba las clases $[(1,0)]$, $[(2,0)]$, $[(3,0)]$, $\dots$ (diagonales bajo la principal).

Se define $\mathbb{Z} = \mathbb{N}^2/{\downarrow}$ y se nombran las clases: $[(0,0)] = 0$, $[(0,i)] = i$ y $[(i,0)] = -i$. El signo "$-$" no significa nada por sí solo: es sólo el nombre de la clase $[(i,0)]$.

## Operaciones sobre los enteros

La suma suma coordenadas y el producto imita $(m-n)(r-s) = (mr + ns) - (ms + nr)$:

$$[(m,n)] + [(r,s)] = [(m+r,\,n+s)], \qquad [(m,n)] \cdot [(r,s)] = [(ms + nr,\; mr + ns)].$$

Ejemplos, con el par $(0,i)$ para $i$ y $(i,0)$ para $-i$:
- $7 + (-5) = [(0,7)] + [(5,0)] = [(5,7)] = [(0,2)] = 2$.
- $-18 + 4 = [(18,0)] + [(0,4)] = [(18,4)] = [(14,0)] = -14$.
- $-3 + (-6) = [(9,0)] = -9$.
- $(-3)\cdot(-4) = [(3,0)]\cdot[(4,0)] = [(0,\,12)] = 12$ y $3 \cdot 3 = [(0,9)] = 9$.

## Preguntas de repaso

> [!question]- ¿Por qué $(2,5)$ y $(7,10)$ son el mismo entero?
> Porque $2 + 10 = 5 + 7$: ambos pares tienen la misma diferencia ($-3$), están en la misma diagonal y forman la clase $[(3,0)]$, el entero $-3$.

> [!question]- ¿Cuál es el índice de $\downarrow$ y por qué?
> Es infinito: hay una clase por cada entero (una diagonal por valor de $m-n$).

> [!question]- ¿Qué pasa con $[2] \cdot_4 [2]$ y por qué es llamativo?
> Es $[4] = [0]$: el producto de dos clases no nulas puede ser nulo, algo que no ocurre en $\mathbb{Z}$.

> [!question]- ¿Por qué hay que comprobar que $[i] +_4 [j] = [i+j]$ no depende de los representantes?
> Porque una clase tiene infinitos representantes y la operación debe dar siempre la misma clase; si no, no sería una función sobre el cuociente.
