---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/estilo
  - origen/complemento
prerrequisitos:
  - "[[10 - Anotaciones de tipo y el módulo typing]]"
---

# Guía de estilo: por qué y cómo nombrar

Escribir código que funciona no basta: otras personas (y tú mismo dentro de unos meses) tienen que poder leerlo. Una **guía de estilo** es un conjunto de reglas de escritura que hace que todo el código parezca escrito por una sola persona. Esta nota explica para qué sirve y las reglas de nombres.

## Qué es una guía de estilo

Es el acuerdo de un equipo (o de una comunidad) sobre cómo escribir código. Hay dos tipos de reglas:

- **Reglas de formato:** cómo se escribe un nombre (`mivariable`, `mi_variable` o `miVariable`) o cuántos espacios se usan.
- **Reglas semánticas:** qué nombre se le da a algo (`funcion_que_suma` o simplemente `suma`).

Qué reglas se usan lo decide cada proyecto: en equipos grandes se acuerdan antes de empezar o se adopta una guía ya creada. Empresas como Meta, Google o Amazon usan guías distintas según el lenguaje y el proyecto.

## Por qué usarla

Seguir reglas puede parecer trabajo extra, pero ahorra tiempo.

| Ventaja | Por qué ocurre |
|---|---|
| **Código más legible** | Se pasa más tiempo leyendo código que escribiéndolo. Python tiene una sintaxis muy legible, pero los malos hábitos la arruinan |
| ***Debugging* más rápido** | Encontrar un error (*bug*) es mirar código por mucho rato; si está ordenado, se encuentra antes |
| **Se escribe más rápido** | Con reglas ya definidas hay menos decisiones que tomar al nombrar cosas |
| **Nombres predecibles** | En proyectos grandes no hay que buscar a mano cómo se llamaba cada función, clase o archivo |

> [!tip] Regla
> El código se escribe una vez y se lee muchas. Conviene optimizar para quien lo va a leer.

## PEP8: la guía de Python

**PEP8** es la guía de estilo oficial de Python. El curso usa solo un subconjunto de sus reglas, y se espera que las apliques en tus tareas. Las reglas de nombres son tres.

### `snake_case` para casi todo

`snake_case` escribe las palabras en minúscula separadas por guion bajo (`_`), sin espacios. Se usa para **variables, atributos, funciones y métodos**, o sea, para prácticamente todo menos las clases.

### `CamelCase` para las clases

`CamelCase` junta las palabras sin separador y cada una empieza con mayúscula (`PerroAmigable`). Se reserva para los **nombres de clases**. Es la variante «con mayúscula inicial» (*upper camel case*).

```python
from __future__ import annotations


class PerroAmigable:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar_amigo(self, amigo: PerroAmigable) -> None:
        print("¡Woof!")
        print("¡Hola " + amigo.nombre + "!")


def saludo_mutuo(perro_1: PerroAmigable, perro_2: PerroAmigable):
    perro_1.saludar_amigo(perro_2)
    perro_2.saludar_amigo(perro_1)
    print()


perro_juan = PerroAmigable("Juan", 21)
perro_pedro = PerroAmigable("Pedro", 20)
saludo_mutuo(perro_juan, perro_pedro)
```

```
¡Woof!
¡Hola Pedro!
¡Woof!
¡Hola Juan!

```

Fíjate: clase en `CamelCase` (`PerroAmigable`), todo lo demás en `snake_case` (`saludar_amigo`, `perro_juan`, `edad`).

### Nombres descriptivos

Nombres como `a`, `l` o `var` ahorran tecleo, pero obligan a adivinar. Compara estas dos funciones, que hacen exactamente lo mismo:

```python
def funcion(l: list) -> int:
    i = 0
    a = l[0]
    for j in range(1, len(l)):
        var = l[j]
        if var > a:
            j = i
            a = var
    return i
```

```python
def indice_de_maximo(lista: list) -> int:
    indice_actual = 0
    maximo_actual = lista[0]
    for indice in range(1, len(lista)):
        elemento = lista[indice]
        if elemento > maximo_actual:
            indice_actual = indice
            maximo_actual = elemento
    return indice_actual

print(indice_de_maximo([3, 9, 2, 9, 5]))
```

```
1
```

En la segunda versión se entiende al instante qué hace. En la primera, además, hay un error escondido (`j = i` en vez de `i = j`) que con nombres claros sería evidente.

> [!warning] Una clase no se llama como una variable
> `perro_amigable` para una clase o `PerroJuan` para una variable rompen la convención. Quien lea el código distingue clases de variables solo por la forma del nombre.

## Preguntas de repaso

> [!question]- ¿Por qué se dice que una guía de estilo ahorra tiempo al escribir código?
> Porque al tener reglas para nombrar cosas se toman menos decisiones, y porque después es más fácil encontrar y arreglar errores en un código ordenado.

> [!question]- ¿Qué convención se usa para el nombre de una clase y cuál para un método?
> Las clases usan `CamelCase` (`PerroAmigable`) y los métodos `snake_case` (`saludar_amigo`).

> [!question]- ¿Qué problema tiene la función `funcion(l)` del ejemplo, además de su nombre?
> Tiene un error: asigna `j = i` en vez de guardar el índice en `i`, así que siempre retorna 0. Con nombres descriptivos ese error se nota mucho más.

