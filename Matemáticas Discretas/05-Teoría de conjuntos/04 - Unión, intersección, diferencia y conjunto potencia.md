---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[01 - Pertenencia, inclusión y axioma de extensión]]"
  - "[[03 - Axioma de abstracción, paradoja de Russell y separación]]"
---

# Unión, intersección, diferencia y conjunto potencia

Con el vacío como único conjunto seguro, las **operaciones** permiten fabricar conjuntos nuevos a partir de otros. Todas se definen con una propiedad lógica sobre los elementos, de modo que cada operación es el reflejo de un conectivo: la unión de "o", la intersección de "y" y la diferencia de "y no".

## Las operaciones

| Operación | Definición | Se lee |
|---|---|---|
| Unión | $A \cup B = \{x \mid x \in A \vee x \in B\}$ | en $A$ o en $B$ (o en ambos) |
| Intersección | $A \cap B = \{x \mid x \in A \wedge x \in B\}$ | en $A$ y en $B$ |
| Diferencia | $A \setminus B = \{x \mid x \in A \wedge x \notin B\}$ | en $A$ pero no en $B$ |
| Complemento | $A^c = U \setminus A$ | lo que no está en $A$, dentro de un universo $U$ |
| Conjunto potencia | $\mathcal{P}(A) = \{X \mid X \subseteq A\}$ | todos los subconjuntos de $A$ |

Ejemplo: con $A = \{1,2,3,4\}$ y $B = \{3,4,5,6\}$ resulta $A \cup B = \{1,\dots,6\}$, $A \cap B = \{3,4\}$, $A \setminus B = \{1,2\}$ y $B \setminus A = \{5,6\}$. La diferencia **no es simétrica**.

Algunas contenciones se usan constantemente: $A \subseteq A \cup B$, $A \cap B \subseteq A$, $A \setminus B \subseteq A$.

![Diagramas de Venn de unión, intersección, diferencia y complemento](adjuntos/Diagramas%20de%20Venn%20de%20las%20operaciones%20entre%20dos%20conjuntos.png)

> [!example]- Transcripción de la imagen
> Cuatro rectángulos que representan el universo $U$, cada uno con dos círculos que se solapan, $A$ y $B$:
> - Primero se sombrean ambos círculos: $A \cup B$.
> - Segundo se sombrea solo la lente central donde se solapan: $A \cap B$.
> - Tercero se sombrea el círculo $B$ menos la lente: $B - A$.
> - Cuarto se sombrea todo el rectángulo y quedan en blanco los dos círculos; el pie del dibujo lo rotula $A^c$. En rigor, el complemento de $A$ también incluye la parte de $B$ que no se solapa con $A$ (el tercer dibujo la sombrea), así que esa región en blanco corresponde en realidad a $(A \cup B)^c$.

> [!warning] Los diagramas ayudan, no demuestran
> Un diagrama de Venn sirve para intuir y para refutar, pero una demostración rigurosa se hace con la definición elemento por elemento (ver [[05 - Leyes de la teoría de conjuntos y demostración por doble inclusión]]).

## Conjunto potencia

$\mathcal{P}(A)$ es un conjunto **de conjuntos**. Para $A = \{1,2,3\}$ tiene ocho elementos:
$$\mathcal{P}(A) = \{\varnothing, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}\}.$$

Siempre se cumple $\varnothing \in \mathcal{P}(A)$ (el vacío es subconjunto de todo) y $A \in \mathcal{P}(A)$ (todo conjunto es subconjunto de sí mismo). Si $A$ tiene $n$ elementos, $\mathcal{P}(A)$ tiene $2^n$: para formar un subconjunto se decide, elemento por elemento, "entra o no entra". Casos pequeños: $\mathcal{P}(\varnothing) = \{\varnothing\}$ (un elemento, $2^0 = 1$) y $\mathcal{P}(\{1,2\})$ tiene $4$ elementos, así que $\mathcal{P}(\mathcal{P}(\{1,2\}))$ tiene $2^4 = 16$.

> [!warning] Potencia no es distributiva con la diferencia
> En general $\mathcal{P}(A \setminus B) \neq \mathcal{P}(A) \setminus \mathcal{P}(B)$. Con $A = \{1,2\}$ y $B = \{2\}$: $\mathcal{P}(A \setminus B) = \{\varnothing, \{1\}\}$ pero $\mathcal{P}(A) \setminus \mathcal{P}(B) = \{\{1\}, \{1,2\}\}$. La razón general: $\varnothing$ está en $\mathcal{P}(A \setminus B)$ y, al estar también en $\mathcal{P}(B)$, se elimina del segundo.

## Preguntas de repaso

> [!question]- ¿Por qué la diferencia no es conmutativa pero la unión y la intersección sí?
> Porque "o" y "y" son simétricos en sus argumentos, mientras que "$x \in A$ y $x \notin B$" trata de forma distinta a $A$ y $B$.

> [!question]- ¿Cuántos elementos tiene $\mathcal{P}(\{a,b,c,d\})$ y por qué?
> $2^4 = 16$: cada uno de los cuatro elementos puede estar o no en un subconjunto, y esas decisiones son independientes.

> [!question]- ¿Por qué $\varnothing \in \mathcal{P}(A)$ aunque $A$ sea vacío?
> Porque $\varnothing \subseteq A$ para todo $A$; si $A = \varnothing$, entonces $\mathcal{P}(A) = \{\varnothing\}$ no es vacío.

> [!question]- ¿Cómo se relaciona cada operación con un conectivo lógico?
> Unión con $\vee$, intersección con $\wedge$, diferencia con $\wedge\,\neg$ y complemento con $\neg$; por eso las leyes de conjuntos reflejan las equivalencias lógicas.
