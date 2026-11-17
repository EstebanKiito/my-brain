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

# Ejercicios de prueba de funciones y cardinalidad

Las interrogaciones y exámenes repiten cinco formatos: **propiedades de funciones** (inyectiva, sobreyectiva, composición, inversa), **biyecciones explícitas** entre conjuntos, **enumerabilidad** (por lista, por unión o por Cantor-Schröder-Bernstein), **no enumerabilidad** por diagonalización y el **teorema de Cantor** con sus consecuencias. La pauta puntúa que se exhiba la función, se pruebe cada propiedad por separado y se indique qué criterio de enumerabilidad se usa.

## Ejercicios

### 1. La inversa de una biyección (I2, 2021-2)
Demuestre que si $f : A \to B$ es biyectiva, la relación inversa $f^{-1}$ es una función biyectiva de $B$ en $A$.

> [!example]- Solución
> Es el teorema de [[03 - Composición e inversa de funciones]]. **Función:** si $x_1 f y$ y $x_2 f y$, la inyectividad de $f$ da $x_1 = x_2$. **Total:** para $y \in B$, la sobreyectividad da $x$ con $f(x) = y$. **Inyectiva:** $f^{-1}(y_1) = f^{-1}(y_2) = x$ implica $y_1 = f(x) = y_2$. **Sobre:** para $x \in A$, $y = f(x)$ cumple $f^{-1}(y) = x$.

### 2. Biyecciones explícitas (I2, 2016-2)
(a) Exhiba una biyección entre $\mathbb{Z}$ y $B = \{2^k \mid k \in \mathbb{N}\}$. (b) Exhiba una biyección entre $(0, 1)$ y $[0, 1]$.

> [!example]- Solución
> (a) Los enteros $a \le 0$ van a exponentes pares y los positivos a exponentes impares: $f(a) = 2^{-2a}$ si $a \le 0$ y $f(a) = 2^{2a - 1}$ si $a > 0$. Es inyectiva: dos imágenes iguales tienen el mismo exponente, y la paridad indica la rama, donde $a \mapsto -2a$ y $a \mapsto 2a - 1$ son inyectivas. Es sobreyectiva: $2^k$ con $k$ par es $f(-k/2)$ y con $k$ impar es $f((k+1)/2)$.
>
> (b) Se "desplaza" la sucesión $1, \tfrac12, \tfrac13, \dots$ para hacer espacio a los extremos. Se define $f : [0, 1] \to (0, 1)$ con $f(0) = \tfrac12$, $f(\tfrac1n) = \tfrac{1}{n+2}$ para $n \ge 1$ y $f(x) = x$ en los demás casos. El valor $\tfrac12$ lo recibe $0$ y cada $\tfrac{1}{m}$ con $m \ge 3$ lo recibe $\tfrac{1}{m-2}$; el resto se queda quieto. Así es inyectiva y cubre todo $(0, 1)$.

### 3. Teorema de Cantor (I2, 2017-2)
Demuestre que $A$ es menos numeroso que $\mathcal{P}(A)$ para todo conjunto $A$.

> [!example]- Solución
> $f(a) = \{a\}$ es inyectiva, luego $A \preceq \mathcal{P}(A)$. Si existiera una biyección $f : A \to \mathcal{P}(A)$, el conjunto $D = \{a \in A \mid a \notin f(a)\}$ estaría en $\mathcal{P}(A)$ y sería $f(b)$ para algún $b$. Si $b \in f(b) = D$, la definición de $D$ da $b \notin f(b)$; si $b \notin f(b)$, entonces $b \in D = f(b)$. En ambos casos hay contradicción; la demostración completa está en [[07 - Diagonalización y teorema de Cantor]].

### 4. Hotel de Hilbert con funciones (I2, 2017-2)
Un hotel tiene infinitas habitaciones $1, 2, 3, \dots$ y está lleno. Con funciones, explique cómo alojar a (a) una persona, (b) $n$ personas, (c) un bus con infinitas personas, (d) infinitos buses con infinitas personas cada uno.

> [!example]- Solución
> Se reubica a los huéspedes con una función **inyectiva** de habitaciones en habitaciones, de modo que quede libre un conjunto de habitaciones donde alojar a los nuevos. (a) El huésped de $k$ pasa a $k + 1$ y la habitación $1$ queda libre. (b) $k \mapsto k + n$ libera $1, \dots, n$. (c) $k \mapsto 2k$ deja libres todas las impares; el pasajero $k$ va a $2k - 1$. (d) $k \mapsto 2k$ libera las impares y el pasajero $i$ del bus $j$ va a $2g(i, j) - 1$, con $g : \mathbb{N}^+ \times \mathbb{N}^+ \to \mathbb{N}^+$ una biyección (recorrido por diagonales). Las asignaciones son inyectivas (nadie comparte pieza) y las listas no se pisan por la paridad.

