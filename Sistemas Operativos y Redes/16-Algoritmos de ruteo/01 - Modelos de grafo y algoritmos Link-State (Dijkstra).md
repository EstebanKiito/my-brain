---
ramo: "Sistemas Operativos y Redes"
tema: "Algoritmos de ruteo"
tags:
  - sistemas-operativos
  - redes
  - enrutamiento
  - grafos
  - link-state
  - dijkstra
  - origen/complemento
prerrequisitos:
  - "[[15-Capa de red y direccionamiento/_Índice|Capa de red y direccionamiento]]"
---

# Modelos de grafo y algoritmos Link-State (Dijkstra)

El [[15-Capa de red y direccionamiento/01 - Servicios de la capa de red: enrutamiento y reenvío|enrutamiento]] es la decisión distribuida que llena las tablas de reenvío. Para estudiarlo, la red se convierte en un problema de grafos: encontrar el camino de menor costo entre dos routers.

## La red como grafo

El conjunto de routers se modela como un **grafo $G = (V, E)$**:

- los **nodos** ($V$) son los routers;
- los **enlaces** son las **aristas** ($E$);
- cada arista tiene un **costo**, que puede representar ancho de banda, congestión, costo monetario, distancia, etc.

Hay dos familias de algoritmos según cuánto sabe cada nodo:

| | Centralizados: **Link-State (LS)** | Descentralizados: **Distance-Vector (DV)** |
|---|---|---|
| Qué conoce cada nodo | La información **completa** de la red | Solo a sus vecinos; no conoce la topología completa |
| Cómo calcula | Explora toda la red y cada nodo determina la ruta más conveniente | Cálculo **iterativo y distribuido** entre los nodos |
| Ejemplo | Dijkstra | Bellman-Ford (ver [[02 - Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito\|Distance-Vector]]) |

"Centralizado" no significa que un solo equipo calcule: cada router calcula por su cuenta, pero con el mapa completo de la red.

## Link-State

1. Cada nodo envía su **información de conectividad** (vecinos y costos) a sus vecinos.
2. La información llega a todos los demás vía **flooding** (cada uno reenvía lo que recibe).
3. Cuando todos conocen la topología, **cada uno calcula las rutas más cortas**, por ejemplo con el **algoritmo de Dijkstra** (1957).

![Algoritmo Link-State de Dijkstra con cálculo de caminos más cortos](adjuntos/Algoritmo%20Link-State%20de%20Dijkstra%20con%20c%C3%A1lculo%20de%20caminos%20m%C3%A1s%20cortos.png)

> [!example]- Transcripción de la imagen
> Grafo de seis routers con sus costos: u–v 2, u–x 1, u–w 5, v–x 2, v–w 3, x–w 3, x–y 1, w–y 1, w–z 5, y–z 2.

## Dijkstra paso a paso

Desde el nodo fuente $u$, el algoritmo mantiene el conjunto $N'$ de nodos cuyo camino mínimo ya se conoce, la distancia $D(v)$ y el predecesor $p(v)$ de cada nodo:

1. **Inicio**: $N' = \{u\}$; $D(v) = c(u, v)$ si $v$ es vecino de $u$, y $\infty$ si no.
2. Elegir el nodo $w \notin N'$ con menor $D(w)$ y agregarlo a $N'$.
3. Para cada vecino $v$ de $w$ fuera de $N'$: $D(v) = \min\big(D(v),\ D(w) + c(w, v)\big)$.
4. Repetir hasta que todos estén en $N'$.

Con el grafo de la figura:

| Paso | $N'$ | $D(v), p(v)$ | $D(w), p(w)$ | $D(x), p(x)$ | $D(y), p(y)$ | $D(z), p(z)$ |
|---|---|---|---|---|---|---|
| 0 | u | 2, u | 5, u | **1, u** | ∞ | ∞ |
| 1 | ux | 2, u | 4, x | | **2, x** | ∞ |
| 2 | uxy | **2, u** | 3, y | | | 4, y |
| 3 | uxyv | | **3, y** | | | 4, y |
| 4 | uxyvw | | | | | **4, y** |
| 5 | uxyvwz | | | | | |

