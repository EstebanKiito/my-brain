---
ramo: Ingeniería de Software
tema: Arquitectura de software
tags: [ingsoft/arquitectura, origen/complemento]
prerrequisitos: ["[[01 - Arquitectura de software|Arquitectura de software]]", "[[01 - Protocolo HTTP|Protocolo HTTP]]"]
---
# Arquitectura cliente-servidor

> [!tip] Complemento — nota nueva (fuente: slides "Arquitecturas Comunes")
> **Qué es:** el sistema se divide en **clientes**, que piden, y **servidores**, que atienden las solicitudes a través de la red (normalmente con HTTP).
>
> ![Slide - cliente y servidor](adjuntos/Slide%20-%20cliente%20y%20servidor.png)
>
> **Clientes:**
> - Una máquina o un programa capaz de **enviar solicitudes (requests)** a través de internet.
> - No necesariamente un navegador (también Postman o una app móvil).
> - Un computador puede tener varios clientes.
>
> **Servidor:**
> - No es necesariamente un dispositivo físico.
> - Las computadoras de alto rendimiento se llaman servidores porque ejecutan **programas que dan servicios** (por ejemplo, Apache o una app Rails).
> - Un servidor puede atender **múltiples clientes al mismo tiempo**.
>
> **Niveles (tiers):**
> | Arquitectura | Dónde está cada parte |
> |---|---|
> | **1 nivel** (one-tier) | presentación, aplicación y datos en la misma máquina |
> | **2 niveles** (two-tier) | cliente (presentación + lógica) ↔ servidor de base de datos |
> | **3 niveles** (three-tier) | cliente ↔ **servidor de aplicación** ↔ servidor de base de datos |
>
> ![Slide - arquitectura de tres niveles](adjuntos/Slide%20-%20arquitectura%20de%20tres%20niveles.png)
>
> Una app Rails típica es de **3 niveles**: navegador → servidor Rails → PostgreSQL.

## Preguntas de repaso

1. ¿Qué es un cliente en la arquitectura cliente-servidor?
> [!question]- Respuesta
> Una máquina o programa que envía solicitudes a un servidor a través de la red, como un navegador, Postman o una app.

2. ¿Qué diferencia a una arquitectura de 2 niveles de una de 3?
> [!question]- Respuesta
> En 2 niveles, el cliente habla directamente con el servidor de base de datos. En 3, hay un servidor de aplicación intermedio con la lógica de negocio.

3. ¿Un servidor atiende a un solo cliente a la vez?
> [!question]- Respuesta
> No, puede atender múltiples clientes al mismo tiempo.