### 5. Unión numerable de numerables (I2, 2016-2)
(a) Si cada $S_i$ ($i \in \mathbb{N}$) es enumerable, demuestre que $\bigcup_i S_i$ es enumerable. (b) Demuestre que el conjunto de las sucesiones enteras eventualmente periódicas (existen $n_0 \in \mathbb{N}$ y $k > 0$ con $z_{n+k} = z_n$ para $n \ge n_0$) es enumerable.

> [!example]- Solución
> (a) Con $S_i = \{s_{i0}, s_{i1}, \dots\}$, la función $(i, j) \mapsto s_{ij}$ va de $\mathbb{N}^2$ (enumerable) sobre la unión. Se recorren los pares por diagonales y se omiten los elementos ya listados: queda una lista sin repetidos. La unión es infinita porque contiene a $S_0$, luego es enumerable.
>
> (b) Para $n_0$ y $k$ fijos, una sucesión que se repite con período $k$ desde $n_0$ queda determinada por sus primeros $n_0 + k$ términos, y cualquier tupla sirve: hay una biyección con $\mathbb{Z}^{n_0+k}$, enumerable. El conjunto total es la unión de esos conjuntos sobre los pares $(n_0, k) \in \mathbb{N} \times \mathbb{N}^+$, que son enumerables, y aplica (a).

### 6. $(0, 1) \times (0, 1) \approx (0, 1)$ (I2, 2018-2)
Sea $S = (0, 1)$. Demuestre que $S \times S \approx S$.

> [!example]- Solución
> Por CSB, bastan dos inyecciones. $f : S \to S \times S$, $f(x) = (x, x)$. Para la otra, se toma para cada real su expansión decimal que no termina en nueves y $g(x, y) = 0{,}x_1 y_1 x_2 y_2 \cdots$, intercalando los dígitos de $x = 0{,}x_1 x_2 \cdots$ e $y = 0{,}y_1 y_2 \cdots$. Los dígitos de $x$ e $y$ se recuperan de las posiciones impares y pares, así que $g$ es inyectiva (y el resultado no termina en nueves, porque ni $x$ ni $y$ terminan en nueves). Luego $S \times S \approx S$.

### 7. Palabras infinitas (I3, 2019-1)
Sea $\Sigma$ un alfabeto finito con $\lvert \Sigma \rvert \ge 2$ y $\Sigma^\omega$ el conjunto de palabras infinitas. (a) Demuestre $\Sigma^\omega \approx \{0, 1\}^\omega$. (b) Demuestre que el conjunto de palabras "regulares" $u \cdot v \cdot v \cdot v \cdots$ (con $u, v \in \Sigma^*$, $v \ne \varepsilon$) es enumerable.

> [!example]- Solución
> (a) CSB. Con $\Sigma = \{a_1, \dots, a_m\}$, $f : \Sigma^\omega \to \{0, 1\}^\omega$ reemplaza cada $a_i$ por el bloque $0^{i-1} 1\, 0^{m-i}$ (de largo $m$): es inyectiva, pues los bloques tienen un único $1$ en posición distinta y la palabra original se lee bloque a bloque. $g : \{0, 1\}^\omega \to \Sigma^\omega$ reemplaza $1 \mapsto a_1$ y $0 \mapsto a_2$: inyectiva (símbolo a símbolo, con $a_1 \ne a_2$).
>
> (b) $\Sigma^*$ es enumerable (cadenas finitas ordenadas por largo), luego $\Sigma^* \times (\Sigma^* \setminus \{\varepsilon\})$ también. La función $(u, v) \mapsto u v v v \cdots$ lleva ese conjunto sobre las palabras regulares; al recorrer la lista de pares y omitir las palabras repetidas se obtiene una lista sin repetidos. Es infinita (por ejemplo $a_1^k a_2^\omega$ para cada $k$), luego enumerable.

### 8. Puntos periódicos e inyectividad (I2, 2025-2)
Sea $f : A \to A$ y $f^n = f \circ \cdots \circ f$ ($n$ veces). (a) Si para todo $a \in A$ existe $n \ge 1$ con $f^n(a) = a$, demuestre que $f$ es inyectiva. (b) Demuestre que la recíproca falla.

> [!example]- Solución
> (a) Sea $f(a) = f(b)$ con $f^n(a) = a$ y $f^m(b) = b$. Aplicando la función varias veces, $f^{nm}(a) = a$ y $f^{nm}(b) = b$. Entonces $a = f^{nm}(a) = f^{nm-1}(f(a)) = f^{nm-1}(f(b)) = f^{nm}(b) = b$.
>
> (b) $f : \mathbb{N} \to \mathbb{N}$, $f(n) = n + 1$ es inyectiva, pero $f^k(0) = k \ne 0$ para todo $k \ge 1$, así que $0$ no es periódico.

