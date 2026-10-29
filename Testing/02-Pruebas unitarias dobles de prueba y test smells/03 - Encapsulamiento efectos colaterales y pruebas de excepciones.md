---
ramo: "Testing"
tema: "Pruebas unitarias dobles de prueba y test smells"
tags:
  - testing/pruebas-unitarias-dobles-de-prueba-y-test-smells
  - origen/complemento
prerrequisitos:
  - "[[01 - Estado e invariante de objetos y estructura Arrange Act Assert]]"
  - "[[02 - Ciclo de vida en unittest setUp tearDown TestSuite y principios FIRST]]"
---

# Encapsulamiento, efectos colaterales y pruebas de excepciones

## El dilema entre encapsulamiento y verificabilidad

En programación orientada a objetos, el **encapsulamiento** nos enseña a ocultar los atributos internos de una clase y exponer únicamente las operaciones públicas estrictamente necesarias para minimizar el acoplamiento. Sin embargo, al escribir pruebas unitarias aparece una tensión natural: **para verificar en la fase *Assert* que un método dejó al objeto en el estado correcto, necesitamos observar ese estado**.

¿Cómo resolvemos este dilema sin destruir el diseño de la clase? Seguimos este orden de prioridad:

1. **Probar a través de la interfaz pública (comportamiento observable):** verificar el efecto mediante métodos públicos de consulta ya existentes (como `wallet.total_balance()`).
2. **Separar la lógica de formato o cálculo del efecto colateral:** si un método hace un cálculo pero solo lo imprime en consola con `print()`, extraemos un método puro que retorne el valor calculado (por ejemplo, `printString()` que devuelve `"juampi 0"`) y probamos ese retorno con `assertEqual`.
3. **Regla de oro:** *prueba el comportamiento público, no los detalles de implementación interna*. Si tus tests inspeccionan directamente atributos privados que luego cambian de estructura en un refactor (por ejemplo, pasar de guardar una lista a un diccionario), todos tus tests se romperán aunque la clase siga funcionando exactamente igual hacia afuera.

---

## Cómo diseñar y probar escenarios de error

Consideremos el método `withdraw(amount)` de nuestra billetera `Wallet` cuando el usuario intenta retirar más dinero del disponible (`amount > self.balance`):

```python
def withdraw(self, amount):
    if amount <= self.balance:
        self.balance -= amount
    else:
        print("Not enough minerals")
```

Si cuando falta dinero el método únicamente ejecuta `print("Not enough minerals")` y no devuelve nada, **es muy difícil de testear unitariamente**, porque el texto se pierde en la salida estándar y la llamada parece haber tenido éxito. En clases estudiamos tres evoluciones de diseño para volver verificables los escenarios de error:

### Alternativa 1: Retornar una bandera booleana (*Flag*)

Modificamos `withdraw` para que devuelva `True` si el retiro se realizó y `False` si fue rechazado. Así la prueba unitaria puede capturar el retorno y usar `self.assertFalse(wallet.withdraw(110))`. Es simple, pero limita al método si además necesitara devolver otro valor útil.

### Alternativa 2: Lanzar excepciones (*Exceptions*)

Un diseño mucho más expresivo en Python consiste en lanzar una excepción semántica cuando se viola una precondición (por ejemplo, `raise ValueError("Amount must be positive")` o una excepción de dominio como `raise InsufficientStockError("Cannot remove more items than available")`). Esto permite distinguir múltiples causas de error y deja libre el valor de retorno para el caso exitoso.

---

## Cómo verificar excepciones en `unittest`

Una vez que nuestro método lanza una excepción ante entradas inválidas, existen tres formas de escribir el test en `unittest`, pero **solo una es la recomendada en la práctica moderna**:

### 1. Con el administrador de contexto `with self.assertRaises(...)` (Recomendado)

Es la forma estándar, clara y segura utilizada en suites profesionales (como vimos en `TestShoppingCart`):

```python
class InsufficientStockError(Exception):
    pass

class TestShoppingCart(unittest.TestCase):
    def test_remove_more_than_available_raises_error(self):
        cart = ShoppingCart()
        cart.add_item("apple", price=1.5, quantity=2)
        # El bloque with pasa SI Y SOLO SI dentro de él se lanza InsufficientStockError
        with self.assertRaises(InsufficientStockError):
            cart.remove_item("apple", quantity=3)
```

Si `cart.remove_item("apple", 3)` lanza `InsufficientStockError`, `assertRaises` la atrapa y el test **pasa**. Si no lanza ninguna excepción (o lanza una excepción de otro tipo, como `KeyError`), el test **falla** inmediatamente.

### 2. Con bloques `try / except` manuales (Verbo y propenso a olvidos)

En las láminas se muestra el patrón manual: llamar al método dentro de un `try:`, poner `self.assertFalse(True)` (o `self.fail()`) en la línea siguiente por si no lanzó excepción, y poner `self.assertFalse(False)` en el `except:`. Aunque funciona, es verboso y un `except:` desnudo atrapa cualquier error accidental (incluso un `NameError` por escribir mal el nombre de una variable), dando falsos positivos.

### 3. Con el decorador `@unittest.expectedFailure` (Cuidado con su semántica)

En `unittest` existe el decorador `@unittest.expectedFailure` sobre un método `test_...`. Si el método termina con un error o excepción no capturada, el *runner* lo marca como *«expected failure»* (`x`) en lugar de romper la corrida. Sin embargo, para verificar que una función valida correctamente sus entradas es preferible `with self.assertRaises(TipoEspecifico):`, porque verifica exactamente **en qué línea** y **qué clase de excepción** ocurrió.

---

## Preguntas de repaso

> [!question]- ¿Por qué un método que ante un error solo ejecuta `print("Error")` sin retornar nada ni lanzar excepciones dificulta el testing unitario?
> Porque `print()` envía texto a la salida estándar (`sys.stdout`) como un efecto colateral externo sin dejar rastro en el valor de retorno del método. El test no tiene qué pasarle a `self.assertEqual` a menos que intercepte la consola global o refactorice la clase para retornar un valor/lanzar una excepción.

> [!question]- ¿Qué peligro tiene probar una excepción usando un bloque `try: ... except: self.assertTrue(True)` sin especificar el tipo de excepción en el `except`?
> Un `except:` genérico captura **cualquier** excepción de Python, incluyendo errores de programación dentro del propio test como `TypeError` (pasar mal el número de argumentos) o `AttributeError` (escribir mal el nombre del método). El test pasaría en verde creyendo que probó la regla de negocio cuando en realidad ni siquiera llegó a ejecutar el método correctamente.

> [!question]- ¿Qué ocurre exactamente cuando se ejecuta un bloque `with self.assertRaises(ValueError):` si el código dentro del bloque termina normalmente sin lanzar ninguna excepción?
> Al salir del bloque `with`, el administrador de contexto de `assertRaises` detecta que no se lanzó `ValueError` y lanza internamente un `AssertionError("ValueError not raised")`, haciendo que la prueba unitaria **falle**.
