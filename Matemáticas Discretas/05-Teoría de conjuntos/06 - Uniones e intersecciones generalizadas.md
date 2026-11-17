---
ramo: "Matemáticas Discretas"
tema: "Teoría de conjuntos"
tags:
  - discretas/conjuntos
  - origen/complemento
prerrequisitos:
  - "[[04 - Unión, intersección, diferencia y conjunto potencia]]"
  - "[[05 - Leyes de la teoría de conjuntos y demostración por doble inclusión]]"
---

# Uniones e intersecciones generalizadas

La unión y la intersección binarias se encadenan sin problema para tres o cuatro conjuntos, pero no sirven para "unir infinitos conjuntos" ni para unir los miembros de una familia cualquiera. Las operaciones **generalizadas** resuelven esto: en vez de dos argumentos reciben un **conjunto de conjuntos** $S$.

## Definiciones

> [!tip] Unión e intersección generalizadas
> $\displaystyle\bigcup S = \{x \mid \exists A \in S\ (x \in A)\}$ (los elementos que están en **algún** conjunto de $S$).
> $\displaystyle\bigcap S = \{x \mid \forall A \in S\ (x \in A)\}$ (los elementos que están en **todos** los conjuntos de $S$).

La unión corresponde a un $\exists$ (como $\vee$) y la intersección a un $\forall$ (como $\wedge$). Se escribe también $\bigcup_{A \in S} A$ y $\bigcap_{A \in S} A$.

Ejemplo: con $S = \{\{1,2,3\},\{2,3,4\},\{3,4,5\}\}$ se tiene $\bigcup S = \{1,2,3,4,5\}$ y $\bigcap S = \{3\}$.

## Colecciones indexadas

Si los conjuntos se numeran, $S = \{A_0, A_1, \dots, A_{n-1}\}$, entonces
$$\bigcup S = \bigcup_{i=0}^{n-1} A_i, \qquad x \in \bigcup_{i=0}^{n-1} A_i \leftrightarrow \exists i\,(0 \le i < n \wedge x \in A_i),$$
y la intersección usa $\forall i$. Con una colección **infinita** $S = \{A_0, A_1, \dots\}$ se escribe $\bigcup_{i=0}^{\infty} A_i$ y $x \in \bigcup_{i \in \mathbb{N}} A_i \leftrightarrow \exists i \in \mathbb{N}\,(x \in A_i)$; análogamente para la intersección con $\forall i \in \mathbb{N}$.

**Ejemplo con intervalos.** Sea $A_i = \left(-\tfrac{1}{i}, \tfrac{1}{i}\right)$ para $i \ge 1$ (los intervalos se achican hacia $0$).

- $\bigcup_{i \ge 1} A_i = (-1, 1)$: el primero, $A_1$, contiene a todos los demás.
- $\bigcap_{i \ge 1} A_i = \{0\}$: el $0$ está en todos; en cambio, un $x \neq 0$ queda fuera en cuanto $1/i \le |x|$.

Esto muestra que la intersección de infinitos conjuntos "abiertos" puede dejar de ser abierta: un detalle que los números reales hacen visible.

## Casos extremos y propiedades

- $\bigcup \varnothing = \varnothing$: no hay conjuntos que aporten elementos.
- $\bigcap \varnothing$ es, por convención lógica, **todo el universo** $U$: la condición "$\forall A \in \varnothing\ (x \in A)$" se cumple por vacuidad para cualquier $x$. Por eso la intersección generalizada se usa solo con $S \neq \varnothing$.
- Se mantienen las leyes de De Morgan generalizadas: $\left(\bigcup_{A \in S} A\right)^c = \bigcap_{A \in S} A^c$ y $\left(\bigcap_{A \in S} A\right)^c = \bigcup_{A \in S} A^c$, que son la negación de $\exists$ y de $\forall$.
- Si $S \subseteq \mathcal{P}(A)$, $\bigcup S \subseteq A$ (la unión de subconjuntos de $A$ sigue dentro de $A$).

> [!warning] $\bigcup S$ no es $S$
> $S$ es un conjunto cuyos **elementos son conjuntos**; $\bigcup S$ "abre" esos conjuntos y junta lo que hay dentro. En el ejemplo, $S$ tiene $3$ elementos y $\bigcup S$ tiene $5$.

## Para qué sirven

Las generalizadas permiten enunciar y probar propiedades de familias de conjuntos: por ejemplo, que la unión de una familia de conjuntos con complemento finito mantiene esa propiedad, o que una partición cubre el conjunto ($\bigcup S = A$). También definen espacios más abstractos, como las topologías, cuyos axiomas piden cerrar bajo uniones arbitrarias e intersecciones finitas.

## Preguntas de repaso

> [!question]- ¿Por qué la unión generalizada usa $\exists$ y la intersección usa $\forall$?
> Estar en la unión pide pertenecer a alguno de los conjuntos y estar en la intersección pide pertenecer a todos; son los análogos de $\vee$ y $\wedge$ para más de dos conjuntos.

> [!question]- ¿Cuánto vale $\bigcap_{i \ge 1}\left(-\tfrac1i, \tfrac1i\right)$ y por qué?
> $\{0\}$: el cero está en todos los intervalos y cualquier $x \neq 0$ sale de ellos cuando $1/i \le |x|$.

> [!question]- ¿Qué pasa con $\bigcap \varnothing$?
> La condición se cumple por vacuidad para todo $x$, así que daría el universo; por eso en la práctica se exige que la familia sea no vacía.

> [!question]- ¿Cómo se niega $\bigcup_{A \in S} A$?
> Cambiando $\exists$ por $\forall$ y complementando: $\left(\bigcup A\right)^c = \bigcap A^c$, la ley de De Morgan generalizada.
