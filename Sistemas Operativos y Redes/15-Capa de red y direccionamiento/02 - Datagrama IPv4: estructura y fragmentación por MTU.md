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
  - origen/complemento
prerrequisitos:
  - "[[15-Capa de red y direccionamiento/01 - Servicios de la capa de red: enrutamiento y reenvío|01 - Servicios de la capa de red: enrutamiento y reenvío]]"
---

# Datagrama IPv4: estructura y fragmentación por MTU

Internet funciona como una **red de datagramas**: cada paquete viaja por su cuenta con la dirección de destino escrita en su header. Esta nota explica por qué se eligió ese modo, qué lleva el datagrama IP y qué pasa cuando un datagrama es más grande de lo que un enlace puede transportar.

## Por qué Internet usa datagramas

Los dos [[01 - Servicios de la capa de red: enrutamiento y reenvío#Modos de conexión|modos de conexión]] se entienden mejor con ejemplos:

- **Circuito virtual (esquema de red telefónica).** Antes de enviar nada, se construye la ruta de a poco: primero se arma "la autopista" entre el emisor y el destino, y cada router guarda el estado de la conexión. A cambio, el ancho de banda queda **garantizado** durante la conexión. El costo es que es **poco flexible ante la congestión**: si un router está saturado, no acepta más conexiones. Por ejemplo, tras un terremoto todos llaman a la vez, la línea telefónica llega a su límite de ancho de banda y las llamadas no se establecen.
- **Datagramas (esquema de Internet).** Los segmentos TCP se encapsulan en paquetes con sus headers y se envían; cada router los reenvía según su **tabla de reenvío**, sin saber nada del camino completo (*connectionless*), así que dos paquetes pueden tomar caminos distintos. **No garantiza ancho de banda**, pero es **flexible ante la congestión** y aprovecha mejor el ancho de banda.

## Tablas de reenvío con prefijos

Un router debe tener respuesta para **cada dirección posible**, así que la tabla guarda **prefijos** de las direcciones de 32 bits y no direcciones completas:

![Estructura y campos de la cabecera del datagrama IPv4](adjuntos/Estructura%20y%20campos%20de%20la%20cabecera%20del%20datagrama%20IPv4.png)

> [!example]- Transcripción de la imagen
> Tabla *Prefix Match* → *Link Interface*: `11001000 00010111 00010` → 0; `11001000 00010111 00011000` → 1; `11001000 00010111 00011` → 2; *otherwise* → 3.

En decimal, `11001000 00010111` es `200.23`, así que las filas corresponden a `200.23.16.0/21`, `200.23.24.0/24` y `200.23.24.0/21`. Una dirección como `200.23.24.170` calza con las filas 1 y 2: se elige la de **prefijo más largo** (la 1). La [[01 - Servicios de la capa de red: enrutamiento y reenvío|nota anterior]] implementa justo esta tabla en Python.

## El datagrama IP

¿Cómo encuentra un mensaje a su destinatario? Gracias al **datagrama (paquete) IP**, que lleva en su header todo lo que los routers necesitan.

![Ejemplo de campos de fragmentación: identificación, flags y offset de fragmento](adjuntos/Ejemplo%20de%20campos%20de%20fragmentaci%C3%B3n:%20identificaci%C3%B3n,%20flags%20y%20offset%20de%20fragmento.png)

> [!example]- Transcripción de la imagen
> Formato del datagrama IPv4 en filas de **32 bits**: *Version*, *Header length*, *Type of service* y *Datagram length (bytes)*; *16-bit Identifier*, *Flags* y *13-bit Fragmentation offset*; *Time-to-live*, *Upper-layer protocol* y *Header checksum*; *32-bit Source IP address*; *32-bit Destination IP address*; *Options (if any)*; *Data*.

| Campo | Para qué sirve |
|---|---|
| Versión y largo del header | Distinguir IPv4 de IPv6 y saber dónde empiezan los datos |
| Largo del datagrama | Tamaño total (16 bits: hasta 65 535 bytes); típicamente **menos de 1500 bytes** |
| Identificador, flags y offset | Reconstruir un datagrama fragmentado; el flag DF (*don't fragment*) prohíbe fragmentarlo |
| **TTL** (*time-to-live*) | Cantidad máxima de saltos (*hops*); cada router lo resta y el paquete se descarta al llegar a 0 |
| Protocolo de capa superior | A quién entregar los datos (6 = TCP, 17 = UDP, 1 = ICMP) |
| Checksum del header | Detectar errores en el header |
| IP de origen y de destino | 32 bits cada una |

Sin *options*, el header mide **20 bytes**.

## Fragmentación por MTU

Cada enlace tiene su **MTU** (*Maximum Transfer Unit*), el tamaño máximo de paquete que puede transportar, y no todos los enlaces tienen la misma. El tamaño que puede tener un datagrama queda determinado por los **enlaces intermedios**, que son un problema de la [[17-Capa de enlace y seguridad/01 - Servicios de capa de enlace y control de acceso al medio (MAC)|capa de enlace]]. Al encontrar un enlace con **menor MTU**:

1. el router **fragmenta** el datagrama;
2. envía los fragmentos con el **mismo identificador**;
3. según el material, el router en el otro extremo del enlace lo **reensambla**.

![Fragmentación de datagramas IP por MTU en enlaces de red](adjuntos/Fragmentaci%C3%B3n%20de%20datagramas%20IP%20por%20MTU%20en%20enlaces%20de%20red.png)

> [!example]- Transcripción de la imagen
> *Fragmentation*: *In: one large datagram (4,000 bytes)*, *Out: 3 smaller datagrams*, en un router frente a un enlace con *Link MTU: 1,500 bytes*. *Reassembly*: *In: 3 smaller datagrams*, *Out: one large datagram (4,000 bytes)*; en la figura, los tres fragmentos se reúnen en el host de destino.

Con los números de la figura: un datagrama de 4000 bytes tiene 20 de header y 3980 de datos. Con MTU de 1500, cada fragmento lleva a lo más 1480 bytes de datos. El **offset** se mide en unidades de 8 bytes, y el flag **MF** (*more fragments*) vale 1 en todos menos el último. Los offsets quedan en $1480/8 = 185$ y $2960/8 = 370$, y el último fragmento lleva los 1020 bytes de datos que sobran. Se usan unidades de 8 bytes porque el campo tiene 13 bits: $2^{13} \cdot 8 = 65\,536$ alcanza para cualquier posición dentro de un datagrama de hasta 65 535 bytes.

```python
def fragmentar(total, mtu, header=20):
    """Divide un datagrama de 'total' bytes (header incluido) para un enlace con esa MTU."""
    datos = total - header
    por_frag = (mtu - header) // 8 * 8          # datos por fragmento: múltiplo de 8
    frags, offset = [], 0
    while datos > 0:
        n = min(por_frag, datos)
        datos -= n
        frags.append({"largo": n + header, "offset": offset // 8, "MF": int(datos > 0)})
        offset += n
    return frags

for f in fragmentar(4000, 1500):
    print(f)   # largos 1500, 1500, 1040; offsets 0, 185, 370; MF 1, 1, 0
```

## Preguntas de repaso

> [!question]- ¿Por qué Internet usa una red de datagramas y no circuitos virtuales?
> Porque es flexible ante la congestión y aprovecha mejor el ancho de banda: los routers no guardan estado ni reservan recursos. A cambio, no garantiza ancho de banda.

> [!question]- ¿Qué indica el TTL y qué pasa cuando llega a 0?
> La cantidad máxima de saltos que le quedan al paquete. Cada router lo disminuye, y al llegar a 0 el paquete se descarta; así no circula para siempre en un ciclo.

> [!question]- ¿Cuándo se fragmenta un datagrama y cómo se sabe qué fragmentos van juntos?
> Cuando debe atravesar un enlace con una MTU menor que su tamaño. Todos los fragmentos llevan el mismo identificador, y el offset indica la posición de cada uno.

> [!question]- Un datagrama de 4000 bytes cruza un enlace de MTU 1500. ¿Cuántos fragmentos salen y con qué offsets?
> Tres: de 1500, 1500 y 1040 bytes, con offsets 0, 185 y 370 (en unidades de 8 bytes).
