---
ramo: "Introducción a la Programación"
tema: "Ciclos"
tags:
  - programacion/ciclos
  - origen/complemento
prerrequisitos:
  - "[[01 - El ciclo while]]"
---

# El ciclo for y range

Con `while` hay que manejar el contador a mano: crearlo, revisarlo en la condición y aumentarlo. Cuando se sabe **de antemano cuántas veces** repetir algo ("pedir 100 notas", "mostrar del 1 al 10"), Python ofrece una forma más corta y menos propensa a errores: el ciclo `for` junto con `range`.

## `for` recorre una secuencia

```text
for variable in secuencia:
    instrucciones
```

`for` toma, uno por uno, los elementos de una **secuencia** y en cada vuelta los guarda en la variable. El ciclo termina solo cuando se acaban los elementos: no hay condición que revisar ni contador que aumentar.

## `range`: generar números

`range` produce una progresión de enteros:

| Llamada | Números que genera | Para recordar |
|---|---|---|
| `range(5)` | 0, 1, 2, 3, 4 | Parte en 0 y **no incluye** el 5 |
| `range(1, 6)` | 1, 2, 3, 4, 5 | Desde el primero, hasta antes del segundo |
| `range(1, 10, 2)` | 1, 3, 5, 7, 9 | El tercer número es el **paso** |
| `range(10, 0, -1)` | 10, 9, …, 1 | Con paso negativo cuenta hacia atrás |

```python
for n in range(1, 5):
    print(n, n ** 2)
```

```
1 1
2 4
3 9
4 16
```

Compárese con el `while` equivalente: las tres líneas de manejo del contador (`n = 1`, `n <= 4`, `n = n + 1`) quedan resumidas en `range(1, 5)`.

> [!warning] `range` no incluye el último número
> `range(1, 100)` llega hasta 99. Para incluir el 100 hay que escribir `range(1, 101)`. Es el error más común con `for`.

## El promedio de notas con `for`

```python
cuantas = int(input("cuantas notas vas a ingresar? "))
suma = 0
for i in range(cuantas):
    nota = float(input("nota? "))
    suma += nota
print("promedio =", suma / cuantas)
```

Aquí `i` toma los valores 0, 1, …, `cuantas - 1`, pero ni siquiera se usa: solo importa que el bloque se repita `cuantas` veces.

## `for` con textos

Un texto también es una secuencia (de caracteres), así que `for` lo puede recorrer letra por letra:

```python
for letra in "hola":
    print(letra)
```

```
h
o
l
a
```

Esto se usa mucho en el tema de strings y, más adelante, con listas.

## ¿`while` o `for`?

| Situación | Ciclo recomendado |
|---|---|
| Se sabe cuántas veces repetir (100 notas, del 1 al 10) | `for` con `range` |
| Recorrer cada letra de un texto o cada elemento de una lista | `for` |
| No se sabe cuántas veces: "hasta que el usuario escriba -1", "hasta adivinar" | `while` |

> [!tip] Regla práctica
> Si al leer el enunciado aparece un número fijo de repeticiones, usa `for`. Si aparece un "hasta que…", usa `while`.

## Algunos detalles de `print` útiles con ciclos

- `"\t"` dentro de un texto es un **tabulador** y alinea columnas: `print(f"{n}\t{n**2}")`.
- `"\n"` es un **salto de línea**.
- Por defecto, `print` termina con un salto de línea. Con `end` se cambia: `print("hola", end=" ")` deja el cursor en la misma línea.

```python
for n in range(1, 6):
    print(n, end=" ")
print()
```

```
1 2 3 4 5
```

## Preguntas de repaso

> [!question]- ¿Qué números genera `range(3, 8)`?
> 3, 4, 5, 6 y 7. Empieza en el primer número y termina justo antes del segundo.

> [!question]- ¿Por qué para un menú que se repite "hasta que el usuario elija salir" conviene `while` y no `for`?
> Porque no se sabe de antemano cuántas veces se repetirá; depende de lo que haga el usuario. `for` con `range` necesita conocer la cantidad antes de empezar.

> [!question]- ¿Cómo se muestran los números pares del 2 al 20 con un solo `range`?
> Con `for n in range(2, 21, 2): print(n)`. El paso 2 salta de par en par y el 21 hace que se incluya el 20.
