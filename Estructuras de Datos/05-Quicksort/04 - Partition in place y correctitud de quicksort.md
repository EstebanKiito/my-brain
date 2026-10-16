---
ramo: "Estructuras de Datos"
tema: "Quicksort"
tags:
  - edd
  - quicksort
  - partition
  - in-place
  - correctitud
  - origen/complemento
prerrequisitos:
  - "[[03 - Quicksort]]"
  - "[[02 - Correctitud de algoritmos]]"
---

# Partition in place y correctitud de quicksort

La versión de Partition con listas $m$ y $M$ gasta $O(n)$ de memoria. La versión **in place** reorganiza el arreglo con intercambios y solo dos índices. Gracias a ella, quicksort no necesita memoria adicional para los datos. Su correctitud se prueba con un **invariante**: una propiedad que se mantiene en cada vuelta del ciclo.

## El algoritmo

```
input : arreglo A[0..n-1], índices i, f
output: índice del pivote en la secuencia ordenada
Partition(A, i, f):
1   x <- índice aleatorio en {i, ..., f}
2   p <- A[x]
3   A[x] <-> A[f]            // el pivote se aparta al final
4   j <- i                   // j: frontera entre menores y mayores
5   for k = i ... f-1:
6       if A[k] < p:         // apareció un menor
7           A[j] <-> A[k]    // lo manda a la zona de menores
8           j <- j + 1
9   A[j] <-> A[f]            // el pivote, a su posición ordenada
10  return j
```

![Partition in place](adjuntos/Partition%20in%20place.png)

> [!example]- Transcripción de la imagen
> "Versión *in place* de Partition", con el mismo pseudocódigo de arriba, líneas 1 a 10.

`k` recorre el tramo, `j` marca dónde empieza la zona de mayores, y en todo momento:

$$\underbrace{A[i \dots j-1]}_{< p} \quad \underbrace{A[j \dots k-1]}_{\ge p} \quad \underbrace{A[k \dots f-1]}_{\text{sin revisar}} \quad \underbrace{A[f]}_{p}$$

Al final, `A[j]` es el primero de los mayores. Al intercambiarlo con el pivote, este queda entre ambos grupos: **en su posición ordenada**.

![Video de partition step](adjuntos/Video%20de%20partition%20step.png)

> [!example]- Transcripción de la imagen
> Captura de un video, "The Partition Step": arreglo 9, 7, **10**, 15, 12 con el índice $i$ marcado bajo el 10, y el pseudocódigo `Partition(A, start, end)`: `pivot = A[end]`, `i = start`, `for j = start to end-1: if A[j] ≤ pivot: exchange A[i] with A[j]; i = i + 1`, `exchange A[i] with A[end]`, `return i`. El video es este: https://www.youtube.com/watch?v=UqVxcO4oNXA

## Correctitud de Partition

**Termina**, porque es un `for` sobre un rango finito. **Cumple su propósito**, por inducción sobre las iteraciones:

![Propiedad del invariante](adjuntos/Partition%20in%20place%20-%20propiedad%20del%20invariante.png)

> [!example]- Transcripción de la imagen
> "Demostración (posición del pivote)". Como en la línea final el pivote se pone en la posición $j$, basta demostrar $P(n)$: luego de la $n$-ésima iteración, $A[i \dots j-1]$ contiene solo elementos menores que $p$ y $A[j \dots k-1]$ solo elementos mayores o iguales que $p$.

![Caso base](adjuntos/Partition%20in%20place%20-%20caso%20base.png)

> [!example]- Transcripción de la imagen
> **CB.** $P(1)$ es el estado tras la primera iteración. Si $A[i] < p$, como $i = j$, $A[i]$ se queda en su lugar y $j, k$ aumentan en 1: $A[i \dots j-1]$ tiene solo $A[i]$, que es menor que $p$, y $A[j \dots k-1]$ está vacío. Si $A[i] \ge p$, no aumenta $j$ pero sí $k$: $A[i \dots j-1]$ está vacío y $A[j \dots k-1]$ tiene un elemento mayor o igual que $p$.

![Hipótesis inductiva](adjuntos/Partition%20in%20place%20-%20hip%C3%B3tesis%20inductiva.png)

> [!example]- Transcripción de la imagen
> **H.I.** Se cumple después de la $n$-ésima iteración: $A[i \dots j-1]$ contiene solo menores que $p$, y $A[j \dots k-1]$ solo mayores o iguales.

![Tesis inductiva](adjuntos/Partition%20in%20place%20-%20tesis%20inductiva.png)

> [!example]- Transcripción de la imagen
> **T.I.** En la iteración $n+1$ hay dos casos. Si $A[k] < p$, se intercambia a la posición $j$ antes de aumentar ambos índices; por H.I. los anteriores eran menores, y el elemento que salió de $j$ (mayor o igual) pasa a $k$, así que se mantiene la condición. Si $A[k] \ge p$, no hay intercambio y solo aumenta $k$; por H.I. $A[j \dots k-1]$ sigue teniendo solo mayores o iguales.

## Correctitud de quicksort

![Finitud parte 1](adjuntos/Quicksort%20-%20finitud%20parte%201.png)

> [!example]- Transcripción de la imagen
> "Demostración (finitud)". Partition termina, así que la línea 2 de Quicksort toma pasos finitos. Cada llamado recursivo es sobre una instancia de tamaño $d = f - i$ estrictamente menor. Si $d < 0$, Quicksort termina sin llamados recursivos.

![Finitud parte 2](adjuntos/Quicksort%20-%20finitud%20parte%202.png)

> [!example]- Transcripción de la imagen
> Si $d \ge 0$, hay dos llamados de tamaños $d_1 = p - 1 - i < d$ y $d_2 = f - p - 1 < d$: con cada llamado, $d$ baja al menos en 1. Como el llamado inicial es `Quicksort(A, 0, n-1)`, la profundidad máxima es $n - 1$ y el algoritmo termina.

![Demostración de ordenación](adjuntos/Quicksort%20-%20demostraci%C3%B3n%20de%20ordenaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "Demostración (ordenación)". Partition ubica bien el pivote, así que basta demostrar que todo elemento de $A[0 \dots n-1]$ es pivote en algún llamado. Si $i > f$ no hay elementos; si $i \le f$, se escoge un pivote y los dos llamados suman $f - i - 1$ elementos. Como los llamados reducen su tamaño hasta quedar vacíos y cada llamado no vacío escoge un pivote, todo elemento es pivote en algún momento, y por lo tanto todo queda ordenado.

> [!tip] La idea de la demostración
> Quicksort es correcto si **todo elemento llega a ser pivote** en algún momento, porque cada pivote queda en su lugar definitivo. Los llamados recursivos se achican estrictamente y nunca pierden elementos (solo sacan al pivote), así que eso está garantizado.

## Preguntas de repaso

> [!question]- ¿Qué invariante mantiene Partition in place?
> Que `A[i..j-1]` tiene solo elementos menores que el pivote y `A[j..k-1]` solo mayores o iguales. Al terminar, el pivote se intercambia con `A[j]` y queda entre ambos grupos.

> [!question]- ¿Por qué se mueve el pivote al final antes de empezar?
> Para sacarlo del recorrido y no tener que seguir dónde quedó durante los intercambios. Al final se intercambia una sola vez con la frontera `j`.

> [!question]- ¿Por qué quicksort termina?
> Porque cada llamado recursivo trabaja sobre un rango estrictamente más chico (sin el pivote) y los rangos vacíos no hacen llamados. La profundidad es como máximo $n - 1$.
