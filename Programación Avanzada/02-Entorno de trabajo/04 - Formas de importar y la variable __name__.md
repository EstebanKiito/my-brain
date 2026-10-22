---
ramo: "Programación Avanzada"
tema: "Entorno de trabajo"
tags:
  - programacion/modulos
  - origen/complemento
prerrequisitos:
  - "[[03 - Modularización: qué es y por qué sirve]]"
---

# Formas de importar y la variable __name__

Python ofrece varias formas de traer definiciones de un módulo, y cada una tiene su lugar (y alguna está prohibida por mala práctica). También existe `__name__`, una variable que permite saber si un archivo fue importado o ejecutado directamente.

Los ejemplos usan `ejemplo.py` de la nota anterior, con `mi_variable`, `saludar` y `MiClase`.

## Las formas de importar

| Forma | Cómo se usa después |
|---|---|
| `import modulo` | `modulo.funcion()` |
| `import modulo as alias` | `alias.funcion()` |
| `from modulo import a, b` | `a()` y `b()` directo |
| `from carpeta import modulo` | `modulo.funcion()` |
| `from modulo import *` | **Mala práctica**, se penaliza en el curso |

### Importación completa

```python
import ejemplo

print(ejemplo.mi_variable)
ejemplo.saludar()
```

Crea una variable con el nombre del módulo y se accede a sus definiciones con punto, igual que a los atributos de un objeto.

### Con alias

```python
import ejemplo as ej

print(ej.mi_variable)
ej.saludar()

ejemplo = "Otra variable"     # no choca con el módulo, que ahora se llama ej
print(ejemplo)
```

El alias sirve cuando el nombre podría confundirse con otro del archivo, o cuando el nombre del módulo es muy largo.

### Importación parcial

```python
from ejemplo import mi_variable, MiClase

print(mi_variable)
instancia = MiClase(23)
print(instancia.argumento)
# saludar()   # NameError: no se importó, así que no existe aquí
```

Evita escribir el nombre del módulo y permite **elegir** qué se importa. Lo que no se nombró no está disponible.

### Módulos dentro de carpetas

Si el proyecto crece, los módulos se ordenan en subcarpetas y se importan con `carpeta.modulo`. Con una carpeta `carpeta_con_modulo` que contiene `modulo.py` (con `variable = "Sopaipillas"`), las cuatro variantes válidas son:

```python
import carpeta_con_modulo.modulo
print(carpeta_con_modulo.modulo.variable)

import carpeta_con_modulo.modulo as modulo
print(modulo.variable)

from carpeta_con_modulo import modulo
print(modulo.variable)

from carpeta_con_modulo.modulo import variable
print(variable)
```

### Importación con asterisco (prohibida)

```python
from modulo import *
```

Trae **todas** las definiciones sin saber cuántas ni cuáles son, y puede **pisar** nombres de tu programa y producir resultados inesperados. Además, quien lee el código no sabe de dónde viene cada nombre.

> [!warning] Se penaliza
> Siempre debe haber una referencia al módulo de origen (importación completa) o una lista explícita de lo importado (importación parcial).

## La variable `__name__`

En cada módulo existe una variable global `__name__`:

- Si el módulo fue **importado**, vale el **nombre del módulo** (como string), con o sin alias.
- Si el módulo es **el que se ejecutó directamente** (el principal), vale `"__main__"`.

```python
# ejemplo2.py
mi_nombre = __name__

if __name__ == "__main__":
    print("Soy el módulo principal")
```

```python
# main.py
import ejemplo2

print(ejemplo2.mi_nombre)    # ejemplo2
print(__name__)              # __main__
```

```
ejemplo2
__main__
```

Al ejecutar `python main.py`, `ejemplo2.py` se importa y el `if` **no** entra (su `__name__` es `"ejemplo2"`), así que no imprime nada. En cambio, si se ejecuta `python ejemplo2.py`, imprime «Soy el módulo principal».

> [!tip] Para qué sirve
> Se usa `if __name__ == "__main__":` en módulos cuyo propósito es ser importados, para dejar código de prueba o de demostración que **solo corre** si alguien ejecuta ese archivo directamente.

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia entre `import ejemplo` y `from ejemplo import mi_variable`?
> Con `import ejemplo` se usa el prefijo (`ejemplo.mi_variable`) y se tiene acceso a todo el módulo. Con `from ... import` se usa el nombre directo, pero solo está disponible lo que se importó.

> [!question]- ¿Por qué `from modulo import *` se considera mala práctica?
> Porque importa nombres desconocidos que pueden tapar variables o funciones propias, y porque el lector no sabe de dónde viene cada nombre.

> [!question]- ¿Qué valor tiene `__name__` dentro de un módulo importado y dentro del principal?
> En el importado, el nombre del módulo (por ejemplo `"ejemplo2"`); en el principal, `"__main__"`.

> [!question]- ¿Por qué se escribe `if __name__ == "__main__":` en un módulo hecho para importarse?
> Para que el código de prueba dentro del `if` no se ejecute al importarlo y solo corra si el archivo se ejecuta directamente.

