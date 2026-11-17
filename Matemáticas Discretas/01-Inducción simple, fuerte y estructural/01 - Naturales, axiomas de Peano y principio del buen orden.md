---
ramo: "Matemáticas Discretas"
tema: "Inducción simple, fuerte y estructural"
tags:
  - discretas/induccion
  - origen/complemento
prerrequisitos: []
---

# Naturales, axiomas de Peano y principio del buen orden

La matemática discreta estudia estructuras que se pueden contar o enumerar, y la más simple de todas es el conjunto de los **números naturales** $\mathbb{N}$. Casi todo el curso (lógica, conjuntos, grafos, algoritmos) se apoya en una propiedad de $\mathbb{N}$ que se deduce de sus axiomas: la inducción.

## Qué son los naturales

Informalmente, $\mathbb{N}$ son los números que sirven para contar los elementos de un conjunto. En este curso el $0$ es natural. Para trabajar con ellos como objeto matemático se fijan unos pocos axiomas, los **axiomas de Peano** (en versión resumida):

1. $0 \in \mathbb{N}$.
2. Si $n \in \mathbb{N}$, entonces su **sucesor** $n + 1 \in \mathbb{N}$.
3. Todo $n \neq 0$ tiene un **antecesor** en $\mathbb{N}$.
4. **Principio del buen orden:** todo subconjunto no vacío de $\mathbb{N}$ tiene un menor elemento.

Los axiomas 1 y 2 dicen que todo natural se alcanza partiendo de $0$ y sumando $1$ muchas veces, y por eso se pueden definir objetos y probar propiedades "paso a paso".

## Principio del buen orden (PBO)

> [!tip] Principio del buen orden
> Si $A \subseteq \mathbb{N}$ y $A \neq \emptyset$, entonces existe $x \in A$ tal que $x \le y$ para todo $y \in A$.

El PBO parece obvio, pero es una propiedad especial de $\mathbb{N}$: no vale en otros conjuntos de números. Basta buscar un subconjunto que "baje sin fin".

## El PBO falla en $\mathbb{Q}$ y en $\mathbb{R}$

Considérese $A = \{x \in \mathbb{Q} \mid x > 0\}$, que no es vacío. Si tuviera un menor elemento $q_0$, entonces $q_0 > 0$ y también $q_0/2 \in A$. Pero $0 < q_0/2 < q_0$, así que $q_0$ no sería el menor: contradicción. Luego $\mathbb{Q}$ no cumple el PBO. La misma demostración funciona en $\mathbb{R}$.

El motivo de fondo es que entre dos racionales siempre hay otro, mientras que en $\mathbb{N}$ cada número tiene un "siguiente" inmediato y no se puede descender indefinidamente.

> [!warning] Antecedente y consecuente
> En una implicación $p \Rightarrow q$, $p$ es el **antecedente** y $q$ el **consecuente**. Muchos principios de este tema (inducción simple y fuerte) son implicaciones cuyo antecedente hay que verificar a mano.

## Por qué importa

El PBO, la inducción simple y la inducción fuerte son tres formas de decir lo mismo sobre $\mathbb{N}$ (se prueba en [[04 - Equivalencia entre buen orden e inducción]]). La inducción es la que más se usa en la práctica, porque convierte una propiedad sobre infinitos números en dos verificaciones finitas. Se desarrolla en [[02 - Inducción simple y caso base distinto de cero]].

## Preguntas de repaso

> [!question]- ¿Qué afirman los axiomas 1 y 2 de Peano en conjunto y qué permiten hacer?
> Que todo natural se obtiene de $0$ aplicando el sucesor una cantidad finita de veces. Eso permite probar propiedades y definir objetos "paso a paso" (inducción y recursión).

> [!question]- ¿Por qué $\{x \in \mathbb{Q} \mid x > 0\}$ muestra que $\mathbb{Q}$ no cumple el buen orden?
> Porque no tiene menor elemento: para cualquier $q_0 > 0$ el número $q_0/2$ es positivo y más chico.

> [!question]- ¿Por qué $\mathbb{Z}$ tampoco cumple el buen orden?
> Porque el propio $\mathbb{Z}$ es un subconjunto no vacío sin menor elemento: siempre hay un entero más negativo. El PBO se salva en $\mathbb{N}$ porque está acotado inferiormente por $0$.
