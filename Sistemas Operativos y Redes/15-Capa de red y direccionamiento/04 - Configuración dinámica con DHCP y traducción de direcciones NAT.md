---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de red y direccionamiento"
tags:
  - sistemas-operativos
  - redes
  - dhcp
  - nat
  - upnp
  - redes-locales
  - origen/complemento
prerrequisitos:
  - "[[15-Capa de red y direccionamiento/03 - Direccionamiento IPv4: subredes, máscaras y notación CIDR|03 - Direccionamiento IPv4: subredes, máscaras y notación CIDR]]"
---

# Configuración dinámica con DHCP y traducción de direcciones NAT

Pocas veces configuramos a mano nuestra IP, y en una casa suele haber muchos equipos con una sola IP pública. Dos protocolos lo hacen posible: **DHCP** entrega la configuración a cada equipo que se conecta, y **NAT** permite que toda una red privada salga a Internet con una sola dirección.

## DHCP: configuración automática

**DHCP** (*Dynamic Host Configuration Protocol*, RFC 2131) es un protocolo **plug-and-play**: cuando detecta que un equipo se conecta a la red, le entrega los parámetros para conectarse, entre ellos su IP. Es un protocolo cliente-servidor de **4 etapas** (por sus iniciales se le dice DORA):

1. **Discover**: el cliente que llega (se enchufa a la red) envía un *DHCP discover message* a `255.255.255.255`, es decir, en **broadcast**: le llega a todos, porque todavía no sabe quién es el servidor.
2. **Offer**: el servidor responde con un *DHCP offer message*, también en broadcast, ofreciendo una IP.
3. **Request**: el cliente envía un *DHCP request message* pidiendo la IP ofrecida.
4. **ACK**: el servidor confirma con un *DHCP ACK message*.

![Flujo de cuatro pasos del protocolo DHCP: Discover, Offer, Request y ACK](adjuntos/Flujo%20de%20cuatro%20pasos%20del%20protocolo%20DHCP:%20Discover,%20Offer,%20Request%20y%20ACK.png)

> [!example]- Transcripción de la imagen
> *DHCP server: 223.1.2.5* y un *Arriving client*. **DHCP discover**: `src: 0.0.0.0, 68`, `dest: 255.255.255.255, 67`, `yiaddr: 0.0.0.0`, `transaction ID: 654`. **DHCP offer**: `src: 223.1.2.5, 67`, `dest: 255.255.255.255, 68`, `yiaddr: 223.1.2.4`, `transaction ID: 654`, `DHCP server ID: 223.1.2.5`, `Lifetime: 3600 secs`. **DHCP request**: `src: 0.0.0.0, 68`, `dest: 255.255.255.255, 67`, `yiaddr: 223.1.2.4`, `transaction ID: 655`, mismo server ID y lifetime. **DHCP ACK**: `src: 223.1.2.5, 67`, `dest: 255.255.255.255, 68`, `yiaddr: 223.1.2.4`, `transaction ID: 655`, mismo server ID y lifetime.

En la figura, el cliente usa `0.0.0.0` como origen porque aún no tiene IP, el servidor escucha en el puerto 67 y el cliente en el 68. La IP ofrecida (`yiaddr`, "your IP address") es `223.1.2.4`, prestada por 3600 segundos.

## NAT: muchas IP privadas, una pública

