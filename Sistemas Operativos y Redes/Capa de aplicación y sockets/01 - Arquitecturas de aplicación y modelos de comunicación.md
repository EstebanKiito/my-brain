---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - capa-de-aplicacion
  - cliente-servidor
  - p2p
prerrequisitos:
  - "[[Fundamentos de redes y modelos en capas/_Índice|Fundamentos de redes y modelos en capas]]"
---

# Arquitecturas de aplicación y modelos de comunicación

La capa de aplicación es la capa superior de los modelos [[Fundamentos de redes y modelos en capas/04 - Modelos de capas: modelo de referencia OSI frente al stack TCP-IP|OSI y TCP/IP]]. Se implementa exclusivamente en los sistemas finales (hosts emisores y receptores) y define los protocolos mediante los cuales los procesos intercambian mensajes a través de la red sin intermediación de los enrutadores en la lógica de aplicación.

---

## Modelos y arquitecturas (mis apuntes)

### CLASE 3
14/10/24

Resumen clase pasada:
- S.Aplicacion → Comunicacion de procesos
4. Transporte → Transporte de msj de origen a destino
- Red → Routing
2. Enlace → Transporte entre dispositivos y acceso al medio
- Fisico → Transporte de bits por medio misico

MODELOS TCP/IP:
Cuando comunico los procesos, no me refiero a que hayan cables directo entre ellos
En el mensaje envio info adicionl (headers) → Como interpretar el mensaje
Ej: En el header de un http digo estoy intentando hacer un post, un get , un delete , etc…

CAPA APLICACION
Capa únicamente implementada en los EMISORES Y RECPETORES de Mensajes

PROTOCOLOS
DNS: domain name system
HTTP: hypertext transfer protocol
FTP: File transfer protocol
SSH: secure shell
etc…

Pregunta Prueba: estoy enviando un archivo html, a que capa pertenece ese archivo de protocolo → CAPA DE APLICACION
Si me piden especificamente cierta accion que esta ejec un proceso → CAPA APLICACION

Hay protocolos que se construyen sobre ciuertas arquitecturas
Protocolos:

TIPOS ARQUITECTURA
Cliente/Servidor → ej: HTTP esta construido aqui, FTP, IMAP, etc…
P2P → ej: BitTorrent

La arquitectura cliente/servidor → El servicio es proveido por un solo computador → FORMA CENTRALIZADA , si se cae el servidor se cae todo el servicio, a diferencia de p2p
Generalmente no se hostea en solo una maquina, probablemente se usen muchos mas
(que pasa si se muere un pc, moriria toda la applicacion → Mejor distribuir)

P2P: Ninguno va a tener una jerarquia sobre el otro
Los Dispositivos van a estar conectados entre si
Esto puede traer problemas de seguridad
Mi mensaje va con mi direccion IP → Esto es peligroso, en la RED pueden tener tu ip
- Es mas dificil que se caiga! → Hay que bajar todos los servicios para botarla
Es ICP Friendly → Por ej: Cuando contratamos servicio internet (nos dice velocidad de bajada)
La velocidad de subida generalmente es mas lenta que la bajada
- En una p2p, por ejemplo torrent, hay mas velocidad de bajada que de subida, de cierta manera podria aprovecharme de la velocidad de subida de varios dispositvos en la red.
Sin embargo, otros usuarios pueden fekear ip, y hacerse pasar por computador, haciendo cosas malas

RESUMEN GRAFICO

![Arquitectura cliente servidor y modelos de comunicación de aplicaciones](adjuntos/Arquitectura%20cliente%20servidor%20y%20modelos%20de%20comunicación%20de%20aplicaciones.png)

> [!example]- Transcripción de la imagen
> Comparación entre arquitecturas de red:
> 1. **Cliente/Servidor**: Servidor siempre activo con dirección IP fija y conocida. Clientes se comunican intermitentemente con el servidor pero no directamente entre sí. Se suele escalar mediante centros de datos / granjas de servidores.
> 2. **Peer-to-Peer (P2P)**: Los pares se comunican directamente sin servidor central siempre encendido. Los pares son clientes y servidores al mismo tiempo (servents), lo que provee auto-escalabilidad (nuevos pares aportan capacidad de subida).

> [!warning] Posible error en apuntes: "Es ICP Friendly"
> En los apuntes se menciona "ICP Friendly"; el término técnico es **ISP-friendly** (amigable con el proveedor de servicios de internet). Debido al tráfico asimétrico de subida/bajada residencial, las redes P2P no optimizadas pueden saturar los enlaces de tránsito de los ISPs.

> [!tip] Complemento de clase: Auto-escalabilidad en P2P
> En un servidor cliente/servidor con capacidad de subida $U_s$, el tiempo mínimo para distribuir un archivo de tamaño $F$ a $N$ clientes es $\max(F/u_s, N \cdot F / u_s)$, creciendo linealmente con $N$. En P2P, cada par $i$ aporta su propia tasa de subida $u_i$, por lo que la capacidad total agregada crece con el número de pares: $T_{P2P} \ge \max(F/u_s, F/d_{min}, N \cdot F / (u_s + \sum u_i))$, otorgando escalabilidad natural.

---

## Preguntas de repaso

> [!question]- ¿Por qué la capa de aplicación reside únicamente en los sistemas finales (hosts)?
> Porque los dispositivos intermedios de la red (routers y conmutadores) solo operan en las capas inferiores (enlace y red) para encaminar paquetes; no ejecutan aplicaciones de usuario ni procesan el contenido de los mensajes de aplicación.

> [!question]- ¿Qué ventaja principal ofrece la arquitectura P2P frente a cliente/servidor en distribución masiva?
> La auto-escalabilidad: cada cliente que descarga un archivo también actúa como servidor subiendo fragmentos a otros pares, aumentando el ancho de banda total del sistema a medida que crece la demanda.

> [!question]- ¿Por qué una solicitud HTML pertenece a la capa de aplicación si se transmite por la red física?
> Porque el formato HTML, la semántica de la petición (`GET`) y la interpretación del documento son definidas y procesadas por los procesos de aplicación (navegador web y servidor web), utilizando a las capas inferiores solo como servicio de transporte.

