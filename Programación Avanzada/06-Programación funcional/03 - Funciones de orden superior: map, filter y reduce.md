---
ramo: "Programación Avanzada"
tema: "Programación funcional"
tags:
  - programacion/funcional
  - programacion/funciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Paradigma funcional y funciones puras]]"
  - "[[04 - Protocolo de iteración: iterables, iteradores y StopIteration]]"
---

# Funciones de orden superior: map, filter y reduce

En el paradigma funcional, el procesamiento de colecciones no se realiza mediante bucles `for` que van modificando variables acumuladoras, sino aplicando transformaciones declarativas sobre secuencias de datos a través de funciones especializadas.

## Funciones de orden superior

Una **función de orden superior** (*higher-order function*) es aquella que cumple al menos una de dos condiciones:

1. Recibe una o más funciones como argumento.
2. Retorna una función como resultado.

En Python, las tres funciones de orden superior más representativas del paradigma son **`map`**, **`filter`** y **`reduce`**.

## 1. Transformación con map()

La función integrada **`map(funcion, iterable)`** aplica una función transformadora sobre cada elemento de una colección:

![Operación de mapeo con map](adjuntos/Operaci%C3%B3n%20de%20mapeo%20con%20map.png)

> [!example]- Transcripción de la imagen
> - Diagrama conceptual de `map`:
>   - Arriba: colección de entrada con elementos independientes.
>   - Centro: una función `f(x)` aplicada uno a uno sobre cada celda.
>   - Abajo: colección resultante con los valores transformados conservando la misma longitud.

```python
def convertir_celsius_a_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

temperaturas_c = [0.0, 20.0, 37.0, 100.0]

# map retorna un iterador perezoso (map object)
iter_fahrenheit = map(convertir_celsius_a_fahrenheit, temperaturas_c)
print(f"Tipo retornado: {type(iter_fahrenheit).__name__}")
print(f"Temperaturas °F: {list(iter_fahrenheit)}")
```

```
Tipo retornado: map
Temperaturas °F: [32.0, 68.0, 98.6, 212.0]
```

`map()` puede recibir múltiples iterables simultáneamente; en ese caso, la función debe aceptar tantos argumentos como iterables se entreguen:

```python
a = [1, 2, 3]
b = [10, 20, 30]
sumas = list(map(lambda x, y: x + y, a, b))
print(f"Suma paralela: {sumas}")
```

```
Suma paralela: [11, 22, 33]
```

## 2. Filtrado con filter()

La función integrada **`filter(predicado, iterable)`** evalúa cada elemento con una función que retorna un booleano (`True` o `False`), conservando únicamente aquellos elementos que satisfacen la condición:

```python
def es_aprobado(nota: float) -> bool:
    return nota >= 4.0

calificaciones = [3.2, 5.5, 6.8, 3.9, 4.0, 2.5]
aprobados = list(filter(es_aprobado, calificaciones))
print(f"Notas aprobadas: {aprobados}")
```

```
Notas aprobadas: [5.5, 6.8, 4.0]
```

Al igual que `map`, `filter` retorna un iterador perezoso que no procesa los datos hasta que son consumidos.

## 3. Plegado y agregación con reduce()

Mientras que `map` y `filter` producen colecciones, **`reduce`** pliega una secuencia entera hasta condensarla en un **único valor escalar** aplicando una función binaria acumulativa de izquierda a derecha.

En Python 3, `reduce` reside dentro del módulo estándar **`functools`**:

![Operación de reducción acumulada con reduce](adjuntos/Operaci%C3%B3n%20de%20reducci%C3%B3n%20acumulada%20con%20reduce.png)

> [!example]- Transcripción de la imagen
> - Diagrama en árbol de `reduce`:
>   - Los primeros dos elementos se combinan mediante una función binaria.
>   - El resultado acumulado se combina con el tercer elemento.
>   - El proceso se repite en cascada hasta condensar toda la lista en un único valor de salida.

```python
from functools import reduce

def multiplicar(acumulado: int, elemento: int) -> int:
    return acumulado * elemento

factores = [1, 2, 3, 4, 5]

# 1 * 2 * 3 * 4 * 5 = 120
producto = reduce(multiplicar, factores)
print(f"Factorial acumulado con reduce: {producto}")
```

```
Factorial acumulado con reduce: 120
```

> [!tip] Evaluación perezosa de map y filter
> Dado que `map` y `filter` retornan iteradores y no listas, encadenar `filter` y `map` no genera listas intermedias en memoria: los datos se filtran y transforman elemento por elemento bajo demanda.

> [!warning] El valor inicial en reduce
> Si la lista entregada a `reduce` está vacía y no se especificó un valor inicial (`reduce(f, [], 0)`), Python levanta una excepción `TypeError: reduce() of empty iterable with no initial value`. Siempre es prudente proveer el tercer argumento `inicial` cuando la colección pueda estar vacía.

## Preguntas de repaso

> [!question]- ¿Qué define conceptualmente a una función de orden superior?
> Es una función que acepta otras funciones como parámetros o retorna una función como su resultado, tratando las operaciones como valores de primera clase.

> [!question]- ¿Por qué `map(funcion, coleccion)` no devuelve una lista inmediatamente en Python 3?
> Porque retorna un iterador perezoso que evalúa cada elemento bajo demanda solo cuando se le solicita, evitando crear y almacenar colecciones completas en la memoria RAM.

> [!question]- ¿Cuál es la diferencia de comportamiento entre `map()` y `filter()`?
> `map()` transforma cada elemento aplicando una función y produce una secuencia con la misma cantidad de elementos que el original; `filter()` aplica una condición lógica y produce una secuencia con un subconjunto de los elementos originales.

> [!question]- ¿Qué ocurre en `reduce(f, [10, 20, 30])` si no se entrega un valor inicial?
> Python toma los dos primeros elementos (`10` y `20`) como argumentos para la primera llamada de `f`, y utiliza el resultado para combinarlo con el tercer elemento (`30`).
