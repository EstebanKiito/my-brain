---
ramo: "Programación Avanzada"
tema: "Tópicos avanzados"
tags:
  - programacion/numpy
  - programacion/ciencia-de-datos
  - origen/complemento
prerrequisitos:
  - "[[02 - Listas: creación y comprensión]]"
  - "[[03 - Listas: slicing y orden]]"
---

# Computación numérica con NumPy ndarrays vectorización y broadcasting

Las listas estándar de Python son colecciones dinámicas de punteros dispersos en memoria donde cada elemento es un objeto completo con su propia sobrecarga de metadatos. Al procesar millones de valores numéricos en simulaciones científicas, gráficos o inteligencia artificial, iterar sobre listas mediante bucles `for` resulta órdenes de magnitud más lento que en lenguajes compilados. **NumPy** resuelve esta limitación introduciendo arreglos multidimensionales homogéneos y vectorización.

## El arreglo multidimensional: ndarray

El componente nuclear de NumPy es el objeto **`ndarray`** (*N-dimensional array*):

- **Memoria contigua en C:** todos los datos residen en un bloque secuencial contiguo de bytes en memoria RAM, permitiendo al procesador transferir datos masivos a la memoria caché y aplicar instrucciones vectoriales (SIMD).
- **Tipado homogéneo (`dtype`):** todos los elementos deben pertenecer al mismo tipo de dato exacto (ejemplo `float64`, `int32`), eliminando la verificación dinámica de tipos en cada operación.

### Creación y atributos esenciales

```python
import numpy as np

# Creación desde listas
vector = np.array([10, 20, 30, 40], dtype=np.int32)
matriz = np.zeros((3, 4))  # Matriz de 3 filas y 4 columnas llena de ceros
secuencia = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
espaciado = np.linspace(0, 1, 5)  # 5 puntos equidistantes entre 0 y 1

print(f"Dimensiones (shape): {matriz.shape}")  # (3, 4)
print(f"Tipo de datos (dtype): {vector.dtype}")   # int32
print(f"Número de dimensiones: {matriz.ndim}")    # 2
```

## Operaciones vectorizadas elemento a elemento

En NumPy las operaciones aritméticas estándar no requieren bucles explícitos: se aplican de forma instantánea a nivel de hardware sobre cada elemento (*element-wise*):

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Operaciones vectorizadas directas
suma = a + b        # [11, 22, 33]
producto = a * b    # [10, 40, 90]
potencia = a ** 2   # [1, 4, 9]
```

## Broadcasting: operando dimensiones desiguales

El mecanismo de **broadcasting** permite a NumPy operar arreglos con diferentes dimensiones o formas sin duplicar datos en memoria:

```python
import numpy as np

matriz = np.ones((3, 3))  # Matriz 3x3 de unos
fila = np.array([1, 2, 3])  # Vector 1D de 3 elementos

# Broadcasting: el vector fila se 'estira' virtualmente sobre cada una de las 3 filas
resultado = matriz + fila
```

**Regla de compatibilidad de broadcasting:** dos dimensiones son compatibles si son **iguales** o si **una de ellas es 1**.

## Indexación booleana y estadísticas por ejes (Axes)

```python
import numpy as np

datos = np.array([15, 28, 42, 9, 31, 55])

# Máscara booleana: filtra elementos sin usar bucles for ni if
mayores_a_30 = datos[datos > 30]  # array([42, 31, 55])

# Reducción estadística a lo largo de ejes en una matriz
tabla = np.array([[10, 20], [30, 40]])
media_columnas = tabla.mean(axis=0)  # [20., 30.] (colapsa filas)
media_filas = tabla.mean(axis=1)     # [15., 35.] (colapsa columnas)
```

> [!tip] Prefiere funciones universales (ufuncs)
> Para aplicar funciones matemáticas sobre un array (raíz cuadrada, funciones trigonométricas, exponenciales), usa siempre las funciones de NumPy como `np.sqrt(arr)` o `np.exp(arr)` en lugar de funciones de la librería `math` estándar, ya que están vectorizadas en C.

## Preguntas de repaso

> [!question]- ¿Por qué un cálculo numérico sobre un `ndarray` de NumPy es mucho más rápido que sobre una lista de Python con un bucle `for`?
> Porque el `ndarray` almacena los datos de forma homogénea en un bloque de memoria contiguo en C, ejecutando las operaciones a nivel de código compilado sin la sobrecarga de interpretación de Python.

> [!question]- ¿Qué regla de compatibilidad debe cumplirse para que dos arreglos puedan operarse mediante *broadcasting*?
> Al comparar las dimensiones desde la derecha hacia la izquierda, cada par de dimensiones debe ser igual o una de ellas debe ser de longitud 1.

> [!question]- ¿Qué retorna la operación `datos > 10` sobre un arreglo de NumPy?
> Retorna un nuevo arreglo booleano de la misma dimensión (*forma*), donde cada posición contiene `True` o `False` según si el elemento respectivo cumple la condición.

> [!question]- ¿Cuál es la diferencia entre calcular la media con `axis=0` versus `axis=1` en una matriz 2D?
> `axis=0` opera verticalmente calculando la media de cada columna (colapsando las filas), mientras que `axis=1` opera horizontalmente calculando la media de cada fila (colapsando las columnas).
