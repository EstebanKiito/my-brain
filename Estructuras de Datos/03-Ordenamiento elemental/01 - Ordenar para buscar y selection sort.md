---
ramo: "Estructuras de Datos"
tema: "Ordenamiento elemental"
tags:
  - edd
  - ordenamiento
  - selection-sort
  - origen/complemento
prerrequisitos:
  - "[[02 - Correctitud de algoritmos]]"
  - "[[04 - Búsqueda binaria y dividir para conquistar]]"
---

# Ordenar para buscar y selection sort

Ordenar tiene sentido sobre todo porque facilita **encontrar**. En datos desordenados, el peor caso es que lo buscado no esté, y hay que revisar todo: $O(n)$. Con los datos ordenados se puede usar [[04 - Búsqueda binaria y dividir para conquistar|búsqueda binaria]], en $O(\log n)$, y con muchos datos el logaritmo es muchísimo menor que el lineal. Cualquier cosa a la que se le pueda poner una etiqueta comparable se puede ordenar.

> [!tip] Definición
> Una secuencia $a_1, a_2, \dots, a_n$ está **ordenada** (de forma no decreciente) si $a_1 \le a_2 \le \dots \le a_n$. **Ordenar** es encontrar una permutación de la secuencia que cumpla esa condición.

## La idea: elegir el menor, una y otra vez

**Selection sort** es la estrategia más directa: buscar el menor, ponerlo primero, buscar el menor de lo que queda, ponerlo segundo, y así hasta terminar. Su primera versión usa una lista de salida y ya se demostró correcta en [[02 - Correctitud de algoritmos|Correctitud de algoritmos]]. Esa versión usa el **doble de memoria**, porque saca los datos de una lista para escribirlos en otra. La versión **in place** hace lo mismo dentro del mismo arreglo: la parte izquierda es la "salida" ordenada y la derecha es lo que falta.

```
SelectionSort(A, n):          // A[0..n-1], n >= 2
    for i = 0 ... n-2:        // i: posición que se fija en esta vuelta
        min = i
        for j = i+1 ... n-1:  // busca el mínimo de A[i..n-1]
            if A[j] < A[min]: min = j
        A[i] <-> A[min]       // un intercambio por vuelta
```

```python
def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]
    return A

print(selection_sort([6, 8, 3, 5, 9, 10, 7, 2, 4, 1]))   # [1, 2, ..., 10]
```

![Animación de selection sort](adjuntos/Animaci%C3%B3n%20de%20selection%20sort.gif)

> [!example]- Transcripción de la imagen
> Animación sobre el arreglo 6, 8, 3, 5, 9, 10, 7, 2, 4, 1. Leyenda: "Yellow is smallest number found, Blue is current item, Green is sorted list". En cada pasada, el cursor azul recorre lo que falta, el amarillo marca el mínimo encontrado hasta ese momento y al final ese mínimo pasa a la zona verde ordenada, a la izquierda.

![Animación de selection sort in place](adjuntos/Animaci%C3%B3n%20de%20selection%20sort%20in%20place.gif)

> [!example]- Transcripción de la imagen
> "SELECTION SORT" sobre las cajas 3, 2, 8, 1, 5. En cada paso se busca el menor entre las cajas no ordenadas y se intercambia con la primera de ellas, hasta llegar a 1, 2, 3, 5, 8.

## Complejidad

![Cálculo de la complejidad de selection sort](adjuntos/C%C3%A1lculo%20de%20la%20complejidad%20de%20selection%20sort.png)

> [!example]- Transcripción de la imagen
> "De forma explícita": buscar el menor de $A$ implica revisar $n$ elementos en la primera iteración y $n-1$ en la siguiente, y así hasta que $A$ tiene 1 elemento. El tiempo es la suma: $T(n) = n + (n-1) + \dots + 2 + 1 = \sum_{i=1}^{n} i = \frac{n(n-1)}{2}$. Conclusión: $T(n) \in \mathcal{O}(n^2)$.

| Propiedad | Selection sort |
|---|---|
| Tiempo | $\Theta(n^2)$ en **todos** los casos |
| Intercambios | $O(n)$: exactamente uno por vuelta |
| Memoria adicional | $O(1)$ (in place) |
| Adaptativo | No: no tiene un mejor caso, porque el orden inicial de los datos no cambia el trabajo |
| Estable | No (ver [[04 - Propiedades de los algoritmos de ordenación\|propiedades]]) |

Contado con precisión, el ciclo interno compara $n-1, n-2, \dots, 1$ veces, así que hay $\frac{n(n-1)}{2}$ comparaciones: $\Theta(n^2)$.

Es fácil de entender, es difícil equivocarse al implementarlo y es rápido con **pocos datos**. Por eso es razonable para conjuntos pequeños. La página de visualizaciones de la Universidad de San Francisco (http://cis.usfca.edu) anima este y los demás algoritmos del curso.

## Preguntas de repaso

> [!question]- ¿Por qué selection sort hace siempre la misma cantidad de comparaciones, sin importar el orden inicial?
> Porque en cada vuelta recorre todo lo que falta para encontrar el mínimo, aunque ya esté en su lugar. Nunca puede saltarse ese recorrido, así que no tiene un mejor caso más rápido.

> [!question]- ¿Cuántos intercambios hace selection sort y por qué es una ventaja?
> A lo más $n-1$, uno por vuelta. Si intercambiar es caro (por ejemplo, registros grandes), hace muchos menos movimientos que otros algoritmos $O(n^2)$.

> [!question]- ¿Qué gana la versión in place respecto de la versión con lista de salida?
> Memoria: usa $O(1)$ adicional en vez de duplicar los datos. La parte izquierda del mismo arreglo cumple el rol de la lista de salida.

> [!question]- ¿Por qué ordenar ayuda a buscar?
> Porque en una secuencia ordenada se puede descartar la mitad en cada comparación (búsqueda binaria, $O(\log n)$), en vez de revisar todos los elementos ($O(n)$).
