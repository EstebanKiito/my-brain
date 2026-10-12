---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de red y direccionamiento"
tags:
  - sistemas-operativos
  - redes
  - icmp
  - ping
  - traceroute
  - ipv6
  - dual-stack
  - tunneling
prerrequisitos:
  - "[[15-Capa de red y direccionamiento/04 - Configuración dinámica con DHCP y traducción de direcciones NAT|04 - Configuración dinámica con DHCP y traducción de direcciones NAT]]"
---

# Protocolo ICMP y transición a IPv6: dual-stack y tunneling

La capa de red se complementa con **ICMP** (*Internet Control Message Protocol*, RFC 792), un protocolo de señalización y diagnóstico utilizado por hosts y routers para comunicar errores en la entrega de datagramas y probar conectividad (como en `ping` y `traceroute`). Ante el agotamiento definitivo del espacio de 32 bits de IPv4, se diseñó **IPv6** (RFC 8200), que ofrece direcciones de 128 bits, cabeceras simplificadas de 40 bytes fijos y estrategias de coexistencia como *Dual-Stack* y *Tunneling*.

---

## Diagnóstico con ICMP y migración a IPv6 (mis apuntes)

ICMP
Protocolo de Control de condiciones de la RED
- Conjunto de reglas de comunicación que se utiliza para diagnosticar problemas de comunicación en una red.
- Usado para Mensajes de Diagnostico y Control de la capa de RED

![Formato de mensajes y tipos del protocolo de control ICMP](adjuntos/Formato%20de%20mensajes%20y%20tipos%20del%20protocolo%20de%20control%20ICMP.png)

> [!example]- Transcripción de la imagen
> Estructura del mensaje ICMP: Encapsulado directamente en un datagrama IP (protocolo 1). Consta de campo Tipo (8 bits), Código (8 bits) y Checksum (16 bits), seguido de los primeros 8 bytes del datagrama que causó el error.

- ICMP contiene dos campos: (ICMP type, ICMP code)

Mensajes Conocidos:
- (8,0) : Echo Request
- (0,0): Echo reply (PING)
- Programa traceroute usa mensajes ICMP con distintos TTL.

IPv6
IPv6 utliza direcciones de 128 bits → Numero tan grande como atomos en el Universo!!!
No todo el mundo aun se cambia a Ipv6
HEADER : 40 Bytes: Prioridad es Agilizar el Procedimiento
¿Como hacer la TRANSICIÓN?
Router IPV6 puede ser backward compatibles (al 4), pero Router IPV4 NO!
- Notar que en el paso de IPv4 a 6, Flow = ??
Soluciones

![Estructura del encabezado simplificado de 40 bytes en IPv6](adjuntos/Estructura%20del%20encabezado%20simplificado%20de%2040%20bytes%20en%20IPv6.png)

> [!example]- Transcripción de la imagen
> Encabezado IPv6 (40 bytes fijos): Versión (4 bits), Traffic Class (8 bits), Flow Label (20 bits), Payload Length (16 bits), Next Header (8 bits, reemplaza al campo Protocolo), Hop Limit (8 bits, reemplaza al TTL), IP Origen (128 bits) e IP Destino (128 bits). Elimina checksum y fragmentación en routers.

- Establecer un dia de cambio mundial? → YA se intentó

![Estrategia de transición Dual-Stack para coexistencia de IPv4 e IPv6](adjuntos/Estrategia%20de%20transición%20Dual-Stack%20para%20coexistencia%20de%20IPv4%20e%20IPv6.png)

> [!example]- Transcripción de la imagen
> Enfoque Dual-Stack: Los routers y hosts intermedios implementan simultáneamente las pilas de protocolos IPv4 e IPv6 completas, traduciendo y encaminando tráfico según la versión del destino.

- Usar Routers DUAL STACK (IPv6/IPv4)
- TUNNELING: Encapsular el paquete de un formato dentro de otro → Para darle la forma para que pase por cierta comunicacion especial (tramos ipv4)

![Técnica de encapsulamiento por tunneling de paquetes IPv6 sobre redes IPv4](adjuntos/Técnica%20de%20encapsulamiento%20por%20tunneling%20de%20paquetes%20IPv6%20sobre%20redes%20IPv4.png)

> [!example]- Transcripción de la imagen
> Túnel IPv6 sobre IPv4 (*Tunneling*): Un datagrama IPv6 completo se encapsula como payload dentro de un datagrama IPv4 estándar para atravesar una red o nube de routers intermediarios que solo soportan IPv4, siendo desencapsulado al alcanzar el siguiente router IPv6.

---

## Preguntas de repaso

> [!question]- ¿Cómo utiliza `traceroute` el campo TTL y los mensajes ICMP para descubrir la ruta hacia un destino?
> Envía datagramas con TTL incremental ($1, 2, 3, \dots$). El router en el salto $N$ decrementa el TTL a 0, descarta el paquete y responde con un mensaje `ICMP Type 11, Code 0` (*Time Exceeded*), revelando su dirección IP al emisor.

> [!question]- ¿Por qué IPv6 eliminó el checksum de cabecera y la fragmentación en routers intermedios?
> Para acelerar el procesamiento de paquetes por hardware en los enrutadores; la detección de errores ya se realiza en las capas de enlace y transporte, y si un paquete excede la MTU, el router emite un mensaje ICMP *Packet Too Big* para que el host origen ajuste el tamaño (*Path MTU Discovery*).

> [!question]- ¿Cuál es la diferencia entre *Dual-Stack* y *Tunneling* como mecanismos de transición a IPv6?
> En *Dual-Stack*, los nodos ejecutan ambas pilas y hablan nativamente IPv4 o IPv6; en *Tunneling*, paquetes completos IPv6 viajan encapsulados dentro de paquetes IPv4 para atravesar infraestructuras antiguas sin necesidad de que todos los routers intermedios sean actualizados a IPv6.

