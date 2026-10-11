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
prerrequisitos:
  - "[[Capa de red y direccionamiento/_Índice|Capa de red y direccionamiento]]"
---

# Modelos de grafo y algoritmos Link-State (Dijkstra)

El problema del enrutamiento en redes de computadores se modela matemáticamente como la búsqueda de caminos de menor costo en un grafo ponderado $G = (V, E)$, donde los vértices $V$ representan a los enrutadores y las aristas $E$ representan los enlaces físicos de comunicación. Los algoritmos de estado de enlace (**Link-State**, LS) operan bajo un paradigma global y centralizado en información: cada nodo aprende la topología completa mediante difusión de anuncios de estado de enlace (*flooding*) y ejecuta de manera autónoma el algoritmo de caminos más cortos de Dijkstra.

---

## Modelado y algoritmo Link-State (mis apuntes)

ALGORITMOS DE RUTEO
Podemos modelar el conjunto de routers como un GRAFO G = (V, E)
- Costo entre conexiones: Ancho de banda, congestion, distancia
- Enlaces Son las Aristas!
- Nodos conocen la info COMPLETA de la RED
- Se explora toda la red
- Y cada nodo determina la ruta mas conveniente
- Algoritmos LINK-STATE (LS)
- ALGORITMOS CENTRALIZADOS
- Calculo Iterativo y Distribuido entre nodos → Sin Conocer la TOPOLOGIA COMPLETA
- Calculo distribuido entre los nodos
- Algoritmos de Distance-Vector (DS)
- ALGORITMOS DECENTRALIZADOS

LINK-STATE
- Cada Nodo ENVIA INFO de conectividad (Vecinos y Costos), a sus VECINOS
- Se comunican via flooding
- Cuando todos tienen la info, cada uno Calcula Rutas mas Cortas
- Implementa por ejemplo : DIJKSTRA

![Algoritmo Link-State de Dijkstra con cálculo de caminos más cortos](adjuntos/Algoritmo%20Link-State%20de%20Dijkstra%20con%20cálculo%20de%20caminos%20más%20cortos.png)

> [!example]- Transcripción de la imagen
> Pseudocódigo del algoritmo de Dijkstra para nodo fuente $u$:
> 1. **Inicialización**: $N' = \{u\}$; para todo $v \notin N'$, si $v$ es vecino de $u$, $D(v) = c(u,v)$, si no $D(v) = \infty$.
> 2. **Bucle**: Encontrar $w \notin N'$ tal que $D(w) = \min_{v \notin N'} D(v)$. Añadir $w$ a $N'$.
> 3. **Actualización**: Para todo vecino $v$ de $w$ no en $N'$: $D(v) = \min(D(v), D(w) + c(w,v))$.
> 4. Repetir hasta que todos los nodos pertenezcan a $N'$.

![Tabla de iteraciones y árbol de caminos más cortos en Dijkstra](adjuntos/Tabla%20de%20iteraciones%20y%20árbol%20de%20caminos%20más%20cortos%20en%20Dijkstra.png)

> [!example]- Transcripción de la imagen
> Tabla de iteraciones y árbol de caminos mínimos: Traza paso a paso la distancia acumulada $D(v)$ y el predecesor inmediato $p(v)$ para cada nodo de la red. Una vez construido el árbol de expansión de caminos más cortos, el router extrae su interfaz de reenvío local para cada destino.

> [!tip] Complemento de clase: Protocolo OSPF (Open Shortest Path First)
> OSPF es el protocolo estándar de la IETF que implementa el algoritmo Link-State en redes IP intra-dominio. Cada router empaqueta el estado de sus enlaces en mensajes LSA (*Link-State Advertisements*) y los difunde mediante flooding a través de toda la red utilizando direccionamiento multicast.

---

## Preguntas de repaso

> [!question]- ¿Por qué el algoritmo de Dijkstra se clasifica como "centralizado" si cada router lo ejecuta por su cuenta?
> Porque es centralizado en términos de **información**: requiere que cada router disponga del mapa completo e idéntico de toda la topología y costos de la red antes de poder ejecutar el cómputo.

> [!question]- ¿Cuál es la complejidad computacional del algoritmo de Dijkstra con $N$ nodos?
> Una implementación ingenua requiere $O(N^2)$ operaciones para buscar el mínimo en cada paso; utilizando una cola de prioridad o un heap de Fibonacci la complejidad se reduce a $O(E + N \log N)$.

> [!question]- ¿Qué problema pueden experimentar los algoritmos Link-State si los costos de enlace dependen de la congestión o tráfico instantáneo?
> Oscilaciones de ruta (*route oscillations*): cuando todos los routers detectan una ruta descongestionada, desvían masivamente su tráfico hacia ella saturándola de golpe, lo que provoca que en la siguiente iteración todos recalculen y desvíen el tráfico en sentido contrario, ciclando continuamente.
