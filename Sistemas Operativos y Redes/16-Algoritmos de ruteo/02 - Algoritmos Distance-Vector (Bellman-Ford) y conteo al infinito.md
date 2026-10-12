---
ramo: "Sistemas Operativos y Redes"
tema: "Algoritmos de ruteo"
tags:
  - sistemas-operativos
  - redes
  - distance-vector
  - bellman-ford
  - poison-reverse
  - conteo-al-infinito
prerrequisitos:
  - "[[16-Algoritmos de ruteo/01 - Modelos de grafo y algoritmos Link-State (Dijkstra)|01 - Modelos de grafo y algoritmos Link-State (Dijkstra)]]"
---

# Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito

A diferencia de Link-State, los algoritmos de vector de distancia (**Distance-Vector**, DV) son descentralizados, iterativos y asíncronos. Cada enrutador no conoce la topología completa de la red; únicamente mantiene un vector con los costos estimados hacia todos los destinos y lo intercambia periódicamente con sus vecinos directos aplicando la ecuación de **Bellman-Ford**.

---

## Vector de distancia y dinámica de convergencia (mis apuntes)

DISTANCE-VECTOR
Utliza la EC de BELLAMN FORD: Para calc la ruta mas corta entre cada par de nodos es: Comparo Ruta directa vs El costo de pasar con cada uno de los costos intermedios
d(x,y) = minv{c(x, v) + d(v, y)}

![Ecuación de Bellman-Ford y tablas de vectores de distancia](adjuntos/Ecuación%20de%20Bellman-Ford%20y%20tablas%20de%20vectores%20de%20distancia.png)

> [!example]- Transcripción de la imagen
> Ecuación de Bellman-Ford y tabla de distancias:
> - $d_x(y) = \min_v \{c(x,v) + d_v(y)\}$ tomado sobre todos los vecinos $v$ de $x$.
> - Cada nodo $x$ almacena su propio vector de distancias $D_x$ y los vectores recibidos de sus vecinos inmediatos, actualizando iterativamente su tabla cuando detecta cambios en los costos de enlace.

DIFERENCIA de implement
Link-State: propaga TOPOLOGIAS
Distance-Vector: Ruta mas corta hacia un destinatario
- Distance Vector a diferencia de LS: se propaga información de rutas, en lugar de enlaces

Sin embargo, distance-vector tiene un problema → CONTEO HACIA EL INFINITO
Poison Ruta → Si se envenena la ruta ejemplo

```
      y
    /   \
   /     \
 4 -> 60  1
 /         \
x --- 50--- z
```

Si el 4 en (y,x) se actualizace a 60, z no sabe que eso paso, y cuando y quiera irse por z, entonces z le dira, pero oye hay una ruta mas corta que toma 5 (1 + 4), y cuando se devuelve toma 61 → Mas caro (se enveneno)
Lo que hacemos para estos casos es DECLARAR LA RUTA INVALIDA

| LINK STATE | DISTANCE-VECTOR |
|---|---|
| N NODOS, E ENLACES: O(NE) Mensajes | Se ejecutan en paralelo, y solo se propaga ruta a los vecinos |
| O(N^2) Complejidad en Cada NODO | Ante Errores, se propaga el error |
| Ante errores → Se propaga ausencia de enlace local | Puede converger muy lentamente, Tiempo de convergencia Indeterminado |

> [!tip] Complemento de clase: Mecanismo de Poisoned Reverse (Reverso Envenenado)
> Si el nodo $z$ enruta su tráfico hacia el destino $x$ a través del vecino $y$, $z$ le miente deliberadamente a $y$ diciéndole que su distancia hacia $x$ es infinita ($D_z(x) = \infty$). De este modo, si el enlace directo $(y, x)$ falla o aumenta bruscamente de costo, $y$ nunca intentará enrutar hacia $x$ pasando por $z$, evitando el bucle de conteo al infinito en ciclos de dos nodos.

---

## Preguntas de repaso

> [!question]- ¿Qué significa que las buenas noticias viajen rápido y las malas noticias viajen lento en Distance-Vector?
> Cuando el costo de un enlace disminuye, el cambio se propaga y converge en una sola iteración por salto; pero cuando un enlace aumenta drásticamente de costo o se cae, se generan bucles de enrutamiento temporales donde los nodos incrementan sus costos paso a paso (conteo al infinito) hasta alcanzar $\infty$.

> [!question]- ¿Por qué *Poisoned Reverse* no resuelve completamente el problema del conteo al infinito?
> Porque solo previene bucles directos entre dos nodos contiguos ($y \leftrightarrow z$); si el bucle involucra tres o más nodos ($x \to y \to z \to w \to x$), ningún nodo le miente al anterior sobre su ruta indirecta y el conteo al infinito persiste.

> [!question]- ¿Cómo se compara la propagación de errores entre Link-State y Distance-Vector?
> En Link-State, un nodo defectuoso solo puede anunciar erróneamente el costo de sus enlaces directos, pero cada router calcula sus propias rutas; en Distance-Vector, un nodo que calcule mal su vector propaga el cálculo corrupto a toda la red contaminando las tablas de sus vecinos.
