---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[01 - Pertenencia, inclusión y axioma de extensión]]"
  - "[[02 - El conjunto vacío y su unicidad]]"
---

# Axioma de abstracción, paradoja de Russell y separación

Definir un conjunto por una propiedad, $\{x \mid \varphi(x)\}$, es la forma más natural de hacerlo. La pregunta es si **cualquier** propiedad sirve. La respuesta es no, y entender por qué muestra el cuidado con que se escriben los axiomas de la teoría.

## Dos formas de definir un conjunto

- **Por extensión**: se listan los elementos, $\mathbb{Z}_5 = \{0,1,2,3,4\}$.
- **Por comprensión**: se da una propiedad, $\mathbb{Z}_5 = \{x \mid x \in \mathbb{N} \wedge x < 5\}$.

La primera sirve solo para colecciones pequeñas o con patrón evidente; la segunda permite describir conjuntos infinitos y es la que genera problemas.

## El axioma de abstracción, demasiado permisivo

> [!tip] Axioma de abstracción (ingenuo)
> Si $\varphi$ es una propiedad sobre objetos, $A = \{x \mid \varphi(x)\}$ es un conjunto y $x \in A \leftrightarrow \varphi(x)$.

Con él, a cada propiedad le corresponde un conjunto. Sirve para definir el vacío ($\varnothing = \{x \mid x \neq x\}$), pero también admite propiedades sobre conjuntos "enormes", como "ser un conjunto con más de tres elementos", "ser un conjunto finito" o "ser un conjunto infinito". Con ellas se pueden armar conjuntos que se contienen a sí mismos o no:

| Conjunto | Contiene... | ¿Se pertenece a sí mismo? |
|---|---|---|
| $A_1$: conjuntos con más de 3 elementos | muchísimos conjuntos | sí, $A_1$ tiene más de 3 elementos |
| $A_2$: conjuntos finitos | infinitos conjuntos finitos | no, $A_2$ es infinito |
| $A_3$: conjuntos infinitos | | sí, $A_3$ es infinito |

Tiene entonces sentido la propiedad $\varphi(x) : x \notin x$, que cumplen los conjuntos que no se contienen a sí mismos (por ejemplo $A_2$).

## La paradoja de Russell

Por abstracción existiría el conjunto
$$R = \{x \mid x \notin x\}.$$
Preguntando si $R \in R$: por definición de $R$, $R \in R$ ocurre exactamente cuando $R$ cumple la propiedad, es decir, cuando $R \notin R$. Queda
$$R \in R \leftrightarrow R \notin R,$$
una contradicción (como "el barbero que afeita a todos los que no se afeitan a sí mismos": ¿se afeita a sí mismo?). Bertrand Russell la descubrió en 1901, justo cuando Frege terminaba una obra que tomaba el axioma de abstracción como base, y obligó a rehacer los cimientos.

> [!warning] ¿Dónde está el error?
> No está en el razonamiento sobre $R$, sino en el axioma: no toda propiedad define un conjunto. El problema son las colecciones "demasiado grandes", como la de **todos** los conjuntos.

## El axioma de separación

La solución es restringir el axioma: solo se permite filtrar elementos de un conjunto que **ya existe**.

> [!tip] Axioma de separación
> Si $\varphi$ es una propiedad y $C$ es un conjunto "sano" (no creado por abstracción), entonces $\{x \mid x \in C \wedge \varphi(x)\}$ es un conjunto: se **separan** de $C$ los elementos que cumplen $\varphi$.

Con esto el intento de definir $R$ queda como $\{x \in C \mid x \notin x\}$, que ya no produce contradicción. En la práctica, cuando se escribe $\{x \mid \varphi(x)\}$ sin más, se entiende que los $x$ se toman de un **universo** sano $U$ que se deduce del contexto: $\{x \mid x \in U \wedge \varphi(x)\}$.

Las teorías modernas agregan otros axiomas (pares, uniones, conjunto potencia, regularidad, reemplazo) y no se conoce ninguna contradicción en ellas; en cambio, Gödel demostró que la matemática no puede probar su propia consistencia desde dentro.

## Preguntas de repaso

> [!question]- ¿Por qué $R \in R$ lleva a contradicción y $R \notin R$ también?
> Si $R \in R$, entonces $R$ cumple $x \notin x$, o sea $R \notin R$. Si $R \notin R$, entonces cumple la propiedad que define a $R$, luego $R \in R$. Ambas suposiciones se refutan a sí mismas.

> [!question]- ¿Qué restringe el axioma de separación respecto al de abstracción?
> Exige partir de un conjunto $C$ ya existente y solo filtrar sus elementos, en vez de reunir todos los objetos que cumplen una propiedad.

> [!question]- ¿Por qué se puede definir $\mathbb{Z}_5 = \{x \in \mathbb{N} \mid x < 5\}$ sin problemas?
> Porque filtra elementos de $\mathbb{N}$, un conjunto sano, con una propiedad concreta; no se está formando una colección arbitrariamente grande.
