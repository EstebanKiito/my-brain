---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/modelos
  - redes/osi
  - redes/tcp-ip
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/12-Fundamentos de redes y modelos en capas/01 - Arquitectura de Internet, nodos, enlaces y protocolos|01 - Arquitectura de Internet, nodos, enlaces y protocolos]]"
---

# Modelos de capas: modelo de referencia OSI frente al stack TCP-IP

El hardware de red resuelve solo la mitad de la tarea: además de mover bits, el mensaje tiene que llegar al **proceso** correcto. Para que algo tan complejo sea manejable, el software de redes se organiza en **capas**: cada una resuelve un problema específico, y esa separación de responsabilidades permite modelar e implementar sistemas complejos.

## Capas, servicios y protocolos

- Las capas se construyen a partir del **medio físico**, de abajo hacia arriba.
- Cada capa **atiende un problema específico** y funciona con un **protocolo** propio.
- Cada capa **entrega servicios a la capa superior** y **solicita servicios a la inferior**.
- Los mensajes pueden **modificarse en cada capa**: se les agregan *headers* o se transforma todo el mensaje.

Un **servicio** es el conjunto de primitivas que provee una funcionalidad hacia arriba; un **protocolo** son las reglas con que una capa conversa con su par del otro lado. Por eso el **protocolo de una capa se puede cambiar sin afectar el servicio** que reciben las demás.

![Comparación de modelos en capas OSI frente a TCP IP](adjuntos/Comparaci%C3%B3n%20de%20modelos%20en%20capas%20OSI%20frente%20a%20TCP%20IP.png)

> [!example]- Transcripción de la imagen
> "*Servicio*: conjunto de primitivas que provee una funcionalidad". Dos pilas, una a cada lado. En cada una, *Layer k* recibe servicios de *Layer k − 1* y ofrece el *Service provided by layer k* a *Layer k + 1*. Entre las dos *Layer k* hay una flecha punteada marcada *Protocol*.

> [!tip] Analogía: dos personas que no hablan el mismo idioma
> Dos personas quieren conversar (capa 3: mensaje entre personas). Cada una le pasa su mensaje a un traductor, y los traductores se ponen de acuerdo en un idioma común (capa 2: mensaje entre traductores). Los traductores se lo pasan a una secretaria que lo envía por fax (capa 1: envío físico). Si los traductores cambian de idioma común, las personas ni se enteran: el protocolo cambió, pero el servicio es el mismo.

## OSI frente a TCP/IP

El **modelo OSI** (ISO, *Open Systems Interconnection*, norma ISO/IEC 7498-1), propuesto en 1983 y revisado en 1995, es un **modelo de referencia**: define las **responsabilidades** de cada capa, pero **no define estándares, protocolos ni implementaciones**. La implementación práctica es el **stack TCP/IP** (modelo Internet), que nació como el stack de protocolos de ARPANET, un proyecto de investigación del Departamento de Defensa de EE. UU. Lo propusieron Vinton Cerf y Robert E. Kahn en 1974 y se estandarizó en 1989. Es más compacto: tiene **5 capas**.

| OSI (7 capas) | TCP/IP (5 capas) | Qué hace | Ejemplos |
|---|---|---|---|
| Aplicación | **Aplicación** | Los procesos intercambian **mensajes** | HTTP, SMTP, FTP, DNS, IMAP, POP, SSH |
| Presentación | (dentro de Aplicación) | Codificación, encriptación, serialización | — |
| Sesión | (dentro de Aplicación) | Sesión entre aplicaciones, autorización y autenticación | — |
| Transporte | **Transporte** | Lleva mensajes entre procesos de origen y destino | TCP, UDP |
| Red | **Red** | Lleva paquetes entre un par de hosts | IP |
| Enlace | **Enlace** | Transfiere datos entre nodos vecinos | Ethernet, Wi-Fi |
| Física | **Física** | Transmite los bits por el medio | Cobre, fibra, radio |

## La capa de aplicación

Funciona con los **procesos**: cuando se programan *sockets*, se trabaja en la capa de aplicación y se le piden servicios a la capa de transporte. Sus protocolos intercambian **mensajes**: HTTP (*HyperText Transfer Protocol*), SMTP (*Simple Mail Transfer Protocol*), FTP (*File Transfer Protocol*), DNS (*Domain Name System*), IMAP, POP, SSH, DHCP, Telnet, XMPP…

Las capas de **presentación y sesión** solo existen en OSI. En TCP/IP, si una aplicación necesita codificar, encriptar o autorizar, lo implementa ella misma (por ejemplo, el cifrado TLS que usa HTTPS). Las capas inferiores se ven en [[05 - Capas de transporte, red, enlace y física|capas de transporte, red, enlace y física]], y cómo se van agregando los *headers* en [[06 - Proceso de encapsulamiento y flujo de datos en la red|encapsulamiento]].

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre un servicio y un protocolo?
> El servicio es lo que una capa ofrece a la capa de arriba (sus primitivas). El protocolo son las reglas con que esa capa se comunica con la capa equivalente del otro extremo. Se puede cambiar el protocolo sin cambiar el servicio.

> [!question]- ¿Por qué OSI es un modelo de referencia y TCP/IP un stack de protocolos?
> OSI define qué responsabilidad tiene cada capa, sin especificar protocolos ni implementaciones. TCP/IP es una implementación concreta, con protocolos reales (IP, TCP, UDP, HTTP…).

> [!question]- ¿Qué pasa con las capas de presentación y sesión en TCP/IP?
> No existen como capas separadas: si una aplicación necesita codificar, encriptar o manejar sesiones y autenticación, lo hace dentro de la capa de aplicación.

> [!question]- Nombra las 5 capas de TCP/IP y un protocolo de cada una.
> Aplicación (HTTP), transporte (TCP), red (IP), enlace (Ethernet) y física (el medio: cobre, fibra o radio).
