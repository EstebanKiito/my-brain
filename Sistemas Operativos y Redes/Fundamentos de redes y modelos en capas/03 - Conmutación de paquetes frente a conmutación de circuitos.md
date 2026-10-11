---
ramo: "Sistemas Operativos y Redes"
tema: "Fundamentos de redes y modelos en capas"
tags:
  - redes/nucleo
  - redes/conmutacion
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Fundamentos de redes y modelos en capas/01 - Arquitectura de Internet, nodos, enlaces y protocolos\|01 - Arquitectura de Internet, nodos, enlaces y protocolos]]"
---

# Conmutación de paquetes frente a conmutación de circuitos

El núcleo de la red interconecta los sistemas terminales utilizando dos paradigmas opuestos de transporte de información: conmutación de paquetes (*Packet Switching*) y conmutación de circuitos (*Circuit Switching*).

## Funcionamiento del núcleo de red y conmutación (mis apuntes)

- FUNCIONAMIENTO DE RED
- Si quiero transmitir L bits sobre un enlace que soporta R bits por segundo
- Entonces puedo transmitir a una velocidad de L/R
- Formula Importante: Demora de trasnmicion : L bits sobre enlace / R (bits/sec)
- La red de INTERNET es una red de Paquetes, transmite paquetes de un destino a otro, con etiquetas origen y destino a una InfraEstructura
- Esta estructura es capaz de mirar los packetes, examinarlos y reenviarlos (reenrutar)
- Estan configurados con tablas (mapeo)
- EJ : “Todos los paquetes que empiezen con 120.algo … mandalos por este camino”
- Cada dispositivo router es capaz de tomar cualqueir paquete, y rutearlo al camino correcto
- PACKET SWITCHING
- ROUTER: Almacena Paquetes
- Examina Paquetes y determina punto de envio (FORWARD)
- Usa Tablas de reenvio (FORWARDING TABLES
- Estos routers tienen una memoria (limitada), si la cola de procesos se llena, decimos que esta congestionado, pero si tenemos varios buffers, podemos enrutar el camino atravez de distintas rutas
- Si tengo mas routers, es mas fácil de manejar la congesiton !!!
- N Saltos (en cada enlace)
- La competencia, es la red (telefonica) o red de INTERCAMBIO DE CIRCUITOS
- CIRCUIT SWITCHING
- En vez de enviar paquetes, se buscan caminos para elegir rutas
- Cada router tiene entradas / salidas
- Cada vez que llamo, la conexion no es instantanea, se genera primero el circuito y luego con ese delay, se establece la conexion
- Es muy SENSIBLE A CONGESTIONES , ej: Cuando hay terremotos, se saturan estas vias

> [!warning] Posible error
> En los apuntes aparecen erratas en `trasnmicion` (transmisión), `packetes` (paquetes) y `congesiton` (congestión). Además, el término estándar en redes es **conmutación de circuitos**, no "intercambio de circuitos".

> [!tip] Complemento: Comparación arquitectónica de Packet Switching frente a Circuit Switching
> 1. **Retardo de transmisión (*Transmission Delay*):**
>    $$d_{\text{trans}} = \frac{L}{R}$$
>    Donde $L$ es la longitud del paquete en bits y $R$ es la tasa de transmisión del enlace (*bandwidth*) en bits por segundo ($\text{bps}$).
> 2. **Conmutación de paquetes (*Packet Switching*):**
>    ![Conmutación de paquetes packet switching y tablas de reenvío](adjuntos/Conmutación%20de%20paquetes%20packet%20switching%20y%20tablas%20de%20reenvío.png)
>    ![Colas de espera en routers y pérdida de paquetes por congestión](adjuntos/Colas%20de%20espera%20en%20routers%20y%20pérdida%20de%20paquetes%20por%20congestión.png)
>    > [!example]- Transcripción de las imágenes
>    > **Mecanismo de Store-and-Forward y colas en Packet Switching:**
>    > - Los routers almacenan el paquete completo antes de comenzar a transmitir el primer bit al siguiente enlace (*almacenar y reenviar*).
>    > - **Tablas de reenvío (*Forwarding Tables*):** mapean prefijos de dirección IP de destino a interfaces de salida físicas.
>    > - **Colas y pérdida de paquetes (*Packet Loss*):** si la tasa de llegada de paquetes excede la capacidad de salida del enlace, los paquetes esperan en búferes de memoria (*queues*). Si la cola se llena (*buffer overflow*), los paquetes excedentes se descartan irrevocablemente.
>
> 3. **Conmutación de circuitos (*Circuit Switching*):**
>    ![Conmutación de circuitos circuit switching y reserva de recursos](adjuntos/Conmutación%20de%20circuitos%20circuit%20switching%20y%20reserva%20de%20recursos.png)
>    > [!example]- Transcripción de la imagen
>    > **Reserva dedicada de circuitos:**
>    > - Se establece un canal físico o lógico exclusivo de extremo a extremo (*end-to-end*) antes de iniciar la transmisión (retardo de establecimiento o *call setup*).
>    > - Recursos garantizados mediante multiplexación por división de frecuencia (FDM) o división de tiempo (TDM).
>    > - Si el circuito está inactivo durante la llamada, los recursos reservados se desperdician (*idle capacity*). Si todos los circuitos están ocupados, nuevas solicitudes son bloqueadas de inmediato.

## Preguntas de repaso

> [!question]- ¿Por qué Internet eligió la conmutación de paquetes (*Packet Switching*) en lugar de la conmutación de circuitos (*Circuit Switching*)?
> Porque la conmutación de paquetes ofrece un uso mucho más eficiente y elástico de la capacidad de los enlaces para tráfico a ráfagas (*bursty traffic*), comparte dinámicamente los recursos entre múltiples usuarios sin necesidad de reserva previa dedicada, y permite una alta resiliencia ante caídas de nodos enrutando por rutas alternativas.

> [!question]- ¿Cómo se calcula el tiempo necesario para transmitir un paquete de $1500\text{ bytes}$ a través de un enlace de $100\text{ Mbps}$?
> Convertimos bytes a bits: $L = 1500 \times 8 = 12000\text{ bits}$. La tasa de transmisión es $R = 100 \times 10^6\text{ bps}$. El retardo de transmisión es $d_{\text{trans}} = \frac{12000}{10^8}\text{ s} = 0.00012\text{ s} = 0.12\text{ ms} = 120\text{ }\mu\text{s}$.

> [!question]- ¿Qué ocurre en un router de conmutación de paquetes cuando el búfer de entrada o salida se llena por congestión?
> El router descarta los nuevos paquetes entrantes (*packet drop* o descarte de paquetes). La recuperación y retransmisión de los paquetes perdidos debe ser gestionada por capas superiores de la pila de protocolos (como TCP en la capa de transporte).

