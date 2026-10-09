---
ramo: Ingeniería de Software
tema: Arquitectura de software
tags: [ingsoft/arquitectura, origen/complemento]
prerrequisitos: ["[[05 - Arquitectura orientada a servicios (SOA)|Arquitectura orientada a servicios (SOA)]]", "[[04 - Escalamiento y teorema CAP|Escalamiento y teorema CAP]]"]
---
# Microservicios

> [!tip] Complemento — nota nueva (fuente: slides "Arquitecturas Comunes")
> **Qué es:** la aplicación se divide en **servicios pequeños y autónomos**, cada uno con una responsabilidad de negocio, **su propia base de datos** y su propio despliegue. Se comunican por la red (HTTP/REST o mensajería).
>
> ![Slide - microservicios vs aplicación tradicional](adjuntos/Slide%20-%20microservicios%20vs%20aplicación%20tradicional.png)
>
> | | Aplicación tradicional (monolito) | Microservicios |
> |---|---|---|
> | Estructura | la mayor parte de la funcionalidad en **un solo proceso**, en capas | funcionalidad separada en **pequeños servicios autónomos** |
> | Escala | **clonando la aplicación completa** en varios servidores o VMs | **desplegando y replicando cada servicio de forma independiente** |
> | Base de datos | una única base monolítica | **una base de datos por microservicio** (*stateless* + *stateful services*) |
>
> **SOA vs. microservicios:** en SOA los servicios se comunican por un **Enterprise Service Bus** y comparten bases de datos. En microservicios no hay bus central "inteligente" y cada uno tiene su propia base.
>
> **Comunicación por mensajes (Kafka):**
>
> ![Slide - Kafka productor broker consumidor](adjuntos/Slide%20-%20Kafka%20productor%20broker%20consumidor.png)
>
> - Un **productor** publica mensajes en un **broker** (un *message log*).
> - Los **consumidores** los leen cuando pueden.
> - En Kafka, el broker es un **clúster de máquinas** con particiones (A, B, C) y los consumidores se agrupan en *groups*. Así los servicios se comunican de forma **asíncrona** y desacoplada (la misma idea del [[05 - Patrón Observer|Observer]], a escala de sistema).
>
> **Ventajas:** escalar solo lo necesario, desplegar independientemente, equipos autónomos por servicio, tecnologías distintas por servicio.
>
> **Costos:** complejidad de un sistema distribuido (red, fallas parciales, CAP), consistencia de datos entre servicios, observabilidad y despliegue (de ahí [[07 - Contenedores con Docker y Kubernetes|Docker y Kubernetes]]).

## Preguntas de repaso

1. ¿Cómo escala un monolito y cómo escalan los microservicios?
> [!question]- Respuesta
> El monolito se escala clonando la aplicación completa. Los microservicios se escalan replicando de forma independiente solo los servicios que lo necesitan.

2. Nombra dos diferencias entre SOA y microservicios.
> [!question]- Respuesta
> SOA usa un Enterprise Service Bus central y los servicios comparten bases de datos. En microservicios no hay bus central y cada servicio tiene su propia base de datos.

3. ¿Para qué sirve un broker de mensajes como Kafka?
> [!question]- Respuesta
> Para que los servicios se comuniquen de forma asíncrona: los productores publican mensajes y los consumidores los leen, sin conocerse directamente. Esto reduce el acoplamiento.
