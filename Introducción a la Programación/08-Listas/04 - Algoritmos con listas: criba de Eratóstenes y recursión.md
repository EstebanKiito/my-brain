---
ramo: "Introducción a la Programación"
tema: "Listas"
tags:
  - programacion/listas
  - origen/complemento
prerrequisitos:
  - "[[03 - Mutabilidad y listas como parámetro]]"
  - "[[01 - Caso base y caso recursivo]]"
---

# Algoritmos con listas: criba de Eratóstenes y recursión

Con listas se pueden programar algoritmos que antes eran imposibles, porque necesitan **recordar muchos valores a la vez**. Esta nota muestra un algoritmo clásico, la criba de Eratóstenes, y cómo se aplica la recursión a listas.

## La criba de Eratóstenes

Para encontrar todos los números primos hasta `n`, en vez de revisar cada número por separado (como `es_primo`), se usa un método de hace más de 2000 años:

1. Escribir todos los números del 2 al `n` (la **criba**, o colador).
2. El menor número que queda es primo. Anotarlo.
3. Tachar ese número y todos sus múltiplos.
4. Repetir desde el paso 2 hasta que la criba quede vacía.

Ejemplo hasta 10: la criba es 2…10. El 2 es primo y se tachan 2, 4, 6, 8, 10. Queda 3, 5, 7, 9: el 3 es primo y se tachan 3 y 9. Quedan 5 y 7, que también son primos.

```python
n = 40
primos = []
criba = list(range(2, n + 1))
while criba != []:
    m = min(criba)                  # el menor que queda es primo
    primos.append(m)
    for multiplo in range(m, n + 1, m):
        if multiplo in criba:
            criba.remove(multiplo)  # tachar m y sus múltiplos
print(primos)
```

```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
```

`range(m, n + 1, m)` genera justamente los múltiplos de `m` (m, 2m, 3m…), gracias al paso. Aquí sí se borra de `criba` sin problema, porque el ciclo recorre `range`, no la criba.

> [!tip] Por qué funciona
> Un número que no fue tachado no es múltiplo de ningún número menor, así que solo es divisible por 1 y por sí mismo: es primo.

## Recursión sobre listas

Una lista se puede pensar recursivamente: es **vacía**, o es **un primer elemento seguido del resto** (`l[0]` y `l[1:]`). Eso da caso base y caso recursivo casi automáticamente.

```python
def largo(lista):
    if lista == []:                 # caso base: la lista vacía mide 0
        return 0
    return 1 + largo(lista[1:])     # el primero, más el largo del resto

def suma(lista):
    if lista == []:
        return 0
    return lista[0] + suma(lista[1:])

print(largo([1, 2, 3, 4, 6, 7]), suma([1, 2, 3, 4, 6, 7]))
```

```
6 23
```

Cada llamada trabaja con una lista un elemento más corta, así que tarde o temprano se llega a la lista vacía.

## Ejemplo: el máximo de forma recursiva

El máximo de una lista es el mayor entre el primer elemento y el máximo del resto. El caso base es una lista de un solo elemento:

```python
def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    resto = maximo(lista[1:])
    if lista[0] > resto:
        return lista[0]
    return resto

print(maximo([4, 17, 3, 9]))   # 17
```

> [!warning] Caso base de las listas vacías
> `maximo([])` no tiene sentido (no hay elementos) y fallaría con `IndexError`. Al pensar el caso base hay que preguntarse cuál es la lista más chica para la que el problema tiene respuesta.

## Preguntas de repaso

> [!question]- En la criba hasta 30, ¿por qué el 25 nunca llega a ser el mínimo de la criba?
> Porque al procesar el 5 se tachan sus múltiplos, y el 25 es uno de ellos. Solo sobreviven números sin divisores menores.

> [!question]- ¿Qué es `lista[1:]` y por qué sirve para la recursión?
> Es la lista sin su primer elemento. Es un problema del mismo tipo pero más pequeño, que se acerca al caso base (la lista vacía).

> [!question]- ¿Cuál es el caso base de `suma(lista)` y por qué retorna 0?
> La lista vacía. Retorna 0 porque sumar ningún número da 0, y así no altera la suma de los demás.
