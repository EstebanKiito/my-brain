---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de enlace y seguridad"
tags:
  - sistemas-operativos
  - redes
  - switches
  - vlan
  - stp
  - lan
  - origen/complemento
prerrequisitos:
  - "[[17-Capa de enlace y seguridad/02 - Direcciones MAC, protocolo ARP y trama Ethernet|02 - Direcciones MAC, protocolo ARP y trama Ethernet]]"
---

# Conmutación en redes locales (Switches L2, STP) y VLANs

Una **LAN** (*Local Area Network*) parte de una interfaz de un router que se extiende a uno o más switches: son todos los dispositivos conectados a una misma **subred**. El switch es el que reparte los frames dentro de ella, usando las [[02 - Direcciones MAC, protocolo ARP y trama Ethernet|direcciones MAC]]. Esta nota explica cómo decide, cómo evita los ciclos y cómo se divide una LAN en **VLANs**.

## El switch L2

Un switch recibe un frame y lo retransmite por el enlace apropiado según la **MAC de destino**. Hace dos cosas:

- **Filtering**: decidir si hace *forward* o *drop* (descarta).
- **Forwarding**: decidir por cuál enlace retransmitir.

Si recibe por el enlace $x$ un frame con destino `DD-DD-DD-DD-DD-DD`:

| Situación en la tabla | Acción |
|---|---|
| No hay entrada para esa MAC | **Broadcast** por todos los enlaces, salvo $x$ |
| La MAC está asociada al mismo enlace $x$ | **Descarta** (*filtering*): el destino ya lo recibió por ahí |
| La MAC está asociada a otro enlace $y \neq x$ | **Reenvía** por $y$ (*forwarding*) |

## La tabla se aprende sola

La tabla parte **vacía**. Por cada frame recibido, el switch guarda la **MAC de origen**, el **enlace** por donde llegó y la **hora**: así aprende dónde está cada host sin que nadie lo configure. Después de un **aging time** borra la entrada, de modo que si un host se reemplaza o se mueve, el switch eventualmente se entera. Por eso **un switch es plug-and-play**.

```python
ENLACES = [1, 2, 3, 4]
tabla = {}                                   # MAC -> enlace (se aprende sola)

def recibir(origen, destino, x):
    """Frame que entra por el enlace x."""
    tabla[origen] = x                        # aprende: 'origen' está detrás de x
    y = tabla.get(destino)
    if y is None:
        return f"broadcast por {[e for e in ENLACES if e != x]}"
    if y == x:
        return "filtering: descartar"
    return f"forwarding por {y}"

print(recibir("AA", "DD", 1))   # DD desconocida: broadcast por [2, 3, 4]
print(recibir("DD", "AA", 3))   # AA ya aprendida: forwarding por 1
print(recibir("AA", "DD", 1))   # forwarding por 3
print(recibir("BB", "AA", 1))   # AA está en el mismo enlace: filtering
```

## Ciclos y Spanning Tree Protocol

Para tener respaldo se conectan switches con enlaces redundantes, y eso forma **ciclos**. Los ciclos son malos para el broadcast: el frame Ethernet no tiene TTL, así que un broadcast da vueltas para siempre y se multiplica (*broadcast storm*, tormenta de difusión). El **Spanning Tree Protocol (STP)** lo evita en cuatro etapas; los switches se coordinan con mensajes BPDU (*Bridge Protocol Data Units*):

1. Elegir un **root bridge**, según una prioridad más un identificador (la MAC).
2. Cada switch, salvo el root, elige su enlace en dirección al root: el **root port** (RP).
3. Cada segmento determina su **designated port**.
4. Los puertos que no se usan quedan **bloqueados** (alternativos).

La topología final se autoconfigura como un **árbol de expansión** (*spanning tree*): sin ciclos, pero con los enlaces bloqueados listos para usarse si otro falla.

## Switch frente a router

| | Switch | Router |
|---|---|---|
| Capa | L2: decide según la MAC | L3: decide según la IP |
| Tabla | Se aprende sola (MAC → enlace) | La llenan algoritmos de ruteo como OSPF o BGP |
| Configuración | Se autoconfigura | Debe configurarse |
| ARP | No lo resuelve (no conoce IP) | Sí |
| Riesgos | *Switch poisoning* y *broadcast storm* | — |

## VLANs

Los switches **no aíslan bien el tráfico**: los broadcasts (ARP, DHCP) recorren toda la LAN conmutada, y cualquiera con un *sniffer* podría verlos. Una solución sería usar varios switches, pero si un usuario cambia de grupo de trabajo habría que recablearlo al switch correcto. Los routers también lo resolverían, pero las **VLANs** (*Virtual LANs*) son más accesibles.

Una **VLAN** separa el tráfico según se quiera, sobre la **misma LAN física**: por ejemplo, una VLAN para domótica y otra para servidores. Hay varias formas de construirlas:

- **por puertos** (cada puerto del switch pertenece a una VLAN);
- **por MAC**;
- **por IP**.

Para tener VLANs **distribuidas entre varios switches** se usa **VLAN trunking**: un **trunk port** pertenece a **todas** las VLANs y reenvía entre switches. ¿Cómo sabe el otro switch a qué VLAN va cada frame? **Se modifica el frame Ethernet**: el estándar **IEEE 802.1Q** agrega un campo *Tag Control Information* (4 bytes en total) con el número de VLAN, el VLAN ID de 12 bits: hasta 4096 VLANs.

Dos hosts en VLANs distintas están en subredes distintas: para hablar entre sí necesitan pasar por un router.

## Preguntas de repaso

> [!question]- ¿Qué hace un switch con un frame cuyo destino no está en su tabla?
> Lo envía por broadcast por todos sus enlaces, salvo por el que llegó.

> [!question]- ¿Cómo aprende un switch su tabla?
> Por cada frame que recibe, anota la MAC de origen, el enlace por donde llegó y la hora. Las entradas se borran después de un aging time.

> [!question]- ¿Por qué hace falta STP y qué produce?
> Porque los enlaces redundantes forman ciclos, y un broadcast sin TTL circularía para siempre. STP elige un root bridge, root ports y designated ports, y bloquea los demás: la topología queda como un árbol sin ciclos.

> [!question]- ¿Cómo sabe un switch a qué VLAN pertenece un frame que llega por un trunk port?
> Porque IEEE 802.1Q agrega al frame Ethernet un campo con el número de VLAN.
