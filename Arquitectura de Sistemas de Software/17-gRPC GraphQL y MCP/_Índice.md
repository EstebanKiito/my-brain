---
ramo: "Arquitectura de Sistemas de Software"
tema: "gRPC GraphQL y MCP"
tags:
  - arquisis/integracion
  - indice
---

# Índice — gRPC GraphQL y MCP

Los contratos alternativos a REST: **gRPC** para velocidad entre módulos, **GraphQL** para consultas definidas por el cliente y **MCP** cuando el cliente es un modelo de IA. Además, cómo evolucionar contratos sin romper consumidores, el patrón **outbox** y una guía para **elegir el mecanismo** de integración en un caso.

## Contenido

1. [[01 - gRPC y protobuf para comunicación entre módulos]] — RPC con protobuf sobre HTTP/2, streaming, pros y contras, dónde usarlo y la regla eficiencia dentro del contexto e independencia entre contextos.
2. [[02 - GraphQL y consultas definidas por el cliente]] — Schema con queries, mutaciones y suscripciones, overfetching y underfetching, pros y contras, seguridad del endpoint y cuándo elegirlo.
3. [[03 - MCP e integración de componentes no deterministas]] — MCP (tools, resources, prompts sobre JSON-RPC) y las tácticas para integrar servicios con modelos adentro: validar, reintentar, presupuesto y fallback.
4. [[04 - Evolución de contratos tests de contrato y outbox]] — Cambios aditivos, lector tolerante, deprecación y versionado, tests de contrato con Pact, outbox y la tabla relación-mecanismo-contrato.
5. [[05 - Cómo elegir el mecanismo de integración]] — Tabla comparativa de todos los mecanismos, árbol de decisión, estructura de una respuesta con puntaje y mini casos de pauta.
