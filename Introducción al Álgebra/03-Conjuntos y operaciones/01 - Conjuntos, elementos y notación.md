---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - origen/complemento
prerrequisitos: []
---

# Conjuntos, elementos y notación

Gran parte de la matemática se enuncia en términos de conjuntos: los números pares, las soluciones de una ecuación, los puntos de una recta. Un **conjunto** agrupa objetos bajo una característica común y se trata a esa colección como una sola entidad, lo que permite operar con ella igual que con los números.

## Conjuntos y pertenencia

Un conjunto es una colección de objetos considerada como una identidad. Los objetos reunidos se llaman **elementos**, y se dice que **pertenecen** al conjunto. Si $a$ es elemento de $A$ se escribe $a \in A$; si no lo es, $a \notin A$.

> [!tip] Conjunto y pertenencia
> Un **conjunto** es una colección de objetos considerada como una sola identidad. Si $a$ está en $A$ se escribe $a \in A$ ("$a$ pertenece a $A$"); si no, $a \notin A$.

**Ejemplos.** Si $A$ es el conjunto de los números pares, $18 \in A$ y $5 \notin A$. Si $R$ es el conjunto de los rectángulos y $P$ un paralelogramo, $P \in R$; un círculo $C$ cumple $C \notin R$.

> [!warning] Los elementos pueden ser conjuntos
> Un conjunto puede tener conjuntos como elementos: si $B$ es un libro, $P$ una página y $L$ una línea, entonces $L \in P$ y $P \in B$. La pertenencia depende de qué se considere "elemento" en cada nivel.

## Describir un conjunto

Un conjunto se escribe encerrando entre llaves sus elementos o la propiedad que los define.

- **Por extensión:** se listan todos los elementos. $A = \{1, 2, 3\}$. Todo lo que no figure no pertenece: $4 \notin A$.
- **Por compresión:** se da una propiedad. $A = \{x \mid P(x)\}$ se lee "$A$ es el conjunto de todos los $x$ tales que $x$ cumple $P(x)$". Por ejemplo, $\{1,2,3\} = \{x \in \mathbb{N} \mid x < 4\}$.

La compresión es útil cuando hay muchos elementos. Por ejemplo, $B = \{2, 4, 6, 8, 10\} = \{x \in \mathbb{N} \mid x \text{ es par y } x < 12\}$.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre escribir un conjunto por extensión y por compresión?
> Por extensión se listan todos los elementos uno a uno ($\{1,2,3\}$); por compresión se da la propiedad que los define ($\{x \mid P(x)\}$). La compresión sirve cuando hay muchos o infinitos elementos.

> [!question]- Escriba por extensión $\{x \mid x \text{ es una vocal del español}\}$.
> $\{a, e, i, o, u\}$.

> [!question]- Escriba por compresión $\{2, 4, 6, 8, 10\}$.
> $\{x \in \mathbb{N} \mid x \text{ es par y } x < 12\}$, o equivalentemente $\{2n \mid n \in \mathbb{N},\ n \le 5\}$.

> [!question]- Si $A = \{1, 2, 3\}$, indique cuáles pertenecen y cuáles no: $2$, $5$, $-1$.
> $2 \in A$; $5 \notin A$; $-1 \notin A$. Solo los elementos listados (o que cumplen la propiedad) pertenecen.
