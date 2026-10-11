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
prerrequisitos:
  - "[[Capa de red y direccionamiento/02 - Datagrama IPv4: estructura y fragmentación por MTU|02 - Datagrama IPv4: estructura y fragmentación por MTU]]"
---

# Direccionamiento IPv4: subredes, máscaras y notación CIDR

Una dirección IPv4 es un identificador de 32 bits asignado a cada interfaz de red conectada a Internet. Para organizar y enrutar el tráfico eficientemente, las direcciones se dividen jerárquicamente en una porción de red (*network prefix*) y una porción de host (*host portion*), delimitadas mediante máscaras de subred y notación CIDR (*Classless Inter-Domain Routing*, `a.b.c.d/x`).

---

## Estructura de direcciones y subredes (mis apuntes)

Como la capa de red, utiliza la capa de enlace para hacer un salto a otro, hay que ver si ¿puede caber? en otros enlaces,
si no cabe, hay que fragmentarlo!!
Por ejemplo en 3 paquetes, con el mismo identificador, y con un flag, cuando se levante, ya no quedan fragmentos

DIRECCIONES IP
- Dado que esos numeros de 32 bits son limitados, no existen unicos para todos los dispositivos
- 146.155.13.15: 10010010.10011011.00001101.00101101
- DOTTED DECIMAL NOTATION → Grupo de 8 BITS: (0-255)
- IPV4: 4 Bytes → 32 bits: 2**32 direcciones posibles

Tenemos subconjuntos llamados Subredes → Se dividen por prefijos de direcciones IP
- ej: 223.1.1.0/24
- 223.1.1 = Subred
- .0/24 = Numero de host → la idea es que no se repite con otro computador
- 24 → Se Refiere a la ctd de bits que requiere la sub RED!!!
- Ademas se le añade una MASCARA

Classless interdomain Routing → a.b.c.d/x
ej: /24 : 255.255.255.0: equivalente a tener 24 bit 1, 8 bit 0

![Estructura de direcciones IPv4 con notación CIDR y máscara de subred](adjuntos/Estructura%20de%20direcciones%20IPv4%20con%20notación%20CIDR%20y%20máscara%20de%20subred.png)

> [!example]- Transcripción de la imagen
> Formato CIDR (`a.b.c.d/x`): La barra `/x` indica que los primeros $x$ bits corresponden a la porción de subred y los restantes $32 - x$ bits corresponden a la porción de host. La máscara de subred contiene $x$ unos binarios seguidos de $32 - x$ ceros.

MASCARA: Si quiero conocer a que su ¿red pertence una subred?, aplico un AND bit a bit con una Mascara
IP & MASCARA = SUBRED
En este caso: Dio que la SUBRED ES : 146.155.13.0

![Cálculo de dirección de red y broadcast mediante máscara de subred](adjuntos/Cálculo%20de%20dirección%20de%20red%20y%20broadcast%20mediante%20máscara%20de%20subred.png)

> [!example]- Transcripción de la imagen
> Operación AND bit a bit para obtener la dirección de subred:
> - IP: `146.155.13.15` $\to$ `10010010.10011011.00001101.00001111`
> - Máscara `/24`: `255.255.255.0` $\to$ `11111111.11111111.11111111.00000000`
> - Dirección de Red (AND): `146.155.13.0`
> - Dirección de Broadcast (hosts en 1): `146.155.13.255`

Para este ejemplo: Siempre son 2 las Direcciones que no podemos utilizar de esos 24 bits que son, para la subred hay 2 que no!
- La que tenga direccion 0 → Es el nombre de la Subred a.b.c.0 → Es la subred
- La que tiene todos: por ej: 146.155.13.255 → Esto sera la direccion de BROADCAST
Bits del host en 1: BROADCAST → Envio a todos los miembros de la SUBRED
→ IPV6: 6 Bytes → 128 bits: 2**128 direcciones posibles

