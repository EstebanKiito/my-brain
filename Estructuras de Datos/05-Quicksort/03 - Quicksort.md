---
ramo: "Estructuras de Datos"
tema: "Quicksort"
tags:
  - edd
  - ordenamiento
  - quicksort
  - dividir-para-conquistar
  - origen/complemento
prerrequisitos:
  - "[[02 - Algoritmos Partition y Median]]"
  - "[[02 - Mergesort y su recurrencia]]"
---

# Quicksort

En el peor caso de [[02 - Algoritmos Partition y Median|Median]], todos los elementos terminan siendo pivotes. Y si **todos** los elementos son pivotes, cada uno está en su posición ordenada: el arreglo quedó **ordenado**. Ordenar con Partition a propósito es **quicksort**. Su nombre no se llama "partition sort" por razones históricas.

![Cada pivote queda en su posición ordenada](adjuntos/Cada%20pivote%20queda%20en%20su%20posici%C3%B3n%20ordenada.png)

> [!example]- Transcripción de la imagen
> "Luego de cada ejecución de Partition, el pivote queda en su posición ordenada". Arreglo 1, 2, 3, 4, 3, 5, 6, 7, 9, 7, 8 con el 6 fijo (gris). Debajo, el tramo izquierdo 1, 2, 3, 5, 4 con el 2 fijo. "Además, las dos sub-secuencias están *del lado correcto* del pivote".

![Quicksort como dividir para conquistar](adjuntos/Quicksort%20como%20dividir%20para%20conquistar.png)

> [!example]- Transcripción de la imagen
> "Nuevamente podemos usar la estrategia dividir para conquistar": 1. dividir el problema en dos sub-problemas con Partition; 2. aplicar recursivamente Partition a cada sub-secuencia; 3. no hace falta combinar nada, porque la secuencia queda ordenada. "Llamaremos Quicksort a este algoritmo".

```
input : secuencia A[0..n-1], índices i, f
output: ∅  (ordena A en su lugar)
QuickSort(A, i, f):
    if i <= f:
        p <- Partition(A, i, f)
        QuickSort(A, i, p-1)
        QuickSort(A, p+1, f)
// llamado inicial: QuickSort(A, 0, n-1)
```

> [!tip] Mergesort al revés
> Mergesort divide **sin pensar** (por la mitad) y hace el trabajo al **combinar** (merge). Quicksort hace el trabajo al **dividir** (partition) y no necesita combinar nada. Quicksort "particiona para ordenar".

## Trazas

![Traza de quicksort sobre ASORTINGEXAMPLE](adjuntos/Traza%20de%20quicksort%20sobre%20ASORTINGEXAMPLE.png)

> [!example]- Transcripción de la imagen
> Quicksort sobre A S O R T I N G E X A M P L E, con el pivote siempre en el extremo derecho del subarreglo ($A[f]$). En cada fila, la letra en rojo es el pivote, que queda fijo en su posición. Los subarreglos se achican hasta letras sueltas y la última fila es A A E E G I L M N O P R S T X.

![Traza de quicksort con pivotes por nivel](adjuntos/Traza%20de%20quicksort%20con%20pivotes%20por%20nivel.png)

> [!example]- Transcripción de la imagen
> Arreglo 7, 3, 5, 2, 1, 9, 7, 8, 6, 4, 3. En el primer nivel el pivote 6 (gris) separa menores (amarillo) y mayores (lila). En cada nivel siguiente se fijan nuevos pivotes en gris dentro de cada tramo, hasta la fila final 1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, toda en gris.

```python
import random

def partition(A, i, f):
    x = random.randint(i, f)
    A[x], A[f] = A[f], A[x]
    p, j = A[f], i
    for k in range(i, f):
        if A[k] < p:
            A[j], A[k] = A[k], A[j]
            j += 1
    A[j], A[f] = A[f], A[j]
    return j

def quicksort(A, i, f):
    if i <= f:
        p = partition(A, i, f)
        quicksort(A, i, p - 1)
        quicksort(A, p + 1, f)

B = list("ASORTINGEXAMPLE"); quicksort(B, 0, len(B) - 1); print("".join(B))   # AAEEGILMNOPRSTX
```

(Esta es la [[04 - Partition in place y correctitud de quicksort|versión in place de Partition]].)

## El peor caso y el pivote aleatorio

Si la secuencia **ya viene ordenada** y el pivote es siempre el primero (o el último), cada partición deja un lado vacío y el otro con $n-1$ elementos. Son $n$ niveles de $O(n)$ trabajo: **$O(n^2)$**, tan malo como selection sort. Elegir el pivote **al azar** hace muy improbable caer en ese caso, y además impide que alguien *envenene* la entrada.

## Cuándo usarlo

Quicksort es un excelente **algoritmo de propósito general**: rápido en promedio, sin memoria adicional para los datos y una buena opción cuando no se sabe nada de la entrada. Su costo es la recursión: con muchísimos datos, la pila de llamadas pesa. También se **paraleliza** mejor que mergesort, porque cada partición se puede entregar a otro procesador. En mergesort, en cambio, el merge final lo hace un solo procesador y se vuelve un cuello de botella.

## Preguntas de repaso

> [!question]- ¿Por qué quicksort no necesita un paso de combinación?
> Porque Partition ya deja cada lado en su lugar correcto respecto del pivote. Cuando los dos lados están ordenados, todo el arreglo lo está.

> [!question]- ¿Qué entrada provoca el peor caso de quicksort con pivote fijo en el primer elemento?
> Una secuencia ya ordenada (o al revés): cada partición deja un lado vacío y el otro con $n-1$ elementos, así que el costo es $O(n^2)$.

> [!question]- ¿Qué gana quicksort al elegir el pivote al azar?
> Que ninguna entrada en particular sea siempre mala. El peor caso pasa a depender de la mala suerte y no de los datos, y se vuelve muy improbable.

> [!question]- ¿Por qué quicksort se paraleliza mejor que mergesort?
> Porque después de particionar, los dos lados son completamente independientes y pueden ordenarse en paralelo sin combinar. Mergesort termina siempre en un merge secuencial del arreglo completo.
