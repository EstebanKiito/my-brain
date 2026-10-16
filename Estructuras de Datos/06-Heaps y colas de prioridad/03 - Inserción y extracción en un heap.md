---
ramo: "Estructuras de Datos"
tema: "Heaps y colas de prioridad"
tags:
  - edd
  - heap
  - sift-up
  - sift-down
  - c
  - origen/complemento
prerrequisitos:
  - "[[02 - Heap binario y su representación en arreglo]]"
---

# Inserción y extracción en un heap

Insertar y extraer rompen momentáneamente la forma o el orden del heap. La estrategia es siempre la misma: primero se **arregla la forma** (el árbol debe seguir casi lleno) y después se **restaura el orden**, moviendo un solo elemento hacia arriba (**SiftUp**) o hacia abajo (**SiftDown**) a lo largo de **un camino** raíz-hoja. Ese camino mide $O(\log n)$.

![Camino de la raíz a la última hoja](adjuntos/Camino%20de%20la%20ra%C3%ADz%20a%20la%20%C3%BAltima%20hoja.png)

> [!example]- Transcripción de la imagen
> El max heap 31, 29, 19, 7, 23, 13, 17, 5, 3, 11 con el camino 31 → 29 → 23 → 11 resaltado (índices 0, 1, 4 y 9), en el árbol y en el arreglo. Llegar de la raíz a una hoja recorre un nodo por nivel: $\log n$ comparaciones, no $n$.

## Extracción: SiftDown

Se saca la raíz (el más prioritario). Para que el árbol siga casi lleno, el **último elemento** pasa a la raíz. Después, mientras sea menor que su hijo mayor, se intercambia con él.

![Se saca la raíz](adjuntos/Extracci%C3%B3n%20-%20se%20saca%20la%20ra%C3%ADz.png)

> [!example]- Transcripción de la imagen
> "Al extraer, sacamos el elemento más prioritario": el 31 de la raíz (posición 0) aparece resaltado.

![El último elemento pasa a la raíz](adjuntos/Extracci%C3%B3n%20-%20el%20%C3%BAltimo%20elemento%20pasa%20a%20la%20ra%C3%ADz.png)

> [!example]- Transcripción de la imagen
> "Ahora el árbol está casi-lleno, pero no se cumple la propiedad de heap": el 11 ocupa la raíz y la posición 9 quedó vacía. Arreglo: 11, 29, 19, 7, 23, 13, 17, 5, 3.

```
Extract(H):                       // H: heap como arreglo H[0..n-1]
    i <- última celda no vacía de H
    best <- H[0]
    H[0] <- H[i];  H[i] <- ∅
    SiftDown(H, 0)
    return best

SiftDown(H, i):
    if i tiene hijos:
        j <- hijo de i con mayor prioridad
        if H[j] > H[i]:
            H[j] <-> H[i]
            SiftDown(H, j)
```

En el ejemplo, el 11 baja intercambiándose con 29 y luego con 23, y el arreglo queda 29, 23, 19, 7, 11, 13, 17, 5, 3. Es un heap válido de nuevo.

## Inserción: SiftUp

El dato nuevo se pone en la **primera celda vacía**, lo que mantiene la forma, y **sube** mientras sea mayor que su padre.

```
Insert(H, e):
    i <- primera celda vacía de H
    H[i] <- e
    SiftUp(H, i)

SiftUp(H, i):
    if i tiene padre:
        j <- ⌊(i-1)/2⌋              // padre, con índices desde 0
        if H[j] < H[i]:
            H[j] <-> H[i]
            SiftUp(H, j)
```

> [!tip] Por qué $O(\log n)$
> Cada operación hace a lo más un intercambio por nivel y hay $O(\log n)$ niveles. Comparado con insertion sort, que en el peor caso compara con todos los elementos, aquí se compara solo a lo largo de un camino.

## Implementación en C (min heap)

Es la implementación de la ayudantía (con `heapify` renombrado como `sift_down`), completada con inserción y extracción. Es un **min heap**: la raíz es el **menor**.

```c
typedef struct minheap { int size; int capacity; int* array; } Minheap;

static void swap(int* a, int* b) { int aux = *a; *a = *b; *b = aux; }

void sift_down(Minheap* heap, int i)
{
    int left = 2 * i + 1, right = 2 * i + 2, smallest = i;
    if (left < heap->size && heap->array[left] < heap->array[smallest]) smallest = left;
    if (right < heap->size && heap->array[right] < heap->array[smallest]) smallest = right;
    if (smallest != i)
    {
        swap(&heap->array[smallest], &heap->array[i]);
        sift_down(heap, smallest);
    }
}

void sift_up(Minheap* heap, int i)
{
    int parent = (i - 1) / 2;
    if (i > 0 && heap->array[i] < heap->array[parent])
    {
        swap(&heap->array[i], &heap->array[parent]);
        sift_up(heap, parent);
    }
}

void heap_insert(Minheap* heap, int value)      // O(log n); supone size < capacity
{
    heap->array[heap->size] = value;
    heap->size += 1;
    sift_up(heap, heap->size - 1);
}

int heap_extract(Minheap* heap)                 // O(log n); supone size > 0
{
    int best = heap->array[0];
    heap->size -= 1;
    heap->array[0] = heap->array[heap->size];
    sift_down(heap, 0);
    return best;
}
// insertando 5, 2, 3, 4, 1, 6, 7, 9, 8, 10, 0 y extrayendo todo: 0 1 2 ... 10 (0 leaks)
```

> [!warning] Arreglo como árbol
> Un heap en arreglo **no** se implementa con nodos y punteros. Usar un árbol de punteros haría perder la ventaja: encontrar "la última hoja" o "la primera celda vacía" ya no sería $O(1)$.

## Preguntas de repaso

> [!question]- ¿Por qué al extraer se mueve el último elemento a la raíz y no, por ejemplo, el mayor de los hijos?
> Porque el último elemento es el único que se puede quitar sin romper la forma de árbol casi lleno. Después SiftDown restaura el orden en $O(\log n)$.

> [!question]- ¿Por qué SiftDown compara con el hijo de mayor prioridad y no con cualquiera?
> Porque ese hijo es el único que puede subir sin violar la propiedad de heap: queda como padre de su hermano, que es menor o igual que él.

> [!question]- Insertar 30 en el max heap 31, 29, 19, 7, 23, 13, 17, 5, 3, 11. ¿Dónde termina?
> Entra en la posición 10, cuyo padre es la 4 (23): como $30 > 23$, sube a la 4. Su nuevo padre es la 1 (29): como $30 > 29$, sube a la 1. Su padre es la raíz (31), y como $30 < 31$, se detiene en la posición 1.

> [!question]- ¿Cuál es el costo de insertar y extraer en un heap de $n$ elementos?
> $O(\log n)$ cada uno, porque solo se recorre un camino entre la raíz y una hoja, y la altura del heap es logarítmica.
