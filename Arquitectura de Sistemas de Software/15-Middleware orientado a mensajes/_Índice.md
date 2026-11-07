---
ramo: "Arquitectura de Sistemas de Software"
tema: "Middleware orientado a mensajes"
tags:
  - arquisis/mom
  - indice
---

# Índice — Middleware orientado a mensajes

Por qué el monolito es el punto de partida, qué cambia al separar el sistema, y cómo el **Message Oriented Middleware** desacopla emisores y receptores: colas y logs, brokers que enrutan y transforman, motores de procesos y la elección entre **orquestación y coreografía**.

## Contenido

1. [[01 - Monolito y comunicación indirecta entre contextos]] — Monolito y monolito modular, cuándo partir (cadencia, escala, fallas) y el problema N×M de las integraciones punto a punto.
2. [[02 - Message Oriented Middleware y desacople temporal]] — MOM como servidor de colas, fire and forget con confirmación de entrega, pros y contras, escalar con réplicas, quórum y particiones, EventBridge.
3. [[03 - Colas frente a logs de eventos]] — Cola vs log, offsets y replay, cuándo usar cada uno, costos, particiones y réplicas al estilo Kafka.
4. [[04 - Broker de ruteo y transformación y motores de procesos]] — Broker que enruta y transforma (dumb pipes), motores de procesos con estado (Airflow, Camunda) y la herencia de SOA (ESB y modelo canónico).
5. [[05 - Orquestación frente a coreografía]] — Diferencias, atributo que sacrifica cada una, relación con mediator y broker de EDA, y dos casos resueltos de pauta.
