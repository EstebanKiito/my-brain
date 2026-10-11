# Sistemas Operativos y Redes (IIC2333) — mapa del curso

Vault de estudio del ramo. Cada nota cubre **un concepto atómico**: no hace falta saber en qué clase se vio, basta con buscar el concepto directamente. Dentro de cada carpeta temática, el número del archivo indica el orden pedagógico de lectura.

## Cómo están hechas las notas
- **Frontmatter:** `ramo`, `tema`, `tags` (`origen/apuntes` = parte de los apuntes originales de Notion; `origen/complemento` = nota complementaria) y `prerrequisitos` (conceptos recomendados para leer antes).
- **Cuerpo:** primero el texto textual de los apuntes; los complementos técnicos (diapositivas oficiales del curso, libros de referencia de Tanenbaum, Silberschatz, OSTEP y Kurose-Ross) van siempre en callouts `[!tip] Complemento` o `[!example]`.
- **Imágenes:** los diagramas originales y slides en PNG, todas con su transcripción textual en un callout plegable `[!example]- Transcripción de la imagen`.
- **Errores detectados:** van en callouts `[!warning] Posible error` y quedan registrados en `_meta/Sistemas Operativos y Redes/DUDAS.md`.
- **Cierre:** cada nota termina con **Preguntas de repaso** conceptuales, con la respuesta oculta en un callout plegable `[!question]- Respuesta`.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Sistemas Operativos y Redes/Estructura de sistemas operativos/_Índice\|Estructura de sistemas operativos]] | Qué es un SO, modos de operación (dual-mode, Ring 0 a 3), kernel monolítico vs microkernel, interrupciones, syscalls, arranque (BIOS/UEFI, GRUB) y multitasking |
| [[Sistemas Operativos y Redes/Procesos/_Índice\|Procesos]] | Concepto de proceso, espacio de memoria (text, data, heap, stack), PCB, estados, cambio de contexto, creación con fork/exec/wait |
| Planificación de CPU *(pendiente)* | Criterios y métricas, algoritmos FIFO, SJF, STCF, Round Robin, colas multinivel con retroalimentación (MLFQ) |
| Señales e IPC *(pendiente)* | Señales UNIX, handlers, máscaras, pipes y comunicación entre procesos |
| Hilos *(pendiente)* | Threads vs procesos, espacio compartido, hilos de usuario vs kernel, modelos de threading y POSIX threads |
| Sincronización *(pendiente)* | Condiciones de carrera, sección crítica, exclusión mutua, hardware (Test-and-Set), mutex, semáforos, problemas clásicos y deadlocks |
| Administración de memoria *(pendiente)* | Jerarquía de memoria, direcciones lógicas vs físicas, MMU, registros base y límite, particiones y fragmentación |
| Paginación y segmentación *(pendiente)* | Segmentos, páginas y marcos, tabla de páginas, TLB, tiempo efectivo de acceso, paginación multinivel |
| Memoria virtual *(pendiente)* | Paginación por demanda, fallos de página (page faults), algoritmos de reemplazo (FIFO, Belady, Óptimo, LRU, Clock) y thrashing |
| Sistemas de archivos *(pendiente)* | Archivos, operaciones, discos magnéticos y SSDs, particionamiento, formateo lógico y estructura de directorios |
| Implementación de archivos y bloques *(pendiente)* | Hard links vs symlinks, asignación contigua, enlazada e indexada (inodos UNIX), gestión de espacio libre |
| Fundamentos de redes y modelos en capas *(pendiente)* | Modelos OSI y TCP/IP, ancho de banda, latencia, encapsulación y arquitectura de Internet |
| Capa de aplicación y sockets *(pendiente)* | Sockets TCP y UDP, protocolos HTTP, FTP, DNS y arquitectura cliente-servidor |
| Capa de transporte *(pendiente)* | Puertos, multiplexación, protocolo UDP, TCP, three-way handshake, control de flujo y control de congestión |
| Capa de red y direccionamiento *(pendiente)* | Direccionamiento IPv4 y IPv6, máscaras de subred, CIDR, DHCP, NAT e ICMP |
| Algoritmos de ruteo *(pendiente)* | Ruteo intra-dominio e inter-dominio, algoritmos Link-State (Dijkstra) y Distance-Vector (Bellman-Ford), BGP |
| Capa de enlace y seguridad *(pendiente)* | Tramas, direcciones MAC, Ethernet, switches, protocolo ARP, CSMA/CD y fundamentos de seguridad |
| Gestión del curso *(pendiente)* | Evaluaciones, tareas, resumen midterm y preparación para exámenes |

## Ruta de estudio sugerida
1. **Estructura de sistemas operativos → Procesos → Hilos:** La base del sistema, cómo se pasa a modo kernel y cómo se ejecutan las unidades de computación.
2. **Planificación de CPU → Sincronización:** Cómo decide la CPU qué ejecutar y cómo evitar que procesos e hilos concurrentes corrompan datos compartidos.
3. **Administración de memoria → Paginación y segmentación → Memoria virtual:** Toda la gestión del espacio de direcciones, desde la MMU hasta el swap en disco.
4. **Sistemas de archivos → Implementación de archivos y bloques:** Cómo se persisten los datos en almacenamiento secundario.
5. **Fundamentos de redes → Capa de aplicación → Capa de transporte → Capa de red → Algoritmos de ruteo → Capa de enlace:** El viaje completo bajando por la pila de protocolos de Internet.

