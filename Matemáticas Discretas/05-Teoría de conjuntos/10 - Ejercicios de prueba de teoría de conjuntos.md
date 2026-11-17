---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Leyes de la teoría de conjuntos y demostración por doble inclusión]]"
  - "[[07 - Pares ordenados y producto cartesiano]]"
  - "[[08 - Números naturales construidos con conjuntos]]"
---

# Ejercicios de prueba de teoría de conjuntos

Las interrogaciones y exámenes preguntan sobre conjuntos en cinco formatos: **propiedades del par ordenado** (definición de Kuratowski), **identidades y contenciones** entre operaciones (por doble inclusión), **producto cartesiano**, **teoremas de los axiomas** (unicidad del vacío, que $\mathbb{N}$ no es sucesor de un conjunto) y **familias cerradas** como las topologías. La pauta suele puntuar: separar bien cada inclusión, elegir un elemento arbitrario y citar la definición usada en cada paso.

## Ejercicios

### 1. Par ordenado de Kuratowski (I2, 2015-2)
(a) Con $(a, b) = \{\{a\}, \{a, b\}\}$, demuestre que $(a, b) = (c, d)$ si y solo si $a = c \wedge b = d$. (b) Muestre que con la definición alternativa $(a, b) = \{a, \{b\}\}$ la propiedad no vale.

> [!example]- Solución
> **(a)** ($\Leftarrow$) es inmediata. ($\Rightarrow$) Si $a = b$, $(a, b) = \{\{a\}\}$ tiene un solo elemento; entonces $\{c\} = \{a\} = \{c, d\}$, así que $c = a$ y $d = c$, y $b = a = c = d$. Si $a \neq b$, $\{a, b\}$ tiene dos elementos y no puede igualar a $\{c\}$, luego $\{a\} = \{c\}$, es decir, $a = c$; de $\{a, b\} = \{a, d\}$ sale $b = d$.
>
> **(b)** Para $x \neq y$ sean $a = \{x\}$, $b = y$, $c = \{y\}$, $d = x$. Entonces $(a, b) = \{\{x\}, \{y\}\} = (c, d)$, pero $a \neq c$ y $b \neq d$.

### 2. Propiedades del producto cartesiano (I2, 2017-2)
Sean $A, B, C, D$ conjuntos y $\{A_i\}_{i \in \mathbb{N}}$ una colección. Demuestre: (a) $A \subseteq B \wedge C \subseteq D \Rightarrow A \times C \subseteq B \times D$; (b) $(A \cup B) \times C = (A \times C) \cup (B \times C)$; (c) $\left(\bigcap_{i} A_i\right) \times B = \bigcap_{i} (A_i \times B)$.

> [!example]- Solución
> Se trabaja con un par arbitrario $(x, y)$.
>
> **(a)** Si $(x, y) \in A \times C$, entonces $x \in A \subseteq B$ e $y \in C \subseteq D$, así que $(x, y) \in B \times D$.
>
> **(b)** $(x, y) \in (A \cup B) \times C \iff (x \in A \vee x \in B) \wedge y \in C \iff (x \in A \wedge y \in C) \vee (x \in B \wedge y \in C) \iff (x, y) \in (A \times C) \cup (B \times C)$ (distributividad de $\wedge$ sobre $\vee$).
>
> **(c)** $(x, y) \in \left(\bigcap_i A_i\right) \times B \iff (\forall i\ x \in A_i) \wedge y \in B \iff \forall i\,(x \in A_i \wedge y \in B) \iff (x, y) \in \bigcap_i (A_i \times B)$. El paso central mete $y \in B$ dentro del $\forall$, lo que es válido porque $y \in B$ no depende de $i$ (y la colección no es vacía).

### 3. Unicidad del vacío (I2, 2019-2)
(a) Demuestre que existe un único conjunto vacío. (b) Demuestre que para todo $A$ se cumple $\varnothing \subseteq A$.

> [!example]- Solución
> **(b)** Hay que probar $\forall x\,(x \in \varnothing \to x \in A)$. Como $x \in \varnothing$ es siempre falso, la implicación es verdadera.
>
> **(a)** Sean $\varnothing_1$ y $\varnothing_2$ vacíos. Por (b), $\varnothing_1 \subseteq \varnothing_2$ y $\varnothing_2 \subseteq \varnothing_1$, luego son iguales por extensión.

### 4. Diferencias y subconjuntos (I1, 2020-2)
Sea $U$ un universo y $A, B, C \subseteq U$. Demuestre: (i) $A \setminus B \subseteq C \iff A \setminus C \subseteq B$; (ii) $A \subseteq B \iff$ para todo $D \subseteq U$, $D \subseteq A \to D \subseteq B$.

> [!example]- Solución
> **(i)** $A \setminus B \subseteq C$ significa $\forall x\,(x \in A \wedge x \notin B \to x \in C)$, que equivale a $\forall x\,(x \notin A \vee x \in B \vee x \in C)$. Con la misma transformación, $A \setminus C \subseteq B$ equivale a $\forall x\,(x \notin A \vee x \in C \vee x \in B)$: la misma fórmula porque $\vee$ es conmutativo.
>
> **(ii)** ($\Rightarrow$) Si $D \subseteq A$ y $A \subseteq B$, la transitividad de $\subseteq$ da $D \subseteq B$. ($\Leftarrow$) Se toma $D = A$ (que es subconjunto de $U$ y de sí mismo): la hipótesis entrega $A \subseteq A \to A \subseteq B$, y como $A \subseteq A$ se concluye $A \subseteq B$.

