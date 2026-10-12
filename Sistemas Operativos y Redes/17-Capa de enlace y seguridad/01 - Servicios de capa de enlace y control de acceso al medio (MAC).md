---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de enlace y seguridad"
tags:
  - sistemas-operativos
  - redes
  - capa-enlace
  - mac
  - aloha
  - csma-cd
  - origen/complemento
prerrequisitos:
  - "[[16-Algoritmos de ruteo/_Índice|Algoritmos de ruteo]]"
---

# Servicios de capa de enlace y control de acceso al medio (MAC)

La capa de red decide la ruta completa; la **capa de enlace** se encarga de cada tramo. Transmite **frames** (su unidad de transmisión) a través de **un** enlace, alámbrico o inalámbrico, y controla quién puede usar el medio cuando varios lo comparten. Su dispositivo característico es el **switch**.

![Diagrama de capa de enlace, switches, LANs, VLANs y protocolos de acceso al medio](adjuntos/Diagrama%20de%20capa%20de%20enlace%2c%20switches%2c%20LANs%2c%20VLANs%20y%20protocolos%20de%20acceso%20al%20medio.png)

> [!example]- Transcripción de la imagen
> Apunte a mano: "Capa de enlace: controlar el acceso al medio; envío de información a través. Dispositivo: Switch. Conceptos: LAN → Local Area network; VLAN → Virtual LAN. Acceso al medio: aleatorio, turnos, frecuencias, tiempos, virtual circuit switching. Protocolo IMPORTANTE: ALOHA → acceso aleatorio. Concepto: Direcciones MAC" (con una flecha roja). A la derecha, un router conectado a un switch que reparte hacia tres equipos, con dos grupos encerrados en rojo.

## Servicios

- **Encapsular** un paquete en frames y transmitirlo a través de **un** enlace.
- Determinar **quién puede usar el medio compartido**: *Medium Access Control* (MAC).
- **Transferencia confiable** en medios con alta tasa de errores.
- **Detección y corrección de errores**.
- **Control de flujo**: qué hacer si un host se satura y no puede recibir o emitir más frames.

**Cada enlace funciona de manera independiente** de los demás: un mismo paquete puede ir por Wi-Fi en un tramo y por Ethernet en otro. La capa de enlace se implementa en la **tarjeta de red** (NIC, *Network Interface Card*). Las LAN, las VLAN y las direcciones MAC se ven en [[02 - Direcciones MAC, protocolo ARP y trama Ethernet|direcciones MAC]] y [[03 - Conmutación en redes locales (Switches L2, STP) y VLANs|switches y VLANs]].

## Detección de errores

Para saber si un frame llegó con errores se agregan **bits de redundancia**:

- **Paridad simple**: un bit extra; detecta errores de un bit.
- **Paridad doble** (por filas y columnas): detecta y corrige errores de un bit, y detecta errores de 2 bits.
- **Checksum**: los bits se toman como enteros de $k$ bits y se suman. Es fácil de implementar en software, pero no protege contra muchos errores.
- **CRC** (*Cyclic Redundancy Check*): con los datos $D$ ($d$ bits) y un patrón conocido $G$ de $r + 1$ bits, se elige $R$ ($r$ bits) tal que la secuencia $\langle D, R \rangle$ sea **divisible por $G$** (en aritmética módulo 2, con XOR). El receptor divide lo que recibe por $G$: si el resto no es 0, hubo un error. Detecta errores de hasta $r$ bits.

Ejemplo del material: $D = 101110$, $G = 1001$; se obtiene $R = 011$ y se envía `101110011`.

```python
def resto(bits, G):
    """Resto de dividir bits por G en aritmética módulo 2 (XOR, sin acarreo)."""
    bits = [int(b) for b in bits]
    for i in range(len(bits) - len(G) + 1):
        if bits[i]:
            for j, g in enumerate(G):
                bits[i + j] ^= int(g)
    return "".join(map(str, bits[-(len(G) - 1):]))

D, G = "101110", "1001"
R = resto(D + "000", G)               # emisor: D·2^r con r = 3
print(R, "-> se envía", D + R)        # 011 -> se envía 101110011
print(resto(D + R, G))                # receptor: 000, sin errores
print(resto("101010011", G))          # con un bit cambiado: 100, se detecta
```

## Acceso al medio

El problema aparece en **medios compartidos** (*broadcast*): si dos nodos transmiten a la vez, sus señales chocan. Hay tres familias de soluciones.

**1. Partición del canal**, por tiempo, frecuencia o código:

