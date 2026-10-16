---
ramo: "Estructuras de Datos"
tema: "Análisis de algoritmos"
tags:
  - edd
  - busqueda-binaria
  - dividir-para-conquistar
  - recursion
  - origen/complemento
prerrequisitos:
  - "[[03 - Notación asintótica O, Omega y Theta]]"
---

# Búsqueda binaria y dividir para conquistar

Una de las razones principales para **ordenar** es que así se **busca** mucho más rápido. En una secuencia desordenada, el peor caso es que el dato no esté: hay que revisar uno por uno hasta el final, en $O(n)$. Si la secuencia está ordenada, se puede descartar la mitad de los datos en cada comparación y encontrar el dato en $O(\log_2 n)$. Con un millón de datos, eso es la diferencia entre un millón de comparaciones y unas 20.

## La estrategia: dividir para conquistar

**Dividir para conquistar** (*divide and conquer*) es una estrategia general de diseño de algoritmos:

1. **Dividir** el problema original en dos o más subproblemas del mismo tipo.
2. **Resolver** recursivamente cada subproblema.
3. **Combinar** las soluciones de los subproblemas para obtener la del problema original.

Sirve para ordenar (mergesort y quicksort), para descomponer problemas sobre árboles o bases de datos y, en su forma más simple, para buscar. Su justificación natural es la [[01 - Inducción simple, fuerte y estructural|inducción fuerte]]: se supone resuelto cualquier problema más chico.

## Búsqueda binaria

```
input : Secuencia ORDENADA A[0..n-1], elemento x, índices i, f
output: Índice m ∈ {0, ..., n-1} con A[m] = x, o -1
BinarySearch(A, x, i, f):
1   if f < i: return -1
2   m = ⌊(i + f) / 2⌋
3   if A[m] = x: return m
4   if A[m] > x:
5       return BinarySearch(A, x, i, m - 1)    // mitad izquierda
6   return BinarySearch(A, x, m + 1, f)        // mitad derecha
```

Así se ven las tres etapas de dividir para conquistar en este caso:

- **Dividir:** se elige un **pivote central** $m$ (línea 2).
- **Resolver:** como $A$ está ordenado, comparar con $A[m]$ basta para saber en qué mitad puede estar $x$. Solo se resuelve **uno** de los dos subproblemas.
- **Combinar:** no hay nada que combinar. La solución del problema es exactamente la del llamado recursivo.

```python
def binary_search(A, x, i, f):
    """Índice de x en A[i..f] (A ordenado) o -1."""
    if f < i:
        return -1
    m = (i + f) // 2
    if A[m] == x:
        return m
    if A[m] > x:
        return binary_search(A, x, i, m - 1)   # mitad izquierda
    return binary_search(A, x, m + 1, f)       # mitad derecha

A = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
print(binary_search(A, 37, 0, len(A) - 1))   # 11
print(binary_search(A, 4, 0, len(A) - 1))    # -1
```

![Búsqueda binaria frente a búsqueda secuencial](adjuntos/B%C3%BAsqueda%20binaria%20frente%20a%20b%C3%BAsqueda%20secuencial.gif)

> [!example]- Transcripción de la imagen
> Animación que busca el 37 en el arreglo ordenado 1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59 (índices 0 a 16). Arriba, *binary search* parte con `low` = 0, `mid` = 8 (valor 23) y `high` = 16, y va acortando el rango a la mitad. Abajo, *sequential search* avanza casilla por casilla. Cada búsqueda lleva un contador de pasos (`steps`). Siguiendo el algoritmo, la binaria encuentra el 37 en 4 pasos (23 → 41 → 31 → 37), mientras que la secuencial revisa 12 casillas (índices 0 a 11).

## Complejidad

Cada llamada hace trabajo constante y deja un subproblema de la mitad del tamaño:

$$T(n) = T(n/2) + O(1) \quad\Rightarrow\quad T(n) \in O(\log n)$$

El rango se puede dividir por 2 solo $\lfloor \log_2 n \rfloor + 1$ veces antes de quedar vacío. Con $n = 10^6$ son a lo más 20 comparaciones.

> [!warning] Requisitos que se olvidan
> - La secuencia tiene que estar **ordenada**. Si no lo está, descartar una mitad puede descartar justo el dato buscado.
> - Se necesita **acceso por índice en $O(1)$**, como en un arreglo. En una lista ligada, llegar al elemento del medio ya cuesta $O(n)$ y se pierde la ventaja.

## Preguntas de repaso

> [!question]- ¿Por qué la búsqueda binaria resuelve solo uno de los dos subproblemas?
> Porque al estar ordenada la secuencia, comparar $x$ con el pivote $A[m]$ garantiza que $x$ no puede estar en una de las mitades. Esa mitad se descarta entera sin revisarla.

> [!question]- ¿Cuál es la etapa de "combinar" en la búsqueda binaria?
> Es trivial: la respuesta del problema es la respuesta del llamado recursivo, sin procesarla. En mergesort, en cambio, combinar (el *merge*) es la parte costosa.

> [!question]- ¿Cuántas comparaciones hace como máximo una búsqueda binaria sobre un millón de datos, y cuántas una secuencial?
> La binaria hace a lo más $\lfloor \log_2 10^6 \rfloor + 1 = 20$. La secuencial, en el peor caso (dato ausente), hace $10^6$.

> [!question]- ¿Por qué no conviene hacer búsqueda binaria sobre una lista ligada?
> Porque la búsqueda binaria necesita acceder al elemento del medio en tiempo constante. En una lista ligada eso exige recorrerla desde el inicio, en $O(n)$, y el costo total deja de ser logarítmico.
