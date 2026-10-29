---
ramo: "Testing"
tema: "Fuzzing basado en búsqueda"
tags:
  - testing/fuzzing-basado-en-busqueda
  - indice
---

# Fuzzing basado en búsqueda

Generación automática de entradas de prueba formulada como un problema de optimización metaheurística (*Search-Based Software Testing*): diseño de funciones de aptitud (*fitness*) con gradiente, generación de vecindarios multidimensionales, algoritmo de ascenso de colina (*Hill Climbing*) y sus estrategias para escapar de óptimos locales y mesetas, derivación sistemática de distancia de ramas (*branch distance*) al estilo EvoSuite y evolución de poblaciones mediante algoritmos genéticos.

## Contenido del tema

1. [[01 - Formulación del testing como optimización y función de fitness]] — Paso del azar ciego a la búsqueda guiada, los tres ingredientes de un problema de búsqueda, paisaje y gradiente de la función de fitness y generación de vecindarios con producto cartesiano.
2. [[02 - Algoritmo Hill Climbing óptimos locales mesetas y reinicios aleatorios]] — Implementación de *Simple* y *Steepest Ascent Hill Climbing*, por qué la búsqueda se atasca en óptimos locales y mesetas, reinicios aleatorios, $(1+1)\text{EA}$ y análisis comparativo de funciones de fitness sobre `x > 100 and y > 100`.
3. [[03 - Distancia de ramas estilo EvoSuite y algoritmos genéticos]] — Reglas mecánicas de *branch distance* para predicados atómicos, compuestos (`and`, `or`, De Morgan para `not`) y ramas anidadas, y evolución de poblaciones con selección por torneo, cruce (*crossover*) y mutación gaussiana.
