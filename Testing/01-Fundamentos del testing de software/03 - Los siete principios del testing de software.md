---
ramo: "Testing"
tema: "Fundamentos del testing de software"
tags:
  - testing/fundamentos-del-testing-de-software
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es el testing error defecto falla y el oráculo de prueba]]"
  - "[[02 - El proceso de testing niveles de prueba y psicología del tester]]"
---

# Los siete principios del testing de software

A lo largo de décadas de práctica industrial e investigación, la comunidad de ingeniería de software (recopilada por el **ISTQB**) destiló **siete principios fundamentales** que gobiernan qué puede lograr el testing, cuáles son sus límites matemáticos y cómo debemos distribuir nuestro esfuerzo.

---

## 1. El testing muestra la presencia de defectos, nunca su ausencia

Enunciado originalmente por Edsger W. Dijkstra en 1972: *«El testing de programas puede usarse para mostrar la presencia de defectos, pero nunca para mostrar su ausencia»*. Como una suite de pruebas $T$ es únicamente una muestra finita del dominio de entradas $D$ ($T \subsetneq D$), que todos los tests pasen en verde solo demuestra que **esas entradas específicas** no activaron ninguna falla. No es una demostración matemática de correctitud para las entradas restantes en $D \setminus T$.

* **Ejemplo real (Therac-25):** antes de causar la primera sobredosis letal, la máquina de radioterapia había funcionado sin incidentes en miles de tratamientos. Esos miles de usos exitosos se interpretaron erróneamente como «el software es seguro», cuando en realidad solo significaban que ningún operador había tecleado todavía la secuencia rápida que disparaba la condición de carrera.

---

## 2. El testing exhaustivo es imposible

Probar absolutamente todas las combinaciones posibles de entradas y precondiciones es computacionalmente inviable salvo en programas triviales:

* **Ejemplo del formulario (visto en clases):** imagina un formulario web con $15$ campos donde cada campo acepta apenas $5$ tipos posibles de valores. El número total de combinaciones es:
  $$5^{15} = 30\,517\,578\,125 \text{ casos de prueba}$$
* **Ejemplo de tipos primitivos:** una simple función que suma dos enteros de $64$ bits tiene un dominio de $|D| = 2^{128} \approx 3.4 \times 10^{38}$ pares posibles, y un campo de contraseña de $20$ caracteres imprimibles alcanza $95^{20}$ combinaciones.

Como no podemos probarlo todo por fuerza bruta, **hacer testing es siempre hacer muestreo inteligente** guiado por el riesgo y por técnicas sistemáticas (partición de equivalencia, valores límite, cobertura o búsqueda).

---

## 3. Testing temprano (*shift-left*)

Las actividades de prueba deben comenzar tan pronto como sea posible en el ciclo de vida del desarrollo (desde que se redactan los requerimientos y se diseñan las interfaces), no esperar a que todo el sistema esté codificado. Como el costo de reparar un defecto crece exponencialmente con el tiempo, detectar una inconsistencia de unidades en el diseño del *Mars Climate Orbiter* habría costado minutos de discusión, en lugar de $327$ millones de dólares al llegar a Marte.

---

## 4. Agrupación de defectos (*defect clustering*)

Los defectos nunca se distribuyen de manera uniforme en el código: siguen una distribución de tipo **Pareto**, donde un pequeño número de módulos concentra la gran mayoría de los defectos descubiertos o de las fallas en producción (por ejemplo, el $80\%$ de los bugs suele esconderse en el $20\%$ de los archivos).

* **Aplicación práctica:** en una aplicación bancaria, el módulo que calcula intereses compuestos, recargos y promociones (lógica densa y modificada frecuentemente) acumulará muchos más defectos que la pantalla estática de «Términos y condiciones». Priorizar el esfuerzo de prueba hacia los módulos complejos o críticos rinde mucho más que repartir las pruebas en partes iguales.

---

## 5. La paradoja del pesticida (*pesticide paradox*)

Si un agricultor aplica exactamente el mismo pesticida temporada tras temporada, los insectos vulnerables mueren al principio, pero las plagas resistentes sobreviven y el pesticida deja de tener efecto. En el software ocurre lo mismo: **si ejecutamos siempre el mismo conjunto estático de pruebas una y otra vez, esa suite dejará de encontrar defectos nuevos**.

A medida que el código evoluciona y se corrigen los bugs viejos, las pruebas antiguas siguen pasando en verde y generan una peligrosa **falsa sensación de seguridad**. Para superar la paradoja del pesticida, debemos revisar, actualizar y diversificar regularmente nuestra suite (principio que motiva directamente el *fuzzing* y el *mutation testing*).

---

## 6. El testing depende del contexto (*context-dependent*)

No existe una receta universal de testing: la estrategia, las métricas exigidas y el rigor dependen directamente del riesgo del dominio. En el software de aviónica de un avión comercial o en un marcapasos, una falla cuesta vidas, por lo que se exigen criterios estrictos de cobertura (como MC/DC) y verificación formal; en cambio, en el prototipo inicial de un videojuego casual, aplicar ese nivel de burocracia destruiría el proyecto, y es mucho más valioso priorizar pruebas ágiles de jugabilidad.

---

