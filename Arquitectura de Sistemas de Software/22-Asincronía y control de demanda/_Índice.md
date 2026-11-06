---
ramo: "Arquitectura de Sistemas de Software"
tema: "Asincronía y control de demanda"
tags:
  - arquisis/performance
  - indice
---

# Índice — Asincronía y control de demanda

Cómo los **contenedores** mejoran el uso de recursos, la evolución de **Twitter** de un monolito saturado a cientos de servicios (y su costo), la **asincronía** como forma de mejorar la performance percibida con el modelo de **NodeJS**, y las tácticas de **control de demanda**: rate limiting, WAF, circuit breakers, timeouts y priorización.

## Contenido

1. [[01 - Contenedores y el caso Twitter]] — Contenedores y utilización de recursos, Twitter en 2007, la transición a la JVM y a servicios, y las 1.200 RPC que hacían lenta la app.
2. [[02 - Asincronía y el modelo de NodeJS]] — Invocar sin esperar, petición-respuesta asíncrona, pros y contras, loop de eventos de NodeJS, sus usos y dónde no conviene.
3. [[03 - Control de demanda con rate limiting circuit breakers y prioridades]] — Throttling, WAF, estados del circuit breaker, reintentos con jitter, timeouts, priorización de eventos y la ausencia de bala de plata.
