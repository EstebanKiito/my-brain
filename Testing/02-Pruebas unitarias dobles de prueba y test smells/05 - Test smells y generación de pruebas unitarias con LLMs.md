---
ramo: "Testing"
tema: "Pruebas unitarias dobles de prueba y test smells"
tags:
  - testing/pruebas-unitarias-dobles-de-prueba-y-test-smells
  - origen/complemento
prerrequisitos:
  - "[[02 - Ciclo de vida en unittest setUp tearDown TestSuite y principios FIRST]]"
  - "[[04 - Dobles de prueba dummies stubs spies mocks y fakes]]"
---

# Test smells y generación de pruebas unitarias con LLMs

## ¿Qué es un *Test Smell*?

Así como en el código de producción existen *code smells* (síntomas de mal diseño que dificultan el mantenimiento), en el código de pruebas existen **test smells**: malas prácticas al estructurar o escribir tests unitarios que los vuelven frágiles, difíciles de diagnosticar cuando fallan o poco confiables, aun cuando hoy pasen en verde.

---

## Catálogo de *Test Smells* fundamentales

### 1. *Indirect Testing* (Prueba indirecta)

Ocurre cuando una clase de prueba dice testear a la clase `Bank`, pero su aserción termina inspeccionando los objetos internos de otra clase (`self.assertEqual(100, bank.wallet.total_balance())`) en lugar de probar cada unidad directamente en aislamiento. Si mañana cambia `Wallet`, el test de `Bank` fallará aunque `Bank` no tenga ningún defecto, ocultando cuál clase es la verdadera responsable.

### 2. *Flaky Tests* (Pruebas inestables o no deterministas)

Pruebas cuyo resultado varía entre ejecuciones sin que el código bajo prueba haya cambiado, típicamente por depender del reloj del sistema (`time.localtime().tm_hour`), de números pseudoaleatorios (`random.random() > 0.5`), de condiciones de carrera o de la red. Violan el principio **Repeatable** de FIRST y destruyen la confianza del equipo («dale a reintentar al pipeline, ese test siempre falla a veces»). Se corrigen inyectando el reloj como dependencia (usando un *stub*) o fijando la semilla aleatoria (`random.seed`).

### 3. *Assertion Roulette* (Ruleta de aserciones)

Apilar múltiples `assert` distintos dentro de un mismo método de prueba sin mensajes descriptivos:

```python
def test_wallet_flow(self):
    wallet = Wallet("juampi")
    wallet.deposit(100)
    self.assertEqual(100, wallet.total_balance())
    wallet.withdraw(30)
    self.assertEqual(70, wallet.total_balance())
    wallet.deposit(50)
    self.assertEqual(121, wallet.total_balance())  # Falla, ¿pero qué etapa del flujo se rompió?
```

Cuando ocurre un `AssertionError` sin contexto en medio de una secuencia larga, hay que depurar todo el método para entender qué operación falló. Se soluciona separando cada escenario en su propio test (con promedio cercano a $1\text{ aserción por test}$, como medimos con el analizador AST sobre `TestShoppingCart`, que promedió $5.03$ líneas y $1.07$ *assertions* por test) o agregando mensajes explícitos en `assertEqual(a, b, "mensaje")`.

### 4. Otros *Test Smells* clásicos de examen

* **Eager Test (Prueba ansiosa):** un único método de prueba invoca y verifica demasiadas funcionalidades distintas de la clase a la vez (por ejemplo, crear orden, listar órdenes, aplicar descuento y cancelar en el mismo test).
* **Mystery Guest (Huésped misterioso):** el test depende de un recurso externo (un archivo en disco o una base de datos como `Database("postgresql://prod-server:5432/orders")`) cuyos datos no son visibles dentro del cuerpo del test. Si el recurso externo cae o alguien modifica sus filas, el test falla misteriosamente.
* **Conditional Test Logic (Lógica condicional en el test):** incluir estructuras `if / else` o bucles `for` dentro del método de prueba para decidir qué `assert` ejecutar. Un test debe ser una línea recta determinista; si tiene `if`, nunca estás seguro de qué rama se verificó realmente.
* **Test Code Duplication:** copiar y pegar las mismas líneas de preparación (*Arrange*) en decenas de métodos en lugar de extraerlas a `setUp()`.
* **Magic Number Test:** usar literales numéricos arbitrarios en los `assert` sin explicar de dónde salen ni qué regla representan.

---

## Generación automática de pruebas unitarias con LLMs

