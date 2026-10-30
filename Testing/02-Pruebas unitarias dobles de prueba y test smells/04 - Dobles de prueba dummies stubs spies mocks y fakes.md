---
ramo: "Testing"
tema: "Pruebas unitarias dobles de prueba y test smells"
tags:
  - testing/pruebas-unitarias-dobles-de-prueba-y-test-smells
  - origen/complemento
prerrequisitos:
  - "[[02 - Ciclo de vida en unittest setUp tearDown TestSuite y principios FIRST]]"
  - "[[03 - Encapsulamiento efectos colaterales y pruebas de excepciones]]"
---

# Dobles de prueba, dummies, stubs, spies, mocks y fakes

## Por qué necesitamos dobles de prueba (*Test Doubles*)

En un sistema real, las clases rara vez trabajan solas: un `PlanificadorRiego` consulta un `ServicioClima` por HTTP, un `ShoppingCart` cobra a través de un `PaymentService` bancario, y `Wallet.printInfo` envía texto a un objeto `Printer`. Si al correr nuestras pruebas unitarias llamamos al servidor de clima real o a la pasarela de pagos real, **violamos FIRST de tres formas a la vez**: la prueba se vuelve lenta (*Fast*), puede fallar si se cae internet (*Repeatable*) y modifica sistemas externos (*Independent*).

Un **doble de prueba** (*test double*, término acuñado por Gerard Meszaros en analogía a los dobles de riesgo del cine) es cualquier objeto liviano y controlado que **reemplaza a una dependencia real** con el único propósito de probar nuestra unidad en aislamiento.

---

## Taxonomía de dobles de prueba (Meszaros y Fowler)

| Tipo de doble | ¿Qué hace exactamente? | ¿Cuándo se utiliza? |
| :--- | :--- | :--- |
| **Dummy** | Objeto de relleno que se pasa por parámetro para cumplir con la firma de un método, pero **nunca llega a usarse**. | Cuando probamos `cart.checkout(payment_service)` con el carrito vacío: lanza `ValueError` en la primera línea antes de tocar `payment_service`. |
| **Stub** | Devuelve **respuestas fijas y preprogramadas** a las llamadas que le hace la unidad bajo prueba. | Cuando nuestra unidad necesita **recibir datos** de una dependencia externa (ej. un servicio de clima que siempre retorna $10.0\text{ }^\circ\text{C}$). |
| **Spy** | Es un *stub* que además **graba información** sobre cómo fue llamado (qué argumentos recibió o cuántas veces se invocó) para consultarla después. | Como `RecordingPaymentService`, que guarda `self.received_amount = amount` cuando `checkout` llama a `pay(total)`. |
| **Mock** | Objeto preprogramado con **expectativas de interacción**: verifica que fue llamado con los argumentos exactos, la cantidad de veces y en el orden esperado. | Cuando el objetivo del test es comprobar el **comportamiento de salida** hacia la dependencia (ej. que se llamó `printer.print` $3$ veces en orden). |
| **Fake** | Implementación funcional real pero con atajos que la hacen liviana y no apta para producción. | Una base de datos en memoria (como un diccionario o SQLite `:memory:`) en vez de un servidor PostgreSQL remoto. |

> [!important] La diferencia clave de Martin Fowler: Stub vs. Mock
> * Un **Stub** sirve para la **verificación de estado** (*state verification*): le damos a la unidad entradas indirectas controladas y en el *Assert* verificamos qué valor devolvió la unidad o cómo quedó su estado.
> * Un **Mock** sirve para la **verificación de comportamiento** (*behavior verification*): en el *Assert* no miramos un valor de retorno, sino que interrogamos al propio *mock* para verificar **cómo interactuó** la unidad con él (`call_count`, `assert_called_with`, `assert_has_calls`).

---

## Implementación en Python: clases propias y `unittest.mock`

### 1. Usando `MagicMock` como Stub (`PlanificadorRiego` y `Termostato`)

Cuando `PlanificadorRiego.plan_riego(ciudad)` llama a `self.servicio.pronostico(ciudad)` (que en producción haría un `requests.get` por red), inyectamos un `MagicMock` configurado con `.return_value`:

```python
from unittest.mock import MagicMock, call
import unittest

class PlanificadorRiegoTest(unittest.TestCase):
    def test_riega_en_madrugada_con_ajuste_por_sequia(self):
        # Arrange: configuramos el doble (actúa como Stub) para devolver un pronóstico fijo
        servicio_stub = MagicMock()
        servicio_stub.pronostico.return_value = {
            "temp_max": 36.0, "prob_lluvia": 0.1, "humedad_suelo": 0.2
        }
        planificador = PlanificadorRiego(servicio_stub)
        # Act: ejecutamos sin tocar la red
        plan = planificador.plan_riego("Santiago")
        # Assert: verificación de estado sobre la respuesta calculada (30 L base + 5 L sequía)
        self.assertEqual(
            plan,
            {"regar": True, "litros": 35, "hora": "06:00", "motivo": "riego_programado"}
        )
```

### 2. Usando un Stub manual vs. un Mock con `MagicMock` (`Wallet.printInfo`)

Supongamos que `wallet.printInfo(printer)` ejecuta tres llamadas sucesivas: `printer.print(self.owner_name)`, `printer.print(" ")` y `printer.print(str(self.balance))`.

