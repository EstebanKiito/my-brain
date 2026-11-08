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

En las pruebas se pide **nombrar cada ley** usada (caracterización de la diferencia, De Morgan, doble complemento, distributividad, absorción…): cada nombre suele valer puntaje.

## Demostrar con una hipótesis de contención

Muchas preguntas dicen "si $A \subseteq C$, entonces…". La hipótesis no se usa como una igualdad sino a través de alguno de estos hechos, todos fáciles de probar con elementos:

> [!tip] Cómo se usa $X \subseteq Y$
> - $X \cap Y = X$ y $X \cup Y = Y$.
> - $X - Y = \emptyset$, es decir, $X \cap Y^{c} = \emptyset$.
> - $Y^{c} \subseteq X^{c}$ (la contención se **invierte** al complementar).
> - $X \cap Z \subseteq Y \cap Z$ y $X \cup Z \subseteq Y \cup Z$ para cualquier $Z$ (monotonía).

**Ejemplo.** Si $A \subseteq C$, entonces $A - B = C - [B \cup (C - A)]$.

$$
\begin{aligned}
C - [B \cup (C - A)] &= C \cap [B^{c} \cap (C \cap A^{c})^{c}] && \text{(diferencia y De Morgan)} \\
&= C \cap [B^{c} \cap (C^{c} \cup A)] && \text{(De Morgan y doble complemento)} \\
&= B^{c} \cap [(C \cap C^{c}) \cup (C \cap A)] && \text{(asociatividad, conmutatividad, distributividad)} \\
&= B^{c} \cap A = A - B && (C \cap C^{c} = \emptyset \text{ y } C \cap A = A \text{ porque } A \subseteq C)
\end{aligned}
$$

## Demostrar una igualdad por doble inclusión

Cuando los conjuntos están definidos por una propiedad (y no como combinación de otros), el álgebra no sirve: se prueba $A \subseteq B$ y $B \subseteq A$ tomando un elemento arbitrario. Para mostrar que **no** son iguales basta un elemento que esté en uno y no en el otro.

**Ejemplo.** $\{n^2 \mid n \in \mathbb{N} \cup \{0\}\} = \{n^2 \mid n \in \mathbb{Z}\}$. La contención $\subseteq$ es inmediata. Para $\supseteq$: si $x = n^2$ con $n \in \mathbb{Z}$ y $n < 0$, entonces $x = (-n)^2$ con $-n \in \mathbb{N}$.

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

> [!question]- Si $A \subseteq B$, ¿qué relación hay entre $A^{c}$ y $B^{c}$?
> $B^{c} \subseteq A^{c}$: si $x \notin B$, entonces $x \notin A$ (contrarrecíproca de $x \in A \Rightarrow x \in B$).

> [!question]- Para probar $X^{c} = U$, ¿qué basta mostrar?
> Que $X = \emptyset$, porque $\emptyset^{c} = U$.
