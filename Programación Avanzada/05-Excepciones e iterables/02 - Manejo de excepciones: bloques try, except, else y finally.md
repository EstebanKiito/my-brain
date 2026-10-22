---
ramo: "Programación Avanzada"
tema: "Excepciones e iterables"
tags:
  - programacion/excepciones
  - programacion/control-de-flujo
  - origen/complemento
prerrequisitos:
  - "[[01 - Excepciones: errores en tiempo de ejecución y tipos comunes]]"
---

# Manejo de excepciones: bloques try, except, else y finally

En lugar de permitir que un fallo inesperado colapse el programa frente al usuario final, los lenguajes modernos ofrecen mecanismos de control defensivo para interceptar los errores, subsanarlos o informar de forma amigable qué ocurrió.

## Estructura básica: try y except

Para proteger una sección de código propensa a errores, se coloca dentro de un bloque **`try`**. Si dentro del bloque ocurre una excepción, la ejecución del bloque se interrumpe y salta de inmediato al bloque **`except`** correspondiente:

```python
def dividir(dividendo: float, divisor: float):
    try:
        resultado = dividendo / divisor
        print(f"El resultado es: {resultado}")
    except ZeroDivisionError as error:
        print(f"No es posible dividir por cero ({error}).")


dividir(10, 2)
dividir(10, 0)
```

```
El resultado es: 5.0
No es posible dividir por cero (division by zero).
```

> [!warning] Prohibido el except desnudo
> Escribir `except:` a secas (sin especificar la clase de excepción) es un grave antipatrón: atrapa incluso errores de tipeo, fallos de memoria e interrupciones del teclado (`KeyboardInterrupt`). Siempre debes capturar **excepciones específicas**.

## Manejo de múltiples excepciones

Una misma operación puede fallar por distintas razones. Python permite encadenar varios bloques `except` o agruparlos en una tupla:

```python
def procesar_elemento(lista: list, indice: int, divisor: int):
    try:
        valor = lista[indice]
        return valor / divisor
    except IndexError:
        print(f"Error: El índice {indice} no existe en la lista.")
    except ZeroDivisionError:
        print("Error: No se puede dividir el elemento por cero.")
    except (TypeError, ValueError) as e:
        print(f"Error de tipo o valor: {e}")


numeros = [10, 20, 30]
procesar_elemento(numeros, 5, 2)   # Dispara IndexError
procesar_elemento(numeros, 0, 0)   # Dispara ZeroDivisionError
```

```
Error: El índice 5 no existe en la lista.
Error: No se puede dividir el elemento por cero.
```

## Flujos complementarios: else y finally

Para estructurar la lógica con precisión profesional, la sentencia `try` admite dos cláusulas opcionales adicionales:

- **`else`:** se ejecuta **únicamente si no ocurrió ninguna excepción** dentro del bloque `try`. Permite mantener el bloque `try` lo más corto posible, reservándolo solo a las líneas que realmente pueden fallar.
- **`finally`:** se ejecuta **siempre**, sin importar si hubo excepción, si fue capturada o si se ejecutó un `return`. Su propósito primordial es la **liberación de recursos** (cerrar archivos, desconectar bases de datos o liberar candados).

```python
def abrir_y_leer_lineas(ruta: str):
    archivo = None
    try:
        archivo = open(ruta, "r", encoding="utf-8")
        contenido = archivo.read()
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")
    else:
        print(f"Archivo leído exitosamente ({len(contenido)} caracteres).")
    finally:
        if archivo:
            archivo.close()
            print("Recurso de archivo cerrado limpiamente.")


abrir_y_leer_lineas("archivo_inexistente.txt")
```

```
No se encontró el archivo: archivo_inexistente.txt
```

> [!tip] La regla de oro del bloque try
> Limita el código dentro de `try` al mínimo indispensable. Cuanto más código coloques en `try`, mayor es el riesgo de capturar accidentalmente una excepción provocada por otra línea que no era la que pretendías proteger.

## Preguntas de repaso

> [!question]- ¿Por qué no se debe utilizar una cláusula `except:` sin indicar el tipo de error?
> Porque intercepta indiscriminadamente cualquier error del sistema (incluyendo interrupciones del teclado con Ctrl+C y errores de nombres de variables), ocultando fallas de programación reales y haciendo imposible la depuración.

> [!question]- ¿Bajo qué condición específica se ejecuta el bloque `else` asociado a un `try-except`?
> Se ejecuta única y exclusivamente cuando el bloque `try` finaliza su ejecución de manera completamente exitosa, sin haber levantado ninguna excepción.

> [!question]- ¿Se ejecuta el bloque `finally` si dentro del bloque `try` o `except` se encuentra una instrucción `return`?
> Sí. El intérprete de Python garantiza que el bloque `finally` se ejecutará justo antes de que el `return` entregue el control y retorne el valor de la función.

> [!question]- ¿Cuál es el orden cronológico estricto de evaluación de una estructura `try-except-else-finally`?
> Primero se ejecuta `try`; si ocurre un error va a `except`; si no hay error va a `else`; y finalmente, en todos los casos y sin excepción, concluye ejecutando `finally`.

