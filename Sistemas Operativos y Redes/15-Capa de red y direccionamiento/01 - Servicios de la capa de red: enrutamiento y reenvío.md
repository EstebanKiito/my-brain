---
ramo: "Sistemas Operativos y Redes"
tema: "Capa de red y direccionamiento"
tags:
  - sistemas-operativos
  - redes
  - capa-de-red
  - enrutamiento
  - reenvio
  - forwarding
prerrequisitos:
  - "[[14-Capa de transporte/_Índice|Capa de transporte]]"
---

# Servicios de la capa de red: enrutamiento y reenvío

La capa de red (Capa 3 de los modelos OSI y TCP/IP) es responsable de la transferencia de paquetes de datos (datagramas) desde el host emisor hasta el host receptor a través de una malla arbitraria de conmutadores y enrutadores intermedios. Su arquitectura se divide conceptualmente en dos planos: el **plano de datos** (acción local de reenvío o *forwarding*) y el **plano de control** (cálculo global de rutas o *routing*).

---

## Retos y funciones de la capa de red (mis apuntes)

### CLASE 6
23/10/24

### CONTENIDO 11 → CAPA DE RED

https://www.youtube.com/watch?v=syQOSjc-7NY&list=PLVTkEjeczcER2aOMHPIfaHCpTx61iKsoV&index=65

Esta capa esta encargada de:
- Un Mensaje sea Dirigido → Encuentre al servidor
- La capa de Red ocurre en cada uno de los dispositivos INTERMEDIOS
- Observar en el diagrama, que los dispositivos intermedios (Routers), llegan hasta la capa de NETWORK (RED)
- Va saltando entre elementos intermedios

![Funciones de la capa de red: enrutamiento en plano de control y reenvío en plano de datos](adjuntos/Funciones%20de%20la%20capa%20de%20red:%20enrutamiento%20en%20plano%20de%20control%20y%20reenv%C3%ADo%20en%20plano%20de%20datos.png)

> [!example]- Transcripción de la imagen
> Separación entre Reenvío (*Forwarding*) y Enrutamiento (*Routing*):
> - **Reenvío (Data Plane)**: Acción local y acelerada por hardware en cada router de transferir un paquete desde un enlace de entrada hacia el enlace de salida apropiado según la tabla de reenvío (*Forwarding Table*).
> - **Enrutamiento (Control Plane)**: Proceso global coordinado mediante algoritmos de enrutamiento (OSPF, BGP) que determina las rutas completas extremo a extremo a través de la red y programa las tablas de reenvío.

Capa de red resuelve 2 desafios : DIRECCIONAMIENTO y ENRUTAMIENTO
Direccionamiento → Como encontrar la ubicacion del nodo destino en la red
Enrutamiento → Cordinar routers para que el pkte llegue al destino
Para realizar esto → Routers poseen un modelo STORE - FORWARD

STORE FORWARD: Almacenamiento y reenvio
- Cada router determina el proximo camino de un paquete mirando su direccion de destino
- Se usa una tabla de forwarding → Tabla local → Ve headers y ve a donde salir
- Cada tabla es unica por router
- Forwarding: Decision local de un router
- Estos algoritmos, permiten llenar la forwarding tables
- Enrutamiento (Routing): Decisión distribuida entre routers, ellos ejecutan algoritmo de routing

> [!tip] Complemento de clase: El paradigma Store-and-Forward
> En *Store-and-Forward*, un router debe recibir el datagrama completo en su búfer de entrada antes de poder comenzar a retransmitir el primer bit hacia el enlace de salida. Esto introduce un retardo de transmisión por cada salto de router: $d_{\text{extremo}} = N \cdot \frac{L}{R}$ (donde $N$ es el número de enlaces idénticos).

---

## Preguntas de repaso

> [!question]- ¿Cuál es la diferencia técnica entre *forwarding* (reenvío) y *routing* (enrutamiento)?
> El reenvío (*forwarding*) es una acción local, por paquete, que toma nanosegundos en hardware para transferir un datagrama de un puerto de entrada a uno de salida; el enrutamiento (*routing*) es el proceso de cómputo global de rutas ejecutado en el plano de control (por software) que puebla las tablas de reenvío.

> [!question]- ¿Por qué la capa de red de Internet opera bajo un servicio de "mejor esfuerzo" (*best-effort*)?
> Porque no ofrece garantías de entrega oportuna, orden ni ancho de banda; esta simplicidad extrema en el núcleo de la red permitió la interconexión masiva de tecnologías heterogéneas, delegando la confiabilidad a la capa de transporte en los extremos.

> [!question]- ¿Qué ocurre en un router cuando su memoria búfer de entrada o salida se llena por congestión?
> Se produce pérdida de paquetes (*packet drop* o descarte de paquetes); las políticas clásicas descartan los datagramas entrantes (*Tail Drop*) o aplican detección temprana aleatoria (RED, *Random Early Detection*).