Siguiendo los predecesores se obtiene el **árbol de caminos más cortos** desde $u$:

![Tabla de iteraciones y árbol de caminos más cortos en Dijkstra](adjuntos/Tabla%20de%20iteraciones%20y%20%C3%A1rbol%20de%20caminos%20m%C3%A1s%20cortos%20en%20Dijkstra.png)

> [!example]- Transcripción de la imagen
> El árbol resultante: U unido a V y a X; X unido a Y; Y unido a W y a Z.

Del árbol sale la tabla de reenvío de $u$: hacia $v$ se sale por el enlace $(u, v)$, y hacia $x$, $y$, $w$ y $z$, por $(u, x)$.

```python
import heapq

ENLACES = {("u","v"): 2, ("u","x"): 1, ("u","w"): 5, ("v","x"): 2, ("v","w"): 3,
           ("x","w"): 3, ("x","y"): 1, ("w","y"): 1, ("w","z"): 5, ("y","z"): 2}
G = {}
for (a, b), c in ENLACES.items():
    G.setdefault(a, {})[b] = c
    G.setdefault(b, {})[a] = c

def dijkstra(origen):
    D, p = {origen: 0}, {}
    cola, listos = [(0, origen)], set()           # listos = N'
    while cola:
        d, w = heapq.heappop(cola)                # el más cercano fuera de N'
        if w in listos:
            continue
        listos.add(w)
        for v, c in G[w].items():                 # actualizar a sus vecinos
            if v not in listos and d + c < D.get(v, float("inf")):
                D[v], p[v] = d + c, w
                heapq.heappush(cola, (D[v], v))
    return D, p

D, p = dijkstra("u")
for v in "vwxyz":
    salto = v
    while p[salto] != "u":                        # retroceder hasta el vecino de u
        salto = p[salto]
    print(f"{v}: D={D[v]} p={p[v]} salida por (u,{salto})")
# v: D=2 (u,v) | w: D=3 (u,x) | x: D=1 (u,x) | y: D=2 (u,x) | z: D=4 (u,x)
```

**Costo:** con $N$ nodos y $E$ enlaces, Link-State envía $O(NE)$ mensajes y cada nodo hace un cálculo de complejidad $O(N^2)$ (con una cola de prioridad, como en el código, baja a $O(E \log N)$). Ante una falla, se propaga la ausencia de un enlace local. En Internet lo implementa **OSPF**, cuyos anuncios de estado de enlace se llaman LSA (*Link-State Advertisements*), usado dentro de los sistemas autónomos (ver [[03 - Enrutamiento jerárquico y sistemas autónomos (Intra-AS e Inter-AS)|enrutamiento jerárquico]]).

## Preguntas de repaso

> [!question]- ¿Qué diferencia a un algoritmo Link-State de uno Distance-Vector?
> En Link-State cada nodo conoce la topología completa y calcula sus rutas solo. En Distance-Vector cada nodo solo conoce a sus vecinos y las rutas se calculan de forma iterativa y distribuida.

> [!question]- ¿Cómo obtiene cada router la topología completa en Link-State?
> Cada nodo envía sus vecinos y costos, y esa información se reparte a toda la red por flooding.

> [!question]- En el grafo de la figura, ¿por qué el camino más corto de u a w cuesta 3 y no 5?
> Porque u → x → y → w cuesta $1 + 1 + 1 = 3$, menos que el enlace directo u–w de costo 5.

> [!question]- ¿Cuántos mensajes y cuánto cálculo requiere Link-State?
> $O(NE)$ mensajes en total, y $O(N^2)$ operaciones en cada nodo con la implementación básica de Dijkstra.
