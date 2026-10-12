---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - capa-de-transporte
  - segmentos
  - multiplexacion
  - origen/complemento
prerrequisitos:
  - "[[13-Capa de aplicación y sockets/_Índice|Capa de aplicación y sockets]]"
---

# Servicios de la capa de transporte y estructura de segmentos

La capa de red sabe llevar paquetes de un **host** a otro, pero en cada host corren muchos procesos. La **capa de transporte** completa el viaje: su objetivo es que un mensaje llegue **desde el proceso emisor hasta el proceso receptor**. Se ubica entre la capa de aplicación y la de red, y vive solo en los extremos: los routers intermedios no examinan sus headers.

![Servicios y responsabilidades de la capa de transporte en sistemas finales](adjuntos/Servicios%20y%20responsabilidades%20de%20la%20capa%20de%20transporte%20en%20sistemas%20finales.png)

> [!example]- Transcripción de la imagen
> Pila de cuatro capas: *Application Layer* (e.g. HTTP, FTP, RTP, RTSP), *Transport Layer* (e.g. UDP, TCP), *Network Layer* (e.g. IPv4, IPv6) y *Link Layer* (e.g. Ethernet/802.3, WiFi/802.11).

## Emisor y receptor

| Agente | Qué hace |
|---|---|
| **Emisor** | Recibe un mensaje de la capa de aplicación, **lo divide en segmentos** y le pide a la capa de red que **envíe** los segmentos al receptor |
| **Receptor** | Recibe los segmentos, **los ensambla** para formar el mensaje y **lo entrega** a la capa de aplicación |

El protocolo de transporte **solo lo ejecutan el origen y el destino**, nunca los intermediarios. Los segmentos viajan **dentro de paquetes IP**.

## Dos protocolos

- **TCP**: entrega **confiable y ordenada**, con **control de flujo** y **establecimiento de conexión** previo.
- **UDP**: entrega **no confiable y desordenada**, pero **más rápida**.

Sobre ellos van los mensajes de la aplicación, por ejemplo una página HTML con sus headers HTTP, que el receptor interpretará según las reglas de su protocolo.

## Puertos: a qué proceso va cada segmento

¿Cómo se distinguen los mensajes de distintos procesos que viajan entre los mismos dos hosts? Con el **puerto**:

- el puerto permite **identificar procesos** dentro del nodo emisor o del receptor;
- el puerto permite **multiplexar** mensajes: varios procesos comparten la misma conexión de red y cada segmento lleva el puerto de su proceso.

![Estructura de un segmento de transporte con datos y cabeceras](adjuntos/Estructura%20de%20un%20segmento%20de%20transporte%20con%20datos%20y%20cabeceras.png)

> [!example]- Transcripción de la imagen
> "Mensaje se divide en segmentos → Segmentos se transmiten en paquetes IP. ¿Cómo identificar mensajes a distintos procesos? **Puerto** permite identificar procesos dentro del nodo emisor o del nodo receptor. **Puerto** permite multiplexar mensajes".

Todo segmento lleva, como mínimo, el **puerto de origen** (para saber a quién responder) y el **puerto de destino** (para saber a qué socket entregarlo). Por ejemplo, el segmento UDP:

![Proceso de multiplexación y desmultiplexación de segmentos mediante puertos](adjuntos/Proceso%20de%20multiplexaci%C3%B3n%20y%20desmultiplexaci%C3%B3n%20de%20segmentos%20mediante%20puertos.png)

> [!example]- Transcripción de la imagen
> Formato del segmento UDP, en filas de **32 bits**: *Source port #* y *Dest. port #*; *Length* y *Checksum*; y luego *Application data (message)*.

El detalle de cómo se reparten los segmentos entre sockets está en [[02 - Multiplexación y desmultiplexación de puertos en UDP y TCP|multiplexación y desmultiplexación]].

> [!tip] Transporte sobre red
> La capa de red (IP) ofrece un servicio de "mejor esfuerzo": no garantiza que los paquetes lleguen ni que lleguen en orden. Sobre esa base, TCP construye un servicio confiable, y UDP ofrece uno mínimo y liviano.

## Preguntas de repaso

> [!question]- ¿Qué hacen el emisor y el receptor de la capa de transporte?
> El emisor divide el mensaje de la aplicación en segmentos y pide a la capa de red que los envíe. El receptor recibe los segmentos, los ensambla y entrega el mensaje a la aplicación.

> [!question]- ¿Por qué los routers no ejecutan la capa de transporte?
> Porque para reenviar un paquete solo necesitan la información de la capa de red (la IP de destino). El transporte es asunto de los extremos.

> [!question]- ¿Para qué sirven los puertos en la capa de transporte?
> Para identificar a qué proceso de cada host pertenece un segmento y así multiplexar los mensajes de varios procesos sobre la misma red.

> [!question]- ¿Qué diferencia hay entre TCP y UDP?
> TCP establece conexión y entrega de forma confiable y ordenada, con control de flujo. UDP no establece conexión ni garantiza la entrega ni el orden, pero es más rápido.
