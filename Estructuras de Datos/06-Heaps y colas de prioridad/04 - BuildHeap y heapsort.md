---
ramo: "Estructuras de Datos"
tema: "Heaps y colas de prioridad"
tags:
  - edd
  - heap
  - heapsort
  - ordenamiento
  - origen/complemento
prerrequisitos:
  - "[[03 - Inserción y extracción en un heap]]"
  - "[[04 - Propiedades de los algoritmos de ordenación]]"
---

# BuildHeap y heapsort

Si ya se tiene un max heap, ordenar es fácil: se extrae el máximo $n$ veces. El problema real es **construir el heap** a partir de un arreglo desordenado de forma eficiente. **Heapsort** es, en el fondo, un [[01 - Ordenar para buscar y selection sort|selection sort]] con la estructura de datos correcta: el mínimo (o máximo) del lado desordenado se encuentra en $O(\log n)$ en vez de $O(n)$.

## Construir el heap

- **Estrategia 1:** insertar los elementos uno a uno en un heap vacío, $n$ inserciones de $O(\log n)$: $O(n \log n)$.
- **Estrategia 2 (BuildHeap):** tratar el arreglo como un árbol y aplicar **SiftDown desde la mitad hacia la raíz**. Los elementos de la segunda mitad son hojas y ya son heaps de un elemento.

![Pseudocódigo de BuildHeap](adjuntos/Pseudoc%C3%B3digo%20de%20BuildHeap.png)

> [!example]- Transcripción de la imagen
> input: arreglo $A[0 \dots n-1]$. `BuildHeap(A)`: `for i = ⌊n/2⌋ - 1 ... 0` (loop decreciente): `SiftDown(A, i)`.

> [!tip] BuildHeap es $O(n)$, no $O(n \log n)$
> La cota directa es $O(n \log n)$ ($n/2$ llamados de hasta $\log n$), pero es pesimista. La mayoría de los nodos está cerca de las hojas y baja muy poco: la mitad no baja nada, un cuarto baja a lo más 1 nivel, un octavo a lo más 2, y así. La suma $\sum_h \frac{n}{2^{h+1}} \cdot h$ es $O(n)$.

> [!example] Min heap desde un max heap
> ¿Cómo se obtiene un min heap a partir de un max heap? Basta con aplicar BuildHeap en versión mínima: funciona sobre **cualquier** arreglo, sin importar cómo venga ordenado. Cuando una pregunta forma parte de otra más grande, la respuesta suele ser más directa de lo que parece.

## Heapsort

![Pseudocódigo de HeapSort](adjuntos/Pseudoc%C3%B3digo%20de%20HeapSort.png)

> [!example]- Transcripción de la imagen
> input: arreglo $A[0 \dots n-1]$. `HeapSort(A)`: `BuildHeap(A)`; `for i = n-1 ... 1` (loop decreciente): `A[0] ⇄ A[i]`, `A.heap_size = A.heap_size - 1`, `ShiftDown(A, 0)`.

El máximo (en `A[0]`) se intercambia con el último elemento del heap. Desde ahí queda en su posición final, y el heap se achica en uno (`heap_size` marca hasta dónde llega). El arreglo queda partido como en selection sort: el heap a la izquierda (desordenado) y la zona ordenada a la derecha. Con un **max heap** se ordena de menor a mayor.

```python
def sift_down(A, i, n):
    while True:
        hijos = [c for c in (2 * i + 1, 2 * i + 2) if c < n]
        if not hijos: return
        j = max(hijos, key=lambda c: A[c])
        if A[j] <= A[i]: return
        A[i], A[j] = A[j], A[i]
        i = j

def heapsort(A):
    for i in range(len(A) // 2 - 1, -1, -1):   # BuildHeap
        sift_down(A, i, len(A))
    for fin in range(len(A) - 1, 0, -1):
        A[0], A[fin] = A[fin], A[0]             # el máximo al final
        sift_down(A, 0, fin)                    # heap_size = fin
    return A

print(heapsort([10, 4, 8, 5, 12, 2, 6, 11, 3, 9, 7, 1]))   # [1, 2, ..., 12]
```

