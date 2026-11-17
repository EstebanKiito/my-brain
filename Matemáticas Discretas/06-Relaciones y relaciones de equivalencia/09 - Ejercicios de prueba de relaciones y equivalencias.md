---
ramo: "Matemáticas Discretas"
tema: "Relaciones y relaciones de equivalencia"
tags:
  - discretas/relaciones
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[05 - Clausuras de una relación]]"
  - "[[07 - Particiones, cuociente e índice y relación inducida]]"
---

# Ejercicios de prueba de relaciones y equivalencias

Las interrogaciones y exámenes repiten cinco formatos: **probar que una relación es de equivalencia** (refleja, simétrica y transitiva), **razonar con propiedades y operaciones** ($R^{-1}$, $\circ$, $I_A$), **clausuras** y la menor equivalencia que contiene a una relación, **describir clases y contar el cuociente**, y **analizar un algoritmo** de clausura. La pauta puntúa cada una de las tres propiedades por separado y exige un contraejemplo concreto cuando se pide refutar. Aquí $I_A = \{(a, a) \mid a \in A\}$ y $R \circ S = \{(a, c) \mid \exists b\ (a, b) \in R \wedge (b, c) \in S\}$.

## Ejercicios

### 1. Par ordenado de Kuratowski (I2, 2015-2)
(a) Con $(a, b) = \{\{a\}, \{a, b\}\}$, demuestre que $(a, b) = (c, d) \iff a = c \wedge b = d$. (b) Con $(a, b) = \{a, \{b\}\}$ la propiedad no se cumple.

> [!example]- Solución
> **(a)** ($\Leftarrow$) es inmediata. ($\Rightarrow$) Si $a = b$, entonces $(a, b) = \{\{a\}\}$ y por igualdad $\{c\} = \{c, d\} = \{a\}$, de donde $c = d = a$. Si $a \neq b$, $\{a, b\}$ tiene dos elementos y no puede igualar a $\{c\}$, así que $\{a\} = \{c\}$ y $a = c$; luego $\{a, b\} = \{a, d\}$ y $b = d$. **(b)** Para $x \neq y$, con $a = \{x\}$, $b = y$, $c = \{y\}$, $d = x$ se tiene $(a, b) = \{\{x\}, \{y\}\} = (c, d)$, pero $a \neq c$.

### 2. Antisimetría y composición (I2, 2019-1)
Sea $R \subseteq A \times A$. Demuestre: (a) si $R$ es antisimétrica, $R \cap R^{-1} \subseteq I_A$; (b) si $R \circ R \subseteq R$, $R$ es transitiva.

> [!example]- Solución
> **(a)** Si $(a, b) \in R \cap R^{-1}$, entonces $(a, b) \in R$ y $(b, a) \in R$; por antisimetría $a = b$, o sea $(a, b) \in I_A$. **(b)** Si $(a, b), (b, c) \in R$, entonces $(a, c) \in R \circ R \subseteq R$.

### 3. Cuasi-orden (I2, 2025-1)
Una relación refleja y transitiva se llama cuasi-orden. Demuestre que si $R$ es un cuasi-orden, $R \cap R^{-1}$ es de equivalencia.

> [!example]- Solución
> **Refleja:** $(a, a) \in R$ y $(a, a) \in R^{-1}$. **Simétrica:** $(a, b) \in R \cap R^{-1}$ significa $(a, b) \in R$ y $(b, a) \in R$, que es simétrico en $a$ y $b$. **Transitiva:** si $(a, b), (b, c) \in R \cap R^{-1}$, la transitividad de $R$ da $(a, c) \in R$ (usando $a \to b \to c$) y $(c, a) \in R$ (usando $c \to b \to a$), es decir $(a, c) \in R \cap R^{-1}$.

