---
ramo: "Seguridad Computacional"
tema: "Seguridad TCP-IP"
tags:
  - seguridad/redes
  - origen/complemento
prerrequisitos:
  - "[[01 - Ataques a TCP e IP falsificada]]"
---

# Denegación de servicio y protocolos de enrutamiento

Aunque no haya problemas de autenticación, la red debe seguir entregando datos. Un ataque de **denegación de servicio** (DoS) busca agotar un recurso (extorsión o parte de un ataque mayor). Además, los protocolos de enrutamiento confían demasiado en sus participantes.

## SYN flooding
El servidor guardaba estado por cada conexión "medio abierta" (para validar el tercer paquete) durante minutos, con un máximo (por ejemplo 50). El atacante envía SYN con IP de origen falsas aleatorias: nunca llega el tercer paquete, la tabla se llena y se ignoran las conexiones legítimas. Es difícil de rastrear (IP falsas, tasa baja: 1996).

> [!tip] SYN cookies
> El servidor se vuelve **sin estado** hasta recibir el ACK: codifica el estado en el número de secuencia, `ISNs = SNc + (timestamp ‖ hash(IPs, puertos, secreto, timestamp))`. Al llegar el ACK recalcula el hash y comprueba que sea válido, lo que también prueba que la IP no era falsa.

## Amplificación de ancho de banda
El atacante envía una solicitud pequeña con la **IP de la víctima falsificada** y muchos servidores responden a la víctima con respuestas grandes.
- **ICMP broadcast:** un `ping` a la dirección de broadcast de una subred de 100 máquinas da amplificación ×100; hoy los enrutadores bloquean el broadcast dirigido.
- **DNS:** consulta pequeña, respuesta grande (más con DNSSEC), por UDP sin verificar el origen. Difícil de evitar: muchos servidores deben responder a clientes abiertos.
- Variantes modernas con Memcached (UDP) y *middleboxes* TCP.

## Protocolos de enrutamiento
| Protocolo | Alcance | Problema |
|---|---|---|
| **ARP** | Una red Ethernet | Cualquiera responde al broadcast sin autenticación: el atacante se hace pasar por el enrutador e intercepta paquetes |
| **DHCP** | Una red Ethernet | Un servidor falso asigna IP, enrutador y servidores DNS del atacante |
| **BGP** | Toda Internet | Cualquier enrutador puede anunciar rutas a cualquier IP: atrae tráfico, lo inspecciona o modifica y lo reenvía (*BGP leak*) |

## Reconocimiento
Internet abierta facilita recolectar información: sondear puertos y banners, `nmap` para adivinar el SO, DNS inverso, `traceroute` para encontrar enrutadores.

## Cómo mejorar
Parches compatibles en las implementaciones (ISN, SYN cookies), **firewalls** (parcial: el adversario puede estar dentro, es difícil saber qué paquete es malicioso y difícil autenticar origen/destino) y criptografía sobre TCP/IP (TLS, SSH, Kerberos), ver [[01 - TLS 1.3 y el canal seguro|TLS]].

## Preguntas de repaso

> [!question]- ¿Por qué las SYN cookies resuelven el SYN flooding sin perder la verificación de la IP?
> Porque el estado va dentro del número de secuencia firmado con un secreto: al recibir el ACK el servidor lo valida sin haber guardado nada, y una IP falsa no puede reproducir un valor válido.

> [!question]- ¿Por qué la amplificación necesita falsificar la IP de origen?
> Para que las respuestas grandes vayan a la víctima y no al atacante; funciona sobre UDP o ICMP porque no hay handshake que verifique el origen.

> [!question]- ¿Qué tienen en común ARP, DHCP y BGP?
> Aceptan información de cualquier participante sin autenticarla, por lo que un atacante puede desviar el tráfico o configurar a las víctimas.
