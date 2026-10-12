---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de red y direccionamiento"
tags:
  - sistemas-operativos
  - redes
  - icmp
  - ping
  - traceroute
  - ipv6
  - dual-stack
  - tunneling
  - origen/complemento
prerrequisitos:
  - "[[15-Capa de red y direccionamiento/04 - Configuración dinámica con DHCP y traducción de direcciones NAT|04 - Configuración dinámica con DHCP y traducción de direcciones NAT]]"
---

# Protocolo ICMP y transición a IPv6: dual-stack y tunneling

Esta nota cierra la capa de red con dos temas. **ICMP** es el protocolo con que la red avisa de problemas y con el que funcionan `ping` y `traceroute`. **IPv6** es la respuesta a la escasez de direcciones IPv4, y el desafío no es tanto diseñarlo como migrar a él sin apagar Internet.

## ICMP: diagnóstico y control

**ICMP** (*Internet Control Message Protocol*, RFC 792) es un conjunto de reglas para **diagnosticar problemas de comunicación** en una red: se usa para mensajes de diagnóstico y control de la capa de red.

- Viaja como *payload* dentro de un paquete IP; el campo *upper-layer protocol* del [[02 - Datagrama IPv4: estructura y fragmentación por MTU|datagrama]] indica que lleva ICMP.
- Cada mensaje tiene dos campos: **(ICMP type, ICMP code)**.

![Formato de mensajes y tipos del protocolo de control ICMP](adjuntos/Formato%20de%20mensajes%20y%20tipos%20del%20protocolo%20de%20control%20ICMP.png)

> [!example]- Transcripción de la imagen
> "Table 1-3 ICMP Message Types", con *ICMP Type / Code / Description*: 0/0 *echo reply (to ping)*; 3/0 *destination network unreachable*; 3/1 *destination host unreachable*; 3/2 *destination protocol unreachable*; 3/7 *destination host unknown*; 8/0 *echo request*; 10/0 *router discovery*; 11/0 *TTL expired*.

Los más conocidos son **(8, 0) echo request** y **(0, 0) echo reply**: es lo que hace `ping`. El programa **traceroute** usa mensajes ICMP con **distintos TTL**: envía paquetes con TTL 1, 2, 3…; el router donde el TTL llega a 0 descarta el paquete y responde **(11, 0) TTL expired**, revelando su dirección. Así se descubre la ruta salto a salto.

```python
RUTA = ["192.168.1.1", "200.1.1.1", "200.2.2.2", "64.233.186.90"]   # 3 routers y el destino

def enviar(ttl):
    """Cada router resta 1 al TTL; si llega a 0, descarta y responde ICMP (11, 0)."""
    for ip in RUTA[:-1]:
        ttl -= 1
        if ttl == 0:
            return ip, (11, 0)           # TTL expired
    return RUTA[-1], (0, 0)              # el destino responde echo reply

ttl = 1
while True:                              # traceroute: TTL = 1, 2, 3, ...
    ip, icmp = enviar(ttl)
    print(ttl, ip, icmp)                 # tres (11, 0) y luego (0, 0) del destino
    if icmp == (0, 0):
        break
    ttl += 1
```

## IPv6

En los años 90 la IETF se dio cuenta de que IPv4 no iba a alcanzar y empezó a desarrollar IPv6; en febrero de 2011 la IANA asignó el último bloque IPv4. IPv6 usa **direcciones de 128 bits**: $2^{128} \approx 3{,}4 \cdot 10^{38}$, un número enorme. Aun así, no todo el mundo se ha cambiado.

El **header mide 40 bytes** fijos, y la prioridad del diseño es **agilizar el procesamiento** en los routers:

- **no hay fragmentación intermedia**, solo en los extremos: si un paquete no cabe, el router responde con el mensaje ICMP *Packet too big*;
- **no hay checksum del header**;
- **ICMPv6** agrega mensajes adicionales.

## ¿Cómo hacer la transición?

El problema es que un router IPv6 puede ser compatible hacia atrás con IPv4, pero un **router IPv4 no entiende IPv6**. Hay tres opciones:

1. **Un día de cambio mundial** (*flag day*): todos cambian a la vez. Ya se intentó, hace unos 25 años, en el paso de NCP a TCP, y con el tamaño actual de Internet no es viable.
2. **Routers *dual-stack*** (IPv6/IPv4): hablan ambos protocolos y traducen. El costo es que **algunos campos se pierden** en la conversión.
3. **Tunneling**: encapsular el paquete de un formato dentro de otro para que pase por un tramo especial (los tramos IPv4).

