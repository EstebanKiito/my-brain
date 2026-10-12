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
  - origen/complemento
prerrequisitos:
  - "[[17-Capa de enlace y seguridad/01 - Servicios de capa de enlace y control de acceso al medio (MAC)|01 - Servicios de capa de enlace y control de acceso al medio (MAC)]]"
---

# Direcciones MAC, protocolo ARP y trama Ethernet

La IP dice **a qué host** debe llegar un paquete al final del camino, pero en cada tramo el frame va de una tarjeta de red a otra. Para eso la capa de enlace usa otra dirección, la **MAC**, y un protocolo, **ARP**, que traduce de una a otra.

## Direcciones MAC

La **dirección MAC** (también dirección física o de hardware) está en la **tarjeta de red** (NIC). Sirve para que el **switch nos identifique** y sepa por qué camino nos llega la información.

- Es un identificador único de **48 bits (6 bytes)**, escrito en hexadecimal: `1A-2F-BB-76-09-AD`. Aunque viene de fábrica, es **modificable por software**.
- **24 bits** identifican al **fabricante** (el OUI, *Organizationally Unique Identifier*, que asigna la IEEE) y **24 bits** a la NIC.
- La estructura de direccionamiento es **plana**: a diferencia de la IP, no dice nada de dónde está el equipo, así que no sirve para rutear entre redes.
- `FF-FF-FF-FF-FF-FF` es la dirección de **broadcast**.

| | Dirección IP | Dirección MAC |
|---|---|---|
| Capa | Red | Enlace |
| Tamaño | 32 bits (IPv4) | 48 bits |
| Estructura | Jerárquica (subred + host) | Plana (fabricante + NIC) |
| Alcance | Todo el camino, de extremo a extremo | Un solo enlace |

## ARP: de IP a MAC

**ARP** (*Address Resolution Protocol*, RFC 826) encuentra la MAC que corresponde a una IP de la misma subred. Cada nodo (host, router y algunos switches) mantiene una **tabla ARP** con asociaciones $\langle \text{IP}, \text{MAC}, \text{TTL} \rangle$, donde el TTL indica cuánto tiempo se recordará la entrada. En un computador se puede ver con el comando `arp`.

¿Cómo se encuentra una MAC? Si C quiere comunicarse con A, pero A no está en su tabla:

1. C envía un **ARP query** (o *ARP request*) con la IP de A, a la MAC `FF-FF-FF-FF-FF-FF`.
2. **Todos** lo reciben (es broadcast).
3. **Solo A** responde con un **ARP response** (o *reply*), que lleva su MAC. Se envía solo a C, porque el query ya traía la MAC de C.
4. C guarda en su tabla la asociación ⟨IP(A), MAC(A)⟩.

## Atravesando subredes

¿Y si el mensaje va a otra subred? Supongamos que `111.111.111.111` quiere enviar un frame a `222.222.222.222`, que no está en su tabla ARP (ni puede descubrirla por broadcast, que no sale de la subred). El paquete lleva ⟨IP = 222.222.222.222, MAC = ?⟩:

- si pusiera la MAC del destino, `49-BD-D2-C7-56-2A`, el frame **no saldría de la subred**;
- debe poner la MAC del **router**, `E6-E9-00-17-BB-4B`. El router recibe el frame, lo pasa a su capa de red y decide el siguiente salto;
- ya en la subred del destino, el router envía el frame con ⟨IP = 222.222.222.222, MAC = 49-BD-D2-C7-56-2A⟩.

La **IP de destino no cambia** en todo el camino; la **MAC de destino cambia en cada salto**.

```python
from ipaddress import ip_address, ip_network

MI_RED = ip_network("111.111.111.0/24")
GATEWAY = "111.111.111.110"
tabla_arp = {"111.111.111.110": "E6-E9-00-17-BB-4B"}    # <IP, MAC> (sin TTL)

def mac_destino(ip_dst):
    """La IP de destino no cambia; la MAC es la del siguiente salto en la subred."""
    salto = ip_dst if ip_address(ip_dst) in MI_RED else GATEWAY
    if salto not in tabla_arp:
        return f"ARP query a FF-FF-FF-FF-FF-FF: ¿quién tiene {salto}?"
    return tabla_arp[salto]

print(mac_destino("222.222.222.222"))   # E6-E9-00-17-BB-4B: la del router
print(mac_destino("111.111.111.112"))   # ARP query: está en mi subred y no la conozco
```

## Ethernet

Ethernet (IEEE 802.3) es el estándar más usado en las LAN. Nació en los años 70 y es conmutado (*switched*) desde los 90:

- **basado en coaxial**: LAN de broadcast, topología de **bus**;
- **basado en hub**: LAN de broadcast, topología de **estrella**;
- **basado en switch**: evita las colisiones; el switch es un dispositivo de capa 2 (ver [[03 - Conmutación en redes locales (Switches L2, STP) y VLANs|switches]]).

El frame Ethernet tiene estos campos:

| Campo | Contenido |
|---|---|
| **Preamble** | 7 bytes `10101010` y 1 byte `10101011` (el SFD, *Start Frame Delimiter*), para sincronizarse |
| **Destination MAC** | El destinatario procesa el frame solo si es su propia MAC o `FF-FF-FF-FF-FF-FF` |
| **Source MAC** | MAC de quien envía |
| **Type** | Protocolo de arriba: IP, Novell IPX, AppleTalk, ARP (por ejemplo `0x0800` IPv4, `0x86DD` IPv6, `0x0806` ARP) |
| **Data** | De 46 a 1500 bytes: la MTU de Ethernet es 1500 (los *jumbo frames* llegan a ~9000) |
| **CRC** (o FCS, 4 bytes) | Si detecta un error, Ethernet **descarta** el frame y **no avisa**: no es confiable |

Que Ethernet no sea confiable no es un problema: si hace falta, la confiabilidad la pone [[14-Capa de transporte/06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa|TCP]] en los extremos.

## Preguntas de repaso

> [!question]- ¿Por qué un host necesita una dirección IP y una MAC?
> La IP es jerárquica y sirve para llegar al destino final a través de muchas redes. La MAC es plana y sirve para entregar el frame dentro de un enlace, de una tarjeta de red a otra.

> [!question]- ¿Cómo descubre C la MAC de A si no está en su tabla ARP?
> Envía un ARP query con la IP de A a `FF-FF-FF-FF-FF-FF`. Todos lo reciben, pero solo A responde con su MAC, y C guarda el par en su tabla.

> [!question]- Si `111.111.111.111` envía a `222.222.222.222`, ¿qué MAC de destino lleva el primer frame?
> La del router (`E6-E9-00-17-BB-4B`). Con la MAC del destino, el frame no saldría de la subred.

> [!question]- ¿Qué hace Ethernet con un frame que llega con error?
> Lo descarta sin avisar: Ethernet no es confiable, y la retransmisión queda a cargo de capas superiores como TCP.