![Animación de heapsort](adjuntos/Animaci%C3%B3n%20de%20heapsort.gif)

> [!example]- Transcripción de la imagen
> Animación sobre el arreglo 10, 4, 8, 5, 12, 2, 6, 11, 3, 9, 7, 1. Primero se construye el heap y después, repetidamente, la raíz se intercambia con el último elemento del heap y se restaura con sift down, hasta que todo queda ordenado.

Hay una visualización en video del proceso en https://www.youtube.com/watch?v=MkHuwIrWZmI&t=1s

## Complejidad y propiedades

![Complejidad de heapsort](adjuntos/Complejidad%20de%20heapsort.png)

> [!example]- Transcripción de la imagen
> BuildHeap: $\mathcal{O}(n)$. SiftDown se repite $\mathcal{O}(n)$ veces: $\mathcal{O}(n\log n)$. Total: $\mathcal{O}(n + n\log n) = \mathcal{O}(n\log n)$. "HeapSort ordena en tiempo $\mathcal{O}(n\log(n))$".

![Tabla de complejidad con heapsort](adjuntos/Tabla%20de%20complejidad%20con%20heapsort.png)

> [!example]- Transcripción de la imagen
> La tabla completa. Selection sort: $\mathcal{O}(n^2)$ en todos los casos, memoria $\mathcal{O}(1)$. Insertion sort: $\mathcal{O}(n)$, $\mathcal{O}(n^2)$, $\mathcal{O}(n^2)$, $\mathcal{O}(1)$. Merge sort: $\mathcal{O}(n\log n)$ en todos los casos, $\mathcal{O}(n)$. Quick sort: $\mathcal{O}(n\log n)$, $\mathcal{O}(n\log n)$, $\mathcal{O}(n^2)$, $\mathcal{O}(1)$. Heap sort: $\mathcal{O}(n\log n)$ en todos los casos, $\mathcal{O}(1)$.

| Propiedad | Heapsort |
|---|---|
| Tiempo | $O(n \log n)$ en **todos** los casos: no se puede *envenenar* |
| Memoria adicional | $O(1)$ (in place) |
| Estable | **No**: el orden parcial y los intercambios a distancia mezclan los iguales |
| En la práctica | Más lento que quicksort en el caso típico (hace más intercambios) |

> [!tip] Cuándo usarlo
> Heapsort es el **seguro** contra el peor caso. Cuando no se puede arriesgar el $O(n^2)$ de quicksort ni gastar la memoria de mergesort, heapsort garantiza $O(n \log n)$ in place. Por eso se usa como mecanismo de prevención (por ejemplo, para cambiar a heapsort si quicksort se está degenerando).

## Preguntas de repaso

> [!question]- ¿Por qué BuildHeap aplica SiftDown solo desde $\lfloor n/2 \rfloor - 1$ hacia atrás?
> Porque desde la posición $\lfloor n/2 \rfloor$ en adelante todos los nodos son hojas, y una hoja ya es un heap. Además, el orden decreciente asegura que, al procesar un nodo, sus subárboles ya son heaps.

> [!question]- ¿Por qué se dice que heapsort es un selection sort con la estructura correcta?
> Ambos llevan repetidamente el máximo (o mínimo) del lado desordenado a la zona ordenada. Selection sort lo busca en $O(n)$, y el heap lo entrega en $O(1)$ y se restaura en $O(\log n)$.

> [!question]- ¿Por qué heapsort no es estable?
> Porque el intercambio de la raíz con el último elemento y los movimientos de SiftDown trasladan elementos a distancia sin respetar el orden original entre llaves iguales.

> [!question]- Si heapsort y mergesort son $O(n \log n)$ en el peor caso, ¿qué ventaja tiene cada uno?
> Heapsort es in place ($O(1)$ de memoria). Mergesort es estable, pero usa $O(n)$ de memoria adicional.