```python
class WalletPrintTest(unittest.TestCase):
    def test_print_with_mock_verifies_behavior(self):
        mock_printer = MagicMock()
        wallet = WalletV7("juampi")
        wallet.printInfo(mock_printer)

        # Verificación de comportamiento (Mock): cantidad de llamadas y argumentos en orden
        self.assertEqual(mock_printer.print.call_count, 3)
        mock_printer.print.assert_has_calls([call("juampi"), call(" "), call("0")])
```

> [!warning] El límite de los mocks: los mocks pueden mentir
> Un doble de prueba codifica **nuestra suposición** sobre cómo funciona la dependencia externa. Si la API real de `ServicioClima` cambia su diccionario y renombra la llave `"temp_max"` a `"max_temp"`, nuestro test con `MagicMock` seguirá pasando en verde porque el doble sigue entregando `"temp_max"`, mientras que el sistema en producción fallará con `KeyError`. Por eso las pruebas unitarias con mocks siempre deben complementarse con pruebas de integración.

---

---

## Ejemplo práctico: Dummy, Spy y Fake escritos a mano

Probamos un carrito que cobra a través de un servicio de pago. Con clases simples (sin `MagicMock`) se ve con claridad qué hace cada doble:

```python
class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, precio):
        self.items.append(precio)

    def checkout(self, pago):
        if not self.items:
            raise ValueError("carrito vacío")
        total = sum(self.items)
        pago.pay(total)
        return total
```

```python
import unittest

class DummyPago:                        # nunca debería usarse
    def pay(self, amount):
        raise AssertionError("no debe llamarse")

class SpyPago:                          # graba cómo lo llamaron
    def __init__(self):
        self.received_amount = None
        self.calls = 0

    def pay(self, amount):
        self.received_amount = amount
        self.calls += 1

class CarritoTest(unittest.TestCase):
    def test_checkout_vacio_no_toca_el_pago(self):          # Dummy
        with self.assertRaises(ValueError):
            Carrito().checkout(DummyPago())

    def test_checkout_cobra_el_total_una_sola_vez(self):    # Spy
        carrito = Carrito()
        carrito.agregar(1000)
        carrito.agregar(500)
        spy = SpyPago()
        carrito.checkout(spy)
        self.assertEqual(1500, spy.received_amount)
        self.assertEqual(1, spy.calls)
```

Un **Fake** es distinto: tiene lógica real pero simplificada. Por ejemplo, un repositorio en memoria que reemplaza a la base de datos:

```python
class FakeRepo:
    def __init__(self):
        self.data = {}

    def save(self, clave, valor):
        self.data[clave] = valor

    def get(self, clave):
        return self.data[clave]
```

El test guarda y luego lee, comprobando el resultado como si fuera la base real, pero sin red ni disco.

---

## Preguntas de repaso

> [!question]- Una clase `CalculadorEnvio` necesita consultar la tarifa por kilómetro a un `ServicioTarifas` externo para devolver el precio final de un despacho. ¿Qué tipo de test double elegirías para reemplazar a `ServicioTarifas` y por qué?
> Elegiría un **Stub**. La unidad `CalculadorEnvio` necesita recibir un dato de entrada indirecto (la tarifa por kilómetro) desde la dependencia para hacer su cálculo matemático, y nuestro test verificará el precio final retornado por `CalculadorEnvio` (verificación de estado), no cuántas veces internas se llamó al servicio.

> [!question]- En `Wallet.printInfo(printer)`, ¿cuál es la diferencia conceptual entre probar el método pasándole un `PrinterStub` que concatena strings en `self.result` frente a pasarle un `MagicMock` y verificar `assert_has_calls`?
> Con `PrinterStub` hacemos **verificación de estado** (comprobamos el texto final acumulado `"juampi 0"` sin importar si se construyó en una o en tres llamadas a `print`). Con `MagicMock` y `assert_has_calls([call("juampi"), call(" "), call("0")])` hacemos **verificación de comportamiento** (exigimos que la interacción ocurra exactamente en $3$ llamadas con esos argumentos precisos).

> [!question]- ¿Qué significa la frase «los mocks pueden mentir» y qué riesgo introduce abusar de ellos (*over-mocking*)?
> Significa que un *mock* o *stub* no ejecuta el código real de la dependencia, sino lo que el programador le programó en `return_value`. Si el contrato real del colaborador cambia (por ejemplo, cambia el formato del JSON o lanza una excepción nueva), los tests unitarios con mocks seguirán pasando en verde validando una fantasía que ya no coincide con la realidad.

> [!question]- ¿Cuál es la diferencia práctica entre un Spy escrito a mano (`SpyPago`) y un `MagicMock`?
> Ambos registran cómo fueron llamados. El Spy manual es una clase explícita cuyo registro (`received_amount`, `calls`) se consulta con asserts normales; el `MagicMock` genera ese registro automáticamente y ofrece métodos como `assert_called_once_with`. Con `MagicMock` se escribe menos código, pero el Spy manual deja el comportamiento más visible y legible.

> [!question]- Para cada caso elige el doble: (a) un `ServicioHora` que siempre debe devolver las 10:00; (b) verificar que se llamó a `notificar()` exactamente dos veces; (c) una base de datos en memoria. 
> (a) **Stub**: respuesta fija preprogramada. (b) **Mock** (o Spy): verificación de comportamiento sobre cuántas veces se llamó. (c) **Fake**: implementación funcional liviana, no apta para producción.
