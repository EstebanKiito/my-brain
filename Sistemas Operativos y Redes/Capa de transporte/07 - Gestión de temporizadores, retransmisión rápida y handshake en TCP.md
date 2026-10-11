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
prerrequisitos:
  - "[[Capa de transporte/06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa|06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa]]"
---

# Gestión de temporizadores, retransmisión rápida y handshake en TCP

El ciclo de vida de una conexión TCP integra tres mecanismos esenciales: el establecimiento ordenado mediante el saludo de tres vías (*three-way handshake*) y su cierre con banderas FIN/RST, la gestión de retransmisiones basada en temporizadores de retransmisión adaptativos (RTO) con avance de ventana `SendBase`, y la optimización de retransmisión rápida (*Fast Retransmit*) gatillada por tres ACKs duplicados sin esperar la expiración del temporizador.

---

## Retransmisión y ciclo de vida de conexión (mis apuntes)

IMPLEMENTACION TCP

![Variables de control SendBase y NextSeqNum en emisor TCP](adjuntos/Variables%20de%20control%20SendBase%20y%20NextSeqNum%20en%20emisor%20TCP.png)

> [!example]- Transcripción de la imagen
> Variables de estado del emisor TCP:
> - `SendBase`: Número del byte más antiguo transmitido y aún no confirmado.
> - `NextSeqNum`: Número del próximo byte a enviar. Los bytes con índice menor a `SendBase` están confirmados; los bytes entre `SendBase` y `NextSeqNum - 1` están en vuelo pendientes de ACK.

SendBase, es la base de la ventana, aqui parte
- se actualiza al crear un segmento nuevo para enviar
Nextseqnum : Nuevo numero de seq a enviar : Lo anterior ya fue enviado (algunos recibieron ACK y otros nop)
- Esto porque el ACK pudo haberse perdido o el paquete enviado tmbn
Al Expirar el TIMER → Se RETRASNMITE segmento con MENOR SEQ NUMBER → (funciona como selected-repeat al no retrasnmitir todo)
- → Dado que se recibieron paquetes con valor menor a SendBase
- → Como usamos el concepto de CUMULATIVE ACK, significa que si recibo por ejemplo el tercer ACK desde sendbase en adelante, significa que ya recibi los ANTERIORES!!!
por eso actualizo SendBase
- Si llega un ACK con valor ACK ≥ SendBase → Se actualiza SendBase

CASOS
- ACK PERDIDO → Si el ack se pierde,
- Reinicia timer y
- reenvia paquete mas antiguo!
- B recibira el paquete repetido, pero lo descartamos, reenviando ACK
- se produce Timeout →

