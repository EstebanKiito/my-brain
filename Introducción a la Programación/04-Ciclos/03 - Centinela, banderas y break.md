---
ramo: "Introducción a la Programación"
tema: "Ciclos"
tags:
  - programacion/ciclos
  - origen/complemento
prerrequisitos:
  - "[[01 - El ciclo while]]"
---

# Centinela, banderas y break

Muchas veces no se sabe cuántos datos va a ingresar el usuario. Un caso típico: "ingresa notas; cuando termines, escribe -1". Ese valor especial que avisa el final se llama **centinela**. Esta nota muestra tres formas de escribir un ciclo que termina con un centinela, y sus ventajas.

## El problema

```
nota? 5.0
nota? 4.0
nota? -1
promedio = 4.5
```

El -1 **no es una nota**: no debe sumarse ni contarse. Ahí está la dificultad.

## Forma 1: leer antes del ciclo y al final de cada vuelta

```python
suma = 0
n = 0
nota = float(input("nota? "))     # primera lectura, antes del ciclo
while nota != -1:
    suma += nota
    n += 1
    nota = float(input("nota? "))  # siguiente lectura, al final
print("promedio =", suma / n)
```

La condición se revisa justo después de cada lectura, así que el -1 nunca alcanza a sumarse. Su costo es que el `input` aparece escrito dos veces.

## Forma 2: una bandera (variable `bool`)

Una **bandera** (*flag*) es una variable `True`/`False` que indica si hay que seguir:

```python
suma = 0
n = 0
seguir = True
while seguir:
    nota = float(input("nota? "))
    if nota == -1:
        seguir = False
    else:
        suma += nota
        n += 1
if n == 0:
    print("No hay suficientes notas")
else:
    print("promedio =", suma / n)
```

Al leer el -1, la bandera pasa a `False`; el ciclo termina la vuelta actual y, al volver a la condición, sale.

> [!warning] Dividir por cero
> Si el usuario escribe -1 de inmediato, `n` queda en 0 y `suma / n` produce `ZeroDivisionError`. Por eso se revisa `n == 0` antes de dividir.

## Forma 3: `break`

`break` **sale del ciclo inmediatamente**, sin terminar la vuelta ni revisar la condición:

```python
suma = 0
n = 0
while True:
    nota = float(input("nota? "))
    if nota == -1:
        break
    suma += nota
    n += 1
print("notas ingresadas:", n)
```

`while True` sería un bucle infinito, pero el `break` dentro del `if` le da una salida. Se usa siempre dentro de un `if`: un `break` suelto cortaría el ciclo en la primera vuelta.

> [!tip] Cuál elegir
> Las tres formas son correctas. La bandera deja explícito por qué termina el ciclo; `break` es más corto, pero si se abusa de él (varios `break` en un ciclo largo) cuesta seguir el flujo del programa. Usar `break` con cuidado.

## Ejemplo: jugar hasta adivinar

Ahora el juego del dado se repite hasta que el usuario acierte:

```python
import random

dado = random.randint(1, 6)
adivinado = False
intentos = 0
while not adivinado:
    n = int(input("Adivina cual numero me sale? "))
    intentos += 1
    if n == dado:
        adivinado = True
    else:
        print("Intenta de nuevo!")
print(f"Adivinaste!! en {intentos} intentos")
```

Aquí no hay un centinela escrito por el usuario: la condición de término es acertar. `not adivinado` se lee "mientras no haya adivinado".

## Preguntas de repaso

> [!question]- En la forma 1, ¿por qué hay que leer la nota antes del `while`?
> Porque la condición `nota != -1` necesita una nota para revisarse. Sin esa primera lectura, la variable `nota` no existiría al llegar al `while`.

> [!question]- ¿Qué diferencia hay entre poner la bandera en `False` y usar `break`?
> Con la bandera, el ciclo termina la vuelta actual y sale al revisar la condición. Con `break`, sale en ese mismo instante, sin ejecutar lo que queda del bloque.

> [!question]- ¿Por qué el -1 no debe sumarse al promedio?
> Porque no es una nota, sino la señal de término. Si se sumara (y contara), el promedio quedaría mal calculado.
