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
  - origen/complemento
prerrequisitos:
  - "[[16-Algoritmos de ruteo/01 - Modelos de grafo y algoritmos Link-State (Dijkstra)|01 - Modelos de grafo y algoritmos Link-State (Dijkstra)]]"
---

# Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito

En [[01 - Modelos de grafo y algoritmos Link-State (Dijkstra)|Link-State]] cada router conoce el mapa completo. **Distance-Vector (DV)** es la alternativa descentralizada: ningún router conoce la topología, solo lo que le cuentan sus vecinos. Es **distribuido, asíncrono e iterativo**, y se basa en la ecuación de Bellman-Ford.

## La ecuación de Bellman-Ford

Para calcular la ruta más corta de $x$ a $y$, se compara la ruta directa con el costo de pasar por cada vecino intermedio:

$$d_x(y) = \min_v \{\, c(x, v) + d_v(y) \,\}$$

donde $v$ recorre los vecinos de $x$: el costo de llegar al vecino más lo que ese vecino dice que le cuesta llegar a $y$.

- Cada nodo mantiene una **tabla** con la mejor ruta conocida a cada destino (su vector de distancias).
- Cada nodo **comparte su tabla con sus vecinos**.
- Cuando la información se ha propagado a todos, cada uno conoce las mejores rutas.
- Un nodo recalcula **cuando cambia el costo de un enlace local** o **cuando recibe un mensaje de un vecino**.

**Diferencia de implementación con Link-State:** LS propaga la **topología** (los enlaces); DV propaga **rutas**, la distancia más corta hacia cada destino.

![Ecuación de Bellman-Ford y tablas de vectores de distancia](adjuntos/Ecuaci%C3%B3n%20de%20Bellman-Ford%20y%20tablas%20de%20vectores%20de%20distancia.png)

> [!example]- Transcripción de la imagen
> Un triángulo con x–y 2, y–z 1 y x–z 7. Tres columnas de tablas *cost to / from* para *Node x*, *Node y* y *Node z*. **Al inicio**, cada nodo solo conoce su fila: x = (0, 2, 7), y = (2, 0, 1), z = (7, 1, 0); las demás filas valen ∞. **Tras recibir los vectores de los vecinos** (flechas), x calcula (0, 2, 3) y z calcula (3, 1, 0), porque x–y–z cuesta 2 + 1 = 3 < 7. **Al final**, las tres tablas coinciden: x = (0, 2, 3), y = (2, 0, 1), z = (3, 1, 0).

Por ejemplo, x actualiza su distancia a z así: $d_x(z) = \min\{c(x,y) + d_y(z),\ c(x,z) + d_z(z)\} = \min\{2 + 1,\ 7 + 0\} = 3$.

## El problema: conteo al infinito

Las **disminuciones** de costo (buenas noticias) se propagan rápido, pero los **aumentos** (malas noticias) se propagan **lentamente**. Es el **conteo al infinito** (*count-to-infinity*).

```
      y
    /   \
  4→60   1
  /       \
 x ---50--- z
```

Antes del cambio, y llega a x en 4 y z llega a x en 5, pasando por y ($1 + 4$). Si el enlace (y, x) sube de 4 a **60**:

1. y recalcula y ve que z anuncia llegar a x en 5. **No sabe** que esa ruta pasa por él mismo, así que cree que por z le cuesta $1 + 5 = 6$, menos que 60.
2. z ve que y ahora está a 6 y actualiza: $1 + 6 = 7$.
3. y vuelve a ver a z en 7 y sube a 8; z sube a 9… y así, de a poco, hasta que el camino pasa de 50 y z prefiere su enlace directo.

Durante todas esas rondas hay un **ciclo**: los paquetes hacia x rebotan entre y y z.

## La solución: reversa envenenada

¿Cómo evitarlo? **Anunciando una ruta infinita**: es la **reversa envenenada** (*poisoned reverse*). Si z llega a x **a través de y**, entonces le dice a y que su distancia a x es $\infty$. Así z declara inválida la ruta, y y nunca intentará llegar a x pasando por z.

```python
INF = float("inf")
C_YX, C_YZ, C_ZX = 60, 1, 50          # el enlace y-x acaba de subir de 4 a 60

def converger(veneno):
    Dy, Dz = 4, 5                      # distancias a x antes del cambio (z iba por y)
    z_por_y, rondas = True, 0
    while True:
        anuncio_z = INF if (veneno and z_por_y) else Dz   # poisoned reverse
        nuevo_y = min(C_YX, C_YZ + anuncio_z)
        nuevo_z = min(C_ZX, C_YZ + nuevo_y)
        z_por_y = C_YZ + nuevo_y < C_ZX
        if (nuevo_y, nuevo_z) == (Dy, Dz):
            return Dy, Dz, rondas
        Dy, Dz, rondas = nuevo_y, nuevo_z, rondas + 1

print("sin veneno:", converger(False))   # (51, 50, 24)
print("con veneno:", converger(True))    # (51, 50, 2)
```

Las dos versiones terminan igual (y llega a x en 51 a través de z, y z en 50 por el enlace directo), pero sin veneno tardan 24 rondas y con veneno, 2: y toma de inmediato su enlace directo (60), z ve que ir por y le costaría $1 + 60 = 61$, más caro que su enlace de 50, y se cambia; luego y descubre que por z llega en $1 + 50 = 51$. La reversa envenenada solo evita ciclos entre **dos** vecinos; con ciclos de tres o más nodos el problema puede seguir.

## Link-State frente a Distance-Vector

| | Link-State | Distance-Vector |
|---|---|---|
| Mensajes y cálculo | $O(NE)$ mensajes con $N$ nodos y $E$ enlaces; $O(N^2)$ de cálculo en cada nodo | Se ejecuta en paralelo y solo se propaga la ruta a los vecinos |
| Ante errores | Se propaga la ausencia de un enlace local | Se propaga el error |
| Convergencia | Cada nodo calcula con la topología completa una vez recibida | Puede ser muy lenta: tiempo de convergencia indeterminado |

En Internet, DV lo usa **RIP** y LS lo usa **OSPF** (ver [[03 - Enrutamiento jerárquico y sistemas autónomos (Intra-AS e Inter-AS)|enrutamiento jerárquico]]).

## Preguntas de repaso

> [!question]- ¿Qué dice la ecuación de Bellman-Ford?
> Que la distancia mínima de $x$ a $y$ es el mínimo, sobre los vecinos $v$ de $x$, del costo del enlace a $v$ más la distancia que $v$ anuncia hasta $y$.

> [!question]- ¿Qué propaga Distance-Vector y qué propaga Link-State?
> Distance-Vector propaga rutas (distancias a cada destino) solo a los vecinos. Link-State propaga la topología (los enlaces) a toda la red.

> [!question]- ¿Por qué las malas noticias se propagan lento en Distance-Vector?
> Porque un nodo puede creer en una ruta alternativa de su vecino que en realidad pasa por él mismo; ambos suben su costo de a poco en cada intercambio (conteo al infinito).

> [!question]- ¿Cómo funciona la reversa envenenada?
> Si z llega a x a través de y, le anuncia a y una distancia infinita hacia x. Así y no usa una ruta por z que dependía de él mismo.
