---
ramo: "Estructuras de Datos"
tema: "Caminos más cortos"
tags:
  - edd
  - grafos
  - dijkstra
  - caminos-mas-cortos
  - greedy
  - origen/complemento
prerrequisitos:
  - "[[01 - Búsqueda en amplitud (BFS)]]"
  - "[[03 - Algoritmo de Prim]]"
---

# Algoritmo de Dijkstra

**Dijkstra** generaliza BFS a aristas con **costos no negativos**. En vez de una cola FIFO usa una **cola de prioridad** (min heap) ordenada por $d[v]$, el costo del mejor camino conocido desde $s$. En cada paso extrae el nodo **más barato** de alcanzar, lo da por terminado y trata de mejorar a sus vecinos. Su estructura es casi idéntica a la de [[03 - Algoritmo de Prim|Prim]]; la diferencia es que la prioridad es el costo **acumulado** desde $s$ y no el costo de una sola arista.

## Algoritmo

![Pseudocódigo de Dijkstra](adjuntos/Pseudoc%C3%B3digo%20de%20Dijkstra.png)

> [!example]- Transcripción de la imagen
> `Dijkstra(s)`: `for u ∈ V − {s}: u.color ← blanco; d[u] ← ∞; π[u] ← ∅`; `s.color ← gris; d[s] ← 0; π[s] ← ∅`; `Q ← cola de prioridades vacía (Min Heap); Insert(Q, s)`; `while Q no está vacía: u ← Extract(Q); for v ∈ α[u]: if v.color = blanco ∨ v.color = gris: if d[v] > d[u] + cost(u, v): d[v] ← d[u] + cost(u, v); π[v] ← u; DecreaseKey(Q, v, d[v])`; `if v.color = blanco: v.color ← gris; Insert(Q, v)`; `u.color ← negro`. "Solo cambia costo + ruta si hay arista que baja el costo".

- **Blanco:** no descubierto. **Gris:** está en el heap con un costo provisorio. **Negro:** extraído; su $d$ es **definitivo**.
- **Relajar** la arista $(u, v)$ es preguntar si llegar a $v$ pasando por $u$ es más barato que lo conocido. Si lo es, se actualizan $d[v]$ y $\pi[v]$.

> [!warning] Orden de las operaciones con un nodo blanco
> Un nodo blanco todavía **no está en el heap**, así que no se le puede aplicar `DecreaseKey`. Lo correcto es: si $v$ es **gris** y mejora, `DecreaseKey`; si $v$ es **blanco**, asignar $d[v]$ y **insertarlo** (pintándolo gris).

```python
import heapq

def dijkstra(G, s):                          # G[u] = [(v, costo)]
    d, pi = {u: float("inf") for u in G}, {u: None for u in G}
    d[s] = 0
    Q, negro = [(0, s)], set()
    while Q:
        du, u = heapq.heappop(Q)
        if u in negro: continue              # entrada obsoleta
        negro.add(u)                         # d[u] queda fija
        for v, c in G[u]:
            if v not in negro and d[v] > du + c:   # solo blancos o grises
                d[v], pi[v] = du + c, u
                heapq.heappush(Q, (d[v], v)) # hace las veces de Insert/DecreaseKey
    return d, pi
```

![Dijkstra - distancias finales desde 0](adjuntos/Dijkstra%20-%20distancias%20finales%20desde%200.png)

> [!example]- Transcripción de la imagen
> Grafo dirigido con nodos 0 a 7 y costos, todos los nodos ya negros. Junto a cada nodo, su distancia final desde 0 (en verde): 0: 0, 2: 26, 4: 38, 7: 60, 5: 73, 3: 99, 1: 105, 6: 151. Las aristas en negrita forman el árbol de rutas más cortas (por ejemplo, 0 → 2 → 7 → 3 → 6).

## Por qué funciona y cuándo falla

Dijkstra es un algoritmo **codicioso**: da por definitivo el nodo más barato del heap sin volver a revisarlo. Es correcto gracias a la **subestructura óptima** de las rutas más cortas: todo tramo de una ruta mínima también es mínimo. Si existiera un atajo intermedio más barato, la ruta no sería mínima. El supuesto escondido es que **agregar aristas a un camino nunca lo abarata**, y eso solo vale si **no hay costos negativos**.

![Grafo con una arista de costo negativo](adjuntos/Grafo%20con%20una%20arista%20de%20costo%20negativo.png)

> [!example]- Transcripción de la imagen
> Grafo con tres nodos: A → B con costo 1, A → C con costo 2 y C → B con costo −3.

![Pizarra - Dijkstra con un costo negativo](adjuntos/Pizarra%20-%20Dijkstra%20con%20un%20costo%20negativo.png)

> [!example]- Transcripción de la imagen
> Foto de pizarra del mismo ejemplo: A unido a B (costo 1) y a C (costo 2), C → B con −3, y los nodos tachados a medida que Dijkstra los termina; junto a B aparece −1, el costo que Dijkstra no encuentra.

![Dijkstra falla con el costo negativo](adjuntos/Dijkstra%20falla%20con%20el%20costo%20negativo.png)

> [!example]- Transcripción de la imagen
> "El estado final de los parámetros nos entrega la ruta encontrada por Dijkstra": $(d[X], \pi[X])$ = A $(0, \varnothing)$, B $(1, A)$, C $(2, A)$, con la cola vacía. "La ruta de A hasta B entregada cumple $cost((A,B)) = 1 > -1 = cost((A, C, B))$".

Dijkstra extrae B con costo 1 y lo pinta de **negro**. Cuando después procesa C y descubre que $2 - 3 = -1$ es mejor, B ya está terminado y no se actualiza. El algoritmo entrega 1 en vez de −1.

**Complejidad** con un heap binario: cada nodo se extrae una vez ($O(V \log V)$) y cada arista puede provocar un `DecreaseKey` ($O(E \log V)$). En total, $O((V + E) \log V)$, es decir, $O(E \log V)$ en grafos conexos. El mismo algoritmo se usa en redes como ruteo Link-State: ver [[01 - Modelos de grafo y algoritmos Link-State (Dijkstra)|Dijkstra en Redes]].

## Preguntas de repaso

> [!question]- ¿Qué diferencia a Dijkstra de BFS?
> BFS usa una cola FIFO y minimiza la cantidad de aristas. Dijkstra usa una cola de prioridad por costo acumulado y minimiza la suma de costos, con costos no negativos.

> [!question]- ¿Por qué un nodo negro ya no se actualiza en Dijkstra?
> Porque cuando se extrae del heap es el más barato pendiente, y con costos no negativos ningún camino que pase por otros nodos pendientes puede costar menos. Su distancia es definitiva.

> [!question]- Explicar con el ejemplo A, B, C por qué Dijkstra falla con costos negativos.
> Extrae B con $d = 1$ y lo termina. Después, al procesar C, el camino A → C → B cuesta $-1$, pero B ya es negro y no se actualiza. Queda 1 en vez de −1.

> [!question]- ¿Qué relación hay entre Dijkstra y Prim?
> Ambos extraen repetidamente el nodo de menor prioridad de un min heap y actualizan a sus vecinos. Prim usa como prioridad el costo de la arista que conecta con el árbol; Dijkstra, el costo acumulado desde el origen.