![Estructura del encabezado simplificado de 40 bytes en IPv6](adjuntos/Estructura%20del%20encabezado%20simplificado%20de%2040%20bytes%20en%20IPv6.png)

> [!example]- Transcripción de la imagen
> Seis routers en línea: A y B (IPv6), C y D (IPv4), E y F (IPv6). *A to B: IPv6*, con `Flow: X, Source: A, Dest: F` y *data*. *B to C: IPv4* y *D to E: IPv4*, con solo `Source: A, Dest: F` y *data*. *E to F: IPv6*, con `Flow: ??, Source: A, Dest: F`.

Fíjate en el campo **Flow**: al pasar por el tramo IPv4 se pierde, porque IPv4 no tiene dónde guardarlo, y al volver a IPv6 queda `Flow = ??`. Eso es lo que se pierde en la conversión *dual-stack*.

![Estrategia de transición Dual-Stack para coexistencia de IPv4 e IPv6](adjuntos/Estrategia%20de%20transici%C3%B3n%20Dual-Stack%20para%20coexistencia%20de%20IPv4%20e%20IPv6.png)

> [!example]- Transcripción de la imagen
> "IPv6 Server on Dual-Stack. IPv6 servers running on a dual stack host accept connections from IPv4 and IPv6 clients". Un *IPv6-only node* (Client, TCP/UDP, IPv6) envía *IPv6 packets*; un *IPv4-only node* (Client, TCP/UDP, IPv4, con dirección `a.b.c.d`) envía *IPv4 packets*. Ambos llegan al *Dual-stack node*: *Server (0::0, port)* sobre TCP/UDP, con pilas IPv4 e IPv6; el cliente IPv4 aparece como `::FFFF:a.b.c.d`. "Kernel: from IPv4 to IPv4-mapped IPv6 address".

Con **tunneling**, en cambio, el paquete IPv6 completo viaja como datos dentro de un paquete IPv4, y nada se pierde:

![Técnica de encapsulamiento por tunneling de paquetes IPv6 sobre redes IPv4](adjuntos/T%C3%A9cnica%20de%20encapsulamiento%20por%20tunneling%20de%20paquetes%20IPv6%20sobre%20redes%20IPv4.png)

> [!example]- Transcripción de la imagen
> **Logical view**: A y B (IPv6), un *Tunnel*, y E y F (IPv6). **Physical view**: A, B (IPv6), C, D (IPv4), E, F (IPv6). *A to B: IPv6* con `Flow: X, Source: A, Dest: F`. *B to C* y *D to E: IPv4 (encapsulating IPv6)*, con un header `Source: B, Dest: E` que envuelve el paquete IPv6 original (`Flow: X, Source: A, Dest: F`, *data*). *E to F: IPv6* con `Flow: X, Source: A, Dest: F`.

| | Dual-stack | Tunneling |
|---|---|---|
| Qué hace en el tramo IPv4 | Traduce el paquete IPv6 a IPv4 | Mete el paquete IPv6 completo dentro de uno IPv4 (de B a E) |
| Campos IPv6 como Flow | Se pierden (`Flow: ??`) | Se conservan (`Flow: X`) |

## Preguntas de repaso

> [!question]- ¿Qué mensajes ICMP usa `ping`?
> Echo request (8, 0) para preguntar y echo reply (0, 0) para responder.

> [!question]- ¿Cómo descubre `traceroute` la ruta hacia un destino?
> Envía paquetes con TTL 1, 2, 3… Cada vez, el router donde el TTL llega a 0 descarta el paquete y responde con ICMP (11, 0) *TTL expired*, revelando su dirección.

> [!question]- ¿Qué simplificaciones hace IPv6 para agilizar el procesamiento en los routers?
> Header fijo de 40 bytes, sin fragmentación intermedia (si no cabe, ICMP *Packet too big*) y sin checksum del header.

> [!question]- ¿Por qué se pierde el campo Flow con dual-stack y no con tunneling?
> Con dual-stack el paquete se convierte a IPv4, que no tiene ese campo. Con tunneling el paquete IPv6 completo viaja encapsulado dentro del IPv4 y sale intacto al otro lado del túnel.
