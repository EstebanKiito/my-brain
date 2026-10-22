---
ramo: "Programación Avanzada"
tema: "Serialización y networking I"
tags:
  - programacion/networking
  - programacion/redes
  - origen/complemento
prerrequisitos:
  - "[[02 - Fundamentos de redes: arquitectura cliente-servidor, sockets y puertos]]"
---

# Modelo de capas y protocolos de transporte: TCP frente a UDP

Enviar un mensaje a través del mundo exige resolver problemas enormemente diversos: desde cómo modular señales eléctricas o pulsos de luz en un cable de fibra óptica, hasta cómo enrutar paquetes entre continentes y cómo garantizar que no se pierdan datos. Para abordar esta complejidad, las redes dividen sus funciones en capas estandarizadas.

## El modelo de capas y el encapsulamiento

Tanto el modelo teórico **OSI** (7 capas) como el modelo práctico de Internet **TCP/IP** (4 capas) aplican el principio de abstracción: cada nivel resuelve una responsabilidad específica y ofrece una interfaz limpia a la capa superior:

![Modelo de capas OSI](adjuntos/Modelo%20de%20capas%20OSI%20y%20encapsulamiento%20de%20datos.png)

> [!example]- Transcripción de la imagen
> - Diagrama de capas y encapsulamiento:
>   - Capa de Aplicación: datos originales del software.
>   - Capa de Transporte: añade cabecera con puertos origen y destino (segmento).
>   - Capa de Red: añade cabecera con direcciones IP (paquete).
>   - Capa de Enlace y Física: añade direcciones MAC y trama binaria transmitida por el medio físico.

Al descender por la pila, cada nivel envuelve los datos del nivel superior agregando sus propios metadatos de control en un encabezado (*header*), proceso conocido como **encapsulamiento** (*encapsulation*). Al llegar al destino, ocurre el proceso inverso de **desencapsulamiento**.

## Protocolos de la capa de transporte: TCP vs UDP

En la capa de transporte, las aplicaciones deben elegir entre dos filosofías de comunicación fundamentales según sus prioridades de confiabilidad o velocidad:

```
+--------------------+---------------------------------+---------------------------------+
| Característica     | TCP (Transmission Control)      | UDP (User Datagram Protocol)    |
+--------------------+---------------------------------+---------------------------------+
| Conexión           | Orientado a conexión (Handshake)| Sin conexión previa             |
| Confiabilidad      | Garantizada (retransmite datos) | No confiable (mejor esfuerzo)   |
| Orden de entrega   | Estrictamente secuencial        | Puede llegar desordenado        |
| Sobrecarga         | Mayor latencia y cabeceras      | Mínima sobrecarga y ultrarrápido|
| Control de flujo   | Sí (evita saturar al receptor)  | No                              |
| Casos de uso       | Web (HTTP), correos, archivos   | Streaming en vivo, juegos, DNS  |
+--------------------+---------------------------------+---------------------------------+
```

### 1. TCP: Confiabilidad y orden estricto
Antes de transmitir cualquier byte, TCP establece una sesión mediante un saludo de tres vías (**three-way handshake**: SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK). Durante la transmisión, el receptor envía confirmaciones (**ACK**) por cada bloque recibido. Si un paquete se pierde en la red, el emisor lo detecta y **lo retransmite automáticamente**. Además, numera cada segmento para reconstruir el mensaje en el orden exacto.

### 2. UDP: Velocidad y mínima latencia
UDP envía datagramas individuales como cartas en el buzón: no establece conexión previa ni espera confirmaciones. Si un paquete se descarta por congestión en un router intermedio, el dato se pierde para siempre. Esta ausencia de controles hace que sea inmediato y perfecto para escenarios donde la frescura del dato supera a la integridad perfecta: en una videollamada o juego en línea, un fotograma o posición retrasada de hace un segundo es inútil y descartable.

> [!tip] Regla de selección rápida
> Si no toleras perder un solo byte de información (archivos de texto, finanzas, HTML) $\rightarrow$ usa **TCP**. Si la inmediatez y la baja latencia son vitales y perder algún paquete no arruina el servicio (audio/video en vivo, sensores rápidos) $\rightarrow$ usa **UDP**.

## Preguntas de repaso

> [!question]- ¿En qué consiste el principio de encapsulamiento en las redes de computadores?
> En que cada capa de la pila de red toma el bloque de datos de la capa superior y le antepone su propio encabezado (*header*) con información de control (puertos, IPs, checksums) antes de pasarlo a la capa inferior.

> [!question]- ¿Cómo garantiza TCP que ningún dato transmitido se pierda en el camino?
> Exige que el receptor envíe un mensaje de confirmación (*ACK*) por cada paquete recibido; si el emisor no recibe el ACK tras un temporizador de espera, retransmite el paquete faltante.

> [!question]- ¿Por qué una transmisión de video en vivo prefiere utilizar UDP sobre TCP?
> Porque retransmitir paquetes perdidos en TCP introduce pausas y latencia acumulada; en un streaming en vivo es preferible perder un cuadro de imagen microscópico antes que congelar la transmisión entera.

> [!question]- ¿Qué ocurre durante el saludo de tres vías (*three-way handshake*) de TCP?
> El cliente envía un paquete `SYN`, el servidor responde confirmando con `SYN-ACK`, y el cliente finaliza con un `ACK`, acordando números de secuencia iniciales antes de enviar datos reales.

