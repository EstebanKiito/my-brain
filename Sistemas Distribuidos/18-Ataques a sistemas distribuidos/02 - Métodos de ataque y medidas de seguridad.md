---
ramo: "Sistemas Distribuidos"
tema: "Ataques a sistemas distribuidos"
tags:
  - sd/seguridad
  - origen/complemento
prerrequisitos:
  - "[[01 - Amenazas y modelo del enemigo]]"
---

# Métodos de ataque y medidas de seguridad

Los ataques a un sistema distribuido explotan canales de comunicación legítimos o simulan conexiones autorizadas. Cada método tiene una defensa característica, y esas defensas (cifrado, autenticación, canales seguros, monitoreo) son el temario del resto de la unidad.

## Métodos de ataque

| Ataque | Qué hace | Ejemplos |
|---|---|---|
| **Eavesdropping** (escucha) | Obtiene copias de mensajes sin autorización; en muchas redes locales basta un programa para capturar el tráfico ajeno | Filtraciones de Snowden; filtraciones masivas de contraseñas |
| **Masquerading** (suplantación) | Envía o recibe mensajes con la identidad de otro principal (persona, software o dispositivo) sin su autoridad | **Phishing** para robar contraseñas o datos de tarjetas; estafas con voces clonadas con IA |
| **Message tampering** (manipulación) | Altera un mensaje para cambiar su significado | *Man-in-the-middle*, inyección SQL, manipulación de código fuente (Stuxnet modificaba instrucciones del computador) |
| **DDoS** (denegación de servicio distribuida) | Invocaciones o mensajes excesivos y sin sentido, desde **muchas fuentes**, que sobrecargan ancho de banda o procesamiento | GitHub resistió uno de los mayores ataques DDoS registrados |

Que el ataque venga de muchas fuentes es lo que hace a un DDoS más difícil de frenar que un DoS: no basta con bloquear una dirección. Su objetivo suele ser retrasar o impedir las acciones de los usuarios legítimos.

**Otros ataques:**

- **Sybil:** crear muchas identidades falsas para manipular votaciones o reputación.
- **Eclipse:** aislar a un nodo controlando todas sus conexiones, bloqueando su visión del sistema.
- **Replay:** interceptar mensajes válidos y retransmitirlos para que parezcan recientes.
- **Routing attack:** manipular la información de enrutamiento (como en DHT o P2P) para redirigir o interceptar datos.

## Medidas de seguridad

El diseño seguro parte de una lista de amenazas y de suposiciones de **peor caso**: el adversario es un "*big boss*", inteligente y con mucho poder. Lo recomendado es construir un **modelo de amenazas** que enumere todas las formas de ataque (desde la red, el entorno físico y el humano) y evalúe el riesgo y las consecuencias de cada una.

| Medida | Qué hace | Protege principalmente de |
|---|---|---|
| **Cifrado** | Oculta el contenido de los mensajes | Eavesdropping y tampering |
| **Autenticación y autorización** | Verifica la identidad declarada y que solo se hagan operaciones permitidas | Masquerading |
| **Canales seguros** | Combinan criptografía y autenticación para dar privacidad e integridad (por ejemplo, una VPN o TLS) | Eavesdropping, tampering y masquerading |
| **Monitoreo** | Rastrea el acceso a los activos para detectar intrusiones externas o internas | DoS y ataques internos |

> [!warning] Cifrar no impide interceptar
> El cifrado no evita que el atacante **capture** los mensajes; evita que entienda su contenido. Tampoco protege por sí solo de la suplantación.

## Compromisos

![Compromisos entre seguridad y otras propiedades](adjuntos/Compromisos%20entre%20seguridad%20y%20otras%20propiedades.png)

> [!example]- Transcripción de la imagen
> ¿Qué *trade-offs* pueden existir? **Rendimiento frente a seguridad:** la criptografía tiende a ser costosa. **Usabilidad frente a seguridad:** tantos mecanismos de autenticación (dos fases, login periódicos) afectan la usabilidad. **Privacidad frente a seguridad:** rastrear todas las acciones del usuario puede invadir su privacidad.

También hay límites legales a lo que se puede monitorear, y preguntas abiertas: ¿hasta qué punto la seguridad pasa por encima de los derechos del usuario? ¿Vale la pena un sistema muy seguro pero lento?

## Preguntas de repaso

> [!question]- ¿Qué ataque describe el modelo del enemigo cuando lee y copia mensajes, y qué defensa lo mitiga?
> Eavesdropping. Se mitiga con cifrado o canales seguros: el atacante sigue capturando los mensajes, pero no entiende su contenido.

> [!question]- ¿Por qué un DDoS es más difícil de defender que un DoS?
> Porque el tráfico viene de muchas fuentes distintas, a menudo equipos legítimos comprometidos, y no basta con bloquear un origen.

> [!question]- ¿Qué busca un ataque de denegación de servicio: obtener datos o algo más?
> Interferir con el uso del sistema (sobrecargar recursos para que los usuarios legítimos no puedan usarlo), no obtener acceso a datos confidenciales.
