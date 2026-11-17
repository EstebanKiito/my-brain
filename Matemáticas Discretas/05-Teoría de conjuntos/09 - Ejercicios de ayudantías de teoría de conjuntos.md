---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Leyes de la teoría de conjuntos y demostración por doble inclusión]]"
  - "[[06 - Uniones e intersecciones generalizadas]]"
  - "[[07 - Pares ordenados y producto cartesiano]]"
---

# Ejercicios de ayudantías de teoría de conjuntos

Cinco ejercicios de ayudantía: dos sobre producto cartesiano, uno sobre diferencia simétrica y dos sobre una familia $T(A)$ de subconjuntos con complemento finito, que ejercita uniones e intersecciones generalizadas. Todos se resuelven por doble inclusión tomando elementos arbitrarios.

## Ejercicios

### 1. Producto cartesiano conmutativo
Sean $A, B$ conjuntos no vacíos. Demuestre que $A \times B = B \times A$ si y solo si $A = B$.

> [!example]- Solución
> ($\Leftarrow$) Si $A = B$, entonces $A \times B = A \times A = B \times A$.
>
> ($\Rightarrow$) Se prueba $A \subseteq B$; la otra inclusión es simétrica. Sea $a \in A$. Como $B \neq \varnothing$, existe $b \in B$, y $(a, b) \in A \times B = B \times A$. Por definición de producto, la primera coordenada de un par de $B \times A$ está en $B$, luego $a \in B$.
>
> La hipótesis de **no vacío** es necesaria: con $A = \{1\}$ y $B = \varnothing$ ambos productos son vacíos, pero $A \neq B$.

### 2. Producto y diferencia
Sean $A, B, C$ no vacíos. Demuestre o refute: $A \times (B \setminus C) = (A \times B) \setminus (A \times C)$.

> [!example]- Solución
> Es **verdadera**; se prueba por doble inclusión.
>
> ($\subseteq$) Si $(x, y) \in A \times (B \setminus C)$, entonces $x \in A$, $y \in B$ e $y \notin C$. Así $(x, y) \in A \times B$ y $(x, y) \notin A \times C$ (porque $y \notin C$).
>
> ($\supseteq$) Si $(x, y) \in (A \times B) \setminus (A \times C)$, entonces $x \in A$, $y \in B$ y $(x,y) \notin A \times C$. Como $x \in A$, la única forma de que $(x, y) \notin A \times C$ es $y \notin C$. Luego $y \in B \setminus C$ y $(x, y) \in A \times (B \setminus C)$.

### 3. Diferencia simétrica
Se define $A \triangle B = (A \setminus B) \cup (B \setminus A)$. Demuestre que si $A \triangle C = B \triangle C$, entonces $A = B$.

> [!example]- Solución
> Se prueba $A \subseteq B$ (la otra es análoga). Sea $x \in A$ y se separan dos casos.
>
> - **$x \notin C$:** entonces $x \in A \setminus C \subseteq A \triangle C = B \triangle C$. Como $x \notin C$, no puede estar en $C \setminus B$, así que está en $B \setminus C$ y por tanto $x \in B$.
> - **$x \in C$:** entonces $x$ no está en $A \setminus C$ ni en $C \setminus A$, es decir, $x \notin A \triangle C$. Como $A \triangle C = B \triangle C$, tampoco está en $B \triangle C$, y en particular $x \notin C \setminus B$. Como $x \in C$, la única posibilidad es $x \in B$.
>
> Esto es una "ley de cancelación": $\triangle$ se comporta como una suma que se puede cancelar. Se comprobó, sobre todos los subconjuntos de $\{0,1,2\}$, que vale incluso sin pedir que los conjuntos sean no vacíos. Ejemplo: $A = \{1,2\}$, $B = \{2,3\}$, $C = \{2\}$ dan $A \triangle C = \{1\} \neq \{3\} = B \triangle C$, consistente con $A \neq B$.

### 4. La familia $T(A)$: vacío, total y unión
Dado un conjunto $A$, sea $T(A) = \{X \in \mathcal{P}(A) \mid X = \varnothing \vee A \setminus X \text{ es finito}\}$. Demuestre que (a) $\varnothing \in T(A)$, (b) $A \in T(A)$ y (c) $\bigcup T(A) \in T(A)$.

> [!example]- Solución
> **(a)** $\varnothing \subseteq A$, luego $\varnothing \in \mathcal{P}(A)$, y cumple la condición "$X = \varnothing$".
>
> **(b)** $A \in \mathcal{P}(A)$ y $A \setminus A = \varnothing$ es finito.
>
> **(c)** Sea $V = \bigcup T(A)$. Como cada elemento de $T(A)$ es subconjunto de $A$, $V \subseteq A$ y $V \in \mathcal{P}(A)$. Si todos los elementos de $T(A)$ son vacíos, $V = \varnothing \in T(A)$. Si no, existe $X \in T(A)$ no vacío, con $A \setminus X$ finito. Como $X \subseteq V$, $A \setminus V \subseteq A \setminus X$, así que $A \setminus V$ es finito y $V \in T(A)$.

### 5. La familia $T(A)$: intersecciones finitas
Con $T(A)$ como en el ejercicio 4, demuestre que si $\mathcal{X} \subseteq T(A)$ es finito y no vacío, entonces $\bigcap \mathcal{X} \in T(A)$.

> [!example]- Solución
> Sea $\mathcal{X} = \{B_1, \dots, B_n\}$ con $n \ge 1$. Como $\bigcap \mathcal{X} \subseteq B_1 \subseteq A$, pertenece a $\mathcal{P}(A)$. Si algún $B_i = \varnothing$, la intersección es $\varnothing \in T(A)$. Si todos son no vacíos, cada $A \setminus B_i$ es finito, y por De Morgan
> $$A \setminus (B_1 \cap \dots \cap B_n) = (A \setminus B_1) \cup \dots \cup (A \setminus B_n).$$
> Es una unión **finita** de conjuntos finitos, luego finita. Por tanto $\bigcap \mathcal{X} \in T(A)$.
>
> Esta familia es cerrada bajo uniones arbitrarias (ejercicio 4) e intersecciones finitas, y contiene a $\varnothing$ y a $A$: es el patrón de una topología.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 1 se exige que $B$ no sea vacío?
> Para poder elegir un $b \in B$ y formar el par $(a, b)$ que traslada la pertenencia de $a$ de $A$ a $B$; sin eso, ambos productos son vacíos aunque $A \neq B$.

> [!question]- ¿Qué técnica se repite en los ejercicios 1 a 3?
> Doble inclusión con un elemento arbitrario (o un par arbitrario $(x, y)$) y, cuando hay una diferencia, separación en casos según pertenezca o no a un conjunto auxiliar.

> [!question]- ¿Por qué en el ejercicio 5 la unión finita preserva la finitud pero no una unión infinita?
> La unión finita de conjuntos finitos es finita, mientras que una unión infinita de conjuntos finitos puede ser infinita (por ejemplo, $\bigcup_{n} \{n\} = \mathbb{N}$).
