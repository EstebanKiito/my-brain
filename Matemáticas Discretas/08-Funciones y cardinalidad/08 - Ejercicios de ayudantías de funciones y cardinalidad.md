---
ramo: "Matemáticas Discretas"
tema: "Funciones y cardinalidad"
tags:
  - discretas/ejercicios
  - discretas/cardinalidad
  - origen/complemento
prerrequisitos:
  - "[[03 - Composición e inversa de funciones]]"
  - "[[07 - Diagonalización y teorema de Cantor]]"
---

# Ejercicios de ayudantías de funciones y cardinalidad

Cinco ejercicios de ayudantía: propiedades de funciones crecientes, enumerabilidad de uniones y subconjuntos, y dos conjuntos de secuencias infinitas cuya enumerabilidad se decide con funciones y con diagonalización. Conviene intentarlos antes de abrir la solución.

## Ejercicios

### 1. Funciones crecientes
Sean $A, B, C \subseteq \mathbb{N}$. Una función $f : A \to B$ es **creciente** si $x < y \Rightarrow f(x) < f(y)$. (a) Demuestre que si $f$ es creciente, es inyectiva. (b) ¿Es cierto que si $f : A \to B$ y $g : B \to C$ son crecientes, $g \circ f$ es inyectiva?

> [!example]- Solución
> (a) Si $x_1 \ne x_2$, uno es menor; sin pérdida de generalidad $x_1 < x_2$, y entonces $f(x_1) < f(x_2)$, o sea $f(x_1) \ne f(x_2)$. Por contrarrecíproco, $f(x_1) = f(x_2)$ fuerza $x_1 = x_2$.
>
> (b) Sí. Si $x_1 < x_2$, como $f$ es creciente $f(x_1) < f(x_2)$, y como $g$ es creciente (y $f(x_1), f(x_2) \in B$), $g(f(x_1)) < g(f(x_2))$. Así $g \circ f$ es creciente y, por (a), inyectiva.

### 2. La unión de dos enumerables
Demuestre que si $A$ y $B$ son enumerables, $A \cup B$ es enumerable.

> [!example]- Solución
> Si $A \cap B = \emptyset$, con biyecciones $f : \mathbb{N} \to A$ y $g : \mathbb{N} \to B$ se define $h(n) = f(n/2)$ si $n$ es par y $h(n) = g((n-1)/2)$ si $n$ es impar. Es inyectiva (las imágenes de pares e impares están en $A$ y en $B$, que son disjuntos, y dentro de cada rama $f$ y $g$ son inyectivas) y sobreyectiva (todo $a = f(k)$ es $h(2k)$ y todo $b = g(k)$ es $h(2k+1)$).
>
> Si no son disjuntos, $A \cup B = A \cup (B \setminus A)$ con $B \setminus A$ finito o enumerable. Si es enumerable, se aplica lo anterior. Si es finito, se pone una lista finita al comienzo y luego los elementos de $A$ (se obtiene también una lista infinita sin repetidos).

### 3. Subconjuntos infinitos de un enumerable
Demuestre que todo subconjunto infinito de un conjunto enumerable es enumerable.

> [!example]- Solución
> Sea $A = \{a_0, a_1, a_2, \dots\}$ enumerable (sin repeticiones) y $B \subseteq A$ infinito. Se definen índices $i_0 = \min\{i \mid a_i \in B\}$ y $i_{k+1} = \min\{i > i_k \mid a_i \in B\}$; existen siempre porque $B$ es infinito. La función $g(k) = a_{i_k}$ es inyectiva (los $i_k$ crecen estrictamente y los $a_i$ no se repiten) y sobreyectiva (si $a_i \in B$, entre $a_0, \dots, a_i$ hay $c \ge 1$ elementos de $B$, que por construcción son $a_{i_0}, \dots, a_{i_{c-1}}$, luego $a_i = g(c-1)$). Así $B \approx \mathbb{N}$.

### 4. Progresiones aritméticas de enteros
Sea $\mathbb{Z}^\omega$ el conjunto de las secuencias infinitas $a_0 a_1 a_2 \cdots$ de enteros y $S_1 = \{a_0 a_1 \cdots \in \mathbb{Z}^\omega \mid \exists c \in \mathbb{Z},\ \forall i,\ a_{i+1} - a_i = c\}$. ¿Es $S_1$ enumerable?

> [!example]- Solución
> Sí. Una secuencia de $S_1$ queda determinada por su primer término y su diferencia: $f(a_0 a_1 \cdots) = (a_0, a_1 - a_0)$ es una función $S_1 \to \mathbb{Z}^2$. Es inyectiva (si dos secuencias tienen el mismo $a_0$ y la misma diferencia, son iguales término a término) y sobreyectiva (el par $(a, c)$ es la imagen de $a, a + c, a + 2c, \dots$). Luego $S_1 \approx \mathbb{Z}^2$, que es enumerable porque $\mathbb{Z} \approx \mathbb{N}$ y $\mathbb{N}^2$ es enumerable. (La solución de ayudantía usa dos inyecciones y CSB; aquí la biyección sale directa.)

### 5. Secuencias con saltos de tamaño fijo
Sea $S_2 = \{a_0 a_1 \cdots \in \mathbb{Z}^\omega \mid \exists c \in \mathbb{Z},\ \forall i,\ \lvert a_{i+1} - a_i \rvert = c\}$. Por ejemplo $7, 10, 7, 4, 1, -2, 1, \dots \in S_2$ con $c = 3$. ¿Es $S_2$ enumerable?

> [!example]- Solución
> No. Se considera el subconjunto $T \subseteq S_2$ de las secuencias con $a_0 = 0$ y $\lvert a_{i+1} - a_i \rvert = 1$ (caso $c = 1$). La función $\{0, 1\}^\omega \to T$ que lleva $b_0 b_1 \cdots$ a la secuencia con $a_0 = 0$ y $a_{i+1} = a_i + 1$ si $b_i = 1$, $a_i - 1$ si $b_i = 0$, es una biyección: de las diferencias se recupera cada $b_i$. Como $\{0, 1\}^\omega$ no es enumerable (diagonalización), $T$ tampoco. Si $S_2$ fuera enumerable, su subconjunto infinito $T$ lo sería por el ejercicio 3, contradicción. Por tanto $S_2$ no es enumerable.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 4 basta una biyección con $\mathbb{Z}^2$ y no hace falta un argumento de diagonal?
> Porque cada secuencia aritmética está determinada por dos enteros, así que el conjunto es una copia de $\mathbb{Z}^2$, que ya se sabe enumerable.

> [!question]- ¿Qué distingue a $S_2$ de $S_1$ para que pase de enumerable a no enumerable?
> En $S_2$ cada paso permite elegir entre $+c$ y $-c$, lo que da una libertad binaria en cada posición y codifica secuencias binarias arbitrarias. En $S_1$ el paso está fijo, así que no hay elecciones.

> [!question]- ¿Por qué el ejercicio 3 es útil en el 5?
> Permite pasar de "un subconjunto no enumerable" a "el conjunto completo no enumerable": si el todo fuera enumerable, el subconjunto infinito también lo sería.
