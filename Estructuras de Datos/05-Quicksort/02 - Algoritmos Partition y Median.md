---
ramo: "Estructuras de Datos"
tema: "Quicksort"
tags:
  - edd
  - partition
  - mediana
  - estadisticos-de-orden
  - origen/complemento
prerrequisitos:
  - "[[01 - Mediana y búsqueda por partición]]"
---

# Algoritmos Partition y Median

La estrategia de la [[01 - Mediana y búsqueda por partición|mediana por partición]] se formaliza en dos algoritmos: **Partition**, que ubica un pivote en su posición ordenada, y **Median**, que llama a Partition hasta que el pivote cae en el centro.

## Partition (con memoria adicional)

![Partición en menores y mayores al pivote](adjuntos/Partici%C3%B3n%20en%20menores%20y%20mayores%20al%20pivote.png)

> [!example]- Transcripción de la imagen
> Si no hay elementos iguales al pivote, elegir un pivote $p$ **particiona** la secuencia en los mayores $M = \{a_i \mid a_i > p\}$ y los menores $m = \{a_i \mid a_i < p\}$. Si se colocan primero los de $m$, luego $p$ y finalmente los de $M$, $p$ queda en su posición ordenada.

```
input : secuencia A[0..n-1], índices i, f      // sin repetidos
output: índice del pivote en la secuencia ordenada
Partition(A, i, f):
1   p <- pivote aleatorio en A[i..f]
2   m, M <- secuencias vacías
3   insertar p en M
4   for x in A[i..f]:
5       if x < p: insertar x en m
6       elif x > p: insertar x en M
7   A[i..f] <- Concat(m, M)                    // p es el menor de M: queda justo después de m
8   return i + |m|
```

![Qué retorna Partition](adjuntos/Qu%C3%A9%20retorna%20Partition.png)

> [!example]- Transcripción de la imagen
> Se ubican los menores, el pivote y luego los mayores. $i$ = número de elementos a la izquierda de $A[i]$; $|m|$ = número de menores a $p$ en $A[i, f]$. Por lo tanto, se retorna la posición correcta de $p$.

![Costo de Partition con memoria adicional](adjuntos/Costo%20de%20Partition%20con%20memoria%20adicional.png)

> [!example]- Transcripción de la imagen
> Las inserciones al final de la EDD son $\mathcal{O}(1)$ en arreglos y listas, una por elemento: total $\mathcal{O}(n)$. La concatenación es $\mathcal{O}(1)$ en listas y $\mathcal{O}(n)$ en arreglos.

![Memoria adicional de Partition](adjuntos/Memoria%20adicional%20de%20Partition.png)

> [!example]- Transcripción de la imagen
> "Además, usa memoria adicional $\mathcal{O}(n)$ para mantener las secuencias $m$, $M$".

Partition cuesta **$O(n)$ en tiempo y $O(n)$ en memoria**. Más adelante se verá una versión in place.

## Median

```
input : secuencia A[0..n-1]
output: elemento en la posición central de A
Median(A):
    i <- 0;  f <- n-1
    x <- Partition(A, i, f)
    while x no es el centro:
        if x < centro: i <- x + 1      // la mediana está a la derecha
        else:          f <- x - 1      // la mediana está a la izquierda
        x <- Partition(A, i, f)
    return A[x]
```

```python
import random

def partition_extra(A, i, f, p_idx):
    p = A[p_idx]
    m = [x for x in A[i:f + 1] if x < p]
    M = [x for x in A[i:f + 1] if x > p]
    A[i:f + 1] = m + [p] + M
    return i + len(m)

def median(A):
    i, f, centro = 0, len(A) - 1, len(A) // 2
    x = partition_extra(A, i, f, random.randint(i, f))
    while x != centro:
        if x < centro: i = x + 1
        else: f = x - 1
        x = partition_extra(A, i, f, random.randint(i, f))
    return A[x]

print(median([7, 3, 5, 2, 1, 9, 6, 8, 4, 10, 0]))   # 5
```

![Qué entrega Median](adjuntos/Qu%C3%A9%20entrega%20Median.png)

> [!example]- Transcripción de la imagen
> Median entrega el elemento en la posición central ordenada. Para $n$ impar, `Median(A)` es la mediana; para $n$ par, es uno de los dos elementos centrales.

Cambiando "el centro" por cualquier posición $k$, el mismo algoritmo encuentra el **$k$-ésimo estadístico de orden** (el $k$-ésimo menor), sin ordenar.

## Complejidad

![Mejor y peor caso de Median](adjuntos/Mejor%20y%20peor%20caso%20de%20Median.png)

> [!example]- Transcripción de la imagen
> **Mejor caso**: escoger la mediana como primer pivote. Separar los demás en $m$ y $M$ toma $\mathcal{O}(n)$, y como se toma un solo pivote, el total es $\mathcal{O}(n)$. **Peor caso**: que todos los datos menos la mediana sean escogidos como pivote. Cada pivote cuesta $\mathcal{O}(n)$ y son $\mathcal{O}(n)$ pivotes: total $\mathcal{O}(n^2)$.

> [!warning] El azar importa
> Si el pivote se eligiera siempre en una posición fija (por ejemplo, el primero), alguien que conoce el algoritmo podría armar una entrada que lo haga caer siempre en el peor caso. A eso se le llama **envenenar** la entrada. Con un pivote aleatorio, el peor caso se vuelve muy improbable.

## Preguntas de repaso

> [!question]- ¿Por qué Partition retorna `i + |m|`?
> Porque en `A[i..f]` quedan primero los $|m|$ menores y justo después el pivote. Su índice absoluto es el inicio del tramo más la cantidad de menores.

> [!question]- ¿Cómo se adapta Median para encontrar el $k$-ésimo menor?
> Reemplazando "el centro" por $k$: se particiona y se sigue a la izquierda o a la derecha según la posición del pivote, hasta que caiga en $k$.

> [!question]- ¿Cuál es el peor caso de Median y cuánto cuesta?
> Que el pivote nunca sea la mediana y se descarte un solo elemento por vez, hasta haber elegido $O(n)$ pivotes. Cada partición cuesta $O(n)$, así que el total es $O(n^2)$.