### 4. Simétrica, transitiva y circular (I2, 2019-2)
(a) Si $R$ es simétrica y transitiva y todo $a$ tiene algún $b$ con $(a, b) \in R$, entonces $R$ es de equivalencia. (b) Si $R$ es refleja y transitiva y $T = \{(a, b) \mid (a, b), (b, a) \in R\}$, entonces $T$ es transitiva. (c) $R$ es de equivalencia si y solo si es refleja y **circular** ($xRy \wedge yRz \to zRx$).

> [!example]- Solución
> **(a)** Falta solo la reflexividad: para $a$ elegido $b$ con $(a, b) \in R$, la simetría da $(b, a) \in R$ y la transitividad $(a, a) \in R$. **(b)** Si $(a, b), (b, c) \in T$, la transitividad de $R$ da $(a, c) \in R$ y $(c, a) \in R$ (por $c \to b \to a$), luego $(a, c) \in T$. **(c)** ($\Rightarrow$) Si $xRy$ y $yRz$, la transitividad da $xRz$ y la simetría $zRx$. ($\Leftarrow$) *Simétrica:* de $aRb$ y $bRb$ (reflexividad) la circularidad da $bRa$. *Transitiva:* de $aRb$ y $bRc$ la circularidad da $cRa$ y la simetría ya demostrada $aRc$.

### 5. Palabras conjugadas (I2, 2017-1)
Sea $R$ la relación sobre $\{0, 1\}^*$ con $(w_1, w_2) \in R \iff \exists u, v\ \ w_1 = uv \wedge w_2 = vu$. (a) Demuestre que es de equivalencia. (b) Describa sus clases.

> [!example]- Solución
> Para una palabra $w$ de largo $n$ y $0 \leq k < n$ sea $\mathrm{rot}_k(w)$ la palabra que se obtiene pasando las primeras $k$ letras al final. Entonces $w_1 \mathrel{R} w_2$ si y solo si $w_2 = \mathrm{rot}_k(w_1)$ para algún $k$. **Refleja:** $k = 0$. **Simétrica:** $\mathrm{rot}_{n-k}$ deshace $\mathrm{rot}_k$. **Transitiva:** $\mathrm{rot}_j(\mathrm{rot}_k(w)) = \mathrm{rot}_{(j+k) \bmod n}(w)$.
>
> **(b)** La clase de $w$ es el conjunto de sus rotaciones, es decir, la palabra pensada como un collar circular: las palabras que dan el mismo collar son equivalentes. Para largo $3$ hay $4$ clases: $\{000\}$, $\{111\}$, $\{001, 010, 100\}$ y $\{011, 110, 101\}$ (para largos $1$ a $6$ son $2, 3, 4, 6, 8, 14$).

### 6. Relación inducida por una función (examen, 2022-1)
Sea $f: A \to B$. Se define $(x, y) \in R_f \iff f(x) = f(y)$. (a) Demuestre que $R_f$ es de equivalencia. (b) Demuestre que $\lvert A/R_f \rvert = \lvert \{f(a) \mid a \in A\} \rvert$.

> [!example]- Solución
> **(a)** Refleja, simétrica y transitiva se heredan de la igualdad en $B$. **(b)** Se define $g: A/R_f \to \mathrm{img}(f)$ por $g([a]) = f(a)$. Está bien definida: si $[a] = [a']$, entonces $f(a) = f(a')$. Es inyectiva: si $g([a]) = g([b])$, entonces $f(a) = f(b)$, o sea $[a] = [b]$. Es sobreyectiva: si $c = f(a)$, entonces $g([a]) = c$. Con $f(x) = x^2 \bmod 7$ sobre $\{0, \dots, 13\}$ hay $4$ clases y $4$ valores en la imagen.

### 7. La menor equivalencia que contiene a $R$ (I2, 2018-1)
Sea $R^t = \bigcup_{i \geq 1} R^i$. (a) Demuestre que $R^t$ es transitiva. (b) Demuestre que $R^\sim = (R \cup R^{-1} \cup I_A)^t$ es la menor equivalencia que contiene a $R$.

