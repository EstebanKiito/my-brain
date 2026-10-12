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
prerrequisitos:
  - "[[17-Capa de enlace y seguridad/03 - Conmutación en redes locales (Switches L2, STP) y VLANs|03 - Conmutación en redes locales (Switches L2, STP) y VLANs]]"
---

# Fundamentos de seguridad en redes: amenazas, ataques y defensas

La **seguridad computacional en redes** aborda la protección de los canales de comunicación y de los sistemas interconectados frente a adversarios activos o pasivos. Históricamente, muchos protocolos fundacionales de Internet (como IP, ARP, DNS y HTTP) fueron diseñados sin mecanismos criptográficos intrínsecos de autenticación o privacidad, asumiendo un entorno cooperativo de confianza. Por ello, la seguridad actual opera bajo una estrategia de **defensa en profundidad** (*Defense in Depth*) a lo largo de todas las capas de la pila protocolar.

---

## Amenazas y estrategias de seguridad (mis apuntes)

CHARLA SEGURIDAD
Anotar lo mas importante → No hay videos del profe RUZ , pero la SLIDES tiene lo importante
- Problemas y Casos tipicos de FALLAS DE SEGURIDAD
- Estrategias Sobre SEGURIDAD

> [!tip] Complemento de clase: Pilares fundamentales de la seguridad (Tríada CIA)
> Toda arquitectura de seguridad informática busca garantizar cuatro propiedades fundamentales:
> 1. **Confidencialidad**: Garantizar que la información transmitida solo sea legible por los destinatarios autorizados mediante técnicas de cifrado.
> 2. **Integridad**: Comprobar que los mensajes recibidos no han sido modificados, truncados o inyectados fraudulentamente en tránsito.
> 3. **Autenticación**: Validar con certeza matemática la identidad del emisor o de la entidad remota antes de conceder acceso a recursos o procesar datos.
> 4. **Disponibilidad**: Garantizar que los servidores, interfaces y servicios de red permanezcan operativos y accesibles ante fallos o agresiones maliciosas.

> [!tip] Complemento de clase: Taxonomía de ataques comunes en redes
> - **Sniffing (Espionaje pasivo)**: Interceptación y lectura de tramas en medios compartidos o mediante herramientas como Wireshark. Si los protocolos transmiten credenciales en texto plano (como HTTP o Telnet), la información queda expuesta de inmediato.
> - **ARP Spoofing / Envenenamiento ARP**: Un atacante en la red local emite respuestas ARP gratuitas falsificadas asociando la IP del router con su propia MAC. Esto canaliza todo el tráfico saliente a través del atacante en un ataque de **Hombre en el Medio** (*Man-in-the-Middle*, MitM).
> - **IP Spoofing**: Inyección de paquetes IP con direcciones de origen falsas para saltarse listas de control de acceso o redirigir respuestas a víctimas involuntarias.
> - **Ataques de Denegación de Servicio (DoS / DDoS)**: Inundación masiva de tráfico coordinada mediante botnets. Ejemplos clásicos:
>   - **TCP SYN Flood**: Envío de oleadas de paquetes SYN sin completar el handshake de 3 vías, agotando la tabla de conexiones pendientes (*backlog queue*) del servidor.
>   - **Ataques de amplificación**: Envío de peticiones UDP (DNS, NTP) con IP de origen falsificada hacia servidores públicos que devuelven respuestas desproporcionadamente grandes hacia la víctima.

> [!tip] Complemento de clase: Estrategias de mitigación y defensa en profundidad
> 1. **Criptografía**:
>    - **Cifrado simétrico** (AES): Utiliza una misma clave secreta compartida; es óptimo por su alta velocidad de procesamiento para flujos masivos de datos.
>    - **Cifrado asimétrico** (RSA, curvas elípticas): Utiliza un par de claves (pública y privada); se usa para autenticación y para establecer claves simétricas de sesión de forma segura.
>    - **Firmas digitales y HMAC**: Proveen integridad irrefutable y no repudio.
> 2. **Protocolos seguros de aplicación y transporte**: Implementación obligatoria de **TLS** (*Transport Layer Security*) sobre TCP para encapsular HTTP (formando HTTPS), SMTP y DNS (DoT/DoH).
> 3. **Cortafuegos (Firewalls)**: Dispositivos o software que inspeccionan paquetes en el perímetro:
>    - *Stateless*: Filtran por tuplas simples (IPs, puertos, flags TCP).
>    - *Stateful*: Realizan seguimiento del estado de cada conexión TCP para bloquear tráfico entrante que no responda a una petición legítima interna.
> 4. **Seguridad en conmutación local**: Mecanismos como *DHCP Snooping*, *Dynamic ARP Inspection* (DAI) y *Port Security* en switches L2 para evitar envenenamiento de tablas y spoofing de direcciones.

---

## Preguntas de repaso

> [!question]- ¿Cómo se ejecuta un ataque de envenenamiento ARP (*ARP Cache Poisoning*) en una red local?
> El atacante transmite periódicamente mensajes falsos de ARP Reply al host víctima indicando que la dirección IP del *Default Gateway* corresponde a la dirección MAC física del atacante. El host actualiza su caché ARP local y redirige todo su tráfico de salida hacia el atacante.

> [!question]- ¿Por qué el cifrado asimétrico se combina habitualmente con el cifrado simétrico en protocolos como TLS/HTTPS en lugar de usar solo cifrado asimétrico?
> Porque los algoritmos asimétricos (como RSA o Diffie-Hellman) son computacionalmente costosos y lentos. Por ello, solo se usan al inicio para autenticar a los pares y negociar una clave secreta de sesión; una vez acordada, todos los datos subsiguientes se cifran con algoritmos simétricos rápidos como AES.

> [!question]- ¿Cómo mitiga un cortafuegos con inspección de estado (*Stateful Firewall*) los paquetes maliciosos no solicitados?
> El cortafuegos mantiene una tabla de estados de conexión en memoria. Si recibe un paquete externo entrante (por ejemplo, un segmento TCP con flag ACK) que no corresponde a ninguna conexión previamente iniciada por un host interno, lo descarta inmediatamente.
