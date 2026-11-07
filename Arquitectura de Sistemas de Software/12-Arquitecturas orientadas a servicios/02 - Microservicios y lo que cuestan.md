---
ramo: "Arquitectura de Sistemas de Software"
tema: "Arquitecturas orientadas a servicios"
tags:
  - arquisis/estilos
  - arquisis/servicios
  - origen/complemento
prerrequisitos:
  - "[[01 - SOA historia y el bus de servicios]]"
  - "[[06 - Microservicios]]"
---

# Microservicios y lo que cuestan

El mayor problema de SOA era que cada servicio terminaba siendo muy grande. De ahí nacen los **microservicios**: servicios pequeños, contratos explícitos y sin bus inteligente. Pero cada frontera de servicio tiene un costo concreto, y la pregunta que el curso exige responder es **qué requisito justifica pagarlo**.

## Qué es (y qué no)

> [!tip] Microservicio
> Es la **unidad de despliegue de un bounded context** que tiene **requisitos propios** de disponibilidad, de escalamiento o de cadencia de despliegue. **Sin ese requisito, ese mismo contexto es un módulo del monolito y no pierde nada.**

- Históricamente es una **reacción a SOA**: servicios pequeños, contratos explícitos y **smart endpoints, dumb pipes**.
- **Ejemplo:** Storefront, Account, Inventory y Shipping, **cada uno con su base de datos**.
- **Anti-ejemplo:** Users, Threads, Posts: **un servicio por sustantivo de la base de datos** (por tabla), no por contexto.

![Microservicios con base propia detrás de una API Gateway](adjuntos/Microservicios%20con%20base%20propia%20detrás%20de%20una%20API%20Gateway.png)

> [!example]- Transcripción de la imagen
> - Tres microservicios, **MS1**, **MS2** y **MS3** (con "…" debajo), cada uno con su propia base de datos.
> - Todos se conectan por interfaces a una **API Gateway** vertical, que expone una sola interfaz hacia afuera.

## Reuso frente a uso

- **Reuso no es lo mismo que uso:** reutilizar exige un contrato estable para todos; usar exige uno para mí.
- La respuesta de los microservicios es **preferir la duplicación al acoplamiento**: **DRY dentro de un bounded context, duplicación entre contextos**.
- **Lo que sí se comparte es la infraestructura** (autenticación, logs, sidecar), **no el dominio**.
- La **frontera del contexto** decide qué se duplica, no el afán de no repetir código.

## Lo que se multiplica por N

Las consideraciones de EDA y del proyecto (contratos, entrega, idempotencia, monitoreo) ya se pagan **por mensaje**. Con microservicios se pagan además **por servicio**: pipelines de CI/CD, bases de datos, **superficies de ataque** y turnos de guardia (*on-call*). **Cambia la unidad de cobro, no la lista de costos.**

### Cuatro facturas por cada frontera

| Factura | Qué significa |
|---|---|
| **Datos** | La consistencia eventual deja de ser entre consumidores y pasa a ser **entre los propios datos** del sistema |
| **Fallas parciales** | Un servicio caído es la mitad de una transacción |
| **Observabilidad** | Una petición cruza N procesos: hay que trazarla |
| **Descubrimiento y despliegue** | Quién está dónde, y cómo se actualiza uno sin bajar a los otros |

## Lo que exige de la organización

- **Ley de Conway:** la estructura del sistema copia la de los equipos. **Un servicio por equipo, no por tabla.**
- ***You build it, you run it***, idealmente con apoyo de un equipo DevOps: CI/CD, on-call y observabilidad por servicio (cultura DevSecOps).
- **Diseñar para fallar:** la red falla, así que cada servicio asume que el otro no está.
- **Consumer-first:** el contrato lo define quien consume (*consumer-driven contracts*).

## Patrones en microservicios

Necesitan muchos patrones para funcionar:
- **Saga:** transacciones distribuidas con compensaciones.
- **Sidecar:** un proceso auxiliar junto a cada servicio (logs, proxy, seguridad).
- **CQRS:** separar el modelo de escritura del de lectura.
- **Circuit breaker:** dejar de llamar a un servicio que falla.
- **Anti-corruption layer** (de DDD).
- **Event sourcing:** guardar los eventos como fuente de verdad.

Según cómo se coordinen, los microservicios se conectan por **orquestación** o por **coreografía**. Ver [[05 - Orquestación frente a coreografía]].

> [!warning] Microservicios sin requisito
> Proponer microservicios "porque escalan" sin un requisito concreto de cadencia, escala o fallas propias es pagar las cuatro facturas sin beneficio. Además, si los servicios se llaman todos entre sí de forma síncrona, no son quantas independientes: es un *big ball of distributed mud*. Las pautas aceptan microservicios **solo si se justifica la división** del backend en subsistemas.

> [!tip] Tips para la prueba de diagramación
> Para cada componente y estilo hay que dejar claro: las **responsabilidades** previas (qué atributos y qué estilos se eligieron), los **estilos** reflejados en el diagrama, las **interfaces** con nombre y las **funcionalidades** del enunciado cubiertas.

## Preguntas de repaso

> [!question]- Según el curso, ¿qué es un microservicio y cuándo no se justifica?
> Es la unidad de despliegue de un bounded context con requisitos propios de disponibilidad, escalamiento o cadencia. Si no tiene esos requisitos, el contexto debería ser un módulo del monolito, porque separarlo solo agrega costos.

> [!question]- ¿Por qué "un servicio por tabla" es un antipatrón?
> Porque las tablas no son fronteras de negocio: las operaciones normales cruzan varias tablas, así que los servicios terminarían llamándose todo el tiempo y compartiendo transacciones. Las fronteras deben seguir los bounded contexts y los equipos.

> [!question]- Explique "DRY dentro de un contexto, duplicación entre contextos".
> Dentro de un bounded context se evita repetir lógica, porque la cambia el mismo equipo. Entre contextos se prefiere duplicar lo poco que se necesita, porque compartirlo crea acoplamiento entre equipos y despliegues. Solo la infraestructura se comparte.

> [!question]- Nombre las cuatro facturas que cobra cada frontera de servicio.
> Datos (consistencia eventual entre los propios datos), fallas parciales (un servicio caído deja transacciones a medias), observabilidad (una petición cruza N procesos) y descubrimiento y despliegue (ubicar servicios y actualizarlos sin bajar a los otros).

> [!question]- ¿Qué exige de la organización trabajar con microservicios?
> Un servicio por equipo (ley de Conway), que cada equipo opere lo que construye (CI/CD, on-call, observabilidad), diseñar asumiendo que los otros servicios fallan y contratos definidos por los consumidores.

> [!question]- Nombre cuatro patrones de microservicios y qué resuelve cada uno.
> Saga (transacciones distribuidas con compensaciones), circuit breaker (no seguir llamando a un servicio caído), sidecar (funcionalidad transversal junto a cada servicio) y CQRS (separar escrituras y lecturas para escalarlas por separado).

> [!question]- Mini caso: una startup de 3 desarrolladores con un e-commerce pequeño quiere 10 microservicios. ¿Qué responde?
> Que no se justifica: con un solo equipo no hay diferencias de cadencia, y probablemente tampoco de escala. Pagaría 10 veces los pipelines, las bases, el monitoreo y las fallas parciales. Conviene un monolito modular por bounded context y separar solo cuando un requisito lo exija.
