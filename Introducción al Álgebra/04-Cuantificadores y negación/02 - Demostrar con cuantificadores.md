---
ramo: "Introducción al Álgebra"
tema: "Cuantificadores y negación"
tags:
  - intro-algebra/cuantificadores
  - origen/complemento
prerrequisitos:
  - "[[01 - Funciones proposicionales y cuantificadores]]"
---

# Demostrar con cuantificadores

Los teoremas con cuantificadores se demuestran de dos formas simétricas: un "para todo" se prueba tomando un elemento arbitrario, y un "existe" se prueba exhibiendo un elemento concreto. Reconocer cuál es cuál ahorra todo el trabajo.

## Demostrar un "para todo"

Una afirmación $\forall a \in A,\ p(a)$ se demuestra reescribiéndola como una implicación y probándola para un $a$ arbitrario:

$$
a \in A \implies p(a).
$$

**Ejemplo.** Pruebe que para todo $x \in \mathbb{R}\setminus\{0\}$, $x^2 > 0$.

Se toma un $x \neq 0$ arbitrario. Como $x \neq 0$, $x$ es positivo o negativo, y en ambos casos $x^2 > 0$ (el producto de dos números del mismo signo es positivo).

## Demostrar un "existe"

Una afirmación $\exists a \in A,\ p(a)$ se demuestra **exhibiendo** un elemento particular que la cumpla.

**Ejemplo.** Pruebe $\exists n \in \mathbb{Z},\ n^2 = 9$.

Basta notar que $3 \in \mathbb{Z}$ y $3^2 = 9$. El $n = 3$ es el testigo de la existencia.

> [!tip] Los dos movimientos
> Para $\forall$: tome un elemento arbitrario y demuestre la propiedad (no puede elegirlo). Para $\exists$: **exhiba** un elemento que cumpla la propiedad (lo elige usted). Son las dos únicas formas de atacar un cuantificador.

## Cuantificadores mezclados

Muchas afirmaciones combinan ambos cuantificadores. Por ejemplo, "para todo entero $n$, si $n$ es par entonces $n^2$ es par" es una implicación universal $(\forall n \in \mathbb{Z})(n \text{ par} \implies n^2 \text{ par})$. Su hipótesis "$n$ es par" es a su vez un enunciado existencial: $(\exists q \in \mathbb{Z})(n = 2q)$.

Para probarla se toma $n$ arbitrario, se supone $n$ par (existe $q$ con $n = 2q$) y se concluye $n^2 = 4q^2 = 2(2q^2)$, que es par.

## Preguntas de repaso

> [!question]- ¿Qué significa "tomar un elemento arbitrario" al probar un $\forall$?
> Fijar un $x$ cualquiera del dominio, sin suponer nada especial de él, y probar que cumple la propiedad. Como no se usó nada particular, el argumento vale para todos.

> [!question]- ¿Cómo se prueba $\exists n \in \mathbb{Z},\ n^2 = 9$?
> Exhibiendo el testigo $n = 3$: se verifica $3 \in \mathbb{Z}$ y $3^2 = 9$. Un ejemplo que cumpla basta.

> [!question]- ¿Por qué "para todo $x \neq 0$, $x^2 > 0$" se prueba en dos casos?
> Porque un real no nulo es o positivo o negativo. En el primer caso $x^2 > 0$ por producto de positivos; en el segundo, por producto de dos negativos.

> [!question]- En "si $n$ es par, $n^2$ es par", ¿dónde aparece el cuantificador existencial?
> En la hipótesis: "$n$ es par" significa $(\exists q \in \mathbb{Z})(n = 2q)$. Con ese $q$, $n^2 = 4q^2 = 2(2q^2)$ es par.
