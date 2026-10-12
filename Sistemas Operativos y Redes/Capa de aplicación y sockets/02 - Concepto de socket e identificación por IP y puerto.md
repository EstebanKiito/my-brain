---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de aplicación y sockets"
tags:
  - sistemas-operativos
  - redes
  - sockets
  - puertos
  - direccionamiento
prerrequisitos:
  - "[[Capa de aplicación y sockets/01 - Arquitecturas de aplicación y modelos de comunicación|01 - Arquitecturas de aplicación y modelos de comunicación]]"
---

# Concepto de socket e identificación por IP y puerto

Un socket es una abstracción de software provista por el sistema operativo que actúa como interfaz y puerta de enlace entre el proceso de aplicación en espacio de usuario y los [[Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física|protocolos de transporte]] (TCP o UDP) gestionados por el kernel.

---

## Comunicación entre procesos en red (mis apuntes)

¿Como un proceso logra comunicarse en la RED?

SOCKETS
SOCKETS: Elemento de software que interactúa con la red
- Puerta de entrada/salida al sistema
- Utiliza servicios de capa Transporte: TCP o UDP
- Solo existe en hosts de origen y destino
- IDentificador conexion → IP (identificar dispositivo) y PUERTO (identidifica procesos)

Servicios
Archvios, Emails WebDocuments → Priorizan no perder data (TCP)
Streaming, telefonia, etc → Priorizan velocidad (UDP)

Puertos:
HTTP: Por default 80
SSH: Usa el puerto 22
HTTPS: 443
- Por ejemplo [https://www.google.com:443](http://www.google.com:443) → Como 443 es el puerto de https → Nos recargara la misma pagina, otro numero no sera identificado porbablemente

![Concepto de socket e identificación por dirección IP y puerto](adjuntos/Concepto%20de%20socket%20e%20identificación%20por%20dirección%20IP%20y%20puerto.png)

> [!example]- Transcripción de la imagen
> El socket como interfaz entre la capa de aplicación y la capa de transporte:
> - En el host de origen, el proceso emisor escribe datos en el socket; el sistema operativo encapsula los datos en segmentos de transporte y paquetes IP.
> - A través de la red física, los paquetes viajan hasta el host de destino.
> - En el host de destino, el kernel entrega el flujo de datos entrante al socket correspondiente identificado por el número de puerto de destino.

TCP: Protocolo de enviado lento pero seguro (por ej: Cuando estoy enviandome archivos)
UDP: Protocolo de enviado rapido pero no confiable (no asegura llegada completa) (por ej: Streaming de video)

> [!tip] Complemento de clase: Identificación de sockets (4-tupla vs 2-tupla)
> - Un socket **UDP** se identifica completamente por una 2-tupla: `(IP destino, Puerto destino)`. Cuando llega un datagrama UDP, el kernel lo enruta al socket escuchando en ese puerto local sin importar el origen.
> - Un socket **TCP** establecido se identifica por una 4-tupla: `(IP origen, Puerto origen, IP destino, Puerto destino)`. El servidor puede tener múltiples sockets conectados escuchando concurrentemente distintos clientes en el mismo puerto local (ej. 80 o 443).

> [!tip] Complemento de clase: Rangos de puertos
> Los puertos de 16 bits ($0$ a $65535$) se dividen en:
> 1. **Puertos bien conocidos (Well-known)**: $0 - 1023$ (reservados para servicios estándar y requieren privilegios de root/administrador: HTTP 80, HTTPS 443, SSH 22, DNS 53, FTP 20/21, SMTP 25).
> 2. **Puertos registrados**: $1024 - 49151$ (asignados por IANA para aplicaciones de usuario específicas).
> 3. **Puertos dinámicos/efímeros**: $49152 - 65535$ (asignados temporalmente por el kernel a clientes salientes).

---

## Preguntas de repaso

> [!question]- ¿Por qué no basta con la dirección IP para entregar un mensaje al destinatario correcto?
> La dirección IP identifica únicamente al computador o interfaz de red en la red global; como en un mismo host se ejecutan decenas de aplicaciones en red simultáneamente, se requiere el número de puerto para multiplexar y desmultiplexar los mensajes hacia el proceso o socket correspondiente.

> [!question]- ¿Qué entidad gestiona los buffers internos asociados a un socket?
> El kernel del sistema operativo; cuando una aplicación envía datos mediante `send()` o `write()`, los bytes se copian del espacio de usuario al buffer del socket en el kernel antes de ser transmitidos por la tarjeta de red.

> [!question]- ¿Por qué acceder a un puerto menor a 1024 suele requerir privilegios de superusuario en UNIX/Linux?
> Porque son puertos bien conocidos reservados para servicios esenciales del sistema (como SSH en 22 o HTTP en 80), previniendo que un proceso ordinario sin privilegios suplante un servicio oficial del servidor.

