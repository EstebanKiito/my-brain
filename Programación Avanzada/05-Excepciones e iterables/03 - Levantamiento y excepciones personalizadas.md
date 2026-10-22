---
ramo: "Programación Avanzada"
tema: "Excepciones e iterables"
tags:
  - programacion/excepciones
  - programacion/poo
  - origen/complemento
prerrequisitos:
  - "[[02 - Manejo de excepciones: bloques try, except, else y finally]]"
  - "[[01 - Herencia y especialización de clases]]"
---

# Levantamiento y excepciones personalizadas

Así como Python detecta cuando intentamos dividir por cero, nuestro propio código debe ser capaz de señalar cuando se vulneran las reglas del dominio de la aplicación: transferir más dinero del disponible, registrar un usuario menor de edad o cargar un formato corrupto.

## La instrucción raise

La palabra clave **`raise`** interrumpe intencionalmente el flujo normal del programa y lanza una excepción:

```python
def registrar_edad(edad: int):
    if not isinstance(edad, int):
        raise TypeError(f"La edad debe ser un número entero, no {type(edad).__name__}.")
    if edad < 0:
        raise ValueError(f"La edad no puede ser negativa ({edad}).")
    print(f"Edad registrada correctamente: {edad}")


registrar_edad(21)
# registrar_edad(-5)  # Levanta ValueError: La edad no puede ser negativa (-5).
```

```
Edad registrada correctamente: 21
```

## Jerarquía de excepciones en Python

En Python todas las excepciones son clases organizadas en un árbol de herencia cuya raíz común es **`BaseException`**:

![Jerarquía de excepciones en Python](adjuntos/Jerarqu%C3%ADa%20de%20excepciones%20en%20Python.png)

> [!example]- Transcripción de la imagen
> - Árbol genealógico de excepciones de Python:
>   - En la cima: `BaseException`.
>   - Subclases de sistema: `SystemExit`, `KeyboardInterrupt`, `GeneratorExit`.
>   - Rama principal: `Exception`, de la cual derivan `ArithmeticError` (que agrupa `ZeroDivisionError`), `LookupError` (que agrupa `IndexError` y `KeyError`), `ValueError`, `TypeError` y las excepciones de usuario.

### Captura polimórfica por clase padre

Al capturar una superclase en un bloque `except`, Python intercepta automáticamente a todas sus subclases:

```python
try:
    diccionario = {"a": 1}
    valor = diccionario["b"]
except LookupError as e:
    # LookupError captura tanto KeyError como IndexError
    print(f"Error de búsqueda capturado: {type(e).__name__}")
```

```
Error de búsqueda capturado: KeyError
```

## Creación de excepciones personalizadas

Para modelar errores de negocio con claridad, podemos crear nuestras propias clases de error. La regla fundamental es **heredar siempre de `Exception`**:

```python
class SaldoInsuficienteError(Exception):
    """Excepción lanzada cuando una cuenta no tiene fondos suficientes."""
    def __init__(self, saldo_actual: float, monto_solicitado: float):
        self.saldo_actual = saldo_actual
        self.monto_solicitado = monto_solicitado
        mensaje = (
            f"Fondos insuficientes: intentó retirar ${monto_solicitado:.2f}, "
            f"pero el saldo actual es solo ${saldo_actual:.2f}."
        )
        super().__init__(mensaje)


def retirar(saldo: float, monto: float) -> float:
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto


try:
    retirar(500.0, 1200.0)
except SaldoInsuficienteError as error:
    print(error)
    print(f"Déficit: ${error.monto_solicitado - error.saldo_actual:.2f}")
```

```
Fondos insuficientes: intentó retirar $1200.00, pero el saldo actual es solo $500.00.
Déficit: $700.00
```

> [!tip] Excepciones personalizadas con atributos
> Almacenar datos en los atributos de la excepción (`error.saldo_actual`, `error.monto_solicitado`) permite que el código que la capture tome decisiones informadas (como ofrecer un crédito o notificar al usuario) sin tener que analizar el texto del mensaje.

> [!warning] Nunca heredar directamente de BaseException
> Si una clase de excepción hereda de `BaseException` en lugar de `Exception`, un bloque estándar `except Exception:` no podrá capturarla, dificultando su manejo en capas superiores del sistema.

## Preguntas de repaso

> [!question]- ¿Qué ocurre cuando se ejecuta la instrucción `raise` en una función y nadie la captura con `try-except`?
> La ejecución de la función se interrumpe de inmediato y la excepción se propaga hacia arriba en la pila de llamadas (*call stack*) hasta que algún bloque la capture o el programa termine con un traceback en la consola.

> [!question]- ¿Por qué un bloque `except LookupError:` es capaz de capturar tanto un `IndexError` como un `KeyError`?
> Porque en la jerarquía de clases de Python, tanto `IndexError` como `KeyError` son subclases directas de `LookupError`, cumpliendo con la relación polimórfica de herencia.

> [!question]- ¿Por qué las excepciones personalizadas deben heredar de `Exception` y no de `BaseException`?
> Porque `BaseException` está reservada para señales críticas del sistema (`KeyboardInterrupt`, `SystemExit`) que no deben ser atrapadas por bloques generales de manejo de errores de aplicación.

> [!question]- ¿Cómo se puede re-lanzar una excepción capturada para que siga propagándose hacia capas superiores?
> Se escribe la instrucción `raise` en solitario (sin argumentos) dentro del bloque `except`, lo que vuelve a lanzar exactamente la misma excepción capturada conservando su traceback original.

