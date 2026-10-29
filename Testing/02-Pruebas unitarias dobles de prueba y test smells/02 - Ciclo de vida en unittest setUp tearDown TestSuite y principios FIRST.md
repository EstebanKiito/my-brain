---
ramo: "Testing"
tema: "Pruebas unitarias dobles de prueba y test smells"
tags:
  - testing/pruebas-unitarias-dobles-de-prueba-y-test-smells
  - origen/complemento
prerrequisitos:
  - "[[01 - Estado e invariante de objetos y estructura Arrange Act Assert]]"
---

# Ciclo de vida en unittest, setUp, tearDown, TestSuite y principios FIRST

## Cómo ejecuta pruebas `unittest`: `TestLoader`, `TestSuite` y `TestRunner`

Cuando ejecutamos una clase de prueba en `unittest` (ya sea con `unittest.main()` en consola o con una función auxiliar `runTests` dentro de un notebook de Jupyter), ocurren tres pasos internos fundamentales:

![Ejecución de una clase de prueba mediante TestLoader, TestSuite y TextTestRunner](adjuntos/Ejecución%20de%20TestSuite%20y%20TestRunner%20en%20unittest.png)

1. **`TestLoader`:** inspecciona la clase `WalletTest` y descubre todos los métodos cuyo nombre empieza con `test_`.
2. **`TestSuite`:** construye una colección de **instancias separadas** de la clase de prueba. Si `WalletTest` define $3$ métodos `test_...`, la suite contiene **$3$ objetos `WalletTest` distintos**, uno para cada método.
3. **`TestRunner`:** recorre la suite y ejecuta cada método en su propia instancia independiente, para evitar que los atributos modificados por un test contaminen al siguiente.

---

## Compartir configuración: `setUp` y `tearDown`

Cuando varios tests de una misma clase repiten exactamente las mismas líneas de preparación (*Arrange*), duplicar ese código en cada método dificulta el mantenimiento. `unittest.TestCase` provee dos métodos de ciclo de vida (similares a los vistos en [[Ingeniería de Software/06-Testing/08 - Setup y teardown en tests|Setup y teardown en tests]]):

* **`setUp(self)`:** se ejecuta automáticamente **antes de cada método de prueba** para preparar un estado inicial fresco y limpio.
* **`tearDown(self)`:** se ejecuta automáticamente **después de cada método de prueba** (incluso si el test falló o lanzó una excepción) para liberar recursos externos, cerrar archivos o limpiar conexiones.

```python
class WalletTest(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet("Javier")
        self.wallet.deposit(100)

    def test_deposit(self):
        self.wallet.deposit(50)
        self.assertEqual(150, self.wallet.total_balance())

    def test_withdraw(self):
        self.wallet.withdraw(30)
        self.assertEqual(70, self.wallet.total_balance())
```

> [!important] El orden exacto de ejecución (pregunta clásica de evaluación)
> `setUp` y `tearDown` **no** se ejecutan una sola vez al principio y al final de la clase, sino que **envuelven individualmente a cada test**. Además, `tearDown` se invoca siempre aunque no lo hayas sobrescrito en tu subclase (porque hereda la implementación vacía de `unittest.TestCase`). Para la clase anterior con dos pruebas, la traza exacta de ejecución es:
> $$\texttt{setUp} \longrightarrow \texttt{test\_deposit} \longrightarrow \texttt{tearDown} \longrightarrow \texttt{setUp} \longrightarrow \texttt{test\_withdraw} \longrightarrow \texttt{tearDown}$$
> Gracias a esto, cuando arranca `test_withdraw`, `self.wallet` es una billetera recién creada con $\$100$, y no una billetera que arrastró los $\$150$ dejados por `test_deposit`.

---

## Criterios de calidad de las pruebas: principios FIRST

Que una suite pase en verde no significa que sea una buena suite. Robert C. Martin sintetizó en el acrónimo **FIRST** las cinco propiedades que debe cumplir toda prueba unitaria de calidad:

| Letra | Principio | Qué exige en la práctica | Ejemplo de violación |
| :---: | :--- | :--- | :--- |
| **F** | **Fast** (Rápida) | Debe ejecutarse en milisegundos para que el equipo la corra constantemente. | Abrir una conexión por red a una base de datos PostgreSQL remota en cada test. |
| **I** | **Independent** (Independiente) | Ningún test debe depender de que otro test haya corrido antes ni del orden de ejecución. | `test_a` inserta un registro en una variable global o tabla compartida y `test_b` asume que ese registro ya existe. |
| **R** | **Repeatable** (Repetible) | Debe producir siempre el mismo resultado determinista en cualquier máquina y a cualquier hora. | Usar `if time.localtime().tm_hour < 12:` o `random.random()` sin semilla fija ni *mock* del reloj. |
| **S** | **Self-validating** (Autovalidable) | Debe reportar `pasa` o `falla` automáticamente mediante `assert`, sin inspección humana. | Imprimir el resultado con `print()` y esperar que el programador lea la consola «a ojo». |
| **T** | **Timely** (Oportuna) | Debe escribirse junto con el código de producción (o justo antes, como en *Test-Driven Development*). | Intentar escribir pruebas unitarias seis meses después para un módulo gigante altamente acoplado. |

---

## Preguntas de repaso

> [!question]- En una clase `WalletTest` con tres métodos (`test_a`, `test_b` y `test_c`), ¿cuántas instancias de `WalletTest` crea `unittest.TestLoader` dentro de la `TestSuite` y cuántas veces en total se ejecuta `setUp()`?
> `TestLoader` crea **$3$ instancias distintas** de `WalletTest` (una por cada método `test_...`), y `setUp()` se ejecuta **$3$ veces** en total (una vez inmediatamente antes de cada método de prueba).

> [!question]- Un compañero tiene dos tests: `test_1_crear_usuario` guarda un usuario en una lista global del módulo, y `test_2_borrar_usuario` borra ese usuario asumiendo que `test_1` ya corrió. Cuando `test_2` falla al correrlo solo, propone renombrarlos para forzar el orden alfabético. ¿Por qué es un antipatrón y cómo se corrige?
> Viola directamente el principio **Independent** de FIRST. Si los tests dependen del orden de ejecución, no se pueden ejecutar de forma aislada al depurar un fallo ni paralelizar, y un fallo en `test_1` provoca fallos en cascada en pruebas cuyos métodos bajo prueba estaban sanos. El arreglo correcto es eliminar el estado global compartido y que cada test prepare su propio estado independiente (por ejemplo, dentro de `setUp`).

> [!question]- Analiza un test que se conecta a `postgresql://prod-server:5432/orders`, inserta dos órdenes y luego ejecuta `if time.localtime().tm_hour < 12: assert orders[0].discount == 0.1`. ¿Qué principios de FIRST viola?
> Viola tres principios simultáneamente:
> 1. **Fast:** la conexión por red a un servidor PostgreSQL introduce latencia de entrada/salida.
> 2. **Independent:** al escribir en una base de datos compartida de producción, ensucia el estado para otras pruebas o ejecuciones concurrentes.
> 3. **Repeatable:** el resultado depende de la hora del reloj del sistema (`tm_hour < 12`), por lo que el mismo código puede pasar a las 10:00 AM y fallar a las 3:00 PM.
