---
ramo: "Introducción a la Programación"
tema: "Ordenamiento"
tags:
  - programacion/ordenamiento
  - origen/complemento
prerrequisitos:
  - "[[01 - Sort, sorted y criterios con key]]"
  - "[[04 - Patrones con ciclos: máximo, mínimo y dígitos]]"
---

# Selection sort: ordenar a mano

`sort` resuelve el problema en una línea, pero ¿cómo lo hace? Programar un **algoritmo de ordenamiento** desde cero es un excelente ejercicio para combinar ciclos, listas y el patrón del mínimo, y es la puerta de entrada a los algoritmos más eficientes que se estudian después.

## La idea

**Selection sort** (ordenamiento por selección) ordena como lo haría una persona con un montón de cartas:

1. Buscar la carta **más chica** de todas y ponerla **primera**.
2. De las que quedan, buscar la más chica y ponerla **segunda**.
3. Repetir hasta llegar al final.

En una lista, "ponerla primera" significa **intercambiarla** con la que estaba en esa posición.

## Traza con `[45, 12, 10, 33, 9]`

| Pasada | Parte sin ordenar | Mínimo | Intercambio | Lista después |
|---|---|---|---|---|
| 0 | `[45, 12, 10, 33, 9]` | 9 (pos. 4) | posiciones 0 y 4 | `[9, 12, 10, 33, 45]` |
| 1 | `[12, 10, 33, 45]` | 10 (pos. 2) | posiciones 1 y 2 | `[9, 10, 12, 33, 45]` |
| 2 | `[12, 33, 45]` | 12 (pos. 2) | ninguno (ya está) | `[9, 10, 12, 33, 45]` |
| 3 | `[33, 45]` | 33 (pos. 3) | ninguno | `[9, 10, 12, 33, 45]` |

Después de cada pasada, la parte izquierda de la lista ya está ordenada y no se vuelve a tocar.

## Versión con `min` e `index`

```python
def ordenar_facil(lista):
    for ip in range(len(lista)):
        menor = min(lista[ip:])                  # el mínimo de lo que falta
        m = lista[ip:].index(menor) + ip         # su posición en la lista completa
        lista[ip], lista[m] = lista[m], lista[ip]

l = [45, 12, 10, 45, 33, 9]
ordenar_facil(l)
print(l)      # [9, 10, 12, 33, 45, 45]
```

Ojo con el `+ ip`: `index` entrega la posición **dentro del slice** `lista[ip:]`, que empieza en `ip`.

## Versión "a mano"

La búsqueda del mínimo es el patrón que ya se conoce: recordar la posición del menor visto hasta ahora.

```python
def selection_sort(lista):
    for ip in range(len(lista)):
        m = ip                                  # posición del menor hasta ahora
        for i in range(ip + 1, len(lista)):
            if lista[i] < lista[m]:
                m = i
        lista[ip], lista[m] = lista[m], lista[ip]

l = [45, 12, 10, 45, 33, 45, 12, 9]
selection_sort(l)
print(l)
```

```
[9, 10, 12, 12, 33, 45, 45, 45]
```

## Intercambiar dos valores

`a, b = b, a` intercambia dos variables en una línea: Python calcula primero todo el lado derecho y después asigna. Sin esta forma habría que usar una variable auxiliar:

```python
lista = ["x", "y"]
aux = lista[0]
lista[0] = lista[1]
lista[1] = aux
print(lista)      # ['y', 'x']
```

> [!warning] Intercambio a medias
> `lista[0] = lista[1]` seguido de `lista[1] = lista[0]` **no** intercambia: después de la primera línea el valor original de `lista[0]` ya se perdió, y ambas posiciones quedan iguales.

## ¿Qué tan rápido es?

Para una lista de `n` elementos, selection sort hace unas `n²/2` comparaciones: con 1000 elementos, cerca de medio millón. El `sort` de Python usa un algoritmo mucho más rápido. Por eso, en la práctica se usa `sort`, y selection sort se aprende para entender **cómo se piensa** un algoritmo. Otros métodos (insertion sort, mergesort, quicksort) y cómo medir su rapidez se ven en [[Estructuras de Datos/_Índice|Estructuras de Datos]].

## Preguntas de repaso

> [!question]- ¿Por qué el ciclo interno empieza en `ip + 1`?
> Porque las posiciones antes de `ip` ya están ordenadas, y `m` parte en `ip`: solo falta comparar con los elementos que vienen después.

> [!question]- ¿Qué pasaría si se olvida el `+ ip` en la versión con `index`?
> Se calcularía la posición del mínimo dentro del pedazo `lista[ip:]` y no en la lista completa, así que se intercambiaría el elemento equivocado.

> [!question]- ¿Por qué `lista[0] = lista[1]; lista[1] = lista[0]` no intercambia los valores?
> Porque la primera asignación sobrescribe `lista[0]` y su valor original se pierde; la segunda solo copia de vuelta el mismo valor.
