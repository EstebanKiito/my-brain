---
ramo: "Arquitectura de Sistemas de Software"
tema: "Flujo de datos e invocación implícita"
tags:
  - arquisis/estilos
  - indice
---

# Índice — Flujo de datos e invocación implícita

Los estilos de **flujo de datos** (por lotes secuencial y **pipe and filter**, con la trampa de filtrar frente a procesar) y de **invocación implícita**: **EDA**, sus invariantes, workers, pros y contras, las topologías **mediator** y **broker** (orquestación y coreografía) y **pub/sub** con MQTT.

## Contenido

1. [[01 - Flujo de datos por lotes y pipe and filter]] — Lotes secuenciales frente a capas, pipe and filter con pipes de Linux, ETL y UML, pros y contras, y cuándo las pautas lo aceptan.
2. [[02 - Invocación implícita y arquitectura orientada a eventos]] — Anunciar en vez de llamar, componentes, invariantes, el patrón de workers, pros y contras, e idempotencia.
3. [[03 - Topologías mediator y broker y el estilo pub sub]] — Mediator con orquestación y trazabilidad, el bus de eventos gestionado, broker con coreografía, pub/sub, MQTT y el V/F de pub/sub.
