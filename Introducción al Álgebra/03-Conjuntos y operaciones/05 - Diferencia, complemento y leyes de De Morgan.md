---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[04 - Unión e intersección y sus propiedades]]"
---

# Diferencia, complemento y leyes de De Morgan

Para "quitar" elementos de un conjunto se usa la **diferencia**, y para hablar de todo lo que queda fuera de un conjunto se usa el **complemento**. Ambas se reducen a la intersección, lo que permite aplicarles las leyes lógicas.

## Diferencia y complemento

La **diferencia** $A - B$ (o $A \setminus B$) es el conjunto de elementos que están en $A$ pero no en $B$:

$$
A - B = \{x \in A \mid x \notin B\}.
$$

El **complemento** de $A$ es todo lo que está fuera de $A$ dentro del universo:

$$
A^{c} = \{x \in U \mid x \notin A\} = U - A.
$$

> [!tip] Diferencia como intersección
> $A - B = A \cap B^{c}$ y $A^{c} = U - A$. Toda diferencia se puede reescribir como una intersección con un complemento, que es la llave para simplificar.

## Leyes de De Morgan y propiedades del complemento

Para conjuntos arbitrarios $A, B \subseteq U$:

1. **De Morgan:** $(A \cup B)^{c} = A^{c} \cap B^{c}$ y $(A \cap B)^{c} = A^{c} \cup B^{c}$.
2. **Doble complemento:** $(A^{c})^{c} = A$.
3. $A \cap A^{c} = \emptyset$ y $A \cup A^{c} = U$.

**Demostración de una ley de De Morgan.** Sea $x \in U$ arbitrario:

$$
x \in (A \cup B)^{c} \iff x \notin (A \cup B) \iff \neg(x \in A \vee x \in B) \iff x \notin A \wedge x \notin B \iff x \in A^{c} \wedge x \in B^{c} \iff x \in A^{c} \cap B^{c}.
$$

Como $x$ es arbitrario, $(A \cup B)^{c} = A^{c} \cap B^{c}$.

> [!warning] De Morgan cambia el conectivo
> Al complementar una unión se obtiene una intersección (y viceversa): $(A \cup B)^{c} = A^{c} \cap B^{c}$, no $A^{c} \cup B^{c}$. Es el mismo error que negar un "o" y dejar el "o".

## Simplificar con diferencia y complemento

**Ejemplo.** Pruebe que $(A \cup B) - B = A - B$.

$$
(A \cup B) - B = (A \cup B) \cap B^{c} = (A \cap B^{c}) \cup (B \cap B^{c}) = (A \cap B^{c}) \cup \emptyset = A \cap B^{c} = A - B.
$$

**Ejemplo.** Simplifique $(A \cap U)^{c} \cap (A - B)$.

$$
(A \cap U)^{c} \cap (A - B) = A^{c} \cap (A \cap B^{c}) = (A^{c} \cap A) \cap B^{c} = \emptyset \cap B^{c} = \emptyset.
$$

## Preguntas de repaso

> [!question]- Escriba $A - B$ usando intersección y complemento.
> $A - B = A \cap B^{c}$: los elementos de $A$ que no están en $B$.

> [!question]- ¿Qué es $(A^{c})^{c}$ y $A \cup A^{c}$?
> $(A^{c})^{c} = A$ (doble complemento) y $A \cup A^{c} = U$ (un conjunto y su complemento cubren todo el universo).

> [!question]- Simplifique $(A \cap B) - (A \cap C)$.
> $(A \cap B) \cap (A \cap C)^{c} = (A \cap B) \cap (A^{c} \cup C^{c}) = (A \cap B \cap A^{c}) \cup (A \cap B \cap C^{c}) = \emptyset \cup (A \cap B \cap C^{c}) = A \cap (B - C)$.

> [!question]- ¿Por qué $A \cap A^{c} = \emptyset$?
> Porque ningún elemento puede estar en $A$ y fuera de $A$ a la vez. Es la versión conjuntista de la contradicción $p \wedge \neg p \equiv F$.
