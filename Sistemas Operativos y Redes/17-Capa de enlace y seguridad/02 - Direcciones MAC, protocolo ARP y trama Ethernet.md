---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de enlace y seguridad"
tags:
  - sistemas-operativos
  - redes
  - mac
  - arp
  - ethernet
  - tramas
prerrequisitos:
  - "[[17-Capa de enlace y seguridad/01 - Servicios de capa de enlace y control de acceso al medio (MAC)|01 - Servicios de capa de enlace y control de acceso al medio (MAC)]]"
---

# Direcciones MAC, protocolo ARP y trama Ethernet

Mientras que las direcciones IP son lógicas y jerárquicas (dependientes de la subred a la que está conectado el host), las direcciones de capa de enlace (**direcciones MAC** o de hardware) son identificadores planos grabados de forma permanente en la memoria ROM o flash de la tarjeta de red (*Network Interface Card*, NIC). Para traducir direcciones lógicas IP en direcciones físicas MAC dentro de una misma subred local, la arquitectura de Internet emplea el protocolo **ARP** (*Address Resolution Protocol*).

---

## Direcciones físicas e identificación de interfaz (mis apuntes)

Direcciones MAC
Direcciones fisicas que se encuentran dentro de la Tarjeta de Red, Nos sirven para que EL SWITCH NOS IDENTIFIQUE, y el camino por donde nos llega la INFO

> [!tip] Complemento de clase: Estructura de las direcciones MAC y trama Ethernet (IEEE 802.3)
> - **Formato de dirección MAC**: Tiene una longitud de 48 bits (6 bytes), expresada como 12 dígitos hexadecimales separados por guiones o dos puntos (por ejemplo, `1A-2F-BB-76-09-AD`).
>   - Los primeros 24 bits (3 bytes) corresponden al **OUI** (*Organizationally Unique Identifier*), asignado por la IEEE a cada fabricante de hardware.
>   - Los últimos 24 bits identifican la interfaz específica producida por ese fabricante.
>   - La dirección de difusión (*broadcast*) en capa de enlace es `FF-FF-FF-FF-FF-FF`.
> - **Estructura del frame Ethernet**:
>   1. **Preámbulo** (8 bytes): 7 bytes `10101010` seguidos de `10101011` (SFD, *Start Frame Delimiter*) para sincronización de osciladores de reloj.
>   2. **Dirección Destino** (6 bytes): MAC del receptor o switch de siguiente salto.
>   3. **Dirección Origen** (6 bytes): MAC de la interfaz transmisora.
>   4. **Tipo** (2 bytes): Identifica el protocolo de capa superior (por ejemplo, `0x0800` para IPv4, `0x86DD` para IPv6, `0x0806` para ARP).
>   5. **Carga útil / Datos** (46 a 1500 bytes): Contiene el paquete IP. La MTU estándar de Ethernet es 1500 bytes.
>   6. **CRC / FCS** (4 bytes): Código de redundancia cíclica de 32 bits para detección de errores.

> [!tip] Complemento de clase: Protocolo de resolución de direcciones (ARP)
> El protocolo **ARP** (RFC 826) permite a un host averiguar la dirección MAC asociada a una dirección IP de destino dentro de la misma red local:
> 1. **Tabla ARP**: Cada nodo almacena una caché en memoria con pares $\langle \text{IP}, \text{MAC}, \text{TTL} \rangle$. Cada entrada expira típicamente tras 10 a 20 minutos.
> 2. **ARP Request**: Si el nodo emisor no tiene la MAC en su tabla, emite una consulta ARP encapsulada en una trama de broadcast (`FF-FF-FF-FF-FF-FF`). Todos los equipos de la LAN procesan el paquete.
> 3. **ARP Reply**: El equipo cuya IP coincide con la solicitada responde directamente al emisor mediante una trama unicast con su dirección MAC física.
> 4. **Tráfico inter-subredes**: Si el destino final se encuentra fuera de la subred local, el emisor consulta ARP por la dirección IP de su *Default Gateway* (router). El datagrama IP conserva las direcciones IP origen y destino finales, pero la trama Ethernet lleva como MAC de destino la interfaz del router local.

---

## Preguntas de repaso

> [!question]- ¿Por qué los hosts requieren tanto direcciones IP como direcciones MAC?
> Porque cumplen roles desacoplados: las direcciones IP son jerárquicas y permiten enrutar paquetes a nivel global a través de múltiples redes arbitrarias; las direcciones MAC son planas e identifican interfaces individuales para el transporte local de trama en trama dentro de un medio físico específico.

> [!question]- ¿Qué ocurre a nivel de tramas cuando un host envía un paquete a otra subred?
> El paquete IP mantiene las IPs del host emisor y receptor original. Sin embargo, el frame Ethernet de capa de enlace coloca como dirección MAC de destino la interfaz física del router local (*Default Gateway*), el cual desencapsulará la trama y la reenviará hacia el siguiente salto.

> [!question]- ¿Por qué los paquetes ARP Request se envían por broadcast mientras que los ARP Reply por unicast?
> La petición se envía por broadcast porque el emisor desconoce qué interfaz posee esa IP y qué dirección MAC tiene. La respuesta se envía por unicast porque la petición ya incluía la dirección MAC física del emisor original, por lo que el destinatario ya sabe exactamente a quién responder.
