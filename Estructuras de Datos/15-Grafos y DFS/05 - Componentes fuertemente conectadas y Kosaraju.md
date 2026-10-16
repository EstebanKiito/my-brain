---
ramo: "Estructuras de Datos"
tema: "Grafos y DFS"
tags:
  - edd
  - grafos
  - componentes-fuertemente-conectadas
  - kosaraju
  - origen/complemento
prerrequisitos:
  - "[[04 - Orden topológico]]"
---

# Componentes fuertemente conectadas y Kosaraju

En un grafo con ciclos no hay orden topológico, pero sí hay una estructura útil: agrupar los nodos que **se alcanzan mutuamente**. Cada grupo se comporta como un solo "supernodo", y el grafo de supernodos ya **no tiene ciclos**. El algoritmo de **Kosaraju** encuentra esos grupos con dos DFS.

> [!tip] Definición
> Una **componente fuertemente conectada** (CFC) de un grafo dirigido $G$ es un conjunto **maximal** de nodos $C$ tal que, para todo $u, v \in C$, existe un camino dirigido de $u$ a $v$ (y por lo tanto también de $v$ a $u$).
>
> Los nodos de un **ciclo** pertenecen siempre a la misma CFC.

![Slide - componentes fuertemente conectadas](adjuntos/Slide%20-%20componentes%20fuertemente%20conectadas.png)

> [!example]- Transcripción de la imagen
> Slide "Componentes fuertemente conectadas". Grafo con nodos a, b, c, d, e, f, g y h. Aristas: a → b, b → e, e → a, b → c, b → f, e → f, c → d, d → c, c → g, d → h, f → g, g → f, g → h y un lazo h → h. Las zonas sombreadas marcan las 4 CFC: {a, b, e}, {c, d}, {f, g} y {h}. Debajo, el grafo de componentes: abe → cd, abe → fg, cd → fg, cd → h, fg → h. "Cada componente tiene un **representante** que combina sus nodos".

## Grafo de componentes

Si se contrae cada CFC en un nodo, se obtiene el **grafo de componentes** $G^{CFC}$: hay una arista $(C_i, C_j)$ si alguna arista de $G$ va de un nodo de $C_i$ a uno de $C_j$.

> [!tip] Teorema
> $G^{CFC}$ es un grafo dirigido **acíclico**. Por lo tanto, tiene un orden topológico.

Si hubiera un ciclo entre componentes, todos sus nodos se alcanzarían mutuamente y formarían una sola CFC más grande, lo que contradice la maximalidad.

## Grafo transpuesto

El **transpuesto** $G^T$ tiene los mismos nodos y todas las aristas **invertidas**: $(u, v) \in E(G) \Rightarrow (v, u) \in E(G^T)$. Una propiedad clave es que **$G$ y $G^T$ tienen las mismas CFC**, porque invertir todas las aristas no cambia quién alcanza a quién de forma mutua. Lo que sí cambia es que, en $G^T$, ya no se puede "escapar" de una componente hacia las que venían después en $G$.

## Algoritmo de Kosaraju

1. Ejecutar DFS sobre $G$ y ordenar los nodos por tiempo de término **decreciente** (como en TopSort). Como $G$ es cíclico, esto **no** es un orden topológico, aunque se construya igual.
2. Recorrer $G^T$ en ese orden: cada nodo todavía sin representante inicia un recorrido que asigna su representante a todos los que alcanza en $G^T$. Esos nodos son exactamente su CFC.

```
Kosaraju(G):                         Assign(G, u, r):
    L ← TopSort(G)                       if u.rep = ∅:
    for u ∈ L:                               u.rep ← r
        Assign(G, u, u)                      for v ∈ N_{G^T}(u):
                                                 Assign(G, v, r)
```

![Slide - Kosaraju sobre el grafo transpuesto](adjuntos/Slide%20-%20Kosaraju%20sobre%20el%20grafo%20transpuesto.png)

> [!example]- Transcripción de la imagen
> Slide "Hacia un algoritmo para determinar las CFC". Arriba, el orden de los nodos según los tiempos de término: b, a, e, c, d, g, h, f. Abajo, el grafo transpuesto (aristas invertidas) con los tiempos de término de cada nodo: b 16, e 15, a 14, c 10, d 9, g 7, h 6, f 4. Las CFC están sombreadas. "La forma en que recorremos las componentes nos da su orden topológico": (bae)(cd)(gf)(h).

```python
def kosaraju(G):
    L = topsort(G)                                   # orden decreciente de término
    GT = {u: [] for u in G}
    for u in G:
        for v in G[u]: GT[v].append(u)               # transponer
    rep = {}
    def assign(u, r):
        if u not in rep:
            rep[u] = r
            for v in GT[u]: assign(v, r)
    for u in L: assign(u, u)
    return rep

H = {"a": ["b"], "b": ["c", "e", "f"], "c": ["d", "g"], "d": ["c", "h"], "e": ["a", "f"],
     "f": ["g"], "g": ["f", "h"], "h": ["h"]}
# componentes: {a, b, e}, {c, d}, {f, g}, {h}
```

Son dos DFS más la transposición, así que Kosaraju es **$O(V + E)$**. Además, las componentes aparecen **en orden topológico** de $G^{CFC}$.

## Preguntas de repaso

> [!question]- ¿Por qué los nodos de un ciclo están en la misma CFC?
> Porque siguiendo el ciclo, cada nodo alcanza a todos los demás, así que se alcanzan mutuamente.

> [!question]- ¿Por qué el grafo de componentes es acíclico?
> Si hubiera un ciclo entre componentes, todos los nodos de esas componentes se alcanzarían mutuamente y deberían formar una sola CFC, lo que contradice que las CFC son maximales.

> [!question]- ¿Para qué recorre Kosaraju el grafo transpuesto?
> Para que el recorrido desde un nodo quede atrapado en su propia componente. Al invertir las aristas, desde una componente "temprana" ya no se puede llegar a las que en $G$ estaban después de ella.

> [!question]- ¿El orden de término de la primera DFS es un orden topológico de $G$?
> No: $G$ tiene ciclos y no tiene orden topológico. Se construye igual que uno, pero solo sirve para decidir en qué orden se recorren los nodos en $G^T$.
