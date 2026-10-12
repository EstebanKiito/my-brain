---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de red y direccionamiento"
tags:
  - sistemas-operativos
  - redes
  - ipv4
  - datagrama
  - mtu
  - fragmentacion
prerrequisitos:
  - "[[Capa de red y direccionamiento/01 - Servicios de la capa de red: enrutamiento y reenvío|01 - Servicios de la capa de red: enrutamiento y reenvío]]"
---

# Datagrama IPv4: estructura y fragmentación por MTU

Internet opera como una red de datagramas sin conexión (*connectionless*), a diferencia de las redes de circuitos virtuales (como las redes telefónicas tradicionales). La PDU fundamental es el datagrama IPv4 (RFC 791). Dado que cada enlace físico de red impone una Unidad Máxima de Transferencia (MTU), los datagramas que superan la capacidad del enlace deben fragmentarse utilizando los campos de identificación, flags y desplazamiento de fragmento (*fragment offset*).

---

## Formato del paquete y fragmentación (mis apuntes)

MODOS DE CONEXION
Es un modo, que usa la via telefonica por ejemplo, establece un circuito
Antes de establecer una conexion, va construyendo una ruta de a poco el circuito
En construye primero la autopista entre yo y el destino

VIRTUAL NETWORK: ESQUEMA RED TELEFONICA
- Router mantiene estado de la conexión: Connection-oriented
- Garantiza ancho de banda durante la conexión
Provoca que si un router esta saturado → No va a poder tener mas conexiones
Por ejemplo → Terremoto, la linea telefonica tiene ancho de banda limite → Satura y la llamada no se establece
- Sin embargo: Poco flexible a CONGESTIONES

DATAGRAM NETWORK: ESQUEMA DE INTERNET
- Asi funciona la internet, mediante segmentos tcp, se encapsulan paquetes, con sus headers, y se envian, y los routers van ruteando ellos, podrian tener distintos caminos
- Los Routers reenvian de acuerdo a forwarding Table
- Routers no saben de caminos: Connectionless
- NO GARANTIZA ANCHO DE BANDA!! → El otro si
- Es Flexible ante CONGESTION!!
- Permite ocupar de mejor manera ancho de banda
- Sin embargo:

FORWARDING TABLES
Router debe tener respuesta para cada direccion posible → Usualmente contiene prefijos!
Ejemplos con 32 bits:

![Estructura y campos de la cabecera del datagrama IPv4](adjuntos/Estructura%20y%20campos%20de%20la%20cabecera%20del%20datagrama%20IPv4.png)

> [!example]- Transcripción de la imagen
> Encabezado IPv4 (20 bytes fijos):
> - Versión (4 bits, ej. 4).
> - Longitud de cabecera (*IHL*, 4 bits, en múltiplos de 32 bits).
> - Tipo de servicio (*TOS*, 8 bits).
> - Longitud total del datagrama (16 bits, hasta 65.535 bytes).
> - Identificador (16 bits), Flags (3 bits: Reservado, DF - Don't Fragment, MF - More Fragments) y Offset de fragmento (13 bits).
> - Tiempo de vida (*TTL*, 8 bits): Decrementado en 1 por cada router para evitar bucles infinitos.
> - Protocolo de capa superior (8 bits, ej. 6 para TCP, 17 para UDP, 1 para ICMP).
> - Checksum de cabecera (16 bits).
> - Dirección IP de origen (32 bits) y Dirección IP de destino (32 bits).

¿Como un mensaje encuentra su destinatario?
Gracias al DATAGRAMA (PAQUETE) IP
Longitud tipica < 1500 bytes
Parametro: MTU : Maximum Transfer Unit

![Fragmentación de datagramas IP por MTU en enlaces de red](adjuntos/Fragmentación%20de%20datagramas%20IP%20por%20MTU%20en%20enlaces%20de%20red.png)

> [!example]- Transcripción de la imagen
> Fragmentación IP: Un datagrama grande (ej. 4000 bytes) proveniente de un enlace con MTU grande debe atravesar un enlace intermedio con MTU menor (ej. 1500 bytes). El router divide el datagrama en múltiples fragmentos más pequeños, cada uno con su propia cabecera IP de 20 bytes.

- Paso 1: Fragmentar Datagrama
- Enviar fragmentos con mismo ID
- Router del otro extremos lo reensambla

![Ejemplo de campos de fragmentación: identificación, flags y offset de fragmento](adjuntos/Ejemplo%20de%20campos%20de%20fragmentación:%20identificación,%20flags%20y%20offset%20de%20fragmento.png)

> [!example]- Transcripción de la imagen
> Cálculo de fragmentación para un paquete de 4000 bytes (20 cabecera + 3980 datos) con MTU = 1500 bytes:
> - Fragmento 1: 1500 bytes (20 cabecera + 1480 datos), `ID=x`, `Offset=0`, `MF=1`.
> - Fragmento 2: 1500 bytes (20 cabecera + 1480 datos), `ID=x`, `Offset=185` ($1480 / 8$), `MF=1`.
> - Fragmento 3: 1040 bytes (20 cabecera + 1020 datos), `ID=x`, `Offset=370` ($2960 / 8$), `MF=0`.

El tamaño va a estar determinado por los ENLACES INTERMEDIO
→ Problemas de la capa de ENLACE
Enlace con MENOR MTU:

> [!warning] Posible error en apuntes: ¿Quién reensambla los fragmentos IP?
> En los apuntes se menciona "Router del otro extremos lo reensambla". En la arquitectura de Internet, los routers intermedios **nunca reensamblan fragmentos**, ya que los fragmentos pueden viajar por rutas distintas y el reensamblado consumiría memoria crítica en los routers. El reensamblado lo realiza exclusivamente el **host receptor final**.

---

## Preguntas de repaso

> [!question]- ¿Por qué el campo *Fragment Offset* se expresa en múltiplos de 8 bytes?
> Porque el campo de desplazamiento tiene solo 13 bits para representar posiciones de hasta 65.535 bytes; al escalarlo por $2^3 = 8$, los 13 bits pueden abarcar hasta $8191 \times 8 = 65.528$ bytes.

> [!question]- ¿Qué ocurre si un único fragmento de un datagrama IP se pierde en la red?
> Todo el datagrama original es descartado por el host receptor una vez que expira su temporizador de reensamblado; la capa de transporte (TCP) tendrá que retransmitir el segmento completo.

> [!question]- ¿Qué función cumple el campo TTL (*Time-To-Live*) en la cabecera IPv4?
> Evita que datagramas atrapados en bucles de enrutamiento circulen indefinidamente por la red; cada router decrementa el TTL en 1 y, si llega a 0, descarta el datagrama y envía un mensaje ICMP *Time Exceeded* al emisor.

