---
ramo: "Matemáticas Discretas"
tema: "Conjunto cuociente, órdenes y elementos extremos"
tags:
  - discretas/ordenes
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[02 - Construcción de Z y de los naturales módulo n]]"
  - "[[07 - Órdenes completos y el caso de los racionales]]"
---

# Ejercicios de prueba de cuocientes y órdenes

Las interrogaciones repiten tres formatos: **demostrar que una relación es de equivalencia o de orden** (refleja, simétrica o antisimétrica, transitiva, con casos), **trabajar con cuocientes** (clases, cantidad de clases, orden entre clases) y **calcular o demostrar supremos, ínfimos y extremos**. La pauta puntúa cada propiedad por separado, así que conviene ordenarlas y cerrar cada una con su justificación.

## Ejercicios

### 1. Cuociente inducido por una función (examen, 2022-1)
Sea $f : A \to B$ y $R_f$ dada por $x\,R_f\,y \iff f(x) = f(y)$. Demuestre que $R_f$ es de equivalencia y que $\lvert A/R_f \rvert = \lvert \operatorname{img}(f) \rvert$.

> [!example]- Solución
> Refleja, simétrica y transitiva se heredan de la igualdad en $B$. Se define $g : A/R_f \to \operatorname{img}(f)$ por $g([a]) = f(a)$; está bien definida porque $[a] = [a']$ implica $f(a) = f(a')$. Es inyectiva ($[a] \ne [b]$ implica $f(a) \ne f(b)$) y sobreyectiva (si $c = f(a)$, entonces $g([a]) = c$). Luego hay una biyección. Por ejemplo, con $f(x) = x^2 \bmod 7$ sobre $\{0,\dots,19\}$ hay $4$ clases y $4$ valores distintos.

### 2. Cuasi-orden (I2, 2025-1)
Una relación refleja y transitiva se llama cuasi-orden. Demuestre que si $R$ lo es, entonces $R \cap R^{-1}$ es de equivalencia.

> [!example]- Solución
> **Refleja:** $(a,a) \in R$ y $(a,a) \in R^{-1}$. **Simétrica:** $(a,b) \in R \cap R^{-1}$ equivale a $(a,b) \in R$ y $(b,a) \in R$, condición simétrica en $a,b$. **Transitiva:** si $(a,b)$ y $(b,c)$ están en $R\cap R^{-1}$, entonces $(a,b),(b,c) \in R$ da $(a,c) \in R$, y $(c,b),(b,a) \in R$ da $(c,a) \in R$; luego $(a,c) \in R \cap R^{-1}$.

### 3. Preorden por ínfimo y supremo (I2, 2015-2)
Sea $\mathcal{F}$ el conjunto de subconjuntos finitos y no vacíos de $\mathbb{N}$ y $A \preceq B \iff \min A \le \min B \wedge \max A \le \max B$. (a) Pruebe que es refleja y transitiva. (b) Pruebe que no es orden parcial. (c) Dé un $S \subseteq \mathcal{F}$ donde sí lo sea.

> [!example]- Solución
> (a) Se hereda de $\le$ en los mínimos y en los máximos. (b) Falla la antisimetría: $A = \{1,2,3\}$ y $B = \{1,3\}$ cumplen $A \preceq B$ y $B \preceq A$ (mismos mínimo y máximo) pero $A \ne B$. (c) Basta que no haya dos elementos distintos con el mismo par (mínimo, máximo): $S = \{\{1\},\{2\},\{1,2\}\}$ tiene pares $(1,1),(2,2),(1,2)$, todos distintos, así que $A \preceq B$ y $B \preceq A$ fuerzan $A = B$. Se verificó por enumeración que es un orden parcial (de hecho total: $\{1\} \preceq \{1,2\} \preceq \{2\}$).

### 4. Orden lexicográfico (I2, 2022-2)
Sean $(A,\preceq_A)$ y $(B,\preceq_B)$ órdenes parciales. En $A \times B$ se define $(a_1,b_1) \preceq (a_2,b_2)$ si (i) $a_1 \ne a_2$ y $a_1 \preceq_A a_2$, o (ii) $a_1 = a_2$ y $b_1 \preceq_B b_2$. Demuestre que es un orden parcial.

> [!example]- Solución
> **Refleja:** vale (ii) con $a=a$ y $b \preceq_B b$. **Antisimétrica:** (i) no puede valer en ambos sentidos (daría $a_1 \preceq_A a_2 \preceq_A a_1$ con $a_1 \ne a_2$, contra la antisimetría de $\preceq_A$); luego valen (ii) en ambos, y $a_1 = a_2$, $b_1 \preceq_B b_2 \preceq_B b_1$ da $b_1 = b_2$. **Transitiva:** con $(a_1,b_1) \preceq (a_2,b_2) \preceq (a_3,b_3)$: (i)(i) da $a_1 \preceq_A a_3$ y $a_1 \ne a_3$ (si fueran iguales, $a_1 \preceq_A a_2 \preceq_A a_1$ daría $a_1 = a_2$); (i)(ii) y (ii)(i) dan $a_1 \ne a_3$ con $a_1 \preceq_A a_3$; (ii)(ii) da $a_1 = a_3$ y $b_1 \preceq_B b_3$. En todos los casos vale (i) o (ii) para los extremos.

