---
ramo: "Programación Avanzada"
tema: "Excepciones e iterables"
tags:
  - programacion/generadores
  - programacion/iterables
  - origen/complemento
prerrequisitos:
  - "[[04 - Protocolo de iteración: iterables, iteradores y StopIteration]]"
---

# Generadores y la palabra clave yield

Crear una lista de diez millones de elementos para recorrerla una sola vez en un bucle obliga al computador a reservar cientos de megabytes de memoria RAM de forma innecesaria. Cuando solo necesitamos un elemento a la vez, la estrategia adecuada es generarlo bajo demanda.

## El problema del almacenamiento en memoria

Una función convencional acumula todos los resultados antes de retornar la lista completa:

```python
def primeros_pares_lista(n: int) -> list:
    resultado = []
    for i in range(n):
        resultado.append(i * 2)
    return resultado  # Debe retener la lista entera en memoria
```

Si `n` es enorme, este enfoque agota la memoria del sistema.

## Qué es un generador y la palabra clave yield

Un **generador** es un iterador especial que produce valores de forma **perezosa** (*lazy evaluation*): calcula cada valor únicamente cuando se le solicita, ocupando una cantidad minúscula y constante de memoria sin importar el tamaño de la secuencia.

Una función se convierte en generadora cuando utiliza la palabra clave **`yield`** en lugar de `return`:

- **`return`:** finaliza la función por completo y destruye su estado local.
- **`yield`:** produce un valor hacia el exterior y **pausa la ejecución de la función**, congelando el valor de sus variables locales hasta que se le solicite el siguiente elemento.

```python
def primeros_pares_generador(n: int):
    for i in range(n):
        yield i * 2  # Pausa y entrega el valor


gen = primeros_pares_generador(3)
print(f"Tipo de objeto: {type(gen).__name__}")

print(next(gen))  # Reanuda hasta el primer yield: 0
print(next(gen))  # Reanuda hasta el segundo yield: 2
print(next(gen))  # Reanuda hasta el tercer yield: 4
# print(next(gen))  # La función termina: levanta StopIteration automáticamente
```

```
Tipo de objeto: generator
0
2
4
```

## Secuencias infinitas en memoria constante

Dado que los generadores no almacenan la secuencia completa en memoria, pueden modelar flujos de datos potencialmente infinitos sin riesgo de desbordar la memoria:

```python
def fibonacci():
    """Generador infinito de la sucesión de Fibonacci."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


serie = fibonacci()
primeros_seis = [next(serie) for _ in range(6)]
print(f"Primeros números de Fibonacci: {primeros_seis}")
```

```
Primeros números de Fibonacci: [0, 1, 1, 2, 3, 5]
```

## Expresiones generadoras (generator expressions)

De forma análoga a las listas por comprensión, Python permite crear generadores de manera concisa reemplazando los corchetes `[...]` por paréntesis `(...)`:

```python
# Lista por comprensión: crea y almacena los 1000 números inmediatamente
cuadrados_lista = [x ** 2 for x in range(1000)]

# Expresión generadora: no calcula nada hasta que se itere sobre ella
cuadrados_gen = (x ** 2 for x in range(1000))

print(f"Primer valor:  {next(cuadrados_gen)}")
print(f"Segundo valor: {next(cuadrados_gen)}")
```

```
Primer valor:  0
Segundo valor: 1
```

> [!tip] Ahorro de memoria con sum() y min()
> Funciones integradas como `sum()`, `max()` o `min()` aceptan generadores directamente sin corchetes: `sum(x for x in range(1000000))`. Esto calcula la suma acumulada ocupando prácticamente cero memoria adicional.

> [!warning] Los generadores no admiten indexación
> Como los elementos se producen al vuelo y no se almacenan, una expresión como `mi_generador[5]` genera un error de tipo `TypeError: 'generator' object is not subscriptable`. Para saltar elementos debes consumirlos con `next()` o `itertools.islice`.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia fundamental entre la instrucción `return` y la instrucción `yield`?
> `return` termina la ejecución de la función y destruye su marco de variables locales; `yield` produce un valor hacia el invocador y suspende la función en ese punto exacto, preservando su estado para la siguiente llamada.

> [!question]- ¿Qué significa el concepto de evaluación perezosa (lazy evaluation) en los generadores?
> Significa que los datos no se calculan ni se reservan en memoria por anticipado, sino que se procesan y generan uno a uno bajo demanda en el instante exacto en que el consumidor solicita el siguiente valor.

> [!question]- ¿Por qué un generador consume sustancialmente menos memoria que una lista equivalente?
> Porque la lista retiene todos sus elementos simultáneamente en la memoria RAM, mientras que el generador solo almacena el estado mínimo necesario para calcular el siguiente elemento inmediato.

> [!question]- ¿Qué ocurre cuando una función generadora llega al final de su cuerpo sin encontrar más sentencias `yield`?
> El intérprete de Python finaliza el generador y levanta automáticamente una excepción `StopIteration` para avisar al consumidor que la secuencia ha concluido.
