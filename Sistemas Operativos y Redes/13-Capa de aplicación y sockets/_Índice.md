# Capa de aplicación y sockets — índice

Principios teóricos, arquitecturas de software y protocolos de la capa de aplicación en Internet, junto a la interfaz de programación de red mediante sockets del sistema operativo. Análisis de los paradigmas de comunicación: arquitectura centralizada cliente-servidor y arquitectura distribuida entre pares (*Peer-to-Peer* / P2P). Abstracción de sockets como punto final de comunicación: multiplexación y direccionamiento mediante pares IP y número de puerto (puertos bien conocidos, registrados y efímeros). Modelos de sockets de datagrama no orientados a conexión (UDP) frente a sockets de flujo continuo orientados a conexión con saludo de tres vías (TCP) y su implementación mediante llamadas al sistema del kernel (`socket`, `bind`, `listen`, `accept`, `connect`, `send`, `recv`, `sendto`, `recvfrom`). Estudio de los protocolos estándar de aplicación: protocolo HTTP (estructura de solicitudes y respuestas, códigos de estado, persistencia frente a no persistencia, cookies de sesión y cachés web intermedias/CDNs), protocolos de transferencia de archivos (FTP con canales de control y datos fuera de banda) y correo electrónico (SMTP, POP3, IMAP). Funcionamiento detallado del Sistema de Nombres de Dominio (DNS): jerarquía distribuida (raíz, TLD, autoritativos y resolvidores locales), consultas recursivas frente a iterativas, caché y registros de recursos (RR tipos A, NS, CNAME y MX). Finalmente, redes P2P y distribución de contenidos masivos mediante BitTorrent (enjambres, fragmentación en bloques, algoritmos *Rarest First* y *Tit-for-Tat*, y Tablas Hash Distribuidas / DHT).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la Clase 3 y Clase 4 de los apuntes originales de Redes, complementadas con las diapositivas oficiales de `Contenido_9_Capa_Aplicacion.pdf` y la literatura estándar de redes de computadores (Kurose & Ross).

## Orden de estudio

1. [[01 - Arquitecturas de aplicación y modelos de comunicación|Arquitecturas de aplicación y modelos de comunicación]]: capa de aplicación en hosts terminales, modelo cliente-servidor centralizado y modelo P2P distribuido con auto-escalabilidad y consideraciones de ISP.
2. [[02 - Concepto de socket e identificación por IP y puerto|Concepto de socket e identificación por IP y puerto]]: abstracción del socket como interfaz de transporte, direccionamiento mediante dirección IP y puerto, y clasificación de rangos de puertos.
3. [[03 - Sockets UDP y TCP: modelos y llamadas al sistema|Sockets UDP y TCP: modelos y llamadas al sistema]]: llamadas al sistema en C y Python para sockets UDP (datagramas independientes sin conexión) y TCP (welcoming socket, handshake y conexiones punto a punto).
4. [[04 - Protocolo HTTP, formato de mensajes y estado con cookies|Protocolo HTTP, formato de mensajes y estado con cookies]]: formato de solicitudes y respuestas HTTP, naturaleza stateless, mantenimiento de sesión mediante cookies, proxies de caché, y comparación con FTP, SMTP, POP3 e IMAP.
5. [[05 - Sistema de nombres de dominio (DNS) y resolución de consultas|Sistema de nombres de dominio (DNS) y resolución de consultas]]: jerarquía de servidores DNS, resolución iterativa frente a recursiva, caché DNS con TTL, y registros de recursos tipo A, NS, CNAME y MX.
6. [[06 - Redes Peer-to-Peer (P2P) y distribución con BitTorrent|Redes Peer-to-Peer (P2P) y distribución con BitTorrent]]: enjambres, trackers, descarga por fragmentos, algoritmos Rarest First y Tit-for-Tat, y tablas hash distribuidas (DHT).

