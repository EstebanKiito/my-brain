---
ramo: "Estructuras de Datos"
tema: "Árboles de cobertura mínima"
tags:
  - edd
  - grafos
  - mst
  - cortes
  - origen/complemento
prerrequisitos:
  - "[[01 - Grafos y su representación]]"
  - "[[01 - Estrategia codiciosa]]"
---

# Árboles de cobertura mínima y cortes

Hay que conectar con fibra óptica un conjunto de ciudades. Cada conexión posible tiene un costo, y la red debe llegar a **todas** las ciudades con el **menor costo total**. Basta con que haya un camino entre cada par de ciudades, así que no tiene sentido pagar por conexiones redundantes. La solución es un **árbol de cobertura mínimo** (*minimum spanning tree*, MST), que aparece en redes eléctricas, telefónicas, de comunicaciones, de tráfico aéreo e incluso en redes biológicas y químicas.

> [!tip] Definición
> Dado un grafo **no dirigido con costos** $G$, un subgrafo $T \subseteq G$ es un **MST** de $G$ si:
> 1. $T$ es un **árbol** (no tiene ciclos y es conexo);
> 2. $V(T) = V(G)$: **cubre** todos los nodos;
> 3. no existe otro árbol de cobertura con **menor costo total**.
>
> Puede haber **más de un MST** si hay aristas con el mismo costo, pero todos tienen el mismo costo total. Un árbol de cobertura de $V$ nodos tiene exactamente $V - 1$ aristas.

![Slide - grafo no dirigido con costos](adjuntos/Slide%20-%20grafo%20no%20dirigido%20con%20costos.png)

> [!example]- Transcripción de la imagen
> Slide "Árboles de cobertura mínimos". Grafo no dirigido con nodos 0 a 7 y costos: 0–2: 29, 0–6: 51, 0–7: 31, 0–1: 32, 0–5: 60, 1–7: 21, 7–6: 25, 7–4: 46, 6–4: 51, 3–5: 18, 3–4: 34, 5–4: 40.

## Cortes: la herramienta para construir un MST

Un **corte** es una partición $(V_1, V_2)$ de los nodos, con ambos conjuntos no vacíos, disjuntos y que juntos cubren $V$. Una arista **cruza** el corte si tiene un extremo en $V_1$ y el otro en $V_2$.

> [!tip] Propiedad del corte
> - Todo MST contiene **al menos una** arista que cruza cada corte. Si no la tuviera, no habría camino entre $V_1$ y $V_2$, y el árbol no cubriría todo.
> - Dado un corte, la arista **más barata** que lo cruza siempre pertenece a **algún** MST.

La segunda propiedad justifica una estrategia **codiciosa**: elegir siempre la arista más barata que cruce algún corte conveniente nunca lleva a un error. Los dos algoritmos clásicos usan esta idea con distintos cortes:

| | Kruskal | Prim |
|---|---|---|
| Qué mantiene | Un **bosque** de árboles que se van uniendo | **Un solo árbol** que crece desde un nodo inicial |
| Qué arista elige | La más barata del grafo que no forme ciclo | La más barata que sale del árbol actual |
| Estructura auxiliar | Conjuntos disjuntos (union-find) | Cola de prioridad (heap) |
| Complejidad | $O(E \log V)$ | $O(E \log V)$ |

En el grafo de la figura, ambos algoritmos llegan al mismo MST: 3–5 (18), 1–7 (21), 7–6 (25), 0–2 (29), 0–7 (31), 3–4 (34) y 7–4 (46), con **costo total 204**. Son 7 aristas para 8 nodos.

## Preguntas de repaso

> [!question]- ¿Qué tres condiciones definen un MST?
> Ser un árbol (sin ciclos y conexo), cubrir todos los nodos del grafo y tener el menor costo total posible entre los árboles que los cubren.

> [!question]- ¿Por qué todo MST debe tener al menos una arista que cruce cualquier corte?
> Porque si ninguna arista del MST cruzara el corte, no habría camino entre los nodos de $V_1$ y los de $V_2$, y el árbol no sería de cobertura.

> [!question]- ¿Puede un grafo tener más de un MST?
> Sí, cuando hay aristas con el mismo costo que pueden intercambiarse. Todos los MST tienen el mismo costo total.

> [!question]- ¿Cuántas aristas tiene un MST de un grafo conexo de $V$ nodos?
> $V - 1$: es la cantidad de aristas de cualquier árbol con $V$ nodos.
