---
ramo: "Testing"
tema: "Pruebas unitarias dobles de prueba y test smells"
tags:
  - testing/pruebas-unitarias-dobles-de-prueba-y-test-smells
  - indice
---

# Pruebas unitarias, dobles de prueba y test smells

Diseño, implementación y evaluación de pruebas unitarias en aislamiento utilizando el módulo `unittest` de Python: conceptos de estado e invariante de objetos, estructura Arrange–Act–Assert, ciclo de vida de ejecución (`setUp`, `tearDown`, `TestSuite` y `TestRunner`), principios de calidad FIRST, manejo de encapsulamiento y excepciones, aislamiento de dependencias mediante dobles de prueba (*dummies*, *stubs*, *spies*, *mocks* y *fakes*), catálogo de *test smells* y análisis experimental de suites generadas con modelos de lenguaje (LLMs).

## Contenido del tema

1. [[01 - Estado e invariante de objetos y estructura Arrange Act Assert]] — Qué es una unidad bajo prueba (*Class Under Test*), diferencia entre estado e invariante de un objeto, y el esqueleto Arrange–Act–Assert en `unittest`.
2. [[02 - Ciclo de vida en unittest setUp tearDown TestSuite y principios FIRST]] — Funcionamiento interno de `TestLoader`, `TestSuite` (una instancia por test) y `TestRunner`, traza exacta de ejecución de `setUp` y `tearDown`, y los cinco criterios FIRST.
3. [[03 - Encapsulamiento efectos colaterales y pruebas de excepciones]] — Tensión entre encapsulamiento y verificabilidad, separación de efectos colaterales (`print`) y verificación de errores con `with self.assertRaises(...)` y `@unittest.expectedFailure`.
4. [[04 - Dobles de prueba dummies stubs spies mocks y fakes]] — Taxonomía de Meszaros y distinción de Fowler entre verificación de estado (*Stub*) y verificación de comportamiento (*Mock*) con `unittest.mock.MagicMock`.
5. [[05 - Test smells y generación de pruebas unitarias con LLMs]] — *Indirect Testing*, *Flaky Tests*, *Assertion Roulette*, *Eager Test*, *Mystery Guest* y *Conditional Test Logic*, junto con el impacto del contexto ($S_1$–$S_4$) y de la instrucción ($P_1$–$P_4$) al generar pruebas con LLMs.

