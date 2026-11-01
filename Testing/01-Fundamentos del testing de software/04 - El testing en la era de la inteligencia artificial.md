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

# El testing en la era de la inteligencia artificial

## El cambio de paradigma: de escribir código a verificarlo

Durante décadas, el flujo clásico de desarrollo estuvo limitado por la velocidad a la que un programador humano podía escribir líneas de código. Con la llegada de los modelos grandes de lenguaje (**LLMs**) y los agentes autónomos de programación, la generación de código se volvió rápida, barata y masiva:

![Comparación entre el flujo de desarrollo tradicional y el flujo actual con inteligencia artificial](adjuntos/Desarrollo%20de%20software%20antes%20y%20ahora%20con%20IA.png)

* **Antes:** el desarrollador pensaba la solución, escribía el código línea por línea y luego escribía las pruebas. Al construirlo manualmente, adquiría un modelo mental detallado de cada `if` y cada caso borde.
* **Ahora:** el desarrollador describe su intención en lenguaje natural (*prompt*), la IA genera muchísimo más código en segundos y **el desarrollador debe verificarlo**.

Como resumió Cristian Cadar (FM 2026), el desarrollo de software está mutando *«de escribir código a revisarlo y validarlo»*. Escribir código dejó de ser el cuello de botella principal; **establecer con evidencia si ese código es correcto** pasó a ser el verdadero desafío de la ingeniería de software moderna.

---

## Deuda de verificación (*verification debt*)

En AWS re:Invent 2025, Werner Vogels (CTO de Amazon) sintetizó el problema central con una frase célebre:

> *«AI can generate code faster than you can understand it.»* (La IA puede generar código más rápido de lo que puedes entenderlo).

Cuando la **velocidad de generación de código** ($\uparrow\uparrow$) crece muy por encima de la **capacidad humana de verificación**, la brecha acumulada entre ambas curvas se convierte en **deuda de verificación** (*verification debt*): código que entra al repositorio y llega a producción sin que nadie en el equipo comprenda del todo sus casos borde ni tenga evidencia rigurosa de que funciona fuera del camino feliz.

---

## Cuatro riesgos críticos del código y los tests generados por IA

¿Por qué no basta con mirar por encima el código que entrega un asistente generativo o pedirle al mismo modelo que escriba los tests?

1. **Plausibilidad engañosa y alucinaciones sutiles:** los LLMs están entrenados para producir código sintácticamente impecable, con buenos nombres de variables y comentarios convincentes. Sin embargo, suelen ser acertados en el caso obvio y frágiles en los bordes, e incluso estudios empíricos (como Perry et al., 2023) muestran que desarrolladores asistidos por IA pueden introducir más vulnerabilidades de seguridad mientras sienten mayor confianza en su código.
2. **Incapacidad de revisión manual a escala:** cuando un asistente o agente modifica decenas de archivos en una sola iteración, la revisión humana línea a línea (*code review*) pierde efectividad por fatiga cognitiva.
3. **Errores correlacionados entre código y tests:** si le pedimos al **mismo modelo** (o usamos el mismo *prompt*) que genere tanto la función como sus pruebas unitarias, el modelo suele replicar exactamente el mismo malentendido en ambos lados. El test generado no actúa como un oráculo independiente, sino como un espejo que confirma el bug del código generado.
4. **Agentes autónomos con efectos en el mundo real:** hoy los agentes de IA no solo sugieren texto en el editor, sino que ejecutan secuencias de acciones (llaman APIs, modifican bases de datos o despliegan servicios). Evaluar si la secuencia de decisiones de un agente fue segura y óptima es un **problema de oráculo abierto**.

---

## La idea central del curso: automatizar la verificación

Frente a la generación masiva de código, el testing manual y artesanal ya no da abasto. Necesitamos un **freno de seguridad** basado en **retroalimentación automática, sistemática e independiente**:

* Si la generación de código se automatiza, **la generación, ejecución y evaluación de pruebas debe automatizarse también**.
* A lo largo del curso construiremos herramientas que no confían en que el código «se vea bien»: mediremos qué líneas y ramas ejecuta realmente (*code coverage*), generaremos miles de entradas maliciosas o guiadas por funciones de aptitud (*fuzzing*), sembraremos bugs artificiales para poner a prueba a los propios tests (*mutation testing*), analizaremos y transformaremos árboles de sintaxis abstracta (**AST**) para detectar malas prácticas automáticamente, y usaremos resolvedores matemáticos (**Z3**) para descubrir entradas exactas que rompan condiciones profundas.

