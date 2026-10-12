---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - tcp
  - timeouts
  - fast-retransmit
  - handshake
  - origen/complemento
prerrequisitos:
  - "[[14-Capa de transporte/06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa|06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa]]"
---

# Gestión de temporizadores, retransmisión rápida y handshake en TCP

Con el [[06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa|segmento y el ACK acumulativo]] definidos, falta ver cómo TCP los usa: cuándo retransmite, cómo evita retransmisiones inútiles y cómo abre y cierra una conexión.

## Implementación: SendBase y NextSeqNum

El emisor lleva dos variables, igual que la ventana de [[14-Capa de transporte/05 - Protocolos de canalización: Go-Back-N y Selective Repeat|Go-Back-N]]:

- **SendBase**: la base de la ventana, el byte más antiguo enviado y aún sin ACK. Desde ahí parte la ventana.
- **NextSeqNum**: el número de secuencia del próximo segmento nuevo. Todo lo anterior ya se envió: una parte recibió ACK y otra no, porque el segmento o su ACK pudieron perderse.

![Variables de control SendBase y NextSeqNum en emisor TCP](adjuntos/Variables%20de%20control%20SendBase%20y%20NextSeqNum%20en%20emisor%20TCP.png)

> [!example]- Transcripción de la imagen
> Una fila de números de secuencia con la clave: *Already ACK'd* (azul oscuro), *Sent, not yet ACK'd* (celeste), *Usable, not yet sent* (gris) y *Not usable* (blanco). **send_base** marca el primer celeste y **nextseqnum** el primer gris; entre send_base y el final de los grises está el *Window size N*.

Las reglas del emisor son tres:

1. **Al expirar el timer** (su duración es el RTO, *retransmission timeout*, que TCP ajusta según el RTT medido), retransmite **solo el segmento con el menor número de secuencia** sin ACK. En eso se parece a Selective Repeat: no reenvía toda la ventana.
2. **Si llega un ACK mayor que SendBase**, actualiza SendBase a ese valor. Como el ACK es acumulativo, recibir un ACK más adelante significa que **ya llegaron todos los bytes anteriores**, aunque sus propios ACK se hayan perdido.
3. Si quedan segmentos sin ACK, reinicia el timer.

## Tres escenarios

**ACK perdido.** A envía `Seq=92` (8 bytes) y el `ACK=100` se pierde. Expira el timer: A reenvía el segmento más antiguo y reinicia el timer. B recibe un duplicado, lo descarta y vuelve a enviar `ACK=100`.

