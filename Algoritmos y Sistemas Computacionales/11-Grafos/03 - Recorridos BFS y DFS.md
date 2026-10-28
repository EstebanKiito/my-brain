---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Grafos"
tags:
  - algoritmos/grafos
  - algoritmos/bfs
  - algoritmos/dfs
  - origen/complemento
prerrequisitos:
  - "[[02 - Representación de grafos|Representación de grafos]]"
---

# Recorridos BFS y DFS

Dado un grafo, una de las preguntas más básicas es cómo recorrerlo: visitar todos los nodos alcanzables sin repetir ninguno. Hay dos estrategias clásicas: **BFS** (*Breadth-First Search*), que explora por niveles, y **DFS** (*Depth-First Search*), que explora en profundidad.

## BFS: explorar por niveles

BFS visita primero los vecinos más cercanos y después los siguientes niveles. Usa una **cola** (FIFO): el primero que entra es el primero que sale.

![Grafo de ejemplo: A conectado con B y C; B con D; C con E](adjuntos/Grafo%20de%20ejemplo%20para%20BFS.png)

> [!example]- Transcripción de la imagen
> - Nodos $A$, $B$, $C$, $D$ y $E$.
> - $A$ está conectado con $B$ y $C$; $B$ con $D$; $C$ con $E$.
> - Comenzando en $A$, el recorrido BFS es $A, B, C, D, E$.
> - Primero se visita el nivel 0 ($A$), luego el nivel 1 ($B, C$) y luego el nivel 2 ($D, E$).

El pseudocódigo es:

```
BFS(G, s)
    crear cola Q
    marcar s como visitado
    encolar(Q, s)
    mientras Q no esté vacía
        u = desencolar(Q)
        visitar(u)
        para cada vecino v de u
            si v no ha sido visitado
                marcar v como visitado
                encolar(Q, v)
```

BFS sirve para encontrar el camino más corto en cantidad de aristas cuando el grafo no tiene pesos, para descubrir contactos a distancia 1, 2, 3… y para verificar conectividad. Su complejidad es $O(V + E)$.

## DFS: explorar en profundidad

DFS sigue un camino hasta el fondo y luego retrocede para probar otra rama. Usa una **pila** (LIFO) o recursión: la pila de llamadas hace el trabajo.

En el mismo grafo, un recorrido DFS posible es $A, B, D, C, E$: se sigue $A \to B \to D$, se retrocede y se explora $C \to E$.

```
DFS(G, u)
    marcar u como visitado
    visitar(u)
    para cada vecino v de u
        si v no ha sido visitado
            DFS(G, v)
```

DFS sirve para detectar ciclos, encontrar componentes conexas, hacer ordenamiento topológico y explorar todas las posibilidades (*backtracking*). Su complejidad también es $O(V + E)$.

## BFS frente a DFS

| Criterio | BFS | DFS |
|---|---|---|
| Estructura | Cola (FIFO) | Pila o recursión |
| Exploración | Por niveles | En profundidad |
| Camino más corto (sin pesos) | Sí | No |
| Detección de ciclos | Posible | Natural |

> [!tip] La idea central
> Ambos recorren el grafo en $O(V + E)$, pero el orden cambia. BFS responde "¿cuál es el camino con menos aristas?"; DFS responde "¿qué hay en cada rama?".

## Componentes conexas y ciclos

Una **componente conexa** es un conjunto de nodos donde todos son alcanzables entre sí. BFS y DFS permiten encontrarlas: se recorre desde un nodo, se marca todo lo alcanzable y, si quedan nodos sin visitar, se empieza otra componente.

Un **ciclo** es un camino que vuelve al punto de partida. DFS es la herramienta natural para detectarlo: si al explorar un vecino se llega a un nodo ya visitado que no es el padre, hay un ciclo.

> [!warning] En un grafo dirigido, un ciclo puede ser difícil de ver
> Que haya un camino de $A$ a $B$ y de $B$ a $A$ no siempre significa un ciclo en el sentido del recorrido; hay que revisar la dirección de cada arista.

> [!tip] Para profundizar
> Los recorridos y sus aplicaciones se ven con más detalle en [[Estructuras de Datos/15-Grafos y DFS/_Índice|Grafos y DFS]] de Estructuras de Datos.

## Preguntas de repaso

> [!question]- ¿Qué estructura usa BFS y qué estructura usa DFS?
> BFS usa una cola (FIFO); DFS usa una pila o la recursión (LIFO).

> [!question]- ¿Por qué BFS encuentra el camino más corto en cantidad de aristas?
> Porque explora por niveles: primero todos los nodos a distancia 1, luego los de distancia 2, y así. El primero que llega a un nodo lo hace por el camino con menos aristas.

> [!question]- ¿Qué complejidad tienen BFS y DFS?
> Ambos $O(V + E)$: visitan cada vértice y cada arista una vez.

> [!question]- ¿Cómo se encuentran las componentes conexas de un grafo?
> Se recorre desde un nodo con BFS o DFS, se marca todo lo alcanzable y, si quedan nodos sin visitar, se repite desde uno de ellos. Cada recorrido descubre una componente.
