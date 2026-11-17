---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[01 - Pertenencia, inclusión y axioma de extensión]]"
---

# El conjunto vacío y su unicidad

Una teoría necesita un punto de partida: algún objeto cuya existencia se asegura sin construirlo. En teoría de conjuntos ese punto de partida es el **conjunto vacío**, y de él se obtienen, junto con las operaciones, todos los demás conjuntos (incluidos los naturales). Además es la primera oportunidad de ver dos formas de demostración típicas del tema: la verdad por vacuidad y la unicidad.

## Axioma del conjunto vacío

> [!tip] Axioma del conjunto vacío
> Existe un conjunto sin elementos: $\exists X\ \forall x\ (x \notin X)$. Se denota $\varnothing$ o $\{\}$.

El axioma solo dice que existe al menos uno. Que sea **el** vacío requiere un teorema.

## Dos teoremas

**Teorema 1.** Para todo conjunto $A$, $\varnothing \subseteq A$.

*Demostración.* Hay que probar $\forall x\,(x \in \varnothing \to x \in A)$. La premisa $x \in \varnothing$ es siempre falsa, y una implicación con premisa falsa es verdadera. Por tanto se cumple **por vacuidad**: no hay ningún elemento que revisar.

**Teorema 2.** Existe un único conjunto vacío.

*Demostración.* Sean $A$ y $B$ conjuntos vacíos. Por el teorema 1, $A \subseteq B$ (pues $A$ es vacío) y, simétricamente, $B \subseteq A$. Por doble inclusión, $A = B$.

> [!warning] Vacuidad no es "no se puede demostrar"
> Que $\varnothing \subseteq A$ sea cierto no significa que el vacío "tenga algo dentro": significa que **no tiene nada que contradiga** la inclusión. Es la misma razón por la que "todos los unicornios de esta sala son azules" es verdadera si no hay unicornios.

## Otras formas de describirlo

Por comprensión, el vacío es el conjunto de los objetos que cumplen una propiedad imposible, por ejemplo $\{x \mid x \neq x\}$. También se tiene que $\varnothing \in \mathcal{P}(A)$ para todo $A$ (porque $\varnothing \subseteq A$), y que $\varnothing \neq \{\varnothing\}$: el primero no tiene elementos y el segundo tiene exactamente uno.

| Conjunto | Elementos | ¿Cuántos? |
|---|---|---|
| $\varnothing$ | ninguno | $0$ |
| $\{\varnothing\}$ | $\varnothing$ | $1$ |
| $\{\varnothing, \{\varnothing\}\}$ | $\varnothing$ y $\{\varnothing\}$ | $2$ |

Esta tabla es el comienzo de la construcción de los naturales (ver [[08 - Números naturales construidos con conjuntos]]).

## Cómo se prueba una unicidad

El esquema del teorema 2 se repite en todo el curso: se suponen **dos** objetos con la propiedad, se deduce que son iguales y se concluye. Formalmente es probar
$$\forall A\,\forall B\,(A \text{ es vacío} \wedge B \text{ es vacío} \to A = B).$$
La forma alternativa es suponer que son distintos y llegar a una contradicción, que es esencialmente el mismo argumento.

## Preguntas de repaso

> [!question]- ¿Por qué $\varnothing \subseteq A$ es verdadero aunque $\varnothing$ no tenga elementos?
> Porque la inclusión es un "para todo $x \in \varnothing$": al no existir tales $x$, no hay contraejemplo posible y la afirmación se cumple por vacuidad.

> [!question]- ¿Qué parte de la demostración de unicidad usa el axioma de extensión?
> El paso final: de $A \subseteq B$ y $B \subseteq A$ se concluye $A = B$, que es la caracterización de la igualdad por extensión.

> [!question]- ¿Por qué $\varnothing \neq \{\varnothing\}$?
> $\{\varnothing\}$ tiene un elemento ($\varnothing$) y $\varnothing$ no tiene ninguno; por extensión, difieren en que $\varnothing \in \{\varnothing\}$ pero $\varnothing \notin \varnothing$.
