---
ramo: "Introducción al Álgebra"
tema: "Técnicas de demostración e inducción"
tags:
  - intro-algebra/tecnicas-demostracion
  - origen/complemento
prerrequisitos:
  - "[[02 - Contraejemplos]]"
---

# Principio de inducción matemática

Para probar que una propiedad vale para *todos* los naturales no alcanza con verificar casos uno por uno: son infinitos. La **inducción matemática** resuelve esto con dos pasos finitos: mostrar que vale para el $1$ y mostrar que, si vale para un $k$ cualquiera, entonces vale para su sucesor $k+1$.

## Por qué comprobar casos no basta

Para un valor concreto, como $n = 8$, se puede verificar la afirmación con un cálculo. Pero por muchos casos que se comprueben numéricamente, nunca se sabrá que vale para *todos* los naturales: siempre queda un número más grande sin verificar. Lo que distingue a los naturales es que se pueden recorrer a partir del $1$ sumando $1$ repetidamente, y la inducción es justamente la formalización de ese hecho.

## El principio de inducción

> [!tip] Principio de inducción
> Sea $P(n)$ una afirmación que depende del natural $n$. Entonces $P(n)$ es verdadera para todo $n \in \mathbb{N}$ si se cumplen:
>
> 1. **Caso base:** $P(1)$ es verdadera.
> 2. **Paso inductivo:** $P(k) \Rightarrow P(k+1)$ para todo natural $k$.

El paso inductivo no pide probar $P(k+1)$ "de la nada": se *supone* $P(k)$ verdadera (la **hipótesis de inducción**) y, a partir de ella, se deduce $P(k+1)$.

## La metáfora del dominó

Si los naturales son fichas de dominó alineadas, el caso base es tumbar la primera ficha y el paso inductivo es que cada ficha, al caer, tumba la siguiente. Con ambas cosas, todas caen: $P(1)$ es cierta, $P(1) \Rightarrow P(2)$ da $P(2)$, $P(2) \Rightarrow P(3)$ da $P(3)$, y así sucesivamente.

## Ejemplo: $n \le 2^n$

Pruebe que $n \le 2^n$ para todo $n \in \mathbb{N}$.

**Demostración por inducción sobre $n$.**

- **Caso base** ($n=1$): $1 \le 2^1 = 2$, verdadero.
- **Paso inductivo:** supongamos que $k \le 2^k$ (hipótesis de inducción). Entonces

$$
k+1 \le 2^k + 1 \le 2^k + 2^k = 2 \cdot 2^k = 2^{k+1},
$$

donde la segunda desigualdad usa que $1 \le 2^k$ para $k \ge 1$. Luego $P(k+1)$ es verdadera.

Por inducción, $n \le 2^n$ para todo $n \in \mathbb{N}$.

> [!warning] No se "verifican" infinitos casos
> El paso inductivo demuestra $P(k) \Rightarrow P(k+1)$ de **una** vez para un $k$ genérico, no caso a caso. Es la diferencia entre "comprobar" (finito) y "demostrar" (todos).

## Preguntas de repaso

> [!question]- ¿Cuáles son las dos condiciones del principio de inducción?
> El caso base $P(1)$ y el paso inductivo $P(k) \Rightarrow P(k+1)$ para todo natural $k$. Con ambas se concluye $P(n)$ para todo $n \in \mathbb{N}$.

> [!question]- ¿Qué es la hipótesis de inducción?
> La suposición, dentro del paso inductivo, de que $P(k)$ es verdadera. Se usa como puente para demostrar $P(k+1)$.

> [!question]- En el ejemplo $n \le 2^n$, ¿dónde se usó la hipótesis de inducción?
> En el primer paso de la cadena: se reemplazó $k$ por $2^k$ gracias a que $k \le 2^k$. Después solo se sumó y se agrupó para llegar a $2^{k+1}$.

> [!question]- ¿Por qué la inducción no funciona si falta el caso base?
> Porque el paso inductivo solo dice "si cae la ficha $k$, cae la $k+1$". Sin tumbar la primera ficha, esa cadena nunca arranca: no hay ningún $P(k)$ del que partir.
