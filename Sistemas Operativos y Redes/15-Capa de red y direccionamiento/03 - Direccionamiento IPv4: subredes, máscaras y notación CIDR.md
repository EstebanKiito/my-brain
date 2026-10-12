---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de red y direccionamiento"
tags:
  - sistemas-operativos
  - redes
  - ipv4
  - subredes
  - mascaras
  - cidr
  - origen/complemento
prerrequisitos:
  - "[[15-Capa de red y direccionamiento/02 - Datagrama IPv4: estructura y fragmentación por MTU|02 - Datagrama IPv4: estructura y fragmentación por MTU]]"
---

# Direccionamiento IPv4: subredes, máscaras y notación CIDR

El [[02 - Datagrama IPv4: estructura y fragmentación por MTU|datagrama IP]] lleva las direcciones de origen y destino, y la capa de red lo hace saltar de enlace en enlace (fragmentándolo si no cabe). Falta entender qué es una dirección IP y cómo se agrupan las direcciones en **subredes**, que es lo que permite que las tablas de reenvío trabajen con prefijos.

## Direcciones IPv4

- Una dirección IPv4 mide **32 bits = 4 bytes**, así que hay $2^{32} = 4\,294\,967\,296$ direcciones posibles.
- Se escribe en **notación decimal con puntos** (*dotted-decimal notation*): cuatro grupos de 8 bits, cada uno entre 0 y 255. Por ejemplo, `146.155.13.45` es `10010010.10011011.00001101.00101101`.
- Debe ser **única globalmente**, aunque solo "casi": como los números de 32 bits son limitados, no alcanzan para todos los dispositivos (de ahí las redes privadas y [[04 - Configuración dinámica con DHCP y traducción de direcciones NAT|NAT]]).

IPv6 resuelve la escasez con direcciones de **128 bits (16 bytes)**: $2^{128}$ direcciones posibles (ver [[05 - Protocolo ICMP y transición a IPv6: dual-stack y tunneling|IPv6]]).

## Subredes y notación CIDR

Una **subred** es un subconjunto de direcciones con el mismo **prefijo**. Se escribe con la notación **CIDR** (*Classless Interdomain Routing*): `a.b.c.d/x`.

- Los **primeros $x$ bits** definen la subred. En `223.1.1.0/24`, los 24 bits de `223.1.1` son la subred.
- Los **últimos $32 - x$ bits** definen el host dentro de la subred, y no se repiten entre dos equipos de la misma subred. En `223.1.1.40/24`, el host es el `.40`.
- La **máscara** tiene $x$ bits en 1 y $32 - x$ en 0. Para `/24` es `255.255.255.0`: 24 unos y 8 ceros.

Para saber a qué subred pertenece una IP se hace un **AND bit a bit** con la máscara: **IP & máscara = subred**.

![Estructura de direcciones IPv4 con notación CIDR y máscara de subred](adjuntos/Estructura%20de%20direcciones%20IPv4%20con%20notaci%C3%B3n%20CIDR%20y%20m%C3%A1scara%20de%20subred.png)

> [!example]- Transcripción de la imagen
> `146.155.13.78` = `10010010.10011011.00001101.01001110`; `255.255.255.0` = `11111111.11111111.11111111.00000000`; el AND bit a bit da `146.155.13.0` = `10010010.10011011.00001101.00000000`.

## Dos direcciones que no se usan

En cada subred hay **dos direcciones reservadas**: la que tiene todos los bits de host en 0 es el **nombre de la subred**, y la que los tiene todos en 1 es la **dirección de broadcast**, que sirve para enviar a todos los miembros de la subred. Por eso una `/24` admite $2^8 - 2 = 254$ hosts.

![Cálculo de dirección de red y broadcast mediante máscara de subred](adjuntos/C%C3%A1lculo%20de%20direcci%C3%B3n%20de%20red%20y%20broadcast%20mediante%20m%C3%A1scara%20de%20subred.png)

> [!example]- Transcripción de la imagen
> "Subred: `146.155.13.0/24`. 24 bits para subred, 8 bit para host. Tamaño de subred: $2^8 = 256 - 2 = 254$ hosts máximo. Nombre de subred: bits de *host* en 0: `146.155.13.0`. Dirección broadcast: bits de *host* en 1: `146.155.13.255`. Máscara (mask): $x$ bit en 1, $32 - x$ bit en 0: `255.255.255.0`". Abajo: "Google: IP calculator".

```python
from ipaddress import IPv4Address as IP

def subred(ip, x):
    """IP & máscara = subred; bits de host en 1 = broadcast."""
    mascara = (0xFFFFFFFF << (32 - x)) & 0xFFFFFFFF      # x unos y 32 - x ceros
    red = int(IP(ip)) & mascara
    broadcast = red | (~mascara & 0xFFFFFFFF)
    return str(IP(mascara)), str(IP(red)), str(IP(broadcast)), 2 ** (32 - x) - 2

print(subred("146.155.13.78", 24))   # ('255.255.255.0', '146.155.13.0', '146.155.13.255', 254)
print(subred("223.1.1.40", 24))      # ('255.255.255.0', '223.1.1.0', '223.1.1.255', 254)
```

