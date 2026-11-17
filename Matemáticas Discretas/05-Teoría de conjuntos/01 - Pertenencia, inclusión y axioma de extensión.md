---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - origen/complemento
prerrequisitos: []
---

# Pertenencia, inclusión y axioma de extensión

Los conjuntos se usan en todo el curso (relaciones, funciones, grafos) de forma intuitiva. Aquí se fijan con precisión las tres ideas con las que se construye todo lo demás: **pertenencia**, **inclusión** e **igualdad**. Sin esa precisión no se pueden hacer demostraciones sobre conjuntos, porque cada paso debe apoyarse en una definición.

## Conjunto, elemento y pertenencia

Un **conjunto** es una colección bien definida de objetos, llamados **elementos**; si $x$ es un elemento de $A$ se escribe $x \in A$ ("$x$ pertenece a $A$"). Los elementos pueden ser a su vez conjuntos, y de ahí sale la primera trampa: la pertenencia no es transitiva.

$$2 \in \{1, 2\} \in \{\{1, 2\}, \{2, 3\}\} \quad\text{pero}\quad 2 \notin \{\{1, 2\}, \{2, 3\}\}.$$

El conjunto $\{\{1,2\},\{2,3\}\}$ tiene exactamente **dos** elementos, que son conjuntos; el número $2$ está "un nivel más abajo" y no es elemento suyo.

## Subconjunto

> [!tip] Definición de subconjunto
> $A \subseteq B$ significa $\forall x\,(x \in A \to x \in B)$: cada elemento de $A$ está también en $B$.

Para probar $A \subseteq B$ se toma un $x$ arbitrario de $A$ y se muestra que está en $B$. Para **refutarlo** basta un único elemento de $A$ que no esté en $B$, porque la negación es
$$A \not\subseteq B \iff \exists x\,(x \in A \wedge x \notin B).$$

Ejemplos: $\mathbb{N} \subseteq \mathbb{Z}$ es cierto; $\{1,2\} \subseteq \{1,2,3\}$ es cierto; pero $\{1,2\} \subseteq \{\{1,2\},\{2,3\}\}$ es **falso**, porque $1$ no es elemento de $\{\{1,2\},\{2,3\}\}$. Lo que sí vale es $\{1,2\} \in \{\{1,2\},\{2,3\}\}$.

> [!warning] $\in$ no es $\subseteq$
> $x \in A$ habla de un elemento; $A \subseteq B$ compara colecciones. Para $A = \{1\}$ se tiene $1 \in A$ y $\{1\} \subseteq A$, pero no $1 \subseteq A$ ni $\{1\} \in A$. Ante la duda, se pregunta "¿es un elemento o es una colección de elementos?".

![Diagramas de Venn de la inclusión A subconjunto de B](adjuntos/Diagramas%20de%20Venn%20de%20la%20inclusi%C3%B3n%20A%20subconjunto%20de%20B.png)

> [!example]- Transcripción de la imagen
> - A la izquierda (a), un círculo pequeño $A$ dentro de otro grande $B$: $A$ es subconjunto de $B$ y tiene menos elementos.
> - A la derecha (b), un único círculo etiquetado $A = B$: el caso extremo en que la inclusión se cumple con igualdad.
> - Ambas son formas válidas de dibujar $A \subseteq B$.

## Igualdad y axioma de extensión

Dos conjuntos son iguales si cada uno está contenido en el otro: $A = B \leftrightarrow A \subseteq B \wedge B \subseteq A$. Desarrollando la definición de subconjunto y agrupando los cuantificadores se llega a la forma que se usa como axioma:

$$A = B \leftrightarrow \forall x\,(x \in A \leftrightarrow x \in B).$$

> [!tip] Axioma de extensión
> Un conjunto queda definido **solo** por sus elementos: no importan el orden, la descripción ni las repeticiones. Por eso $\{x, x\} = \{x\}$ y $\{1, 2\} = \{2, 1\}$.

La consecuencia práctica es el método estándar para demostrar $A = B$: la **doble inclusión**, probar $A \subseteq B$ y $B \subseteq A$ por separado.

## Subconjunto propio

$A$ es **subconjunto propio** de $B$ ($A \subsetneq B$) si $A \subseteq B$ y $A \neq B$. Como $A \neq B$ equivale a $A \not\subseteq B \vee B \not\subseteq A$, y $A \subseteq B$ ya se asume, la condición se reduce a $B \not\subseteq A$, es decir, a que **existe** un $x \in B$ con $x \notin A$. Por ejemplo $\{1,2\} \subsetneq \{1,2,3\}$ (el $3$ sobra), pero $\{1,2\} \not\subsetneq \{2,1\}$ porque son el mismo conjunto.

## Preguntas de repaso

> [!question]- ¿Por qué $\{1,2\} \in \{\{1,2\},\{2,3\}\}$ pero $\{1,2\} \not\subseteq \{\{1,2\},\{2,3\}\}$?
> Porque los elementos del conjunto grande son los dos pares, no los números. Para la inclusión habría que tener $1 \in \{\{1,2\},\{2,3\}\}$, y no es así.

> [!question]- ¿Cómo se demuestra que dos conjuntos son iguales, y por qué funciona?
> Por doble inclusión: se prueba $A \subseteq B$ y $B \subseteq A$. Funciona porque, por definición, la igualdad es exactamente la conjunción de ambas inclusiones (axioma de extensión).

> [!question]- ¿Qué basta para probar que $A \not\subseteq B$?
> Exhibir un elemento de $A$ que no esté en $B$: la negación de un "para todo" es un "existe".

> [!question]- ¿Es $\{1, 1, 2\}$ distinto de $\{1, 2\}$?
> No. Los conjuntos tienen los mismos elementos y, por extensión, son iguales; las repeticiones no cuentan.
