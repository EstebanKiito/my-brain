---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Fundamentos de la web"
tags:
  - web
  - tcp
  - udp
  - tls
  - origen/complemento
prerrequisitos:
  - "[[04 - Mensajes HTTP y versiones del protocolo]]"
---

# Capas de la web, TCP, UDP y TLS

HTTP dice **qué** se pide, pero no cómo viajan los bytes ni cómo se protegen. Esa responsabilidad se reparte en **capas**: cada una resuelve un problema y se apoya en la de abajo, sin preocuparse de cómo funciona. Entender las capas explica por qué HTTPS es seguro, por qué DNS es tan rápido y dónde encajan HTML, CSS y JavaScript.

## Las capas del Internet protocol

![Capas del Internet protocol](adjuntos/Capas%20del%20Internet%20protocol.png)

> [!example]- Transcripción de la imagen
> De arriba hacia abajo:
> - **Application layer**: HTTP, TLS, DNS.
> - **Transport layer**: TCP, UDP.
> - **Network layer**: IP (v4, v6).
> - **Link layer**: Ethernet, Wireless LAN.

- **Enlace**: mueve los datos por un medio físico concreto (cable Ethernet o Wi-Fi).
- **Red**: IP lleva cada paquete de una máquina a otra a través de routers, usando direcciones IP.
- **Transporte**: entrega los datos a la aplicación correcta dentro de la máquina (mediante puertos) y decide si la entrega es confiable.
- **Aplicación**: los protocolos que usan los programas, como HTTP, DNS y TLS.

## TCP frente a UDP

![Comparación entre TCP y UDP](adjuntos/Comparaci%C3%B3n%20entre%20TCP%20y%20UDP.png)

> [!example]- Transcripción de la imagen
> - **TCP**: el emisor pregunta "¿Estás listo?", el receptor responde "Sí" y el emisor dice "Empiezo". Luego envía "Paquete 1", el receptor contesta "Correcto", envía "Paquete 2" y recibe otro "Correcto".
> - **UDP**: el receptor manda una "Solicitud" y el emisor responde con una ráfaga de paquetes, uno tras otro, sin confirmaciones.

| | **TCP** | **UDP** |
|---|---|---|
| Conexión | Se establece antes de enviar (*handshake*) | No hay conexión |
| Confiabilidad | Confirma cada envío, retransmite lo perdido y entrega en orden | No confirma ni retransmite |
| Costo | Más lento por las idas y vueltas | Rápido y liviano |
| Uso en la web | HTTP/1.1 y HTTP/2, TLS | DNS, streaming, juegos |

La regla para elegir es simple: si perder un byte arruina el resultado (una página, un archivo), se usa TCP. Si importa más la velocidad que la perfección (una consulta DNS que se puede repetir, un frame de video), se usa UDP. El detalle está en [[06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa|Protocolo TCP]] y [[03 - Protocolo UDP: datagramas, sobrecarga y checksum|Protocolo UDP]].

## Dónde queda la web

![Tecnologías de la web por capa](adjuntos/Tecnolog%C3%ADas%20de%20la%20web%20por%20capa.png)

> [!example]- Transcripción de la imagen
> Una flecha vertical rotulada "The Web" abarca toda la pila. De arriba hacia abajo:
> - **Client**: HTML, CSS y, a la derecha, Web APIs sobre JavaScript, todo sobre HTTP.
> - **Application / transport**: DNS sobre UDP a la izquierda; TLS sobre TCP a la derecha.
> - **IP layer**: IP en la base.

HTML, CSS y JavaScript (con las Web APIs del navegador) son lo que ve y ejecuta el **cliente**. Todos llegan por HTTP, que a su vez viaja sobre TCP, protegido o no con TLS. El DNS, en cambio, va por UDP.

## TLS y HTTPS

**TLS** es un protocolo de seguridad que da **privacidad** (nadie en el camino puede leer los datos) e **integridad** (nadie puede alterarlos sin que se note) a las comunicaciones por Internet. HTTPS es simplemente HTTP sobre TLS, en el puerto 443.

![Establecimiento de una sesión TLS](adjuntos/Establecimiento%20de%20una%20sesi%C3%B3n%20TLS.png)

> [!example]- Transcripción de la imagen
> Entre *User* y *Server*:
> 1. "Let's set up a secure TLS session".
> 2. El servidor responde "This is my certificate"; el usuario verifica que el certificado sea válido y que lo haya firmado alguien en quien confía.
> 3. El usuario envía "a one-time encryption key for our session", cifrada con la llave pública del servidor.
> 4. El servidor descifra la llave de sesión con su llave privada y queda establecida una sesión segura.

> [!tip] Por qué dos tipos de llave
> La llave pública del certificado solo sirve para enviar de forma segura una **llave de sesión** que solo el servidor puede descifrar. Desde ahí ambos cifran con esa llave compartida, que es mucho más rápida.

> [!warning] HTTPS no oculta todo
> En una red pública, HTTPS impide que un intermediario (ataque *man in the middle*) lea el contenido. Pero el atacante aún puede ver el dominio al que se conecta el usuario, las IPs involucradas, los tiempos de las conexiones y otros metadatos.

## Preguntas de repaso

> [!question]- ¿Por qué DNS usa UDP y HTTP usa TCP?
> Una consulta DNS es un mensaje corto que, si se pierde, se repite sin problema, así que el handshake de TCP sería puro costo. Una página HTTP debe llegar completa y en orden, y eso es justamente lo que garantiza TCP.

> [!question]- ¿Qué garantiza TLS y qué no?
> Garantiza privacidad e integridad del contenido entre cliente y servidor, y que el servidor es quien dice ser (por el certificado). No oculta los metadatos: el dominio visitado, las IPs ni los tiempos de conexión.

> [!question]- ¿Para qué sirve el certificado en el establecimiento de TLS?
> Para que el cliente verifique que el servidor es legítimo (lo firma alguien de confianza) y obtenga su llave pública, con la que cifra la llave de sesión que solo ese servidor puede descifrar.
