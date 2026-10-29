---
ramo: "Testing"
tema: "Reglas de código automáticas y linters"
tags:
  - testing/reglas-de-codigo-automaticas-y-linters
  - origen/complemento
prerrequisitos:
  - "[[Testing/08-Reglas de código automáticas y linters/02 - Implementación de reglas AST eval condiciones constantes y exceso de argumentos|Implementación de reglas AST eval condiciones constantes y exceso de argumentos]]"
  - "[[Testing/08-Reglas de código automáticas y linters/03 - Reglas sobre comparaciones y detección automática de test smells con AST|Reglas sobre comparaciones y detección automática de test smells con AST]]"
---

# Cómo probar un linter: casos positivos, negativos y límites estáticos

## ¿Quién prueba al linter? Casos positivos y casos negativos

Un linter es una pieza de software más, y una regla mal programada puede arruinar el flujo de trabajo de todo un equipo. Para verificar que una regla funciona bien, no basta con probar que detecta el código malo: toda suite de pruebas para un linter debe incluir obligatoriamente **dos familias de tests**:

1. **Casos positivos (sensibilidad / evitar falsos negativos):** fragmentos de código que **sí contienen** la mala práctica y donde la regla debe emitir exactamente el `Warning` esperado en la línea correcta.
2. **Casos negativos (especificidad / evitar falsos positivos):** fragmentos de código limpios o sintácticamente parecidos (por ejemplo, `x is None` o `x == 5` para `CompareNoneRule`, o `obj.eval()` para `EvalUsedRule`) donde la regla **debe quedarse callada** y devolver la lista vacía `[]`.

En el curso construimos una clase base `LinterTest(unittest.TestCase)` con un método de aserción a medida `assertWarnings(actual, expected)`:

```python
import unittest

class LinterTest(unittest.TestCase):
    def assertWarnings(self, actual, expected):
        self.assertEqual(len(actual), len(expected),
                         "El número de advertencias no coincide")
        for a, e in zip(actual, expected):
            self.assertEqual(str(a), str(e))

class TestEvalRule(LinterTest):
    def test_eval_detectado_caso_positivo(self):
        result = Linter.analyze(EvalUsedRule, "eval('2')")
        self.assertWarnings(result, [
            Warning("EvalWarning", 1, "eval should not be used!!")
        ])

    def test_eval_ausente_caso_negativo(self):
        result = Linter.analyze(EvalUsedRule, "5 + 1")
        self.assertWarnings(result, [])
```

---

## Falsos negativos por alias sintáctico: ¿por qué escapa `e = eval; e('x')`?

Una pregunta conceptual clásica del libro de apuntes y de la Interrogación 2 es analizar qué ocurre cuando le pasamos este código de dos líneas a `EvalUsedRule`:

```python
e = eval
e("x")
```

* **¿Lo detecta `EvalUsedRule`?** **No** (devuelve `[]`, produciendo un **falso negativo**).
* **Explicación en términos del AST:**
  1. En la línea 1 (`e = eval`), el nodo es un `ast.Assign(targets=[Name(id='e')], value=Name(id='eval'))`. No hay ningún nodo `ast.Call`, por lo que `visit_Call` ni siquiera se activa.
  2. En la línea 2 (`e("x")`), sí hay un nodo `ast.Call`, pero su atributo `node.func` es `Name(id='e')`. Como `node.func.id` es `'e'` y no `'eval'`, la condición `node.func.id == 'eval'` da `False`.
* **¿Es un error tonto de nuestra regla o un límite profundo del análisis sintáctico?**
  Podríamos intentar parchar la regla rastreando asignaciones simples `e = eval` dentro del mismo archivo, pero en Python una función es un objeto de primera clase: puede guardarse en un diccionario (`d['fn'] = eval`), pasarse como parámetro a otra función (`aplicar(eval, 'x')`) o importarse con alias (`from builtins import eval as ejecutar`). Saber con certeza a qué objeto apunta una variable en cualquier punto requiere **análisis de flujo de datos o ejecución dinámica**. Un análisis puramente sintáctico sobre el AST solo ve los nombres escritos, no los objetos en memoria.

---

## Falsos positivos, intención humana y fatiga de alertas (*alert fatigue*)

El problema opuesto ocurre cuando queremos hacer una regla «demasiado inteligente». Supongamos que extendemos `AlwaysTrueIfRule` para que no solo detecte `if True:`, sino cualquier condición compuesta por constantes o variables de configuración, como `if 2 > 1:` o `if DEBUG_MODE:`.

* **¿Qué riesgo aparece?** Aparecen **falsos positivos**: un desarrollador puede haber escrito deliberadamente una bandera de configuración (`if ENABLE_CACHE:`) o una constante de versión para desactivar temporalmente una funcionalidad sin borrar el código. El AST ve la estructura sintáctica, pero **no puede ver la intención del programador**.
* **El peligro de la fatiga de alertas (*alert fatigue*):** si un linter está mal calibrado y llena la pantalla con decenas de advertencias irrelevantes o falsos positivos en cada *commit*, ocurre el efecto «Pedro y el lobo»: **el equipo se acostumbra a ignorar o desactivar el linter**, y cuando finalmente aparece una advertencia crítica real (como una vulnerabilidad de seguridad), nadie la lee. Por eso, en ingeniería de software, la precisión de un linter (bajos falsos positivos) suele ser más valiosa que intentar atrapar el $100\%$ de los casos dudosos.

---

## Preguntas de repaso

> [!question]- Explica en términos de los nodos del AST por qué `EvalUsedRule` detecta `eval('2 + 2')` pero no detecta `f = eval; f('2 + 2')`.
> Porque `EvalVisitor` solo inspecciona nodos `ast.Call` verificando `isinstance(node.func, Name) and node.func.id == 'eval'`. En `f = eval` el nodo es un `ast.Assign` (no un `Call`), y en `f('2 + 2')` el nodo `Call` tiene `node.func = Name(id='f')`, cuyo `.id` es `'f'` en lugar de `'eval'`.

> [!question]- ¿Por qué es indispensable incluir pruebas de casos negativos (código que NO debe disparar advertencias) al probar una regla de linter o un detector de *test smells*?
> Porque una regla defectuosa (por ejemplo, una que emita un `Warning` en todo nodo `ast.Compare` sin verificar el operador ni el operando) pasaría todos los casos positivos al detectar `x == None`, pero sería inútil en la práctica por marcar erróneamente como defectuoso cualquier `if x == 5:` o `if x is None:` del proyecto.

> [!question]- ¿Qué es la «fatiga de alertas» (*alert fatigue*) en herramientas de análisis estático y por qué un exceso de falsos positivos termina reduciendo la detección de defectos reales?
> Es el fenómeno psicológico y operativo donde los desarrolladores reciben tantas advertencias falsas o triviales del linter que pierden la confianza en la herramienta, optando por ignorar su salida o silenciarla globalmente (`# noqa`), lo que provoca que las advertencias verdaderas pasen desapercibidas.

