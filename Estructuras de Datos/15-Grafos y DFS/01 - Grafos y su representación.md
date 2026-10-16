---
ramo: "Estructuras de Datos"
tema: "Grafos y DFS"
tags:
  - edd
  - grafos
  - listas-de-adyacencia
  - origen/complemento
prerrequisitos:
  - "[[01 - Arreglos frente a listas ligadas]]"
---

# Grafos y su representación

Un **grafo** es la estructura para representar **relaciones** entre elementos: tareas que dependen de otras, calles entre esquinas, amistades entre personas. Muchos problemas se resuelven en dos pasos: **modelar** la situación como grafo y aplicar un algoritmo conocido.

## Ejemplo motivador: proyecto con requisitos

Un proyecto se divide en tareas indivisibles, y algunas tienen otras como **requisito**. Si B requiere A, se escribe $A \to B$. El proyecto es **inviable** si hay una referencia circular $X \to T_1 \to \dots \to T_n \to X$, porque ninguna de esas tareas podría empezar. La ausencia de ciclos es una condición **necesaria y suficiente** para la viabilidad: sin ciclos, las tareas se pueden ordenar y ejecutar en ese orden.

![Slide - grafo de dependencias entre tareas](adjuntos/Slide%20-%20grafo%20de%20dependencias%20entre%20tareas.png)

> [!example]- Transcripción de la imagen
> Slide "Representación de la dependencia de tareas". T0: sin requisitos; T1: requiere T0; T2: requiere T1; T3: requiere T1, T6 y T8; T4: requiere T3, T5 y T9; T5: requiere T6 y T8; T6: requiere T7; T7: requiere T0; T8: requiere T1 y T7; T9: requiere T2 y T8. Debajo, el grafo dirigido con los nodos 0 a 9 y una flecha desde cada requisito hacia la tarea que lo necesita.

## Definiciones

> [!tip] Grafo dirigido y no dirigido
> - Un **grafo dirigido** es un par $G = (V, E)$, con $V$ el conjunto de **nodos** y $E$ un conjunto de **aristas** $(u, v)$, que son pares ordenados. Se usa cuando hay un **origen** y un **destino** (por ejemplo, $V = \{0, \dots, 4\}$, $E = \{(0,1), (0,2), (1,2), (1,3), (2,4)\}$).
> - Un **grafo no dirigido** tiene aristas $\{u, v\}$, que son pares sin orden, con $u \ne v$. Se usa cuando importa agrupar **vecinos**.

La complejidad de los algoritmos sobre grafos se expresa en función de $V = |V|$ y $E = |E|$. ¿Es mejor $O(V)$ u $O(E)$? Depende del grafo, porque $E$ puede ir de $0$ hasta $O(V^2)$ en un grafo completo.

## Representaciones

![Slide - lista y matriz de adyacencias](adjuntos/Slide%20-%20lista%20y%20matriz%20de%20adyacencias.png)

> [!example]- Transcripción de la imagen
> Slide "Representación de grafos". A la izquierda, el grafo de las tareas 0 a 9. A la derecha, su **lista de adyacencias** $\alpha$: 0 → 1, 7; 1 → 2, 8; 2 → 3, 9; 3 → 4; 4 → (vacía); 5 → 4; 6 → 3, 5; 7 → 6, 8; 8 → 3, 5, 9; 9 → 4. "La complejidad en grafos puede depender de qué representación se usa".

| | Lista de adyacencias | Matriz de adyacencias |
|---|---|---|
| Qué guarda | Celda $i$: lista de los vecinos $j$ con $(i, j) \in E$ | Celda $[i][j]$: si existe la arista $(i, j)$ |
| Memoria | $O(V + E)$ | $O(V^2)$ |
| ¿Existe $(i, j)$? | $O(\text{grado de } i)$ | $O(1)$ |
| Recorrer los vecinos de $i$ | $O(\text{grado de } i)$ | $O(V)$ |
| Conviene para | Grafos **dispersos** (pocas aristas) | Grafos **densos** |

En ambas, los nodos son las "dimensiones" de la estructura y las aristas son los datos. Recorrer todo el grafo cuesta $O(V + E)$ con listas y $O(V^2)$ con matriz.

## Preguntas de repaso

> [!question]- ¿Por qué un proyecto con requisitos es viable si y solo si su grafo no tiene ciclos?
> Si hay un ciclo, ninguna tarea del ciclo puede empezar, porque cada una espera a otra del mismo ciclo. Si no hay ciclos, siempre existe una tarea sin requisitos pendientes, y repitiendo esa idea se obtiene un orden de ejecución.

> [!question]- ¿Cuándo conviene una lista de adyacencias y cuándo una matriz?
> La lista conviene en grafos dispersos: usa $O(V + E)$ de memoria y recorre los vecinos en proporción al grado. La matriz conviene en grafos densos o cuando hay que consultar muchas veces si existe una arista, en $O(1)$.

> [!question]- ¿Cuál es la diferencia entre una arista de un grafo dirigido y una de un grafo no dirigido?
> En el dirigido, $(u, v)$ es un par ordenado: va de $u$ a $v$. En el no dirigido, $\{u, v\}$ es un conjunto: conecta a ambos sin dirección.

> [!question]- ¿Cuántas aristas puede tener un grafo dirigido de $V$ nodos sin aristas repetidas?
> Hasta $V(V-1)$ (o $V^2$ si se permiten lazos), es decir, $O(V^2)$.
