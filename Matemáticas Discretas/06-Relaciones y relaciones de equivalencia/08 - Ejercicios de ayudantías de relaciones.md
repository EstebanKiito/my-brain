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

# Ejercicios de ayudantías de relaciones

Cuatro ejercicios de ayudantía: demostrar propiedades de una relación definida a partir de otra estructura, caracterizar cuándo una unión es de equivalencia, construir los racionales como cuociente y relacionar composición con equivalencia. En todos la composición es $R \circ S = \{(a, c) \mid \exists b\ (a, b) \in R \wedge (b, c) \in S\}$. Conviene intentar cada uno antes de abrir la solución.

## Ejercicios

### 1. Conjuntos buenos para la suma
Un conjunto $X \subseteq \mathbb{R}$ es *bueno para la suma* si $0 \in X$ y, para todo $x, y \in X$, $x + y \in X$. Dado $X$, se define en $\mathbb{R}$ la relación $x\,R_X\,y \iff (x - y) \in X$. Demuestre que si $X$ es bueno para la suma, $R_X$ es refleja y transitiva.

> [!example]- Solución
> **Refleja:** para todo $x$, $x - x = 0 \in X$, luego $x\,R_X\,x$. **Transitiva:** si $x\,R_X\,y$ e $y\,R_X\,z$, entonces $x - y \in X$ y $y - z \in X$. Como $X$ es cerrado bajo la suma, $(x - y) + (y - z) = x - z \in X$, es decir $x\,R_X\,z$.
>
> Con $X = \mathbb{N}$ se obtiene la relación $\geq$ (refleja y transitiva, no simétrica); con $X = \{0\}$, la igualdad. La simetría exigiría además que $X$ sea cerrado bajo opuestos.

### 2. Unión de equivalencias y composición
Sean $R_1$ y $R_2$ relaciones de equivalencia sobre $A$. Demuestre que $R_1 \cup R_2$ es de equivalencia si y solo si $R_1 \cup R_2 = R_1 \circ R_2$.

> [!example]- Solución
> ($\Rightarrow$) Sea $R_1 \cup R_2$ de equivalencia. *Inclusión $\subseteq$:* si $(x, y) \in R_1$, usando $(y, y) \in R_2$ resulta $(x, y) \in R_1 \circ R_2$; si $(x, y) \in R_2$, usando $(x, x) \in R_1$ resulta lo mismo. *Inclusión $\supseteq$:* si $(x, z) \in R_1$ y $(z, y) \in R_2$, ambos pares están en $R_1 \cup R_2$ y, por transitividad de esta, $(x, y) \in R_1 \cup R_2$.
>
> ($\Leftarrow$) Sea $R_1 \cup R_2 = R_1 \circ R_2$. **Refleja:** $(x, x) \in R_1$. **Simétrica:** si $(x, y)$ está en $R_1$ (o en $R_2$), su vuelta $(y, x)$ también, por simetría de cada una. **Transitiva:** dados $(x, y), (y, z) \in R_1 \cup R_2$ hay cuatro casos. Si ambos están en $R_1$ (o ambos en $R_2$), la transitividad de esa relación da $(x, z)$. Si $(x, y) \in R_1$ y $(y, z) \in R_2$, entonces $(x, z) \in R_1 \circ R_2 = R_1 \cup R_2$. Si $(x, y) \in R_2$ y $(y, z) \in R_1$, se invierten ambos pares: $(z, y) \in R_1$ y $(y, x) \in R_2$ dan $(z, x) \in R_1 \circ R_2 = R_1 \cup R_2$, y por simetría $(x, z) \in R_1 \cup R_2$.

### 3. Los racionales como cuociente
Sea $Q = \mathbb{Z} \times (\mathbb{Z} \setminus \{0\})$ y $(a, b) \uparrow (c, d) \iff ad = bc$.
(a) Demuestre que $\uparrow$ es de equivalencia. (b) Interprete $Q/{\uparrow}$. (c) Defina una suma y (d) un producto sobre las clases que imiten a los racionales, con un ejemplo.

