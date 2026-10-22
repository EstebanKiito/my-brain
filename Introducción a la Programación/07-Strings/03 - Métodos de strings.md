---
ramo: "Introducción a la Programación"
tema: "Strings"
tags:
  - programacion/strings
  - origen/complemento
prerrequisitos:
  - "[[02 - Slicing: rebanar strings]]"
---

# Métodos de strings

Contar letras o buscar un pedazo de texto con ciclos es un buen ejercicio, pero son tareas tan comunes que Python ya las trae resueltas como **métodos**. Un método es una función que "pertenece" a un valor y se llama con un punto: `s.count("a")` en vez de `contar(s, "a")`.

## Métodos más usados

| Método | Qué entrega | Ejemplo con `s = "abracadabra"` |
|---|---|---|
| `s.count(x)` | Cuántas veces aparece `x` | `s.count("a")` → `5` |
| `s.find(x)` | Primera posición de `x`, o `-1` | `s.find("rac")` → `2` |
| `s.lower()` | Copia en minúsculas | `"Hola".lower()` → `"hola"` |
| `s.upper()` | Copia en mayúsculas | `"Hola".upper()` → `"HOLA"` |
| `s.strip()` | Copia sin espacios ni saltos de línea al inicio y al final | `"  hola \n".strip()` → `"hola"` |
| `s.replace(x, y)` | Copia con cada `x` cambiado por `y` | `s.replace("a", "o")` → `"obrocodobro"` |
| `s.startswith(x)` | ¿Empieza con `x`? | `s.startswith("abra")` → `True` |
| `s.endswith(x)` | ¿Termina con `x`? | `s.endswith("bra")` → `True` |

`count` y `find` aceptan además desde dónde (y hasta dónde) buscar: `s.find("ra", 4)` busca a partir del índice 4 y entrega `9`. `strip` también puede recibir qué caracteres borrar: `"xxholaxx".strip("x")` → `"hola"`.

> [!warning] Los métodos no cambian el string
> Como los strings son inmutables, `s.upper()` **entrega** un string nuevo y deja `s` igual. Si se escribe solo `s.upper()` en una línea, el resultado se pierde. Hay que guardarlo: `s = s.upper()`.

## Preguntar cómo es un string

Otros métodos responden `True` o `False`:

| Método | ¿Es verdadero cuando…? | `"Hola"` | `"1234"` | `"hola y chao"` |
|---|---|---|---|---|
| `isalpha()` | todos son letras | True | False | False (tiene espacios) |
| `isdecimal()` | todos son dígitos | False | True | False |
| `isalnum()` | todos son letras o dígitos | True | True | False |
| `islower()` | las letras están en minúscula | False | False | True |
| `isupper()` | las letras están en mayúscula | False | False | False |
| `isspace()` | todos son espacios | False | False | False |

Son útiles para validar datos: por ejemplo, revisar con `isdecimal()` que el usuario escribió un número antes de convertirlo con `int`.

## El operador `in`

`x in s` pregunta si `x` aparece **en alguna parte** de `s`:

```python
print("za" in "manzana")    # True
print("az" in "manzana")    # False
print("m" in "manzana")     # True
```

Es la forma más legible de buscar cuando solo importa *si está*, no *dónde*.

## Comparar strings: orden alfabético

Los operadores `<`, `>`, `==` también funcionan con strings y comparan en orden alfabético, letra por letra: `"barco" < "casa"` es `True`. Pero hay una trampa: el computador ordena según un código numérico de cada carácter, y en ese código **todas las mayúsculas van antes que todas las minúsculas** (A < … < Z < a < … < z).

```python
print("casa" < "barco")     # False, como en el diccionario
print("Casa" < "barco")     # True: "C" mayúscula va antes que "b" minúscula
print(ord("A"), ord("a"))   # 65 97: los códigos de cada letra
```

> [!tip] Solución
> Para comparar textos sin que importen las mayúsculas, se pasan ambos a minúscula: `a.lower() < b.lower()`.

## Ejemplo: ordenar tres palabras

```python
def ordenar(x, y, z):
    x, y, z = x.lower(), y.lower(), z.lower()
    if x <= y <= z:
        print(x, y, z)
    elif x <= z <= y:
        print(x, z, y)
    elif y <= x <= z:
        print(y, x, z)
    elif y <= z <= x:
        print(y, z, x)
    elif z <= x <= y:
        print(z, x, y)
    else:
        print(z, y, x)

ordenar("Casa", "arbol", "Barco")
```

```
arbol barco casa
```

## Más métodos

`help(str)` en la consola de Python muestra la lista completa de métodos de strings. No hace falta memorizarlos: basta saber que existen y buscarlos cuando se necesiten.

## Preguntas de repaso

> [!question]- ¿Por qué después de `s = "hola"` y `s.upper()` la variable `s` sigue siendo `"hola"`?
> Porque los métodos de strings no modifican el original (es inmutable): entregan un string nuevo, que hay que guardar con `s = s.upper()`.

> [!question]- ¿Qué entrega `"abracadabra".find("z")` y por qué es útil ese valor?
> Entrega `-1`, que indica que no se encontró. Como ningún índice válido es -1, permite distinguir "no está" de "está en la posición 0".

> [!question]- ¿Por qué `"Zorro" < "abeja"` es `True`?
> Porque en el código de caracteres todas las mayúsculas van antes que las minúsculas, así que "Z" es menor que "a". Para comparar alfabéticamente de verdad hay que pasar ambos a minúscula.
