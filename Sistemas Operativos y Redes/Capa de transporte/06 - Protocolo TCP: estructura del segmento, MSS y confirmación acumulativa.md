---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - tcp
  - mss
  - cumulative-ack
  - piggybacking
prerrequisitos:
  - "[[Capa de transporte/05 - Protocolos de canalización: Go-Back-N y Selective Repeat|05 - Protocolos de canalización: Go-Back-N y Selective Repeat]]"
---

# Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa

El Protocolo de Control de Transmisión (TCP, *Transmission Control Protocol*, RFC 793) es el protocolo de transporte orientado a conexión predominante en Internet. Transforma el canal no confiable de la capa de red en un flujo de bytes continuo, bidireccional (*full-duplex*) y confiable. A diferencia de los modelos teóricos que cuentan paquetes, TCP numera cada byte individual del flujo de datos, gestionando la segmentación según el Tamaño Máximo de Segmento (*Maximum Segment Size*, MSS).

---

## Segmentos y números de secuencia en TCP (mis apuntes)

### CLASE 5
21/10/24

PROTOCOLO TCP
- Protocolo de transmisión CONFIABLE
- Encadenada → Secuencia de PAquetes → Hay un orden en que deben guardarse, para mantener el mensaje original enviado
- Hay un buffer en emisor y Receptor
- Orientado a CONEXION → HANDSHAKE → (Establencimiento de conexion antes de envio de pktes)
- Posee un overhead mayor a UDP (8): Posee 20 Bits

![Estructura y campos del encabezado TCP de 20 bytes](adjuntos/Estructura%20y%20campos%20del%20encabezado%20TCP%20de%2020%20bytes.png)

> [!example]- Transcripción de la imagen
> Encabezado TCP (20 bytes base):
> - Puertos origen y destino (16 bits cada uno).
> - Número de secuencia (*Sequence Number*, 32 bits): Número del primer byte de datos del segmento.
> - Número de confirmación (*Acknowledgment Number*, 32 bits): Próximo byte esperado del otro extremo.
> - Longitud de encabezado (*Data Offset*, 4 bits) y campos reservados (6 bits).
> - Flags de control (6 bits): URG, ACK, PSH, RST, SYN, FIN.
> - Ventana de recepción (*Receive Window*, 16 bits): Control de flujo.
> - Checksum de Internet (16 bits) y Puntero urgente (16 bits).

Funciona con NUMERO DE SEQUENCIA → No como vimos anteriormente que aumenta de a 1 bit, si no que aumenta segun cantidad de bytes enviados
El mensaje original se divide en varios segmentos:
- MSS : Tamaño maximo de Segmento
- Num Seq: Ademas cuentan con bytes en la seq

![Segmentación de flujo de bytes y número de secuencia en TCP](adjuntos/Segmentación%20de%20flujo%20de%20bytes%20y%20número%20de%20secuencia%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> Segmentación y numeración de bytes en TCP: Si un flujo de 500.000 bytes se divide en segmentos con MSS = 1.000 bytes, el segmento 0 tendrá `Seq = 0`, el segmento 1 tendrá `Seq = 1000`, el segmento 2 tendrá `Seq = 2000`, etc.

- ACK contiene el sequence number del siguiente byte que se espera → Cumulative ACK
- → Piggybacked ACK: Es como cuando vas a la cocina y hay una taza en el camino, aprovecha de llevarla → OPTIMIZACION
- Mensaje de respuesta funciona tambien como ACK

![Piggybacked ACKs y confirmación acumulativa en flujo bidireccional TCP](adjuntos/Piggybacked%20ACKs%20y%20confirmación%20acumulativa%20en%20flujo%20bidireccional%20TCP.png)

> [!example]- Transcripción de la imagen
> Confirmación acoplada (*Piggybacking*): En una sesión interactiva Telnet, el cliente envía `Seq=42, ACK=79, data='C'`. El servidor responde enviando `Seq=79, ACK=43, data='C'`, confirmando el byte 42 (`ACK=43`) y devolviendo el eco en el mismo segmento de transporte.

- En el ejemplo, viene un byte, con ‘c’, si la data fuera por ejemplo ‘iic2333’ serian 7 bites, por lo que el ack = 43 → Pasaria a enviarse como ACK = 49

> [!warning] Posible error en apuntes: 20 bits vs 20 bytes y 7 bites vs 7 bytes
> En los apuntes dice "Posee 20 Bits": el encabezado base de TCP mide **20 bytes** (160 bits), frente a los 8 bytes de UDP. Asimismo, cuando se menciona que 'iic2333' son 7 "bites", son **7 bytes** (caracteres ASCII).

---

## Preguntas de repaso

> [!question]- ¿Qué representa exactamente el campo *Sequence Number* en un segmento TCP?
> Representa el índice numérico del primer byte de datos contenido en ese segmento dentro del flujo total de bytes de la conexión (establecido a partir del número de secuencia inicial ISN acordado en el handshake).

> [!question]- ¿Por qué la confirmación en TCP se denomina acumulativa (*Cumulative ACK*)?
> Porque cuando un receptor envía `ACK = N`, confirma implícitamente que ha recibido correctamente y en orden todos los bytes previos hasta el byte $N-1$, solicitando el byte $N$ a continuación.

> [!question]- ¿Qué es el MSS (*Maximum Segment Size*) y cómo se determina?
> Es la cantidad máxima de datos de aplicación (excluyendo cabeceras) que un host puede empaquetar en un segmento TCP. Típicamente se calcula restando 40 bytes (20 de IP + 20 de TCP) al MTU del enlace físico (ej. MTU Ethernet de 1500 bytes $\to$ $\text{MSS} = 1460$ bytes).