Dentro del direccionamiento de REDES, cada Router es un LIMITANTE → pto limite
Cada ROUTER posee una direccion IP en cada salida
→ Switches por otro lado, NO poseen direccion IP
→ Switches son dispositivos de CAPA 2 (ENLACE)
Cada grupo de HOSTS conectados a un ROUTER → Forma una SUBRED
- En el ejemplo, hay 6 subredes!

![Topología de subredes conectadas mediante routers e interfaces IP](adjuntos/Topología%20de%20subredes%20conectadas%20mediante%20routers%20e%20interfaces%20IP.png)

> [!example]- Transcripción de la imagen
> Topología de subredes aisladas por routers: Una subred es una red IP cuyos dispositivos pueden comunicarse físicamente entre sí a nivel de Capa 2 (conmutadores) sin intermediación de un router. Los enlaces punto a punto entre interfaces de routers también constituyen subredes independientes (ej. con máscara `/30` o `/31`).

Direcciones reservadas
- 0.0.0.0. Forma de referirse a la Dirección de host actual (sólo sirve como origen). "Todas las IPs locales".
- 127.0.0.1. Dirección loopback (localhost)

Subredes reservadas
- Red local: 0.0.0.0/8
- Red loopback: 127.0.0.0/8
- 10.0.0.0 / 8
- 172.16.0.0 / 12
- 192.168.0.0 / 16
- Redes privadas:

Modelo antiguo de clasificacion de redes → CLASES

![Clasificación histórica de direcciones IP en clases A, B y C frente a CIDR](adjuntos/Clasificación%20histórica%20de%20direcciones%20IP%20en%20clases%20A,%20B%20y%20C%20frente%20a%20CIDR.png)

> [!example]- Transcripción de la imagen
> Direccionamiento por Clases (*Classful Addressing*):
> - Clase A: Prefijo `0...` (/8), 126 redes, 16 millones de hosts.
> - Clase B: Prefijo `10...` (/16), 16.384 redes, 65.534 hosts.
> - Clase C: Prefijo `110...` (/24), 2 millones de redes, 254 hosts.
> - Reemplazado por CIDR debido al desperdicio masivo de direcciones públicas.

Luego esto se descarto porque se usaban mas direcciones de las que realmente se necesitaban, era mas facil usar las MASCARAS para determinar el tamaño de subredes
Asignacion de Direcciones
ISPs (Proveedores de internet) asignan bloques de direcciones a organizaciones, y publican sus bloques
Organizaciones pueden crear nuevas subredes dentro de su bloque

> [!warning] Posible error en apuntes: Tamaño de dirección IPv6
> En los apuntes dice "IPV6: 6 Bytes → 128 bits". En realidad, 128 bits equivalen exactamente a **16 bytes** ($128 / 8 = 16$), no 6 bytes.

---

## Preguntas de repaso

> [!question]- ¿Por qué una subred con máscara `/24` solo permite direccionar hasta 254 hosts?
> Porque con 8 bits para hosts existen $2^8 = 256$ combinaciones posibles, pero se descuentan 2 direcciones especiales obligatorias: la dirección de red (todos ceros binarios, ej. `.0`) y la dirección de broadcast (todos unos binarios, ej. `.255`).

> [!question]- ¿Por qué un router tiene asignada más de una dirección IP?
> Porque un router es un dispositivo multitarjeta que interconecta dos o más subredes; cada interfaz física de red conectada a una subred distinta debe poseer una dirección IP válida perteneciente a dicha subred.

> [!question]- ¿Cuáles son los rangos de direcciones IP privadas definidos por el RFC 1918 y por qué no se enrutan en Internet?
> `10.0.0.0/8`, `172.16.0.0/12` y `192.168.0.0/16`. Están reservadas para redes locales privadas y los routers globales de Internet descartan cualquier paquete dirigido a ellas, exigiendo NAT para salir al exterior.