---

---

## Ejemplo práctico: el test «espejo» generado por la misma IA

Imagina que le pedimos a un asistente: *«escribe una función que calcule el promedio de notas ignorando la peor nota, y sus tests»*. Entrega algo que se ve impecable:

```python
def promedio_sin_peor(notas):
    return sum(sorted(notas)[1:]) / len(notas)      # bug: divide por len(notas)
```

```python
import unittest

class PromedioGeneradoTest(unittest.TestCase):
    def test_promedio_sin_peor(self):
        notas = [4.0, 5.0, 6.0]
        esperado = sum(sorted(notas)[1:]) / len(notas)   # copia la lógica del código
        self.assertEqual(promedio_sin_peor(notas), esperado)
```

El test pasa en verde, pero es un **espejo**: repite la misma fórmula defectuosa, así que no es un oráculo independiente (riesgo 3). La función promedia $5.0$ y $6.0$ dividiendo por $3$ en vez de por $2$, y devuelve $3.67$.

Un oráculo independiente se calcula **a mano, desde la especificación**:

```python
class PromedioIndependienteTest(unittest.TestCase):
    def test_promedio_calculado_a_mano(self):
        # sin la peor (4.0): (5.0 + 6.0) / 2 = 5.5
        self.assertEqual(promedio_sin_peor([4.0, 5.0, 6.0]), 5.5)   # FALLA: 3.666...

    def test_lista_de_una_nota(self):
        # ¿qué debería pasar? la especificación no lo dice → hay que decidirlo
        with self.assertRaises(ValueError):
            promedio_sin_peor([5.0])         # FALLA: devuelve 0.0
```

Esto resume la idea del curso: **no confiar en que el código «se vea bien»**, sino generar verificación independiente. El segundo test además muestra que la IA no preguntó por el caso borde de la lista corta, y esa es justo la **deuda de verificación** que nos toca pagar.

---

## Preguntas de repaso

> [!question]- ¿Qué es la deuda de verificación (*verification debt*) y por qué se dispara con el uso de asistentes de IA?
> Es la brecha acumulada entre el volumen de código que se incorpora a un sistema y la capacidad real del equipo humano para comprenderlo, revisarlo y verificar su correctitud. Se dispara con la IA porque los modelos generan cientos de líneas plausibles en segundos, superando ampliamente la velocidad de lectura y análisis crítico de los desarrolladores.

> [!question]- Si un desarrollador le pide a un LLM: «escribe la función `calcular_impuesto` y escribe también sus tests unitarios», y todos los tests pasan en verde al primer intento, ¿por qué no podemos confiar ciegamente en ese resultado?
> Porque el código y los tests provienen de la misma fuente y comparten el mismo contexto: sufren de **errores correlacionados**. Si el LLM malinterpretó una regla de borde del impuesto al programar la función, codificará exactamente esa misma suposición errónea como valor esperado en los `assert` de la prueba, violando la independencia del oráculo.

> [!question]- ¿Cómo cambia la cadena causal $\text{Error} \to \text{Defecto} \to \text{Falla}$ cuando el código lo escribe un modelo de lenguaje en lugar de una persona?
> El marco conceptual se mantiene intacto: aunque no haya habido un «error de razonamiento humano» explícito al teclear la línea (sino una predicción estadística defectuosa del modelo o una ambigüedad en el *prompt*), el **defecto** sigue quedando escrito estáticamente en el código fuente y seguirá provocando una **falla** observable cuando un usuario ejecute ese camino en producción.

> [!question]- Un agente de IA genera una función y sus tests, y todo pasa. Da dos razones por las que eso no basta como evidencia de corrección.
> (1) Los errores están **correlacionados**: el mismo modelo suele repetir el mismo malentendido en el código y en los tests, así que el test no es un oráculo independiente (test espejo). (2) La plausibilidad engañosa: el código se ve bien y acierta el caso obvio, pero puede fallar en bordes que ni el modelo ni el revisor apurado consideraron.

> [!question]- ¿Qué significa «deuda de verificación» y cómo la reduce automatizar la generación y evaluación de pruebas?
> Es la brecha entre la velocidad a la que se genera código y la capacidad humana de comprender y verificarlo; el código acumulado sin evidencia de correctitud es deuda. Automatizar la verificación (cobertura, fuzzing, mutation testing, análisis estático) entrega evidencia sistemática e independiente a la misma velocidad que la generación, en lugar de depender de revisión manual que no escala.
