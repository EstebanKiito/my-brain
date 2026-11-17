---
ramo: "Matemáticas Discretas"
tema: "Funciones y cardinalidad"
tags:
  - discretas/cardinalidad
  - origen/complemento
prerrequisitos:
  - "[[06 - Teorema de Cantor-Schröder-Bernstein y orden entre cardinalidades]]"
---

# Diagonalización y teorema de Cantor

Hasta aquí todos los infinitos vistos ($\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{N}^n$, programas) eran del mismo tamaño que $\mathbb{N}$. La **diagonalización** de Cantor muestra que no todos los infinitos coinciden: dada cualquier lista, se fabrica un elemento que no está en ella. La misma idea, aplicada a un conjunto cualquiera y su conjunto potencia, demuestra que siempre hay un infinito mayor.

## $(0, 1)$ no es enumerable

> [!tip] Teorema
> El intervalo real $(0, 1)$ es infinito pero no enumerable.

Es infinito porque contiene a $\tfrac12, \tfrac13, \tfrac14, \dots$. Para ver que no es enumerable se razona por contradicción. Si lo fuera, existiría una lista $r_0, r_1, r_2, \dots$ con todos sus elementos, y cada uno tendría una expansión decimal $r_i = 0{,}d_{i0}d_{i1}d_{i2}\cdots$ con $d_{ij} \in \{0, \dots, 9\}$. Se escribe la lista como una tabla infinita y se mira su **diagonal** $d_{00}, d_{11}, d_{22}, \dots$

![Diagonal de Cantor sobre la lista de reales](adjuntos/Diagonal%20de%20Cantor%20sobre%20los%20reales.png)

> [!example]- Transcripción de la imagen
> Tabla con una fila por real $r_0, r_1, r_2, \dots$ y sus dígitos decimales $d_{ij}$ en columnas. Los dígitos de la diagonal ($d_{00}, d_{11}, d_{22}, d_{33}, d_{44}$) están resaltados. Debajo, la regla $d_i = d_{ii} + 1$ si $d_{ii} < 9$ y $d_i = 0$ si $d_{ii} = 9$, y el real $r = 0{,}d_0 d_1 d_2 \cdots$.

Se define un número nuevo cambiando cada dígito de la diagonal: $d_i = d_{ii} + 1$ si $d_{ii} < 9$ y $d_i = 0$ si $d_{ii} = 9$. Sea $r = 0{,}d_0 d_1 d_2 \cdots$. Entonces $r \in (0, 1)$, pero $r \ne r_i$ para todo $i$, porque difieren en el dígito de la posición $i$ (se tiene $d_i \ne d_{ii}$). Así $r$ no está en la lista, contradiciendo que la lista los contenía a todos.

> [!warning] Dos escrituras para un mismo real
> Algunos reales tienen dos expansiones decimales ($0{,}5000\ldots = 0{,}4999\ldots$), y un dígito distinto en una expansión no garantiza un número distinto. Se evita eligiendo los dígitos de $r$ solo entre $1$ y $2$ (por ejemplo $d_i = 2$ si $d_{ii} = 1$, y $d_i = 1$ en los demás casos), de modo que $r$ nunca termina en ceros ni en nueves.

Ese argumento es el de la **diagonalización**, base de resultados de computación: por ejemplo, hay más problemas que programas que los resuelvan, porque los programas son enumerables y los problemas de decisión corresponden a $\mathcal{P}(\mathbb{N})$. Con inyecciones y CSB se obtiene además $(0, 1) \approx \mathbb{R} \approx \mathcal{P}(\mathbb{N})$, y por lo tanto $\lvert \mathbb{N} \rvert < \lvert \mathbb{R} \rvert$. También el conjunto $\{0, 1\}^\omega$ de las secuencias binarias infinitas no es enumerable, por la misma diagonal cambiando $0 \leftrightarrow 1$.

## Teorema de Cantor: $\lvert A \rvert < \lvert \mathcal{P}(A) \rvert$

> [!tip] Teorema de Cantor
> Para todo conjunto $A$ (finito o infinito), $A \prec \mathcal{P}(A)$: $A$ es menos numeroso que su conjunto potencia.

**Inyección.** $f(a) = \{a\}$ es una función inyectiva $A \to \mathcal{P}(A)$, así que $A \preceq \mathcal{P}(A)$.

**No hay biyección.** Por contradicción, sea $f : A \to \mathcal{P}(A)$ biyectiva. Se define el **conjunto diagonal**
$$D = \{a \in A \mid a \notin f(a)\} \subseteq A.$$
Como $D \in \mathcal{P}(A)$ y $f$ es sobreyectiva, existe $x$ con $f(x) = D$. Hay dos casos:
- si $x \in f(x)$, entonces $x \in D$ (pues $f(x) = D$), pero por definición de $D$ eso exige $x \notin f(x)$;
- si $x \notin f(x)$, entonces $x \notin D$, pero por definición de $D$ eso exige $x \in f(x)$.

Ambos casos son contradictorios, así que no existe tal $f$.

Ejemplo con $A = \{a, b, c, d\}$ y una $f$ cualquiera. La fila de $x$ marca los elementos de $f(x)$:

| $x$ | $a \in f(x)$ | $b \in f(x)$ | $c \in f(x)$ | $d \in f(x)$ |
|---|---|---|---|---|
| $a$ | sí | sí | no | no |
| $b$ | no | no | sí | no |
| $c$ | sí | no | sí | sí |
| $d$ | no | no | no | no |

La diagonal dice si $x \in f(x)$: $a$ sí, $b$ no, $c$ sí, $d$ no. El conjunto diagonal es $D = \{b, d\}$ (los que **no** están en su propia imagen) y difiere de cada fila en la diagonal, así que ninguna fila es $D$.

## Consecuencias

La cadena $\lvert A \rvert < \lvert \mathcal{P}(A) \rvert < \lvert \mathcal{P}(\mathcal{P}(A)) \rvert < \cdots$ no termina: hay infinitos tamaños de infinito. Y si $A$ es infinito, $\mathcal{P}(A)$ nunca es enumerable, porque $\mathbb{N} \preceq A \prec \mathcal{P}(A)$.

## Preguntas de repaso

> [!question]- ¿Por qué el número diagonal $r$ no puede estar en la lista?
> Porque difiere de $r_i$ en el dígito $i$ para todo $i$. Como la lista pretendía contener todos los reales de $(0,1)$ y $r$ pertenece a $(0,1)$, hay contradicción.

> [!question]- ¿Dónde usa la prueba del teorema de Cantor que $f$ es sobreyectiva?
> Para asegurar que el conjunto diagonal $D \in \mathcal{P}(A)$ tiene una preimagen $x$ con $f(x) = D$. Sin esa preimagen no se podría preguntar si $x \in D$.

> [!question]- ¿Cómo se concluye que no existe un conjunto infinito cuyo potencia sea enumerable?
> Si $A$ es infinito, $\mathbb{N} \preceq A$. Si además $\mathcal{P}(A) \approx \mathbb{N}$, entonces $\mathcal{P}(A) \preceq A$, y con $A \preceq \mathcal{P}(A)$ el teorema CSB da $A \approx \mathcal{P}(A)$, contra el teorema de Cantor.
