---
ramo: "Arquitectura de Sistemas de Software"
tema: "Caché y protocolos web"
tags:
  - arquisis/performance
  - arquisis/red
  - origen/complemento
prerrequisitos:
  - "[[02 - Caché web navegador proxy CDN y proxy inverso]]"
  - "[[03 - Protocolos de transporte TCP y UDP]]"
---

# Evolución de HTTP 1 a HTTP 3

El protocolo también es parte del stack que afecta la performance. Una página moderna pide decenas de recursos (HTML, CSS, JS, imágenes), y la forma en que HTTP maneja esas peticiones sobre la red determina cuánto espera el usuario. Cada versión de HTTP resolvió un cuello de botella de la anterior.

## HTTP/1.0 y HTTP/1.1

- **HTTP/1.0:** ¡**una petición por conexión TCP**! Cada recurso paga el costo de abrir una conexión (y, con HTTPS, el handshake TLS).
- **HTTP/1.0 con `Connection: keep-alive`:** varias peticiones, una después de otra, sobre la misma conexión. Minimiza el costo de abrir conexiones, pero es **bloqueante**: solo hay una petición pendiente a la vez.
- **HTTP/1.1 con *pipelining*:** se pueden enviar varias peticiones seguidas, pero las respuestas siguen llegando **en orden (FIFO)**. Si la primera es lenta, bloquea a todas las demás. Es el **head-of-line (HOL) blocking**, y por eso el pipelining está desactivado por defecto.
- **Parche de los navegadores:** abrir **4 a 8 conexiones** en paralelo por dominio.

## HTTP/2

Viene de SPDY, de Google (RFC 9113). Mejora sustancialmente a HTTP/1.1:
- **Protocolo binario**, más eficiente de procesar que el texto.
- **Una sola conexión multiplexada**: varias peticiones **priorizadas**, **fuera de orden** y **entrelazadas** en la misma conexión.
- **Compresión de headers** (HPACK): los headers repetidos (cookies, user-agent) no viajan completos cada vez.
- **Server push**: el servidor envía recursos que sabe que el cliente pedirá (llenado preventivo). En la práctica, los navegadores lo deshabilitaron después.

![Diagrama de una conexión HTTP/2 con peticiones y respuestas entrelazadas](adjuntos/Conexión%20multiplexada%20de%20HTTP%202.png)

> [!example]- Transcripción de la imagen
> - (1) El cliente abre **una** conexión con el servidor. (2) Envía `GET /index.html` y (3) recibe la respuesta.
> - (4) Envía `GET /styles.css` y `GET /scripts.js` casi al mismo tiempo.
> - (5) Las dos respuestas vuelven entrelazadas por la misma conexión. (6) El cliente renderiza la página.
> - (7) La conexión queda abierta para peticiones futuras.

## HTTP/3

Basado en **QUIC** (*Quick UDP Internet Connections*), RFC 9114. Corre sobre **UDP** en vez de TCP:
- **Multiplexado avanzado:** en HTTP/2, una pérdida de paquete TCP detiene **todos** los streams (HOL a nivel de transporte). En QUIC cada stream es independiente.
- **Cifrado obligatorio y prenegociado:** TLS 1.3 integrado, con menos viajes para establecer la conexión (0-RTT si ya se habló antes con el servidor).
- **Mejor recuperación de errores** y migración de conexión (cambiar de wifi a datos sin reconectar).

![Comparación de handshakes HTTPS sobre TCP y sobre QUIC y throughput de una CDN al activar QUIC](adjuntos/Ganancias%20de%20HTTP%203%20sobre%20QUIC.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, dos diagramas de secuencia. **HTTPS over TCP + TLS** necesita varios viajes de ida y vuelta antes de enviar datos: 200 ms en una conexión repetida y 300 ms la primera vez. **HTTPS over QUIC** necesita 0 ms en una conexión repetida y 100 ms la primera vez.
> - A la derecha, *Cloud CDN throughput (50th percentile)* de noviembre de 2017 a febrero de 2018: el throughput sube de unos 6.000-7.000 kbps a más de 8.000 kbps desde el punto marcado "QUIC enabled".

| | HTTP/1.1 | HTTP/2 | HTTP/3 |
|---|---|---|---|
| Transporte | TCP | TCP | **UDP (QUIC)** |
| Formato | Texto | Binario | Binario |
| Peticiones por conexión | Una a la vez (o pipelining en orden) | Multiplexadas | Multiplexadas e independientes |
| HOL blocking | En HTTP y en TCP | Solo en TCP | No |
| Headers | Repetidos completos | Comprimidos (HPACK) | Comprimidos (QPACK) |
| Cifrado | Opcional (TLS aparte) | En la práctica obligatorio | Obligatorio, integrado |

> [!warning] gRPC depende de HTTP/2
> gRPC usa la multiplexación y el streaming de HTTP/2. Por eso no funciona directo desde el navegador y necesita gRPC-Web o Connect.

## Preguntas de repaso

> [!question]- ¿Qué problema tenía HTTP/1.0 y cómo lo mitigó keep-alive?
> Abría una conexión TCP por cada petición, así que cada recurso pagaba el handshake. Keep-alive reutiliza la conexión para varias peticiones seguidas, aunque solo una puede estar pendiente a la vez.

> [!question]- ¿Qué es el head-of-line blocking en el pipelining de HTTP/1.1?
> Las respuestas deben llegar en el mismo orden en que se enviaron las peticiones. Si la primera respuesta es lenta, todas las siguientes esperan detrás aunque ya estén listas.

> [!question]- Nombre cuatro mejoras de HTTP/2 sobre HTTP/1.1.
> Protocolo binario, multiplexación de varias peticiones en una sola conexión (priorizadas y fuera de orden), compresión de headers y server push.

> [!question]- Si HTTP/2 ya multiplexa, ¿qué HOL blocking queda que HTTP/3 elimina?
> El de TCP: como todos los streams comparten una conexión TCP, un paquete perdido detiene la entrega de todos hasta que se retransmite. QUIC sobre UDP maneja cada stream de forma independiente, así que una pérdida solo afecta a su stream.

> [!question]- ¿Por qué los navegadores abrían 4 a 8 conexiones por dominio con HTTP/1.1 y por qué con HTTP/2 ya no hace falta?
> Con HTTP/1.1, cada conexión atendía una petición a la vez, así que se abrían varias para paralelizar. HTTP/2 multiplexa muchas peticiones en una sola conexión, lo que hace innecesarias las conexiones extra (y su costo de handshake).

> [!question]- Según la comparación de handshakes, ¿cuánto tarda establecer HTTPS sobre TCP frente a QUIC en una conexión repetida?
> Sobre TCP + TLS, unos 200 ms antes de enviar datos. Sobre QUIC, 0 ms, porque puede reanudar con 0-RTT. En la primera conexión, unos 300 ms frente a unos 100 ms.

> [!question]- V o F: "HTTP/3 usa TCP con un cifrado más rápido".
> Falso. HTTP/3 usa QUIC sobre UDP, con TLS 1.3 integrado en el propio protocolo de transporte.
