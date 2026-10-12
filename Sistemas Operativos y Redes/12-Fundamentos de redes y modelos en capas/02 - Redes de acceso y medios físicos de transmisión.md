---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/acceso
  - redes/medios-fisicos
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/12-Fundamentos de redes y modelos en capas/01 - Arquitectura de Internet, nodos, enlaces y protocolos\|01 - Arquitectura de Internet, nodos, enlaces y protocolos]]"
---

# Redes de acceso y medios físicos de transmisión

Antes de cruzar Internet, los datos de un computador tienen que llegar a la red: ese primer tramo es la **red de acceso**. Hay muchas tecnologías para hacerlo, y todas terminan transmitiendo bits por algún **medio físico**: un cable, una fibra o el aire.

## Clientes y servidores

La comunicación es **de extremo a extremo** entre **hosts**, dispositivos que ejecutan programas. Unos actúan como **clientes** y otros como **servidores**; es un **rol que toma un programa**, no un tipo de máquina:

- **Clientes:** en dispositivos livianos que **solicitan** servicios; suelen estar bajo control del usuario.
- **Servidores:** en dispositivos poderosos que **proveen** servicios; suelen vivir en *data centers* o en la nube.

## Tecnologías de acceso

| Tecnología | Cómo funciona | Característica clave |
|---|---|---|
| **DSL** (*Digital Subscriber Line*) | Usa la **línea telefónica** tradicional. El módem DSL convierte la señal digital en análoga y el **DSLAM** de la central la reconvierte | Separa la línea por **frecuencias**: teléfono 0-4 kHz, subida 4-50 kHz, bajada 50 kHz-1 MHz. Enlace **privado** |
| **Cable** (HFC, *Hybrid Fiber Coaxial*) | Usa la red de TV por cable: fibra hasta un nodo del barrio y luego **coaxial** | **Medio compartido**: si muchos vecinos navegan a la vez, se congestiona. Asimétrico (42,8 Mbps bajada, 30,7 Mbps subida) |
| **FTTH** (*Fiber To The Home*) | **Fibra óptica** hasta la casa; el ONT (casa) y el OLT (proveedor) convierten entre señal óptica y eléctrica | Muy alta tasa de transmisión; estándares desde 1 Mbps a 1 Gbps |
| **Dial-up** y **satélite** | Dial-up por línea telefónica (2,4 a 56 kbps), la conexión original; satélite para zonas rurales | Lentos, históricamente |
| **Ethernet** (IEEE 802.3) | Pares trenzados de cobre | 10 Mbps a 10 Gbps; implementa la **LAN** (*Local Area Network*) |
| **Wi-Fi** (IEEE 802.11) | Como Ethernet, pero **inalámbrico** y de corto alcance | 54 Mbps, 150 Mbps…; implementa la **WLAN** (*Wireless LAN*) |
| **Banda ancha móvil** (3G, 4G, LTE) | Inalámbrico de **área amplia** (*wide area*) | Conexión a través de antenas celulares |

En una LAN típica, el router se conecta a un **switch**, que comparte la conexión con varios dispositivos, cada uno con su ancho de banda estandarizado.

![Red de acceso mediante línea telefónica DSL](adjuntos/Red%20de%20acceso%20mediante%20l%C3%ADnea%20telef%C3%B3nica%20DSL.png)

> [!example]- Transcripción de la imagen
> *Home phone* y *Home PC* (con *DSL modem*) se unen en un *Splitter* conectado a la *Existing phone line*: "0-4KHz phone; 4-50KHz upstream data; 50KHz-1MHz downstream data". En la *Central office*, el **DSLAM** separa el tráfico hacia *Internet* y hacia la *Telephone network*.

![Red de acceso mediante cable coaxial y medio compartido](adjuntos/Red%20de%20acceso%20mediante%20cable%20coaxial%20y%20medio%20compartido.png)

> [!example]- Transcripción de la imagen
> Grupos de *Hundreds of homes* conectados por *Coaxial cable* a un *Fiber node*; desde ahí, *Fiber cable* hasta el *Cable head end*, donde el **CMTS** conecta con *Internet*.

![Red de área local cableada Ethernet con switches y routers](adjuntos/Red%20de%20%C3%A1rea%20local%20cableada%20Ethernet%20con%20switches%20y%20routers.png)

> [!example]- Transcripción de la imagen
> Varios computadores conectados a 100 Mbps a un *Ethernet switch*, junto con un *Server*; el switch se conecta a un *Institutional router*, que va *To Institution's ISP*.

![Red de acceso inalámbrico Wi-Fi y banda ancha móvil](adjuntos/Red%20de%20acceso%20inal%C3%A1mbrico%20Wi-Fi%20y%20banda%20ancha%20m%C3%B3vil.png)

> [!example]- Transcripción de la imagen
> Una *House* con notebook y computador conectados (inalámbricamente y por cable) a un router con punto de acceso; el router va a un módem de cable, y de ahí por el tendido al *Cable head end* y a *Internet*.

## Medios físicos

Los bits se transmiten como **ondas** a través de un medio:

- **Guiados** (sólidos): el par trenzado de cobre, el cable coaxial y la fibra óptica.
- **No guiados**: inalámbricos y enlace satelital, donde la señal se difunde (*broadcast*).

| Medio | Características |
|---|---|
| **Par trenzado de cobre** (UTP, *unshielded twisted pair*) | Cables de cobre trenzados entre sí, sin blindaje (la versión blindada es STP); categorías según cuán trenzados están (3, 5, 5e, 6, 6a). 10 Mbps a 10 Gbps. Se usa en telefonía y Ethernet (LAN) |
| **Cable coaxial de cobre** | Un par concéntrico (no trenzado), con **alta resistencia al ruido externo**; fácil insertar nodos nuevos; **medio compartido** |
| **Fibra óptica** | Transmite **haces de luz** por fibra de vidrio. **Inmune a la interferencia electromagnética**, alta velocidad y baja atenuación (más de 100 km). Monomodo (un haz) o multimodo (varios haces en distintos ángulos) |
| **Inalámbrico** | La señal se debilita al propagarse y queda expuesta a interferencias y obstáculos. **Propagación multicamino**: la señal llega por varios caminos (rebotes) a distintos tiempos y se distorsiona |

> [!tip] Para profundizar
> Video de referencia sobre redes de acceso: <https://www.youtube.com/watch?v=_pyWVod9dzE&list=PLVTkEjeczcER2aOMHPIfaHCpTx61iKsoV&index=51>

## Preguntas de repaso

> [!question]- ¿Por qué el acceso por cable puede ponerse lento en horas punta y DSL no tanto?
> Porque el cable es un medio compartido entre los hogares del barrio: si muchos lo usan a la vez, se reparten la capacidad. En DSL, cada casa tiene su propia línea hasta la central.

> [!question]- ¿Cómo comparte DSL la línea telefónica entre voz y datos?
> Usando frecuencias distintas: el teléfono va de 0 a 4 kHz, la subida de 4 a 50 kHz y la bajada de 50 kHz a 1 MHz.

> [!question]- ¿Qué diferencia hay entre medios guiados y no guiados?
> En los guiados la señal viaja por un medio sólido (cobre o fibra). En los no guiados se propaga por el aire o el espacio, y queda más expuesta a atenuación, interferencias y propagación multicamino.

> [!question]- ¿Qué ventajas tiene la fibra óptica frente al cobre?
> Transmite luz en vez de electricidad, así que es inmune a la interferencia electromagnética, alcanza velocidades más altas y se atenúa muy poco con la distancia.
