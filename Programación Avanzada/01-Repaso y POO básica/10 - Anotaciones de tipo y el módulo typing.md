---
ramo: "Programación Avanzada"
tema: "Repaso y POO básica"
tags:
  - programacion/typing
  - origen/complemento
prerrequisitos:
  - "[[06 - Clases, objetos y variables de clase]]"
---

# Anotaciones de tipo y el módulo typing

A medida que un programa crece, cuesta recordar qué tipo de dato espera cada variable o función. Las **anotaciones** dejan ese dato escrito en el código: sirven de documentación y hacen que el editor (IDE) autocomplete y avise de errores. Esta nota es de profundización.

## Anotar variables y funciones

Después del nombre se escribe `:` y el tipo. En una función, el tipo del resultado se indica con `->` después de los parámetros.

```python
variable_numerica: int = 42
nombre: str = "Julián"

def direccion(calle: str, numero: int) -> str:
    return f'{calle.strip().title()} {numero}'

print(direccion("  alameda ", 10))
```

```
Alameda 10
```

También sirven las propias clases como tipo:

```python
class Computador:
    def __init__(self) -> None:
        self.energia: int = 100

    def reducir_energia(self) -> None:
        self.energia -= 1

mi_pc: Computador = Computador()
```

`-> None` indica que el método no devuelve nada.

> [!warning] Las anotaciones no obligan
> Escribir `variable_numerica = "la respuesta"` hace que el IDE muestre una alerta, pero **el programa se ejecuta igual**. Son una guía, no una regla que Python haga cumplir.

## El módulo `typing`

Para tipos más flexibles, el módulo `typing` aporta los siguientes:

| Tipo | Significado | Ejemplo |
|---|---|---|
| `Any` | Cualquier tipo, sin restricción | `x: Any = 1` |
| `Union[A, B]` | Puede ser `A` o `B` (desde Python 3.10 también `A \| B`) | `Union[int, float]` o `int \| float` |
| `Optional[X]` | Es `X` o `None` (equivale a `X \| None`) | `Optional[int]` |
| `Callable[[args], ret]` | Una función, con tipos de argumentos y retorno | `Callable[[int, int], float]` |
| `List[X]` | Lista cuyos elementos son de tipo `X` | `List[int]` |

```python
from typing import Any, Union, Callable, Optional, List

def dividir(numerador: Union[int, float], denominador: Union[int, float]) -> float:
    return numerador / denominador

funcion: Callable[[Union[int, float], Union[int, float]], float] = dividir
print(funcion(1.0, 2))

valor: Optional[int] = None
valor = 1

lista: List[int] = [1, 2, 3, 4, 5, 6]
```

```
0.5
```

`typing` ofrece tipos equivalentes para el resto de las estructuras (diccionarios, conjuntos, etc.) y para las de `collections`; la documentación oficial tiene la lista completa.

## Una clase que se nombra a sí misma

Hay un problema: dentro de una clase no se puede usar su propio nombre como tipo, porque al momento de leer la definición la clase aún no existe.

```python
from __future__ import annotations   # pospone la evaluación de las anotaciones
from typing import Optional

class Persona:
    def __init__(self: Persona) -> None:
        self.bff: Optional[Persona] = None

    def asignar_bff(self: Persona, otro: Persona) -> None:
        self.bff = otro

ana = Persona()
ben = Persona()
ana.asignar_bff(ben)
print(ana.bff is ben)
```

```
True
```

La línea `from __future__ import annotations` hace que las anotaciones se evalúen **después**, cuando todos los tipos ya existen. Sin ella, el código con `Persona` dentro de `Persona` falla al definir la clase.

## Preguntas de repaso

> [!question]- ¿Para qué sirve anotar tipos si Python no los exige?
> Para documentar el código y para que los IDE autocompleten y avisen de errores antes de ejecutar. Ayuda sobre todo cuando se vuelve a código antiguo o ajeno.

> [!question]- ¿Qué significan `Optional[int]` y `int | None`?
> Lo mismo: la variable puede contener un entero o `None`.

> [!question]- ¿Por qué una clase no puede anotarse a sí misma sin `from __future__ import annotations`?
> Porque al evaluar la anotación dentro de la definición de la clase, el nombre de la clase todavía no existe. La importación pospone la evaluación hasta que ya exista.
