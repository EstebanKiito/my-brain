---
ramo: "Testing"
tema: "Pruebas unitarias dobles de prueba y test smells"
tags:
  - testing/pruebas-unitarias-dobles-de-prueba-y-test-smells
  - origen/complemento
prerrequisitos:
  - "[[Testing/01-Fundamentos del testing de software/01 - Qué es el testing error defecto falla y el oráculo de prueba|Qué es el testing error defecto falla y el oráculo de prueba]]"
  - "[[Programación Avanzada/01-Repaso y POO básica/06 - Clases, objetos y variables de clase|Clases, objetos y variables de clase]]"
---

# Estado e invariante de objetos y estructura Arrange Act Assert

## Por qué probar una unidad en aislamiento

Como escribió Kent Beck: *«Escribe pruebas hasta que el miedo se transforme en aburrimiento»*. En la base de la pirámide de testing están las **pruebas unitarias**: pequeños programas automatizados que verifican que una **unidad** (una función, un método o una clase) se comporta exactamente según sus requerimientos en completo aislamiento del resto del sistema.

El valor principal de probar una unidad pequeña y aislada es su **precisión quirúrgica de diagnóstico**: si falla el test unitario de `withdraw()`, sabemos de inmediato que el defecto está en `withdraw()`, sin tener que rastrear una falla difusa a través de veinte servicios conectados.

---

## Vocabulario orientado a objetos bajo prueba

Al probar una clase (**Class Under Test**, o **CUT**) necesitamos distinguir cuatro conceptos fundamentales sobre el ciclo de vida de sus instancias:

![Definiciones de estado de objeto, invariante, getter y encapsulamiento sobre la clase Wallet](adjuntos/Definiciones%20de%20estado%20e%20invariante%20en%20Wallet.png)

* **Estado de un objeto (*Object State*):** el conjunto de valores actuales almacenados en los atributos de una instancia en un instante dado (por ejemplo, `self.balance == 50` y `self.owner_name == "Lili"`).
* **Invariante de objeto (*Object Invariant*):** la condición lógica que debe cumplirse **siempre** antes y después de ejecutar cualquier método público para que el objeto se considere en un estado consistente y válido. En una billetera sin sobregiro (`Wallet`), el invariante es $\text{balance} \ge 0$; si después de una operación `self.balance` quedara en $-10$, el objeto habría violado su invariante y entrado en un estado corrupto.
* **Getter (método de consulta):** método público que devuelve el valor de un atributo o una proyección del estado interno (como `total_balance()`).
* **Encapsulamiento:** el grado de ocultamiento de los atributos y métodos internos de una clase (público, protegido o privado) para reducir el acoplamiento con el resto del programa.

---

## Anatomía de una prueba unitaria: Arrange–Act–Assert (AAA)

En Python utilizamos el módulo estándar `unittest`. Toda prueba unitaria bien estructurada divide su cuerpo en tres fases explícitas conocidas como el patrón **Arrange–Act–Assert (AAA)** (Roy Osherove):

![Comparación entre la clase bajo prueba Wallet y su clase de prueba WalletTest en unittest](adjuntos/Clase%20bajo%20prueba%20frente%20a%20clase%20de%20test%20en%20unittest.png)

1. **Arrange (Preparar / *Setup*):** construye los objetos necesarios, define los datos de entrada y deja el sistema en el estado inicial requerido por el escenario.
2. **Act (Actuar / *Stimulus*):** invoca la operación o método específico que queremos poner a prueba.
3. **Assert (Verificar):** evalúa el **oráculo de prueba** comparando el valor retornado o el nuevo estado del objeto contra el resultado esperado mediante métodos de `unittest.TestCase` como `self.assertEqual(esperado, real)`, `self.assertTrue(...)` o `self.assertIn(...)`.

```python
import unittest

class Wallet:
    def __init__(self, owner):
        self.balance = 0
        self.owner_name = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money")

    def total_balance(self):
        return self.balance

class WalletTest(unittest.TestCase):
    def test_deposit_increases_balance(self):
        # 1. Arrange: creamos una billetera con saldo inicial 0
        wallet = Wallet("Lili")
        # 2. Act: depositamos 20 unidades
        wallet.deposit(20)
        # 3. Assert: el oráculo verifica que el saldo final sea 20
        self.assertEqual(20, wallet.total_balance())
```

> [!tip] Por qué separar claramente las tres fases
> Mantener un único bloque *Arrange*, una acción *Act* clara y su bloque *Assert* al final evita mezclar múltiples escenarios inconexos dentro del mismo método `test_...`. Cuando una prueba con estructura AAA falla, basta leer las tres líneas para saber qué estado había antes, qué método se llamó y qué expectativa se incumplió.

---

## Preguntas de repaso

> [!question]- ¿Qué es el invariante de un objeto (*Object Invariant*) y cómo se diferencia del estado de un objeto (*Object State*)?
> El **estado de un objeto** son los valores concretos que tienen sus atributos en un momento puntual (por ejemplo, `balance = 100`), los cuales cambian a medida que el programa corre. El **invariante de un objeto** es la regla o predicado de consistencia que todo estado válido debe respetar en todo momento (por ejemplo, `balance >= 0` y `owner_name != ""`).

> [!question]- En el patrón Arrange–Act–Assert, ¿cuál de las tres etapas materializa el concepto teórico de «oráculo de prueba» visto en el Tema 01?
> La etapa **Assert**. Mientras que *Arrange* prepara la entrada $d$ y el estado previo, y *Act* calcula $P(d)$, la aserción (`self.assertEqual(esperado, real)`) es la que contrasta el resultado observado contra el valor esperado independiente y emite el veredicto booleano $\in \{\text{pasa}, \text{falla}\}$.

> [!question]- ¿Por qué todos los métodos de prueba en una clase que hereda de `unittest.TestCase` deben comenzar obligatoriamente con el prefijo `test_`?
> Porque el recolector automático de pruebas (`unittest.TestLoader`) inspecciona la clase buscando métodos cuyo nombre empiece por `test_` para distinguirlos de métodos auxiliares o de configuración. Si escribes `def check_deposit(self):` sin el prefijo `test_`, el *runner* lo ignorará silenciosamente y nunca se ejecutará.
