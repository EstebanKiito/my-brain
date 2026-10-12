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
prerrequisitos:
  - "[[Capa de transporte/03 - Protocolo UDP: datagramas, sobrecarga y checksum|03 - Protocolo UDP: datagramas, sobrecarga y checksum]]"
---

# Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)

Construir un canal de transferencia confiable sobre una red subyacente que pierde, corrompe y desordena paquetes es uno de los problemas fundacionales de redes. Mediante una serie evolutiva de protocolos (*Reliable Data Transfer*, rdt 1.0 a 3.0), se incorporan gradualmente mecanismos de detección de errores (checksums), confirmaciones positivas/negativas (ACK/NAK), números de secuencia y temporizadores de retransmisión (*timers*).

---

## Evolución de rdt (mis apuntes)

→ Para entender protocolo TCP, estudiaremos primero PRINCIPIOS de TRANSMISION CONFIABLE
- desafio: Proveer transferencia confiable sobre un MEDIO NO CONFIABLE

Transmisión Confiable
- El Emisor cuando la capa superior le pide enviar algo, crea un paquete y lo envia
- El receptor, recibe un paquete, extrae el mensaje y lo pasa a la aplicacion
- Problema: Paquetes pueden llegar con errores
- La comunicacion mas sencilla es:
- Version 1.0 : Emisor y Receptor de mensajes

![Protocolo de transferencia confiable rdt 1.0 sobre canal perfectamente confiable](adjuntos/Protocolo%20de%20transferencia%20confiable%20rdt%201.0%20sobre%20canal%20perfectamente%20confiable.png)

> [!example]- Transcripción de la imagen
> rdt 1.0: Máquinas de estados finitos (FSM) para canal perfectamente confiable:
> - Emisor: Espera llamada de capa superior $\to$ `rdt_send(data)` $\to$ crea paquete `make_pkt(data)` $\to$ `udt_send(packet)`.
> - Receptor: Espera llamada de capa inferior $\to$ `rdt_rcv(packet)` $\to$ extrae datos `extract(packet, data)` $\to$ entrega `deliver_data(data)`.

- Nota: Para leer la maquina de estados arriba del guion esta el evento que se pide, abajo de la barrita horizontal son las acciones que ocurren → En el caso uno, si no piden un send de data, se ejecuta crear el paquete, y mandarlo

CHEKSUMS (ACK)
- Version 2.0 : Junto con el envio del paquete, agregamos una SUMA (Cheksum), si un dato llego corrupto, no va a coincidir con su cheksum
- ACK y NAK (usa cheksums) → Comprobar si la informacion llego bien o es la esperada
- ACK: Acnolagment: Decirle al emisor que llego el mensaje

![Protocolo rdt 2.0 con detección de errores mediante checksum y ACKs NACKs](adjuntos/Protocolo%20rdt%202.0%20con%20detección%20de%20errores%20mediante%20checksum%20y%20ACKs%20NACKs.png)

> [!example]- Transcripción de la imagen
> rdt 2.0 (Canal con errores de bits): Introduce `checksum`, confirmación positiva (`ACK`) y negativa (`NAK`). Si el receptor recibe un paquete corrupto, responde `NAK` y el emisor retransmite (paradigma Stop-and-Wait / ARQ).

Problema → Si llega el ACK o NAK corrupto?
- Retransmitir al recibir un ACK o NAK corrupto → Pueden llegar duplicados. → corregido: 2.1

Ejemplo Visual
Computador —— HTML ——> Serv: Le envio una peticion html
Computador ←—- ACK ——— Serv : Le devuelvo una Ack que me llego bien (Nack seria si no llego bien) → Ahi se entra en el loop visto en la diapositiva
- El recibidor: espera un ACK y ademas un numero de secuencia, para corroborar bien si llego
- Si me llega mal, llega un nack, con el id indicado (secuencia)

![Protocolo rdt 2.1 con números de secuencia para manejar ACKs corruptos](adjuntos/Protocolo%20rdt%202.1%20con%20números%20de%20secuencia%20para%20manejar%20ACKs%20corruptos.png)

> [!example]- Transcripción de la imagen
> rdt 2.1: Agrega número de secuencia de 1 bit (0 o 1) a cada paquete. Si un ACK/NAK se corrompe, el emisor retransmite y el receptor detecta si el paquete es duplicado inspeccionando el bit de secuencia.

