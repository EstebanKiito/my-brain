---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/ordenes
  - origen/complemento
prerrequisitos: []
---

# Órdenes parciales y totales

Ordenar es decidir quién va "antes" que quién. Con los números todo par se puede comparar, pero con divisibilidad o con conjuntos hay pares que simplemente no se comparan. Las relaciones de orden capturan esa estructura mínima: lo que hace falta para que "$\preceq$" se comporte como un $\le$, sin exigir que todos sean comparables.

## Orden parcial

Una relación $\preceq$ sobre $A$ es un **orden parcial** si es refleja, antisimétrica y transitiva. Se escribe $x \preceq y$ y se lee "$x$ es menor o igual que $y$". El par $(A,\preceq)$ se llama también orden parcial: el conjunto importa, porque la misma relación puede ser orden en un conjunto y no en otro.

> [!tip] Las tres propiedades
> **Refleja:** $x \preceq x$. **Antisimétrica:** $x \preceq y$ e $y \preceq x$ implican $x = y$. **Transitiva:** $x \preceq y$ e $y \preceq z$ implican $x \preceq z$.

Ejemplos clásicos:
- $(\mathbb{N},\le)$, $(\mathbb{Z},\le)$ y $(\mathbb{R},\le)$.
- $(\mathbb{N}\setminus\{0\}, \mid)$, la divisibilidad ($a \mid b$ si $b$ es múltiplo de $a$): $2 \mid 6$, pero $2 \nmid 3$ y $3 \nmid 2$.
- $(\mathcal{P}(A),\subseteq)$ para cualquier conjunto $A$.

**Demostración para $(\mathcal{P}(A),\subseteq)$.** Refleja: $X \subseteq X$. Antisimétrica: $X \subseteq Y$ e $Y \subseteq X$ dan $X = Y$ por doble inclusión. Transitiva: si $x \in X$ entonces $x \in Y$ y luego $x \in Z$.

> [!warning] El conjunto importa
> La divisibilidad **no** es orden parcial en $\mathbb{Z}$: $2 \mid -2$ y $-2 \mid 2$ pero $2 \ne -2$, así que falla la antisimetría. Tampoco $<$ es orden parcial (no es refleja).

## Orden total

Dos elementos son **comparables** si $x \preceq y$ o $y \preceq x$. Un orden es **total** (o lineal) si es parcial y todos los pares son comparables (propiedad **conexa**). $(\mathbb{N},\le)$ es total; $(\mathbb{N}\setminus\{0\},\mid)$ no lo es ($2$ y $3$ son incomparables), y $(\mathcal{P}(\{1,2\}),\subseteq)$ tampoco ($\{1\}$ y $\{2\}$).

| Orden | ¿Parcial? | ¿Total? | Un par incomparable |
|---|---|---|---|
| $(\mathbb{Z},\le)$ | sí | sí | ninguno |
| $(\mathbb{N}\setminus\{0\},\mid)$ | sí | no | $2$ y $3$ |
| $(\mathcal{P}(\{1,2,3\}),\subseteq)$ | sí | no | $\{1,2\}$ y $\{2,3\}$ |

## Orden lexicográfico

Dados dos órdenes parciales $(A,\preceq_A)$ y $(B,\preceq_B)$, el **orden lexicográfico** sobre $A\times B$ compara primero la primera coordenada y sólo desempata con la segunda:

$$(a_1,b_1) \preceq (a_2,b_2) \iff (a_1 \ne a_2 \wedge a_1 \preceq_A a_2) \ \vee\ (a_1 = a_2 \wedge b_1 \preceq_B b_2).$$

Así, con $\le$ en ambas coordenadas, $(1,4) \preceq (2,0)$ (manda la primera), $(2,3) \preceq (2,5)$ (empate y desempate) y $(3,0) \not\preceq (2,9)$. Es el orden del diccionario. Si ambos órdenes son parciales, el resultado es parcial; si ambos son totales, también lo es. Con divisibilidad en ambas coordenadas sigue siendo parcial pero no total: $(1,2)$ y $(1,3)$ no se comparan.

> [!warning] Parcial no significa "a medias"
> "Parcial" sólo indica que **puede** haber incomparables. Todo orden total es en particular parcial.

## Preguntas de repaso

> [!question]- ¿Por qué se exige antisimetría en un orden y no sólo reflexividad y transitividad?
> Sin ella, dos elementos distintos podrían ser "menores el uno que el otro" y no habría un primero y un último claros. Una relación refleja y transitiva sin antisimetría se llama preorden y agrupa elementos equivalentes.

> [!question]- ¿Es $\subseteq$ un orden total sobre $\mathcal{P}(\{1\})$? ¿Y sobre $\mathcal{P}(\{1,2\})$?
> Sobre $\mathcal{P}(\{1\}) = \{\emptyset,\{1\}\}$ sí, porque $\emptyset \subseteq \{1\}$. Sobre $\mathcal{P}(\{1,2\})$ no: $\{1\}$ y $\{2\}$ son incomparables.

> [!question]- ¿Cómo se ve que el orden lexicográfico sobre $\mathbb{N}\times\mathbb{N}$ es total?
> Dados dos pares, si las primeras coordenadas difieren, el menor de ellos ordena el par; si coinciden, se comparan las segundas, que sí son comparables. Siempre una de las dos posibilidades vale.

> [!question]- ¿Por qué hay que decir "el orden $(A,\preceq)$" y no sólo "la relación $\preceq$"?
> Porque la misma relación puede cumplir las propiedades en un conjunto y fallar en otro, como la divisibilidad en $\mathbb{N}\setminus\{0\}$ y en $\mathbb{Z}$.