> [!example]- Solución
> **(a)** Si $(a, b) \in R^i$ y $(b, c) \in R^j$, entonces $(a, c) \in R^{i+j} \subseteq R^t$.
>
> **(b)** Sea $U = R \cup R^{-1} \cup I_A$; $(a, b) \in U^i$ significa que hay un camino $a = x_0, \dots, x_i = b$ con cada paso en $U$. *Contiene a $R$:* $R \subseteq U \subseteq U^t$. *Refleja:* $I_A \subseteq U$. *Simétrica:* como $U$ es simétrica, el camino invertido muestra $(b, a) \in U^i$. *Transitiva:* por (a). *Minimalidad:* si $E$ es de equivalencia y $R \subseteq E$, entonces $R^{-1}, I_A \subseteq E$ (simetría y reflexividad), luego $U \subseteq E$, y por inducción en $i$ (la transitividad de $E$ une un camino de largo $i$ y un paso) $U^i \subseteq E$ para todo $i$, así que $U^t \subseteq E$.

### 8. Conjuntos $\langle a \rangle_R$ que forman partición (I2, 2018-2)
Dada $R$ sobre $A$, sea $\langle a \rangle = \{b \mid (a, b) \in R\}$ y $S_R = \{\langle a \rangle \mid a \in A\}$. (a) Si $R$ es refleja y $S_R$ es partición de $A$, ¿es $R$ de equivalencia? (b) ¿Y si $R$ es simétrica en vez de refleja?

> [!example]- Solución
> **(a) Sí.** *Simétrica:* si $(a, b) \in R$, entonces $b \in \langle a \rangle$ y, por reflexividad, $b \in \langle b \rangle$; como $S_R$ es partición y las clases se solapan, $\langle a \rangle = \langle b \rangle$, y como $a \in \langle a \rangle$ resulta $a \in \langle b \rangle$, o sea $(b, a) \in R$. *Transitiva:* si $(a, b), (b, c) \in R$, entonces $\langle a \rangle = \langle b \rangle$ y $c \in \langle b \rangle = \langle a \rangle$.
>
> **(b) No.** En $A = \{1, 2\}$ con $R = \{(1, 2), (2, 1)\}$: $R$ es simétrica y $\langle 1 \rangle = \{2\}$, $\langle 2 \rangle = \{1\}$ forman una partición, pero $R$ no es refleja.

### 9. Intersección de equivalencias y un tablero (examen, 2026-1)
(a) Si $R_1, R_2$ son de equivalencia sobre $A$, $R_1 \cap R_2$ también. (b) En un tablero de ajedrez $8 \times 8$, $a\,R_1\,b$ si están en la misma fila y $a\,R_2\,b$ si tienen el mismo color. ¿Cuántas clases tiene $R_1 \cap R_2$?

> [!example]- Solución
> **(a)** Las tres propiedades se verifican en cada relación y se heredan a la intersección: $(a, a) \in R_1, R_2$; si $(a, b)$ está en ambas, $(b, a)$ también; y si $(a, b), (b, c)$ están en ambas, $(a, c)$ también. **(b)** Dos casillas son equivalentes si están en la misma fila y tienen el mismo color. En cada fila hay $4$ casillas de cada color, así que cada clase tiene $4$ casillas y hay $64 / 4 = 16$ clases (una por pareja fila-color, $8 \cdot 2$).

### 10. Relaciones de punto medio (I2, 2018-1)
$R$ es *de punto medio* si $(a, b) \in R$ implica que existe $c$ con $(a, c), (c, b) \in R$. (a) Si $A$ es finito, $R \neq \emptyset$ es transitiva y de punto medio, existe $x$ con $(x, x) \in R$. (b) ¿Vale con $A$ infinito?

