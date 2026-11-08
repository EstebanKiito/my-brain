---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[02 - Igualdad, conjunto vacío y universo]]"
---

# Subconjuntos y diagramas de Venn

Decir que un conjunto está "dentro" de otro es la relación de **contención**. Junto con la igualdad, es la forma básica de comparar conjuntos, y se visualiza con los **diagramas de Venn**.

## Subconjuntos

Un conjunto $A$ es **subconjunto** de $B$ si todo elemento de $A$ también es elemento de $B$; se escribe $A \subseteq B$. Si no lo es, $A \nsubseteq B$.

> [!tip] Subconjunto
> $A \subseteq B$ significa "todo elemento de $A$ pertenece a $B$". Para probarlo se toma un $x \in A$ arbitrario y se muestra que $x \in B$; para refutarlo basta un elemento de $A$ que no esté en $B$.

La contención cumple propiedades básicas: para conjuntos arbitrarios,

1. $\emptyset \subseteq A \subseteq U$,
2. $A \subseteq A$ (reflexiva),
3. si $A \subseteq B$ y $B \subseteq C$, entonces $A \subseteq C$ (transitiva),
4. $A = B$ si y solo si $A \subseteq B$ y $B \subseteq A$.

La última es la forma estándar de probar una igualdad de conjuntos: **doble contención**.

## Pertenece vs. está contenido

Los símbolos $\in$ y $\subseteq$ están relacionados pero no son lo mismo:

$$
a \in A \iff \{a\} \subseteq A.
$$

Un *elemento* pertenece; un *conjunto* está contenido. Confundirlos produce errores como escribir $\{a\} \in A$ donde corresponde $\{a\} \subseteq A$.

> [!warning] $\in$ no es $\subseteq$
> $\in$ relaciona un elemento con un conjunto; $\subseteq$ relaciona dos conjuntos. Para que $a \in A$ se convierta en una contención se escribe $\{a\} \subseteq A$.

## Diagramas de Venn

Un **diagrama de Venn** representa los conjuntos como figuras planas cerradas (discos) dentro de un rectángulo que es el universo $U$. Sirve para ver de un vistazo las relaciones de contención y las operaciones.

![Diagramas de Venn de inclusión, intersección y conjuntos disjuntos](adjuntos/Diagramas%20de%20Venn%20de%20inclusi%C3%B3n,%20intersecci%C3%B3n%20y%20conjuntos%20disjuntos.png)

> [!example]- Transcripción de la imagen
> Tres rectángulos rotulados $U$ (el universo), cada uno con dos conjuntos. Izquierda: $A$ dibujado dentro de $B$, es decir, $A \subseteq B$. Centro: $A$ y $B$ se superponen; tienen elementos en común. Derecha: $A$ y $B$ están separados; no tienen elementos en común (son disjuntos).

## Preguntas de repaso

> [!question]- ¿Cómo se demuestra que $A = B$?
> Por doble contención: se prueba $A \subseteq B$ y $B \subseteq A$. Si ambas valen, $A$ y $B$ tienen exactamente los mismos elementos.

> [!question]- ¿Es cierto que $A \subseteq A$ para todo conjunto $A$? Justifique.
> Sí (reflexiva): todo elemento de $A$ está en $A$ por definición. Es trivial pero es una de las propiedades básicas de la contención.

> [!question]- Escriba "$a$ pertenece a $A$" usando el símbolo $\subseteq$.
> $\{a\} \subseteq A$: el conjunto cuyo único elemento es $a$ está contenido en $A$.

> [!question]- ¿Qué representa el rectángulo en un diagrama de Venn?
> El conjunto universo $U$: todos los elementos que se están considerando. Los demás conjuntos se dibujan como discos dentro de él.
