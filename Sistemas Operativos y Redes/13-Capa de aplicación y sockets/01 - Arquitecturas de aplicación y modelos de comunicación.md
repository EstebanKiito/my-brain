---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - capa-de-aplicacion
  - cliente-servidor
  - p2p
  - origen/complemento
prerrequisitos:
  - "[[12-Fundamentos de redes y modelos en capas/_Índice|Fundamentos de redes y modelos en capas]]"
---

# Arquitecturas de aplicación y modelos de comunicación

Las aplicaciones de red (la web, el correo, DNS, WhatsApp, Torrent…) se construyen con **procesos en distintos nodos que se comunican**. La **capa de aplicación** es donde viven esos procesos y sus protocolos, en la cima de los [[12-Fundamentos de redes y modelos en capas/04 - Modelos de capas: modelo de referencia OSI frente al stack TCP-IP|modelos OSI y TCP/IP]]. Antes de ver protocolos concretos, conviene ubicar la capa y elegir una arquitectura: cliente-servidor o P2P.

## Repaso: qué hace cada capa

| Capa | Función |
|---|---|
| Aplicación | Comunicación entre procesos |
| Transporte | Transporte de mensajes de origen a destino |
| Red | Routing |
| Enlace | Transporte entre dispositivos y acceso al medio |
| Física | Transporte de bits por el medio físico |

Comunicar dos procesos no significa que haya un cable directo entre ellos: el mensaje lleva **información adicional en headers** que indica cómo interpretarlo. Por ejemplo, el header de un mensaje HTTP dice si se está haciendo un `GET`, un `POST` o un `DELETE`.

## La capa de aplicación

Se implementa **únicamente en los emisores y receptores** de mensajes, los hosts. Los routers y switches no la ejecutan: solo trabajan en las capas inferiores.

Algunos de sus protocolos son DNS (*Domain Name System*), HTTP (*HyperText Transfer Protocol*), FTP (*File Transfer Protocol*), SSH (*Secure Shell*), Telnet, SMTP, POP, IMAP, NTP, IRC y LDAP.

> [!tip] ¿A qué capa pertenece?
> Si se está enviando un archivo HTML, o si se pide una acción concreta que ejecuta un proceso, se está en la **capa de aplicación**: el formato y el significado del mensaje los definen y procesan las aplicaciones, y las demás capas solo lo transportan.

## Dos arquitecturas

![Arquitectura cliente servidor y modelos de comunicación de aplicaciones](adjuntos/Arquitectura%20cliente%20servidor%20y%20modelos%20de%20comunicaci%C3%B3n%20de%20aplicaciones.png)

> [!example]- Transcripción de la imagen
> A la izquierda, **Server-based**: seis computadores conectados solo a un servidor central (topología en estrella). A la derecha, **P2P-network**: seis computadores conectados todos con todos, sin servidor.

| | **Cliente-servidor** | **P2P** (*peer-to-peer*) |
|---|---|---|
| Quién habla con quién | Los clientes se comunican con el servidor, **no entre ellos** | Los pares se comunican **directamente**; ninguno tiene jerarquía sobre otro |
| Servidor | Tiene una **dirección fija y conocida** y recibe muchas solicitudes | Requerimientos mínimos de servidores |
| Infraestructura | Intensiva: capacidad de atención y ancho de banda, en *data centers* | Cada miembro aporta capacidad: **auto-escalabilidad** |
| Si se cae un nodo | **Centralizado**: si cae el servidor, cae el servicio (por eso se suele distribuir en muchas máquinas) | Es más difícil que caiga: habría que bajar a todos los pares |
| Ejemplos | Web (HTTP), FTP, Telnet, SSH, correo (IMAP) | BitTorrent, aceleradores de descarga, Skype, IPTV |

**Desafíos de P2P:**

- **ISP friendly**: muchas conexiones domésticas son **asimétricas**, con la subida más lenta que la bajada. P2P se apoya en la subida de muchos dispositivos, así que pone presión justo sobre la parte más débil del enlace.
- **Seguridad**: hay múltiples puntos de vulnerabilidad. Cada mensaje lleva la IP del usuario, que queda expuesta a otros pares, y un par malicioso puede hacerse pasar por otro.

> [!example]- Por qué P2P escala: un ejemplo numérico
> Distribuir un archivo de 1 GB a $N$ usuarios con un servidor de 30 Mbps de subida, usuarios que suben a 2 Mbps y bajan a 10 Mbps. En cliente-servidor, el servidor debe subir $N$ copias: el tiempo crece linealmente con $N$ (44 min para 10, 444 min para 100). En P2P, cada usuario también sube partes a otros y la capacidad total crece con $N$: unos 27 min para 10 y 58 min para 100.
>
> Las cotas usadas (Kurose), con $F$ el tamaño del archivo, $u_s$ la subida del servidor, $u_i$ la de cada par y $d_{min}$ la menor bajada:
> $$T_{cs} \ge \max\left(\frac{N F}{u_s}, \frac{F}{d_{min}}\right) \qquad T_{P2P} \ge \max\left(\frac{F}{u_s}, \frac{F}{d_{min}}, \frac{N F}{u_s + \sum u_i}\right)$$

## Preguntas de repaso

> [!question]- ¿Por qué la capa de aplicación solo existe en los hosts?
> Porque los dispositivos intermedios (routers y switches) solo trabajan en las capas inferiores para mover los paquetes; no ejecutan aplicaciones ni interpretan el contenido de los mensajes.

> [!question]- ¿Qué diferencia hay entre cliente-servidor y P2P?
> En cliente-servidor, los clientes hablan solo con un servidor de dirección fija, que concentra el servicio. En P2P, los pares hablan directamente entre ellos, sin jerarquía, y cada uno aporta capacidad.

> [!question]- ¿Qué es la auto-escalabilidad de P2P?
> Que cada nuevo miembro, además de consumir, aporta capacidad (por ejemplo, subiendo partes de un archivo a otros), así que la capacidad total crece con la cantidad de usuarios.

> [!question]- ¿Qué desafíos tiene P2P?
> No es amigable con los ISP, porque explota la subida, que suele ser la parte más lenta de las conexiones asimétricas. Y tiene problemas de seguridad: muchos puntos de vulnerabilidad, la IP de cada usuario queda expuesta y un par puede hacerse pasar por otro.
