---
ramo: "Introducción a la Programación"
tema: "Funciones y módulos"
tags:
  - programacion/funciones
  - origen/complemento
prerrequisitos:
  - "[[03 - Return versus print y funciones booleanas]]"
---

# Módulos propios e import

Cuando un programa crece, tener todas las funciones en un solo archivo lo vuelve largo y difícil de navegar. Además, una función útil (como `primos_relativos`) podría servir en otros programas. La solución es guardarla en un archivo aparte, un **módulo**, e **importarlo** donde se necesite, igual que `math` o `random`.

## Un módulo es un archivo `.py`

Cualquier archivo de Python es un módulo. Si se guarda esto en `util.py`:

```text
# util.py
def primos_relativos(x, y):
    for d in range(2, min(x, y) + 1):
        if x % d == 0 and y % d == 0:
            return False
    return True

def suma(x, y):
    return x + y
```

otro archivo **en la misma carpeta** puede usar sus funciones:

```text
# programa.py
import util

print(util.primos_relativos(5, 7))   # True
print(util.suma(5, 7))               # 12
```

## Formas de importar

| Forma | Cómo se llama la función | Cuándo conviene |
|---|---|---|
| `import util` | `util.primos_relativos(5, 7)` | La más clara: se ve de dónde viene cada función |
| `import util as u` | `u.primos_relativos(5, 7)` | Si el nombre del módulo es largo |
| `from util import primos_relativos` | `primos_relativos(5, 7)` | Si solo se usan una o dos funciones |
| `from util import *` | `primos_relativos(5, 7)`, `suma(5, 7)` | Trae todo; cómodo, pero puede chocar con nombres propios |

Lo mismo vale para los módulos de Python: `from math import sqrt` permite escribir `sqrt(9)` en vez de `math.sqrt(9)`.

```python
from math import sqrt, pi
import random as r

print(sqrt(9), round(pi, 2))
print(1 <= r.randint(1, 6) <= 6)
```

```
3.0 3.14
True
```

> [!warning] Choque de nombres con `import *`
> Si el módulo tiene una función `suma` y el programa también define una variable `suma`, una tapa a la otra. Con `import util` no pasa, porque la función se llama `util.suma`.

## Funciones escritas por otros

En los ejercicios del curso es común recibir un módulo ya hecho (por ejemplo, uno que entrega datos de una red de amigos o del recorrido de una lagartija) y tener que usar sus funciones **sin saber cómo están programadas por dentro**. Basta con conocer qué parámetros reciben y qué retornan. Así funciona la programación en equipo: cada persona usa las funciones de las demás confiando en lo que prometen hacer.

Un patrón típico: pedir datos al módulo uno por uno hasta que se acaben.

```text
import amigos

nombre = input()
i = 1
amigo = amigos.obtener_amigo(nombre, i)
while amigo != "":
    if amigos.estudia(amigo) == amigos.estudia(nombre):
        print(amigo)
    i += 1
    amigo = amigos.obtener_amigo(nombre, i)
```

## El bloque `if __name__ == "__main__":`

Al importar un módulo, Python **ejecuta todo su código**. Si `util.py` tuviera pruebas sueltas al final (`print(suma(2, 3))`), aparecerían al importarlo. Para evitarlo, el código de prueba se pone dentro de:

```python
def suma(x, y):
    return x + y

if __name__ == "__main__":
    print(suma(2, 3))   # solo corre al ejecutar este archivo directamente
```

Algunos editores, como PyCharm, crean este bloque automáticamente en los archivos nuevos.

> [!tip] Idea clave
> Un módulo es solo un archivo `.py` con funciones. `import nombre` (sin el `.py`) lo carga, y sus funciones se usan como `nombre.funcion(...)`. El archivo debe estar en la misma carpeta que el programa.

## Preguntas de repaso

> [!question]- ¿Qué ventaja tiene `import util` sobre `from util import *`?
> Deja claro de dónde viene cada función y evita que los nombres del módulo choquen con variables o funciones del programa.

> [!question]- ¿Qué pasa si `util.py` está en otra carpeta que el programa?
> Python no lo encuentra y `import util` da `ModuleNotFoundError`. El módulo debe estar en la misma carpeta (o en un lugar donde Python busque módulos).

> [!question]- ¿Para qué sirve conocer los parámetros y el resultado de una función escrita por otra persona?
> Para usarla correctamente sin leer su código: basta saber qué hay que entregarle y qué devuelve.