> [!example]- Solución
> **(a)** Refleja: $ab = ba$. Simétrica: $ad = bc$ implica $cb = da$. Transitiva: de $(m, n) \uparrow (r, s)$ y $(r, s) \uparrow (t, u)$ se tiene $ms = nr$ y $ru = st$. Entonces $msu = nru = nst$ y, como $s \neq 0$, $mu = nt$, que es $(m, n) \uparrow (t, u)$.
>
> **(b)** $ad = bc$ equivale a $\tfrac{a}{b} = \tfrac{c}{d}$, así que la clase $[(a, b)]$ contiene exactamente los pares que representan la fracción $a/b$. Se nombra esa clase como el racional $a/b$ y $Q/{\uparrow} = \mathbb{Q}$.
>
> **(c)** $[(a, b)] +_\uparrow [(c, d)] = [(ad + bc,\, bd)]$. Por ejemplo, $[(21, 5)] +_\uparrow [(-7, 2)] = [(21 \cdot 2 + 5 \cdot (-7),\, 10)] = [(7, 10)] = 0{,}7$, que coincide con $\tfrac{21}{5} - \tfrac{7}{2}$.
>
> **(d)** $[(a, b)] \cdot_\uparrow [(c, d)] = [(ac,\, bd)]$. Por ejemplo, $[(21, 5)] \cdot_\uparrow [(-7, 2)] = [(-147, 10)] = -14{,}7$, igual a $\tfrac{21}{5} \cdot \left(-\tfrac{7}{2}\right)$. Falta comprobar que el resultado no depende del representante: si se cambia $(a, b)$ por $(ka, kb)$ con $k \neq 0$, el par $(ad + bc, bd)$ pasa a $(k(ad + bc), kbd)$, que es equivalente.

### 4. La composición de equivalencias (repaso de la segunda interrogación)
Sean $S, T$ relaciones de equivalencia sobre $A$. Demuestre que $S \circ T = T \circ S \iff S \circ T$ es una relación de equivalencia.

> [!example]- Solución
> ($\Rightarrow$) Asuma $S \circ T = T \circ S$. **Refleja:** $(a, a) \in S$ y $(a, a) \in T$. **Simétrica:** si $(a, b) \in S \circ T$, hay $z$ con $(a, z) \in S$, $(z, b) \in T$; por simetría $(b, z) \in T$ y $(z, a) \in S$, es decir $(b, a) \in T \circ S = S \circ T$. **Transitiva:** sean $a\,S\,z_1\,T\,b$ y $b\,S\,z_2\,T\,c$. Como $z_1\,T\,b\,S\,z_2$, se tiene $(z_1, z_2) \in T \circ S = S \circ T$, o sea hay $w$ con $z_1\,S\,w\,T\,z_2$. Entonces $a\,S\,z_1\,S\,w$ da $a\,S\,w$ y $w\,T\,z_2\,T\,c$ da $w\,T\,c$, luego $(a, c) \in S \circ T$.
>
> ($\Leftarrow$) Si $S \circ T$ es de equivalencia, es simétrica: $S \circ T = (S \circ T)^{-1} = T^{-1} \circ S^{-1} = T \circ S$, usando que $S$ y $T$ son simétricas.

## Preguntas de repaso

> [!question]- En el ejercicio 1, ¿por qué no se concluye que $R_X$ sea simétrica?
> Porque $X$ solo es cerrado bajo la suma: $x - y \in X$ no garantiza que $y - x = -(x - y)$ esté en $X$. Con $X = \mathbb{N}$, $R_X$ es $\geq$, que no es simétrica.

> [!question]- ¿Qué caso del ejercicio 2 usa de verdad que la unión es simétrica?
> El de $(x, y) \in R_2$ e $(y, z) \in R_1$: se necesita invertir ambos pares para poder aplicar la definición de $R_1 \circ R_2$ en el orden correcto.

> [!question]- ¿Por qué en el ejercicio 3 hay que verificar que la suma no depende del representante?
> Porque una clase tiene infinitos representantes y la suma se calcula con uno de ellos; si el resultado dependiera de la elección, la operación no estaría bien definida sobre clases.
