---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - intro-algebra/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[06 - Álgebra de conjuntos y cardinalidad]]"
---

# Ejercicios de prueba de conjuntos

Preguntas de interrogaciones anteriores. Hay cuatro tipos que se repiten: operar con conjuntos concretos (con diagrama de Venn), probar una igualdad con álgebra de conjuntos **nombrando cada ley**, probar algo bajo una hipótesis de contención, y decidir si dos conjuntos definidos por una propiedad son iguales.

## Ejercicios

### 1. Conjuntos concretos y diagrama de Venn
Sea $U = \{r, e, m, o, l, i, n, a\}$, $A = \{m, o, n, a\}$, $B = \{r, e, m, o\}$ y $C = \{l, i, m, o, n\}$. (a) Ubique los elementos en un diagrama de Venn. (b) Describa por extensión $(A^{c} - B)^{c} - C$. (c) Exprese $\{a, r, e, n\}$ como operación entre $A$, $B$ y $C$.

> [!example]- Solución
> (a)
> ![Diagrama de Venn con los elementos de U repartidos](adjuntos/Diagrama%20de%20Venn%20con%20los%20elementos%20de%20U%20repartidos.png)
>
> > [!example]- Transcripción de la figura
> > Rectángulo $U$ con tres círculos: $A$ abajo a la izquierda, $B$ abajo a la derecha y $C$ arriba. En la zona común de los tres están $m$ y $o$; en $A \cap C$ fuera de $B$ está $n$; solo en $A$ está $a$; solo en $C$ están $l$ e $i$; solo en $B$ están $r$ y $e$. Las zonas $A \cap B$ fuera de $C$, $B \cap C$ fuera de $A$ y el exterior de los círculos quedan vacías.
>
> (b) Primero se simplifica: $(A^{c} - B)^{c} = (A^{c} \cap B^{c})^{c} = A \cup B$ (diferencia, De Morgan, doble complemento). Luego $(A \cup B) - C = \{m, o, n, a, r, e\} \cap \{r, e, a\} = \{r, e, a\}$.
> (c) $B - A = \{r, e\}$ y $A - B = \{n, a\}$, así que $\{a, r, e, n\} = (A - B) \cup (B - A) = A \,\Delta\, B$. Hay otras respuestas válidas, como $(A \cup B) - (A \cap B)$.

### 2. Igualdad nombrando las leyes
Demuestre que $[A - (B - A^{c})]^{c} \cap A^{c} = A^{c}$.

> [!example]- Solución
> $$\begin{aligned}
> [A - (B - A^{c})]^{c} \cap A^{c} &= [A \cap (B \cap A)^{c}]^{c} \cap A^{c} && \text{(diferencia dos veces, doble complemento)} \\
> &= [A^{c} \cup (B \cap A)] \cap A^{c} && \text{(De Morgan y doble complemento)} \\
> &= A^{c} && \text{(absorción: } (A^{c} \cup X) \cap A^{c} = A^{c})
> \end{aligned}$$

### 3. Tres identidades encadenadas
Pruebe: (a) $(A \cap B) - C = B - (A^{c} \cup C) = B \cap (A - C)$. (b) $(A \cup B) - C = (A - C) \cup (B - C)$. (c) Si $A \cap B \subseteq C$, entonces $[B \cap (A - C)]^{c} = U$.

> [!example]- Solución
> (a) $(A \cap B) - C = (A \cap B) \cap C^{c} = B \cap (A \cap C^{c})$ por conmutatividad y asociatividad. Eso ya es $B \cap (A - C)$. Además $A \cap C^{c} = (A^{c} \cup C)^{c}$ por De Morgan y doble complemento, así que también es $B \cap (A^{c} \cup C)^{c} = B - (A^{c} \cup C)$.
> (b) $(A \cup B) \cap C^{c} = (A \cap C^{c}) \cup (B \cap C^{c})$ por distributividad.
> (c) Basta probar que $B \cap (A - C) = \emptyset$. Por (a), es $(A \cap B) \cap C^{c}$, y por la hipótesis y monotonía, $(A \cap B) \cap C^{c} \subseteq C \cap C^{c} = \emptyset$.

### 4. Contención y complemento
Demuestre: (a) $A \subseteq B \iff B^{c} \subseteq A^{c}$. (b) $(B - A) \subseteq C \iff C^{c} \subseteq B^{c} \cup A$.

> [!example]- Solución
> (a) $A \subseteq B$ significa $x \in A \Rightarrow x \in B$ para todo $x$, que por contrarrecíproca equivale a $x \notin B \Rightarrow x \notin A$, es decir, $x \in B^{c} \Rightarrow x \in A^{c}$: $B^{c} \subseteq A^{c}$.
> (b) Por (a), $(B - A) \subseteq C \iff C^{c} \subseteq (B - A)^{c}$, y $(B - A)^{c} = (B \cap A^{c})^{c} = B^{c} \cup A$.

### 5. Usar la hipótesis dentro de una cadena
Demuestre que si $(B - A) \subseteq C$, entonces $(D - C) \subseteq (D - B) \cup A$.

