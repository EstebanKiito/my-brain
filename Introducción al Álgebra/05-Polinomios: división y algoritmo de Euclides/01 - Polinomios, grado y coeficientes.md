---
ramo: "Introducción al Álgebra"
tema: "Polinomios: división y algoritmo de Euclides"
tags:
  - intro-algebra/polinomios
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones proposicionales y cuantificadores]]"
---

# Polinomios, grado y coeficientes

Los polinomios son las funciones que se pueden construir con sumas y productos de una variable y constantes. Son el objeto de trabajo del álgebra: se suman, se multiplican y, como se ve en el tema, se dividen como los números enteros.

## Función polinomial

Una **función polinomial** de grado $n$ es una función de la forma

$$
P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0,
$$

donde $n$ es un entero no negativo y $a_n \neq 0$. Los $a_0, a_1, \dots, a_n$ son los **coeficientes**: $a_0$ es el **coeficiente constante** y $a_n$, que acompaña a la mayor potencia, es el **coeficiente principal**. El grado de $P$ es $n$.

> [!tip] Grado y coeficiente principal
> El **grado** es el mayor exponente con coeficiente no nulo; el **coeficiente principal** es el de esa mayor potencia. La función constante $P(x) = 0$ también es polinomio, pero no tiene grado asignado.

Se denota $\mathbb{K}[x]$ al conjunto de los polinomios con coeficientes en el cuerpo $\mathbb{K}$ (por ejemplo $\mathbb{R}[x]$ o $\mathbb{Q}[x]$). Por ejemplo, $P(x) = 1 + x - x^3 + \sqrt{2}\,x^7$ está en $\mathbb{R}[x]$ pero no en $\mathbb{Q}[x]$, porque $\sqrt{2} \notin \mathbb{Q}$.

## Igualdad de polinomios

Dos polinomios $P(x) = \sum a_k x^k$ y $Q(x) = \sum b_k x^k$ son iguales si y solo si $a_k = b_k$ para todo $k$. Coeficiente a coeficiente.

## Grado de la suma y del producto

Para $P, Q \in \mathbb{R}[x]$:

1. $\operatorname{grad}(P + Q) \le \max\{\operatorname{grad}(P), \operatorname{grad}(Q)\}$,
2. $\operatorname{grad}(P \cdot Q) = \operatorname{grad}(P) + \operatorname{grad}(Q)$.

> [!warning] La suma puede bajar de grado
> En $P + Q$ el grado puede ser **menor** que el máximo: los términos principales pueden cancelarse (por ejemplo, $(x^2 + 1) + (-x^2 + 2) = 3$). El producto, en cambio, siempre suma grados.

## Preguntas de repaso

> [!question]- ¿Qué condición define el grado de un polinomio?
> El mayor exponente cuyo coeficiente es distinto de cero. Por eso el polinomio nulo no tiene grado: no tiene ningún coeficiente no nulo.

> [!question]- Identifique grado, coeficiente principal y constante de $7x^4 + x^3 - 3x^2 - 5$.
> Grado $4$; coeficiente principal $7$; coeficiente constante $-5$.

> [!question]- Si $P(x) = D(x) Q(x)$ con $\operatorname{grad}(P) = 9$ y $\operatorname{grad}(D) = 3$, ¿cuánto vale $\operatorname{grad}(Q)$?
> $\operatorname{grad}(Q) = 9 - 3 = 6$, porque el grado del producto es la suma de los grados.

> [!question]- ¿Por qué $\sqrt{2}\,x^7 + 1 \notin \mathbb{Q}[x]$?
> Porque el coeficiente $\sqrt{2}$ no es racional. Los coeficientes deben pertenecer al cuerpo $\mathbb{K}$; aquí $\sqrt{2} \in \mathbb{R}$ pero $\notin \mathbb{Q}$.