### 5. Orden sobre intervalos (I2, 2022-1)
Sea $X$ el conjunto de intervalos $[a,b] = \{c \in \mathbb{N} \mid a \le c \le b\}$ y $R$ dada por $I_1\,R\,I_2$ si $x \le y$ para todo $x \in I_1$ e $y \in I_2$. (a) Pruebe que su clausura refleja $R^r$ es un orden parcial. (b) Dé un $S \ne \emptyset$ sin mínimo.

> [!example]- Solución
> (a) **Refleja** por ser clausura. **Antisimétrica:** si $I_1\,R\,I_2$ y $I_2\,R\,I_1$ con $I_i = [a_i,b_i]$, entonces $a_1 \le b_1 \le a_2 \le b_2 \le a_1$, luego todo es igual y $I_1 = I_2 = [a,a]$. **Transitiva:** si $I_1 R I_2$ e $I_2 R I_3$, para $x \in I_1$, $z \in I_3$ y cualquier $y \in I_2$ se tiene $x \le y \le z$, así que $I_1 R I_3$. (b) $S = \{[1,3],[2,4]\}$: $3 \in [1,3]$ y $2 \in [2,4]$ con $2<3$, y $4\in[2,4]$, $3 \in [1,3]$ con $3<4$. Son incomparables, y ninguno es mínimo.

### 6. Orden de subcadena (examen, 2016-2)
Sobre $\Sigma^*$, $w \trianglelefteq s$ si $w$ aparece como bloque contiguo de $s$. Demuestre que es un orden parcial y estudie mínimo y máximo.

> [!example]- Solución
> **Refleja:** $w$ está en $w$ desde la posición $1$. **Antisimétrica:** si cada una es subcadena de la otra, tienen el mismo largo, y una subcadena del mismo largo es la cadena misma. **Transitiva:** si $w$ empieza en la posición $k$ de $s$ y $s$ en la $j$ de $u$, $w$ empieza en la posición $j + k - 1$ de $u$. **Mínimo:** $\varepsilon$ (la palabra vacía) es subcadena de todas. **Máximo:** no hay: para cualquier $s$ y una letra $a$, $sa$ no es subcadena de $s$ por ser más larga. (Si no se cuenta $\varepsilon$, el mínimo sólo existe cuando el alfabeto tiene una letra.)

### 7. Supremo e ínfimo en $(\mathcal{P}(A),\subseteq)$ (I2, 2016-2)
Pruebe que $\sup\{C,D\} = C \cup D$, $\inf\{C,D\} = C \cap D$, y en general $\sup\mathcal{B} = \bigcup\mathcal{B}$ e $\inf\mathcal{B} = \bigcap\mathcal{B}$ para $\mathcal{B} \subseteq \mathcal{P}(A)$.

> [!example]- Solución
> $\bigcup\mathcal{B}$ es cota superior porque cada $X \in \mathcal{B}$ cumple $X \subseteq \bigcup\mathcal{B}$. Si $U$ es otra cota superior, $X \subseteq U$ para todo $X \in \mathcal{B}$, de modo que todo elemento de la unión está en $U$: $\bigcup\mathcal{B} \subseteq U$. Es entonces la menor cota superior. Para el ínfimo, $\bigcap\mathcal{B}$ está contenida en cada $X$ y toda cota inferior $L$ está contenida en cada $X$, luego en la intersección. Los casos $\{C,D\}$ son $\mathcal{B} = \{C,D\}$.

### 8. Supremo en un orden total (I2, 2019-2)
Sea $(A,\preceq)$ total y $S$ finito no vacío. (a) Pruebe que $\sup S$ e $\inf S$ existen y pertenecen a $S$. (b) Si $S_1$ tiene supremo y $S_2 \subsetneq S_1$ cumple que para todo $x \in S_1$ hay $y \in S_2$ con $x \preceq y$, pruebe que $\sup S_2 = \sup S_1$.

> [!example]- Solución
> (a) Inducción en $\lvert S \rvert$. Con un elemento es él mismo. Con $S = S' \cup \{x\}$ y $m = \sup S' \in S'$, por conexidad $x \preceq m$ o $m \preceq x$; el mayor de los dos es cota superior de $S$, pertenece a $S$ y es el menor de las cotas posibles. Análogo para el ínfimo. (b) Toda cota superior de $S_1$ lo es de $S_2 \subseteq S_1$, luego $\sup S_1$ es cota superior de $S_2$. Si $c$ fuera cota superior de $S_2$ con $c \prec \sup S_1$, $c$ no sería cota de $S_1$: habría $x \in S_1$ con $c \prec x$, y por hipótesis $y \in S_2$ con $x \preceq y$, de donde $c \prec y$, contradicción. Así $\sup S_1$ es la menor cota superior de $S_2$.

