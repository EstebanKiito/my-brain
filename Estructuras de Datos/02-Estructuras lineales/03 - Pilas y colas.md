---
ramo: "Estructuras de Datos"
tema: "Estructuras lineales"
tags:
  - edd
  - pilas
  - colas
  - fifo
  - lifo
  - origen/complemento
prerrequisitos:
  - "[[01 - Arreglos frente a listas ligadas]]"
---

# Pilas y colas

Muchos problemas solo necesitan **insertar** y **sacar** elementos, en un orden que depende de cuándo llegaron. Las **colas** y las **pilas** son las estructuras para eso: ambas son una fila de elementos con dos operaciones básicas, pero difieren en **cuál sale primero**. Que sean tan restringidas es justamente lo que permite implementarlas con todas sus operaciones en $O(1)$.

## Cola (FIFO)

En una **cola** (*queue*), el primero en entrar es el primero en salir: **FIFO** (*First In, First Out*). Se inserta al **final** y se extrae desde la **cabeza**, como en una fila de banco. Puede verse como una cola cuya prioridad es el **orden de llegada**: el primer elemento es el más prioritario porque lleva más tiempo esperando, y el último es el menos prioritario.

![Cola FIFO con enqueue y dequeue](adjuntos/Cola%20FIFO%20con%20enqueue%20y%20dequeue.png)

> [!example]- Transcripción de la imagen
> "Queue". Una fila de cinco bloques con "Back" (final) a la izquierda y "Front" (cabeza) a la derecha. Un bloque nuevo entra por atrás con la flecha "Enqueue" y otro sale por adelante con "Dequeue".

## Pila (LIFO)

En una **pila** (*stack*), el último en entrar es el primero en salir: **LIFO** (*Last In, First Out*). Se inserta y se extrae por el **mismo extremo**, el tope, como una pila de platos. Es una "cola" con el orden de prioridad invertido. El [[04 - Funciones y stack de llamadas|stack de llamadas]] de un programa funciona exactamente así.

![Pila LIFO al apilar un elemento](adjuntos/Pila%20LIFO%20al%20apilar%20un%20elemento.png)

> [!example]- Transcripción de la imagen
> Una pila con "Elemento 1" abajo y "Elemento 4" arriba. "Nuevo 5" entra por arriba (flecha "Entra") y queda en el tope de la pila resultante. Una flecha "Orden" baja desde el tope: lo que se saca primero es lo último que entró.

## Costos según la implementación

| Operación | Arreglo | Lista ligada |
|---|---|---|
| Cola: insertar al final | $O(1)$, salvo que el arreglo se llene | $O(1)$ con puntero al último |
| Cola: extraer la cabeza | $O(1)$ **si no se reubican** los demás | $O(1)$ |
| Pila: push y pop en el tope | $O(1)$ (al final del arreglo) | $O(1)$ (en la cabeza) |

La trampa está en la cola sobre arreglo. Si al extraer se corren todos los elementos una posición, la extracción cuesta $O(n)$. La solución es no mover nada: se guarda el índice de la cabeza y se avanza en **círculo** (cola circular).

```python
class ColaCircular:
    """FIFO sobre un arreglo de tamaño fijo: inicio y fin avanzan en círculo."""
    def __init__(self, capacidad):
        self.A = [None] * capacidad
        self.inicio = 0                  # índice de la cabeza
        self.n = 0                       # cantidad de elementos
    def encolar(self, x):                # O(1)
        if self.n == len(self.A):
            raise OverflowError("cola llena")
        self.A[(self.inicio + self.n) % len(self.A)] = x
        self.n += 1
    def desencolar(self):                # O(1): no se reubica nada
        x = self.A[self.inicio]
        self.inicio = (self.inicio + 1) % len(self.A)
        self.n -= 1
        return x

c = ColaCircular(3)
for x in "abc": c.encolar(x)
print(c.desencolar(), c.desencolar())      # a b
c.encolar("d"); c.encolar("e")             # reutiliza las celdas que quedaron libres
print([c.desencolar() for _ in range(3)])  # ['c', 'd', 'e']
```

Una pila sobre arreglo es todavía más simple: `append` y `pop` al final de una lista de Python son $O(1)$. Para colas, Python trae `collections.deque`, con `append` y `popleft` en $O(1)$.

> [!warning] Cuándo no alcanza una cola FIFO
> Si la prioridad no es el orden de llegada sino un atributo del dato (el avión con menos combustible aterriza primero, el paciente más grave se atiende primero), una cola FIFO no sirve. Hace falta una **cola de prioridad**, que se implementa eficientemente con un heap.

## Preguntas de repaso

> [!question]- ¿Qué diferencia una cola de una pila?
> El extremo por el que se extrae. La cola saca el elemento más antiguo (FIFO), y la pila saca el más reciente (LIFO).

> [!question]- ¿Por qué una cola sobre arreglo puede tener extracción en $O(n)$ y cómo se evita?
> Porque, si al sacar la cabeza se corren todos los elementos una posición, eso cuesta $O(n)$. Se evita guardando el índice de la cabeza y avanzándolo de forma circular (módulo la capacidad), sin mover datos.

> [!question]- ¿Por qué en una lista ligada conviene implementar la pila en la cabeza y no en la cola?
> Porque insertar y extraer en la cabeza es $O(1)$. Extraer el último nodo exigiría encontrar el penúltimo, lo que en una lista simple cuesta $O(n)$.

> [!question]- Dar un ejemplo de problema que una cola FIFO no resuelve bien.
> Atender según urgencia, como aterrizar primero al avión con menos combustible. La prioridad depende de un atributo y no del orden de llegada, así que se necesita una cola de prioridad.
