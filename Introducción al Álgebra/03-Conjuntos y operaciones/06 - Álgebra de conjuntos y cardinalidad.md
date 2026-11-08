---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[05 - Diferencia, complemento y leyes de De Morgan]]"
---

# Álgebra de conjuntos y cardinalidad

Con las leyes de la unión, la intersección, la diferencia y el complemento se simplifican expresiones de conjuntos paso a paso, como se despeja en álgebra. La **cardinalidad** añade una dimensión numérica: cuenta cuántos elementos hay en cada conjunto.

## Simplificar con el álgebra de conjuntos

La técnica es reescribir diferencias como intersecciones con complementos y luego aplicar distributividad, De Morgan, idempotencia y las identidades con $\emptyset$ y $U$.

**Ejemplo.** Pruebe que $(A \cap B) \cup (A - B) = A$.

$$
(A \cap B) \cup (A - B) = (A \cap B) \cup (A \cap B^{c}) = A \cap (B \cup B^{c}) = A \cap U = A.
$$

**Ejemplo.** Pruebe que $(A - B) \cup B = A \cup B$.

$$
(A - B) \cup B = (A \cap B^{c}) \cup B = (A \cup B) \cap (B^{c} \cup B) = (A \cup B) \cap U = A \cup B.
$$

> [!tip] Álgebra de conjuntos
> Reescriba $A - B = A \cap B^{c}$, agrupe con distributividad, use $B \cup B^{c} = U$, $B \cap B^{c} = \emptyset$, y las identidades con $\emptyset$ y $U$. El objetivo es llegar a una expresión sin diferencias ni complementos anidados.

## Cardinalidad de uniones

Para conjuntos finitos, la cardinalidad de una unión no es la suma simple de cardinalidades: hay que restar lo que se cuenta dos veces.

> [!tip] Principio de inclusión-exclusión
> $n(\emptyset) = 0$, y para dos y tres conjuntos:
>
> $$n(A \cup B) = n(A) + n(B) - n(A \cap B),$$
> $$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C).$$

**Ejemplo.** Si $n(A) = 35$, $n(B) = 40$ y $n(A \cap B) = 8$, entonces $n(A \cup B) = 35 + 40 - 8 = 67$. Si además fueran disjuntos ($A \cap B = \emptyset$), sería $n(A \cup B) = 35 + 40 = 75$.

> [!warning] No sumar de más
> Al sumar $n(A) + n(B)$ los elementos de $A \cap B$ se cuentan dos veces, por eso se restan una vez. Con tres conjuntos hay que volver a sumar la triple intersección, que se restó de más.

## Preguntas de repaso

> [!question]- ¿Por qué en $n(A \cup B)$ se resta $n(A \cap B)$?
> Porque al sumar $n(A) + n(B)$ los elementos comunes se contaron dos veces; restar $n(A \cap B)$ deja cada elemento contado exactamente una vez.

> [!question]- Simplifique $(A \cup B) - A$.
> $(A \cup B) \cap A^{c} = (A \cap A^{c}) \cup (B \cap A^{c}) = \emptyset \cup (B - A) = B - A$.

> [!question]- Si $n(A) = 5$, $n(B) = 8$ y $n(A \cup B) = 11$, ¿cuánto vale $n(A \cap B)$?
> $11 = 5 + 8 - n(A \cap B)$, así que $n(A \cap B) = 13 - 11 = 2$.

> [!question]- En el principio de inclusión-exclusión con tres conjuntos, ¿por qué el último término se suma?
> Porque al restar las tres intersecciones dobles, la triple intersección se restó tres veces; al sumar $n(A \cap B \cap C)$ se compensa y queda contada una sola vez.
