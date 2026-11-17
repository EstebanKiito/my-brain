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

# Pares ordenados y producto cartesiano

Los conjuntos no tienen orden ni repeticiones, pero una tabla de base de datos, una coordenada $(x, y)$ o una relación sí los necesitan: $(1, 2)$ y $(2, 1)$ deben ser objetos distintos. El **par ordenado** agrega esa noción usando solo conjuntos, y el **producto cartesiano** reúne todos los pares posibles entre dos conjuntos.

## Definición de Kuratowski

> [!tip] Par ordenado
> $(a, b) = \{\{a\}, \{a, b\}\}$. Propiedad clave: $(a, b) = (c, d) \iff a = c \wedge b = d$.

La definición se elige para que valga esa propiedad, que es lo único que se espera de un par. El orden queda codificado así: $a$ es el elemento que aparece en el conjunto de **un** elemento, y $b$ el que acompaña en el de dos. Ejemplo: $(1,2) = \{\{1\},\{1,2\}\}$ y $(2,1) = \{\{2\},\{1,2\}\}$ son distintos, mientras que $(1,1) = \{\{1\}\}$.

**Demostración de la propiedad.** ($\Leftarrow$) Si $a = c$ y $b = d$, los conjuntos son literalmente el mismo. ($\Rightarrow$) Se supone $\{\{a\},\{a,b\}\} = \{\{c\},\{c,d\}\}$ y se separan casos:

- **$a = b$**: el lado izquierdo es $\{\{a\}\}$, un conjunto con un solo elemento. Entonces $\{c\} = \{a\}$ y $\{c, d\} = \{a\}$, de donde $c = a$ y $d = c = a = b$.
- **$a \neq b$**: $\{a, b\}$ tiene dos elementos, así que no puede igualar a $\{c\}$; por extensión debe ser $\{a\} = \{c\}$, o sea $a = c$. Entonces $\{a, b\} = \{a, d\}$ y, como $a$ está en ambos, $b = d$.

> [!warning] No cualquier definición sirve
> Con $(a, b) = \{a, \{b\}\}$ la propiedad **falla**: para $x \neq y$, $a = \{x\}$, $b = y$, $c = \{y\}$, $d = x$ da $(a,b) = \{\{x\},\{y\}\} = (c,d)$ aunque $a \neq c$ y $b \neq d$. Los dos pares "se confunden" porque el conjunto no distingue cuál elemento hace de primero.

## Tuplas

Las **$n$-tuplas** se definen recursivamente a partir de los pares: $(a, b, c) = ((a, b), c)$ y, en general,
$$(a_1, \dots, a_n) = ((a_1, \dots, a_{n-1}), a_n).$$

## Producto cartesiano

> [!tip] Producto cartesiano
> $A \times B = \{(a, b) \mid a \in A \wedge b \in B\}$, y $A_1 \times \cdots \times A_n = (A_1 \times \cdots \times A_{n-1}) \times A_n$.

Ejemplo: con $A = \{1,2\}$ y $B = \{3,4\}$, $A \times B = \{(1,3),(1,4),(2,3),(2,4)\}$. Si $A$ y $B$ son finitos, $\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert$; con un tercer conjunto de $3$ elementos, $\lvert A \times B \times C \rvert = 2 \cdot 2 \cdot 3 = 12$. Una **relación** (siguiente tema del curso) es simplemente un subconjunto de un producto cartesiano.

## Propiedades y demostraciones

- **No es conmutativo**: $A \times B = B \times A$ si y solo si $A = B$ (cuando ambos no son vacíos). Con $A = \{1\}$ y $B = \{2\}$ se tiene $(1,2) \in A \times B$ pero $(1,2) \notin B \times A$.
- **Monotonía**: si $A \subseteq B$ y $C \subseteq D$, entonces $A \times C \subseteq B \times D$.
- **Distribuye** sobre unión: $(A \cup B) \times C = (A \times C) \cup (B \times C)$, y sobre diferencia: $A \times (B \setminus C) = (A \times B) \setminus (A \times C)$.

Todas se prueban con pares arbitrarios $(x, y)$: se baja $(x,y) \in A \times B$ a "$x \in A \wedge y \in B$" y se trabaja con la lógica. Por ejemplo, para la unión:
$$(x, y) \in (A \cup B) \times C \iff (x \in A \vee x \in B) \wedge y \in C \iff (x \in A \wedge y \in C) \vee (x \in B \wedge y \in C).$$

## Preguntas de repaso

> [!question]- ¿Qué propiedad debe cumplir una definición de par ordenado y por qué la de Kuratowski la cumple?
> Que $(a,b) = (c,d)$ equivalga a $a = c \wedge b = d$. La de Kuratowski lo logra porque $a$ queda distinguido como el único elemento del conjunto unitario.

> [!question]- ¿Por qué $\{a, \{b\}\}$ no sirve como par ordenado?
> Porque pares distintos como $(\{x\}, y)$ y $(\{y\}, x)$ dan el mismo conjunto $\{\{x\},\{y\}\}$.

> [!question]- ¿Por qué $A \times B \neq B \times A$ en general?
> Los pares $(a, b)$ y $(b, a)$ son distintos cuando $a \neq b$; los productos solo coinciden si cada uno de los conjuntos coincide con el otro.

> [!question]- ¿Cuántos elementos tiene $\{1,2,3\} \times \{a,b\}$?
> $3 \cdot 2 = 6$ pares: por cada elemento de la primera coordenada hay dos opciones para la segunda.
