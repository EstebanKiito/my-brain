---
ramo: "Matemáticas Discretas"
tema: "Inducción simple, fuerte y estructural"
tags:
  - discretas/induccion
  - discretas/recursion
  - origen/complemento
prerrequisitos:
  - "[[05 - Definiciones inductivas y listas enlazadas]]"
---

# Inducción estructural

Cuando un conjunto se define por inducción, las demostraciones sobre él siguen la misma forma que la definición: un caso por cada elemento base y uno por cada regla de construcción. Eso es la **inducción estructural**, y generaliza la inducción simple (que es el caso del conjunto $\mathbb{N}$ con el sucesor como única regla).

## El principio

> [!tip] Principio de inducción estructural
> Sea $A$ un conjunto definido inductivamente y $P$ una propiedad sobre sus elementos. Si **(1)** todos los elementos base cumplen $P$ y **(2)** para cada regla de construcción, aplicada a elementos que cumplen $P$, el resultado también cumple $P$, entonces todo elemento de $A$ cumple $P$.

La hipótesis de inducción es "los elementos de entrada de la regla cumplen $P$" y la tesis es "el elemento construido cumple $P$".

## Ejemplo: flechas y elementos

Propiedad $P(L)$: *$L$ tiene tantas flechas como elementos.*

- **Base:** $\emptyset$ no tiene flechas ni elementos.
- **HI:** una lista $L$ cualquiera tiene tantas flechas como elementos.
- **TI:** $L \to k$ agrega exactamente una flecha y un elemento más que $L$; luego mantiene la igualdad.

Por inducción estructural, todas las listas de $L_\mathbb{N}$ cumplen $P$.

## Ejemplo mayor: igualdad por sufijo y suma

> [!tip] Teorema
> Si $L_1, L_2 \neq \emptyset$, entonces $L_1 = L_2$ si y solo si $\mathrm{suf}(L_1) = \mathrm{suf}(L_2)$ y $\mathrm{sum}(L_1) = \mathrm{sum}(L_2)$.

La dirección ($\Rightarrow$) es inmediata (listas iguales tienen sufijos y sumas iguales). Para ($\Leftarrow$), por inducción estructural:

- **Base:** $L_1 = \to k$ y $L_2 = \to j$. Como $\mathrm{sum}(\to k) = k$ y $\mathrm{sum}(\to j) = j$, de $\mathrm{sum}(L_1) = \mathrm{sum}(L_2)$ sale $k = j$, y por tanto $L_1 = L_2$.
- **HI:** para listas $L_1, L_2$ cualesquiera, si $\mathrm{suf}(L_1) = \mathrm{suf}(L_2)$ y $\mathrm{sum}(L_1) = \mathrm{sum}(L_2)$, entonces $L_1 = L_2$.
- **TI:** se toman $L_1 \to k$ y $L_2 \to j$ con sufijos y sumas iguales. Por definición, $\mathrm{suf}(L_1) \to k = \mathrm{suf}(L_2) \to j$ y $\mathrm{sum}(L_1) + k = \mathrm{sum}(L_2) + j$. Por igualdad de listas, $\mathrm{suf}(L_1) = \mathrm{suf}(L_2)$ y $k = j$; de ahí $\mathrm{sum}(L_1) = \mathrm{sum}(L_2)$. La HI da $L_1 = L_2$ y entonces $L_1 \to k = L_2 \to j$.

> [!warning] Cuidado con la HI en implicaciones
> Cuando la propiedad es una implicación, la HI es también una implicación: su antecedente no tiene por qué cumplirse. Hay que **probar** que se cumple (aquí, con la igualdad de listas) antes de usar la conclusión.

## Receta

1. Identificar el conjunto y sus reglas (casos base y reglas de construcción).
2. Probar la propiedad en **cada** caso base.
3. Para **cada** regla, suponer la propiedad en los elementos de entrada (HI) y probarla en el elemento construido (TI).

Más adelante la misma receta sirve para árboles, fórmulas lógicas y estructuras recursivas en general.

## Preguntas de repaso

> [!question]- ¿Por qué la inducción simple es un caso particular de la estructural?
> Porque $\mathbb{N}$ se define inductivamente con un caso base ($0$) y una única regla (el sucesor), así que el principio estructural coincide con el simple.

> [!question]- Si un conjunto tiene dos reglas de construcción, ¿cuántos pasos inductivos hay que probar?
> Dos: uno por regla (más los casos base).

> [!question]- ¿Cuál es la diferencia entre la HI y la tesis en una propiedad sobre listas?
> La HI es que $L$ cumple $P$; la tesis es que $L \to k$ cumple $P$.