### 9. Funciones ortogonales y aditivas (I2, 2019-1)
Sean $f, g : \mathbb{N} \to \mathbb{N}$, $h_c$ la constante $c$ y $f$ *ortogonal* a $g$ si para todo $x$, $g(f(x)) = 0$. (a) Demuestre que $f$ es sobreyectiva si y solo si es ortogonal únicamente a $h_0$. (b) Si $f(a + b) = f(a) + f(b)$ para todo $a, b$, demuestre que $f$ es inyectiva si y solo si $f(1) \ne 0$.

> [!example]- Solución
> (a) ($\Rightarrow$) Si $f$ es sobre y ortogonal a $g$, para cada $a$ hay $x$ con $f(x) = a$, y entonces $g(a) = g(f(x)) = 0$; luego $g = h_0$. ($\Leftarrow$) Si $f$ no es sobre, existe $b$ fuera de su imagen; la función $g'$ con $g'(b) = 1$ y $g'(x) = 0$ en el resto cumple $g'(f(x)) = 0$ para todo $x$ y es distinta de $h_0$.
>
> (b) De $f(0) = f(0 + 0) = 2f(0)$ sale $f(0) = 0$. ($\Rightarrow$) Si $f(1) = 0$, entonces $f(0) = f(1)$ con $0 \ne 1$: no es inyectiva. ($\Leftarrow$) Por inducción $f(n) = n f(1)$; si $f(n) = f(m)$, entonces $(n - m) f(1) = 0$ y como $f(1) \ne 0$, $n = m$.

### 10. Cuántas funciones tienen cierta imagen (I2, 2026-1)
Sean $X, Y, A, B$ finitos con $A \subseteq B \subseteq Y$. ¿Puede haber más funciones $f : X \to Y$ con $f(X) = A$ que con $f(X) = B$?

> [!example]- Solución
> Sí. Con $X = \{1\}$, $Y = B = \{1, 2\}$ y $A = \{1\}$ hay una función con imagen $\{1\}$ (la que envía $1 \mapsto 1$) y ninguna con imagen $\{1, 2\}$, porque un único elemento del dominio tiene una sola imagen. En general, que la imagen sea exactamente $B$ exige $\lvert X \rvert \ge \lvert B \rvert$ (por el palomar), una condición más fuerte que $\lvert X \rvert \ge \lvert A \rvert$, que es la que necesita $A$.

### 11. No existe un infinito con potencia enumerable (I2, 2025-2)
Demuestre que no existe un conjunto infinito $A$ tal que $\mathcal{P}(A)$ sea enumerable.

> [!example]- Solución
> Si $A$ es infinito, tiene un subconjunto enumerable, luego $\mathbb{N} \preceq A$. Si $\mathcal{P}(A) \approx \mathbb{N}$, componiendo, $\mathcal{P}(A) \preceq \mathbb{N} \preceq A$. Junto con $A \preceq \mathcal{P}(A)$ (por $a \mapsto \{a\}$), CSB da $A \approx \mathcal{P}(A)$, lo que contradice el teorema de Cantor.

### 12. Funciones inyectivas de $\mathbb{N}$ en $\mathbb{N}$ (I2, 2022-1)
Demuestre que $F = \{f : \mathbb{N} \to \mathbb{N} \mid f \text{ inyectiva}\}$ no es enumerable.

> [!example]- Solución
> Por diagonalización: si $f_0, f_1, f_2, \dots$ listara a $F$, se define $g(i) = 1 + i + \sum_{k=0}^{i} f_k(k)$. Es estrictamente creciente, pues $g(i+1) - g(i) = 1 + f_{i+1}(i+1) \ge 1$, luego inyectiva y $g \in F$. Pero $g(m) \ge 1 + f_m(m) > f_m(m)$, así que $g \ne f_m$ para todo $m$ y $g$ no está en la lista: contradicción.

## Preguntas de repaso

> [!question]- ¿Cuándo se usa CSB en vez de dar una biyección?
> Cuando es difícil armar la biyección pero se ven con facilidad dos inyecciones (inclusiones, codificaciones), como en los ejercicios 6 y 7.

> [!question]- ¿Qué tienen en común los ejercicios 3, 11 y 12 al probar que algo no es enumerable?
> Suponen una lista (o biyección) y fabrican un elemento que difiere de cada uno de los de la lista en una posición propia: la diagonal.

> [!question]- ¿Por qué en el ejercicio 4 las funciones son inyectivas y no necesariamente biyectivas?
> Porque lo único que se exige es que nadie comparta habitación; la reubicación no necesita cubrir todas las habitaciones, y de hecho deja libres justo las que ocuparán los recién llegados.