![Manejo de timeout y retransmisión por pérdida de ACK en TCP](adjuntos/Manejo%20de%20timeout%20y%20retransmisión%20por%20pérdida%20de%20ACK%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> Pérdida de ACK: Host A envía `Seq=92, 8 bytes`. Host B responde `ACK=100`, pero se pierde en tránsito. Expira el timer en A $\to$ A retransmite `Seq=92` $\to$ B descarta el duplicado y reenvía `ACK=100`.

- A reenviara el paquete mas antiguo, y reinicia su timer
- A recibe el ACK y reinicia el timer del sgte mensaje
- A No reenvia el siguiente mensaje ya que su ACK llega antes del timeout
- B recibe el mensaje inicial dubplicado, lo descarta, pero envia CUMULATIVE ACK
- TIMEOUT PREMATURO → Si ocurre timeout antes que llegue el ACK, no importa

![Escenario de timeout prematuro y confirmación acumulativa en TCP](adjuntos/Escenario%20de%20timeout%20prematuro%20y%20confirmación%20acumulativa%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> Timeout prematuro y ACKs acumulativos: A envía segmentos con `Seq=92` y `Seq=100`. Si el timer de 92 expira antes de llegar los ACKs, A retransmite 92. Al llegar `ACK=120`, confirma ambos segmentos acumulativamente y evita retransmitir 100.

- CUMULATIVE ACK → Evita retransmision (porque pesca todos los anteriores que perdieron ACK si recibe un ACK mas grande!)
- Fijate que llega el 120 y listo, es como que hubiera llegado el 100 cuando no llego (se perdio)
- A no reenvia seq=92
- A Incrementa SendBase
- Cuando me llega el 120 → CORTO EL TIMER!!! → Recibi todos los paquetes anteriores correctamente

![Cancelación de temporizador y avance de SendBase en TCP](adjuntos/Cancelación%20de%20temporizador%20y%20avance%20de%20SendBase%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> Cancelación y actualización de timer: A envía `Seq=92` y `Seq=100`. El `ACK=100` se pierde, pero el `ACK=120` llega antes del timeout de 92; como `ACK=120` supera la base, A avanza `SendBase` a 120 y reinicia el timer para los bytes restantes.

- Envia proactivamente segmentos perdidos, antes que ocurra un timeout
- LA vuelta final despues de todo
- Responde con ACK = 157
- RETRANSMISION RAPIDA → Asi es como funciona TCP basicamente

![Mecanismo de retransmisión rápida con tres ACKs duplicados en TCP](adjuntos/Mecanismo%20de%20retransmisión%20rápida%20con%20tres%20ACKs%20duplicados%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> Retransmisión Rápida (*Fast Retransmit*): Si un emisor recibe tres ACKs duplicados (4 ACKs idénticos en total con el mismo valor), asume que el segmento siguiente se perdió y lo retransmite inmediatamente sin esperar a que expire el temporizador.

TCP HANDSHAKE
Establecimiento de Conexion de 3 pasos
- Incluye numero sequencia incial (del CLIENTE)
- Cliente envia segmento con el flag → SYN:
- Servidor asigna Buffer
- Servidor Establece numero sec inicial (Del SERVIDOR)
- Servidor Recibe SYN, y responde con SYN y ACK
- Este paquete enviado → YA PUEDE ENVIAR DATOS
- Cliente Recibe SYN Y ACK y responde con ACK

![Establecimiento de conexión TCP con saludo de tres vías y terminación con FIN](adjuntos/Establecimiento%20de%20conexión%20TCP%20con%20saludo%20de%20tres%20vías%20y%20terminación%20con%20FIN.png)

> [!example]- Transcripción de la imagen
> Three-Way Handshake y Cierre de conexión TCP:
> 1. Paso 1 (Cliente $\to$ Servidor): `SYN=1, Seq=client_isn`.
> 2. Paso 2 (Servidor $\to$ Cliente): `SYN=1, ACK=1, Seq=server_isn, Ack=client_isn + 1`.
> 3. Paso 3 (Cliente $\to$ Servidor): `ACK=1, Seq=client_isn + 1, Ack=server_isn + 1` (puede transportar datos).
> Cierre: Cada extremo envía `FIN=1` y espera su `ACK`. El iniciador entra en estado `TIME_WAIT` durante $2 \times \text{MSL}$ para asegurar que el último ACK no se pierda.

A la derecha se encuentra el termino de conexion → Cerrar buffer → Cerrar conexion

---

## Preguntas de repaso

> [!question]- ¿Por qué tres ACKs duplicados disparan la retransmisión rápida en TCP en vez de retransmitir con el primer ACK duplicado?
> Porque los paquetes en Internet pueden reordenarse en la red sin haberse perdido; recibir uno o dos ACKs duplicados puede deberse solo a un desfase de llegada, mientras que tres ACKs duplicados constituyen evidencia estadística contundente de pérdida.

> [!question]- ¿Por qué TCP utiliza un saludo de tres vías en vez de dos vías (*Two-Way Handshake*)?
> Para sincronizar bidireccionalmente los números de secuencia iniciales (ISN) y prevenir que segmentos retrasados o duplicados de conexiones viejas sean aceptados por error como válidos en una nueva sesión.

> [!question]- ¿Cuál es el propósito del estado `TIME_WAIT` al cerrar una conexión TCP?
> Garantiza que el último ACK enviado por el cliente llegue al servidor (si se pierde, el servidor retransmitirá el FIN y el cliente en TIME_WAIT podrá reenviar el ACK) y permite que los paquetes rezagados en la red expiren antes de reutilizar el mismo puerto.