![Manejo de timeout y retransmisión por pérdida de ACK en TCP](adjuntos/Manejo%20de%20timeout%20y%20retransmisi%C3%B3n%20por%20p%C3%A9rdida%20de%20ACK%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> Host A envía `Seq=92, 8 bytes data`. Host B responde `ACK=100`, que se pierde (*X loss*). Tras el *Timeout*, A reenvía `Seq=92, 8 bytes data` y B responde `ACK=100`, que esta vez llega.

**Timeout prematuro.** A envía `Seq=92` y `Seq=100`, pero el timer de 92 expira antes de que lleguen los ACK. No importa: A reenvía solo `Seq=92` y reinicia el timer. Luego llegan `ACK=100` y `ACK=120`: el de 120 confirma también el segmento 100, así que A **no reenvía** `Seq=100`. B recibe el 92 duplicado, lo descarta y responde con el ACK acumulativo `ACK=120`.

![Escenario de timeout prematuro y confirmación acumulativa en TCP](adjuntos/Escenario%20de%20timeout%20prematuro%20y%20confirmaci%C3%B3n%20acumulativa%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> A envía `Seq=92, 8 bytes data` y `Seq=100, 20 bytes data`. B responde `ACK=100` y `ACK=120`, pero llegan después de que termina el *seq=92 timeout interval*. A reenvía `Seq=92, 8 bytes data` y abre un nuevo intervalo; B responde `ACK=120`.

**El ACK acumulativo evita una retransmisión.** A envía `Seq=92` y `Seq=100`; el `ACK=100` se pierde, pero `ACK=120` llega antes del timeout. Es como si hubiera llegado el 100: A sabe que B recibió todo hasta el byte 119, **no reenvía** `Seq=92`, avanza SendBase a 120 y **corta el timer**.

![Cancelación de temporizador y avance de SendBase en TCP](adjuntos/Cancelaci%C3%B3n%20de%20temporizador%20y%20avance%20de%20SendBase%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> A envía `Seq=92, 8 bytes data` y `Seq=100, 20 bytes data`. El `ACK=100` se pierde (*X loss*). El `ACK=120` llega dentro del *Seq=92 timeout interval*, así que no hay retransmisión.

## Retransmisión rápida

Los timeouts pueden tomar mucho tiempo. La **retransmisión rápida** (*fast retransmit*) reenvía de forma proactiva un segmento que probablemente se perdió, **antes de que ocurra el timeout**. La señal son los **ACK duplicados**: si se pierde un segmento, el receptor sigue confirmando el mismo byte por cada segmento posterior que recibe. Al recibir **tres ACK duplicados** (cuatro ACK iguales en total), el emisor reenvía el segmento sin esperar el timer. Se esperan tres y no uno porque un segmento que llega un poco desordenado también produce algún duplicado.

![Mecanismo de retransmisión rápida con tres ACKs duplicados en TCP](adjuntos/Mecanismo%20de%20retransmisi%C3%B3n%20r%C3%A1pida%20con%20tres%20ACKs%20duplicados%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> A envía `seq=92` (8 bytes), `seq=100` (20 bytes, se pierde: X), `seq=120` (15 bytes), `seq=135` (6 bytes) y `seq=141` (16 bytes). B responde `ack=100` cuatro veces. Al recibir los duplicados, dentro del intervalo de *Timeout*, A reenvía `seq=100, 20 bytes of data`.

Cuando llega el reenvío, B ya tiene en buffer el resto y responde `ACK = 157` ($141 + 16$): confirma todo de una vez. Básicamente, así funciona TCP.

```python
SEGS = {92: 8, 100: 20, 120: 15, 135: 6, 141: 16}   # seq -> bytes, como en la figura

def ack(recibidos, esperado=92):
    """ACK acumulativo: próximo byte esperado (lo fuera de orden queda en buffer)."""
    while esperado in recibidos:
        esperado += SEGS[esperado]
    return esperado

recibidos, ultimo, dup = set(), None, 0
for seq in SEGS:
    if seq == 100:
        continue                          # se pierde: no genera ACK
    recibidos.add(seq)
    a = ack(recibidos)
    print(f"llega seq={seq} -> ACK={a}")  # 100, 100, 100, 100
    dup = dup + 1 if a == ultimo else 0
    ultimo = a
    if dup == 3:                          # tercer ACK duplicado
        recibidos.add(a)                  # retransmisión rápida del seq=100
        print(f"reenvío seq={a} antes del timeout -> ACK={ack(recibidos)}")  # 157
```

## Handshake de tres pasos y cierre

TCP es orientado a conexión: antes de enviar datos, cliente y servidor acuerdan sus números de secuencia iniciales.

1. El cliente envía un segmento con el flag **SYN** y su número de secuencia inicial (`client_isn`).
2. El servidor recibe el SYN, **asigna buffers**, elige su propio número inicial (`server_isn`) y responde con un **SYN ACK** (`ack = client_isn + 1`).
3. El cliente recibe el SYN ACK y responde con un **ACK** (`ack = server_isn + 1`). Este segmento **ya puede llevar datos**.

Con tres pasos, cada lado confirma el número inicial del otro; así no se confunde una conexión nueva con segmentos atrasados de una vieja.

Para **cerrar**, cada lado envía un **FIN** y espera su ACK: se cierran los buffers y luego la conexión. El que cerró primero espera un tiempo (*timed wait*, estado `TIME_WAIT`) antes de cerrar del todo (típicamente $2 \times$ MSL, el tiempo máximo de vida de un segmento en la red), por si su último ACK se pierde y tiene que reenviarlo. Un segmento con **RST** aborta la conexión sin este intercambio.

![Establecimiento de conexión TCP con saludo de tres vías y terminación con FIN](adjuntos/Establecimiento%20de%20conexi%C3%B3n%20TCP%20con%20saludo%20de%20tres%20v%C3%ADas%20y%20terminaci%C3%B3n%20con%20FIN.png)

> [!example]- Transcripción de la imagen
> **Izquierda**: *Connection request*: el cliente envía `SYN=1, seq=client_isn`. *Connection granted*: el servidor responde `SYN=1, seq=server_isn, ack=client_isn+1`. *ACK*: el cliente envía `SYN=0, seq=client_isn+1, ack=server_isn+1`. **Derecha**: el cliente hace *Close* y envía `FIN`; el servidor responde `ACK`. Luego el servidor hace *Close* y envía `FIN`; el cliente responde `ACK`, pasa por *Timed wait* y queda *Closed*.

## Preguntas de repaso

> [!question]- ¿Qué segmento retransmite TCP cuando expira el timer?
> Solo el de menor número de secuencia sin ACK (el que está en SendBase), no toda la ventana.

> [!question]- En el escenario donde se pierde `ACK=100` pero llega `ACK=120` antes del timeout, ¿qué hace A?
> Nada se retransmite: el ACK acumulativo confirma todo hasta el byte 119. A avanza SendBase a 120 y corta el timer.

> [!question]- ¿Qué dispara la retransmisión rápida y por qué no basta un ACK duplicado?
> Tres ACK duplicados. Un solo duplicado puede deberse a un segmento que llegó desordenado; tres son señal fuerte de pérdida.

> [!question]- ¿Qué hace el servidor en el segundo paso del handshake?
> Asigna buffers, elige su número de secuencia inicial y responde con SYN ACK, confirmando `client_isn + 1`.

> [!question]- ¿Para qué espera el cliente en *timed wait* al cerrar?
> Por si su último ACK se pierde: el servidor reenviaría su FIN y el cliente podría volver a confirmarlo.
