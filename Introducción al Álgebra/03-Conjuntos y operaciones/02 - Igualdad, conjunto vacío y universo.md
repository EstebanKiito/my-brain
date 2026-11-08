---
ramo: "Introducción al Álgebra"
tema: "Conjuntos y operaciones"
tags:
  - intro-algebra/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[01 - Conjuntos, elementos y notación]]"
---

# Igualdad, conjunto vacío y universo

Para operar con conjuntos hacen falta tres nociones de base: cuándo dos conjuntos son iguales, el conjunto que no tiene elementos y el marco de referencia donde se trabaja. Las tres determinan si una descripción por compresión es correcta o no.

## Igualdad de conjuntos

Dos conjuntos son **iguales** si tienen exactamente los mismos elementos. Ni el orden ni las repeticiones importan: $\{1, 2, 3\} = \{3, 2, 3, 2, 1\}$ porque ambos contienen $1$, $2$ y $3$.

> [!tip] Igualdad de conjuntos
> $A = B$ si y solo si tienen los mismos elementos. El orden en que se listan y las repeticiones no cambian el conjunto.

## Conjunto vacío

El **conjunto vacío**, denotado $\emptyset$, es el conjunto que no tiene elementos. Por ejemplo, $\{x \mid x \text{ es un alumno con más de 300 años}\} = \emptyset$, y $\{x \in \mathbb{N} \mid x < 1\} = \emptyset$ porque el menor natural es $1$.

> [!warning] $\emptyset \neq \{\emptyset\}$
> El conjunto vacío no tiene elementos, mientras que $\{\emptyset\}$ tiene **un** elemento (que es el vacío). Es la diferencia entre una caja vacía y una caja que contiene una caja vacía.

## Conjunto universo

En cada aplicación, todos los conjuntos viven dentro de un conjunto fijo llamado **universo**, denotado $U$. El universo importa: la compresión puede dar conjuntos distintos según el universo. Por ejemplo, $A = \{x \in U \mid x^2 + 3 = 7\}$ tiene como soluciones de $x^2 - 4 = 0$ a $x = \pm 2$, de modo que $A = \{2\}$ si $U = \mathbb{N}$, pero $A = \{-2, 2\}$ si $U = \mathbb{Z}$.

## Cardinalidad

La **cardinalidad** de un conjunto finito es su número de elementos, denotada $n(A)$. Por ejemplo, $n(\{h,i,j,k,l,n\}) = 6$, y $n(\{x, y, x, x, y\}) = 2$ porque solo hay dos elementos distintos.

## Preguntas de repaso

> [!question]- ¿$\{1, 2\}$ y $\{2, 1, 2\}$ son iguales? ¿Por qué?
> Sí. Tienen los mismos elementos ($1$ y $2$); el orden y las repeticiones no alteran un conjunto.

> [!question]- ¿Cuál es la cardinalidad de $\emptyset$ y de $\{\emptyset\}$?
> $n(\emptyset) = 0$ y $n(\{\emptyset\}) = 1$: el segundo contiene un elemento, que es el conjunto vacío.

> [!question]- ¿Por qué el conjunto universo puede cambiar una respuesta?
> Porque la compresión $\{x \in U \mid P(x)\}$ solo admite elementos de $U$. En $\mathbb{N}$, $x^2 = 4$ da $\{2\}$; en $\mathbb{Z}$, da $\{-2, 2\}$.

> [!question]- Dé un ejemplo de un conjunto descrito por compresión que sea vacío.
> $\{x \in \mathbb{N} \mid x < 1\} = \emptyset$, ya que no hay naturales menores que $1$.
