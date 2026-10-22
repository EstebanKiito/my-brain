---
ramo: "Seguridad Computacional"
tema: "DDoS y cadena de suministro"
tags:
  - seguridad/disponibilidad
  - origen/complemento
prerrequisitos:
  - "[[02 - Denegación de servicio y protocolos de enrutamiento]]"
---

# DoS, DDoS y ataques de reflexión

La **disponibilidad** es uno de los tres pilares de la tríada CIA, y un ataque de denegación de servicio la ataca directamente: el dato sigue íntegro y confidencial, pero inaccesible para quien lo necesita.

## Tres variantes

| Ataque | Cómo actúa | Ejemplos |
|---|---|---|
| **DoS** | Una fuente explota fallas de protocolo o aplicación (capas 4 y 7) | Slowloris (HTTP), ReDoS |
| **DDoS** | Muchas fuentes coordinadas aportan más capacidad (capas 3 a 5) | Botnets, APK con malware, voluntarios coordinados (LOIC) |
| **DrDoS** (reflexión) | Se abusa de servidores mal configurados para que envíen tráfico no solicitado a la víctima | NTP (×550), DNS (×60), SSDP (×100), SNMP, CHARGEN (×400) |

Un DrDoS es más anónimo y difícil de localizar, y usa protocolos pensados para la Internet de antaño.

## Cómo funciona la reflexión
El atacante envía paquetes con la **IP de origen falsificada** (la de la víctima) a muchos reflectores; estos, creyendo que la víctima preguntó, le envían respuestas **amplificadas**. Por ejemplo, con DNS: consulta pequeña (`QTYPE=ANY/TXT` de un dominio con muchos registros) que genera una respuesta de unos 4 KB o más hacia la víctima. Con 1 Mbps el atacante logra decenas de Gbps combinando reflectores.

Conviene distinguir la amplificación en **paquetes por segundo** (PPS), que agota la CPU de enrutadores de software que procesan paquete a paquete, y en **volumen** (Gbps/Tbps), que satura el enlace; los enrutadores de hardware (ASIC) reenvían a velocidad de línea con menos observabilidad. Falsificar la IP exige saltarse capas de abstracción del sistema (sockets *raw*), y el enrutador puede descartar el paquete.

**Daño colateral:** el ataque no solo tumba a la víctima, también puede saturar al proveedor y afectar a otros clientes del mismo enlace.

## Defensas
- **RTBH** (*Remote Triggered Blackhole*): se pide al proveedor descartar el tráfico hacia una IP; el atacante igual gana, porque el servicio queda sin conectividad.
- **Protección remota (scrubbing centers):** un proveedor recibe tu tráfico, lo limpia y reenvía solo el legítimo por un túnel (GRE).
- **Anycast propio:** la misma IP anunciada por BGP desde varios puntos de presencia reparte y absorbe el ataque volumétrico (20 Gbps repartidos en cuatro PoP de ~5 Gbps).
- Defensas en capa 7. Preventivas: filtrado de IP falsas (BCP38) y bloquear servicios abiertos.

Los ataques tienen también un componente social: dan estatus, y se usan como venganza, censura o extorsión; el atacante busca reconocimiento (noticias, reclamos).

## Preguntas de repaso

> [!question]- ¿Por qué la reflexión necesita falsificar la IP de origen?
> Porque las respuestas deben llegar a la víctima y no al atacante; por eso funciona con protocolos sin handshake (UDP) donde el origen no se verifica.

> [!question]- ¿Por qué el RTBH "da la victoria" al atacante?
> Porque descarta todo el tráfico hacia la IP, también el legítimo: el servicio queda inaccesible, que era el objetivo del ataque.

> [!question]- ¿Cómo ayuda anycast contra un ataque volumétrico?
> Anuncia la misma IP desde muchos PoP, de modo que el tráfico se reparte (cada PoP absorbe y filtra una fracción) y no se concentra en un solo enlace.
