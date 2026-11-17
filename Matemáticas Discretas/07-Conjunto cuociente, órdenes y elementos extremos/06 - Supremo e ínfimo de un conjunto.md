---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/ordenes
  - origen/complemento
prerrequisitos:
  - "[[05 - Cotas elementos minimales y mínimos]]"
---

# Supremo e ínfimo de un conjunto

Muchos conjuntos no tienen mínimo ni máximo y, sin embargo, tienen un "borde" natural: el intervalo $(0,1)$ no incluye al $0$ ni al $1$, pero igual se acerca a ellos. El **ínfimo** y el **supremo** extienden el mínimo y el máximo a ese borde, que puede quedar fuera del conjunto.

## Definición

Sea $(A,\preceq)$ un orden parcial y $S \subseteq A$.

> [!tip] Supremo e ínfimo
> El **ínfimo** $\inf(S)$ es la **mayor cota inferior** de $S$: es cota inferior y toda otra cota inferior $s'$ cumple $s' \preceq \inf(S)$. El **supremo** $\sup(S)$ es la **menor cota superior**.

Se obtienen así en dos pasos: primero se juntan todas las cotas inferiores (o superiores) y después se busca la mayor (o la menor) entre ellas, que debe estar dentro del conjunto de cotas.

**Ejemplos.**
- En $(\mathbb{R},\le)$, $S = (0,1)$ no tiene mínimo ni máximo, pero $\inf S = 0$ y $\sup S = 1$.
- En $(\mathbb{N}\setminus\{0\},\mid)$ con $S = \{2,3,5,10,15,20\}$: las cotas superiores son los múltiplos de $60$ y la menor es $60$, así que $\sup S = 60 = \operatorname{mcm}(S)$; la única cota inferior es $1$, por lo que $\inf S = 1 = \operatorname{mcd}(S)$.
- En $(\mathcal{P}(A),\subseteq)$, para una familia $\mathcal{B}$, $\sup\mathcal{B} = \bigcup\mathcal{B}$ e $\inf\mathcal{B} = \bigcap\mathcal{B}$: la unión es cota superior porque contiene a cada miembro y es la menor porque toda cota superior contiene a todos y por tanto a su unión.

## Unicidad

> [!tip] Teorema
> Si $S$ tiene supremo (o ínfimo), es único.

Si $s_1$ y $s_2$ son supremos, ambos son cotas superiores. Como $s_1$ es la **menor** cota superior, $s_1 \preceq s_2$; por simetría del argumento, $s_2 \preceq s_1$. Por antisimetría, $s_1 = s_2$. Gracias a esto se habla de **el** supremo y **el** ínfimo.

## Relación con máximo y mínimo

Si $S$ tiene máximo, ese máximo es el supremo (es cota superior y es menor o igual que toda otra cota superior). La recíproca falla: $(0,1)$ tiene supremo $1$ y ningún máximo. Con $S = \{\{1\},\{2\},\{1,2\},\{1,3\}\}$ en $(\mathcal{P}(\{1,2,3\}),\subseteq)$ se obtiene $\sup S = \{1,2,3\}$, que no está en $S$, e $\inf S = \emptyset$.

| Concepto | ¿Pertenece a $S$? | ¿Siempre existe? |
|---|---|---|
| mínimo / máximo | sí, obligatorio | no |
| ínfimo / supremo | no necesariamente | no |

> [!warning] El supremo vive en el conjunto del orden
> El supremo debe ser un elemento de $A$, no de "algún conjunto mayor". En $(\mathbb{Q},\le)$, $\{q \mid q^2 \le 2\}$ no tiene supremo porque $\sqrt2 \notin \mathbb{Q}$ (véase [[07 - Órdenes completos y el caso de los racionales]]).

En un orden **total**, todo conjunto finito y no vacío tiene supremo e ínfimo, y pertenecen al conjunto (son su máximo y su mínimo). En uno parcial, incluso un conjunto de dos elementos puede no tenerlos.

## Preguntas de repaso

> [!question]- ¿Por qué el ínfimo no tiene que ser un elemento de $S$?
> Se define por comparación con otras cotas inferiores, no por pertenecer a $S$; si perteneciera, sería además el mínimo.

> [!question]- ¿Qué tienen en común el supremo de $\{a,b\}$ en la divisibilidad y en la inclusión?
> En ambos es la menor cota superior común: el mínimo común múltiplo y la unión, respectivamente.

> [!question]- ¿Por qué un conjunto puede tener cotas superiores y aun así no tener supremo?
> Porque entre las cotas superiores puede no haber una menor. En un orden parcial cabe que haya varias cotas minimales incomparables entre sí.

> [!question]- Si $S$ tiene máximo $m$, ¿cuál es $\sup S$ y por qué?
> Es $m$: es cota superior, y cualquier otra cota superior es mayor o igual a $m$ porque $m \in S$.
