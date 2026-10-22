---
ramo: "Programación Avanzada"
tema: "Estructuras de datos de Python"
tags:
  - programacion/estructuras-de-datos
  - programacion/sets
  - origen/complemento
prerrequisitos:
  - "[[05 - Diccionarios: llave-valor, hashing y métodos]]"
---

# Sets: conjuntos únicos y pertenencia

Al gestionar listas de usuarios registrados, inventarios o etiquetas, es común necesitar garantizar que ningún elemento aparezca repetido y poder verificar si un elemento específico ya existe en el sistema sin recorrer toda la colección de principio a fin.

## Qué es un Set

Un **conjunto** o **set** (`set`) es una estructura de datos no secuencial, mutable y no ordenada que almacena únicamente **elementos únicos** (sin duplicados).

Se comporta de forma análoga a los conjuntos de las matemáticas. Al igual que los diccionarios, los conjuntos están implementados internamente con una **tabla hash**, lo que permite verificar si un elemento pertenece al conjunto en **tiempo constante promedio $O(1)$**.

```python
# Creación de conjuntos
conjunto_vacio = set()  # {} crearía un diccionario vacío
artistas = {"Sting", "Mon Laferte", "Sting", "Taylor Swift"}

# Los duplicados se descartan automáticamente
print(f"Conjunto: {artistas}")
print(f"Total únicos: {len(artistas)}")
```

```
Conjunto: {'Mon Laferte', 'Taylor Swift', 'Sting'}
Total únicos: 3
```

> [!warning] Las llaves vacías crean un dict, no un set
> Escribir `x = {}` crea siempre un diccionario vacío (`dict`). Para crear un conjunto vacío es imprescindible usar el constructor funcional **`x = set()`**.

## Elementos permitidos y falta de orden

Dado que un conjunto opera como una tabla hash sin valores asociados (solo llaves), comparte las mismas reglas de los diccionarios:

1. **Solo admite elementos hasheables:** sus elementos deben ser inmutables (enteros, flotantes, strings, booleanos y tuplas inmutables). No permite listas ni diccionarios.
2. **No soporta indexación:** los elementos no tienen una posición fija. Escribir `artistas[0]` genera un error de tipo `TypeError: 'set' object is not subscriptable`.
3. **El conjunto es mutable:** se le pueden añadir y quitar elementos, pero por esa misma razón un conjunto **no puede contener a otros conjuntos**.

## Operaciones de modificación: add, remove y discard

```python
colores = {"azul", "rojo"}

# Agregar elementos con add
colores.add("verde")
colores.add("azul")  # No tiene efecto, ya existía
print(f"Tras add: {colores}")

# Eliminar con remove (falla si el elemento no existe)
colores.remove("rojo")
# colores.remove("amarillo")  # KeyError: 'amarillo'

# Eliminar seguro con discard (no falla si no existe)
colores.discard("amarillo")  # Se ejecuta sin errores
print(f"Tras eliminar: {colores}")
```

```
Tras add: {'rojo', 'verde', 'azul'}
Tras eliminar: {'verde', 'azul'}
```

> [!tip] Preferir discard frente a remove cuando la existencia es incierta
> Usa **`remove()`** cuando la ausencia del elemento deba ser tratada como una anomalía en tu lógica, y **`discard()`** cuando quieras asegurar que un elemento no esté en el conjunto sin necesidad de capturar un `KeyError`.

## Verificación de pertenencia y deduplicación

Verificar si un elemento existe en una lista con `x in lista` toma tiempo lineal $O(N)$ porque recorre elemento por elemento. En cambio, en un conjunto `x in conjunto` toma tiempo constante $O(1)$ mediante cálculo hash.

Además, los conjuntos permiten eliminar duplicados de cualquier lista de forma inmediata:

```python
numeros_repetidos = [1, 2, 2, 3, 4, 4, 4, 5, 1]
sin_duplicados = list(set(numeros_repetidos))
sin_duplicados.sort()

print(f"Lista deduplicada: {sin_duplicados}")
```

```
Lista deduplicada: [1, 2, 3, 4, 5]
```

## Preguntas de repaso

> [!question]- ¿Por qué la instrucción `s = {}` no crea un conjunto vacío en Python?
> Porque en la sintaxis histórica de Python las llaves literales vacías `{}` fueron asignadas exclusivamente a la creación de diccionarios (`dict`). Para crear un conjunto vacío se debe invocar la función constructora `set()`.

> [!question]- ¿Cuál es la diferencia fundamental entre los métodos `remove()` y `discard()` de un conjunto?
> `remove(x)` levanta una excepción `KeyError` si el elemento `x` no se encuentra en el conjunto, mientras que `discard(x)` ignora la ausencia y finaliza exitosamente sin levantar ninguna excepción.

> [!question]- ¿Por qué un conjunto no puede contener una lista o a otro conjunto común en su interior?
> Porque las listas y los conjuntos son objetos mutables, por lo que carecen de un valor hash inmutable. Los conjuntos requieren que todos sus elementos sean estrictamente hasheables para ubicarlos en su tabla hash interna.

> [!question]- ¿Qué desventaja tiene utilizar `list(set(lista_original))` para eliminar duplicados si el orden importa?
> Los conjuntos no preservan el orden original de inserción de los elementos, por lo que transformar una lista a conjunto y de regreso a lista alterará el orden original de la secuencia.
