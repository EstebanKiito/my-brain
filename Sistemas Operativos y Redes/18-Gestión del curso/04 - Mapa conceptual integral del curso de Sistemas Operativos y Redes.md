---
ramo: "Sistemas Operativos y Redes"
tema: "Gestión del curso"
tags:
  - sistemas-operativos
  - redes
  - gestion-curso
  - mapa-conceptual
  - sintesis
prerrequisitos:
  - "[[18-Gestión del curso/03 - Síntesis de sincronización, memoria y archivos para el Midterm|03 - Síntesis de sincronización, memoria y archivos para el Midterm]]"
---

# Mapa conceptual integral del curso de Sistemas Operativos y Redes

El curso de **Sistemas Operativos y Redes (IIC2333)** ofrece una visión unificada de cómo el software interactúa con el hardware para administrar recursos de cómputo en un solo equipo y cómo múltiples equipos autónomos se coordinan a través de una red global para intercambiar información de manera confiable y segura.

---

## Estructura dual del curso

El programa académico se estructura en dos grandes mitades complementarias:

### Parte 1: Sistemas Operativos (El computador individual)

1. **Abstracción del Hardware y Arquitectura**:
   - [[01-Estructura de sistemas operativos/_Índice|Estructura de sistemas operativos]]: Modos duales de CPU (Kernel vs Usuario), llamadas al sistema (*syscalls*), y tipos de núcleos (monolítico vs microkernel).
2. **Unidades de Ejecución y Planificación**:
   - [[02-Procesos/_Índice|Procesos]]: Modelo de memoria de un proceso, bloque PCB, llamadas `fork`, `exec` y `wait`, y ciclo de vida.
   - [[03-Planificación de CPU/_Índice|Planificación de CPU]]: Métricas de rendimiento, algoritmos FCFS, SJF, Round Robin y colas multinivel retroalimentadas (MLFQ).
   - [[04-Señales e IPC/_Índice|Señales e IPC]]: Notificaciones asíncronas, señales POSIX (SIGTERM, SIGKILL, SIGINT) y tuberías (*pipes*).
   - [[05-Hilos/_Índice|Hilos]]: Concurrencia liviana, recursos compartidos vs privados, modelos de hilos a nivel de usuario y kernel.
3. **Coordinación y Sincronización**:
   - [[06-Sincronización/_Índice|Sincronización]]: Condiciones de carrera, exclusión mutua, primitivas atómicas, mutex, semáforos contadores, variables de condición y prevención de deadlocks.
4. **Espacio de Direcciones y Memoria**:
   - [[07-Administración de memoria/_Índice|Administración de memoria]]: Relocalización dinámica, registros base y límite, fragmentación y algoritmos de particionamiento.
   - [[08-Paginación y segmentación/_Índice|Paginación y segmentación]]: Páginas y marcos (*frames*), tablas de páginas multinivel, TLB y paginación invertida.
   - [[09-Memoria virtual/_Índice|Memoria virtual]]: Paginación por demanda, espacio swap, fallo de página y algoritmos de reemplazo (FIFO, LRU, Clock).
5. **Persistencia y Almacenamiento Secundario**:
   - [[10-Sistemas de archivos/_Índice|Sistemas de archivos]]: Abstracción de archivos y directorios, geometrías físicas HDD vs SSD, y planificación de cabezal.
   - [[11-Implementación de archivos y bloques/_Índice|Implementación de archivos y bloques]]: Inodos UNIX, asignación indexada multinivel, enlaces duros vs simbólicos y gestión de bloques libres.

---

### Parte 2: Redes de Computadores (La comunicación distribuida)

1. **Arquitectura y Modelos en Capas**:
   - [[12-Fundamentos de redes y modelos en capas/_Índice|Fundamentos de redes y modelos en capas]]: Modelo OSI de 7 capas vs suite TCP/IP de 5 capas, conmutación de paquetes y retardos.
2. **Capa de Aplicación**:
   - [[13-Capa de aplicación y sockets/_Índice|Capa de aplicación y sockets]]: Programación de sockets TCP y UDP, protocolo HTTP, caché, cookies, arquitectura DNS y redes P2P BitTorrent.
3. **Capa de Transporte**:
   - [[14-Capa de transporte/_Índice|Capa de transporte]]: Multiplexación por puertos, protocolo UDP, principios de transferencia confiable (rdt), ventanas deslizantes (Go-Back-N, Selective Repeat) y protocolo TCP con control de flujo y 3-way handshake.
4. **Capa de Red**:
   - [[15-Capa de red y direccionamiento/_Índice|Capa de red y direccionamiento]]: Datagrama IPv4, direccionamiento CIDR, máscaras de subred, DHCP, NAT, ICMP y transición a IPv6.
   - [[16-Algoritmos de ruteo/_Índice|Algoritmos de ruteo]]: Grafos y algoritmos Link-State (Dijkstra) vs Distance-Vector (Bellman-Ford), conteo al infinito y enrutamiento jerárquico BGP entre Sistemas Autónomos.
5. **Capa de Enlace y Seguridad**:
   - [[17-Capa de enlace y seguridad/_Índice|Capa de enlace y seguridad]]: Control de acceso al medio (MAC, CSMA/CD), direcciones MAC, protocolo ARP, tramas Ethernet, conmutadores L2, STP, VLANs y fundamentos de seguridad defensiva.

---

## Preguntas de repaso

> [!question]- ¿Cómo se relacionan los sockets de la capa de aplicación con las llamadas al sistema del sistema operativo?
> Los sockets son descriptores de archivos virtuales administrados por el kernel del sistema operativo. Una aplicación interactúa con la red invocando llamadas al sistema como `socket()`, `bind()`, `listen()`, `accept()`, `send()` y `recv()`, transfiriendo el control al modo kernel para que la pila de red del SO ensamble las cabeceras TCP/IP y gestione los buffers de la tarjeta de red.

> [!question]- ¿Qué principio común comparten la memoria virtual y el enrutamiento jerárquico de Internet?
> Ambos aplican el principio de **desacoplamiento lógico de la realidad física mediante tablas y jerarquías**: la memoria virtual permite a los procesos operar con direcciones lógicas contiguas ignorando la fragmentación de la RAM física, mientras que los Sistemas Autónomos (AS) y el direccionamiento CIDR permiten enrutar paquetes globalmente agrupando millones de direcciones en prefijos jerárquicos compactos.

> [!question]- ¿Por qué tanto los sistemas operativos como las redes basan su diseño en modelos de capas abstractas?
> Porque la abstracción por capas desacopla la complejidad: permite modificar o mejorar la implementación de un nivel (por ejemplo, cambiar de HDD a SSD en almacenamiento, o de Wi-Fi a fibra óptica en capa de enlace) sin alterar los contratos ni el código de las capas superiores.