> [!example]- Solución
> Por el ejercicio 4, la hipótesis da $C^{c} \subseteq A \cup B^{c}$. Entonces
> $$D - C = D \cap C^{c} \subseteq D \cap (A \cup B^{c}) = (D \cap A) \cup (D \cap B^{c}) \subseteq A \cup (D - B),$$
> usando monotonía, distributividad y $D \cap A \subseteq A$. Ojo: hay pasos con $\subseteq$, no todos son $=$.

### 6. La diferencia simétrica es asociativa
Con $A \,\Delta\, B = (A - B) \cup (B - A)$, demuestre que $(A \,\Delta\, B) \,\Delta\, C = A \,\Delta\, (B \,\Delta\, C)$.

> [!example]- Solución
> Primero, $(A \,\Delta\, B)^{c} = (A \cap B^{c})^{c} \cap (A^{c} \cap B)^{c} = (A^{c} \cup B) \cap (A \cup B^{c}) = (A^{c} \cap B^{c}) \cup (A \cap B)$ (De Morgan, distributividad, se eliminan $A^{c} \cap A$ y $B \cap B^{c}$). Entonces
> $$(A \,\Delta\, B) \,\Delta\, C = [(A \,\Delta\, B) \cap C^{c}] \cup [(A \,\Delta\, B)^{c} \cap C],$$
> y al distribuir queda
> $$(A \cap B^{c} \cap C^{c}) \cup (A^{c} \cap B \cap C^{c}) \cup (A^{c} \cap B^{c} \cap C) \cup (A \cap B \cap C).$$
> Esta expresión es **simétrica** en $A, B, C$: son los elementos que están en exactamente uno o en los tres (un número impar). Haciendo el mismo cálculo con $(B \,\Delta\, C) \,\Delta\, A = A \,\Delta\, (B \,\Delta\, C)$ se obtiene la misma unión, así que son iguales. El diagrama de Venn ayuda a verlo, pero la pauta exige la demostración.

### 7. ¿Son iguales?
Decida si $A = B$: (a) $A = \{x \in \mathbb{R} \mid |x + 1| \ge 2\}$, $B = \{x \in \mathbb{R} \mid \lvert |x| + 1 \rvert \ge 2\}$. (b) $A = \{\frac{p}{q} \mid p, q \in \mathbb{Z},\ q \neq 0\}$, $B = \{\frac{p}{q} \mid p \in \mathbb{N} \cup \{0\},\ q \in \mathbb{Z} - \{0\}\}$. (c) $A = \{x \in \mathbb{R} \mid x^2 + 2 = 0\}$, $B = \{x \in \mathbb{Q} \mid x^2 - 2 = 0\}$.

> [!example]- Solución
> (a) No: $-1 \in B$ porque $|-1| + 1 = 2$, pero $-1 \notin A$ porque $|0| = 0 < 2$. Un elemento basta.
> (b) Sí. $B \subseteq A$ es inmediato. Para $A \subseteq B$: si $p < 0$, se reescribe $\frac{p}{q} = \frac{-p}{-q}$ con $-p \in \mathbb{N}$ y $-q \neq 0$.
> (c) Sí, ambos son vacíos: $x^2 = -2$ no tiene solución real y $\pm\sqrt 2$ no son racionales.

### 8. Un conjunto definido por casos
Sean $A, B \subseteq U$ fijos con $A \neq \emptyset$. Para $X \subseteq U$ se define $C(X) = X - B$ si $A \cap X \neq \emptyset$, y $C(X) = X \cup B$ si $A \cap X = \emptyset$. Pruebe: (a) $C(A) = A - B$; (b) $C(A^{c}) = (C(A))^{c}$; (c) $C(A) \cup C(B) \subseteq A \cup B$.

> [!example]- Solución
> (a) $A \cap A = A \neq \emptyset$, así que $C(A) = A - B$.
> (b) $A \cap A^{c} = \emptyset$, así que $C(A^{c}) = A^{c} \cup B$; y $(C(A))^{c} = (A \cap B^{c})^{c} = A^{c} \cup B$.
> (c) Por casos según $A \cap B$. Si $A \cap B \neq \emptyset$: $C(B) = B - B = \emptyset$ y $C(A) \cup C(B) = A - B \subseteq A \cup B$. Si $A \cap B = \emptyset$: $C(B) = B \cup B = B$ y $C(A) \cup C(B) = (A - B) \cup B = A \cup B$.

## Preguntas de repaso

> [!question]- ¿Qué técnica conviene si los conjuntos están definidos por una propiedad y no por operaciones?
> Doble inclusión con un elemento arbitrario; para refutar la igualdad, un solo elemento que esté en uno y no en el otro.

> [!question]- ¿Cómo se usa $C \subseteq D$ dentro de una cadena de igualdades?
> Como $C \cap D = C$, o como $D^{c} \subseteq C^{c}$, o por monotonía ($C \cap Z \subseteq D \cap Z$); en este último caso la cadena pasa a ser de contenciones.

> [!question]- ¿Qué elementos forman $A \,\Delta\, B \,\Delta\, C$?
> Los que están en un número impar de los tres conjuntos: en exactamente uno o en los tres.