Las casas y oficinas pequeñas forman una **LAN**, pero el ISP les da una cantidad limitada de IP públicas, a veces solo una. **NAT** (*Network Address Translation*, RFC 2663 y RFC 3022) permite que **varios dispositivos se conecten a Internet usando una sola dirección IP pública**: dentro de la red se usan [[03 - Direccionamiento IPv4: subredes, máscaras y notación CIDR#Direcciones y subredes reservadas|direcciones privadas]] y el router traduce. Como la traducción usa también los puertos, a esta variante se le llama a veces NAPT (*Network Address and Port Translation*).

![Arquitectura de traducción de direcciones de red NAT en red local](adjuntos/Arquitectura%20de%20traducci%C3%B3n%20de%20direcciones%20de%20red%20NAT%20en%20red%20local.png)

> [!example]- Transcripción de la imagen
> PC1 (`192.168.0.5`), PC2 (`192.168.0.6`) y PC3 (`192.168.0.7`) se conectan al switch SW1, en la *Private network 192.168.0.0/24*. SW1 va a la interfaz `f0/0` (`192.168.0.1`) del *Router with NAT* R1, cuya interfaz `f0/1` (`200.100.101.1`) da a la *Public NETWORK* e Internet.

## Un ejemplo cotidiano

Mi IP interna es `192.168.1.86` y quiero conectarme desde el puerto 8120 a YouTube (`64.233.186.90`, puerto 443, HTTPS). Esa IP de destino no está en mi subred, así que el paquete va al **gateway** (puerta de enlace): el router.

1. El router NAT ve que alguien interno quiere hablar con alguien externo y **cambia el header**: reemplaza el origen `192.168.1.86:8120` por la IP que le dio el ISP, `138.76.29.7`, con un puerto nuevo, 6010. Anota la traducción en su tabla.
2. El servidor responde con origen `64.233.186.90:443` y destino `138.76.29.7:6010`.
3. El propio router busca en la tabla a quién corresponde el puerto 6010 y reescribe el destino a `192.168.1.86:8120`.

![Tabla de traducción NAT con puertos y direcciones IP públicas y privadas](adjuntos/Tabla%20de%20traducci%C3%B3n%20NAT%20con%20puertos%20y%20direcciones%20IP%20p%C3%BAblicas%20y%20privadas.png)

> [!example]- Transcripción de la imagen
> *NAT translation table*: *WAN side* `138.76.29.7, 5001` ↔ *LAN side* `10.0.0.1, 3345`. (1) el host `10.0.0.1` envía `S = 10.0.0.1, 3345; D = 128.119.40.186, 80` al router (`10.0.0.4` hacia dentro, `138.76.29.7` hacia fuera); (2) sale `S = 138.76.29.7, 5001; D = 128.119.40.186, 80`; (3) vuelve `S = 128.119.40.186, 80; D = 138.76.29.7, 5001`; (4) entra `S = 128.119.40.186, 80; D = 10.0.0.1, 3345`. A mano, en rojo, el ejemplo de YouTube: *IP externa 138.76.29.7: 6010* ↔ *192.168.1.86: 8120*, *IP destino (pública): 64.233.186.90*, y las respuestas *Origen 64.233.186.90:443, Destino 138.76.29.7:6010* y luego *Destino 192.168.1.86:8120*.

```python
IP_PUBLICA = "138.76.29.7"
tabla = {}                 # (IP pública, puerto WAN) -> (IP privada, puerto LAN)
siguiente_puerto = 6010

def salida(origen, destino):
    """Paquete que sale: se reemplaza el origen privado por la IP pública y un puerto nuevo."""
    global siguiente_puerto
    wan = (IP_PUBLICA, siguiente_puerto)
    siguiente_puerto += 1
    tabla[wan] = origen
    return wan, destino

def entrada(origen, destino):
    """Respuesta que entra: la tabla dice a qué host interno corresponde."""
    return origen, tabla[destino]

print(salida(("192.168.1.86", 8120), ("64.233.186.90", 443)))   # origen 138.76.29.7:6010
print(entrada(("64.233.186.90", 443), ("138.76.29.7", 6010)))   # destino 192.168.1.86:8120
```

## Servidores detrás de NAT

Eso funciona desde el lado del cliente. ¿Y si el **servidor** está detrás de NAT? Un cliente externo no puede contactarlo, porque su IP es **privada**. Tiene que conectarse a la dirección del router, y el router debe saber a quién reenviar. Para eso existe **UPnP** (*Universal Plug and Play*): permite que los servidores se **registren en el router NAT** con un mapeo dinámico `(IP privada, puerto privado) → (IP pública, puerto público)`. El router guarda qué puerto lleva a qué dirección, y el servidor debe **anunciarse** (por ejemplo, en un DNS) para que los clientes sepan a qué puerto conectarse.

![Traversal de NAT y reenvío de puertos mediante UPnP para servidores internos](adjuntos/Traversal%20de%20NAT%20y%20reenv%C3%ADo%20de%20puertos%20mediante%20UPnP%20para%20servidores%20internos.png)

> [!example]- Transcripción de la imagen
> Un *Client* con un signo de pregunta frente al *NAT router* (`138.76.29.7` hacia fuera, `10.0.0.4` hacia dentro). Anotaciones en rojo: "Cliente no puede contactar a la dirección de destino: `10.0.0.1:443`". "Debe conectarse a la dirección del router. IP destino: `138.76.29.7`, p: ?" y luego "IP destino: `138.76.29.7`, p: 4577". En el router, "Registro p:4577 --> `10.0.0.1`, p:443", que lleva al "servidor web. IP privada: `10.0.0.1`, p: 443".

## Los detractores de NAT

NAT es muy usado, pero tiene **detractores**:

- los **números de puerto son para procesos**, no para hosts: son de la [[14-Capa de transporte/02 - Multiplexación y desmultiplexación de puertos en UDP y TCP|capa de transporte]];
- los routers son de **capa 3**, y NAT los obliga a modificar puertos, que no son de capa 3;
- **viola el principio de extremo a extremo**: la comunicación debería ocurrir sin modificaciones intermedias;
- complica las aplicaciones en que alguien de afuera debe iniciar la conexión, como [[13-Capa de aplicación y sockets/06 - Redes Peer-to-Peer (P2P) y distribución con BitTorrent|P2P]] (de ahí UPnP);
- **es un parche**: con IPv6 ya no debería necesitarse NAT.

## Preguntas de repaso

> [!question]- ¿Por qué el DHCP discover se envía a `255.255.255.255`?
> Porque el cliente aún no tiene IP ni sabe cuál es el servidor DHCP: el broadcast llega a todos los equipos de la subred, incluido el servidor.

> [!question]- ¿Qué cambia el router NAT en un paquete que sale y cómo sabe a quién entregar la respuesta?
> Reemplaza la IP y el puerto de origen privados por su IP pública y un puerto nuevo, y anota esa traducción en su tabla. Cuando llega la respuesta a ese puerto, la tabla le dice a qué IP y puerto internos reenviarla.

> [!question]- ¿Cómo puede un cliente externo llegar a un servidor que está detrás de NAT?
> Conectándose a la IP pública del router en un puerto que el servidor registró (por ejemplo con UPnP); el router reenvía ese puerto a la IP y puerto privados del servidor.

> [!question]- ¿Por qué se dice que NAT viola el principio de extremo a extremo?
> Porque un dispositivo intermedio modifica los paquetes, y además toca puertos, que pertenecen a la capa de transporte, siendo el router un dispositivo de capa 3.
