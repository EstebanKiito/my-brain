---
ramo: "Estructuras de Datos"
tema: "Ordenamiento elemental"
tags:
  - edd
  - ordenamiento
  - insertion-sort
  - origen/complemento
prerrequisitos:
  - "[[01 - Ordenar para buscar y selection sort]]"
---

# Insertion sort

**Insertion sort** ordena como se ordenan naipes en la mano: se toma la carta siguiente y se **inserta en su lugar** entre las que ya están ordenadas. A diferencia de selection sort, que siempre recorre todo lo que falta, insertion sort aprovecha el orden que ya traen los datos: si vienen casi ordenados, casi no mueve nada.

## Versión con lista de salida

```
InsertionSort(A):             // salida: nueva secuencia B, ordenada
1   B <- secuencia vacía
2   tomar el primer dato x de A
3   sacar x de A
4   insertar x en B de modo que B quede ordenada
5   si quedan datos en A, volver a la línea 2
    return B
```

La diferencia con selection sort está en **dónde se trabaja**. Selection *elige* ordenadamente (busca el mínimo en la entrada), e insertion *inserta* ordenadamente (ubica el dato en la salida). Una consecuencia es que **en cada paso la lista $B$ está ordenada**, y de ahí sale su correctitud por inducción. El CB es que un solo elemento está ordenado. En el TI, si $B$ está ordenada y el nuevo dato se inserta entre los valores que lo rodean, $B$ sigue ordenada.

Otra ventaja es que puede ordenar **a medida que los datos llegan** (*online*), porque no necesita ver toda la entrada para empezar.

## El costo de insertar

![Insertar ordenadamente en un arreglo](adjuntos/Insertar%20ordenadamente%20en%20un%20arreglo.png)

> [!example]- Transcripción de la imagen
> Insertar el 20 en el arreglo ordenado 2, 8, 14, 16, 17, 25, 32, 35, 37. Primero "hay que encontrar la posición en la que debe quedar el 20" (entre 17 y 25). Después "estos 4 datos deben ser movidos cada uno un lugar hacia abajo, empezando por el 37" (25, 32, 35 y 37). Al final, el 20 queda en su lugar.

Insertar en un arreglo cuesta $O(n)$, porque hay que correr los mayores. En promedio se mueve la mitad de los datos. En una lista ligada no se corre nada, pero encontrar la posición exige recorrerla, así que también es $O(n)$. Con $n$ inserciones de costo $O(n)$, **insertion sort es $O(n^2)$** en el peor caso.

## Versión in place

```
InsertionSort(A, n):
    for i = 1 ... n-1:
        j = i
        while j > 0 and A[j] < A[j-1]:   // compara hacia la izquierda
            A[j] <-> A[j-1]
            j = j - 1
```

```python
def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A
```

Si los datos vienen ordenados, el `while` **nunca se ejecuta** y el algoritmo hace una sola pasada: $O(n)$. Selection sort compara hacia la **derecha** (busca el mínimo en lo que falta); insertion sort compara hacia la **izquierda** (busca el lugar en lo ya ordenado).

![Pseudocódigo in place de selection e insertion sort](adjuntos/Pseudoc%C3%B3digo%20in%20place%20de%20selection%20e%20insertion%20sort.png)

> [!example]- Transcripción de la imagen
> Los dos pseudocódigos in place lado a lado. `SelectionSort(A, n)`: `for i = 0...n-2`, `min ← i`, `for j = i+1...n-1`, `if A[j] < A[min]: min ← j`, `A[i] ⇄ A[min]`. `InsertionSort(A, n)`: `for i = 1...n-1`, `j ← i`, `while (j > 0) ∧ (A[j] < A[j-1])`, `A[j] ⇄ A[j-1]`, `j ← j-1`.

![Traza de insertion sort sobre SORTINGEXAMPLE](adjuntos/Traza%20de%20insertion%20sort%20sobre%20SORTINGEXAMPLE.png)

> [!example]- Transcripción de la imagen
> Traza por filas de insertion sort sobre las letras S O R T I N G E X A M P L E. En cada fila, en verde subrayado, el prefijo ordenado crece en uno. En rojo está la letra recién insertada. Anotaciones: "datos ordenados: I N O R S T", "último dato insertado ordenadamente: N" y "próximo dato a ser insertado ordenadamente: G". La última fila es A E E G I L M N O P R S T X.

![Animación de insertion sort](adjuntos/Animaci%C3%B3n%20de%20insertion%20sort.gif)

> [!example]- Transcripción de la imagen
> Barras de colores con los valores 8, 5, 3, 2, 6, 9, 7, 4, 1. Cada barra nueva se compara hacia la izquierda y se va corriendo hasta quedar sobre una menor. El prefijo izquierdo queda siempre ordenado y al final están 1 a 9 en orden.

![Animación de insertion sort in place](adjuntos/Animaci%C3%B3n%20de%20insertion%20sort%20in%20place.gif)

> [!example]- Transcripción de la imagen
> "INSERTION SORT" sobre las cajas 3, 2, 8, 1, 5. Cada caja se intercambia con su vecina izquierda mientras sea menor, hasta terminar en 1, 2, 3, 5, 8.

## Preguntas de repaso

> [!question]- ¿Qué invariante mantiene insertion sort en cada paso?
> Que el prefijo procesado (la lista $B$ o la parte izquierda del arreglo) está ordenado. Insertar el siguiente dato en su lugar preserva esa propiedad.

> [!question]- ¿Por qué insertion sort es $O(n)$ si los datos ya vienen ordenados?
> Porque cada nuevo elemento ya es mayor o igual que su vecino izquierdo, así que el `while` no entra nunca y solo queda la pasada del `for`.

> [!question]- ¿Por qué usar una lista ligada no mejora el peor caso de insertion sort?
> Porque aunque insertar en la lista no obligue a correr elementos, encontrar la posición sigue requiriendo recorrerla, en $O(n)$. Son $n$ inserciones de costo $O(n)$, así que el total sigue siendo $O(n^2)$.

> [!question]- ¿Qué significa que insertion sort pueda ordenar "a medida que llegan los datos"?
> Que no necesita la entrada completa: cada dato nuevo se inserta en la parte ya ordenada al llegar. Selection sort, en cambio, necesita ver todos los datos para encontrar el mínimo.
