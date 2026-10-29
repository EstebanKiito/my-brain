---
ramo: "Testing"
tema: "Fuzzing aleatorio y fuzzing basado en mutación"
tags:
  - testing/fuzzing-aleatorio-y-fuzzing-basado-en-mutacion
  - indice
---

# Fuzzing aleatorio y fuzzing basado en mutación

Generación automática y masiva de entradas de prueba mediante *fuzzing*: desde el enfoque aleatorio puro (`RandomFuzzer`) y por qué fracasa estadísticamente frente a entradas estructuradas, pasando por el diseño de mutadores a nivel de carácter (`delete`, `insert`, `flip`), el apilamiento iterativo de mutaciones entre `min_mutations` y `max_mutations` en `MutationFuzzer`, hasta el *greybox fuzzing* guiado por cobertura (`MutationCoverageFuzzer`) que evoluciona un *corpus* de semillas para explorar caminos nuevos del programa.

## Contenido del tema

1. [[01 - Fuzzing aleatorio y sus límites ante entradas estructuradas]] — Concepto de *fuzzing*, oráculos implícitos, implementación de `RandomFuzzer` y demostración probabilística de por qué la aleatoriedad pura choca contra validadores estructurados como `validate_url`.
2. [[02 - Fuzzing por mutación operadores de strings y apilamiento de mutaciones]] — Partir de una semilla válida (*seed input*), los tres operadores clásicos de strings, su efecto sobre invariantes de entrada (`validar_pin`) y el rol exacto de `min_mutations` y `max_mutations` al apilar $K$ mutaciones sucesivas.
3. [[03 - Fuzzing por mutación guiado por cobertura]] — Retroalimentación con `Coverage` en `MutationCoverageFuzzer`, construcción automática de un *corpus* que alcanza $100\%$ de cobertura en `validate_url` y límites del enfoque frente a condiciones exactas.
