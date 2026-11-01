---
ramo: "Testing"
tema: "Fundamentos del testing de software"
tags:
  - testing/fundamentos-del-testing-de-software
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es el testing error defecto falla y el oráculo de prueba]]"
---

# El proceso de testing, niveles de prueba y psicología del tester

## El proceso de testing según ISTQB

Probar software de manera profesional no consiste en abrir la terminal a última hora y teclear entradas al azar para ver si algo explota. Según el estándar **ISTQB**, el testing es un proceso estructurado compuesto por seis actividades iterativas que se solapan a lo largo del desarrollo:

1. **Planificación:** definir el alcance, los riesgos que queremos mitigar, los recursos y los criterios de salida (cuándo consideraremos que ya probamos suficiente).
2. **Análisis (*¿qué probar?*):** examinar la base de prueba (requerimientos, diseño o código) para identificar qué comportamientos y condiciones requieren verificación.
3. **Diseño (*¿con qué casos?*):** aplicar técnicas sistemáticas (como partición de equivalencia, valores límite o cobertura) para elegir qué entradas específicas compondrán nuestra muestra $T \subseteq D$.
4. **Implementación:** traducir esos casos diseñados a scripts automatizados (siguiendo el esqueleto **Arrange–Act–Assert**: preparar el estado, ejecutar la unidad bajo prueba y aplicar el oráculo) y preparar los datos de prueba.
5. **Ejecución:** correr las suites de pruebas, comparar las salidas reales contra el oráculo y registrar cualquier discrepancia.
6. **Evaluación de criterios de salida y reporte:** analizar las métricas obtenidas (cobertura, *mutation score*, defectos abiertos) y comunicar al equipo la evidencia recolectada.

---

## Niveles de prueba y la pirámide de testing

El proceso de prueba se aplica en cuatro niveles de granularidad creciente (que conectan con lo estudiado en [[Ingeniería de Software/06-Testing/03 - Niveles de testing en Rails|Niveles de testing en Rails]]):

| Nivel de prueba | ¿Qué evalúa exactamente? | Base de prueba (oráculo) | Velocidad y costo |
| :--- | :--- | :--- | :--- |
| **Unidad / Componente** | Una función, método o clase en completo aislamiento del resto del sistema. | Diseño detallado y código fuente. | Muy rápidas (milisegundos) y baratas de mantener. |
| **Integración** | Las interfaces, contratos y comunicación entre dos o más módulos o servicios externos. | Diseño arquitectónico y contratos de interfaz (APIs). | Velocidad y costo intermedios. |
| **Sistema** | El comportamiento de extremo a extremo (*end-to-end*) del sistema integrado como un todo. | Requerimientos funcionales y no funcionales, casos de uso. | Lentas, costosas y más propensas a fragilidad (*flakiness*). |
| **Aceptación** | Si el sistema satisface la necesidad real del usuario o cliente (validación). | Procesos de negocio, contratos y expectativas del usuario. | Muy costosas; suelen involucrar usuarios o entornos reales. |

Estos cuatro niveles se organizan en la clásica **pirámide de pruebas** (Mike Cohn): la base debe estar formada por **muchas pruebas unitarias** que dan retroalimentación inmediata en cada cambio; una capa intermedia más pequeña de **pruebas de integración** que previenen catástrofes de interfaz como la del *Mars Climate Orbiter*; y una cúspide reducida de **pruebas de sistema y aceptación**.

### El costo exponencial de los defectos en el tiempo

Como demostró Barry Boehm, el costo de encontrar y reparar un defecto crece de forma **aproximadamente exponencial** según la etapa en que se descubre ($\text{requerimientos} \to \text{build} \to \text{test} \to \text{uso en vivo}$). Corregir una ambigüedad al escribir los requerimientos o al correr un test unitario toma minutos; descubrir ese mismo defecto cuando el software ya está en producción (*live use*) puede costar millones de dólares, pérdida de datos o vidas humanas.

---

## La psicología del testing y el sesgo de confirmación

Glenford Myers destacó una verdad incómoda que distingue al testing del resto de la ingeniería de software: **el testing es un acto destructivo dentro de un oficio fundamentalmente constructivo**. Después de pasar días construyendo una clase o un módulo, nuestro cerebro quiere demostrar que la obra funciona. Para probarla bien, debemos invertir nuestro objetivo y **querer romperla**.

Esta tensión psicológica tiene tres consecuencias prácticas directas:

* **Inversión del concepto de éxito:** una prueba «exitosa» no es la que pasa en verde, sino la que **logra destapar una falla**. Una prueba en verde solo dice que esa entrada puntual no reveló defectos, pero no garantiza nada sobre el resto del dominio.
* **Sesgo de confirmación:** quien escribió el código tiende inconscientemente a diseñar pruebas amables que confirman que su solución funciona en el camino feliz, evitando los casos borde que podrían hacerla fallar. Por ello, aumentar el **grado de independencia** entre quien programa y quien diseña las pruebas (desde pruebas cruzadas entre compañeros hasta equipos de QA dedicados) incrementa drásticamente la tasa de detección.
* **Cultura del programador humilde (Dijkstra):** cuando un compañero o una prueba reporta una falla, es natural sentirlo como una crítica personal. Una cultura de ingeniería sana separa el defecto de la persona: cada falla encontrada antes de llegar a producción es una victoria compartida del equipo, nunca un reproche.

---

---

## Ejemplo práctico: la misma lógica probada en dos niveles y con dos mentalidades

Partimos de una función de descuento y de un carrito que la usa:

