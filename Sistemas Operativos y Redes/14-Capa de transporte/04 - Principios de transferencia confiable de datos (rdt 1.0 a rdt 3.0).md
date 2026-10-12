---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - rdt
  - transferencia-confiable
  - timeouts
  - checksum
  - origen/complemento
prerrequisitos:
  - "[[14-Capa de transporte/03 - Protocolo UDP: datagramas, sobrecarga y checksum|03 - Protocolo UDP: datagramas, sobrecarga y checksum]]"
---

# Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)

Para entender TCP, primero hay que entender el problema que resuelve: **proveer transferencia confiable sobre un medio no confiable**. Los protocolos **rdt** (*reliable data transfer*) lo construyen por pasos: cada versión agrega un mecanismo que repara el problema que dejaba la anterior.

> [!tip] Cómo leer las máquinas de estados
> En cada flecha, **sobre la línea** va el evento que la dispara y **bajo la línea** las acciones que se ejecutan. Λ significa "no hacer nada".

## 1.0: canal perfecto

Se asume un canal confiable. El **emisor**, cuando la capa de arriba le pide enviar algo, crea un paquete y lo envía; el **receptor**, al recibir un paquete, extrae el mensaje y lo pasa a la aplicación.

![Protocolo de transferencia confiable rdt 1.0 sobre canal perfectamente confiable](adjuntos/Protocolo%20de%20transferencia%20confiable%20rdt%201.0%20sobre%20canal%20perfectamente%20confiable.png)

> [!example]- Transcripción de la imagen
> **a. rdt1.0: sending side**: un estado *Wait for call from above*; evento `rdt_send(data)`, acciones `packet=make_pkt(data)` y `udt_send(packet)`. **b. rdt1.0: receiving side**: un estado *Wait for call from below*; evento `rdt_rcv(packet)`, acciones `extract(packet,data)` y `deliver_data(data)`.

**Problema:** los paquetes pueden llegar con errores.

## 2.0: checksum, ACK y NAK (protocolo ARQ)

Es un protocolo **ARQ** (*Automatic Repeat reQuest*). Se agrega:

- **detección de errores** con un **checksum**: si un dato llega corrupto, no coincide con su checksum;
- **paquetes de feedback**: **ACK** (*acknowledgment*, "llegó bien") y **NAK** (*negative ACK*, "llegó mal");
- **retransmisión** cuando llega un NAK.

Por ejemplo: el computador le envía una petición HTML al servidor, y el servidor responde con un ACK si llegó bien o con un NAK si llegó mal, y en ese caso el computador la reenvía.

![Protocolo rdt 2.0 con detección de errores mediante checksum y ACKs NACKs](adjuntos/Protocolo%20rdt%202.0%20con%20detecci%C3%B3n%20de%20errores%20mediante%20checksum%20y%20ACKs%20NACKs.png)

> [!example]- Transcripción de la imagen
> **Emisor**: de *Wait for call from above*, con `rdt_send(data)`, hace `sndpkt=make_pkt(data,checksum)`, `udt_send(sndpkt)` y pasa a *Wait for ACK or NAK*. Ahí, si llega un `isNAK` reenvía `sndpkt`; si llega un `isACK` vuelve al estado inicial (Λ). **Receptor**: en *Wait for call from below*, si el paquete está `corrupt` envía un NAK; si está `notcorrupt` lo extrae, lo entrega y envía un ACK.

**Problema:** ¿y si el ACK o el NAK llegan corruptos? Si el emisor retransmite por las dudas, pueden llegar **duplicados**.

## 2.1: número de secuencia

Cada paquete lleva un **número de secuencia** de **1 bit** (0 o 1). Si llega un paquete con el número que no se esperaba, el receptor sabe que es un **duplicado** del anterior: lo descarta y vuelve a confirmar. Basta 1 bit porque el emisor manda un paquete y espera su confirmación antes del siguiente (*stop-and-wait*).

![Protocolo rdt 2.1 con números de secuencia para manejar ACKs corruptos](adjuntos/Protocolo%20rdt%202.1%20con%20n%C3%BAmeros%20de%20secuencia%20para%20manejar%20ACKs%20corruptos.png)

> [!example]- Transcripción de la imagen
> **Emisor** con 4 estados: *Wait for call 0 from above* → (`make_pkt(0,data,checksum)`) → *Wait for ACK or NAK 0* → (ACK no corrupto) → *Wait for call 1 from above* → (`make_pkt(1,data,checksum)`) → *Wait for ACK or NAK 1* → de vuelta al inicio. En los estados de espera, si llega algo corrupto o un NAK, reenvía. **Receptor** con 2 estados, *Wait for 0 from below* y *Wait for 1 from below*: si recibe el número esperado sin errores, entrega y responde ACK; si llega corrupto responde NAK; si llega el número equivocado (duplicado), responde ACK sin entregar.

## 2.2: sin NAK

