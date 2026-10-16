---
ramo: "Estructuras de Datos"
tema: "Caminos más cortos"
tags:
  - edd
  - grafos
  - bfs
  - caminos-mas-cortos
  - origen/complemento
prerrequisitos:
  - "[[02 - Detección de ciclos y búsqueda en profundidad]]"
  - "[[03 - Pilas y colas]]"
---

# Búsqueda en amplitud (BFS)

Para planificar un viaje en auto entre dos ciudades, se modela la red de caminos como un **grafo dirigido con costos** y se busca la forma más barata de ir de A a C. Si todas las aristas costaran lo mismo, bastaría con **contar aristas**: gana el camino con menos aristas. Ese caso más simple se resuelve con la **búsqueda en amplitud** (*Breadth First Search*, BFS).

![Grafo dirigido con costos no negativos](adjuntos/Grafo%20dirigido%20con%20costos%20no%20negativos.png)

> [!example]- Transcripción de la imagen
> Grafo dirigido con nodos A, B, C, D, E, F, G y H y costos en las aristas (por ejemplo, F → B: 32, B → D: 29, A → C: 26, G → E: 93). "Notemos que en este problema, los costos son **no negativos**".

## La idea: recorrer por capas

DFS avanza en profundidad hasta no poder más. BFS, en cambio, explora **por distancia** desde el nodo inicial $s$: primero todos los nodos a distancia 1, después los de distancia 2, y así hasta cubrir el grafo. Para respetar ese orden usa una **cola FIFO**: los nodos se procesan en el orden en que se descubrieron.

$\delta(v)$ es la **menor cantidad de aristas** para llegar de $s$ a $v$, y $\pi[v]$ es el nodo desde el que se descubrió $v$.

![Pseudocódigo de BFS](adjuntos/Pseudoc%C3%B3digo%20de%20BFS.png)

> [!example]- Transcripción de la imagen
> input: vértice de inicio $s$. `BFS(s)`: `for u ∈ V − {s}: u.color ← blanco; u.δ ← ∞; π[u] ← ∅`; `s.color ← gris; s.δ ← 0; π[s] ← ∅`; `Q ← cola FIFO vacía; Insert(Q, s)`; `while Q no está vacía: u ← Extract(Q); for v ∈ α[u]: if v.color = blanco: v.color ← gris; v.δ ← u.δ + 1; π[v] ← u; Insert(Q, v)`; `u.color ← negro`.

```python
from collections import deque

def bfs(G, s):
    delta, pi = {u: float("inf") for u in G}, {u: None for u in G}
    delta[s] = 0
    Q = deque([s])                          # cola FIFO
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if delta[v] == float("inf"):     # blanco: aún no descubierto
                delta[v], pi[v] = delta[u] + 1, u
                Q.append(v)
    return delta, pi

L = {"A": ["C", "E"], "C": ["H"], "E": ["H", "F"], "F": ["E", "B"], "H": ["F", "D"],
     "B": ["D"], "D": ["G"], "G": ["A", "C", "E"]}
# delta: A 0, C 1, E 1, F 2, H 2, B 3, D 3, G 4;  pi[D] = H
```

![BFS - distancias desde A](adjuntos/BFS%20-%20distancias%20desde%20A.png)

> [!example]- Transcripción de la imagen
> "Ahora visitamos los nodos con $\delta = 4$ desde A". El grafo con las distancias en verde: A: 0; C y E: 1; F y H: 2; B y D: 3; G: 4. Las aristas usadas para descubrir cada nodo están en negrita. "Notemos que D no es descubierto desde B": se descubrió antes, desde H.

> [!tip] El árbol de rutas más cortas
> Al terminar, $\pi$ describe un **árbol de rutas más cortas** desde $s$: para reconstruir el camino a $v$, se siguen $\pi[v], \pi[\pi[v]], \dots$ hasta llegar a $s$. Cada nodo se descubre **una sola vez** y por la primera capa en que aparece, que es la de menor distancia.

En rigor, el color **negro** no hace falta: un nodo que sale de la cola no vuelve a entrar. Lo que importa es distinguir a los **blancos** (no descubiertos). Como DFS, BFS revisa cada nodo y cada arista una vez: **$O(V + E)$**.

> [!warning] Solo cuenta aristas
> BFS encuentra el camino con **menos aristas**, no el de **menor costo**. Si las aristas tienen costos distintos, un camino con más aristas puede ser más barato. Para eso está Dijkstra.

## Preguntas de repaso

> [!question]- ¿Por qué BFS usa una cola FIFO y no una pila?
> Porque necesita procesar los nodos en orden de distancia: los descubiertos primero, que están más cerca, deben explorarse antes. Con una pila se exploraría en profundidad, como DFS.

> [!question]- ¿Qué garantiza $\delta(v)$ al terminar BFS?
> Que es la menor cantidad de aristas de un camino de $s$ a $v$, porque $v$ se descubre en la primera capa en que es alcanzable y nunca se actualiza después.

> [!question]- En el ejemplo, ¿por qué D no queda como descubierto desde B?
> Porque H, que está a distancia 2, lo descubrió antes, en la capa de distancia 3. Cuando se procesa B, D ya no es blanco y no se vuelve a asignar.

> [!question]- ¿Cuándo BFS no sirve para encontrar el camino más corto?
> Cuando las aristas tienen costos distintos: BFS minimiza la cantidad de aristas, no la suma de costos.