- Version 2.1 : Ahora los envios de mensajes son con un NUMERO DE SEQUENCIA (identificador),
- Si nos llega un ACK, con un numero de sequencia incorrecto: identificamos un DUPLICADO de un mensaje anterior

MEJORA → ENVIAR NAK se vuelve innecesario:
- Version 2.2 :
Si el paquete llega corrupto, lo sabré → No necesito una confirmacion negativa!
El emisor:
- Le piden enviar un paquete → sndpkt(0, data, cheksum) → El 0 es el numero de seq
- Reenvio paquetes cuando esta corrupto o el Ack con el numero 1, (asi lo identificamos como fallido)

![Protocolo rdt 2.2 con ACKs duplicados sin NACKs](adjuntos/Protocolo%20rdt%202.2%20con%20ACKs%20duplicados%20sin%20NACKs.png)

> [!example]- Transcripción de la imagen
> rdt 2.2 (Protocolo sin NAK): En lugar de enviar un NAK ante un error, el receptor envía un ACK explícito del último paquete correcto recibido. Un ACK duplicado produce el mismo efecto que un NAK en el emisor.

- Reenvio hasta rebir un paquete no corrupto y con Ack 0 → En ese momento cambio de estado
El receptor:
- Lo mismo, si llega corrupto o tiene numero de sequencia no correcto → Se mantiene en estado
- Y si recibe un paquete no corrupto, y con sequencia 0, lo extrae y lo envia a la capa superior

![Protocolo rdt 3.0 con temporizador para canales con pérdida de paquetes](adjuntos/Protocolo%20rdt%203.0%20con%20temporizador%20para%20canales%20con%20pérdida%20de%20paquetes.png)

> [!example]- Transcripción de la imagen
> rdt 3.0 (Canal con errores y pérdida de paquetes): El emisor inicia un temporizador de cuenta regresiva (*countdown timer*) tras cada envío. Si no recibe el ACK antes de expirar el timeout, retransmite el paquete.

- Version 3.0: En el sender se implementa un TimeOut → Solo en el sender
- Asumo con esto, que algo se perdio, con eso reenvio el paquete, sin importar que lleguen 2, esperando a que me llegue el ACK para poder avanzar

RESUMEN
- Versión 1. Tiene los supuestos, pero los paquetes pueden llegar con errores
- Versión 2. Implementa los checksums, pero pueden haber paquetes de feedback duplicados(ACK O NAK).
- Versión 2.1. Agrega un bit que es el sequence number.
- Versión 2.2. Se pueden eliminar los NAK.
- Versión 3.0. Funciona pero el desempeño es malo

FUNCIONAMIENTOS SIN PERDIDA Y CON PERDIDA

![Escenarios de operación de rdt 3.0 con pérdida de paquetes y timeouts](adjuntos/Escenarios%20de%20operación%20de%20rdt%203.0%20con%20pérdida%20de%20paquetes%20y%20timeouts.png)

> [!example]- Transcripción de la imagen
> Escenarios de rdt 3.0: operación normal sin pérdidas, pérdida de paquete de datos (disparo de timeout y retransmisión), pérdida de ACK (retransmisión y descarte de duplicado en receptor), y timeout prematuro con ACK retrasado.

- En esta version se ve mejor que procede

---

## Preguntas de repaso

> [!question]- ¿Por qué rdt 2.0 falla ante la corrupción de un paquete de confirmación (ACK o NAK)?
> Porque si el ACK o NAK se corrompe en tránsito, el emisor no puede saber si el receptor recibió bien o mal el paquete; si retransmite a ciegas sin números de secuencia, el receptor no distingue si los datos entrantes son nuevos o un duplicado.

> [!question]- ¿Por qué un número de secuencia de solo 1 bit (0 y 1) es suficiente en rdt 2.1 y rdt 3.0?
> Porque operan bajo el modelo *Stop-and-Wait*: el emisor envía un único paquete y espera su confirmación antes de enviar el siguiente, por lo que solo se necesita diferenciar el paquete actual del inmediatamente anterior.

> [!question]- ¿Cuál es la principal limitación de desempeño de rdt 3.0 en enlaces de alta velocidad?
> Su pobre utilización de canal: al esperar un RTT completo entre cada paquete transmitido, la fracción de tiempo en que el emisor realmente inyecta bits al enlace es diminuta ($U = \frac{L/R}{\text{RTT} + L/R}$).