Si cada **ACK incluye el número de secuencia** del último paquete recibido bien, el NAK sobra: un **ACK duplicado** (con el número del paquete anterior) tiene el mismo efecto. El emisor envía `make_pkt(0, data, checksum)`, y reenvía mientras reciba un ACK corrupto o con el número equivocado. Cuando llega un ACK 0 correcto, cambia de estado.

![Protocolo rdt 2.2 con ACKs duplicados sin NACKs](adjuntos/Protocolo%20rdt%202.2%20con%20ACKs%20duplicados%20sin%20NACKs.png)

> [!example]- Transcripción de la imagen
> **Emisor de rdt2.2**: los mismos 4 estados que 2.1, pero las esperas son *Wait for ACK 0* y *Wait for ACK 1*. En *Wait for ACK 0*, si llega algo corrupto o `isACK(rcvpkt,1)`, reenvía; con `isACK(rcvpkt,0)` no corrupto, pasa a *Wait for call 1 from above*.

![Protocolo rdt 3.0 con temporizador para canales con pérdida de paquetes](adjuntos/Protocolo%20rdt%203.0%20con%20temporizador%20para%20canales%20con%20p%C3%A9rdida%20de%20paquetes.png)

> [!example]- Transcripción de la imagen
> **Receptor de rdt2.2**: estados *Wait for 0 from below* y *Wait for 1 from below*. Con un paquete correcto y `has_seq0`, entrega los datos y envía `make_pkt(ACK,0,checksum)`. Si llega corrupto o con el número equivocado, se queda en el estado y reenvía el último ACK (`make_pkt(ACK,1,checksum)` estando en "0").

**Problema:** ¿y si se **pierden** paquetes?

## 3.0: timeout

El emisor inicia un **temporizador** con cada envío. Si el ACK no llega antes del *timeout*, asume que algo se perdió y **retransmite**, aunque eso pueda generar duplicados (que el número de secuencia ya resuelve). El timeout **se implementa solo en el emisor**.

![Escenarios de operación de rdt 3.0 con pérdida de paquetes y timeouts](adjuntos/Escenarios%20de%20operaci%C3%B3n%20de%20rdt%203.0%20con%20p%C3%A9rdida%20de%20paquetes%20y%20timeouts.png)

> [!example]- Transcripción de la imagen
> **a. Operation with no loss**: pkt0 → ACK0, pkt1 → ACK1, pkt0 → ACK0. **b. Lost packet**: el emisor envía pkt0 y recibe ACK0; envía pkt1, que se pierde (*X loss*); tras el *timeout* reenvía pkt1, el receptor responde ACK1 y el envío continúa con pkt0.

```python
import random

def rdt30(mensajes, p_perdida, semilla=1):
    """Stop-and-wait con bit de secuencia y timeout: reenvía hasta recibir el ACK correcto."""
    rnd = random.Random(semilla)
    seq, esperado, entregados, envios = 0, 0, [], 0
    for m in mensajes:
        while True:
            envios += 1
            if rnd.random() < p_perdida: continue      # se pierde el paquete -> timeout
            if seq == esperado:                         # paquete nuevo: se entrega
                entregados.append(m); esperado ^= 1
            if rnd.random() < p_perdida: continue      # se pierde el ACK -> timeout
            seq ^= 1; break                             # ACK correcto: siguiente
    return "".join(entregados), envios

print(rdt30(list("HOLA MUNDO"), 0.3))   # ('HOLA MUNDO', 27): llega todo, sin duplicados
```

**Funciona, pero el desempeño es malo**: el emisor pasa casi todo el tiempo esperando ACKs. Con 1000 bytes ($L = 8000$ bits) en un enlace de 1 Gbps y un RTT de 30 ms, la utilización es $\frac{L/R}{RTT + L/R} \approx 0{,}00027$. Lo resuelven los [[05 - Protocolos de canalización: Go-Back-N y Selective Repeat|protocolos con pipelining]].

## Preguntas de repaso

> [!question]- ¿Qué problema resuelve cada versión de rdt?
> 2.0 detecta errores con checksum y pide retransmisión con ACK/NAK. 2.1 agrega número de secuencia para reconocer duplicados cuando el feedback llega corrupto. 2.2 elimina el NAK usando ACK con número de secuencia. 3.0 agrega un timeout para recuperarse de paquetes perdidos.

> [!question]- ¿Por qué basta un número de secuencia de 1 bit?
> Porque el emisor envía un paquete y espera su ACK antes del siguiente: solo hay que distinguir el paquete actual del anterior.

> [!question]- ¿Cómo reemplaza un ACK duplicado al NAK en rdt 2.2?
> El receptor confirma siempre el último paquete que recibió bien. Si el emisor recibe un ACK con el número del paquete anterior, sabe que el actual no llegó bien y lo reenvía.

> [!question]- ¿Por qué rdt 3.0 tiene mal desempeño?
> Porque es stop-and-wait: tras cada paquete espera un RTT completo por el ACK. En enlaces rápidos, el tiempo de transmisión es mínimo comparado con el RTT, y la utilización queda cerca de cero.
