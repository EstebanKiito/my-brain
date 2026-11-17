---
ramo: "Matemáticas Discretas"
tema: "Grafos, caminos y ciclos"
tags:
  - discretas/grafos
  - origen/complemento
prerrequisitos:
  - "[[01 - Definición de grafo y tipos de aristas]]"
  - "[[04 - Isomorfismo y complemento de grafos]]"
---

# Caminatas y conectividad

La pregunta central sobre un grafo es "¿se puede llegar de aquí a allá?". Para responderla se define qué es un recorrido, se usa la relación "estar conectados" (que resulta ser de equivalencia) y sus clases son las piezas del grafo, llamadas componentes conexas.

## Recorridos

Una **caminata** es una secuencia de vértices $(v_0, v_1, \dots, v_k)$ con $(v_{i-1}, v_i) \in E$ para cada $i$: se va saltando de vértice en vértice por aristas. Es **cerrada** si $v_0 = v_k$. Un **camino** es una caminata que no repite aristas y un **ciclo** es una caminata cerrada que no repite aristas. El **largo** es la cantidad de aristas; un solo vértice es una caminata de largo $0$.

| Recorrido | Aristas repetidas | Cerrado |
|---|---|---|
| Caminata | sí, permitido | no necesariamente |
| Camino | no | no necesariamente |
| Ciclo | no | sí |

En el ramo estas definiciones solo prohíben repetir **aristas**; los vértices sí pueden repetirse. Cuando se quiere un ciclo "de verdad" (como $C_n$) se usa un ciclo sin vértices repetidos salvo el inicial y final, y los hamiltonianos lo exigen explícitamente.

## Conectividad y componentes

Dos vértices $x, y$ están **conectados** si existe un camino de $x$ a $y$. Esta relación es de equivalencia:

- **Refleja:** el camino de largo $0$, $(v)$, une $v$ consigo mismo.
- **Simétrica:** si $(v_1, u_1, \dots, u_n, v_2)$ es un camino, recorrerlo al revés lo es también, porque $E$ es simétrica.
- **Transitiva:** de $v_1$ a $v_2$ y de $v_2$ a $v_3$ se concatenan los caminos; si repiten aristas, se corta el segundo en el último vértice que comparte con el primero y se sigue desde ahí.

Sus clases de equivalencia son las **componentes conexas** (junto con las aristas entre sus vértices). Un grafo es **conexo** si todo par de vértices está conectado, o sea, si tiene una única componente conexa; si no, es **disconexo**.

> [!tip] Contar componentes con aristas
> Un grafo con $n$ vértices y $k$ aristas tiene al menos $n - k$ componentes conexas. Sin aristas hay $n$ componentes (cada vértice es la suya) y cada arista agregada reduce las componentes en a lo más $1$ (solo cuando une dos componentes distintas). Corolario: un grafo conexo con $n$ vértices tiene al menos $n - 1$ aristas.

Ejemplo: $5$ vértices y $3$ aristas $\{1,2\}, \{2,3\}, \{4,5\}$ tienen componentes $\{1,2,3\}$ y $\{4,5\}$, es decir $2 \geq 5 - 3$.

## Aristas y vértices de corte

Una **arista de corte** es una arista cuya eliminación aumenta la cantidad de componentes conexas; un **vértice de corte** lo es si al eliminarlo (con sus aristas incidentes) aumenta esa cantidad. Representan puntos débiles de una red: un puente que, si falla, parte la red en dos.

> [!tip] Caracterización de las aristas de corte
> Una arista es de corte si y solo si **no pertenece a ningún ciclo**.

Se puede suponer $G$ conexo (si no, se trabaja en la componente de la arista).

- Si la arista $\{u, v\}$ está en un ciclo $C$, al quitarla $u$ y $v$ siguen conectados por el resto de $C$. Cualquier camino que usaba $\{u, v\}$ se reemplaza dando el rodeo por $C$, así que el grafo sigue conexo: no es de corte.
- Si $\{u, v\}$ no es de corte, al sacarla el grafo sigue conexo y hay un camino $P$ de $u$ a $v$ sin ella. Agregando la arista $\{u, v\}$ a $P$ se forma un ciclo que la contiene.

**Aplicación:** en $C_4$ ninguna arista es de corte (todas están en el ciclo); en $P_4$ las tres lo son (no hay ciclos). Esta caracterización es la base de una de las definiciones equivalentes de árbol.

> [!warning] Arista de corte no es vértice de corte
> En $P_3 = (1, 2, 3)$ las dos aristas son de corte y el vértice $2$ también, pero los extremos $1$ y $3$ no son de corte: borrarlos deja el grafo conexo. Las dos nociones son distintas.

## Preguntas de repaso

> [!question]- ¿Por qué "estar conectados" necesita que el grafo sea no dirigido para ser simétrica?
> Porque la simetría de la relación sale de que cada arista se pueda recorrer en ambos sentidos. En un grafo dirigido puede haber camino de $x$ a $y$ sin camino de $y$ a $x$.

> [!question]- ¿Cuántas componentes conexas tiene, como mínimo, un grafo con $10$ vértices y $4$ aristas?
> Al menos $10 - 4 = 6$. La cota se alcanza cuando cada arista une dos componentes distintas, es decir, cuando ninguna arista cierra un ciclo; si alguna lo hace, hay más componentes.

> [!question]- ¿Por qué una arista dentro de un ciclo nunca es de corte?
> Porque al quitarla sus extremos siguen unidos por el otro lado del ciclo, de modo que todo recorrido que pasaba por ella tiene un desvío y la conectividad no cambia.
