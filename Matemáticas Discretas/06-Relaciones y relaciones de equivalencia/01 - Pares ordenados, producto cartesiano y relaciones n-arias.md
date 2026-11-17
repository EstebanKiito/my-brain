---
ramo: "Matemáticas Discretas"
tema: "Relaciones y relaciones de equivalencia"
tags:
  - discretas/relaciones
  - origen/complemento
prerrequisitos: []
---

# Pares ordenados, producto cartesiano y relaciones n-arias

Una tabla de una base de datos relaciona valores de varios dominios: el identificador de una persona con su nombre, su ocupación, etc. Los conjuntos, por sí solos, no distinguen orden ni repiten elementos, así que primero hay que construir el **par ordenado**; con él se define el producto cartesiano y, sobre este, las relaciones.

## Par ordenado

Un par $(a, b)$ debe cumplir una sola propiedad: dos pares son iguales exactamente cuando coinciden componente a componente. La definición de Kuratowski la consigue usando solo conjuntos:

$$(a, b) = \{\{a\}, \{a, b\}\}.$$

> [!tip] Propiedad fundamental
> $(a, b) = (c, d)$ si y solo si $a = c$ y $b = d$.

La demostración de ($\Rightarrow$) separa dos casos. Si $a = b$, entonces $(a, b) = \{\{a\}\}$, así que $\{c\}$ y $\{c, d\}$ son ambos iguales a $\{a\}$, de donde $c = d = a = b$. Si $a \neq b$, el conjunto $\{a, b\}$ tiene dos elementos y no puede ser igual a $\{c\}$; por extensión $\{a\} = \{c\}$, luego $a = c$, y entonces $\{a, b\} = \{a, d\}$ da $b = d$. La implicación ($\Leftarrow$) es inmediata.

> [!warning] No sirve cualquier definición
> Con $(a, b) = \{a, \{b\}\}$ la propiedad falla. Para $x \neq y$, los pares $(\{x\}, y) = \{\{x\}, \{y\}\}$ y $(\{y\}, x) = \{\{y\}, \{x\}\}$ son el mismo conjunto, aunque sus componentes son distintas.

## Tuplas y producto cartesiano

Las tuplas se definen recursivamente: $(a_1, \dots, a_n) = ((a_1, \dots, a_{n-1}), a_n)$. El **producto cartesiano** reúne todos los pares posibles:

$$A \times B = \{(a, b) \mid a \in A \wedge b \in B\}.$$

Con $A = \{1, 2\}$ y $B = \{3, 4\}$ resulta $A \times B = \{(1,3), (1,4), (2,3), (2,4)\}$, con $\lvert A \rvert \cdot \lvert B \rvert = 4$ elementos. El orden importa: $A \times B \neq B \times A$ en general. Para varios conjuntos, $A_1 \times \dots \times A_n = (A_1 \times \dots \times A_{n-1}) \times A_n$, y cuando todos son el mismo se escribe $A^n$.

## Relaciones n-arias

Una **relación** sobre $A_1, \dots, A_n$ es cualquier subconjunto $R \subseteq A_1 \times \dots \times A_n$. Su **aridad** es el tamaño de las tuplas: 2 es binaria, 3 ternaria, etc. Un ejemplo ternario es la suma sobre los naturales:

$$+_{\mathbb{N}} = \{(n_1, n_2, n_3) \in \mathbb{N}^3 \mid n_1 + n_2 = n_3\},$$

donde $(3, 4, 7) \in +_{\mathbb{N}}$ pero $(0, 0, 1) \notin +_{\mathbb{N}}$. Una tabla con columnas *id*, *nombre*, *apellido*, *ocupación* y *MBTI* es una relación de aridad 5: cada fila es una 5-tupla y la tabla completa es un subconjunto del producto de los cinco dominios. Esa es la razón de que se hable de bases de datos **relacionales**.

Como cada relación binaria de $A$ en $B$ es un subconjunto de $A \times B$, que tiene $\lvert A \rvert \lvert B \rvert$ elementos, hay $2^{\lvert A \rvert \lvert B \rvert}$ relaciones posibles: para $A = \{1, 2\}$ y $B = \{3, 4\}$ son $2^4 = 16$.

## Preguntas de repaso

> [!question]- ¿Por qué $\{a, b\}$ no sirve como par ordenado?
> Porque $\{a, b\} = \{b, a\}$: no distingue el orden de las componentes, que es justo lo que un par debe recordar.

> [!question]- ¿Qué se rompe en la definición $(a, b) = \{a, \{b\}\}$?
> No se cumple la igualdad componente a componente: dos pares con componentes distintas, como $(\{x\}, y)$ y $(\{y\}, x)$, resultan ser el mismo conjunto.

> [!question]- ¿Cuántos elementos tiene $A \times B \times C$ si $\lvert A \rvert = 2$, $\lvert B \rvert = 3$ y $\lvert C \rvert = 4$?
> $24$: se elige una componente de cada conjunto de forma independiente, $2 \cdot 3 \cdot 4$.

> [!question]- ¿Es una tabla de base de datos un conjunto de tuplas?
> Sí: cada fila es una tupla y la tabla es una relación $n$-aria, es decir, un subconjunto del producto cartesiano de los dominios de sus columnas.
