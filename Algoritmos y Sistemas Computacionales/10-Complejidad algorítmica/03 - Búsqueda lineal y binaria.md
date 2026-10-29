---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Complejidad algorítmica"
tags:
  - algoritmos/complejidad
  - algoritmos/busqueda
  - origen/complemento
prerrequisitos:
  - "[[02 - Crecimiento y notación asintótica|Crecimiento y notación asintótica]]"
---

# Búsqueda lineal y binaria

Buscar un valor en una lista es un problema cotidiano en programación. Hay dos estrategias clásicas: revisar uno por uno (**búsqueda lineal**) o descartar la mitad en cada paso (**búsqueda binaria**). La diferencia de complejidad es enorme cuando la lista crece.

## Búsqueda lineal

Se recorre la lista desde el principio hasta encontrar el valor o llegar al final.

```python
def busqueda_lineal(lista, x):
    for i, valor in enumerate(lista):
        if valor == x:
            return i
    return -1

print(busqueda_lineal([5, 2, 8, 1], 8))  # 2
```

En el peor caso (el valor no está o está al final) se revisan los $n$ elementos. Su complejidad es $O(n)$. No necesita que la lista esté ordenada.

## Búsqueda binaria

Si la lista está **ordenada**, se compara el valor buscado con el elemento del medio:

- Si es igual, se encontró.
- Si es menor, se busca en la mitad izquierda.
- Si es mayor, se busca en la mitad derecha.

```python
def busqueda_binaria(lista, x):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == x:
            return medio
        if x < lista[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1
    return -1

print(busqueda_binaria([1, 3, 5, 7, 9], 7))  # 3
```

En cada paso se descarta la mitad de la lista. El número de pasos es $\log_2 n$, así que su complejidad es $O(\log n)$.

## La diferencia en números

| Tamaño de la lista | Búsqueda lineal (peor caso) | Búsqueda binaria |
|---:|---:|---:|
| 10 | 10 comparaciones | ~4 |
| 1.000 | 1.000 | ~10 |
| 1.000.000 | 1.000.000 | ~20 |

> [!tip] La idea central
> La búsqueda binaria es muchísimo más rápida para listas grandes, pero exige que la lista esté ordenada. Ordenar cuesta tiempo; si se hacen muchas búsquedas, ese costo se recupera.

> [!warning] La búsqueda binaria no sirve en listas desordenadas
> Si la lista no está ordenada, comparar con el medio no dice nada sobre dónde puede estar el valor. En ese caso hay que ordenar primero o usar búsqueda lineal.

## Preguntas de repaso

> [!question]- ¿Por qué la búsqueda lineal es $O(n)$?
> Porque en el peor caso revisa los $n$ elementos de la lista, uno por uno.

> [!question]- ¿Por qué la búsqueda binaria es $O(\log n)$?
> Porque en cada paso descarta la mitad de los elementos. El número de pasos es el logaritmo en base 2 de $n$.

> [!question]- ¿Qué requisito tiene la búsqueda binaria?
> Que la lista esté ordenada. Sin orden, no se puede decidir en qué mitad seguir buscando.

> [!question]- ¿Cuándo conviene ordenar una lista para usar búsqueda binaria?
> Cuando se harán muchas búsquedas sobre los mismos datos. El costo de ordenar una vez se compensa con la velocidad de las búsquedas.