```python
def aplicar_descuento(precio, porcentaje):
    return round(precio * (1 - porcentaje / 100), 2)

class Carrito:
    def __init__(self, catalogo):
        self.catalogo = catalogo
        self.items = []

    def agregar(self, sku):
        self.items.append(sku)

    def total(self, porcentaje=0):
        bruto = sum(self.catalogo.precio(sku) for sku in self.items)
        return aplicar_descuento(bruto, porcentaje)
```

**Nivel unidad:** probamos `aplicar_descuento` sola, sin carrito ni catálogo. Es rápida y señala exactamente dónde está el problema si falla.

```python
import unittest

class DescuentoUnitTest(unittest.TestCase):
    def test_descuento_veinte_por_ciento(self):
        self.assertEqual(aplicar_descuento(10000, 20), 8000)
```

**Nivel integración:** probamos que `Carrito` y el catálogo se entienden entre sí (suman precios por SKU y luego aplican el descuento). Aquí usamos un catálogo falso en memoria para no depender de una base de datos real, pero lo que verificamos es la **colaboración** entre módulos.

```python
class CatalogoFake:
    def precio(self, sku):
        return {"A": 1000, "B": 2500}[sku]

class CarritoIntegracionTest(unittest.TestCase):
    def test_total_suma_items_y_aplica_descuento(self):
        carrito = Carrito(CatalogoFake())
        carrito.agregar("A")
        carrito.agregar("B")
        # (1000 + 2500) con 10% de descuento
        self.assertEqual(carrito.total(porcentaje=10), 3150)
```

**Nivel sistema / aceptación (descripción, sin código):** un tester abre la tienda web, agrega dos productos, ingresa el cupón y comprueba que el total mostrado y el cobro en la pasarela de pago coinciden. Es más lento, más caro y más frágil, por eso hay pocos.

### Mentalidad «amable» frente a mentalidad «destructiva»

El test amable de arriba pasa en verde. Ahora pensemos como Myers: ¿cómo podemos *romper* `aplicar_descuento`?

```python
class DescuentoDestructivoTest(unittest.TestCase):
    def test_cien_por_ciento_deja_precio_en_cero(self):
        self.assertEqual(aplicar_descuento(10000, 100), 0)

    def test_cero_por_ciento_no_cambia_el_precio(self):
        self.assertEqual(aplicar_descuento(10000, 0), 10000)

    def test_porcentaje_mayor_a_cien_es_invalido(self):
        with self.assertRaises(ValueError):
            aplicar_descuento(10000, 101)   # FALLA: devuelve -100.0
```

El último test **falla**, y por eso es la prueba «exitosa»: destapó un defecto que el test amable jamás habría encontrado (un descuento de 101 % nos haría *pagarle* al cliente). La corrección es validar el rango:

```python
def aplicar_descuento(precio, porcentaje):
    if not 0 <= porcentaje <= 100:
        raise ValueError("porcentaje fuera de rango")
    return round(precio * (1 - porcentaje / 100), 2)
```

---

## Preguntas de repaso

> [!question]- ¿Por qué la pirámide de pruebas propone tener muchas más pruebas unitarias en la base que pruebas de sistema en la cúspide?
> Porque las pruebas unitarias ejecutan funciones aisladas en memoria en pocos milisegundos y señalan con precisión quirúrgica qué línea falló. En cambio, las pruebas de sistema levantan bases de datos, red o interfaces gráficas completas: son órdenes de magnitud más lentas, más caras de configurar y cuando fallan es mucho más difícil aislar la causa raíz.

> [!question]- Dos módulos de un banco calculan correctamente sus fórmulas internas y pasan todas sus pruebas unitarias, pero uno envía los montos en pesos y el otro los interpreta en miles de pesos. ¿Qué nivel de prueba faltó aplicar y por qué?
> Faltaron **pruebas de integración**. Las pruebas unitarias verifican cada componente por separado asumiendo que sus entradas tienen el formato esperado, mientras que las pruebas de integración están diseñadas específicamente para verificar la compatibilidad de las interfaces y el intercambio de datos entre módulos.

> [!question]- ¿En qué consiste el sesgo de confirmación al escribir pruebas sobre nuestro propio código y cómo se mitiga en la práctica?
> Es la tendencia humana inconsciente a elegir entradas de prueba que confirman nuestra propia hipótesis de que el código está bien hecho, pasando por alto los supuestos erróneos que ya teníamos al programarlo. Se mitiga aplicando técnicas sistemáticas de diseño de casos (como valores límite o análisis de mutación) y aumentando la independencia mediante revisión entre pares o pruebas escritas por otra persona.

> [!question]- En el ejemplo del carrito, el test de integración usa un `CatalogoFake` en memoria. ¿Sigue siendo una prueba de integración o se volvió una prueba unitaria?
> Sigue siendo de integración, porque lo que verifica es la **colaboración** entre `Carrito`, `aplicar_descuento` y la interfaz del catálogo (que los precios se sumen y luego se descuenten). El fake solo reemplaza el recurso externo costoso (la base de datos); el nivel lo define lo que se prueba (la interacción entre módulos), no si algún componente es falso.

> [!question]- Un compañero escribe `aplicar_descuento` y también sus tests, y todos pasan. Menciona dos acciones concretas para reducir el sesgo de confirmación.
> (1) Que otra persona (compañero o QA) diseñe o revise los casos, aumentando la independencia entre quien programa y quien prueba. (2) Escribir deliberadamente casos «destructivos»: valores en los bordes (0 %, 100 %), fuera de rango (101 %, −5 %) y tipos inválidos, en vez de solo el camino feliz.
