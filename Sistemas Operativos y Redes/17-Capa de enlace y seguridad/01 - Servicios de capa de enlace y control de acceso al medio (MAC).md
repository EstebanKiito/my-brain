---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de enlace y seguridad"
tags:
  - sistemas-operativos
  - redes
  - capa-enlace
  - mac
  - aloha
  - csma-cd
prerrequisitos:
  - "[[16-Algoritmos de ruteo/_Índice|Algoritmos de ruteo]]"
---

# Servicios de capa de enlace y control de acceso al medio (MAC)

La **capa de enlace** (*Data Link Layer*) es responsable de transferir datagramas de la capa de red entre nodos contiguos (hosts, routers o switches) a través de un canal de comunicación individual. A diferencia de las capas de transporte y red, que operan de extremo a extremo a nivel global, cada enlace funciona de manera completamente independiente, pudiendo utilizar diferentes tecnologías y protocolos físicos (por ejemplo, Ethernet en una LAN cableada y 802.11 en el acceso Wi-Fi).

---

## Servicios y acceso al medio (mis apuntes)

Clase 7
4/11/24

CONTENIDO 12: CAPA ENLACE
SWITCH → XD
Por Estudiar:

![Diagrama de capa de enlace, switches, LANs, VLANs y protocolos de acceso al medio](adjuntos/Diagrama%20de%20capa%20de%20enlace%2c%20switches%2c%20LANs%2c%20VLANs%20y%20protocolos%20de%20acceso%20al%20medio.png)

> [!example]- Transcripción de la imagen
> Esquema conceptual manuscrito de capa de enlace:
> - **Capa de enlace**: Controlar el acceso al medio y envío de información a través de los enlaces físicos.
> - **Dispositivo central**: Switch de capa 2.
> - **Conceptos clave**: LAN (*Local Area Network*) y VLAN (*Virtual LAN*), ilustrando un router conectado a un switch que distribuye puertos hacia estaciones divididas en subredes lógicas.
> - **Acceso al medio**: Clasificación en aleatorio, turnos, frecuencias, tiempos y *virtual circuit switching*.
> - **Protocolo destacado**: ALOHA para acceso aleatorio con temporización tras colisiones.
> - **Identificación**: Direcciones MAC físicas en la interfaz de red (tarjeta de red).

CAPA ENLACE:
- Controla el Acceso al Medio
- Controla el Envio de informaciones a traves de los medios (Alambricos o Inalambricos)
El Dispositivo es el Switch

ACCESO AL MEDIO
- Aleatorio → Importante para el algoritmo ALOHA
- Turnos
- Frecuencias
- Virtual Circuit Switching
Protocolo Importante: ALOHA → Todos los dispositivos que estan en una red, le permite a cada uno hablar de forma aleatoria, si hay colisiones, te toca hablar en cierto tiempo despues
Se controla el tiempo de forma aleatoria.

> [!tip] Complemento de clase: Taxonomía de protocolos de acceso múltiple (MAC)
> En enlaces de difusión compartidos (*broadcast channels*), los protocolos MAC (*Medium Access Control*) previenen colisiones coordinando las transmisiones:
> 1. **Particionamiento de canal**: Dividen el ancho de banda en porciones fijas.
>    - **TDMA** (*Time Division Multiple Access*): Divide el tiempo en slots o ranuras periódicas.
>    - **FDMA** (*Frequency Division Multiple Access*): Divide el espectro en bandas de frecuencia exclusivas.
>    - **CDMA** (*Code Division Multiple Access*): Asigna un código ortogonal diferente a cada emisor.
> 2. **Acceso aleatorio**: Los nodos transmiten a máxima tasa de canal ($R$). Si ocurre una colisión, retransmiten tras un tiempo aleatorio.
>    - **ALOHA puro**: Transmisión inmediata. Máxima eficiencia de utilización: $1/(2e) \approx 18.4\%$.
>    - **Slotted ALOHA**: Tiempo dividido en ranuras discretas; las transmisiones solo inician en el borde del slot. Eficiencia: $1/e \approx 36.8\%$.
>    - **CSMA** (*Carrier Sense Multiple Access*): "Escuchar antes de hablar". Si el canal está ocupado, el nodo pospone su transmisión.
>    - **CSMA/CD** (*Collision Detection*, Ethernet 802.3): Si se detecta colisión durante la transmisión, se aborta inmediatamente y se aplica retroceso exponencial binario (*exponential backoff*).
> 3. **Por turnos** (*Taking-Turns*): **Polling** (nodo maestro consulta secuencialmente a esclavos) o **Token Passing** (un testigo especial circula entre nodos en anillo).

> [!tip] Complemento de clase: Detección y corrección de errores en capa de enlace
> Los frames añaden bits de redundancia para verificar la integridad física de los datos:
> - **Bit de paridad**: Paridad simple detecta errores impares de 1 bit. La paridad bidimensional (filas y columnas) puede detectar y corregir errores de 1 bit.
> - **CRC** (*Cyclic Redundancy Check*): Basado en aritmética de polinomios en campo de Galois módulo 2 (operaciones XOR sin acarreo). Dado un generador estándar $G$ de $r+1$ bits, se calcula un resto $R$ de $r$ bits tal que $(D \cdot 2^r) \text{ XOR } R$ sea divisible exactamente por $G$. Ampliamente utilizado en Ethernet y Wi-Fi por su gran capacidad de detección de ráfagas de error.

---

## Preguntas de repaso

> [!question]- ¿Por qué se dice que los enlaces en la capa de enlace son independientes entre sí?
> Porque cada segmento de red físico puede implementar un protocolo de enlace y medio de transmisión distinto (por ejemplo, Wi-Fi 802.11 entre laptop y router, y fibra óptica Ethernet entre el router y el ISP). La capa de enlace solo entrega frames de un salto al siguiente.

> [!question]- ¿Qué ventaja ofrece CSMA/CD frente a protocolos de acceso aleatorio simples como ALOHA?
> En CSMA/CD los nodos escuchan el canal antes de transmitir (reduciendo colisiones) y, si dos nodos transmiten simultáneamente, detectan la colisión de inmediato y abortan la transmisión, evitando desperdiciar el tiempo de canal transmitiendo tramas corruptas completas.

> [!question]- ¿Cómo funciona el algoritmo de retroceso exponencial binario (*exponential backoff*) tras una colisión?
> Tras la $m$-ésima colisión consecutiva (hasta un tope), el nodo selecciona al azar un número entero $K \in \{0, 1, 2, \dots, 2^m - 1\}$ y espera $K$ tiempos de ranura antes de reintentar la transmisión, dispersando eficientemente a los competidores.
