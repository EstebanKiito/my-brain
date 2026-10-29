---
ramo: "Testing"
tema: "Análisis de flujo de información y taint analysis"
tags:
  - testing/analisis-de-flujo-de-informacion-y-taint-analysis
  - origen/complemento
prerrequisitos:
  - "[[Testing/10-Análisis de flujo de información y taint analysis/01 - Flujo de información sources sinks sanitizers e inyección SQL|Flujo de información sources sinks sanitizers e inyección SQL]]"
  - "[[Programación Avanzada/01-Repaso y POO básica/06 - Clases, objetos y variables de clase|Clases, objetos y variables de clase]]"
---

# Implementación de strings contaminados con la clase tstr en Python

## ¿Cómo le pegamos una etiqueta a un `str` sin romper el código existente?

Si queremos rastrear por dónde viaja un string en un programa Python ya escrito, no podemos cambiar los strings por tuplas `("hola", "LOW")`, porque en cuanto el programa llame a `texto.upper()` o `texto + " mundo"` fallaría al no ser un objeto `str`.

La solución elegante (usada en *The Fuzzing Book*) es la **herencia**: creamos una clase **`tstr` que hereda directamente de `str`**. Como toda instancia de `tstr` **es** un `str` (`isinstance(s, str) == True`), pasa todos los chequeos de tipos y posee todos los métodos de una cadena normal, pero además lleva guardado un atributo extra: **`self.taint`**.

---

## El detalle técnico de heredar de un tipo inmutable (`__new__` frente a `__init__`)

En Python, casi siempre inicializamos atributos dentro de `__init__(self, ...)`. Sin embargo, **`str` es un tipo inmutable en C**: el valor de texto de la cadena se fija en el momento mismo en que se reserva la memoria del objeto, **antes** de que se ejecute `__init__`, mediante el método especial de construcción **`__new__(cls, value, ...)`**.

Si intentas pasar `taint='LOW'` a `tstr('hello', taint='LOW')` sin sobrescribir `__new__`, el método `str.__new__` de Python se quejará diciendo que `str` no acepta el argumento con nombre `taint`. Por eso, en `tstr` separamos las dos fases de vida del objeto:

1. **`__new__(cls, value, *args, **kw)`:** intercepta la creación del objeto inmutable y le pasa a `str.__new__(cls, value)` **únicamente el `value`** (la cadena de texto), devolviendo la nueva instancia de `tstr`.
2. **`__init__(self, value, taint=None, **kwargs)`:** recibe la instancia recién creada por `__new__` y le adjunta el atributo mutable **`self.taint = taint`**.

```python
from typing import Any

class tstr(str):
    """Wrapper para strings que almacena y propaga información de taint."""

    def __new__(cls, value, *args, **kw):
        """Crea la instancia inmutable de tstr pasando solo value a str.__new__."""
        return str.__new__(cls, value)

    def __init__(self, value: Any, taint: Any = None, **kwargs) -> None:
        """Guarda el metadato taint en la instancia ya creada."""
        self.taint: Any = taint

    def __repr__(self):
        """Devuelve la representación conservando el taint en un nuevo tstr."""
        return tstr(str.__repr__(self), taint=self.taint)

    def __str__(self) -> str:
        """Convierte a un str estándar limpio."""
        return str.__str__(self)
```

Observa la diferencia intencional entre `__repr__` y `__str__`:
* `repr(thello)` devuelve otro `tstr` que **conserva el `taint`** (`repr(thello).taint == 'LOW'`), por si el programa construye mensajes o consultas usando `repr(x)` o `%r`.
* `str(thello)` llama a `str.__str__(self)`, devolviendo un `str` nativo de Python sin atributo `taint`.

---

## Métodos para consultar, limpiar y clonar la mancha (`has_taint`, `clear_taint`, `create`)

Una vez definida la base de `tstr`, agregamos tres métodos auxiliares que nos permiten inspeccionar la mancha, sanitizarla o transmitirla a una cadena hija:

```python
class tstr(tstr):
    def has_taint(self) -> bool:
        """Verifica si la cadena posee actualmente alguna marca de taint."""
        return self.taint is not None

    def clear_taint(self):
        """Remueve la marca de taint (actúa como sanitizer) y retorna self."""
        self.taint = None
        return self

    def create(self, s) -> "tstr":
        """Fábrica interna: envuelve cualquier string s heredando el taint de self."""
        return tstr(s, taint=self.taint)
```

Veamos cómo interactúan estos tres métodos en un flujo real:

```python
thello = tstr("hello", taint="LOW")
assert thello.has_taint() is True
assert thello.taint == "LOW"

# Si a partir de thello fabricamos otro string con .create(), hereda 'LOW':
derivado = thello.create("world")
assert derivado.taint == "LOW"

# Si sanitizamos thello con clear_taint(), su mancha desaparece:
thello.clear_taint()
assert thello.has_taint() is False
assert thello.taint is None
```

El método `self.create(s)` parece diminuto, pero es la pieza arquitectónica más importante de la clase: cualquier operación sobre `self` que produzca un texto nuevo `res` solo tendrá que retornar **`self.create(res)`** para que la mancha viaje automáticamente al resultado.

---

## Preguntas de repaso

> [!question]- ¿Por qué al heredar de `str` para construir `tstr` es obligatorio definir `__new__(cls, value, *args, **kw)` además de `__init__(self, value, taint=None)`?
> Porque `str` es un tipo inmutable cuyo contenido se aloja en memoria dentro de `str.__new__`, el cual solo acepta el valor del string y la codificación, pero rechaza argumentos extra como `taint='LOW'`. Sobrescribir `__new__` permite filtrar `*args` y `**kw` al llamar a `str.__new__(cls, value)`, dejando que `__init__` reciba y asigne `self.taint = taint`.

> [!question]- ¿Por qué `clear_taint(self)` termina con `return self` en lugar de no retornar nada (`None`)?
> Para permitir encadenamiento fluido (*method chaining*) al sanitizar una expresión en una sola línea, por ejemplo `query = entrada_usuario.clear_taint()` o `sink( sanitizar(cmd).clear_taint() )`.

> [!question]- ¿Qué devuelve `repr(tstr('hola', taint='HIGH')).taint` y por qué `__repr__` está diseñado de esa forma?
> Devuelve `'HIGH'`, porque `tstr.__repr__` envuelve el resultado de `str.__repr__(self)` dentro de un nuevo `tstr(..., taint=self.taint)`. Está diseñado así para que el rastro de contaminación no se pierda cuando un programa formatea o serializa cadenas usando `repr(x)` o `f"{x!r}"`.
