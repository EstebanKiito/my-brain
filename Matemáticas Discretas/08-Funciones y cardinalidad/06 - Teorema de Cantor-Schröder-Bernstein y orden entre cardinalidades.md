---
ramo: "Matemáticas Discretas"
tema: "Funciones y cardinalidad"
tags:
  - discretas/cardinalidad
  - origen/complemento
prerrequisitos:
  - "[[05 - Conjuntos enumerables y listas infinitas]]"
---

# Teorema de Cantor-Schröder-Bernstein y orden entre cardinalidades

Construir una biyección explícita entre dos conjuntos puede ser muy difícil, pero encontrar una función inyectiva en cada dirección suele ser fácil. El teorema de Cantor-Schröder-Bernstein dice que eso basta, y de paso permite comparar cardinalidades con un orden.

## "No es más numeroso que"

Se escribe $A \preceq B$ si existe una función **inyectiva** $f : A \to B$, y entonces $\lvert A \rvert \le \lvert B \rvert$: $A$ cabe dentro de $B$ sin que se junten elementos. Es refleja (la identidad) y transitiva (la composición de inyectivas es inyectiva), es decir, un **preorden**.

La versión estricta es $A \prec B$ si $A \preceq B$ pero **no** $A \approx B$: existe una inyección de $A$ en $B$ y ninguna biyección. Entonces $\lvert A \rvert < \lvert B \rvert$.

> [!tip] Teorema de Cantor-Schröder-Bernstein (CSB)
> $A \approx B$ si y solo si existen funciones inyectivas $f : A \to B$ y $g : B \to A$. Es decir, $A \preceq B$ y $B \preceq A$ implican $A \approx B$.

El sentido "$\Rightarrow$" es inmediato (una biyección y su inversa son inyectivas). El sentido útil es el recíproco: **no hay que construir la biyección**, solo dos inyecciones. Con él, $\preceq$ pasa a ser antisimétrica sobre cardinalidades y, por lo tanto, un orden entre ellas.

## Ejemplo: $A = \{2^i \cdot 3^j \mid i, j \in \mathbb{N}\}$ es enumerable

Se buscan inyecciones entre $A$ y $\mathbb{N}$:
- $f : A \to \mathbb{N}$, $f(x) = x$ es inyectiva (cada elemento de $A$ ya es un natural).
- $g : \mathbb{N} \to A$, $g(x) = 2^x \cdot 3^x = 6^x$ es inyectiva, pues $6^x = 6^y$ obliga $x = y$.

Por CSB, $A \approx \mathbb{N}$. Armar a mano la biyección habría exigido ordenar todos los productos $2^i 3^j$.

## Más usos habituales

- **Reales.** $(0, 1) \preceq \mathbb{R}$ por inclusión y $\mathbb{R} \preceq (0, 1)$ por $x \mapsto \tfrac{1}{\pi}\arctan x + \tfrac12$, así que $(0, 1) \approx \mathbb{R}$; las dos inyecciones evitan tener que dar una biyección exacta. También vale $(0, 1) \approx \mathcal{P}(\mathbb{N})$.
- **Estructuras codificadas.** Si cada elemento de $A$ se puede codificar de forma reversible como un elemento de $B$ y viceversa, $A \approx B$. Ejemplos: secuencias infinitas sobre un alfabeto de $k$ símbolos frente a secuencias binarias, o $S \times S \approx S$ para $S = (0, 1)$ intercalando dígitos decimales.
- **Cotas.** Si $A \subseteq B$ entonces $A \preceq B$ (la inclusión es inyectiva). Así, un subconjunto de un enumerable, si es infinito, es enumerable (ver la nota anterior).

> [!warning] Dos inyecciones, no una inyección y una sobreyección cualquiera
> Para CSB las dos funciones tienen que ser inyectivas y en direcciones opuestas. Una inyección de $A$ en $B$ sola solo prueba $A \preceq B$; que $A$ sea una parte propia de $B$ no impide que $A \approx B$ (como los pares y $\mathbb{N}$).

## Una cadena de cardinalidades

Se sabe que $\lvert \mathbb{N} \rvert = \lvert \mathbb{Z} \rvert = \lvert \mathbb{Q} \rvert < \lvert \mathbb{R} \rvert = \lvert (0, 1) \rvert = \lvert \mathcal{P}(\mathbb{N}) \rvert$. La desigualdad estricta se prueba en [[07 - Diagonalización y teorema de Cantor]]. Queda la pregunta de si existe algo estrictamente entre $\lvert \mathbb{N} \rvert$ y $\lvert \mathbb{R} \rvert$: la **hipótesis del continuo** afirma que no, y se llama "hipótesis" porque no es demostrable ni refutable desde los axiomas habituales de la teoría de conjuntos.

## Preguntas de repaso

> [!question]- ¿Qué ventaja tiene CSB frente a construir una biyección?
> Para dos conjuntos con estructuras complicadas, una biyección explícita suele ser difícil; basta pensar en una inyección de cada lado, que casi siempre es una codificación o una inclusión simple.

> [!question]- ¿Por qué $\preceq$ es refleja y transitiva?
> Refleja porque la identidad es inyectiva; transitiva porque si $f : A \to B$ y $g : B \to C$ son inyectivas, $g \circ f$ lo es.

> [!question]- ¿Cómo se prueba que $\{2^i 3^j\}$ es enumerable sin ordenar sus elementos?
> Con las inyecciones $x \mapsto x$ (a $\mathbb{N}$) y $x \mapsto 6^x$ (desde $\mathbb{N}$), y luego CSB entrega la biyección sin construirla.
