---
ramo: "Introducción a la Programación"
tema: "Condicionales"
tags:
  - programacion/control-de-flujo
  - origen/complemento
prerrequisitos:
  - "[[01 - If, else e indentación]]"
---

# Condiciones compuestas: and, or y not

Muchas reglas tienen más de una parte: "apruebas si tu promedio es mayor o igual a 4 **y** tienes asistencia", "entras gratis si eres menor de 12 **o** mayor de 65". Para expresarlas se combinan comparaciones con los **operadores lógicos** `and`, `or` y `not`.

## Condición simple y condición compuesta

Una **condición simple** es una sola comparación (`valor >= 0`). Una **condición compuesta** une varias con operadores lógicos:

| Operador | Significado | Es verdadera cuando… |
|---|---|---|
| `and` | "y" | **ambas** partes son verdaderas |
| `or` | "o" | **al menos una** parte es verdadera |
| `not` | "no" | la condición es falsa (la invierte) |

Tabla de verdad (V = `True`, F = `False`):

| `c1` | `c2` | `c1 and c2` | `c1 or c2` | `not c1` |
|---|---|---|---|---|
| V | V | V | V | F |
| V | F | F | V | F |
| F | V | F | V | V |
| F | F | F | F | V |

```python
edad = 70
print(edad < 12 or edad > 65)    # True: basta con que una se cumpla
print(edad > 18 and edad < 30)   # False: la segunda no se cumple
print(not edad > 65)             # False: invierte True
```

## Ejemplo: cachipún

Piedra (1), papel (2), tijeras (3). El usuario gana en tres situaciones: piedra contra tijeras, papel contra piedra o tijeras contra papel. Cada situación es un `and`, y las tres se unen con `or`:

```python
import random

print("Juguemos cachipun!")
computador = random.randint(1, 3)
usuario = int(input("Elige: (1) Piedra, (2) Papel, (3) Tijeras: "))
gano = (usuario == 1 and computador == 3) or \
       (usuario == 2 and computador == 1) or \
       (usuario == 3 and computador == 2)
print(f"Yo juego: {computador}")
print(f"Ganaste: {gano}")
```

Los paréntesis agrupan cada situación y hacen el código fácil de leer. (La `\` al final de una línea permite seguir la instrucción en la línea siguiente.)

## Rangos: estar "entre" dos valores

Para saber si un valor está entre 0 y 99:

```python
valor = 124
print(valor >= 0 and valor <= 99)   # False
print(0 <= valor <= 99)             # False: forma abreviada, igual que en matemáticas
```

Python permite **encadenar** comparaciones: `0 <= valor <= 99` significa exactamente `0 <= valor and valor <= 99`. Es más corta y se parece a cómo se escribe en matemáticas.

> [!warning] `or` con la variable repetida
> Para preguntar si `x` es 1 o 2 se escribe `x == 1 or x == 2`. Escribir `x == 1 or 2` **no** funciona como se espera: Python lo lee como `(x == 1) or 2`, y `2` cuenta como verdadero, así que la condición siempre se cumple.

## Ejemplo: divisible por 6

Un número es divisible por 6 si es divisible por 2 **y** por 3:

```python
n = 18
if n % 2 == 0 and n % 3 == 0:
    print(n, "es divisible por 6")
```

> [!tip] Cómo traducir una regla
> "y" en el enunciado → `and`. "o" → `or`. "no", "a menos que" → `not` (o la comparación contraria). Antes de escribir, conviene probar la regla con un par de ejemplos a mano.

## Preguntas de repaso

> [!question]- ¿Por qué en el cachipún se usan `and` dentro de los paréntesis y `or` entre ellos?
> Cada forma de ganar exige dos cosas a la vez (mi jugada **y** la del computador), por eso `and`. Basta con que ocurra cualquiera de las tres formas, por eso se unen con `or`.

> [!question]- ¿Qué devuelve `True and False or True`?
> `True`. `and` se evalúa antes que `or`: `True and False` es `False`, y `False or True` es `True`. Para evitar dudas conviene usar paréntesis.

> [!question]- ¿Por qué `x == 1 or 2` es siempre verdadero?
> Porque Python evalúa `x == 1` y, si es falso, toma el `2` como segunda condición, y cualquier número distinto de 0 cuenta como verdadero. Hay que escribir `x == 1 or x == 2`.
