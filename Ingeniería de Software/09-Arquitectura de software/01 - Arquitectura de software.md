---
ramo: Ingeniería de Software
tema: Arquitectura de software
tags: [ingsoft/arquitectura, origen/complemento]
prerrequisitos: ["[[01 - Buen diseño de software|Buen diseño de software]]", "[[03 - Patrón MVC en Rails|Patrón MVC en Rails]]"]
---
# Arquitectura de software

*Mi lista de contenidos de la prueba práctica nombraba "Arquitectura" y "Arquitectura Software", pero sin notas; este tema se arma con las slides "Arquitecturas Comunes".*

> [!tip] Complemento — nota nueva (fuente: slides "Arquitecturas Comunes")
> **Qué es:** la arquitectura es la **estructura de alto nivel** de un sistema: qué componentes tiene, cómo se comunican y dónde se ejecutan. Son las decisiones **caras de cambiar después**.
>
> **¿Qué es arquitectura de software? (slides)**
> - Centrarse en la **estructura**.
> - **Anticiparse** a decisiones costosas.
> - Hacer **explícitas las decisiones** para tener una buena calidad.
>
> **Requisitos (no funcionales) de un sistema moderno ("siglo 2021"):**
> | Requisito | Atributo de calidad |
> |---|---|
> | Que se desarrolle y mantenga por muchos años | **Maintainability** (mantenibilidad) |
> | Que soporte millones de usuarios | **Scalability** (escalabilidad) |
> | Que esté disponible 24/7 | **Reliability** (confiabilidad) |
> | Que tenga buena latencia | **Efficiency** (eficiencia) |
>
> **Un poco de historia** de la comunicación entre sistemas distribuidos:
>
> ![Slide - historia de las arquitecturas distribuidas](adjuntos/Slide%20-%20historia%20de%20las%20arquitecturas%20distribuidas.png)
>
> RPC (*Remote Procedure Call*, 1981) → CORBA (1991) → SOAP (1998) → REST (*Representational State Transfer*, 2000) → GraphQL (2011).
>
> **Arquitecturas comunes vistas en clase:**
> 1. [[02 - Arquitectura cliente-servidor|Cliente-servidor]] (y arquitecturas de 1, 2 y 3 niveles)
> 2. [[03 - Arquitectura en capas|En capas]]
> 3. [[05 - Arquitectura orientada a servicios (SOA)|Orientada a servicios (SOA)]]
> 4. [[06 - Microservicios|Microservicios]]
>
> Además: el [[04 - Escalamiento y teorema CAP|escalamiento]] y la implementación con [[07 - Contenedores con Docker y Kubernetes|contenedores]].
>
> **Arquitectura vs. diseño:** la arquitectura decide la estructura global (por ejemplo, microservicios con una base de datos cada uno); el diseño decide las clases dentro de un componente (por ejemplo, un Strategy en el módulo de pagos). [[03 - Patrón MVC en Rails|MVC]] es un patrón arquitectónico de la capa de presentación.

## Preguntas de repaso

1. ¿Qué caracteriza a las decisiones de arquitectura?
> [!question]- Respuesta
> Definen la estructura global del sistema y son costosas de cambiar más adelante, por eso hay que anticiparlas y hacerlas explícitas.

2. Nombra cuatro atributos de calidad que guían la arquitectura de un sistema moderno.
> [!question]- Respuesta
> Mantenibilidad, escalabilidad, confiabilidad (disponibilidad 24/7) y eficiencia (baja latencia).

3. Ordena cronológicamente: REST, RPC, GraphQL, SOAP, CORBA.
> [!question]- Respuesta
> RPC (1981), CORBA (1991), SOAP (1998), REST (2000), GraphQL (2011).
