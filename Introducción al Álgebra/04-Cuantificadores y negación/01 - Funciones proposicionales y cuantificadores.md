---
ramo: "Introducción al Álgebra"
tema: "Cuantificadores y negación"
tags:
  - intro-algebra/cuantificadores
  - origen/complemento
prerrequisitos:
  - "[[01 - Proposiciones y valores de verdad]]"
---

# Funciones proposicionales y cuantificadores

Una frase como "$x - 5 \le 0$" no es proposición mientras no se sepa $x$. Para convertirla en una, o se da un valor a $x$, o se **cuantifica** $x$: se dice si la propiedad vale para todos o para alguno. Los cuantificadores son la herramienta para afirmar sobre conjuntos enteros.

## Funciones proposicionales

Una **función proposicional** (o predicado) $p(x)$ es una expresión que depende de una variable $x$: al reemplazar $x$ por un elemento del conjunto de referencia $U$, se obtiene una proposición.

**Ejemplos.** $p(x) \iff x - 5 \le 0$ en $\mathbb{Z}$: $p(3)$ es verdadera y $p(7)$ es falsa. También puede haber varias variables: $p(x, y) \iff x + y + 1 = 0$ en $\mathbb{R}$, con $p(-2, 1)$ verdadera y $p(1, 1)$ falsa.

## Los cuantificadores

Dada $p(x)$ con dominio $U$, sea $A = \{x \in U \mid p(x)\}$ el conjunto de valores donde $p$ es verdadera. Los cuantificadores se definen por lo que le piden a $A$:

$$
(\forall x \in U)\ p(x) \iff A = U, \qquad
(\exists x \in U)\ p(x) \iff A \neq \emptyset, \qquad
(\exists!\, x \in U)\ p(x) \iff A = \{u\}.
$$

> [!tip] Cuantificadores
> $(\forall x \in U)\,p(x)$: $p$ vale para **todo** $x$ de $U$ (equivale a $A = U$).
> $(\exists x \in U)\,p(x)$: $p$ vale para **al menos un** $x$ de $U$ (equivale a $A \neq \emptyset$).
> $(\exists!\, x \in U)\,p(x)$: $p$ vale para **exactamente un** $x$ (equivale a $A$ con un solo elemento).

**Ejemplo.** Con $U = \mathbb{N}$ y $p(n) \iff n \text{ es par}$, el conjunto $A$ es el de los pares. Entonces $(\forall n \in \mathbb{N})\,p(n)$ es falsa, $(\exists n \in \mathbb{N})\,p(n)$ es verdadera y $(\exists!\, n \in \mathbb{N})\,p(n)$ es falsa (hay más de un par).

> [!warning] El dominio importa
> El valor de verdad de una proposición cuantificada depende del universo. $(\forall x)(x^2 > 0)$ es falsa en $\mathbb{R}$ (por $x = 0$), pero verdadera en $\mathbb{R}\setminus\{0\}$.

## Preguntas de repaso

> [!question]- ¿Qué convierte a una función proposicional en una proposición?
> Reemplazar la variable por un valor concreto del dominio, o bien cuantificarla ($\forall$, $\exists$ o $\exists!$). Ambas cosas fijan un valor de verdad.

> [!question]- Dé un ejemplo de función proposicional de dos variables.
> $p(x, y) \iff x + y + 1 = 0$ en $\mathbb{R}$. Se vuelve proposición al dar valores: $p(-2, 1)$ es V y $p(1, 1)$ es F.

> [!question]- ¿Cuándo es falsa $(\forall x \in U)\,p(x)$?
> Cuando hay al menos un $x \in U$ con $p(x)$ falsa, es decir, cuando $A \neq U$. Basta un contraejemplo.

> [!question]- ¿Qué significa $(\exists!\, x \in U)\,p(x)$?
> Que existe exactamente un $x$ en $U$ que cumple $p$: el conjunto $A = \{x \in U \mid p(x)\}$ tiene un solo elemento.
