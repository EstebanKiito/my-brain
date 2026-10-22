---
ramo: "Introducción a la Programación"
tema: "Primeros pasos en Python"
tags:
  - programacion/python
  - origen/complemento
prerrequisitos:
  - "[[01 - Python, IDLE y el primer programa]]"
---

# Variables, input y conversión de tipos

Un programa que solo muestra mensajes fijos sirve de poco. Para ser útil tiene que **pedir datos**, **recordarlos** y **trabajar con ellos**. Para eso se usan `input` (leer del teclado), las **variables** (guardar valores) y las conversiones de tipo (pasar de texto a número y al revés).

## Variables: cajas con nombre

Una **variable** es como una caja con una etiqueta: guarda un valor y se le pone un nombre para poder usarlo después y distinguirlo de otros.

```python
a = 3
nombre = "Juan"
```

La instrucción `nombre = valor` se llama **asignación**. Se lee de **derecha a izquierda**: "toma el valor de la derecha y guárdalo en la variable de la izquierda". Por eso `a = 3` es correcto, pero `3 = a` da error (no se puede guardar algo dentro del número 3).

> [!warning] `=` no es "igual" de matemáticas
> En Python `=` significa "guardar". `x = x + 1` no es una ecuación imposible: significa "calcula `x + 1` con el valor actual de `x` y guarda el resultado otra vez en `x`". Para *preguntar* si dos cosas son iguales se usa `==` (ver [[04 - Funciones predefinidas, random y booleanos|Funciones predefinidas, random y booleanos]]).

**Reglas para los nombres:**
- Pueden tener letras, números y `_`, pero **no pueden empezar con un número** (`nota1` sí, `1nota` no).
- No pueden ser palabras reservadas de Python (`if`, `for`, `while`, `def`, `True`…).
- Conviene que sean descriptivos: `millas` dice mucho más que `m`.

## `input`: pedir datos al usuario

```python
nombre = input("Dime tu nombre: ")
print("Hola " + nombre + "!")
```

```
Dime tu nombre: Valeria
Hola Valeria!
```

`input("…")` hace dos cosas: muestra el mensaje y **espera** a que el usuario escriba algo y presione Enter. Lo escrito se **entrega como resultado**, y con `=` se guarda en una variable para recordarlo.

## Tipos de datos

Cada valor tiene un **tipo**, que define qué se puede hacer con él:

| Tipo | Qué guarda | Ejemplos |
|---|---|---|
| `str` | Texto (string) | `"hola"`, `"42"` |
| `int` | Números enteros | `42`, `-7` |
| `float` | Números con decimales | `3.4`, `72.3` |
| `bool` | Verdadero o falso | `True`, `False` |

Los `str` se pueden **unir** con `+`: `"hola" + "chao"` da `"holachao"`. Los números se suman: `2 + 3` da `5`. El mismo símbolo hace cosas distintas según el tipo.

## Conversión de tipos

`input` **siempre entrega texto**, aunque el usuario escriba un número. Para hacer cálculos hay que convertirlo:

| Función | Convierte | Ejemplo |
|---|---|---|
| `int(...)` | texto → entero | `int("345")` da `345` |
| `float(...)` | texto → decimal | `float("45.3")` da `45.3` |
| `str(...)` | número → texto | `str(345)` da `"345"` |

Ejemplo, el juego de **Jalisco** (siempre gana con un número más):

```python
n = int(input("Dime un numero: "))
print("Te gano con el " + str(n + 1))
```

```
Dime un numero: 10
Te gano con el 11
```

`int(input(...))` combina dos pasos: primero `input` lee el texto `"10"`, luego `int` lo convierte en el número `10`. Al final, `n + 1` es un número y, para pegarlo a un texto con `+`, se convierte con `str`.

> [!warning] Mezclar texto y números con `+`
> `"Te gano con el " + 11` da error (`TypeError`): Python no sabe sumar un texto con un número. Y si se olvida el `int`, `input` entrega `"10"` y `"10" + 1` también falla.

## Tres formas de mostrar texto y variables

```python
n = "Valeria"
print("Hola " + n + "!")   # 1. concatenar con + (todo debe ser str)
print("Hola", n, "!")      # 2. separar con comas (agrega espacios y acepta números)
print(f"Hola {n}!")        # 3. f-string: lo que va entre {} se reemplaza por su valor
```

Las **f-strings** (una `f` antes de las comillas) son la forma más cómoda: aceptan números y cálculos sin convertir, como `f"Te gano con el {n + 1}"`.

Otro ejemplo, convertir millas a kilómetros:

```python
millas = float(input("Cuantas millas vas a viajar? "))
print(f"Son {millas * 1.609} kms")
```

Se usa `float` y no `int` porque las millas pueden tener decimales (`72.3`).

## Preguntas de repaso

> [!question]- ¿Por qué hay que escribir `int(input(...))` para sumar 1 al número ingresado?
> Porque `input` siempre devuelve texto. Sin convertirlo con `int`, Python intentaría sumar un texto con un número y daría error.

> [!question]- ¿Qué muestra `print("2" + "3")` y qué muestra `print(2 + 3)`?
> El primero muestra `23`, porque une dos textos. El segundo muestra `5`, porque suma dos números.

> [!question]- ¿Cuándo conviene usar `float` en vez de `int` al leer un dato?
> Cuando el dato puede tener decimales, como una distancia, un precio o una temperatura. `int("72.3")` da error, mientras que `float("72.3")` funciona.

> [!question]- ¿Qué significa `x = x + 1`?
> Calcula el valor actual de `x` más uno y guarda ese resultado de nuevo en `x`; o sea, aumenta `x` en 1.
