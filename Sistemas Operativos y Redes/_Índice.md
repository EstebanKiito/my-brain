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
| [[Sistemas Operativos y Redes/01-Estructura de sistemas operativos/_Índice\|Estructura de sistemas operativos]] | Qué es un SO, modos de operación (dual-mode, Ring 0 a 3), kernel monolítico vs microkernel, interrupciones, syscalls, arranque (BIOS/UEFI, GRUB) y multitasking |
| [[Sistemas Operativos y Redes/02-Procesos/_Índice\|Procesos]] | Concepto de proceso, espacio de memoria (text, data, heap, stack), PCB, estados, cambio de contexto, creación con fork/exec/wait |
| [[Sistemas Operativos y Redes/03-Planificación de CPU/_Índice|Planificación de CPU]] | Niveles de planificación (largo, mediano y corto plazo), métricas, FCFS, SJF, Round Robin y colas multinivel con retroalimentación (MLFQ) |
| [[Sistemas Operativos y Redes/04-Señales e IPC/_Índice|Señales e IPC]] | Señales UNIX (SIGINT, SIGTERM, SIGKILL, SIGSTOP, SIGCONT), handlers en C, máscaras e introducción a IPC (pipes) |
| [[Sistemas Operativos y Redes/05-Hilos/_Índice|Hilos]] | Threads vs procesos, recursos compartidos vs privados, estándar POSIX Threads (pthreads), hilos en espacio de usuario vs kernel |
| [[Sistemas Operativos y Redes/06-Sincronización/_Índice|Sincronización]] | Condiciones de carrera, sección crítica, exclusión mutua, hardware (Test-and-Set), mutex, semáforos, problemas clásicos y deadlocks |
| [[Sistemas Operativos y Redes/07-Administración de memoria/_Índice|Administración de memoria]] | Jerarquía de memoria, direcciones lógicas vs físicas, MMU, registros base y límite, particiones y fragmentación |
| [[Sistemas Operativos y Redes/08-Paginación y segmentación/_Índice|Paginación y segmentación]] | Segmentos, páginas y marcos, tabla de páginas, TLB, tiempo efectivo de acceso, paginación multinivel |
| [[Sistemas Operativos y Redes/09-Memoria virtual/_Índice|Memoria virtual]] | Paginación por demanda, fallos de página (page faults), algoritmos de reemplazo (FIFO, Belady, Óptimo, LRU, Clock) y thrashing |
| [[Sistemas Operativos y Redes/10-Sistemas de archivos/_Índice|Sistemas de archivos]] | Archivos, operaciones, discos magnéticos y SSDs, particionamiento, formateo lógico y estructura de directorios |
| [[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/_Índice|Implementación de archivos y bloques]] | Hard links vs symlinks, asignación contigua, enlazada e indexada (inodos UNIX), gestión de espacio libre |
| [[Sistemas Operativos y Redes/12-Fundamentos de redes y modelos en capas/_Índice|Fundamentos de redes y modelos en capas]] | Modelos OSI y TCP/IP, ancho de banda, latencia, encapsulación y arquitectura de Internet |
| [[Sistemas Operativos y Redes/13-Capa de aplicación y sockets/_Índice|Capa de aplicación y sockets]] | Sockets TCP y UDP, llamadas al sistema, protocolos HTTP, FTP, DNS, cookies, y redes P2P BitTorrent |
| [[Sistemas Operativos y Redes/14-Capa de transporte/_Índice|Capa de transporte]] | Puertos, multiplexación, protocolo UDP, evolución rdt, Go-Back-N, Selective Repeat y TCP con 3-way handshake |
| [[Sistemas Operativos y Redes/15-Capa de red y direccionamiento/_Índice|Capa de red y direccionamiento]] | Direccionamiento IPv4 y IPv6, fragmentación por MTU, máscaras, CIDR, DHCP, NAT e ICMP |
| [[Sistemas Operativos y Redes/16-Algoritmos de ruteo/_Índice|Algoritmos de ruteo]] | Ruteo intra-dominio e inter-dominio, Link-State (Dijkstra), Distance-Vector (Bellman-Ford), y Sistemas Autónomos |
| [[Sistemas Operativos y Redes/17-Capa de enlace y seguridad/_Índice|Capa de enlace y seguridad]] | Tramas, direcciones MAC, Ethernet, switches, protocolo ARP, CSMA/CD y fundamentos de seguridad |
| [[Sistemas Operativos y Redes/18-Gestión del curso/_Índice|Gestión del curso]] | Evaluaciones, tareas, resumen midterm y preparación para exámenes |

## Ruta de estudio sugerida
1. **Estructura de sistemas operativos → Procesos → Hilos:** La base del sistema, cómo se pasa a modo kernel y cómo se ejecutan las unidades de computación.
2. **Planificación de CPU → Sincronización:** Cómo decide la CPU qué ejecutar y cómo evitar que procesos e hilos concurrentes corrompan datos compartidos.
3. **Administración de memoria → Paginación y segmentación → Memoria virtual:** Toda la gestión del espacio de direcciones, desde la MMU hasta el swap en disco.
4. **Sistemas de archivos → Implementación de archivos y bloques:** Cómo se persisten los datos en almacenamiento secundario.
5. **Fundamentos de redes → Capa de aplicación → Capa de transporte → Capa de red → Algoritmos de ruteo → Capa de enlace:** El viaje completo bajando por la pila de protocolos de Internet.

