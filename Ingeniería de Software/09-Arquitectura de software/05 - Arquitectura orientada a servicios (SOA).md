---
ramo: Ingeniería de Software
tema: Arquitectura de software
tags: [ingsoft/arquitectura, origen/complemento]
prerrequisitos: ["[[03 - Arquitectura en capas|Arquitectura en capas]]"]
---
# Arquitectura orientada a servicios (SOA)

> [!tip] Complemento — nota nueva (fuente: slides "Arquitecturas Comunes")
> **Qué es:** la aplicación se divide en **servicios de negocio** (cuentas, libros, órdenes, envíos) que se comunican a través de un bus central, el **Enterprise Service Bus (ESB)**.
>
> ![Slide - arquitectura orientada a servicios](adjuntos/Slide%20-%20arquitectura%20orientada%20a%20servicios.png)
>
> - **Consumers layer:** consumidores de servicios en la nube y navegadores (usuarios).
> - **Enterprise Service Bus (ESB):** el intermediario por el que pasan todas las comunicaciones. Enruta, transforma formatos y orquesta.
> - **Providers layer:** Account Service, Book Service, Order Service y Shipping Service.
> - Los servicios **comparten bases de datos**.
>
> **Características:**
> - servicios reutilizables con contratos bien definidos (históricamente con SOAP/XML);
> - el ESB concentra la lógica de integración, y por eso puede volverse un **cuello de botella** y un punto único de falla;
> - la diferencia con [[06 - Microservicios|microservicios]] está en esa nota.

## Preguntas de repaso

1. ¿Qué es el Enterprise Service Bus?
> [!question]- Respuesta
> Un componente central de SOA por el que pasan las comunicaciones entre consumidores y servicios: enruta, transforma y orquesta los mensajes.

2. ¿Qué riesgo tiene concentrar la integración en el ESB?
> [!question]- Respuesta
> Que se convierta en un cuello de botella y en un punto único de falla, además de acoplar los servicios a él.

3. En el diagrama de SOA, ¿cada servicio tiene su propia base de datos?
> [!question]- Respuesta
> No: los servicios comparten bases de datos. Esa es una diferencia con los microservicios.
