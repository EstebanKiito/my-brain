---
ramo: "Testing"
tema: "Análisis de mutación y diseño de pruebas de caja negra"
tags:
  - testing/analisis-de-mutacion-y-diseno-de-pruebas-de-caja-negra
  - origen/complemento
prerrequisitos:
  - "[[01 - Mutation Testing operadores de mutación y cálculo del mutation score]]"
---

# Hipótesis del mutation testing, mutantes equivalentes y mutación con LLMs

## ¿Por qué sembrar cambios minúsculos sirve para encontrar bugs reales?

A primera vista podría parecer extraño que cambiar un `+` por un `-` o un `>=` por un `>` nos diga algo sobre los errores complejos que cometen los humanos en producción. El *Mutation Testing* se sostiene sobre **dos hipótesis fundamentales y un efecto empírico** (Jia & Harman, 2011; Just et al., FSE 2014):

1. **Hipótesis del Programador Competente (*Competent Programmer Hypothesis*):** los desarrolladores competentes no escriben código al azar; entregan programas que están muy cerca de ser correctos, y sus defectos suelen ser pequeñas desviaciones locales (un caso borde mal puesto, un operador invertido, una variable equivocada).
2. **Hipótesis de la Vecindad Finita (*Finite Neighborhood Hypothesis*):** los defectos reales viven en una vecindad sintáctica finita y cercana al programa correcto, que puede alcanzarse mediante pequeñas modificaciones válidas.
3. **Efecto de Acoplamiento (*Coupling Effect*):** los defectos complejos están «acoplados» a los defectos simples de tal manera que **una batería de pruebas lo bastante sensible para detectar mutaciones simples de primer orden también detectará, con altísima probabilidad, fallas compuestas más complejas**.

---

## El problema del mutante equivalente y su indecidibilidad

No todo cambio sintáctico introduce un bug. Un **mutante equivalente** es una modificación del código fuente que **preserva exactamente el mismo comportamiento observable para absolutamente todas las entradas posibles del dominio**.

### Ejemplos clásicos de mutantes equivalentes

* **En `precio_final`:** cambiar `rate = 0.0` por `rate = 0` cuando `rate` solo se usa en una multiplicación flotante posterior, o cambiar `if total < 0: total = 0` por `if total <= 0: total = 0` (si `total` ya vale `0`, reasignarle `0` produce exactamente el mismo resultado).
* **En el algoritmo de Euclides (`new_gcd(a, b)`):** eliminar una asignación redundante o cambiar una condición en un punto donde ambas ramas convergen al mismo estado.

> [!important] ¿Por qué los mutantes equivalentes son el talón de Aquiles de la técnica?
> 1. **Ninguna prueba puede matarlos:** como su salida $M(d)$ es idéntica a la del programa original $P(d)$ para todo $d \in D$, jamás harán fallar un `assert`.
> 2. **Distorsionan el *Mutation Score*:** si de $10$ mutantes generados $2$ son equivalentes y no los descontamos del denominador, ni siquiera una suite perfecta podrá superar el $80\%$ de score.
> 3. **Detectarlos automáticamente es indecidible:** demostrar en general si dos programas arbitrarios $P$ y $M$ calculan exactamente la misma función para toda entrada equivale al Problema de la Detención (*Halting Problem*). Por eso la detección de mutantes equivalentes requiere inspección humana o heurísticas parciales.

---

## Mutation Testing mecánico frente a mutantes generados por LLMs

Al comparar mutantes generados por operadores mecánicos clásicos (`generar_clasicos()`) contra mutantes propuestos por LLMs (como GPT y Gemini sobre `ReservationService` y `ShoppingCart` en `LLMClassAnalyzer`), clasificamos cada mutante en cuatro estados: **`killed`**, **`sobrevive`**, **`invalido`** y **`equivalente`**:

| Dimensión | Operadores mecánicos clásicos (AST) | Mutantes generados por LLMs |
| :--- | :--- | :--- |
| **Validez sintáctica (`invalido`)** | Siempre válidos ($0$ inválidos) porque transforman nodos del AST directamente. | Pueden producir mutantes **inválidos** si cuentan mal el número de línea (línea corrida), copian mal el `precode`, proponen código que no compila o devuelven `aftercode == precode`. |
| **Naturaleza de los cambios** | Sistemáticos y exhaustivos sobre cada operador (`>=` $\to$ `>`, `+` $\to$ `-`), excelentes para destapar bordes numéricos no verificados. | Suelen proponer cambios semánticos más expresivos, pero a menudo concentran sus $20$ propuestas en **mutaciones obvias o triviales** (como invertir un booleano de retorno). |
| **Interpretación de un score de $100\%$** | Indica que la suite verifica rigurosamente cada rama y cada frontera. | Un $100\%$ sobre $20$ mutantes de un LLM **no significa que la suite sea perfecta**: suele indicar que el modelo propuso mutantes fáciles de matar, mientras que el *baseline* clásico sí logra dejar sobrevivientes en bordes sutiles. |

---

---

## Ejemplo práctico: sembrar mutantes sobre `precio_final`

