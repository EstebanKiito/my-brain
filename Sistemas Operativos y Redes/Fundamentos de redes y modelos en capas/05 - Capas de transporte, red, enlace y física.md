---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/transporte
  - redes/red
  - redes/enlace
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Fundamentos de redes y modelos en capas/04 - Modelos de capas: modelo de referencia OSI frente al stack TCP-IP\|04 - Modelos de capas: modelo de referencia OSI frente al stack TCP-IP]]"
---

# Capas de transporte, red, enlace y física

Las cuatro capas inferiores del modelo TCP/IP implementan la entrega de mensajes de extremo a extremo entre procesos, el enrutamiento a través de la malla global de hosts y la transmisión física de tramas y bits sobre el medio de enlace.

## Capas inferiores de la pila de protocolos (mis apuntes)

- CAPA TRANSPORTE
- Transporta mensajes entre ORGIN Y DESTINY
- Sevicion connection-oriented
- Garantias de entrega
- Control de flujo
- TCP: + seguro
- Servicion connection-less
- no gratiza entrega
- UDP: + rapido
- CAPA RED
- Se ocupa de transmitir SEGMENTOS DE MENSAJES entre un par de HOSTS
- Se preocupa de la RUTA de donde se envia el mensaje → (Routing del segmento)
- Intermediarios: ROUTERS
- Hardware routers
- ipv4, ipv6
- IP (internet protocol)
- ICMP: mensajes de control (ping, echo, trace)
- IGMP, OSPF: Protocolos entre routers
- CAPA ENLACE
- Capa se preocupa del salto entre un dispositivo a otro
- Se transmiten en cada par de hosts, de acuerdo a las Caracteristicas del enlace
- PAQUETES de capa de enlace se conocen como FRAMES
- Transmision confiable
- Proveen Control Errores
- Control de acceso al medio (MAC)
- Ethernet, IEEE 802.3 → Medio cableado
- Wi-Fi → Medio Inalambrico
- Hardware: SWITCHS y hub’s
- Frames: Unidades de bytes, se envian atraves de un enlace en especifico de un dispositivo a otro dispositivo
- CAPA FISICA
- Capa mas inferior de todas
- Se encarga de transmitir bits
- A traves de cables, fibras, inalambrico
- Como se traslada, como se transmite una señal inalambrica a traves de una antena, etc

> [!warning] Posible error
> En los apuntes aparecen erratas en `ORGIN Y DESTINY` (*origin and destination*), `Sevicion` (servicio), `gratiza` (garantiza), `SWITCHS` (*switches*) y `atraves` (a través).

> [!tip] Complemento: Unidades de datos (PDU) y responsabilidades por capa
> 1. **Capa de Transporte (PDU: Segmento):**
>    - Provee canal lógico proceso a proceso mediante puertos (0 a 65535).
>    - **TCP:** orientado a conexión, entrega en orden, retransmisiones (ARQ), control de flujo (ventana deslizante) y control de congestión.
>    - **UDP:** no orientado a conexión, sin control de flujo ni garantías de entrega; mínima sobrecarga de cabecera ($8\text{ bytes}$ frente a los $20\text{ bytes}$ mínimos de TCP).
> 2. **Capa de Red (PDU: Datagrama o Paquete):**
>    - Provee comunicación lógica de host a host a través de múltiples saltos de red.
>    - **Funciones:** enrutamiento (*routing*, plano de control que calcula rutas) y reenvío (*forwarding*, plano de datos que mueve paquetes de entrada a salida en el router).
>    - **Protocolos:** IPv4, IPv6, ICMP (*Internet Control Message Protocol*), OSPF, BGP.
> 3. **Capa de Enlace (PDU: Trama / *Frame*):**
>    - Mueve tramas entre dos nodos directamente adyacentes conectados por un enlace físico.
>    - **Direccionamiento:** direcciones físicas MAC de 48 bits (`XX:XX:XX:XX:XX:XX`).
>    - **Protocolos:** Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11). Dispositivos: switches (Capa 2).
> 4. **Capa Física (PDU: Bits):**
>    - Modula y transmite bits individuales como señales físicas (voltajes, pulsos de luz o radiofrecuencia).

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia de alcance entre la capa de red y la capa de transporte?
> La capa de red provee comunicación lógica entre **hosts** físicos (identificados por direcciones IP). La capa de transporte extiende esa comunicación para entregar datos entre **procesos específicos** que se ejecutan dentro de esos hosts (identificados mediante números de puerto).

> [!question]- ¿Cómo se denomina formalmente la unidad de datos de protocolo (PDU) en cada una de las capas de transporte, red y enlace?
> En la capa de transporte se denomina **segmento** (*segment*), en la capa de red se denomina **datagrama** o **paquete** (*datagram / packet*), y en la capa de enlace se denomina **trama** (*frame*).

> [!question]- ¿Por qué un switch opera en la capa de enlace (Capa 2) mientras que un router opera en la capa de red (Capa 3)?
> Un switch toma decisiones de reenvío basándose únicamente en las direcciones MAC contenidas en la cabecera de la trama de enlace. Un router debe examinar la dirección IP contenida en la cabecera del datagrama de red para determinar el siguiente salto en la topología global.

