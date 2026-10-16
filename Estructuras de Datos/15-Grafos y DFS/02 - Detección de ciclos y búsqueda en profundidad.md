---
ramo: "Estructuras de Datos"
tema: "Grafos y DFS"
tags:
  - edd
  - grafos
  - dfs
  - ciclos
  - origen/complemento
prerrequisitos:
  - "[[01 - Grafos y su representación]]"
---

# Detección de ciclos y búsqueda en profundidad

Para saber si un [[01 - Grafos y su representación|proyecto con requisitos]] es viable hay que detectar si su grafo tiene un **ciclo**. El algoritmo que resulta recorre el grafo **en profundidad**: avanza por las aristas hasta no poder más y después retrocede. Esa estrategia, la **DFS** (*Depth First Search*), es la base de muchos otros algoritmos sobre grafos.

> [!tip] Camino y ciclo
> Un **camino** es una secuencia de nodos $v_0, v_1, \dots, v_n$ en la que cada par consecutivo es una arista; su **largo** es $n$. Si $n > 0$ y $v_0 = v_n$, el camino es un **ciclo**, y un grafo con un ciclo es **cíclico**.

## Primer intento: los posteriores de un nodo

Y es **posterior** a X si $X \to Y$, o si $X \to Z$ e Y es posterior a Z. Calcular los posteriores es recursivo: se sigue cada arista de salida y se baja por ella antes de mirar la siguiente.

```
Posteriors(G, X):
    if X.visited = 1: return ∅        // sin esta línea, un ciclo hace que no termine
    X.visited ← 1
    P ← ∅
    for Y tal que X → Y:
        P ← P ∪ {Y} ∪ Posteriors(G, Y)
    return P
```

Sin marcar visitados, el algoritmo repite trabajo y, si hay un ciclo, **no termina**. Con la marca siempre termina, pero todavía no **detecta** ciclos. Llegar a un nodo ya visitado no basta, porque puede tratarse de dos caminos que llegan al mismo nodo sin formar ciclo.

## Colores: blanco, gris y negro

La clave es distinguir **por qué** está visitado un nodo. Mientras `Posteriors(G, X)` no retorna, todos los nodos que va marcando son posteriores a X. Si se vuelve a uno de ellos, hay ciclo.

- **Blanco:** no visitado.
- **Gris:** visitado y **en proceso**: es un ancestro del nodo actual en la recursión.
- **Negro:** visitado y **terminado**: todos sus posteriores ya se exploraron.

```
cycleAfter(G, X):                     isCyclic(G):
    if X.color = gris: return true        for X ∈ V(G):
    if X.color = negro: return false          if X.color ≠ blanco: continue
    X.color ← gris                            if cycleAfter(G, X): return true
    for Y tal que X → Y:                  return false
        if cycleAfter(G, Y): return true
    X.color ← negro
    return false
```

![Slide - detección de ciclos con colores](adjuntos/Slide%20-%20detecci%C3%B3n%20de%20ciclos%20con%20colores.png)

> [!example]- Transcripción de la imagen
> Slide "Detección de ciclos". Grafo con nodos Y, T, N, X, R, H, K y B. Y y T están en blanco (no visitados); N, X, R, H y K, en gris (en proceso); B, en negro (terminado). La arista R → H está marcada en rojo.

> [!warning] Llegar a un nodo negro no es un ciclo
> Si la arista lleva a un nodo **negro**, ese nodo ya terminó y no es ancestro del actual: otro camino llegó antes a él. Solo una arista hacia un nodo **gris** cierra un ciclo.

## DFS básico

Si se quita la parte de los ciclos, queda el recorrido puro, que solo cambia colores:

```
Dfs(G):                                DfsVisit(G, u):
    for u ∈ V(G): u.color ← blanco         u.color ← gris
    for u ∈ V(G):                          for v ∈ N_G(u):          // vecinos de u
        if u.color = blanco:                   if v.color = blanco:
            DfsVisit(G, u)                         DfsVisit(G, v)
                                           u.color ← negro
```

Cada nodo se inicializa una vez ($O(V)$), se visita una vez ($O(V)$) y cada arista se revisa una vez al mirar los vecinos ($O(E)$, con listas de adyacencias). **DFS toma $O(V + E)$**, es decir, es lineal en el tamaño del grafo.

## Preguntas de repaso

> [!question]- ¿Por qué marcar los nodos como visitados no basta para detectar ciclos?
> Porque un nodo puede estar visitado porque otro camino llegó antes a él (y ya terminó), sin que haya ciclo. Hay que distinguir si el nodo visitado es un ancestro en proceso (gris) o uno ya terminado (negro).

> [!question]- ¿Qué indica una arista hacia un nodo gris?
> Que ese nodo es un ancestro del actual en la recursión, es decir, que se puede volver a él: hay un ciclo.

> [!question]- ¿Por qué DFS es $O(V + E)$?
> Porque cada nodo pasa de blanco a gris y a negro una sola vez, y cada arista se examina una vez al recorrer los vecinos de su origen.

> [!question]- ¿Qué pasa con Posteriors si el grafo tiene un ciclo y no se marcan visitados?
> No termina: recorre el ciclo indefinidamente, volviendo a llamar a nodos que ya estaban en la pila de recursión.
