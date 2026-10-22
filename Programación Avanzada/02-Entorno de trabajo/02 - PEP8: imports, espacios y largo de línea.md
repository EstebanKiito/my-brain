---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/estilo
  - origen/complemento
prerrequisitos:
  - "[[01 - Guía de estilo: por qué y cómo nombrar]]"
---

# PEP8: imports, espacios y largo de línea

Además de los nombres, PEP8 fija cómo se acomoda el código en el archivo: dónde van los `import`, cómo se usan los espacios, cuánto se indenta y cuánto puede medir una línea. Son reglas pequeñas que hacen el código mucho más fácil de recorrer con la vista.

## Imports al comienzo del archivo

Todas las importaciones van **arriba**, antes del resto del código. Así todas las dependencias externas se encuentran en un solo lugar y no repartidas por el archivo.

```python
import os
import random

# ...
# El resto del código
```

## Espacios

**Un espacio después de la coma**, siempre que se enumeren elementos: al importar, en la definición de funciones, en los `return`, en las listas y en las llamadas.

```python
from random import randint, choice


def operaciones_con_potencia(lista: list, potencia: int) -> tuple[int, int]:
    suma = 0
    multiplicacion = 1
    for elemento in lista:
        suma += elemento ** potencia
        multiplicacion *= elemento ** potencia
    return suma, multiplicacion


numeros = [3, 6, 2, 4]
print(operaciones_con_potencia(numeros, 2))
```

```
(65, 20736)
```

**Espacios a cada lado de los operadores** matemáticos:

```python
valor_1 = ((6 ** 17) - 1) / 2
resultado = (1 + valor_1) * 3
resto_en_dos = resultado % 2
```

## Indentación: 4 espacios, sin tabs

Cada nivel de indentación usa **cuatro espacios**, no tabuladores (*tabs*). Python 3 no permite mezclar ambos en un mismo archivo para indentar bloques, y los editores se pueden configurar para insertar espacios al apretar la tecla Tab.

## Largo máximo de línea: 100 caracteres

PEP8 original recomienda 80 caracteres (por compatibilidad con herramientas que muestran solo ese ancho); en el curso se relaja a **100 caracteres**, contando espacios e indentación. La regla busca evitar líneas largas en general, no solo arreglar las que pasen el límite.

Este código tiene una línea muy larga:

```python
valor_1 = 600
valor_2 = 700
if valor_1 + valor_2 >= 1000 and (valor_1 - valor_2 >= 1000 or valor_2 - valor_1 >= 1000):
    print("Los números suman mucho y están muy separados")
```

Hay tres formas de acortarla.

**1. Barra invertida (`\`)** para continuar en la línea siguiente:

```python
# valor_1 = 600 y valor_2 = 700 (igual que arriba)
if valor_1 + valor_2 >= 1000 and \
            (valor_1 - valor_2 >= 1000 or valor_2 - valor_1 >= 1000):
    print("Los números suman mucho y están muy separados")
```

**2. Variables auxiliares**, que además dan nombre a cada idea:

```python
valor_1 = 600
valor_2 = 700
suma = valor_1 + valor_2
diferencia = abs(valor_1 - valor_2)
if suma >= 1000 and diferencia >= 1000:
    print("Los números suman mucho y están muy separados")
elif suma >= 1000:
    print("Los números suman mucho")
elif diferencia >= 1000:
    print("Los números están muy separados")
else:
    print("Los números son apropiados")
```

```
Los números suman mucho
```

> [!tip] Cuál preferir
> Se prefiere reescribir con variables auxiliares antes que usar `\`, porque la barra invertida es menos legible y un espacio olvidado después de ella rompe el código.

## Resumen de reglas

| Regla | Ejemplo correcto |
|---|---|
| `import` al inicio del archivo | `import os` en la primera línea |
| Un espacio tras la coma | `f(a, b, c)` |
| Espacios alrededor de operadores | `x = (a + b) * 2` |
| 4 espacios por nivel, sin tabs | `····if x:` |
| Máximo 100 caracteres por línea | partir con variables auxiliares |

## Preguntas de repaso

> [!question]- ¿Por qué conviene dejar todos los `import` arriba del archivo?
> Porque así las dependencias externas están todas en un solo lugar y se ven de un vistazo, en vez de aparecer repartidas por el archivo.

> [!question]- ¿Por qué se prefiere una variable auxiliar a la barra invertida para acortar una línea?
> La variable auxiliar da un nombre a cada idea y deja el código más claro; la barra invertida es menos legible y se rompe si queda un espacio después de ella.

> [!question]- ¿Qué pasa si se mezclan tabs y espacios para indentar en Python 3?
> Python no lo permite dentro de un mismo bloque y da un error de indentación. Por eso se usan siempre 4 espacios.
