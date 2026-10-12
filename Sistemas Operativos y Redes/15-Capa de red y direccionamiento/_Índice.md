# Capa de red y direccionamiento — índice

Principios teóricos, formatos de paquetes, esquemas de direccionamiento y protocolos de la capa de red (Capa 3 del modelo OSI e Internet). Separación funcional entre el plano de datos (reenvío local o *forwarding* en hardware mediante tablas de reenvío en routers bajo el modelo *Store-and-Forward*) y el plano de control (cálculo coordinado de rutas globales o *routing*). Comparación entre redes de circuitos virtuales (orientadas a conexión con reserva de ancho de banda como la telefonía) y redes de datagramas (no orientadas a conexión, flexibles ante congestión y robustas ante caídas de nodos como Internet). Estructura detallada del datagrama IPv4 (cabecera fija de 20 bytes, campos TTL y checksum) y mecanismos de fragmentación por MTU en enlaces heterogéneos mediante identificadores, flags (DF/MF) y desplazamientos (*fragment offset*). Esquemas de direccionamiento IPv4: notación decimal con puntos, máscaras de subred, notación CIDR (`a.b.c.d/x`), direcciones especiales (red, broadcast, loopback) y rangos privados (RFC 1918). Protocolos de soporte y borde: configuración dinámica de parámetros de red mediante DHCP (ciclo DORA: Discover, Offer, Request, ACK), traducción de direcciones de red NAT/NAPT (tablas de mapeo puerto-IP, traverse con UPnP y debate arquitectónico de extremo a extremo), diagnóstico y control con ICMP (mensajes Echo Request/Reply en `ping` y time exceeded en `traceroute`). Finalmente, diseño y arquitectura de IPv6 (direcciones de 128 bits, cabecera simplificada de 40 bytes) y estrategias de transición y coexistencia (*Dual-Stack* y *Tunneling*).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la Clase 6 de los apuntes originales de Redes (`CONTENIDO 11 → CAPA DE RED`), complementadas con las diapositivas oficiales de `Contenido_11_Capa_Red.pdf` y la literatura estándar de redes (Kurose & Ross, Tanenbaum).

## Orden de estudio

1. [[01 - Servicios de la capa de red: enrutamiento y reenvío|Servicios de la capa de red: enrutamiento y reenvío]]: responsabilidades de capa 3 en hosts y routers, separación entre plano de datos (forwarding) y plano de control (routing), y paradigma Store-and-Forward.
2. [[02 - Datagrama IPv4: estructura y fragmentación por MTU|Datagrama IPv4: estructura y fragmentación por MTU]]: comparación de redes de datagramas frente a circuitos virtuales, estructura de la cabecera IPv4 y cálculo de fragmentación y offsets por MTU.
3. [[03 - Direccionamiento IPv4: subredes, máscaras y notación CIDR|Direccionamiento IPv4: subredes, máscaras y notación CIDR]]: notación CIDR, cálculo de dirección de red y broadcast mediante máscaras bit a bit, subredes en topologías con routers y rangos reservados.
4. [[04 - Configuración dinámica con DHCP y traducción de direcciones NAT|Configuración dinámica con DHCP y traducción de direcciones NAT]]: protocolo plug-and-play DHCP (DORA), mitigación del espacio IP mediante NAT, tablas de traducción, UPnP y violación de extremo a extremo.
5. [[05 - Protocolo ICMP y transición a IPv6: dual-stack y tunneling|Protocolo ICMP y transición a IPv6: dual-stack y tunneling]]: mensajes de control y diagnóstico ICMP en ping y traceroute, cabecera de 40 bytes de IPv6, y técnicas de coexistencia Dual-Stack y Tunneling.

