---
ramo: "Estructuras de Datos"
tema: "Grafos y DFS"
tags:
  - edd
  - grafos
  - orden-topologico
  - dfs
  - origen/complemento
prerrequisitos:
  - "[[03 - Tiempos de DFS y tipos de aristas]]"
---

# Orden topológico

Volviendo al [[01 - Grafos y su representación|proyecto con requisitos]]: si el grafo no tiene ciclos, hay que encontrar un **orden** en que ejecutar las tareas de modo que cada una vaya después de sus requisitos. Eso es un **orden topológico**, y DFS lo entrega casi gratis.

> [!tip] Definición
> Un **orden topológico** de un grafo dirigido $G$ es una secuencia $v_0, v_1, \dots, v_n$ de sus nodos en la que cada nodo aparece **exactamente una vez** y, si $(v_i, v_j) \in E$, entonces $v_i$ aparece **antes** que $v_j$.
>
> **Si $G$ es cíclico, no existe orden topológico**: en un ciclo, cada nodo tendría que ir antes que sí mismo.

## La idea: ordenar por tiempo de término decreciente

En un grafo acíclico, si hay una arista $(u, v)$, entonces $v$ **termina antes** que $u$ en DFS: o es descendiente de $u$, o ya había terminado (arista cruzada). Nunca puede ser una arista hacia atrás. Por eso, ordenar los nodos de **mayor a menor tiempo de término** pone cada nodo antes que todos los nodos a los que apunta.

![Slide - orden topológico desde los tiempos de término](adjuntos/Slide%20-%20orden%20topol%C3%B3gico%20desde%20los%20tiempos%20de%20t%C3%A9rmino.png)

> [!example]- Transcripción de la imagen
> Slide "Orden topológico". El grafo acíclico de 7 nodos con sus intervalos: 0 [7, 14], 1 [8, 13], 3 [9, 12], 2 [10, 11], 4 [1, 6], 6 [2, 5], 5 [3, 4]. "Deducimos el orden topológico de $G$ dado por" 0, 1, 3, 2, 4, 6, 5: los nodos ordenados de mayor a menor tiempo de término.

```
TopSort(G):
    L ← lista vacía
    Dfs(G)
    insertar en L los nodos en orden decreciente según end
    return L
```

Para no tener que ordenar al final, basta con **insertar cada nodo como cabeza de $L$ en el momento en que termina** (dentro de `DfsVisit`, justo después de asignar `u.end`). El último en terminar queda primero, y el algoritmo sigue siendo **$O(V + E)$**.

```python
def topsort(G, orden=None):
    L, visto = [], set()
    def visit(u):
        visto.add(u)
        for v in G[u]:
            if v not in visto: visit(v)
        L.insert(0, u)                 # al terminar u, va a la cabeza
    for u in (orden or G):
        if u not in visto: visit(u)
    return L

G = {0: [1, 3], 1: [3, 4], 2: [5], 3: [2, 4, 5, 6], 4: [6], 5: [], 6: [5]}
print(topsort(G, orden=[4, 0, 1, 2, 3, 5, 6]))   # [0, 1, 3, 2, 4, 6, 5]
```

> [!warning] El orden topológico no es único
> Dependiendo de por qué nodo parta DFS y en qué orden recorra los vecinos, se obtienen órdenes distintos, todos válidos. Lo que se garantiza es que cada arista va "hacia adelante" en la secuencia.

## Preguntas de repaso

> [!question]- ¿Por qué un grafo cíclico no tiene orden topológico?
> Porque si $v_0 \to v_1 \to \dots \to v_0$, cada nodo del ciclo debería aparecer antes que el siguiente, y $v_0$ terminaría teniendo que ir antes que sí mismo.

> [!question]- ¿Por qué ordenar por tiempo de término decreciente da un orden topológico en un grafo acíclico?
> Porque para toda arista $(u, v)$, $v$ termina antes que $u$ (no hay aristas hacia atrás). Al ordenar de mayor a menor término, $u$ queda antes que $v$.

> [!question]- ¿Cómo se evita ordenar al final en TopSort?
> Insertando cada nodo como cabeza de la lista en el momento en que termina. Así la lista queda en orden decreciente de término sin un paso extra.

> [!question]- ¿Cuál es la complejidad de TopSort?
> $O(V + E)$, la misma que DFS, porque solo agrega una inserción en $O(1)$ al terminar cada nodo.
