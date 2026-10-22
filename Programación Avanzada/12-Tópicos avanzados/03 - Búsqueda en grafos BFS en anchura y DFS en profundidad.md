---
ramo: "Programación Avanzada"
tema: "Tópicos avanzados"
tags:
  - programacion/grafos
  - programacion/algoritmos
  - origen/complemento
prerrequisitos:
  - "[[02 - Grafos y representaciones listas y matrices de adyacencia]]"
  - "[[04 - Colas FIFO y deques de doble extremo]]"
---

# Búsqueda en grafos BFS en anchura y DFS en profundidad

Una vez representado un grafo en memoria, necesitamos responder preguntas concretas: ¿existe un camino entre dos nodos?, ¿cuál es la ruta con menor cantidad de conexiones?, o ¿cómo recorrer todos los nodos accesibles sin quedar atrapados en un bucle infinito? Para responderlas existen dos algoritmos fundamentales de exploración: **BFS** y **DFS**.

## El peligro de los ciclos y el conjunto de visitados

A diferencia de los árboles binarios donde solo existe un camino descendente, los grafos pueden contener **ciclos** (caminos cerrados que regresan al mismo nodo). Si un algoritmo recorre vecinos sin memoria, caerá en un bucle infinito de visitas repetidas.

> [!warning] La regla fundamental de recorrido en grafos
> Es obligatorio mantener una estructura de **conjunto de visitados** (`visitados = set()`). Antes de encolar o apilar un nodo vecino, se comprueba si ya fue visitado; si no lo está, se añade al conjunto inmediatamente.

## BFS: Búsqueda en Anchura (Breadth-First Search)

**BFS** recorre el grafo de forma radial por niveles concéntricos: primero visita al nodo origen, luego a todos sus vecinos directos (a distancia 1), luego a los vecinos de sus vecinos (a distancia 2), y así sucesivamente.

- **Estructura subyacente:** utiliza una **Cola FIFO** (`collections.deque`).
- **Propiedad clave:** en grafos no ponderados, **BFS garantiza encontrar el camino con el menor número de aristas (saltos)** entre el origen y el destino.

```python
from collections import deque

def bfs_recorrido(grafo: dict, inicio: str) -> list:
    visitados = {inicio}
    cola = deque([inicio])
    orden_visita = []

    while cola:
        nodo_actual = cola.popleft()  # Extrae del frente (FIFO)
        orden_visita.append(nodo_actual)

        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

    return orden_visita
```

## DFS: Búsqueda en Profundidad (Depth-First Search)

**DFS** avanza tan profundo como sea posible a lo largo de una rama explorando nodos sucesivos hasta alcanzar un callejón sin salida (un nodo sin vecinos no visitados); en ese punto retrocede (**backtracking**) al nodo previo para explorar ramas alternativas.

- **Estructura subyacente:** utiliza una **Pila LIFO** (con una lista `list` y `pop()`), o se implementa de forma recursiva aprovechando la pila de llamadas (*call stack*) de Python.
- **Casos de uso:** detección de ciclos, resolución de laberintos y ordenamiento topológico.

```python
def dfs_recursivo(grafo: dict, nodo: str, visitados: set = None) -> list:
    if visitados is None:
        visitados = set()

    visitados.add(nodo)
    recorrido = [nodo]

    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:
            recorrido.extend(dfs_recursivo(grafo, vecino, visitados))

    return recorrido
```

### Comparativa: BFS frente a DFS

```
+--------------------+---------------------------------+---------------------------------+
| Criterio           | BFS (Anchura)                   | DFS (Profundidad)               |
+--------------------+---------------------------------+---------------------------------+
| Estructura         | Cola FIFO (deque)               | Pila LIFO (stack o recursión)   |
| Estrategia         | Ondas concéntricas por nivel    | Ramas hasta el fondo y retroceso|
| Camino más corto   | **Garantizado** (en saltos)     | No garantizado                  |
| Uso de memoria     | Proporcional al ancho del nivel | Proporcional a la profundidad   |
| Complejidad tiempo | $O(|V| + |E|)$                  | $O(|V| + |E|)$                  |
+--------------------+---------------------------------+---------------------------------+
```

> [!tip] Cuándo elegir cuál
> Si buscas la **ruta más corta** o el amigo más cercano en una red social $\rightarrow$ usa **BFS**. Si buscas verificar **conectividad completa**, resolver un puzzle explorando caminos o detectar ciclos $\rightarrow$ usa **DFS**.

## Preguntas de repaso

> [!question]- ¿Por qué BFS garantiza encontrar el camino más corto en un grafo no ponderado?
> Porque explora exhaustivamente todos los nodos a distancia $k$ antes de examinar cualquier nodo a distancia $k + 1$, asegurando que la primera vez que alcance el destino será por la ruta de menor cantidad de aristas.

> [!question]- ¿Qué estructura de datos permite transformar un algoritmo de búsqueda de anchura (BFS) a profundidad (DFS)?
> Cambiar la cola FIFO (`deque.popleft()`) por una pila LIFO (`list.pop()`); el resto de la lógica de exploración y registro de visitados permanece idéntica.

> [!question]- ¿Qué problema ocurre si se ejecuta un DFS recursivo sobre un grafo muy grande o con ciclos si no se usa un conjunto `visitados`?
> Caerá en un bucle infinito de llamadas recursivas que agotará el límite de la pila de ejecución de Python, arrojando un error `RecursionError: maximum recursion depth exceeded`.

> [!question]- ¿Cuál es la complejidad temporal de recorrer un grafo con listas de adyacencia usando BFS o DFS?
> Es $O(|V| + |E|)$, ya que cada vértice se encola/visita a lo sumo una vez y cada arista se examina un número constante de veces.

