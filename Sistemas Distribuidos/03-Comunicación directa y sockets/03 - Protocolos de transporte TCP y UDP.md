---
ramo: "Sistemas Distribuidos"
tema: "Comunicación directa y sockets"
tags:
  - sd/comunicacion
  - redes
  - origen/complemento
prerrequisitos:
  - "[[01 - Persistencia, sincronía y acoplamiento]]"
---

# Protocolos de transporte TCP y UDP

Toda comunicación por la red responde dos preguntas. La primera es **cómo se transporta** la información: con TCP o con UDP. La segunda es **qué pasos** sigue cada servicio (transferir un archivo, enviar un correo), y eso lo definen los protocolos de aplicación. Esta nota trata la primera; la elección entre TCP y UDP es un intercambio entre garantías y velocidad.

## TCP: confiable y ordenado

![Handshake y retransmisión en TCP](adjuntos/Handshake%20y%20retransmisi%C3%B3n%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> Diagrama de secuencia entre un cliente y un servidor: `SYN`, `SYN + ACK` y `ACK` establecen la conexión (✅). Luego el servidor envía `Data 1`, que se pierde (❌); el cliente responde `Nak`, el servidor reenvía `Data 1` y el cliente confirma con `ACK` (✅).

- **Antes de enviar datos** establece una conexión bidireccional con el **three-way handshake** (`SYN`, `SYN+ACK`, `ACK`).
- **Garantiza** que todos los datos lleguen a destino, **en orden y sin duplicados**.
- Implementa **acknowledgments y retransmisiones** para manejar la pérdida de paquetes.
- Puede enviar mensajes grandes, que fragmenta en **segmentos**.
- **Desventaja:** es más lento, y a veces sus garantías son redundantes para la aplicación.

Lo usan HTTP (páginas web), FTP (archivos), SMTP (correo) y SSH (acceso remoto).

## UDP: rápido y sin garantías

![Datagramas UDP perdidos y desordenados](adjuntos/Datagramas%20UDP%20perdidos%20y%20desordenados.png)

> [!example]- Transcripción de la imagen
> El cliente envía un `Request` y el servidor responde con `Data 1` a `Data 5`. `Data 1` se pierde (❌) y no se reenvía; `Data 2`, `Data 3` y `Data 5` llegan, y `Data 4` llega al final, después de `Data 5`.

- **No hay handshake** ni conexión previa.
- Envía datagramas de **máximo 64 KB**.
- Los paquetes **se pueden perder o llegar desordenados**, y **no se reenvían**.
- Es **mucho más rápido**, porque se salta las verificaciones y los reenvíos.

Se usa cuando la velocidad importa más que la integridad y el orden: juegos en línea, llamadas, sensores y protocolos como **DNS** y **NTP** (sincronización de relojes, que se estudia más adelante).

```python
import socket
srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv.bind(("localhost", 4446))
cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cli.sendto(b"posicion x=10 y=4", ("localhost", 4446))   # sin connect ni handshake
datos, origen = srv.recvfrom(1024)
print(datos.decode(), "desde", origen[0])               # posicion x=10 y=4 desde 127.0.0.1
```

## Cuándo usar cada uno

| | TCP | UDP |
|---|---|---|
| Conexión previa | Sí (handshake) | No |
| Entrega y orden | Garantizados | No garantizados |
| Retransmisión | Sí | No |
| Velocidad | Menor | Mayor |
| Ejemplos | Web, archivos, correo, SSH, chat | Juegos, voz, video en vivo, DNS, NTP |

> [!tip] El ejemplo del juego de disparos
> En un juego en línea las **posiciones y balazos** van por **UDP**: un dato viejo no sirve, y es mejor perder uno que esperar su reenvío. Los mensajes del **chat** van por **TCP**: tienen que llegar todos y en orden.

> [!warning] UDP "rápido" no significa "mejor"
> Si la aplicación necesita todos los datos, al usar UDP tiene que reimplementar por su cuenta las confirmaciones y los reenvíos, y suele terminar haciéndolo peor que TCP.

El funcionamiento interno (segmentos, checksum, ventanas, temporizadores) está en [[06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa|Protocolo TCP]], [[07 - Gestión de temporizadores, retransmisión rápida y handshake en TCP|Handshake y retransmisión en TCP]] y [[03 - Protocolo UDP: datagramas, sobrecarga y checksum|Protocolo UDP]].

## Preguntas de repaso

> [!question]- ¿Para qué sirve el three-way handshake de TCP?
> Para que ambos extremos confirmen que el otro está dispuesto a comunicarse y acuerden el estado inicial de la conexión antes de enviar datos. Sin él, TCP no podría garantizar entrega ni orden.

> [!question]- ¿Por qué DNS usa UDP si una respuesta perdida rompe la consulta?
> Porque la consulta y la respuesta son mensajes pequeños de un solo paquete: es más barato reintentar la consulta completa si no hay respuesta que pagar un handshake en cada búsqueda.

> [!question]- En una videollamada, ¿qué pasa si un paquete de audio se pierde con UDP y qué pasaría con TCP?
> Con UDP se pierde un fragmento breve y la llamada sigue. Con TCP se esperaría su retransmisión y todo el audio posterior quedaría detenido, lo que se nota como cortes y retraso.
