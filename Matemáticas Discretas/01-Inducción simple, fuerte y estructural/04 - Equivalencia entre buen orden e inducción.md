---
ramo: "Matemáticas Discretas"
tema: "Inducción simple, fuerte y estructural"
tags:
  - discretas/induccion
  - origen/complemento
prerrequisitos:
  - "[[01 - Naturales, axiomas de Peano y principio del buen orden]]"
  - "[[03 - Inducción fuerte]]"
---

# Equivalencia entre buen orden e inducción

El principio del buen orden, la inducción simple y la inducción fuerte parecen tres herramientas distintas, pero son **equivalentes**: cualquiera de las tres implica las otras. Esto significa que no hay que "creer" en la inducción como un axioma extra, porque sale de cómo son los naturales.

> [!tip] Teorema
> Las siguientes afirmaciones son equivalentes: **(1)** Principio del buen orden, **(2)** Principio de inducción simple, **(3)** Principio de inducción fuerte.

Para probarlo basta un ciclo de implicaciones $1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1$.

## $1 \Rightarrow 2$: buen orden implica inducción simple

Se prueba por **contrarrecíproco**: se supone que el PIS es falso y se muestra que el PBO también.

1. Si el PIS falla, existe $A \subseteq \mathbb{N}$ con $0 \in A$ y ($n \in A \Rightarrow n+1 \in A$), pero $A \ne \mathbb{N}$.
2. Sea $B = \mathbb{N} \setminus A$. Entonces $B \subseteq \mathbb{N}$ y $B \neq \emptyset$.
3. Si $B$ tuviera un menor elemento $b$ (el PBO), entonces:
   - $b \ne 0$, porque $0 \in A$;
   - luego $b - 1 \in \mathbb{N}$, y como $b$ es el mínimo de $B$, $b - 1 \notin B$, es decir $b - 1 \in A$;
   - como $A$ cumple el paso inductivo, $b \in A$. Contradicción con $b \in B$.

Así $B$ es un subconjunto no vacío sin menor elemento, y el PBO falla.

## Las otras dos implicaciones

- **$2 \Rightarrow 3$** (simple implica fuerte): dado $A$ con la premisa fuerte, se define $B = \{n \mid \{0, \dots, n\} \subseteq A\}$ y se prueba con inducción simple que $B = \mathbb{N}$. En el caso base, $\{0, \dots, -1\} = \emptyset \subseteq A$ da $0 \in A$, luego $0 \in B$; si $n \in B$, la premisa fuerte da $n + 1 \in A$, o sea $n + 1 \in B$. Como $B = \mathbb{N}$, se deduce $A = \mathbb{N}$.
- **$3 \Rightarrow 1$** (fuerte implica buen orden): si un subconjunto no vacío $A$ no tuviera mínimo, la inducción fuerte aplicada a $\mathbb{N} \setminus A$ mostraría que $\mathbb{N} \setminus A = \mathbb{N}$, o sea $A = \emptyset$. Contradicción.

> [!warning] Método usado
> Aquí se emplea la demostración por contrarrecíproco: $p \Rightarrow q$ equivale a $\neg q \Rightarrow \neg p$. Es útil cuando es más fácil trabajar desde "el principio es falso".

## Preguntas de repaso

> [!question]- ¿Qué significa que tres principios sean equivalentes y qué ganamos con eso?
> Que cualquiera implica a los otros, así que se puede usar el más cómodo en cada demostración sin suponer nada nuevo.

> [!question]- En $1 \Rightarrow 2$, ¿para qué sirve el conjunto $B = \mathbb{N} \setminus A$?
> Reúne a los naturales donde falla la propiedad; si no está vacío, el PBO entrega su menor elemento, y de ahí sale la contradicción con el paso inductivo.

> [!question]- ¿Por qué en $1 \Rightarrow 2$ se descarta $b = 0$?
> Porque $0 \in A$ por el caso base, así que $0 \notin B$; si $b$ fuera $0$ no estaría en $B$.