La literatura reciente estudiada en el curso (sobre más de $216\,300$ tests generados con modelos como GPT-3.5, GPT-4, Mistral y Mixtral) y nuestra experimentación sistemática sobre `ReservationService` revelan cuatro lecciones clave al usar LLMs para generar suites de `unittest`:

1. **Prevalencia de *test smells*:** los tests generados por LLMs presentan **más *test smells*** (especialmente *Magic Number Test* y *Assertion Roulette*) que los escritos por humanos o por herramientas basadas en búsqueda como EvoSuite, y la técnica de *prompting* altera drásticamente su frecuencia.
2. **Efecto del contexto entregado al modelo ($S_1$ a $S_4$):**
   * Cuando el LLM ve el **código completo** ($S_1$), con *docstrings* ($S_3$) o con anotaciones de tipos ($S_4$), puede inspeccionar los `if` internos y generar tests que alcanzan alta cobertura de sentencias y ramas (aunque suele olvidar bordes compuestos, como cancelar el mismo día del *check-in*, que requieren tests manuales adicionales).
   * Cuando el LLM **solo ve las firmas de los métodos sin sus cuerpos** ($S_2$), no conoce la implementación y sufre de **semántica inventada** (asume reglas de negocio inexistentes, como reembolsos proporcionales cuando son por tramos) y **contrato mal inferido** (inventa tipos de retorno o excepciones distintas a las reales). En ese escenario, los tests que fallan contra el código real no son errores de sintaxis, sino evidencia directa de lo que el modelo alucinó.
3. **Efecto de la instrucción del *prompt* ($P_1$ a $P_4$):** pedir explícitamente `100% code coverage` ($P_2$), aislamiento con mocks ($P_3$) o máxima detección de fallas ($P_4$) cambia la estructura de la suite. Por ejemplo, al pedir mocks ($P_3$) para aislar colaboradores como el reloj o el notificador en `ReservationService`, el modelo utiliza `unittest.mock`, pero a veces mockea de más o configura mal los retornos, disminuyendo la cobertura efectiva.
4. **Cobertura no equivale a calidad del oráculo:** un LLM puede generar un test que ejecuta todas las líneas de un método pero termina con una **aserción trivial o tautológica** (como `self.assertIsNotNone(resultado)`). El test pasa en verde y suma $100\%$ de cobertura, pero sería incapaz de detectar si el cálculo numérico estuvo completamente equivocado.

---

## Preguntas de repaso

> [!question]- Observa el siguiente fragmento dentro de un método de prueba: `db = Database("postgresql://prod-server:5432/orders")` seguido más abajo de `if time.localtime().tm_hour < 12: assert orders[0].discount == 0.1 else: assert orders[0].discount == 0.0`. Identifica y explica tres *test smells* presentes.
> 1. **Mystery Guest:** el test se conecta a una base de datos externa (`prod-server`) cuyo estado y registros no están definidos ni controlados dentro del test.
> 2. **Conditional Test Logic:** el test contiene una bifurcación `if / else` que cambia qué aserción se ejecuta según el entorno.
> 3. **Flaky Test:** al depender de `time.localtime().tm_hour`, el comportamiento del test varía según la hora del día en que se corra.

> [!question]- Al pedirle a un LLM que genere pruebas unitarias entregándole únicamente el constructor y las firmas vacías de una clase ($S_2$, sin los cuerpos de los métodos), muchos de los tests generados fallan al correrlos contra el código real. ¿En qué dos categorías se clasifican esos fallos y por qué ocurren?
> Se clasifican en:
> 1. **Semántica inventada:** al no ver el código ni tener una especificación detallada, el modelo adivina reglas de negocio a partir del nombre del método (por ejemplo, inventa porcentajes de descuento o tramos de cancelación que no coinciden con los reales).
> 2. **Contrato mal inferido:** el modelo asume tipos de datos, estructuras de retorno o clases de excepción (`ValueError` vs. una excepción propia) diferentes a los que realmente implementa el método.

> [!question]- ¿Por qué un test generado por IA que ejecuta un método complejo y verifica únicamente `self.assertIsNotNone(resultado)` demuestra que el porcentaje de cobertura no basta para medir la calidad de una suite?
> Porque la cobertura solo mide qué líneas de código fueron **ejecutadas** durante la fase *Act*, pero no evalúa la fuerza del **oráculo** en la fase *Assert*. Verificar `assertIsNotNone` pasa siempre que la función devuelva cualquier objeto distinto de `None` (incluso un monto negativo o erróneo), dando un $100\%$ de cobertura con casi $0\%$ de capacidad real para detectar defectos.