## Routers y subredes

Cada router es un **punto límite** entre subredes: posee **una dirección IP en cada salida** (interfaz). Los **switches**, en cambio, **no tienen dirección IP**, porque son dispositivos de capa 2 ([[17-Capa de enlace y seguridad/03 - Conmutación en redes locales (Switches L2, STP) y VLANs|enlace]]). Cada grupo de hosts conectados a un router forma una subred, y también los enlaces entre routers.

![Topología de subredes conectadas mediante routers e interfaces IP](adjuntos/Topolog%C3%ADa%20de%20subredes%20conectadas%20mediante%20routers%20e%20interfaces%20IP.png)

> [!example]- Transcripción de la imagen
> Tres routers en triángulo. **R1** tiene las interfaces `223.1.1.3` (hacia los hosts `223.1.1.1` y `223.1.1.4`), `223.1.9.2` y `223.1.7.0`. **R2** tiene `223.1.9.1`, `223.1.8.1` y `223.1.2.6` (hacia `223.1.2.1` y `223.1.2.2`). **R3** tiene `223.1.7.1`, `223.1.8.0` y `223.1.3.27` (hacia `223.1.3.1` y `223.1.3.2`).

En el ejemplo hay **6 subredes**: las tres de hosts (`223.1.1`, `223.1.2` y `223.1.3`) y las tres que unen a los routers entre sí (`223.1.7`, `223.1.8` y `223.1.9`).

## Direcciones y subredes reservadas

| Dirección o subred | Uso |
|---|---|
| `0.0.0.0` | El host actual, "todas las IPs locales"; solo sirve como origen |
| `127.0.0.1` | *Loopback* (`localhost`) |
| `0.0.0.0/8` | Red local |
| `127.0.0.0/8` | Red *loopback* |
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | Redes privadas (RFC 1918) |

## De las clases a CIDR

En el modelo antiguo (*classful routing*), las direcciones se dividían en **clases** según sus primeros bits, con tamaños fijos de red:

![Clasificación histórica de direcciones IP en clases A, B y C frente a CIDR](adjuntos/Clasificaci%C3%B3n%20hist%C3%B3rica%20de%20direcciones%20IP%20en%20clases%20A,%20B%20y%20C%20frente%20a%20CIDR.png)

> [!example]- Transcripción de la imagen
> Tabla *Clase / bits / Rango de direcciones / Hosts por red / # redes*: **A**, `0`, 1.0.0.0 → 126.0.0.0, $2^{24} - 2 = 16\,777\,214$, $2^7 - 2 = 126$. **B**, `10`, 128.1.0.0 → 191.254.0.0, $2^{16} - 2 = 65\,534$, $2^{14} - 2 = 16\,382$. **C**, `110`, 192.0.1.0 → 223.255.254.0, $2^8 - 2 = 254$, $2^{21} - 2 = 2\,097\,150$. **D**, `1110`, 224.0.0.1 → 239.255.255.254, multicast. **E**, `11110`, 240.0.0.1 → 247.255.255.254, reservado para uso futuro. Abajo, las 32 bits de cada clase divididas en *Red* y *Host* (A: 8/24, B: 16/16, C: 24/8).

Se descartó porque se asignaban muchas más direcciones de las que se necesitaban: una organización con 300 equipos no cabía en una clase C y recibía una B de 65 534. Con **máscaras** de largo arbitrario, el tamaño de cada subred se ajusta a lo necesario.

**Asignación:** los ISP asignan bloques de direcciones a las organizaciones y publican sus bloques; cada organización puede crear nuevas subredes dentro del suyo. Los bloques los administra la ICANN (*Internet Corporation for Assigned Names and Numbers*), que los asigna a los registros regionales de Internet.

## Preguntas de repaso

> [!question]- ¿Cómo se obtiene la subred de `146.155.13.78/24`?
> Con un AND bit a bit entre la IP y la máscara `255.255.255.0`: da `146.155.13.0`.

> [!question]- ¿Por qué una subred `/24` admite solo 254 hosts?
> Porque los 8 bits de host dan 256 combinaciones, y se descuentan el nombre de la subred (bits de host en 0) y el broadcast (bits de host en 1).

> [!question]- ¿Por qué un router tiene varias direcciones IP y un switch ninguna?
> El router tiene una IP en cada interfaz porque cada una pertenece a una subred distinta. El switch trabaja en la capa 2 y no necesita dirección IP.

> [!question]- ¿Por qué se reemplazaron las clases por CIDR?
> Porque las clases tenían tamaños fijos (8, 16 o 24 bits de red) y se desperdiciaban direcciones. CIDR permite máscaras de cualquier largo.
