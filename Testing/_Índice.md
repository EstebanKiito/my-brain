---
ramo: "Testing"
tags:
  - testing/indice
  - indice
---

# Testing (IIC3745)

Curso de pruebas de software, verificación automatizada y análisis estático y dinámico de programas. Todas las unidades están explicadas desde cero con ejemplos paso a paso en Python pensando en un estudiante de 2° año de Ciencia de la Computación, cubriendo íntegramente los capítulos del libro de apuntes del profesor, las presentaciones de clases, los notebooks interactivos y las pautas de ejercicios de evaluación.

## Mapa de unidades del curso

### Bloque 1 — Fundamentos, Pruebas Unitarias, Cobertura, Fuzzing Sintáctico y Mutación
1. [[01-Fundamentos del testing de software/_Índice|Fundamentos del testing de software]] — Costo de las fallas reales, diferencia entre error, defecto y falla, modelo RIPR, principios de Dijkstra e ISTQB, pirámide de Cohn y problema del oráculo.
2. [[02-Pruebas unitarias dobles de prueba y test smells/_Índice|Pruebas unitarias, dobles de prueba y test smells]] — Anatomía AAA, principios FIRST, `unittest`, aislamiento con *Stubs* y *Mocks* (`unittest.mock`), catálogo de *Test Smells* y evaluación de tests generados con LLMs.
3. [[03-Cobertura de código e instrumentación con settrace/_Índice|Cobertura de código e instrumentación con settrace]] — Grafos de flujo de control (CFG), cobertura de líneas, ramas y caminos, relaciones de subsunción e implementación de un colector con `sys.settrace`.
4. [[04-Fuzzing aleatorio y fuzzing basado en mutación/_Índice|Fuzzing aleatorio y fuzzing basado en mutación]] — Límites estadísticos del *random fuzzing*, operadores de mutación de strings y bucle de *Greybox Fuzzing* guiado por cobertura (*seed queue* y función de energía).
5. [[05-Fuzzing basado en búsqueda/_Índice|Fuzzing basado en búsqueda]] — Reformulación del testing como optimización, cálculo de distancia de rama (*branch distance*), *Hill Climbing*, óptimos locales, *plateaus* y algoritmos genéticos estilo *EvoSuite/Pynguin*.
6. [[06-Análisis de mutación y diseño de pruebas de caja negra/_Índice|Análisis de mutación y diseño de pruebas de caja negra]] — Hipótesis del programador competente y efecto de acoplamiento, *Mutation Score*, mutantes equivalentes, y técnicas de caja negra (Particiones de Equivalencia, Valores Límite, Tablas de Decisión y Transición de Estados).

### Bloque 2 — Análisis Estático, Transformación de AST, Ejecución Simbólica y Profiling
7. [[07-Análisis estático y árboles de sintaxis abstracta/_Índice|Análisis estático y árboles de sintaxis abstracta]] — Alcances del análisis estático y el Teorema de Rice, gramáticas e intérpretes con `MiniScheme`, categorías de nodos del módulo `ast` de Python (`mod`, `stmt`, `expr`, `expr_context`) y el patrón *Visitor* (`NodeVisitor`).
8. [[08-Reglas de código automáticas y linters/_Índice|Reglas de código automáticas y linters]] — Arquitectura `AbstractRule` / `Warning`, reglas sin estado, reglas con contexto de función o bucle, y análisis de alcance léxico (*scope stack* y *shadowing*) para detectar variables no utilizadas.
9. [[09-Transformaciones de código con AST/_Índice|Transformaciones de código con AST]] — Mecánica de `ast.NodeTransformer` y `fix_missing_locations`, reescritura de operadores y llamadas, la trampa de `RenameTransformer`, inyección de sensores, limpieza de código muerto en dos pasadas y compresión de AST para prompts de LLMs.
10. [[10-Análisis de flujo de información y taint analysis/_Índice|Análisis de flujo de información y taint analysis]] — Modelo de Fuentes (*Sources*), Sumideros (*Sinks*) y Sanitizadores, prevención de *SQL Injection*, seguimiento dinámico con `tstr` y diferencia entre flujo explícito y flujo implícito (canales laterales).
11. [[11-Ejecución simbólica y fuzzing concólico/_Índice|Ejecución simbólica y fuzzing concólico]] — Variables simbólicas y condiciones de camino ($PC$), árboles de ejecución simbólica, uso de `z3-solver`, arquitectura de enteros y strings concólicos (`zint`, `zstr`), negación sistemática de prefijos y límites ante explosión de caminos en ciclos y funciones criptográficas.
12. [[12-Análisis dinámico y perfilado de ejecución/_Índice|Análisis dinámico y perfilado de ejecución]] — Localización de *hotspots*, implementación de `FunctionInstrumentor` y `Profiler` manejando múltiples `return` y recursividad, *Execution Sampling* con `sys._current_frames()`, construcción del *Calling Context Tree (CCT)*, *Efecto del Observador* y sesgo de período constante $K$.

### Organización y Síntesis
13. [[13-Gestión del curso/_Índice|Gestión del curso]] — Programa oficial, ponderaciones y requisitos de aprobación/eximición, y guía integradora de estudio para las interrogaciones y el examen.