Programa original y una suite con tres tests:

```python
def precio_final(total, cliente_vip):
    if total < 0:
        total = 0
    tasa = 0.10 if cliente_vip else 0.0
    return total * (1 - tasa)
```

```python
import unittest

class PrecioFinalTest(unittest.TestCase):
    def test_vip(self):
        self.assertEqual(precio_final(1000, True), 900.0)

    def test_cliente_normal(self):
        self.assertEqual(precio_final(1000, False), 1000.0)

    def test_total_negativo_se_trunca(self):
        self.assertEqual(precio_final(-5, False), 0)
```

Generamos cuatro mutantes de primer orden (un solo cambio cada uno) y corremos la suite contra cada uno:

| Mutante | Cambio | ¿Qué test lo mata? | Estado |
| :--- | :--- | :--- | :---: |
| **M1** | `total < 0` → `total <= 0` | Ninguno: si `total == 0`, reasignar `0` no cambia nada | **Equivalente** (sobrevive) |
| **M2** | `0.10` → `0.20` | `test_vip` (devuelve $800$) | Muerto |
| **M3** | `1 - tasa` → `1 + tasa` | `test_vip` (devuelve $1100$) | Muerto |
| **M4** | se elimina el bloque `if total < 0` | `test_total_negativo_se_trunca` (devuelve $-5$) | Muerto |

Cálculo del *mutation score*:

* **Sin ajustar:** $\dfrac{3\text{ muertos}}{4\text{ mutantes}} = 75\%$.
* **Ajustado** (descontando el equivalente M1 del denominador): $\dfrac{3}{4-1} = 100\%$.

La suite es perfecta aunque el score sin ajustar diga $75\%$. Mira qué pasa si borramos `test_total_negativo_se_trunca`: **M4 sobrevive**, el score ajustado baja a $\frac{2}{3} = 67\%$ y la herramienta nos está diciendo exactamente qué test falta. Esa es la utilidad de la técnica: cada sobreviviente no equivalente es un test pendiente.

---

## Preguntas de repaso

> [!question]- Un compañero corre una herramienta de *Mutation Testing*, obtiene un *Mutation Score* sin ajustar del $85\%$ y afirma: «Mis pruebas dejan pasar el $15\%$ de los bugs». ¿Por qué su conclusión puede ser equivocada?
> Porque dentro de ese $15\%$ de mutantes sobrevivientes puede haber **mutantes equivalentes**: cambios sintácticos que no alteran el comportamiento del programa para ninguna entrada y que, por definición, no son bugs ni pueden ser matados por ningún test. Si todo ese $15\%$ fueran mutantes equivalentes, el *mutation score* ajustado real de su batería sería del $100\%$.

> [!question]- ¿Qué afirma el «Efecto de Acoplamiento» (*Coupling Effect*) y por qué es tan importante para que el *Mutation Testing* sea viable en la práctica?
> Afirma que las pruebas capaces de detectar pequeños defectos simples (mutantes con un solo operador modificado) también detectan en la gran mayoría de los casos defectos complejos formados por la combinación de varios errores. Es crucial porque nos permite generar solo mutantes de primer orden (un cambio a la vez) en lugar de enfrentar la explosión combinatoria de mutar múltiples líneas simultáneamente.

> [!question]- En una evaluación comparativa sobre una batería con $100\%$ de cobertura, los $20$ mutantes propuestos por un LLM mueren todos ($\text{score} = 100\%$), pero los mutantes mecánicos clásicos dejan un $18\%$ de sobrevivientes no equivalentes ($\text{score} = 82\%$). ¿Significa esto que el LLM es mejor evaluador?
> Al contrario: el objetivo de un generador de mutantes es poner en jaque a la batería de pruebas encontrando sus puntos ciegos (sobrevivientes no equivalentes). Que todos los mutantes del LLM mueran mientras varios mutantes clásicos de borde sobreviven demuestra que el LLM propuso mutaciones demasiado obvias o drásticas que las aserciones existentes atraparon fácilmente.

> [!question]- Dado `def es_mayor(a, b): return a > b`, el mutante cambia `>` por `>=`. ¿Qué test lo mata y cuándo sería equivalente?
> Lo mata cualquier test con `a == b`, por ejemplo `assertFalse(es_mayor(3, 3))` (el original da `False` y el mutante da `True`). Sería equivalente solo si el programa garantizara que `a` y `b` nunca pueden ser iguales, porque entonces ninguna entrada válida distinguiría ambas versiones.

> [!question]- Una suite mata $9$ de $12$ mutantes y, tras inspección manual, $2$ de los $3$ sobrevivientes son equivalentes. ¿Cuál es el score sin ajustar y el ajustado? ¿Qué debes hacer con el sobreviviente restante?
> Sin ajustar: $9/12 = 75\%$. Ajustado: $9/(12-2) = 9/10 = 90\%$. El sobreviviente restante es un mutante no equivalente: revela una conducta que ningún test verifica, así que hay que escribir un test (normalmente un caso borde) que lo mate.