## 7. La falacia de la ausencia de errores (*absence-of-errors fallacy*)

Encontrar y corregir hasta el último defecto técnico del código no sirve de nada si el sistema resultante es inusable o no resuelve la necesidad real del usuario. Es la manifestación directa de lograr un $100\%$ de **verificación** con un $0\%$ de **validación**. El ejemplo canónico es *Google Wave*: una plataforma de ingeniería técnicamente brillante y con poquísimos bugs, pero que fracasó y fue cancelada porque los usuarios no entendían qué problema les resolvía.

---

---

## Ejemplo práctico: los principios en acción con un solo bug

Una función `es_bisiesto` escrita con una regla incompleta:

```python
def es_bisiesto(anio):
    return anio % 4 == 0      # defectuosa: ignora la regla de los siglos
```

Y una suite que parece razonable:

```python
import unittest

class BisiestoTest(unittest.TestCase):
    def test_anio_bisiesto(self):
        self.assertTrue(es_bisiesto(2024))

    def test_anio_comun(self):
        self.assertFalse(es_bisiesto(2023))
```

**Principio 1 (presencia, no ausencia):** la suite pasa en verde, pero eso solo prueba que `2024` y `2023` no activan el defecto. `1900` y `2100` **no** son bisiestos y la función dice que sí.

**Principio 5 (paradoja del pesticida):** si seguimos ejecutando siempre estos mismos dos tests, nunca encontrarán el bug. Hay que *diversificar* la suite añadiendo casos nuevos:

```python
    def test_siglo_no_divisible_por_400_no_es_bisiesto(self):
        self.assertFalse(es_bisiesto(1900))   # FALLA → destapa el defecto

    def test_siglo_divisible_por_400_es_bisiesto(self):
        self.assertTrue(es_bisiesto(2000))
```

Con la corrección `anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)` los cuatro tests pasan.

**Principio 2 (exhaustivo es imposible):** ¿y si quisiéramos probar el formulario de $15$ campos con $5$ valores cada uno, a $1\,000$ tests por segundo?

```python
campos, valores = 15, 5
combinaciones = valores ** campos
print(combinaciones)                         # 30517578125
print(combinaciones / 1000 / 3600 / 24)      # ≈ 353 días de ejecución continua
```

Casi un año para un solo formulario: por eso muestreamos con partición de equivalencia y valores límite en vez de probar todo.

---

## Preguntas de repaso

> [!question]- Tras el accidente del Therac-25, los ingenieros argumentaron que la máquina ya había funcionado sin fallas en miles de pacientes previos, por lo que el software estaba probado. ¿Qué principio del testing contradice directamente ese argumento y por qué?
> Contradice el principio **«El testing muestra la presencia de defectos, no su ausencia»**. Que miles de ejecuciones previas no hayan fallado solo prueba que las secuencias de entrada habituales no activaron el bug, pero no descarta que exista un defecto latente esperando una combinación específica (como teclear rápido una corrección) para manifestarse.

> [!question]- Una empresa mantiene desde hace tres años exactamente los mismos $150$ tests de regresión. Como siempre pasan al $100\%$ en el servidor de integración continua, la gerencia afirma que las nuevas funcionalidades salen sin bugs. ¿Qué principio se está ignorando?
> Se está ignorando la **paradoja del pesticida**. Ejecutar indefinidamente el mismo conjunto fijo de casos de prueba deja de revelar defectos nuevos a medida que el sistema cambia; que los $150$ tests antiguos pasen en verde solo confirma que no se rompieron esos $150$ caminos puntuales, pero no evalúa la lógica recién agregada.

> [!question]- ¿Cómo se complementan el principio de «testing exhaustivo es imposible» y el principio de «agrupación de defectos» al planificar las pruebas de un sistema operativo?
> Como es matemáticamente imposible probar todas las entradas posibles del sistema operativo (principio 2), estamos obligados a muestrear y priorizar. El principio de agrupación de defectos (principio 4) nos guía sobre *dónde* concentrar ese muestreo: en los componentes más complejos y riesgosos (como el planificador de procesos, drivers de red o manejo de memoria concurrente) en lugar de utilidades triviales.

> [!question]- Una suite tiene $100\%$ de cobertura de líneas y todos sus tests pasan. Según los principios 1 y 5, ¿por qué no podemos asegurar que el programa esté libre de defectos?
> Porque (principio 1) los tests solo muestran que **esas entradas** no revelaron fallas, no que no existan fallas para el resto del dominio; y la cobertura mide qué líneas se ejecutaron, no si se verificó el valor correcto en cada una. Además (principio 5), si la suite no se renueva con casos nuevos, deja de encontrar defectos: el ejemplo de `es_bisiesto` pasa con $100\%$ de cobertura usando solo `2023` y `2024`.

> [!question]- Calcula cuántos casos requeriría probar exhaustivamente un formulario con $8$ campos de $10$ valores posibles cada uno, y explica qué principio ilustra.
> $10^8 = 100\,000\,000$ casos. Ilustra el principio 2 (el testing exhaustivo es imposible): con $8$ campos modestos ya tenemos cien millones de combinaciones, así que se debe muestrear con técnicas como partición de equivalencia, valores límite o pruebas combinatorias priorizadas por riesgo.
