---
ramo: "Programación Avanzada"
tema: "Excepciones e iterables"
tags:
  - programacion/excepciones
  - programacion/control-de-flujo
  - origen/complemento
prerrequisitos:
  - "[[01 - Repaso de Python: tipos, funciones y módulos]]"
---

# Excepciones: errores en tiempo de ejecución y tipos comunes

Incluso cuando un programa no tiene errores ortográficos ni faltas de sintaxis, pueden surgir situaciones imprevistas al ejecutarse: un archivo que no existe en el disco, una división por cero o un usuario que introduce una letra cuando se esperaba un número entero.

## Errores sintácticos vs Excepciones

En Python los problemas de código se dividen en dos categorías fundamentales:

1. **Errores de sintaxis (*SyntaxError*):** se detectan antes de ejecutar cualquier instrucción, durante la fase de análisis del código (*parsing*). Ocurren por escribir mal una instrucción, olvidar dos puntos (`:`) o tener problemas de indentación (*IndentationError*). El programa ni siquiera comienza a correr.
2. **Excepciones en tiempo de ejecución (*exceptions*):** ocurren mientras el programa ya se encuentra corriendo. La sintaxis es válida, pero una operación no puede completarse de manera exitosa. Si no se manejan, detienen el programa de inmediato.

## Lectura de la traza de error (traceback)

Cuando una excepción no es capturada, Python imprime un reporte llamado **traceback** (o traza de la pila). Debe leerse de **abajo hacia arriba**:

- **Última línea:** indica el **tipo de excepción** y una descripción específica del motivo de la falla.
- **Líneas anteriores:** muestran la ruta de llamadas de funciones desde donde se originó el error hasta llegar al archivo y número de línea exacto donde ocurrió.

```python
def calcular_promedio(numeros: list) -> float:
    return sum(numeros) / len(numeros)

# Si la lista está vacía, len(numeros) es 0 y se genera una excepción:
# calcular_promedio([])  # ZeroDivisionError: division by zero
```

## Catálogo de excepciones comunes en Python

Python incluye decenas de excepciones estándar predefinidas. Las más habituales en el desarrollo cotidiano son:

| Tipo de excepción | Causa común | Ejemplo típico |
|---|---|---|
| **`ZeroDivisionError`** | División o módulo por cero | `10 / 0` |
| **`IndexError`** | Acceso a un índice fuera del rango de una secuencia | `lista[10]` cuando `len(lista) == 3` |
| **`KeyError`** | Consulta directa de una llave inexistente en un diccionario | `monedas["Argentina"]` |
| **`AttributeError`** | Intentar acceder a un atributo o método que el objeto no posee | `"hola".append("!")` |
| **`TypeError`** | Aplicar una operación sobre un tipo de dato incompatible | `"texto" + 5` |
| **`ValueError`** | Tipo correcto pero valor inapropiado | `int("veinte")` |
| **`FileNotFoundError`** | Intentar abrir un archivo que no existe en esa ruta | `open("no_existe.txt", "r")` |

```python
# Ejemplo de TypeError vs ValueError
try:
    numero = int("palabra")
except ValueError as e:
    print(f"Capturado ValueError: {e}")

try:
    resultado = "Longitud: " + len([1, 2, 3])
except TypeError as e:
    print(f"Capturado TypeError: {e}")
```

```
Capturado ValueError: invalid literal for int() with base 10: 'palabra'
Capturado TypeError: can only concatenate str (not "int") to str
```

> [!tip] TypeError vs ValueError
> Usa esta regla nemotécnica: `TypeError` significa "este objeto no admite esta operación en absoluto" (sumar string con entero); `ValueError` significa "el tipo es aceptable pero este valor específico no tiene sentido" (`int("42")` funciona, pero `int("abc")` falla).

> [!warning] Las excepciones detienen la ejecución inmediatamente
> Cuando ocurre una excepción no capturada en la línea 15 de una función, ninguna de las líneas siguientes (16, 17, etc.) se llegará a ejecutar. Por eso es indispensable prever y capturar las fallas esperadas.

## Preguntas de repaso

> [!question]- ¿Por qué un SyntaxError detiene el programa antes de que comience a ejecutarse cualquier línea?
> Porque el intérprete de Python debe analizar léxica y gramaticalmente todo el archivo para generar el *bytecode*; si encuentra una regla de lenguaje violada, aborta la compilación antes de iniciar el entorno de ejecución.

> [!question]- ¿Cómo debe leerse un traceback impreso en la terminal ante un error?
> Debe leerse de abajo hacia arriba: la última línea revela el nombre exacto de la excepción y el mensaje de error, mientras que las líneas superiores permiten rastrear la cadena de llamadas hasta la línea que originó la falla.

> [!question]- ¿Cuál es la diferencia entre un `IndexError` y un `KeyError`?
> `IndexError` ocurre al intentar acceder por una posición numérica entera inexistente en una estructura secuencial (como una lista o tupla), mientras que `KeyError` ocurre al consultar una clave inexistente en una estructura asociativa (como un diccionario).

> [!question]- ¿Qué excepción se produce al intentar ejecutar `int([1, 2, 3])` frente a `int("10.5")`?
> `int([1, 2, 3])` produce un `TypeError` porque `int()` no acepta listas como argumento; mientras que `int("10.5")` produce un `ValueError` porque acepta cadenas de texto pero esa cadena contiene caracteres incompatibles con una representación entera.
