---
ramo: "Matemáticas Discretas"
tema: "Inducción simple, fuerte y estructural"
tags:
  - discretas/induccion
  - origen/complemento
prerrequisitos:
  - "[[02 - Inducción simple y caso base distinto de cero]]"
---

# Inducción fuerte

A veces el caso $n$ no se deduce solo del caso $n-1$. En la sucesión de Fibonacci, $F(n) = F(n-1) + F(n-2)$ depende de **dos** anteriores. La **inducción fuerte** (o por curso de valores) permite suponer la propiedad para todos los valores menores a $n$.

## El principio

> [!tip] Principio de inducción por curso de valores (PICV)
> Sea $P$ una propiedad sobre $\mathbb{N}$. Si para todo $n \in \mathbb{N}$: ($P(k)$ es verdadera para todo $k < n$) $\Rightarrow P(n)$, entonces $P(n)$ vale para todo $n \in \mathbb{N}$.

En su versión con conjuntos: si $\{0, \dots, n-1\} \subseteq A \Rightarrow n \in A$ para todo $n$, entonces $A = \mathbb{N}$. La HI es "todos los anteriores cumplen $P$" y la tesis es "$n$ cumple $P$".

> [!warning] ¿Dónde está el caso base?
> No aparece escrito porque queda incluido en el paso: para $n = 0$ la hipótesis es vacía ($\{0, \dots, -1\} = \emptyset$) y hay que probar $P(0)$ sin ayuda. En la práctica, igual hay que **demostrar a mano los casos base**, y suele haber más de uno: tantos como "pasos hacia atrás" use el paso inductivo.

## Ejemplo: Fibonacci acotada por $2^n$

Con $F(0) = 0$, $F(1) = 1$ y $F(n) = F(n-1) + F(n-2)$ para $n \ge 2$, se prueba $F(n) \le 2^n$.

- **CB:** $F(0) = 0 \le 2^0$ y $F(1) = 1 \le 2^1$. Son **dos** casos base porque el paso usa dos términos previos.
- **HI:** $F(k) \le 2^k$ para todo $k < n$.
- **TI** ($n \ge 2$): $F(n) = F(n-1) + F(n-2) \le 2^{n-1} + 2^{n-2} \le 2^{n-1} + 2^{n-1} = 2^n$.

Con inducción simple no alcanza: para acotar $F(n)$ hacen falta $F(n-1)$ **y** $F(n-2)$, y la HI simple solo entrega $P(n-1)$.

## Ejemplo: todo $n \ge 2$ tiene un factor primo

Se prueba por inducción fuerte desde $n = 2$ (que es primo). Dado $n$:

- Si $n$ es primo, él mismo es su factor primo (este es un caso base disfrazado dentro del paso).
- Si no, $n = k_1 k_2$ con $1 < k_1, k_2 < n$. Por HI $k_1$ tiene un factor primo, y ese factor también divide a $n$.

Aquí el valor menor que se usa es un divisor cualquiera, no $n-1$: justo el caso típico donde la inducción simple no sirve.

## Simple frente a fuerte

| | Simple | Fuerte |
|---|---|---|
| Se asume | $P(n)$ | $P(k)$ para todo $k < n$ |
| Se prueba | $P(n+1)$ | $P(n)$ |
| Casos base | uno (el inicial) | los que necesite el paso |

Toda demostración por inducción simple se puede hacer con inducción fuerte (se usa solo la última hipótesis). El recíproco también es cierto, aunque requiere más trabajo (ver [[04 - Equivalencia entre buen orden e inducción]]).

## Preguntas de repaso

> [!question]- ¿Cuándo es necesaria la inducción fuerte en vez de la simple?
> Cuando el caso $n$ depende de valores anteriores que no son solo $n-1$: dos o más términos de una recurrencia, divisores, o mitades de un problema.

> [!question]- ¿Por qué Fibonacci necesita dos casos base?
> Porque $F(n)$ usa $F(n-1)$ y $F(n-2)$; para $n = 1$ el segundo término no existe, así que $F(0)$ y $F(1)$ deben verificarse a mano.

> [!question]- ¿Qué pasa si en la HI fuerte solo se verifican los casos base de $0$ y se olvida el $1$?
> El paso inductivo para $n = 2$ usa $F(1)$ y $F(0)$; si $F(1)$ no se probó, el argumento queda sin sustento para todo $n \ge 2$.
