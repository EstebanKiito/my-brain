---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de enlace y seguridad"
tags:
  - sistemas-operativos
  - redes
  - seguridad
  - criptografia
  - ataques
  - defensas
  - origen/complemento
prerrequisitos:
  - "[[17-Capa de enlace y seguridad/03 - Conmutación en redes locales (Switches L2, STP) y VLANs|03 - Conmutación en redes locales (Switches L2, STP) y VLANs]]"
---

# Fundamentos de seguridad en redes: amenazas, ataques y defensas

Casi todos los protocolos vistos en el curso (IP, ARP, DNS, HTTP) se diseñaron suponiendo que todos en la red cooperan: no autentican a nadie ni cifran nada. Esta nota repasa los **casos típicos de fallas de seguridad** que eso permite y las **estrategias** para defenderse. La idea de fondo es la **defensa en profundidad** (*defense in depth*): proteger cada capa, sin confiar en una sola barrera.

## Qué se quiere proteger

Confidencialidad, integridad y disponibilidad forman la llamada tríada CIA (*confidentiality, integrity, availability*); a menudo se agrega la autenticación.

| Propiedad | Pregunta que responde | Herramienta típica |
|---|---|---|
| **Confidencialidad** | ¿Solo el destinatario puede leer el mensaje? | Cifrado |
| **Integridad** | ¿El mensaje llegó sin modificaciones? | Firmas digitales, HMAC |
| **Autenticación** | ¿Quien habla es quien dice ser? | Certificados, claves públicas |
| **Disponibilidad** | ¿El servicio sigue funcionando ante fallas o ataques? | Redundancia, filtrado de tráfico |

## Ataques típicos

Cada ataque explota algo que ya vimos que un protocolo **no verifica**:

- **Sniffing** (espionaje pasivo): leer los frames que pasan por un medio compartido, por ejemplo con Wireshark. Si un protocolo envía credenciales en texto plano (HTTP, Telnet), quedan expuestas.
- **ARP spoofing** (envenenamiento ARP): [[02 - Direcciones MAC, protocolo ARP y trama Ethernet|ARP]] acepta cualquier respuesta. Un atacante de la LAN envía respuestas falsas que asocian la IP del router con **su** MAC; las víctimas actualizan su tabla y le mandan todo su tráfico. Es un ataque de **hombre en el medio** (*man-in-the-middle*, MitM). Es un pariente del *switch poisoning*, que afecta la [[03 - Conmutación en redes locales (Switches L2, STP) y VLANs|tabla del switch]].
- **IP spoofing**: enviar paquetes con una IP de origen falsa, para saltarse listas de acceso o para que las respuestas le lleguen a otra víctima.
- **Denegación de servicio** (DoS, o DDoS si es coordinado desde una *botnet*): saturar a la víctima para que no atienda a nadie.
  - **TCP SYN flood**: enviar muchos SYN sin completar el [[14-Capa de transporte/07 - Gestión de temporizadores, retransmisión rápida y handshake en TCP|handshake]]. Como el servidor asigna buffers en el segundo paso, se le agota la cola de conexiones pendientes (*backlog*).
  - **Amplificación**: enviar consultas UDP pequeñas (DNS, NTP) con la IP de la víctima como origen falso; los servidores le responden a ella con respuestas mucho más grandes.

## Estrategias de defensa

**1. Criptografía.**

- **Cifrado simétrico** (AES): una misma clave secreta para cifrar y descifrar. Es rápido, ideal para grandes volúmenes de datos, pero ambos lados deben compartir la clave.
- **Cifrado asimétrico** (RSA, curvas elípticas): un par de claves, pública y privada. Es lento, así que se usa para autenticar y para acordar una clave simétrica de sesión.
- **Firmas digitales y HMAC**: garantizan integridad; las firmas además impiden negar la autoría (no repudio).

**2. Protocolos seguros.** **TLS** (*Transport Layer Security*) va sobre TCP y protege a la aplicación: HTTP sobre TLS es HTTPS, y también se usa con SMTP y DNS. Combina ambos cifrados: el asimétrico al inicio y el simétrico para los datos.

**3. Firewalls.** Inspeccionan los paquetes en el borde de la red:

- *stateless*: filtran cada paquete por sí solo, según IP, puertos y flags TCP;
- *stateful*: recuerdan las conexiones abiertas desde adentro y solo dejan entrar lo que responde a ellas.

```python
conexiones = set()          # conexiones iniciadas desde adentro: (ip_int, p_int, ip_ext, p_ext)

def sale(ip_int, p_int, ip_ext, p_ext):
    conexiones.add((ip_int, p_int, ip_ext, p_ext))
    return "permitido"

def entra(ip_ext, p_ext, ip_int, p_int):
    """Stateful: solo deja pasar respuestas a conexiones que alguien de adentro abrió."""
    return "permitido" if (ip_int, p_int, ip_ext, p_ext) in conexiones else "descartado"

print(sale("192.168.1.86", 8120, "64.233.186.90", 443))    # permitido
print(entra("64.233.186.90", 443, "192.168.1.86", 8120))   # permitido: es una respuesta
print(entra("203.0.113.9", 4444, "192.168.1.86", 8120))    # descartado: nadie lo pidió
```

**4. Seguridad en la LAN.** Los switches pueden validar lo que otros protocolos no validan: *DHCP snooping* (solo aceptar ofertas DHCP del puerto del servidor legítimo), *Dynamic ARP Inspection*, DAI (descartar respuestas ARP que no calzan con las asignaciones conocidas) y *port security* (limitar qué MAC pueden usar cada puerto). Las [[03 - Conmutación en redes locales (Switches L2, STP) y VLANs|VLANs]] también ayudan, porque aíslan los broadcasts.

## Preguntas de repaso

> [!question]- ¿Cómo funciona un ataque de envenenamiento ARP?
> El atacante envía respuestas ARP falsas que asocian la IP del router con su propia MAC. Las víctimas actualizan su tabla ARP y le envían su tráfico, y el atacante queda en medio de la comunicación.

> [!question]- ¿Por qué un SYN flood agota los recursos de un servidor?
> Porque en el handshake el servidor asigna buffers al recibir cada SYN. Si nunca llega el ACK final, esas conexiones a medias llenan la cola de pendientes y no quedan recursos para clientes legítimos.

> [!question]- ¿Por qué TLS usa cifrado asimétrico y simétrico, y no solo uno?
> El asimétrico permite autenticar y acordar una clave sin haberla compartido antes, pero es lento. Por eso solo se usa al inicio, y los datos se cifran con el simétrico, que es rápido.

> [!question]- ¿Qué hace un firewall stateful con un paquete entrante que no responde a ninguna conexión?
> Lo descarta: solo deja entrar paquetes que corresponden a conexiones iniciadas desde la red interna.
