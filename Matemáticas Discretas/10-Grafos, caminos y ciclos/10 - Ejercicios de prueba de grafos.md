---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - discretas/ejercicios
  - origen/complemento
prerrequisitos:
  - "[[06 - Grafos bipartitos y ciclos impares]]"
  - "[[08 - Ciclos hamiltonianos]]"
---

# Ejercicios de prueba de grafos

Las interrogaciones y exámenes usan los grafos de cuatro maneras: **demostraciones estructurales** (grados, cliques, ciclos, distancias), **formalización en lógica de predicados** de propiedades de grafos, **cardinalidad** de familias de grafos y **complejidad** (NP-completitud con cliques, subgrafos o ciclos hamiltonianos; reducción a SAT). En las demostraciones la pauta puntúa elegir el objeto correcto (un vértice, el camino más largo, dos vértices extremos) y cubrir todos los casos.

## Ejercicios

### 1. Propiedades de grafos en lógica de predicados (examen, 2016-2)
Con el predicado $E(x, y)$ ("hay una arista entre $x$ e $y$"), escriba fórmulas que un grafo satisface solo si: (a) es completo, (b) tiene un clique de tamaño $3$, (c) tiene un conjunto independiente de tamaño $3$, (d) tiene un ciclo de tamaño $4$, (e) todo par de vértices está a no más de $3$ pasos.

> [!example]- Solución
> (a) $\forall x \forall y\,(x = y \lor E(x, y))$.
>
> (b) $\exists x \exists y \exists z\,(x \neq y \land x \neq z \land y \neq z \land E(x,y) \land E(x,z) \land E(y,z))$.
>
> (c) igual a (b) con $\neg E$ en lugar de $E$.
>
> (d) $\exists w \exists x \exists y \exists z\,(\text{los cuatro distintos} \land E(w,x) \land E(x,y) \land E(y,z) \land E(z,w))$.
>
> (e) Se definen $\varphi_2(x, y) = \exists p\,(p \neq x \land p \neq y \land E(x,p) \land E(p,y))$ y $\varphi_3(x, y) = \exists p \exists q\,(p, q, x, y \text{ distintos} \land E(x,p) \land E(p,q) \land E(q,y))$. La fórmula es
> $\forall x \forall y\,(x = y \lor E(x,y) \lor \varphi_2(x,y) \lor \varphi_3(x,y))$.
>
> La disyunción con $x = y$ es necesaria: sin ella, la fórmula exigiría $x \neq y$ para todo par, incluido $x = y$, y sería insatisfacible.

### 2. Dos vértices con el mismo grado (examen, 2017-2)
Demuestre que todo grafo con más de un vértice tiene al menos dos vértices con el mismo grado.

> [!example]- Solución
> Por contradicción: si los $n$ grados fueran distintos, como cada grado está en $\{0, \dots, n-1\}$ (que tiene $n$ elementos), aparecerían todos. Pero un vértice de grado $n-1$ es adyacente a todos los demás, de modo que ninguno puede tener grado $0$. Contradicción.

### 3. Seis personas (interrogación 2, 2022-2)
¿Es cierto que entre $6$ personas siempre hay $3$ que se conocen mutuamente o $3$ que se desconocen mutuamente? Demuéstrelo con grafos.

> [!example]- Solución
> Sí. Sea $G$ el grafo de "se conocen" con $\lvert V \rvert = 6$; hay que mostrar un clique de tamaño $3$ en $G$ o en $\overline{G}$ (un clique en $\overline{G}$ es un conjunto de tres que no se conocen). Un vértice $v$ tiene $5$ posibles vecinos, así que o tiene al menos $3$ en $G$ o al menos $3$ en $\overline{G}$. Si tiene tres vecinos $x, y, z$ en $G$: si alguna arista une dos de ellos, junto con $v$ forma un triángulo en $G$; si no, $\{x,y,z\}$ es un clique en $\overline{G}$. El otro caso es idéntico intercambiando $G$ y $\overline{G}$. (Con $5$ personas es falso: $C_5$ no tiene ninguno de los dos.)

