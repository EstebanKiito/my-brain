---
ramo: "Programación Avanzada"
tema: "POO avanzada"
tags:
  - programacion/poo
  - programacion/metodos-magicos
  - origen/complemento
prerrequisitos:
  - "[[03 - Polimorfismo y duck typing]]"
---

# Sobrecarga de operadores y métodos dunder

Al crear clases personalizadas que representan conceptos matemáticos, geométricos o de dominio —como vectores, fracciones o carritos de compra—, escribir `v1.sumar(v2)` resulta poco natural. Queremos poder escribir directamente `v1 + v2` o verificar igualdad con `v1 == v2`.

## Qué es la sobrecarga de operadores

La **sobrecarga de operadores** (*operator overloading*) permite redefinir el comportamiento de los operadores integrados de Python (`+`, `-`, `*`, `==`, `<`, entre otros) para que interactúen de forma idiomática con nuestras clases personalizadas.

Python logra esto mediante **métodos especiales** o **dunder** (*double underscore*, porque empiezan y terminan con doble guion bajo). Cuando se evalúa una expresión como `a + b`, Python la traduce internamente a `a.__add__(b)`.

```python
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Sobrecarga del operador + (a + b)
    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    # Sobrecarga del operador == (a == b)
    def __eq__(self, otro):
        if not isinstance(otro, Vector2D):
            return False
        return self.x == otro.x and self.y == otro.y

    # Representación amigable para print() y str()
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Representación técnica y unívoca para depuración
    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
v3 = v1 + v2

print(f"Suma con +: {v3}")
print(f"¿Son iguales?: {v3 == Vector2D(4, 6)}")
```

```
Suma con +: (4, 6)
¿Son iguales?: True
```

## Métodos dunder más comunes

| Categoría | Operador | Método dunder asociado |
|---|---|---|
| **Aritmética** | `+`, `-`, `*`, `/` | `__add__`, `__sub__`, `__mul__`, `__truediv__` |
| **Comparación** | `==`, `!=` | `__eq__`, `__ne__` |
| **Orden** | `<`, `<=`, `>`, `>=` | `__lt__`, `__le__`, `__gt__`, `__ge__` |
| **Colecciones** | `len(obj)`, `obj[i]` | `__len__`, `__getitem__` |

Al implementar `__lt__` (menor que), las instancias de nuestra clase se pueden ordenar automáticamente con `lista.sort()` o la función `sorted()`.

## Diferencia entre __str__ y __repr__

Ambos métodos retornan una cadena que describe al objeto, pero cumplen propósitos distintos:

- **`__str__`:** pensado para el **usuario final**. Produce un texto limpio, legible y amigable. Es el método que invoca `print(obj)` o `str(obj)`.
- **`__repr__`:** pensado para el **programador**. Debe ser un texto técnico, preciso y sin ambigüedades, idealmente una cadena que al pegarla en el intérprete reconstruya el objeto. Es el método invocado en la consola interactiva o por `repr(obj)`.

```python
from datetime import date

hoy = date(2026, 10, 22)

print(f"Salida de str:  {str(hoy)}")
print(f"Salida de repr: {repr(hoy)}")
```

```
Salida de str:  2026-10-22
Salida de repr: datetime.date(2026, 10, 22)
```

> [!tip] La regla del respaldo de __repr__
> Si una clase define `__repr__` pero no implementa `__str__`, Python utiliza automáticamente `__repr__` como respaldo ante llamadas a `print()`. Por esta razón, se recomienda implementar siempre al menos `__repr__` en cualquier clase.

> [!warning] Comprobar el tipo en comparaciones
> En el método `__eq__(self, otro)` siempre debes validar si `otro` es una instancia compatible. Si intentas comparar un `Vector2D` con un entero `v == 5` sin comprobar el tipo, acceder a `otro.x` provocará una excepción `AttributeError`.

## Preguntas de repaso

> [!question]- ¿Qué ocurre a nivel interno cuando el intérprete de Python evalúa la expresión `obj1 + obj2`?
> Python busca el método `__add__` en la clase de `obj1` y ejecuta la llamada equivalente `obj1.__add__(obj2)`.

> [!question]- ¿Cuál es la principal diferencia de público objetivo entre `__str__` y `__repr__`?
> `__str__` está orientado al usuario final para presentar información legible, mientras que `__repr__` está orientado al programador para depuración, debiendo ser explícito y sin ambigüedades.

> [!question]- ¿Por qué implementar el método `__lt__` permite ordenar una lista de objetos personalizados con `sorted()`?
> Porque los algoritmos de ordenamiento de Python (Timsort) comparan elementos mediante el operador menor que (`<`); al definir `__lt__`, Python puede comparar cualquier par de objetos de esa clase.

> [!question]- ¿Qué método dunder debe implementarse para que una clase responda a la función `len(mi_objeto)`?
> Se debe implementar el método `__len__(self)`, el cual debe retornar obligatoriamente un número entero mayor o igual a cero.
