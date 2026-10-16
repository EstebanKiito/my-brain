---
ramo: "Estructuras de Datos"
tema: "Caminos más cortos"
tags:
  - edd
  - grafos
  - bellman-ford
  - caminos-mas-cortos
  - programacion-dinamica
  - origen/complemento
prerrequisitos:
  - "[[02 - Algoritmo de Dijkstra]]"
  - "[[01 - Subproblemas solapados y subestructura óptima]]"
---

# Algoritmo de Bellman-Ford

[[02 - Algoritmo de Dijkstra|Dijkstra]] falla con aristas negativas porque decide demasiado pronto: da por definitivo un nodo que todavía podría abaratarse por un camino con más aristas. **Bellman-Ford** no se apura. Revisa **todas** las aristas una y otra vez, admite **costos negativos** y, además, **detecta** si hay un **ciclo de costo negativo**, en cuyo caso no existe ruta más corta.

## Por qué no detenerse

Con costos negativos, un camino **más largo** (con más aristas) puede ser **más barato**. La estrategia es de **programación dinámica** sobre la cantidad de aristas:

- primero, las rutas más cortas desde $s$ con **a lo más 1** arista;
- con ellas, las de a lo más 2 aristas;
- y así sucesivamente: las rutas de a lo más $k$ aristas se construyen extendiendo las de a lo más $k - 1$.

¿Hasta cuándo? Una ruta más corta **no repite nodos**: si tuviera un ciclo de costo no negativo, se podría quitar sin empeorar. Por eso tiene a lo más $V - 1$ aristas, igual que un árbol de cobertura. Bastan $V - 1$ rondas.

![Pizarra - rutas con más aristas pero menor costo](adjuntos/Pizarra%20-%20rutas%20con%20m%C3%A1s%20aristas%20pero%20menor%20costo.png)

> [!example]- Transcripción de la imagen
> Foto de pizarra: dos nodos unidos por un camino directo y por otro camino más largo que da una vuelta. El dibujo ilustra que una ruta con más aristas puede terminar siendo más barata, por lo que hay que seguir revisando.

## Algoritmo

![Pseudocódigo de Bellman-Ford](adjuntos/Pseudoc%C3%B3digo%20de%20Bellman-Ford.png)

> [!example]- Transcripción de la imagen
> `BellmanFord(s)`: 1–2. `for u ∈ V: d[u] ← ∞; π[u] ← ∅`; 3. `d[s] ← 0`; 4. `for k = 1...|V| − 1:`; 5. `for (u, v) ∈ E:`; 6. `if d[v] > d[u] + cost(u, v):`; 7. `d[v] ← d[u] + cost(u, v)`; 8. `π[v] ← u`. "Al revisar $|V| - 1$ veces **todas** las aristas, nos aseguramos de actualizar rutas en caso de encontrar atajos".

> [!tip] Lo que el código no dice explícitamente
> Parece que relaja aristas sin seguir los caminos desde $s$. Pero mientras $d[u] = \infty$, la condición $d[v] > d[u] + cost$ nunca se cumple: solo se propagan las aristas que salen de nodos **ya alcanzados**. Así, en la ronda $k$ quedan correctas todas las rutas de a lo más $k$ aristas. El ciclo externo es solo un **contador** que limita la cantidad de aristas. A diferencia de Dijkstra, la ruta óptima a un nodo puede **cambiar** varias veces durante la ejecución.

## Detectar ciclos negativos

Si después de $V - 1$ rondas **todavía** se puede relajar alguna arista, existe un camino con más de $V - 1$ aristas que es más barato. Eso solo es posible si hay un **ciclo de costo negativo**: dando vueltas en él, el costo baja indefinidamente y **no hay ruta más corta**.

![Bellman-Ford con chequeo de ciclos negativos](adjuntos/Bellman-Ford%20con%20chequeo%20de%20ciclos%20negativos.png)

> [!example]- Transcripción de la imagen
> `ValidBellmanFord(s)`: las líneas 1–8 son iguales a BellmanFord; después, 9. `for (u, v) ∈ E:`; 10. `if d[v] > d[u] + cost(u, v):`; 11. `return false`; 12. `return true`. "El resultado de este algoritmo indica si los costos en $d$ son válidos como costos de rutas más cortas".

```python
def bellman_ford(G, s):                   # G[u] = [(v, costo)]
    d, pi = {u: float("inf") for u in G}, {u: None for u in G}
    d[s] = 0
    aristas = [(u, v, c) for u in G for v, c in G[u]]
    for _ in range(len(G) - 1):           # rutas de a lo más 1, 2, …, V-1 aristas
        for u, v, c in aristas:
            if d[u] + c < d[v]:
                d[v], pi[v] = d[u] + c, u
    valido = all(d[u] + c >= d[v] for u, v, c in aristas)   # ¿queda algo por relajar?
    return d, valido

T = {"A": [("B", 1), ("C", 2)], "B": [], "C": [("B", -3)]}
print(bellman_ford(T, "A"))               # ({'A': 0, 'B': -1, 'C': 2}, True)  donde Dijkstra daba B = 1
T2 = {"A": [("B", 1)], "B": [("C", 2)], "C": [("B", -3)]}
print(bellman_ford(T2, "A")[1])           # False: el ciclo B → C → B suma -1
```

## Complejidad

![Complejidad de Bellman-Ford](adjuntos/Complejidad%20de%20Bellman-Ford.png)

> [!example]- Transcripción de la imagen
> Actualización de costos: $\mathcal{O}(V)$ iteraciones, cada una con $\mathcal{O}(E)$ comparaciones; total $\mathcal{O}(VE)$. Chequeo de ciclos: $\mathcal{O}(E)$ comparaciones.

**Bellman-Ford es $O(VE)$**, más lento que Dijkstra ($O(E \log V)$). Se usa cuando puede haber costos negativos o cuando se necesita detectar ciclos negativos. Una mejora práctica es terminar antes si una ronda completa no actualizó nada. La versión distribuida de esta idea es el ruteo Distance-Vector: ver [[02 - Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito|Bellman-Ford en Redes]].

| | BFS | Dijkstra | Bellman-Ford |
|---|---|---|---|
| Costos | Todos iguales | No negativos | Cualquiera, sin ciclos negativos |
| Estructura | Cola FIFO | Min heap | Recorre todas las aristas |
| Estrategia | Por capas | Codiciosa | Programación dinámica |
| Complejidad | $O(V + E)$ | $O(E \log V)$ | $O(VE)$ |

## Preguntas de repaso

> [!question]- ¿Por qué bastan $V - 1$ rondas de relajación?
> Porque una ruta más corta no repite nodos (sin ciclos negativos), así que tiene a lo más $V - 1$ aristas, y la ronda $k$ deja correctas todas las rutas de a lo más $k$ aristas.

> [!question]- ¿Cómo detecta Bellman-Ford un ciclo negativo?
> Haciendo una ronda extra: si alguna arista todavía se puede relajar después de $V - 1$ rondas, hay un camino más barato con más de $V - 1$ aristas, lo que implica un ciclo de costo negativo.

> [!question]- ¿Por qué un grafo con un ciclo negativo alcanzable no tiene ruta más corta?
> Porque cada vuelta al ciclo reduce el costo total, así que siempre existe un camino más barato: el mínimo no existe.

> [!question]- ¿Cuándo conviene Dijkstra y cuándo Bellman-Ford?
> Dijkstra, cuando todos los costos son no negativos, porque es más rápido ($O(E \log V)$). Bellman-Ford, cuando hay costos negativos o hay que verificar que no existan ciclos negativos ($O(VE)$).