### 5. Topología de complementos finitos (I1, 2022-2)
$T \subseteq \mathcal{P}(A)$ es una **topología** si $\varnothing, A \in T$; si $\mathcal{S} \subseteq T$ entonces $\bigcup \mathcal{S} \in T$; y si $X, Y \in T$ entonces $X \cap Y \in T$. (a) Dé una topología sobre $\mathbb{N}$. (b) Pruebe que $T = \{X \subseteq A \mid X = \varnothing \vee X^c \text{ es finito}\}$ es una topología sobre $A$.

> [!example]- Solución
> **(a)** $\{\varnothing,\ \text{pares},\ \text{impares},\ \mathbb{N}\}$: la unión de pares e impares es $\mathbb{N}$ y su intersección es $\varnothing$, así que la familia es cerrada (se comprobó sobre un universo finito de seis elementos). También sirven $\{\varnothing, \mathbb{N}\}$ y $\mathcal{P}(\mathbb{N})$.
>
> **(b)** $\varnothing \in T$ por definición y $A^c = \varnothing$ es finito, luego $A \in T$.
> - *Uniones:* sea $\mathcal{S} \subseteq T$. Si todos sus elementos son vacíos, $\bigcup \mathcal{S} = \varnothing \in T$. Si no, hay $X_0 \in \mathcal{S}$ no vacío con $X_0^c$ finito, y $\left(\bigcup \mathcal{S}\right)^c = \bigcap_{X \in \mathcal{S}} X^c \subseteq X_0^c$ es finito.
> - *Intersecciones:* si $X$ o $Y$ es vacío, $X \cap Y = \varnothing$. Si no, $(X \cap Y)^c = X^c \cup Y^c$ es una unión finita de finitos.

### 6. Identidad con diferencias (Examen, 2022-2)
Demuestre que $A \setminus (B \cup C) = (A \setminus B) \setminus C$.

> [!example]- Solución
> $a \in A \setminus (B \cup C) \iff a \in A \wedge \neg(a \in B \vee a \in C) \iff a \in A \wedge a \notin B \wedge a \notin C \iff a \in (A \setminus B) \setminus C$. Cada paso es una equivalencia (definición de diferencia y unión, y De Morgan lógica), así que no hace falta separar inclusiones.

### 7. Diferencia y conjunto potencia (I1, 2025-2)
(a) Demuestre que $(A \setminus B) \setminus C \subseteq A \setminus (B \setminus C)$. (b) Demuestre que $\mathcal{P}(A \setminus B) \neq \mathcal{P}(A) \setminus \mathcal{P}(B)$ para todos $A$ y $B$.

> [!example]- Solución
> **(a)** Si $x \in (A \setminus B) \setminus C$, entonces $x \in A$, $x \notin B$ y $x \notin C$. Como $x \notin B$, $x \notin B \setminus C$, y por tanto $x \in A \setminus (B \setminus C)$.
>
> **(b)** $\varnothing \in \mathcal{P}(A \setminus B)$ siempre. Pero también $\varnothing \in \mathcal{P}(B)$, así que $\varnothing \notin \mathcal{P}(A) \setminus \mathcal{P}(B)$. Un elemento los distingue, y por extensión los conjuntos son distintos. (Ejemplo: $A = \{1,2\}$, $B = \{2\}$ da $\{\varnothing, \{1\}\}$ frente a $\{\{1\}, \{1,2\}\}$.)

### 8. $\mathbb{N}$ no es el sucesor de un conjunto (I1, 2025-2)
El sucesor de $A$ es $A \cup \{A\}$. Demuestre que no existe $A$ con $A \cup \{A\} = \mathbb{N}$, sabiendo que ningún conjunto cumple $A \in A$.

> [!example]- Solución
> Por contradicción, supóngase $A \cup \{A\} = \mathbb{N}$. Como $A \in \{A\} \subseteq A \cup \{A\}$, se tiene $A \in \mathbb{N}$. Pero $\mathbb{N}$ es cerrado bajo el sucesor, así que $A \cup \{A\} \in \mathbb{N}$, o sea $\mathbb{N} \in \mathbb{N}$. Esto contradice que ningún conjunto es elemento de sí mismo.

## Preguntas de repaso

> [!question]- ¿Cuándo basta una cadena de $\iff$ y cuándo conviene la doble inclusión?
> La cadena basta en identidades puramente booleanas (ejercicios 2b, 4i, 6), donde cada paso es reversible; la doble inclusión se usa cuando hay cuantificadores o la reversibilidad no es evidente.

> [!question]- ¿Qué se busca cuando se pide "no vale para todos $A$ y $B$"?
> Un elemento que pertenezca a un lado y no al otro, como $\varnothing$ en el ejercicio 7b; se prueba que una desigualdad se cumple siempre, no solo en un ejemplo.

> [!question]- ¿Por qué en el ejercicio 5(b) la unión de una familia arbitraria sigue teniendo complemento finito?
> Basta un miembro no vacío $X_0$: la unión contiene a $X_0$, así que su complemento queda dentro del complemento (finito) de $X_0$.
