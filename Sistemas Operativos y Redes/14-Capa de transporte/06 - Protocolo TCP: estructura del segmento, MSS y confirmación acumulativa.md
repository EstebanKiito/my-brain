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
  - origen/complemento
prerrequisitos:
  - "[[14-Capa de transporte/05 - Protocolos de canalización: Go-Back-N y Selective Repeat|05 - Protocolos de canalización: Go-Back-N y Selective Repeat]]"
---

# Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa

**TCP** (*Transmission Control Protocol*, RFC 793) junta las ideas de [[14-Capa de transporte/04 - Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)|rdt]] y del [[14-Capa de transporte/05 - Protocolos de canalización: Go-Back-N y Selective Repeat|pipelining]] en un protocolo real. Convierte la red no confiable en un flujo de bytes confiable y ordenado entre dos procesos.

## Características

- Transmisión **confiable**.
- Transmisión **encadenada** (*chained*): los segmentos tienen un orden que hay que respetar para reconstruir el mensaje original.
- **Buffer en el emisor y en el receptor**, y **control de flujo** a través del tamaño de la ventana.
- **Orientado a conexión**: antes de enviar datos se establece la conexión con un *handshake* (ver [[07 - Gestión de temporizadores, retransmisión rápida y handshake en TCP|handshake en TCP]]).
- Más overhead que UDP: un header de **20 bytes** como mínimo, frente a 8.

## El segmento TCP

![Estructura y campos del encabezado TCP de 20 bytes](adjuntos/Estructura%20y%20campos%20del%20encabezado%20TCP%20de%2020%20bytes.png)

> [!example]- Transcripción de la imagen
> Formato del segmento TCP en filas de **32 bits**: *Source port #* y *Dest port #*; *Sequence number*; *Acknowledgment number*; *Header length*, *Unused*, los flags *URG, ACK, PSH, RST, SYN, FIN* y *Receive window*; *Internet checksum* y *Urgent data pointer*; luego *Options* (variable) y *Data*.

| Campo | Para qué sirve |
|---|---|
| Puertos de origen y destino | Identificar los procesos |
| Número de secuencia | Posición del primer byte del segmento en el flujo |
| Número de ACK | Próximo byte que se espera recibir |
| Flags (SYN, ACK, FIN, RST…) | Control de la conexión: abrir, confirmar, cerrar |
| Ventana de recepción | Control de flujo: cuánto más puede recibir el receptor |
| Checksum | Detectar errores |

## Bytes, no paquetes: MSS y números de secuencia

El mensaje se divide en segmentos de a lo más **MSS** bytes (*Maximum Segment Size*, tamaño máximo de segmento). A diferencia de rdt, donde el número de secuencia era 0 o 1, en TCP **los números de secuencia cuentan bytes**: el número de secuencia de un segmento es la posición de su primer byte.

![Segmentación de flujo de bytes y número de secuencia en TCP](adjuntos/Segmentaci%C3%B3n%20de%20flujo%20de%20bytes%20y%20n%C3%BAmero%20de%20secuencia%20en%20TCP.png)

> [!example]- Transcripción de la imagen
> Un *File* de bytes numerados de 0 a 499 999. *Data for 1st segment*: bytes 0 a 999. *Data for 2nd segment*: bytes 1000 a 1999. Y así sucesivamente.

El MSS suele ser el MTU del enlace menos 40 bytes de headers (20 de IP y 20 de TCP): en Ethernet, con MTU de 1500 bytes, MSS = 1460. La numeración no parte en 0, sino en un número de secuencia inicial (ISN) que cada extremo elige al abrir la conexión; en los ejemplos se usa 0 para simplificar.

Con un archivo de 500 000 bytes y MSS = 1000, el primer segmento tiene número de secuencia 0, el segundo 1000, el tercero 2000, etc.

## ACK acumulativo y piggybacking

- El ACK lleva el **número de secuencia del siguiente byte que se espera**. Confirma así **todo lo anterior** a la vez: es un **ACK acumulativo** (*cumulative ACK*).
- Un **mensaje de respuesta puede funcionar también como ACK**: es el **piggybacked ACK**. Si hay que enviar datos de vuelta, el ACK viaja en el mismo segmento, sin enviar uno aparte. Es como ir a la cocina y, de paso, llevar la taza que estaba en el camino.

![Piggybacked ACKs y confirmación acumulativa en flujo bidireccional TCP](adjuntos/Piggybacked%20ACKs%20y%20confirmaci%C3%B3n%20acumulativa%20en%20flujo%20bidireccional%20TCP.png)

> [!example]- Transcripción de la imagen
> "Ejemplo: TELNET". El *User types 'C'* en el Host A, que envía `Seq=42, ACK=79, data='C'`. El Host B *ACKs receipt of 'C', echoes back 'C'*: `Seq=79, ACK=43, data='C'`. El Host A *ACKs receipt of echoed 'C'*: `Seq=43, ACK=80`. A mano, círculos rojos sobre `Seq=42` y `ACK=43`.

El servidor responde `ACK = 43` porque recibió el byte 42 (un carácter) y espera el 43. Si en vez de `'C'` se enviaran los 7 bytes de `"iic2333"`, el ACK sería $42 + 7 = 49$. Y en esa misma respuesta, el servidor aprovecha de enviar el eco `'C'` (piggybacking).

```python
def siguiente_ack(seq, datos):
    """ACK acumulativo: número del próximo byte esperado."""
    return seq + len(datos)

print(siguiente_ack(42, "C"))         # 43
print(siguiente_ack(42, "iic2333"))   # 49
print([i * 1000 for i in range(3)])   # números de secuencia con MSS = 1000: [0, 1000, 2000]
```

## Preguntas de repaso

> [!question]- ¿Qué indica el número de secuencia de un segmento TCP?
> La posición, dentro del flujo de bytes, del primer byte de datos del segmento. TCP numera bytes, no paquetes.

> [!question]- ¿Qué significa que el ACK de TCP sea acumulativo?
> Que `ACK = N` dice que llegaron bien todos los bytes hasta el $N - 1$ y que se espera el byte $N$. Un solo ACK confirma todo lo anterior.

> [!question]- Si el cliente envía `Seq=42` con los 7 bytes `"iic2333"`, ¿qué ACK responde el servidor?
> `ACK = 49`: recibió los bytes 42 a 48 y espera el 49.

> [!question]- ¿Qué es un piggybacked ACK y qué ahorra?
> Un ACK que viaja dentro de un segmento que además lleva datos de respuesta. Ahorra enviar un segmento aparte solo para confirmar.
