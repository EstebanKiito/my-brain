---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[01 - Pertenencia, inclusión y axioma de extensión]]"
  - "[[04 - Unión, intersección, diferencia y conjunto potencia]]"
---

# Leyes de la teoría de conjuntos y demostración por doble inclusión

Las operaciones de conjuntos cumplen un puñado de identidades, el **álgebra de conjuntos**, que permiten simplificar expresiones sin volver a la definición cada vez. Son el reflejo exacto de las equivalencias de la lógica proposicional, y por eso se demuestran con ellas.

## Las leyes

Fijado un universo $U$ y $A, B, C \subseteq U$, con complemento $A^c = U \setminus A$:

| Ley | Forma |
|---|---|
| Asociatividad | $A \cup (B \cup C) = (A \cup B) \cup C$; $A \cap (B \cap C) = (A \cap B) \cap C$ |
| Conmutatividad | $A \cup B = B \cup A$; $A \cap B = B \cap A$ |
| Idempotencia | $A \cup A = A$; $A \cap A = A$ |
| Absorción | $A \cup (A \cap B) = A$; $A \cap (A \cup B) = A$ |
| Elemento neutro | $A \cup \varnothing = A$; $A \cap U = A$ |
| Distributividad | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$; $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| De Morgan | $(A \cup B)^c = A^c \cap B^c$; $(A \cap B)^c = A^c \cup B^c$ |
| Elemento inverso | $A \cup A^c = U$; $A \cap A^c = \varnothing$ |
| Dominación | $A \cup U = U$; $A \cap \varnothing = \varnothing$ |

Cada ley viene en pareja: la segunda se obtiene de la primera intercambiando $\cup \leftrightarrow \cap$ y $\varnothing \leftrightarrow U$ (**dualidad**). Todas son la traducción de equivalencias lógicas con $\cup \leftrightarrow \vee$, $\cap \leftrightarrow \wedge$ y complemento $\leftrightarrow \neg$.

## Cómo se demuestra una igualdad

> [!tip] Dos métodos
> 1. **Doble inclusión**: tomar $x$ arbitrario del lado izquierdo y llegar al derecho, y viceversa.
> 2. **Cadena de equivalencias**: $x \in \text{lado izq.} \iff \dots \iff x \in \text{lado der.}$, traduciendo cada operación a su conectivo y usando equivalencias lógicas. Todos los pasos deben ser reversibles.

**Ejemplo: De Morgan, $(A \cup B)^c = A^c \cap B^c$.** Por equivalencias:
$$x \in (A \cup B)^c \iff x \notin A \cup B \iff \neg(x \in A \vee x \in B) \iff x \notin A \wedge x \notin B \iff x \in A^c \cap B^c.$$
La tercera equivalencia es la ley de De Morgan de la lógica.

**Ejemplo: $A \setminus (B \cup C) = (A \setminus B) \setminus C$.**
$$x \in A \setminus (B \cup C) \iff x \in A \wedge \neg(x \in B \vee x \in C) \iff x \in A \wedge x \notin B \wedge x \notin C \iff x \in (A \setminus B) \setminus C.$$

**Ejemplo con contención (una sola dirección):** $(A \setminus B) \setminus C \subseteq A \setminus (B \setminus C)$. Si $x \in (A \setminus B) \setminus C$, entonces $x \in A$, $x \notin B$ y $x \notin C$. Como $x \notin B$, tampoco está en $B \setminus C$ (que exige estar en $B$), y por tanto $x \in A \setminus (B \setminus C)$. La inclusión inversa **falla**: con $A = B = C = \{1\}$ el lado derecho es $\{1\} \setminus \varnothing = \{1\}$ pero el izquierdo es $\varnothing$.

> [!warning] Equivalencias, no "parece que"
> Cuando se usa una cadena de $\iff$, cada paso debe ser una equivalencia válida; si un paso solo es una implicación ($\Rightarrow$), el resultado es únicamente una inclusión. Un diagrama de Venn puede ayudar a anticipar el resultado, pero no sustituye la demostración.

## Contenciones útiles

Se usan como lemas: $A \subseteq A \cup B$, $A \cap B \subseteq A$, $A \subseteq B \iff A \cup B = B \iff A \cap B = A$, y $A \cup B \subseteq C \iff (A \subseteq C \wedge B \subseteq C)$.

## Preguntas de repaso

> [!question]- ¿Cuándo conviene la doble inclusión y cuándo la cadena de equivalencias?
> La cadena sirve cuando todo paso es reversible (identidades "limpias" con operaciones booleanas); la doble inclusión es más segura si hay cuantificadores, funciones o pares ordenados, donde reversibilidad no es evidente.

> [!question]- ¿Por qué la ley $A \cup (A \cap B) = A$ es cierta?
> Todo elemento de $A \cap B$ ya está en $A$, así que añadirlo a $A$ no agrega nada. En lógica es $p \vee (p \wedge q) \equiv p$.

> [!question]- ¿Cómo se refuta una "identidad" de conjuntos?
> Con un contraejemplo concreto: conjuntos pequeños para los que ambos lados difieran, como $A = B = C = \{1\}$ en $(A \setminus B) \setminus C$ frente a $A \setminus (B \setminus C)$.
