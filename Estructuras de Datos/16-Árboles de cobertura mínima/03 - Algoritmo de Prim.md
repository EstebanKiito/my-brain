---
ramo: "Estructuras de Datos"
tema: "Árboles de cobertura mínima"
tags:
  - edd
  - mst
  - prim
  - heap
  - origen/complemento
prerrequisitos:
  - "[[01 - Árboles de cobertura mínima y cortes]]"
  - "[[03 - Inserción y extracción en un heap]]"
---

# Algoritmo de Prim

**Prim** construye el MST como **un solo árbol** que crece desde un nodo inicial. En cada paso, el corte es (nodos del árbol, resto), y se agrega la arista **más barata que lo cruza**. Para encontrarla rápido, mantiene en una **cola de prioridad** (min heap) el costo más barato conocido para conectar cada nodo pendiente.

## La idea

1. $R = \{s\}$ (el nodo inicial) y $\bar R = V - R$.
2. Sea $e$ la arista de menor costo que cruza de $R$ a $\bar R$, y $u$ su extremo en $\bar R$.
3. Agregar $e$ al MST y pasar $u$ de $\bar R$ a $R$.
4. Si quedan nodos en $\bar R$, volver al paso 2.

El paso 2 es el caro. Para hacerlo eficiente, cada nodo $v$ pendiente guarda $d[v]$, el costo de la arista más barata que lo conecta al árbol, y $\pi[v]$, el nodo del árbol en el otro extremo. El heap ordena por $d[v]$.

```
Prim(s):
    Q ← cola de prioridad vacía (min heap)
    T ← lista vacía
    for u ∈ V − {s}: d[u] ← ∞; π[u] ← ∅; Insert(Q, u)
    d[s] ← 0; π[s] ← ∅; Insert(Q, s)
    while Q no está vacía:
        u ← Extract(Q)                       // el más barato de conectar
        T ← T ∪ {(π[u], u)}
        for v ∈ α[u]:                         // vecinos de u
            if v ∈ Q and d[v] > cost(u, v):
                d[v] ← cost(u, v); π[v] ← u
                DecreaseKey(Q, v, d[v])        // mejora su prioridad
    return T
```

> [!tip] Cambiar una prioridad dentro del heap
> Cuando aparece una arista más barata hacia $v$, hay que **bajar su clave** en el min heap (en un max heap sería subirla: `IncreaseKey`). Se cambia el valor y se hace [[03 - Inserción y extracción en un heap|SiftUp]]: como la propiedad de heap solo puede romperse en el camino de $v$ a la raíz, cuesta $O(\log V)$.

![Slide - Prim tras extraer los nodos 0 y 2](adjuntos/Slide%20-%20Prim%20tras%20extraer%20los%20nodos%200%20y%202.png)

> [!example]- Transcripción de la imagen
> Slide "Árboles de cobertura mínimos". El grafo de ejemplo durante Prim desde 0: los nodos 0 (clave 0) y 2 (clave 29, unido por la arista roja 0–2) ya están en el árbol (naranjo). Los demás muestran su clave $d$ actual: 6 → 51, 7 → 31, 1 → 32, 5 → 60 (aristas naranjas desde 0), y 3 y 4 → ∞.

![Slide - MST obtenido por Prim](adjuntos/Slide%20-%20MST%20obtenido%20por%20Prim.png)

> [!example]- Transcripción de la imagen
> Todos los nodos en el árbol (naranjo), con las aristas del MST en verde: 0–2 (29), 0–7 (31), 7–1 (21), 7–6 (25), 7–4 (46), 4–3 (34) y 3–5 (18). Junto a cada nodo, el costo con que se conectó.

En el ejemplo, Prim desde 0 extrae los nodos en el orden 0, 2, 7, 1, 6, 4, 3, 5, y obtiene el mismo MST de costo 204 que Kruskal.

```python
import heapq

def prim(ady, s):                       # ady[u] = [(costo, v), …]
    en_arbol, T, heap = set(), [], [(0, s, None)]
    while heap:
        d, u, p = heapq.heappop(heap)   # el más barato que cruza el corte
        if u in en_arbol: continue      # entrada obsoleta (reemplaza a DecreaseKey)
        en_arbol.add(u)
        if p is not None: T.append((p, u, d))
        for c, v in ady[u]:
            if v not in en_arbol: heapq.heappush(heap, (c, v, u))
    return T
```

En Python no hay `DecreaseKey`: se inserta de nuevo el nodo con la clave mejor y se ignoran las entradas obsoletas al extraerlas.

## Correctitud y complejidad

Por inducción sobre las iteraciones: tras la $n$-ésima extracción, $T$ es un MST del subgrafo $G_n$ formado por los $n$ nodos extraídos. Al extraer $u$, $(\pi[u], u)$ es la arista más barata que conecta $u$ con $G_n$. Agregarla mantiene la cobertura (se conecta $u$), no forma ciclo ($u$ no estaba) y el costo sigue siendo mínimo (propiedad del corte). Termina porque cada nodo se extrae una vez.

| Paso | Costo |
|---|---|
| $V$ extracciones del heap | $O(V \log V)$ |
| Cada arista se revisa una vez, con un posible `DecreaseKey` | $O(E \log V)$ |

Total $O((V + E) \log V)$. Como en un grafo conexo $E \ge V - 1$, **Prim es $O(E \log V)$**, igual que Kruskal.

## Preguntas de repaso

> [!question]- ¿Qué diferencia la estrategia de Prim de la de Kruskal?
> Prim hace crecer un solo árbol desde un nodo, agregando siempre la arista más barata que sale de él. Kruskal mantiene un bosque y agrega la arista más barata de todo el grafo que no forme ciclo.

> [!question]- ¿Qué representa $d[v]$ en Prim?
> El costo de la arista más barata conocida que conecta $v$ con el árbol actual. Es la prioridad de $v$ en el heap.

> [!question]- ¿Por qué DecreaseKey cuesta $O(\log V)$?
> Porque al bajar la clave de un nodo en un min heap, solo puede violarse la propiedad de heap en el camino hacia la raíz, y se corrige subiendo el nodo (SiftUp), a lo más $\log V$ niveles.

> [!question]- ¿Por qué la complejidad $O((V+E) \log V)$ se simplifica a $O(E \log V)$?
> Porque en un grafo conexo $E \ge V - 1$, así que $V \in O(E)$ y $V + E \in O(E)$.
