---
ramo: "Testing"
tema: "Análisis de mutación y diseño de pruebas de caja negra"
tags:
  - testing/analisis-de-mutacion-y-diseno-de-pruebas-de-caja-negra
  - indice
---

# Análisis de mutación y diseño de pruebas de caja negra

Evaluación de la efectividad real de una batería de pruebas mediante **Mutation Testing** (sembrado de defectos artificiales, operadores de mutación, cálculo del *mutation score*, hipótesis teóricas y problema de los mutantes equivalentes) y diseño sistemático de casos de prueba de **caja negra** a partir de la especificación: partición de equivalencia (PE), análisis de valores límite (BVA de $2$ y $3$ puntos), tablas de decisión y pruebas de transición de estados (*0-switch* y *1-switch coverage*).

## Contenido del tema

1. [[01 - Mutation Testing operadores de mutación y cálculo del mutation score]] — Por qué el $100\%$ de cobertura no garantiza buenos oráculos (`strong_suite` vs. `weak_suite` en `triangle`), operadores de mutación, cálculo del *mutation score* ajustado y resolución del caso `distance(dx, dy)`.
2. [[02 - Hipótesis del mutation testing mutantes equivalentes y mutación con LLMs]] — Hipótesis del programador competente, vecindad finita y efecto de acoplamiento; por qué detectar mutantes equivalentes es indecidible; y comparación entre mutadores mecánicos clásicos y mutantes generados con LLMs.
3. [[03 - Pruebas de caja negra partición de equivalencia y valores límite]] — Clases de equivalencia válidas e inválidas, por qué probar inválidas por separado, y análisis de valores límite de $2$ puntos (*two-point*) y $3$ puntos (*three-point*) con ejercicios resueltos.
4. [[04 - Tablas de decisión combinaciones de reglas y colapso de tablas]] — Construcción de matrices de $2^n$ reglas, colapso de condiciones indiferentes (`—`) en préstamos bancarios y manejo de combinaciones imposibles (`X`) en descuentos.
5. [[05 - Pruebas de transición de estados cobertura 0-switch y 1-switch]] — Modelado con máquinas de estados finitas, diagrama de estados frente a tabla Estado $\times$ Evento para cazar transiciones inválidas, y cálculo de cobertura *0-switch* y *1-switch*.