> [!example]- Solución
> **(a)** Sea $(a, b) \in R$ y $n = \lvert A \rvert$. Aplicando punto medio a $(a, b)$ se obtiene $c_1$ con $(a, c_1), (c_1, b) \in R$; a $(a, c_1)$, un $c_2$ con $(a, c_2), (c_2, c_1) \in R$; y así sucesivamente, con $(c_{k+1}, c_k) \in R$. Entre $c_1, \dots, c_{n+1}$ hay dos iguales, $c_i = c_j$ con $i < j$. La cadena $c_j \to c_{j-1} \to \cdots \to c_i$ tiene al menos una flecha y por transitividad da $(c_j, c_i) = (c_i, c_i) \in R$. **(b) No.** $<$ sobre $\mathbb{R}$ es transitiva y de punto medio (entre $a < b$ siempre hay un real $\frac{a+b}{2}$), pero ningún $x$ cumple $x < x$.

### 11. Algoritmo de clausura transitiva (examen, 2024-2)
![Algoritmo de clausura transitiva](adjuntos/Algoritmo%20de%20clausura%20transitiva.png)

> [!example]- Transcripción de la imagen
> Pseudocódigo con entrada una relación binaria $R$ sobre un conjunto finito $A$ y salida $R^+$. Línea 1: $R^+ \leftarrow R$. Línea 2: $R_{prev} \leftarrow \emptyset$. Línea 3: mientras $R_{prev} \neq R^+$. Línea 4: $R_{prev} \leftarrow R^+$. Línea 5: $R^+ \leftarrow R^+ \cup (R^+ \circ R^+)$. Línea 6: fin del mientras. Línea 7: retornar $R^+$.

(a) Demuestre que el algoritmo calcula la clausura transitiva. (b) Dé una cota para el número de iteraciones.

> [!example]- Solución
> **(a)** Sea $R_i$ el valor de $R^+$ tras $i$ iteraciones. *Contiene a $R$:* cada iteración solo agrega pares. *Transitiva:* al terminar $R^+ = R^+ \cup (R^+ \circ R^+)$, o sea $R^+ \circ R^+ \subseteq R^+$. *Minimal:* si $S$ es transitiva y $R \subseteq S$, por inducción $R_i \subseteq S$: un par nuevo de $R_i \circ R_i$ es $(a, c)$ con $(a, b), (b, c) \in R_i \subseteq S$ y la transitividad de $S$ lo incluye. Además el ciclo termina, porque $R^+$ crece dentro del conjunto finito $A \times A$.
>
> **(b)** Cada iteración agrega al menos un par, luego hay a lo más $\lvert A \rvert^2$ iteraciones. Una cota más fina viene de que $R_i$ contiene exactamente los pares unidos por un camino de largo entre $1$ y $2^i$ (la composición duplica el alcance). Como bastan caminos de largo $\leq n = \lvert A \rvert$, tras $\lceil \log_2 n \rceil$ iteraciones se tiene la clausura y una más confirma que no cambió: $O(\log \lvert A \rvert)$ iteraciones. En una cadena de $9$ nodos, por ejemplo, el ciclo corre $4$ veces.

## Preguntas de repaso

> [!question]- ¿Qué se demuestra aparte en cada problema de «probar que es de equivalencia»?
> Las tres propiedades por separado: reflexividad (para todo $a$, $aRa$), simetría ($aRb \Rightarrow bRa$) y transitividad ($aRb \wedge bRc \Rightarrow aRc$). La pauta puntúa cada una.

> [!question]- ¿Cómo se prueba que una clausura es *la menor*?
> Probando tres cosas: que contiene a $R$, que cumple la propiedad y que está contenida en cualquier otra relación que contenga a $R$ y cumpla la propiedad (típicamente por inducción sobre la longitud de los caminos).

> [!question]- ¿Por qué en el ejercicio 8(a) hace falta la reflexividad para concluir la simetría?
> Porque sin ella $b$ podría no estar en $\langle b \rangle$ y no habría una clase compartida con $\langle a \rangle$; el contraejemplo del apartado (b) lo muestra: las clases son disjuntas pero $R$ no es refleja.