### 9. Refinamiento de particiones (I2, 2024-2)
Sean $\mathbb{P}(A)$ las particiones de $A$ y $P \preceq P'$ si todo bloque de $P$ está contenido en algún bloque de $P'$. (a) Demuestre que es un orden parcial. (b) ¿Es total? (c) Demuestre que $\{P,P'\}$ tiene ínfimo.

> [!example]- Solución
> (a) **Refleja:** cada bloque está en sí mismo. **Transitiva:** $X \subseteq Y \subseteq Z$. **Antisimétrica:** si $P \preceq P' \preceq P$ y $X \in P$, existen $Y \in P'$ y $Z \in P$ con $X \subseteq Y \subseteq Z$; como $X \ne \emptyset$, $X \cap Z \ne \emptyset$ y por ser partición $X = Z$, luego $X = Y \in P'$. Análogamente $P' \subseteq P$. (b) No: en $\{1,2,3,4\}$, $\{\{1,2\},\{3,4\}\}$ y $\{\{1\},\{2,3,4\}\}$ son incomparables. (c) El ínfimo es $Q = \{X \cap Y \mid X \in P,\ Y \in P',\ X\cap Y \ne \emptyset\}$: es una partición, es cota inferior de ambas y, si $I$ es cota inferior de ambas, cada bloque $Z$ de $I$ está en un $X$ y un $Y$, luego en $X \cap Y \in Q$. Se comprobó por enumeración en las 15 particiones de $\{1,2,3,4\}$.

### 10. Funciones, preorden y orden en el cuociente (I2, 2017-2)
Sea $F$ el conjunto de funciones $A \to A$, $A$ finito, y $f_1 \rightsquigarrow f_2$ si existe $f$ con $f \circ f_1 = f_2$. (a) Pruebe que $\rightsquigarrow$ es refleja y transitiva. (b) $f_1 \sim f_2$ si $f_1 \rightsquigarrow f_2$ y $f_2 \rightsquigarrow f_1$: pruebe que es de equivalencia. (c) En $F/{\sim}$, $[f_1] \preceq [f_2]$ si $f_1 \rightsquigarrow f_2$: pruebe que es orden parcial y halle mínimo y máximo.

> [!example]- Solución
> (a) Con $f = \mathrm{id}$ se tiene reflexividad; si $f \circ f_1 = f_2$ y $g \circ f_2 = f_3$, entonces $(g\circ f)\circ f_1 = f_3$. (b) Refleja y transitiva por (a), simétrica por definición. (c) $\preceq$ está bien definido y hereda reflexividad y transitividad; antisimétrica: $[f_1] \preceq [f_2] \preceq [f_1]$ da $f_1 \sim f_2$, o sea $[f_1] = [f_2]$. Interpretación: $f_1 \rightsquigarrow f_2$ cuando $f_1(x) = f_1(y)$ implica $f_2(x) = f_2(y)$, es decir, la partición de $A$ en fibras de $f_1$ refina la de $f_2$; las clases agrupan funciones con las mismas fibras. El **mínimo** es la clase de las biyecciones (desde ellas se llega a cualquier función) y el **máximo** la de las constantes (a ellas se llega desde toda función). Con $\lvert A \rvert = 3$ hay $27$ funciones y $5$ clases, una por cada partición de $A$; las biyecciones son $6$ y las constantes $3$.

### 11. Todo orden parcial finito cabe en un orden total (I2, 2026-1)
Sea $A$ finito. Demuestre que todo orden parcial $\preceq$ sobre $A$ es subconjunto de un orden total sobre $A$.

> [!example]- Solución
> Se define $f(a) = \lvert \{x \in A \mid x \preceq a\} \rvert$. Si $x \preceq y$ y $x \ne y$, todo $z \preceq x$ cumple $z \preceq y$ (transitividad) y además $y \preceq y$ pero $y \not\preceq x$ (antisimetría), así que $f(x) < f(y)$. Se numeran los elementos de $A$ arbitrariamente y se ordena por el par $(f(a),\text{número})$ de forma lexicográfica; es un orden total y, si $x \preceq y$, $x$ queda antes que $y$. Se comprobó con órdenes parciales aleatorios.

## Preguntas de repaso

> [!question]- ¿Por qué para probar un orden parcial se demuestran las tres propiedades por separado?
> Porque la pauta asigna puntaje por cada una y porque cada una usa una herramienta distinta: reflexividad por definición, antisimetría por doble desigualdad o inclusión y transitividad por encadenar.

> [!question]- ¿Qué indica que una relación refleja y transitiva no sea antisimétrica?
> Que es un preorden: hay elementos distintos que se comparan en ambos sentidos. Al identificarlos (cuociente por $R\cap R^{-1}$) se obtiene un orden parcial, como en los ejercicios 2, 3 y 10.

> [!question]- ¿Qué se prueba primero al mostrar que $\sup\mathcal{B} = \bigcup\mathcal{B}$: que es cota o que es la menor?
> Ambas hacen falta: primero que es cota superior y luego que cualquier otra cota superior la contiene.
