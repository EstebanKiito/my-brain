---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/ordenes
  - origen/complemento
prerrequisitos:
  - "[[03 - Órdenes parciales y totales]]"
  - "[[04 - Diagramas de Hasse y retículos]]"
---

# Cotas, elementos minimales y mínimos

En un orden total, "el menor" de un conjunto es un concepto claro. En un orden parcial hay tres ideas distintas que se confunden con facilidad: una cota (un elemento que está debajo de todos, sin importar si pertenece al conjunto), un elemento minimal (nada del conjunto queda debajo) y un mínimo (el menor de todos y además del conjunto). Entenderlas por separado evita la mayoría de los errores.

## Definiciones

Sea $(A,\preceq)$ un orden parcial, $S \subseteq A$ y $x \in A$.

| Concepto | Condición |
|---|---|
| $x$ es **cota inferior** de $S$ | $x \preceq y$ para todo $y \in S$ ($x$ puede no estar en $S$) |
| $x$ es **minimal** de $S$ | $x \in S$ y, para todo $y \in S$, $y \preceq x \Rightarrow y = x$ |
| $x$ es **mínimo** de $S$ | $x \in S$ y $x$ es cota inferior de $S$ |

Los conceptos duales son **cota superior**, **maximal** y **máximo**, invirtiendo el orden.

> [!tip] Minimal frente a mínimo
> Mínimo = **está en $S$ y es menor que todos**. Minimal = **está en $S$ y nadie de $S$ es estrictamente menor**. Todo mínimo es minimal, pero un minimal puede no ser mínimo. En un orden total ambos coinciden.

## Ejemplo con divisibilidad

En $(\mathbb{N}\setminus\{0\},\mid)$ sea $S = \{2,3,5,10,15,20\}$.
- **Cotas inferiores:** $1$ (divide a todos). El $2$ no sirve: $2 \nmid 3$.
- **Cotas superiores:** $60$, el mínimo común múltiplo, y cualquier múltiplo de $60$ ($120$, $180$, …).
- **Minimales:** $2$, $3$ y $5$, porque ningún otro elemento de $S$ los divide.
- **Maximales:** $15$ y $20$, que no dividen a ningún otro elemento de $S$. En cambio $10$ no es maximal porque divide a $20$.
- **Mínimo y máximo:** no hay, porque las cotas ($1$ y $60$) no pertenecen a $S$.

## Ejemplo con inclusión

En $(\mathcal{P}(\{1,2,3,4\}),\subseteq)$ sea $S = \{\{1\},\{1,2\},\{1,3\},\{1,2,3,4\}\}$.
- $\{1\}$ es cota inferior, minimal y **mínimo**; $\emptyset$ también es cota inferior.
- $\{1,2,3,4\}$ es cota superior, maximal y **máximo**; no hay otras cotas superiores porque el orden vive dentro de $\mathcal{P}(\{1,2,3,4\})$.
- $\{1,2\}$ y $\{1,3\}$ no son minimales ni maximales: tienen a $\{1\}$ debajo y a $\{1,2,3,4\}$ encima.

## Todos minimales y maximales a la vez

Basta tomar elementos incomparables entre sí, que forman una **anticadena**: $S = \{2,3,5\}$ en la divisibilidad, o $S = \{\{1\},\{2\},\{3\},\{4\}\}$ en la inclusión. Ninguno es menor que otro, así que todos son minimales y maximales.

## Unicidad del mínimo

> [!tip] Teorema
> Si $S$ tiene mínimo, es único (y análogamente el máximo). Se anota $\min(S)$ y $\max(S)$.

Si $s_1$ y $s_2$ son mínimos de $S$, ambos están en $S$ y cada uno es cota inferior del otro: $s_1 \preceq s_2$ y $s_2 \preceq s_1$. Por antisimetría, $s_1 = s_2$. Esto no se extiende a los minimales: $\{2,3,5\}$ tiene tres.

## Preguntas de repaso

> [!question]- ¿Por qué un mínimo siempre es minimal?
> Si $x$ es mínimo y $y \in S$ cumple $y \preceq x$, también $x \preceq y$ (por ser cota inferior), y la antisimetría da $y = x$.

> [!question]- ¿Puede un conjunto no vacío tener varios minimales y aun así tener mínimo?
> No. Si hay mínimo, es menor que cualquier otro elemento, así que ningún otro elemento puede ser minimal.

> [!question]- ¿Por qué $\emptyset$ es cota inferior de $S = \{\{1\},\{1,2\}\}$ pero no es su mínimo?
> Es menor que todos los elementos de $S$, pero no pertenece a $S$, y el mínimo debe ser un elemento de $S$.

> [!question]- ¿Existe un conjunto de $(\mathbb{Z},\le)$ no vacío sin mínimo?
> Sí, el propio $\mathbb{Z}$ o $\{x \in \mathbb{Z} \mid x < 0\}$: el orden es total pero no tiene primer elemento. En $\mathbb{N}$, en cambio, todo subconjunto no vacío tiene mínimo.