### 4. Un grafo y su complemento no tienen ambos diámetro mayor que 3 (examen, 2015-2)
El diámetro de $G$ es el más largo de los caminos más cortos entre dos vértices. Demuestre que $G$ y $\overline{G}$ no pueden tener ambos diámetro mayor que $3$.

> [!example]- Solución
> Si $D(G) \leq 3$ no hay nada que probar. Se supone $D(G) \geq 4$ y se muestra $D(\overline{G}) \leq 3$. **Si $G$ no es conexo**, vértices de componentes distintas son adyacentes en $\overline{G}$, y dos de una misma componente se unen en $\overline{G}$ a través de un vértice de otra: distancia $\leq 2$. **Si $G$ es conexo**, hay $u, v$ con $d(u, v) \geq 4$, así que $\{u, v\} \in \overline{E}$ y todo otro vértice no es adyacente a $u$ o no lo es a $v$ en $G$, es decir, es adyacente en $\overline{G}$ a $u$ o a $v$. Dos vértices $x, y$ se unen en $\overline{G}$ por $x u y$, $x v y$, $x u v y$ o $x v u y$: largo $\leq 3$.

### 5. Grado mínimo 2 implica ciclo (examen, 2025-1)
Sea $G$ un grafo simple con $n \geq 3$ vértices y grado mínimo $\delta(G) \geq 2$. Demuestre que contiene un ciclo.

> [!example]- Solución
> Se toma un camino sin vértices repetidos $(v_1, \dots, v_k)$ de **largo máximo**. Todos los vecinos de $v_k$ están en el camino: si hubiera uno fuera, se extendería el camino, contra la maximalidad. Como $\delta(v_k) \geq 2$ tiene un vecino $v_i$ distinto de $v_{k-1}$, con $i < k - 1$, y $(v_i, v_{i+1}, \dots, v_k, v_i)$ es un ciclo de largo al menos $3$.

