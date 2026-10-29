---
ramo: "Testing"
tema: "Análisis dinámico y perfilado de ejecución"
tags:
  - testing/analisis-dinamico-y-perfilado-de-ejecucion
  - indice
---

# Índice — Análisis dinámico y perfilado de ejecución

Unidad dedicada al **profiling** de programas para localizar cuellos de botella (*hotspots*) mediante las dos técnicas fundamentales de análisis dinámico: **perfilado por instrumentación AST** y **perfilado por muestreo estadístico (*Execution Sampling*)**.

## Contenido de la unidad

1. [[01 - Qué es el profiling y perfilado por instrumentación con AST]] — Concepto de *hotspots*, diferencias entre instrumentación y muestreo, diseño de `FunctionProfiler` y conteo exacto de llamadas y *callers*.
2. [[02 - Implementación de FunctionInstrumentor manejo de return y recursión]] — Arquitectura completa del proyecto `instrumentor`: inyección de `Profiler.record_start`, envoltura de sentencias `return` con `Profiler.record_end` y manejo de funciones recursivas sin pisar tiempos de inicio.
3. [[03 - Perfilado por muestreo Execution Sampling y Calling Context Tree]] — Captura no intrusiva de la pila de llamadas con `sys._current_frames()`, diferencia entre *Call Graph* y *Calling Context Tree (CCT)*, y lectura de contadores inclusivos frente a exclusivos.
4. [[04 - Instrumentación frente a muestreo efecto del observador y sesgo de período constante]] — Comparativa exhaustiva de precisión vs. *overhead*, el *Efecto del Observador* en funciones pequeñas muy frecuentes y el sesgo de sincronización al usar un período de muestreo constante $K$.
