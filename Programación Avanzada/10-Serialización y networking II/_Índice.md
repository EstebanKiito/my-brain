# Serialización y networking II — índice

Conceptos y herramientas avanzadas para la persistencia binaria y la comunicación de bajo nivel en red utilizando sockets en Python: serialización nativa con `pickle` y sus vulnerabilidades críticas de ejecución de código, tipos binarios `bytes` y `bytearray`, codificación UTF-8 y ordenamiento de bytes en memoria (*endianness* y orden de red), arquitectura y ciclo de vida de sockets TCP con el módulo estándar `socket`, resolución del flujo continuo mediante protocolos de longitud prefijada (*chunking* con cabecera de 4 bytes), implementación de servidores concurrentes multihilo para múltiples clientes y topologías P2P, y comunicación veloz no orientada a conexión mediante datagramas con sockets UDP.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los cuatro notebooks principales y el notebook bonus de la undécima semana del curso (serialización con pickle, manejo de bytes y encoding, networking con Python, ejemplos avanzados de sockets y bonus de sockets UDP), complementado con las diapositivas de clases.

## Orden de estudio
1. [[01 - Serialización binaria con pickle y riesgos de seguridad|Serialización binaria con pickle y riesgos de seguridad]]: persistencia binaria de objetos complejos de Python, métodos `dumps`/`loads` y `dump`/`load`, personalización con `__getstate__` y `__setstate__`, y prevención de ejecución arbitraria de código.
2. [[02 - Manejo de bytes codificación y endianness|Manejo de bytes, codificación y endianness]]: inmutabilidad de `bytes` y mutabilidad de `bytearray`, conversión numérica con `to_bytes` y `from_bytes`, orden Big-endian frente a Little-endian, y procesamiento por trozos (*chunks*).
3. [[03 - Sockets TCP en Python: arquitectura y ciclo de vida|Sockets TCP en Python: arquitectura y ciclo de vida]]: puntos finales de red (*endpoints*), ciclo del servidor (`bind`, `listen`, `accept`, `recv`, `sendall`), ciclo del cliente (`connect`), socket dedicado por cliente y opciones `SO_REUSEADDR`.
4. [[04 - Transmisión de mensajes estructurados y protocolo de longitud fija|Transmisión de mensajes estructurados y protocolo de longitud fija]]: naturaleza de flujo continuo de TCP (*stream*), prevención de truncamiento y pérdida de paquetes, y diseño de un protocolo de aplicación con cabecera de 4 bytes y acumulación de chunks.
5. [[05 - Servidores concurrentes multihilo y arquitecturas distribuidas|Servidores concurrentes multihilo y arquitecturas distribuidas]]: superación del cuello de botella monofilo mediante el patrón hilo por cliente (*thread per client*), clientes multiconexión y sistemas distribuidos entre pares (P2P).
6. [[06 - Sockets UDP: comunicación no orientada a conexión con datagramas|Sockets UDP: comunicación no orientada a conexión con datagramas]]: modelo de datagramas sin sesión con `SOCK_DGRAM`, métodos `recvfrom` y `sendto`, ausencia de `listen`/`accept`, y control de pérdidas con `settimeout()`.