| | Cómo divide | Costo |
|---|---|---|
| **TDMA** (tiempo) | Turnos fijos: con $N$ nodos y slots de $T$, rondas de $NT$. Con 6 nodos y slots de 5 s, el nodo 0 transmite en [0, 5), [30, 35), [60, 65)… | Los slots no usados se pierden |
| **FDMA** (frecuencia) | Cada estación tiene una banda fija, como los canales de radio o televisión | Las bandas no usadas quedan inactivas |
| **CDMA** (código) | Todos en la misma frecuencia, cada uno con un código ortogonal: se transmite dato × código | — |

**2. Acceso aleatorio** (protocolos optimistas): cada nodo transmite cuando quiere, con todo el ancho de banda. Si dos transmiten a la vez hay **colisión**, y el protocolo define cómo detectarla y cómo recuperarse.

- **ALOHA particionado** (*slotted ALOHA*): frames del mismo tamaño y tiempo dividido en particiones; solo se empieza a transmitir al inicio de una. Ante una colisión, cada nodo reintenta en la siguiente partición con probabilidad $p$. Con $N$ nodos, la probabilidad de que alguno transmita con éxito es $Np(1-p)^{N-1}$, cuyo máximo tiende a $1/e \approx 0{,}37$: el canal se usa **a lo más el 37 %** del tiempo.
- **ALOHA** (puro, sin particiones): cada uno habla cuando quiere y, si hay colisión, vuelve a intentar tras un **tiempo aleatorio**. Sin sincronización hay más colisiones: un frame enviado en $t_0$ choca con los enviados en $[t_0 - 1, t_0 + 1]$, y la eficiencia baja a **≈ 0,18** ($1/(2e) \approx 18{,}4\,\%$).
- **CSMA** (*Carrier Sense Multiple Access*): no interrumpir a los demás. Se **escucha antes de transmitir**: si el canal está libre se envía, y si no, se espera. Los retrasos de propagación igual permiten colisiones.
- **CSMA/CD** (*Collision Detection*): detecta la colisión rápido y **aborta** de inmediato, con una *jam signal*. Se usa en Ethernet (IEEE 802.3), comparando niveles de señal; en redes inalámbricas es difícil detectarla.
- **CSMA/CA** (*Collision Avoidance*): ante una colisión espera un tiempo aleatorio con **exponential backoff** (tras la $m$-ésima colisión, elige $K$ al azar en $\{0, 1, \dots, 2^m - 1\}$ y espera $K$ slots: cuantas más colisiones, más se dispersan los intentos), y el receptor confirma con un ACK si el CRC es correcto. Es el de Wi-Fi (IEEE 802.11). Como puede haber **terminales ocultos**, se complementa con los mensajes **RTS** (*Request to Send*) y **CTS** (*Clear to Send*).

**3. Por turnos:**

- **Polling (maestro/esclavo)**: el maestro invita a cada esclavo a transmitir. Es eficiente con terminales simples, pero tiene alta latencia con muchos esclavos y un punto de falla central. Lo usa Bluetooth.
- **Token**: los nodos se pasan un token y solo transmite quien lo tiene. Tiene alta latencia con muchos miembros, y el problema de qué pasa si desaparece el nodo que tiene el token. Ejemplos: FDDI, IEEE 802.5 *Token ring*.

## Preguntas de repaso

> [!question]- ¿Qué servicios ofrece la capa de enlace?
> Encapsular paquetes en frames y transmitirlos por un enlace, controlar el acceso al medio compartido (MAC), transferencia confiable, detección y corrección de errores, y control de flujo.

> [!question]- Con $D = 101110$ y $G = 1001$, ¿qué CRC se agrega y cómo verifica el receptor?
> $R = 011$, y se envía `101110011`. El receptor divide lo recibido por $G$ en módulo 2: si el resto es 0, no detectó errores.

> [!question]- ¿Por qué ALOHA particionado es más eficiente que ALOHA?
> Porque al empezar a transmitir solo al inicio de una partición, un frame solo puede chocar con los de la misma partición. Sube de ≈ 18 % a ≈ 37 %.

> [!question]- ¿Qué diferencia a CSMA/CD de CSMA/CA?
> CSMA/CD detecta la colisión mientras transmite y aborta (Ethernet). CSMA/CA, pensado para redes inalámbricas donde es difícil detectarla, espera tiempos aleatorios, confirma con ACK y usa RTS/CTS por los terminales ocultos.

> [!question]- ¿Qué desventajas tienen los protocolos por turnos?
> Alta latencia cuando hay muchos nodos y un punto de falla: el maestro en polling, o el nodo que tiene el token si desaparece.
