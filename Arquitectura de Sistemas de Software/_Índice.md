---
ramo: "Arquitectura de Sistemas de Software"
tags:
  - arquisis/indice
  - indice
---

# Arquitectura de Sistemas de Software (IIC2173)

Curso sobre cómo tomar decisiones de arquitectura: qué características necesita un sistema, qué estilos y patrones las logran, cómo se diagraman y cómo se integran, se aceleran y se escalan. Las notas están escritas para estudiar: cada concepto va con su porqué, su costo, ejemplos y preguntas tipo prueba.

> [!tip] Ruta de estudio para la I2
> La I2 evalúa todo hasta Escalabilidad, con foco teórico en lo nuevo. Un orden que funciona:
> 1. **Integración** (14 → 17). Termina en [[05 - Cómo elegir el mecanismo de integración]], que resume todo el bloque en una tabla y un árbol de decisión.
> 2. **DDD táctico** (18). La pregunta guía es *¿qué debe ser cierto a la vez?*
> 3. **Performance** (19 → 22). Las tácticas de [[03 - Tácticas de performance de Bass y Kazman]] y la caché son lo más preguntado.
> 4. **Escalabilidad** (23 → 25). Practicar los cálculos de [[03 - Leyes de Little Amdahl y Gustafson]] y no confundir sharding, partitioning y leader-follower.
> 5. Repasar las preguntas de repaso de cada nota y, al final, los casos resueltos.

## Fundamentos características DDD estratégico UML y estilos

01. [[01-Fundamentos de la arquitectura de software/_Índice|Fundamentos de la arquitectura de software]] — Definiciones, analogía con la construcción, el rol del arquitecto, tradeoffs, ley de Conway y conocimiento de dominio.
02. [[02-Cohesión acoplamiento y connascence/_Índice|Cohesión acoplamiento y connascence]] — Cohesión, tipos de acoplamiento, connascence estática y dinámica, reglas de grado y localidad.
03. [[03-Componentes quanta y documentación/_Índice|Componentes quanta y documentación]] — Componente, quanta arquitectónica, vistas y ADR.
04. [[04-Características arquitectónicas y escenarios/_Índice|Características arquitectónicas y escenarios]] — Stakeholders, tipos de NFR, cómo priorizar, escenarios de seis partes, decisiones relevantes y tácticas.
05. [[05-Atributos estructurales/_Índice|Atributos estructurales]] — Mantenibilidad, flexibilidad, inyección de dependencias, portabilidad e interoperabilidad.
06. [[06-Atributos operacionales/_Índice|Atributos operacionales]] — Performance y escalabilidad como requisitos, confiabilidad y disponibilidad con cálculo de nueves.
07. [[07-Atributos transversales/_Índice|Atributos transversales]] — Elasticidad, seguridad, reusabilidad, soporte, eficiencia, usabilidad y McCall.
08. [[08-DDD estratégico/_Índice|DDD estratégico]] — Dominio, subdominios core, support y genéricos, bounded contexts, lenguaje ubicuo, context map y el ejercicio VoltVecino.
09. [[09-Diagramación y UML de componentes/_Índice|Diagramación y UML de componentes]] — ADL, 4+1, C4, variantes UML, notación del diagrama de componentes y método con descuentos de pauta.
10. [[10-Estilos jerárquicos y de capas/_Índice|Estilos jerárquicos y de capas]] — Estilo frente a patrón, monolito, main y subrutinas, capas, máquina virtual, cliente-servidor y microkernel.
11. [[11-Flujo de datos e invocación implícita/_Índice|Flujo de datos e invocación implícita]] — Lotes secuenciales, pipe and filter, EDA, mediator frente a broker y pub/sub.
12. [[12-Arquitecturas orientadas a servicios/_Índice|Arquitecturas orientadas a servicios]] — SOA, su historia y el bus, servicio compartido como acoplamiento, microservicios y sus costos.
13. [[13-Otros estilos arquitectónicos/_Índice|Otros estilos arquitectónicos]] — Intérprete, código móvil, reglas, pizarra, P2P y tabla para elegir estilos.

## Integración DDD táctico performance y escalabilidad

14. [[14-Integración y relaciones entre contextos/_Índice|Integración y relaciones entre contextos]] — Integrabilidad, context map, las siete relaciones de DDD y tácticas básicas de integración.
15. [[15-Middleware orientado a mensajes/_Índice|Middleware orientado a mensajes]] — Monolito y comunicación indirecta, MOM, colas vs logs, broker, motores de procesos, orquestación vs coreografía.
16. [[16-REST y contratos de API/_Índice|REST y contratos de API]] — REST como estilo, árbol de derivación, componentes y conectores, interfaz uniforme, madurez de Richardson y OpenAPI.
17. [[17-gRPC GraphQL y MCP/_Índice|gRPC GraphQL y MCP]] — gRPC, GraphQL, MCP, evolución de contratos, outbox y cómo elegir el mecanismo de integración.
18. [[18-DDD táctico/_Índice|DDD táctico]] — Entidades, objetos de valor, agregados, repositorios, servicios, eventos de dominio e integración y arquitectura hexagonal.
19. [[19-Fundamentos de performance/_Índice|Fundamentos de performance]] — Definición y métricas de performance, percentiles, escenarios, medición experimental y teórica, y tácticas de Bass y Kazman.
20. [[20-Hardware red y performance/_Índice|Hardware red y performance]] — CPU, RAM, almacenamiento, GPU y TPU, falacias de la red y el caso Amazon Prime Video.
21. [[21-Caché y protocolos web/_Índice|Caché y protocolos web]] — Caché (desafíos, desalojo, cuándo no usarla), caché web con navegador, proxy y CDN, y HTTP/1 a HTTP/3.
22. [[22-Asincronía y control de demanda/_Índice|Asincronía y control de demanda]] — Contenedores, caso Twitter, asincronía y NodeJS, rate limiting, circuit breakers, timeouts y priorización.
23. [[23-Medición de escalabilidad/_Índice|Medición de escalabilidad]] — Definición, escenarios, cuellos de botella, métricas, tipos de pruebas y leyes de Little, Amdahl y Gustafson.
24. [[24-Métodos de escalabilidad/_Índice|Métodos de escalabilidad]] — Vertical y horizontal, balanceo, modelación de componentes, conectores y configuraciones, Instagram, serverless, frontend y nube.
25. [[25-Escalabilidad de datos/_Índice|Escalabilidad de datos]] — Índices, CAP y BASE, sharding y partitioning, caché y leader-follower, Google, Hadoop y Aurora.

## Práctica infraestructura y gestión

26. [[26-Resolución de casos de diseño/_Índice|Resolución de casos de diseño]] — Método de respuesta y casos resueltos de pruebas pasadas con sus pautas y diagramas de referencia.
27. [[27-Infraestructura y despliegue en la nube/_Índice|Infraestructura y despliegue en la nube]] — Cloud y AWS, Linux y SSH, Docker y Compose, DNS, nginx y reverse proxy, S3 con CloudFront e IaaC.
28. [[28-Gestión del curso/_Índice|Gestión del curso]] — 2 notas: evaluaciones y cálculo de la nota; qué entra en cada prueba y cómo estudiar.
