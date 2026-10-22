---
ramo: "Programación Avanzada"
tema: "Programación funcional"
tags:
  - programacion/funcional
  - programacion/funciones
  - origen/complemento
prerrequisitos:
  - "[[03 - Funciones de orden superior: map, filter y reduce]]"
---

# Funciones anónimas lambda, zip y enumerate

En muchas situaciones prácticas necesitamos una función simple de una sola línea —por ejemplo, para ordenar una lista por el segundo campo de una tupla o para calcular una fórmula breve en un `map`— donde declarar formalmente una función con `def` añade ruido visual innecesario.

## Funciones anónimas: la expresión lambda

Una **función lambda** es una función pequeña, anónima (sin nombre identificador obligatorio) definida en una sola línea mediante la palabra clave **`lambda`**:

```python
# Sintaxis: lambda argumentos: expresion
cuadrado = lambda x: x ** 2
sumar = lambda a, b: a + b

print(cuadrado(5))
print(sumar(3, 7))
```

```
25
10
```

### Características y limitaciones de lambda

- **Una única expresión:** el cuerpo de una función lambda solo puede contener una única expresión evaluable; no puede contener múltiples sentencias, bucles `while`, bloques `try-except` ni declaraciones complejas.
- **Retorno implícito:** el resultado de la expresión evaluada se retorna de forma automática sin escribir la palabra `return`.
- **Uso ideal:** se utilizan como argumentos temporales pasados directamente a funciones de orden superior (`map`, `filter`) o como clave de ordenamiento en `sorted()`:

```python
estudiantes = [("Carla", 22), ("Andrés", 19), ("Beatriz", 25)]

# Ordenar por edad (segundo elemento de la tupla)
estudiantes_por_edad = sorted(estudiantes, key=lambda alumno: alumno[1])
print(f"Ordenados por edad: {estudiantes_por_edad}")
```

```
Ordenados por edad: [('Andrés', 19), ('Carla', 22), ('Beatriz', 25)]
```

> [!warning] Cuándo evitar lambda según PEP8
> Si necesitas asignar una lambda a una variable (`mi_func = lambda x: ...`), la guía oficial de estilo PEP8 recomienda definirla siempre como una función convencional con `def mi_func(x):`. Reserva `lambda` únicamente para funciones anónimas pasadas directamente como argumento dentro de otra expresión.

## La función zip() y el desempaquetado de secuencias

La función integrada **`zip(*iterables)`** toma dos o más colecciones y empareja sus elementos correspondientes en una secuencia de **tuplas**:

```python
nombres = ["Ana", "Pedro", "Clara"]
edades = [20, 22, 21]
carreras = ["Computación", "Civil", "Medicina"]

# Empareja elementos paralelos en tuplas
estudiantes_completos = list(zip(nombres, edades, carreras))
print(estudiantes_completos)
```

```
[('Ana', 20, 'Computación'), ('Pedro', 22, 'Civil'), ('Clara', 21, 'Medicina')]
```

- **Truncamiento:** si los iterables tienen longitudes distintas, `zip` se detiene en cuanto se agota el iterable más corto (para iterar hasta el más largo rellenando con un valor por defecto se utiliza `itertools.zip_longest`).
- **Inversa de sí misma:** el operador `*` permite desempaquetar una lista de tuplas para separar nuevamente las columnas originales con `zip(*pares)`:

```python
pares = [(1, "A"), (2, "B"), (3, "C")]
numeros, letras = zip(*pares)
print(f"Números: {numeros}")
print(f"Letras:  {letras}")
```

```
Números: (1, 2, 3)
Letras:  ('A', 'B', 'C')
```

## Enumeración idiomática con enumerate()

Para recorrer una colección obteniendo simultáneamente el **índice** numérico de cada posición y su **valor**, la herramienta idiomática es **`enumerate(iterable, start=0)`**:

```python
cursos = ["IIC1103", "IIC2233", "MAT1610"]

# start define el número inicial del contador
for posicion, sigla in enumerate(cursos, start=1):
    print(f"Prioridad {posicion}: {sigla}")
```

```
Prioridad 1: IIC1103
Prioridad 2: IIC2233
Prioridad 3: MAT1610
```

> [!tip] Evita range(len(...))
> El patrón `for i in range(len(lista)):` es una práctica heredada de C que resulta redundante en Python. Usa siempre `for i, item in enumerate(lista):`.

## Preguntas de repaso

> [!question]- ¿Qué limitación sintáctica principal tienen las funciones anónimas lambda frente a las funciones definidas con `def`?
> Solo pueden contener una única expresión que se evalúa y retorna automáticamente; no admiten sentencias múltiples, asignaciones dentro de su cuerpo ni bloques de control como `try-except`.

> [!question]- ¿Qué ocurre cuando se aplica `zip()` sobre dos listas que tienen diferente longitud?
> La iteración finaliza automáticamente tan pronto como se agotan los elementos de la lista más corta, descartando los elementos sobrantes de la lista más larga.

> [!question]- ¿Cómo se utiliza `zip(*matriz)` para trasponer una matriz de listas anidadas?
> El operador asterisco `*` desempaqueta las filas de la matriz como argumentos separados para `zip()`, lo que agrupa los elementos en la misma columna creando las filas transpuestas.

> [!question]- ¿Qué ventaja ofrece `enumerate(lista, start=1)` frente a declarar una variable manual `i = 1` y hacer `i += 1` en cada vuelta?
> Es más limpio, evita errores humanos de actualización u omisión del contador y mantiene el código alineado con los estándares idiomáticos de Python.
