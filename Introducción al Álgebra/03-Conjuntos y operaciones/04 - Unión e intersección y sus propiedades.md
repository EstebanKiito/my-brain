---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[02 - Igualdad, conjunto vacío y universo]]"
  - "[[02 - Negación, conjunción y disyunción]]"
---

# Unión e intersección y sus propiedades

A partir de conjuntos conocidos se obtienen nuevos conjuntos con operaciones. Las dos fundamentales, **unión** e **intersección**, se definen con los conectivos lógicos: la unión junta con "o" y la intersección selecciona con "y".

## Unión e intersección

Para $A, B \subseteq U$:

$$
A \cup B = \{x \in U \mid (x \in A) \vee (x \in B)\}, \qquad
A \cap B = \{x \in U \mid (x \in A) \wedge (x \in B)\}.
$$

La unión reúne todo lo que está en al menos uno; la intersección, solo lo que está en ambos.

> [!tip] Unión e intersección
> $A \cup B$: elementos en $A$ **o** en $B$ (o en ambos). $A \cap B$: elementos en $A$ **y** en $B$. Son las traducciones de $\vee$ y $\wedge$ al lenguaje de conjuntos.

## Monotonía de la contención

Si $X \subseteq Y$ y $W \subseteq Z$, entonces la unión y la intersección respetan la contención:

$$
X \cap W \subseteq Y \cap Z, \qquad X \cup W \subseteq Y \cup Z.
$$

En particular, $(A \cap B) \subseteq A \subseteq (A \cup B)$: la intersección "recorta" y la unión "agranda". Además, si $A \subseteq B$ y $A \subseteq C$ entonces $A \subseteq B \cap C$; y si $A \subseteq B$ y $C \subseteq B$ entonces $A \cup C \subseteq B$.

## Propiedades algebraicas

La unión y la intersección cumplen leyes análogas a las de la lógica:

| Propiedad | Igualdades |
|---|---|
| Idempotencia | $A \cap A = A$, $A \cup A = A$ |
| Identidad | $A \cup \emptyset = A$, $A \cap \emptyset = \emptyset$ |
| Dominancia | $A \cup U = U$, $A \cap U = A$ |
| Conmutatividad | $A \cup B = B \cup A$, $A \cap B = B \cap A$ |
| Asociatividad | $A \cup (B \cup C) = (A \cup B) \cup C$, $A \cap (B \cap C) = (A \cap B) \cap C$ |
| Distributividad | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$, $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |

Son el "álgebra" que permite simplificar expresiones de conjuntos, como se ve en los temas siguientes.

## Preguntas de repaso

> [!question]- ¿Qué elementos hay en $A \cup B$ y en $A \cap B$?
> En $A \cup B$ están los de $A$, los de $B$ y los de ambos (el "o" inclusivo). En $A \cap B$ solo los que están en $A$ y en $B$ a la vez.

> [!question]- Si $A = \{1, 2, 3\}$ y $B = \{3, 4\}$, calcule $A \cup B$ y $A \cap B$.
> $A \cup B = \{1, 2, 3, 4\}$ y $A \cap B = \{3\}$.

> [!question]- ¿Por qué $(A \cap B) \subseteq A$?
> Todo elemento de $A \cap B$ está, por definición, en $A$ (y en $B$). En particular está en $A$, luego $A \cap B \subseteq A$.

> [!question]- Simplifique $A \cap U$ y $A \cup \emptyset$.
> $A \cap U = A$ (identidad) y $A \cup \emptyset = A$ (identidad). El universo no recorta y el vacío no agrega.
