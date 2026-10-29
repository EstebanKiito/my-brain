---
ramo: "Testing"
tema: "Cobertura de código e instrumentación con settrace"
tags:
  - testing/cobertura-de-codigo-e-instrumentacion-con-settrace
  - indice
---

# Cobertura de código e instrumentación con settrace

Fundamentos del testing de caja blanca y medición automática de cobertura estructural en Python: distinción entre cobertura de funciones, sentencias (*statement coverage*) y decisiones o ramas (*decision / branch coverage*), instrumentación dinámica del intérprete mediante `sys.settrace` e inspección de marcos de pila (`frame`), construcción del administrador de contexto `Coverage`, álgebra de conjuntos para localizar código no probado y análisis crítico de los límites de la cobertura.

## Contenido del tema

1. [[01 - Pruebas de caja blanca y métricas de cobertura estructural]] — Enfoque de caja blanca, ventajas y ceguera ante errores de omisión, fórmula general de cobertura y análisis estructural de `cgi_decode`.
2. [[02 - Cobertura de sentencias frente a cobertura de ramas]] — Por qué el $100\%$ de *statement coverage* puede ocultar decisiones al $50\%$ en condicionales sin `else`, y cálculo manual paso a paso sobre `clasificar_impuesto`.
3. [[03 - Rastreo de ejecución en Python con sys settrace y frames de pila]] — Funcionamiento de `sys.settrace(trace_func)`, anatomía de `frame`, `event` y `arg`, importancia de retornar el callback y visualización línea por línea con `inspect.getsource`.
4. [[04 - La clase Coverage diferencias de conjuntos y límites de la cobertura]] — Implementación de `Coverage` con `__enter__` y `__exit__`, resta de conjuntos ($A - B$) para aislar líneas exclusivas o pendientes, límites de la cobertura sin oráculo (`dias_en_mes`) y predicción estática con LLMs.