### 6. Homomorfismos y grafo producto (examen, 2024-2)
Un homomorfismo $f : V \to V'$ de $G$ a $G'$ cumple $(u,v) \in E \Rightarrow (f(u), f(v)) \in E'$. El producto $G \times G'$ tiene vértices $V \times V'$ y arista entre $(u,u')$ y $(v,v')$ si $(u,v) \in E$ y $(u',v') \in E'$. Pruebe (a) que $G \times G'$ es homomorfo a $G$ y (b) que si $H$ es homomorfo a $G$ y a $G'$, es homomorfo a $G \times G'$.

> [!example]- Solución
> (a) La proyección $\pi(u, u') = u$ es homomorfismo: si $((u,u'), (v,v'))$ es arista del producto, en particular $(u, v) \in E$. (b) Si $f : H \to G$ y $g : H \to G'$ son homomorfismos, $h(s) = (f(s), g(s))$ lo es hacia el producto: para una arista $(s, t)$ de $H$, $(f(s), f(t)) \in E$ y $(g(s), g(t)) \in E'$, luego $(h(s), h(t))$ es arista del producto.

### 7. Cardinalidad de grafos con vértices en un conjunto infinito (interrogación 2, 2021-2)
Sea $A$ infinito y $\Gamma$ el conjunto de grafos con $V \subseteq A$. (a) Si $A$ es enumerable, $\Gamma$ lo es. (b) Si $A$ no es enumerable, $\Gamma$ tampoco. (c) $\Gamma/\!\cong$ es enumerable.

> [!example]- Solución
> (a) Un grafo es un par (conjunto finito $V \subseteq A$, $E \subseteq V \times V$). Los subconjuntos finitos de un conjunto enumerable son enumerables, y cada $V$ admite finitos $E$; una unión enumerable de conjuntos finitos es enumerable. (b) Los grafos $(\{a\}, \emptyset)$ con $a \in A$ forman un subconjunto de $\Gamma$ en biyección con $A$; si $\Gamma$ fuera enumerable, también lo sería este subconjunto y por tanto $A$. (c) Para cada $n$ hay finitas clases de isomorfismo de grafos con $n$ vértices (un representante en cada clase usa $n$ elementos de $A$), y todo grafo es finito; la unión sobre $n \in \mathbb{N}$ es enumerable.

### 8. Sub-Isomorphism es NP-completo (examen, 2018-2)
$\text{Sub-Isomorphism} = \{(G, H) \mid \exists G' \subseteq G,\ G' \cong H\}$. Demuestre que es NP-completo.

> [!example]- Solución
> **En NP:** el certificado es $(G', f)$ con $G'$ subgrafo de $G$ y $f$ la biyección; verificar que $G' \subseteq G$ y que $f$ preserva aristas toma tiempo polinomial. **NP-difícil:** reducción desde Clique. Dado $(G, k)$ se construye $(G, K_k)$: $G$ tiene un clique de tamaño $k$ si y solo si tiene un subgrafo isomorfo a $K_k$ (el subgrafo inducido por el clique).

### 9. Half-Circle es NP-completo (examen, 2017-2)
Un círculo es un ciclo sin vértices repetidos. $\text{Half-Circle}$ es el conjunto de grafos con $n$ vértices que tienen un círculo de tamaño $n/2$. Demuestre que es NP-completo.

> [!example]- Solución
> **En NP:** el certificado es la secuencia de vértices del círculo; se verifica en tiempo polinomial que son distintos, que consecutivos son adyacentes y que hay $n/2$. **NP-difícil:** reducción desde Hamiltoniano (ver [[08 - Ciclos hamiltonianos]]). Dado $G$ con $n$ vértices se construye $G'$ agregando $n$ vértices aislados. Si $G$ tiene ciclo hamiltoniano, es un círculo de tamaño $n$ = la mitad de los $2n$ vértices de $G'$. Recíprocamente, un círculo de tamaño $n$ en $G'$ no puede usar los aislados, así que usa $n$ vértices de $G$: es hamiltoniano. La construcción es polinomial.

### 10. Covid-3 se reduce a SAT (examen, 2020-2)
Un grafo es COVID-$k$ si tiene un clique y un conjunto independiente de tamaño $k$. Demuestre $\text{Covid-3} \propto \text{SAT}$.

> [!example]- Solución
> Con variables $p_{ij}$ ("hay arista entre $i$ y $j$") se define $\varphi = \varphi_1 \land \varphi_2 \land \varphi_3 \land \varphi_4$, con $\varphi_1 = \bigvee_{i,j,k \text{ distintos}} (p_{ij} \land p_{jk} \land p_{ki})$ (existe clique de tamaño $3$), $\varphi_2 = \bigvee_{i,j,k \text{ distintos}} (\neg p_{ij} \land \neg p_{jk} \land \neg p_{ki})$ (existe independiente de tamaño $3$), $\varphi_3 = \bigwedge_{\{i,j\} \in E} p_{ij}$ y $\varphi_4 = \bigwedge_{\{i,j\} \notin E} \neg p_{ij}$. $\varphi_3$ y $\varphi_4$ fuerzan la valuación $\sigma(p_{ij}) = 1 \iff \{i, j\} \in E$, y bajo ella $\varphi_1$ y $\varphi_2$ valen exactamente cuando el grafo tiene ambos conjuntos. La fórmula tiene tamaño polinomial.

## Preguntas de repaso

> [!question]- ¿Por qué en el ejercicio 5 se elige un camino de largo máximo?
> Porque la maximalidad garantiza que todos los vecinos del último vértice están ya en el camino; así su segundo vecino cierra un ciclo con un tramo del camino, sin necesidad de recorrer más el grafo.

> [!question]- ¿Qué técnica se repite en los ejercicios 3 y 4 sobre el complemento?
> Se analiza un vértice o un par de vértices extremos y se usa que lo que falta en $G$ aparece en $\overline{G}$; los casos se cubren completos (por ejemplo, vecinos o no vecinos).

> [!question]- ¿Por qué las reducciones de los ejercicios 8 y 9 solo tienen dos direcciones que verificar?
> Una reducción desde un problema NP-completo muestra "difícil" si la instancia transformada es sí exactamente cuando la original es sí; se prueban las dos implicancias y que la transformación es polinomial. Aparte hay que mostrar pertenencia a NP con un certificado verificable.
