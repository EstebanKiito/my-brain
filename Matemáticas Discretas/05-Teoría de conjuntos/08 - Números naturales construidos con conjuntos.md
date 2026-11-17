---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[02 - El conjunto vacío y su unicidad]]"
  - "[[04 - Unión, intersección, diferencia y conjunto potencia]]"
  - "[[05 - Definiciones inductivas y listas enlazadas]]"
  - "[[06 - Inducción estructural]]"
---

# Números naturales construidos con conjuntos

Con solo el conjunto vacío y la unión se pueden fabricar **todos** los números naturales. Esto no es un truco: muestra que la teoría de conjuntos basta como cimiento de la aritmética, y que las definiciones inductivas del tema de inducción ([[05 - Definiciones inductivas y listas enlazadas]]) se pueden realizar con objetos concretos.

## El operador sucesor

Se define $\delta(x) = x \cup \{x\}$: agrega a $x$ un nuevo elemento, el propio $x$. Se declara $0 = \varnothing$ y se aplica $\delta$ repetidamente:

| Número | Construcción | Como conjunto |
|---|---|---|
| $0$ | $\varnothing$ | $\varnothing$ |
| $1$ | $\delta(0) = \varnothing \cup \{\varnothing\}$ | $\{\varnothing\}$ |
| $2$ | $\delta(1) = \{\varnothing\} \cup \{\{\varnothing\}\}$ | $\{\varnothing, \{\varnothing\}\}$ |
| $3$ | $\delta(2)$ | $\{\varnothing, \{\varnothing\}, \{\varnothing, \{\varnothing\}\}\}$ |

Observando la tercera columna: $1 = \{0\}$, $2 = \{0, 1\}$, $3 = \{0, 1, 2\}$ y, en general, $n = \{0, 1, \dots, n-1\}$, un conjunto con exactamente $n$ elementos. Así, $m < n$ equivale a $m \in n$.

> [!tip] Definición inductiva de $\mathbb{N}$
> $\mathbb{N}$ es el **menor** conjunto tal que $\varnothing \in \mathbb{N}$ y, si $n \in \mathbb{N}$, entonces $\delta(n) \in \mathbb{N}$. Solo con $\varnothing$ y $\delta$ se obtiene todo $\mathbb{N}$.

"Menor" significa que no hay más elementos que los generados por estas reglas, lo que habilita la inducción estructural sobre $\mathbb{N}$.

## Aritmética definida por recursión

Con $\delta$ como sucesor, la suma se define por recursión sobre el segundo argumento:
$$\text{sum}(m, 0) = m, \qquad \text{sum}(m, \delta(n)) = \delta(\text{sum}(m, n)).$$

**Ejemplo: $\text{sum}(3, 4) = 7$.** Se baja el segundo argumento hasta $0$ y luego se sube aplicando $\delta$:
$$\text{sum}(3,4) = \delta(\text{sum}(3,3)) = \delta\delta(\text{sum}(3,2)) = \delta\delta\delta(\text{sum}(3,1)) = \delta\delta\delta\delta(\text{sum}(3,0)) = \delta\delta\delta\delta(3) = 7.$$

La multiplicación se define con la suma: $\text{mult}(m, 0) = 0$ y $\text{mult}(m, \delta(n)) = \text{sum}(m, \text{mult}(m, n))$. Así, $\text{mult}(3, 2) = \text{sum}(3, \text{mult}(3,1)) = \text{sum}(3, \text{sum}(3, 0)) = \text{sum}(3, 3) = 6$.

## Una propiedad por inducción estructural: la suma es asociativa

Se prueba $\text{sum}(\text{sum}(a,b), c) = \text{sum}(a, \text{sum}(b, c))$ por inducción sobre $c$, con $a$ y $b$ fijos:

- **Base** ($c = 0$): ambos lados valen $\text{sum}(a, b)$, porque $\text{sum}(x, 0) = x$.
- **HI:** vale para $c$.
- **Paso:** $\text{sum}(\text{sum}(a,b), \delta(c)) = \delta(\text{sum}(\text{sum}(a,b), c)) \overset{\text{HI}}{=} \delta(\text{sum}(a, \text{sum}(b, c))) = \text{sum}(a, \delta(\text{sum}(b,c))) = \text{sum}(a, \text{sum}(b, \delta(c)))$.

Cada igualdad usa la segunda regla de $\text{sum}$ (hacia un lado o hacia el otro) o la HI.

## $\mathbb{N}$ no tiene predecesor "de conjuntos"

Como ningún conjunto se pertenece a sí mismo (la paradoja de Russell obliga a cuidar esto; ver [[03 - Axioma de abstracción, paradoja de Russell y separación]]), no existe un conjunto $A$ con $\delta(A) = \mathbb{N}$. En efecto, $A \cup \{A\} = \mathbb{N}$ daría $A \in \mathbb{N}$, y como $\mathbb{N}$ es cerrado bajo $\delta$, $A \cup \{A\} \in \mathbb{N}$, o sea $\mathbb{N} \in \mathbb{N}$: imposible.

## Preguntas de repaso

> [!question]- ¿Por qué $n = \{0, 1, \dots, n-1\}$ tiene exactamente $n$ elementos?
> Porque cada $\delta$ agrega un elemento nuevo (el conjunto anterior) que no estaba antes; por inducción, $\delta(n)$ tiene un elemento más que $n$.

> [!question]- ¿Qué papel cumple la palabra "menor" en la definición de $\mathbb{N}$?
> Garantiza que no hay elementos extra además de $\varnothing$ y sus sucesores, que es lo que permite demostrar propiedades por inducción.

> [!question]- ¿Por qué la prueba de asociatividad induce sobre $c$ y no sobre $a$?
> Porque la suma se define por recursión sobre su **segundo** argumento; inducir sobre $c$ permite desplegar $\text{sum}(\cdot, \delta(c))$ con la definición.
