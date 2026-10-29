---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Grafos"
tags:
  - algoritmos/grafos
  - algoritmos/representacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es un grafo|Qué es un grafo]]"
---

# Representación de grafos

Un grafo se puede dibujar en papel, pero un programa necesita guardarlo en memoria. Las dos representaciones más usadas son la **lista de adyacencia** y la **matriz de adyacencia**. La elección depende de cuántas conexiones tenga el grafo y de las operaciones que se quieran hacer.

## Lista de adyacencia

Cada nodo guarda una lista con sus vecinos:

```
A: B, C
B: A, D
C: A, D
D: B, C
```

- **Ventaja:** ocupa poco espacio cuando el grafo tiene pocas conexiones (**grafo disperso**).
- **Desventaja:** para saber si $A$ está conectado con $D$ hay que recorrer la lista de $A$.

## Matriz de adyacencia

Se usa una matriz de $V \times V$: la fila es el nodo de origen y la columna el de destino. Si hay arista, se escribe 1; si no, 0.

| | A | B | C | D |
|---|---:|---:|---:|---:|
| **A** | 0 | 1 | 1 | 0 |
| **B** | 1 | 0 | 0 | 1 |
| **C** | 1 | 0 | 0 | 1 |
| **D** | 0 | 1 | 1 | 0 |

- **Ventaja:** consultar si existe una conexión es inmediato: se mira la celda.
- **Desventaja:** ocupa $V^2$ posiciones aunque haya pocas aristas. Para un grafo con muchos nodos y pocas conexiones, se desperdicia mucha memoria.

## Comparación

| Criterio | Lista de adyacencia | Matriz de adyacencia |
|---|---|---|
| Espacio | $O(V + E)$ | $O(V^2)$ |
| Consultar si hay arista | $O(\text{grado})$ | $O(1)$ |
| Recorrer todos los vecinos | $O(\text{grado})$ | $O(V)$ |
| Mejor para | Grafos dispersos | Grafos densos |

> [!tip] La idea central
> Si el grafo tiene muchas conexiones, la matriz es cómoda y rápida. Si tiene pocas, la lista ahorra memoria. No hay una representación mejor para todos los casos.

> [!warning] El grado de un nodo
> El **grado** es la cantidad de aristas que llegan a un nodo. En una lista de adyacencia, recorrer los vecinos cuesta $O(\text{grado})$, no $O(V)$.

## Preguntas de repaso

> [!question]- ¿Cuánto espacio ocupa una matriz de adyacencia con $V$ nodos?
> $O(V^2)$, porque tiene una celda por cada par de nodos, haya o no conexión.

> [!question]- ¿Cuándo conviene usar una lista de adyacencia?
> Cuando el grafo es disperso, es decir, tiene muchas menos conexiones que el máximo posible. Así se ahorra memoria.

> [!question]- ¿Cómo se consulta si existe una arista en una matriz?
> Se mira la celda en la fila del nodo de origen y la columna del destino. Si vale 1, hay arista.

> [!question]- ¿Qué es el grado de un nodo?
> La cantidad de aristas conectadas a ese nodo. En un grafo dirigido se distingue entre grado de entrada y de salida.
