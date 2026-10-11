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
prerrequisitos:
  - "[[Capa de enlace y seguridad/02 - Direcciones MAC, protocolo ARP y trama Ethernet|02 - Direcciones MAC, protocolo ARP y trama Ethernet]]"
---

# Conmutación en redes locales (Switches L2, STP) y VLANs

En las redes de área local modernas (**LAN**), los conmutadores o **switches de capa 2** (L2) son los dispositivos centrales encargados de interconectar estaciones y servidores. A diferencia de los concentradores antiguos (*hubs*), que operaban como medios compartidos en capa física retransmitiendo bits a todos los puertos, un switch aísla dominios de colisión y reenvía tramas selectivamente en base a direcciones MAC. Para segmentar el tráfico y aislar dominios de difusión sin necesidad de comprar equipamiento físico adicional, se emplean **VLANs** (*Virtual Local Area Networks*).

---

## Conmutación, LAN y VLANs (mis apuntes)

LAN : Local Area Network → A partir de un router, una interfaz que puede ser extendida a un switch, la Lan son todos aquellos dispositivos conectados a una misma SUBRED
VLAN : Lans Virtuales, para separar trafico de pquetes segun se quiera separar (ej: Domotica, servidores, etc..)

> [!tip] Complemento de clase: Operación de switches y autoaprendizaje (*self-learning*)
> Los switches son dispositivos transparentes y *plug-and-play*:
> 1. **Tabla de conmutación**: Mantiene entradas $\langle \text{Dirección MAC}, \text{Puerto/Interfaz}, \text{TTL} \rangle$.
> 2. **Autoaprendizaje**: Cuando una trama arriba al switch por el puerto $x$ con MAC de origen $S$, el switch aprende automáticamente que el host con MAC $S$ está conectado en ese puerto.
> 3. **Lógica de reenvío**:
>    - Si la MAC destino $D$ ya está en la tabla asociada al mismo puerto $x$, la trama se filtra/descarta.
>    - Si la MAC destino $D$ está asociada a otro puerto $y$, la trama se transmite exclusivamente por el puerto $y$.
>    - Si la MAC destino $D$ no existe en la tabla (o es broadcast), el switch realiza una inundación (*flooding*), replicando la trama por todos los puertos excepto por el puerto de llegada $x$.

> [!tip] Complemento de clase: Ciclos de red y Spanning Tree Protocol (STP, IEEE 802.1D)
> Cuando se instalan switches con enlaces redundantes para alta disponibilidad, se crean ciclos físicos. Dado que las tramas Ethernet carecen de un campo TTL (a diferencia de los paquetes IP), las tramas de difusión atrapadas en un ciclo generan **tormentas de difusión** (*broadcast storms*) y tablas de conmutación oscilantes, colapsando la red en milisegundos.
> El protocolo **STP** (IEEE 802.1D) evita estos bucles de forma autónoma:
> - Los switches intercambian mensajes **BPDU** (*Bridge Protocol Data Units*) para elegir un conmutador raíz (*Root Bridge*).
> - Cada switch calcula el camino de menor costo hacia la raíz y bloquea lógicamente los puertos redundantes (*blocking state*), convirtiendo la topología física mallada en un árbol de expansión acíclico. Si un enlace activo falla, el protocolo recalcula el árbol y activa los enlaces de respaldo.

> [!tip] Complemento de clase: VLANs y enlace troncal (IEEE 802.1Q)
> Las **VLANs** dividen los puertos físicos de un switch en redes locales lógicas independientes:
> - **Aislamiento de tráfico**: El tráfico de difusión (broadcast ARP, DHCP) de una VLAN nunca llega a los puertos de otra VLAN, mejorando seguridad y rendimiento.
> - **VLAN Trunking**: Para transportar el tráfico de múltiples VLANs a través de un único enlace físico entre switches, se utiliza el estándar **IEEE 802.1Q**. Este protocolo inserta una cabecera de 4 bytes en la trama Ethernet que contiene el **VLAN ID** (12 bits, permitiendo hasta 4096 VLANs).
> - **Intercomunicación entre VLANs**: Dos hosts en distintas VLANs pertenecen a subredes IP distintas; para comunicarse requieren obligatoriamente un enrutador de capa 3 (*Router-on-a-Stick* o switch multicapa L3).

---

## Preguntas de repaso

> [!question]- ¿Por qué una trama Ethernet que entra en un ciclo de switches puede derribar una red local mientras que un paquete IP en un ciclo de routers no lo hace?
> Porque los encabezados Ethernet no poseen un campo de tiempo de vida (*TTL* o *Hop Limit*). Un paquete IP se descarta tras agotar su TTL, pero un frame Ethernet en broadcast circula infinitamente, duplicándose en cada ciclo hasta saturar la memoria y el ancho de banda de todos los switches.

> [!question]- ¿Cuál es la diferencia fundamental entre un switch de capa 2 y un router de capa 3?
> Un switch L2 opera con direcciones físicas MAC de capa de enlace, mantiene una tabla de conmutación autoaprendida y aísla dominios de colisión; un router L3 opera con direcciones IP jerárquicas de capa de red, ejecuta algoritmos de enrutamiento (como OSPF o BGP) y aísla dominios de difusión entre subredes.

> [!question]- ¿Qué función cumple el etiquetado IEEE 802.1Q en un puerto troncal (*trunk port*)?
> Añade una etiqueta de 4 bytes a la trama Ethernet que identifica el *VLAN ID* al que pertenece el frame, permitiendo a los switches receptores discriminar y distribuir las tramas a sus respectivas VLANs lógicas de destino.
