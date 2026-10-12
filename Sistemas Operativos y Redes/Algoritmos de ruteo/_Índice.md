# Algoritmos de ruteo — índice

Modelos formales, análisis de complejidad y protocolos de encaminamiento en el plano de control de la capa de red. Abstracción de la topología de red como un grafo ponderado $G = (V, E)$, donde los vértices representan enrutadores y las aristas enlaces con costos asociados (retardo, capacidad y congestión). Clasificación fundamental de los algoritmos de encaminamiento en dos familias: algoritmos de estado de enlace (**Link-State**, LS), con información global propagada por inundación (*flooding*) y cómputo de caminos mínimos mediante el algoritmo de Dijkstra ($O(N^2)$ o $O(E + N \log N)$); frente a algoritmos de vector de distancia (**Distance-Vector**, DV), descentralizados e iterativos, basados en la ecuación de Bellman-Ford ($d(x,y) = \min_v \{c(x,v) + d(v,y)\}$). Estudio detallado de los fenómenos de convergencia, bucles temporales y la anomalía del conteo hacia el infinito (*count-to-infinity*), junto a técnicas de mitigación como el reverso envenenado (*Poisoned Reverse*). Finalmente, estructuración jerárquica de la red global de Internet en **Sistemas Autónomos** (AS): partición entre protocolos internos de enrutamiento intra-dominio (Intra-AS como OSPF y RIP) y protocolos inter-dominio basados en políticas de tránsito comercial (Inter-AS como BGP) con enrutadores de pasarela (*gateway routers*).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la sección `ALGORITMOS DE RUTEO` de los apuntes originales de Redes, complementadas con las diapositivas oficiales de `Contenido_11_Capa_Red.pdf` y la literatura estándar de redes de computadores (Kurose & Ross).

## Orden de estudio

1. [[01 - Modelos de grafo y algoritmos Link-State (Dijkstra)|Modelos de grafo y algoritmos Link-State (Dijkstra)]]: abstracción de redes como grafos ponderados, inundación de LSA, y ejecución del algoritmo de Dijkstra para árboles de caminos más cortos.
2. [[02 - Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito|Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito]]: cálculo iterativo descentralizado, ecuación de Bellman-Ford, bucles de enrutamiento, conteo al infinito y poisoned reverse.
3. [[03 - Enrutamiento jerárquico y sistemas autónomos (Intra-AS e Inter-AS)|Enrutamiento jerárquico y sistemas autónomos (Intra-AS e Inter-AS)]]: necesidad de jerarquía en Internet, sistemas autónomos (AS), gateway routers, ruteo Intra-AS (OSPF) e Inter-AS (BGP) y hot-potato routing.
