---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/repaso-python
  - origen/complemento
prerrequisitos: []
---

# Repaso de Python: tipos, funciones y módulos

Este ramo da por sabido lo básico de Python. Esta nota es un repaso rápido de lo mínimo que se usa en todas las clases siguientes: tipos de datos, funciones (propias y de módulos) y valores por defecto. Si algo te suena nuevo, conviene practicarlo antes de seguir.

## Los tipos de datos básicos

Cada valor en Python tiene un **tipo**, y el tipo decide qué operaciones se pueden hacer con él.

| Tipo | Qué guarda | Ejemplo |
|---|---|---|
| `int` | Números enteros | `x = 10` |
| `float` | Números con decimales | `precio = 5.5` |
| `str` | Texto (cadena de caracteres) | `s = 'Bienvenidos a IIC2233'` |
| `bool` | Verdadero o falso | `a = True` |
| `list` | Colección ordenada y modificable | `lista = [10, 'variable', True, 5.5]` |

```python
x = 10
y = 20
print(x + y)            # 30

a = True
b = 3 > 4               # una comparación entrega un bool
print(a == b)           # False

lista = [10, 'variable', True, 5.5]
print(lista[0])         # 10
```

```
30
False
10
```

Una comparación como `1 >= 0` entrega `True`, y `10 == 5` entrega `False`. Fíjate en que `==` **compara** y `=` **asigna**.

> [!tip] Listas y strings tienen su propia nota
> Las listas se profundizan en [[02 - Listas: creación y comprensión|Listas]] y [[03 - Listas: slicing y orden|slicing]] y los strings en [[04 - Strings: inmutabilidad, escapes y métodos|Strings]].

## Funciones: encapsular una tarea

Una **función** agrupa código que resuelve una tarea concreta, para poder reutilizarlo con un nombre. Hay tres orígenes posibles:

1. **Funciones *built-in*:** vienen con Python y siempre están disponibles (`print`, `len`, `type`…).
2. **Funciones de módulos:** hay que importarlas primero.
3. **Funciones propias:** las defines tú con `def`.

### Importar de un módulo

Un **módulo** es un archivo con funciones ya hechas. Hay tres formas de usarlo:

```python
import math                       # módulo completo
print(math.sqrt(16))

from math import sqrt, pi         # solo lo que se necesita
print(sqrt(25), pi)

import math as m                  # con un alias (otro nombre)
print(m.floor(3.7))
```

```
4.0
5.0 3.141592653589793
3
```

### Definir una función propia

Se usa `def`, se listan los parámetros y, si hay un resultado, se entrega con `return`. Apenas se ejecuta un `return`, la función termina.

```python
def sumar(numero1, numero2):
    """Retorna la suma de dos números enteros."""
    suma = numero1 + numero2
    return suma

resultado = sumar(10, 20)
print(resultado)
```

```
30
```

Las funciones pueden recibir 0 o más parámetros y devolver 0 o más valores; lo habitual es devolver uno. El texto entre triples comillas (el *docstring*) explica qué hace la función.

### Valores por defecto

Un parámetro puede traer un valor por defecto: se usa si quien llama a la función no entrega ese dato.

```python
def sumar(n1=0, n2=0):
    return n1 + n2

print(sumar())          # usa los dos por defecto
print(sumar(10))        # n2 usa el valor por defecto
print(sumar(10, 13))    # no usa ninguno
```

```
0
10
23
```

> [!warning] Sin `return`, la función entrega `None`
> Si una función solo hace `print` del resultado, no lo devuelve. Para usarlo en otro cálculo hace falta `return`.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre `import math` y `from math import sqrt`?
> Con `import math` se trae todo el módulo y se usa con el prefijo (`math.sqrt(4)`). Con `from math import sqrt` se trae solo esa función y se usa sin prefijo (`sqrt(4)`).

> [!question]- ¿Qué pasa si llamas a `sumar(10)` cuando solo `n1` tiene valor por defecto?
> Falla con un error por falta del argumento `n2`: un parámetro sin valor por defecto es obligatorio.

> [!question]- ¿Por qué `a = True` y `b = 3 > 4` hacen que `a == b` sea `False`?
> Porque `3 > 4` es falso, entonces `b` vale `False`, y `True == False` es falso.
