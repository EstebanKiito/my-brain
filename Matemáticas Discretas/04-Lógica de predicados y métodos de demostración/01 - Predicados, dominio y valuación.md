---
ramo: "Matemáticas Discretas"
tema: "Lógica de predicados y métodos de demostración"
tags:
  - discretas/logica
  - origen/complemento
prerrequisitos: []
---

# Predicados, dominio y valuación

La lógica proposicional trata enunciados completos como átomos indivisibles: no puede ver que «Sócrates es persona» y «Platón es persona» hablan de la misma propiedad aplicada a objetos distintos. Para razonar sobre «todas las personas son mortales» hacen falta tres ingredientes nuevos: **objetos** de un conjunto, **predicados** que hablan de ellos y **cuantificadores** («para todo», «existe»). Con ellos se construye la **lógica de predicados** (o de primer orden).

## Predicados: afirmaciones abiertas

Un **predicado** $P(x)$ es una afirmación con un hueco: su valor de verdad depende del objeto que se ponga en $x$. «$x$ es par» no es verdadera ni falsa mientras no se sepa quién es $x$; en cambio «$2$ es par» sí lo es. Evaluar el predicado en un objeto $a$ se llama **valuación** y se escribe $P(a)$; vale $1$ o $0$.

Con $P(x) := x$ es par, $R(x) := x$ es primo y $M(x) := x$ es mortal:

| Valuación | Valor |
|---|---|
| $P(2)$ | $1$ |
| $P(3)$ | $0$ |
| $R(7)$ | $1$ |
| $M(\text{Sócrates})$ | $1$ |
| $M(\text{Zeus})$ | $0$ |

## Predicados de varias variables

Un predicado **$n$-ario** $P(x_1, \dots, x_n)$ tiene $n$ huecos y se evalúa en $n$ objetos, en orden. Sirven para expresar relaciones: $O(x, y) := x \le y$, $S(x, y, z) := x + y = z$, $\text{Padre}(x, y) := x$ es padre de $y$.

- $O(2, 3) = 1$, porque $2 \le 3$.
- $S(5, 10, 15) = 1$ y $S(4, 12, 1) = 0$.
- $\text{Padre}(\text{Homero}, \text{Bart}) = 1$, pero el orden importa: $\text{Padre}(\text{Bart}, \text{Homero}) = 0$.

Un predicado **0-ario** no tiene huecos: es una proposición común, verdadera o falsa sin importar nada más.

## El dominio

> [!tip] Todo predicado vive en un dominio
> Un predicado sólo tiene sentido sobre un conjunto de objetos, su **dominio**. $x \le y$ puede evaluarse sobre $\mathbb{N}$, $\mathbb{Z}$ o $\mathbb{Q}$, y $x + y = z$ sobre $\mathbb{Q}$; «$x$ es padre de $y$» sólo sobre personas. El mismo símbolo puede ser verdadero en un dominio y falso en otro.

Las variables $x_1, \dots, x_n$ de un predicado se llaman **variables libres**: esperan que alguien les dé un valor. Más adelante los cuantificadores permiten «ligarlas».

> [!warning] Símbolo versus predicado
> Un símbolo como $\triangle$ o $\lhd$ no significa nada por sí solo. Recién cuando se fija un dominio y se interpreta (por ejemplo, $\triangle$ como «es subcadena de» o $\lhd$ como suma de naturales) se obtienen valores de verdad. La nota sobre [[03 - Interpretaciones y satisfacción de fórmulas|interpretaciones]] formaliza esta idea.

## Predicados compuestos

Los predicados se combinan con los conectivos $\neg, \wedge, \vee, \to, \leftrightarrow$ igual que las proposiciones, siempre sobre el mismo dominio. La valuación se calcula recursivamente. Sobre $\mathbb{N}$, con $P(x) := x$ es par y $O(x, y) := x \le y$:

- $P'(x) := \neg P(x)$ cumple $P'(4) = 0$.
- $O'(x, y, z) := O(x, y) \wedge O(y, z)$ dice «$y$ está entre $x$ y $z$»; $O'(1, 2, 3) = 1$ y $O'(1, 3, 2) = 0$.
- $P''(x, y) := (P(x) \wedge P(y)) \to O(x, y)$ dice «si ambos son pares, el primero no supera al segundo»; $P''(4, 2) = 0$ y $P''(4, 3) = 1$ (el antecedente es falso).

## Preguntas de repaso

> [!question]- ¿Por qué «$x$ es par» no es una proposición pero «$2$ es par» sí?
> Una proposición tiene un valor de verdad definido. «$x$ es par» depende del valor de $x$, es una afirmación abierta; al reemplazar $x$ por $2$ (valuación) el hueco se llena y el enunciado pasa a ser verdadero.

> [!question]- ¿Es lo mismo $O(2, 3)$ que $O(3, 2)$ para $O(x, y) := x \le y$?
> No. Los argumentos se asignan por posición: $O(2, 3) = 1$ pero $O(3, 2) = 0$. El orden de los argumentos es parte de la definición del predicado.

> [!question]- ¿Qué cambia si se evalúa el mismo predicado en otro dominio?
> Puede cambiar el valor de verdad. Por ejemplo, «existe $z$ con $x + z = y$» no es siempre cierto sobre $\mathbb{N}$ (con $x = 5$, $y = 3$), pero sí sobre $\mathbb{Z}$. Por eso todo predicado va acompañado de su dominio.
