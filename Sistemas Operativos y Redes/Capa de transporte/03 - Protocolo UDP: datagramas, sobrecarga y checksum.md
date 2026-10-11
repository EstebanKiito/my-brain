---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de transporte"
tags:
  - sistemas-operativos
  - redes
  - udp
  - datagramas
  - checksum
prerrequisitos:
  - "[[Capa de transporte/02 - Multiplexación y desmultiplexación de puertos en UDP y TCP|02 - Multiplexación y desmultiplexación de puertos en UDP y TCP]]"
---

# Protocolo UDP: datagramas, sobrecarga y checksum

El Protocolo de Datagramas de Usuario (UDP, *User Datagram Protocol*, RFC 768) es un protocolo de transporte mínimo sin conexión. Proporciona una interfaz directa y sin garantías sobre el protocolo IP ("mejor esfuerzo"), sin establecimiento previo de conexión ni control de congestión, ofreciendo una cabecera extremadamente liviana de solo 8 bytes.

---

## Características y estructura de UDP (mis apuntes)

UDP
- Servicio de "mejor esfuerzo" (best-effort).
- Segmentos pueden perderse.
- Segmentos pueden llegar en distinto orden.
- Servicio no orientado a conexión (connection-less)
- No se establece conexión previa
- SIN estado de conexión
- Cada segmento se gestiona de manera independiente

![Proceso de multiplexación y desmultiplexación de segmentos mediante puertos](adjuntos/Proceso%20de%20multiplexación%20y%20desmultiplexación%20de%20segmentos%20mediante%20puertos.png)

> [!example]- Transcripción de la imagen
> Gestión independiente de datagramas UDP: Cada datagrama contiene su propia cabecera con puertos origen y destino, entregándose de forma autónoma sin estado de conexión ni sincronización previa.

- Segmento UDP solo tiene 8 byte de overhead
Para identificar necesitamos una Ip, pero esta se maneja de una capa anterior (Red)
Cheksum → Para ver simplemente si el mensaje llego correcto, en UDP → Si el cheksum no coincide se ignora

¿Porque UDP? → VENTAJAS UDP
- Capa Aplicación puede controlar el envío
- Menor Overhead de tiempo
- No hay demora en establecer conexión
- Menor overhead: 8 bytes → TCP USA 20bytes !!

> [!tip] Complemento de clase: Los 4 campos de la cabecera UDP (8 bytes)
> La cabecera UDP consta de exactamente cuatro campos de 16 bits (2 bytes cada uno, totalizando 8 bytes):
> 1. **Puerto de origen** (16 bits)
> 2. **Puerto de destino** (16 bits)
> 3. **Longitud** (16 bits, indica el tamaño total en bytes del segmento UDP, cabecera + datos)
> 4. **Checksum / Suma de verificación** (16 bits, detección de errores por complemento a 1)

> [!tip] Complemento de clase: Cálculo del Checksum UDP
> El checksum de Internet trata el segmento UDP (junto a una pseudo-cabecera IP con IPs y protocolo) como una secuencia de enteros de 16 bits. Se suman todos los enteros de 16 bits; los acarreos se suman al final (aritmética complemento a 1) y se invierten todos los bits. En el receptor, si la suma de todos los campos incluyendo el checksum da $1111111111111111_2$, el paquete no tiene errores detectados.

---

## Preguntas de repaso

> [!question]- ¿Por qué aplicaciones como DNS o streaming de audio/video prefieren UDP en lugar de TCP?
> Porque priorizan la baja latencia y el control directo de la tasa de transmisión: no sufren el retardo de establecimiento de conexión (RTT adicional) ni pausas por retransmisiones automáticas que perjudicarían la experiencia en tiempo real.

> [!question]- ¿Qué hace el receptor UDP si la suma de comprobación (*checksum*) falla?
> Descarta silenciosamente el datagrama dañado (o lo entrega a la aplicación con una advertencia de error si el socket lo configuró), pero nunca solicita una retransmisión por sí mismo.

> [!question]- ¿Es posible lograr transferencia confiable utilizando UDP como protocolo de transporte?
> Sí; la confiabilidad debe implementarse en la propia capa de aplicación (como hace HTTP/3 sobre QUIC), agregando números de secuencia, confirmaciones y temporizadores en espacio de usuario.

