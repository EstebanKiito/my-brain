---
ramo: "Estructuras de Datos"
tema: "Ordenamiento elemental"
tags:
  - edd
  - ordenamiento
  - estabilidad
  - in-place
  - origen/complemento
prerrequisitos:
  - "[[03 - Inversiones y análisis de casos de insertion sort]]"
---

# Propiedades de los algoritmos de ordenación

Dos algoritmos con la misma complejidad pueden no ser intercambiables. Además del tiempo, cada algoritmo de ordenación se describe con un puñado de propiedades que deciden si sirve para un problema concreto. Estas propiedades se usan para comparar todos los algoritmos del curso.

## Las propiedades

- **In place:** usa $O(1)$ de memoria adicional y ordena dentro del mismo arreglo.
- **Adaptativo:** aprovecha el orden que ya traen los datos, es decir, tiene un mejor caso más rápido cuando la entrada está casi ordenada.
- **Estable:** si dos elementos tienen la **misma clave**, conservan en la salida el orden relativo que tenían en la entrada.
- **Online:** puede ordenar a medida que llegan los datos, sin conocer la entrada completa.

> [!tip] Por qué importa la estabilidad
> Permite ordenar por **dos criterios**. Si se ordena primero por nombre y después, con un algoritmo estable, por nota, los empatados en nota quedan ordenados por nombre. Con un algoritmo no estable, ese primer orden se pierde.

```python
datos = [("ana", 5), ("beto", 4), ("cata", 5), ("dani", 3)]
# ordenando por nota (x[1]) con cada algoritmo:
# selection sort -> [('dani', 3), ('beto', 4), ('cata', 5), ('ana', 5)]   cata pasó delante de ana
# insertion sort -> [('dani', 3), ('beto', 4), ('ana', 5), ('cata', 5)]   se respeta el orden original
```

Selection sort no es estable porque el **intercambio a distancia** puede saltarse a un elemento igual. En el ejemplo, el primer intercambio lleva a `ana` (5) hasta el final, detrás de `cata` (5). Insertion sort sí es estable, porque solo intercambia **vecinos estrictamente desordenados** (`A[j] < A[j-1]`) y dos iguales nunca se cruzan.

## Comparación de los algoritmos elementales

| | Selection sort | Insertion sort | Bubble sort |
|---|---|---|---|
| Peor caso | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ |
| Mejor caso | $O(n^2)$ | $O(n)$ (ordenado) | $O(n)$ (con corte si no hay intercambios) |
| Intercambios | $O(n)$ | $O(n^2)$ (uno por inversión) | $O(n^2)$ |
| Memoria adicional | $O(1)$ | $O(1)$ | $O(1)$ |
| Adaptativo | No | Sí | Sí |
| Estable | No | Sí | Sí |
| Online | No | Sí | No |

[[02 - Correctitud de algoritmos|Bubble sort]] se vio como ejemplo de correctitud. Su comportamiento se parece al de insertion sort, pero hace más intercambios.

## Cuándo usar cada uno

- **Selection sort:** con **pocos datos** (del orden de 100 o menos), cuando se busca algo simple y difícil de equivocar, o cuando intercambiar es caro.
- **Insertion sort:** cuando los datos vienen **casi ordenados** o llegan de a uno. Por eso los algoritmos $O(n \log n)$ prácticos lo usan para las particiones pequeñas.
- **Ninguno de los dos** para muchos datos desordenados: para eso están mergesort, quicksort y heapsort, de $O(n \log n)$.

> [!warning] Paralelizar no los salva
> Selection e insertion sort avanzan de a un elemento sobre una sola zona ordenada, así que no se reparten bien entre varios procesadores. Los algoritmos de dividir para conquistar sí se pueden paralelizar.

## Preguntas de repaso

> [!question]- ¿Qué significa que un algoritmo de ordenación sea estable y para qué sirve?
> Que los elementos con la misma clave mantienen su orden relativo original. Sirve para ordenar por varios criterios, aplicando primero el secundario y después el principal con un algoritmo estable.

> [!question]- ¿Por qué selection sort no es estable, pero insertion sort sí?
> Selection intercambia el mínimo con una posición lejana, y eso puede pasar a un elemento por encima de otro con la misma clave. Insertion solo intercambia vecinos con `A[j] < A[j-1]` estricto, así que dos elementos iguales nunca se cruzan.

> [!question]- ¿Qué significa que un algoritmo sea adaptativo? Da un ejemplo y un contraejemplo.
> Que su costo baja cuando la entrada ya está parcialmente ordenada. Insertion sort es adaptativo ($O(n + k)$), y selection sort no lo es (siempre $\Theta(n^2)$).

> [!question]- Si intercambiar dos registros es muy caro, ¿qué algoritmo elemental conviene y por qué?
> Selection sort, porque hace a lo más $n-1$ intercambios. Insertion y bubble sort pueden hacer $O(n^2)$.
