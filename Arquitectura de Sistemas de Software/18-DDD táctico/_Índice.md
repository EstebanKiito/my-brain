---
ramo: "Arquitectura de Sistemas de Software"
tema: "DDD táctico"
tags:
  - arquisis/ddd
  - indice
---

# Índice — DDD táctico

Qué hay **dentro** de un bounded context: entidades y objetos de valor, **agregados** como límites de consistencia, repositorios y fábricas, servicios de dominio y de aplicación, eventos de dominio frente a eventos de integración, y la **arquitectura hexagonal** que protege al dominio. La pregunta guía es *¿qué debe ser cierto al mismo tiempo?*

## Contenido

1. [[01 - Entidades y objetos de valor]] — Identidad frente a valor, inmutabilidad, Address y Dinero, primitive obsession y la regla de intercambiabilidad.
2. [[02 - Agregados y raíz del agregado]] — Invariante, raíz del agregado, una transacción por agregado, referencias por id, consistencia eventual y UserEntity en código.
3. [[03 - Diseñar agregados y sus antipatrones]] — Agregados chicos y el test de la misma transacción, agregado gigante, modelo anémico y señales de un sistema sin DDD táctico.
4. [[04 - Repositorios fábricas y servicios de dominio y aplicación]] — Repositorio por raíz como puerto, fábricas, servicio de dominio frente a servicio de aplicación y dónde va la transacción.
5. [[05 - Eventos de dominio y eventos de integración]] — Eventos en pasado y lenguaje ubicuo, manejo dentro del contexto, traducción a evento de integración versionado y outbox.
6. [[06 - Arquitectura hexagonal con puertos y adaptadores]] — Dominio al centro, puertos, adaptadores primarios y secundarios, regla de dependencia, estructura de domain-driven-hexagon y fitness function.
