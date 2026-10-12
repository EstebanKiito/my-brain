# Progreso: estandarización de notas de Sistemas Operativos y Redes

Rama `fix/ssoo-redes`. Estándar en [ESTANDAR-NOTAS.md](ESTANDAR-NOTAS.md). Un commit por nota: `reescribe: <nota>`.

Estados: pendiente · reescrita · sin marca (no se toca) · saltada (motivo).

Notas con marca detectadas: 95 de 100.

Reescritas hasta ahora: 4 de 92 notas de concepto (95 marcadas menos 3 saltadas).
Última reescrita: 01-Estructura de sistemas operativos/02 - Modos de operación y anillos de protección.md. Para retomar, sigue con la próxima fila 'pendiente' de la tabla.

## Notas

| # | Nota | Estado | Observaciones |
|---|---|---|---|
| 1 | 01-Estructura de sistemas operativos/01 - Qué es un sistema operativo.md | reescrita (piloto) | 84 líneas; 2 imágenes; Mermaid ok; 1 duda |
| 2 | 01-Estructura de sistemas operativos/02 - Modos de operación y anillos de protección.md | reescrita | 79 líneas; 1 imagen; Mermaid ok |
| 3 | 01-Estructura de sistemas operativos/03 - Arquitecturas de kernel monolítico y microkernel.md | pendiente | |
| 4 | 01-Estructura de sistemas operativos/04 - Interrupciones y excepciones.md | pendiente | |
| 5 | 01-Estructura de sistemas operativos/05 - Llamadas al sistema.md | pendiente | |
| 6 | 01-Estructura de sistemas operativos/06 - Arranque del sistema computacional.md | reescrita (piloto) | 74 líneas; Mermaid ok |
| 7 | 01-Estructura de sistemas operativos/07 - Multitasking y fundamentos de multiprocesamiento.md | pendiente | |
| 8 | 02-Procesos/01 - Concepto de proceso y espacio de memoria.md | pendiente | |
| 9 | 02-Procesos/02 - Bloque de control de procesos y tabla de procesos.md | pendiente | |
| 10 | 02-Procesos/03 - Estados de un proceso y ciclo de vida.md | pendiente | |
| 11 | 02-Procesos/04 - Cambio de contexto y tipos de procesos.md | pendiente | |
| 12 | 02-Procesos/05 - Jerarquía y creación de procesos con fork.md | pendiente | |
| 13 | 02-Procesos/06 - Control de procesos con wait, exec y terminación.md | pendiente | |
| 14 | 02-Procesos/07 - Programación de procesos en C y prevención de fork bombs.md | reescrita (piloto) | 111 líneas; 2 imágenes; C compila y corre; 1 duda |
| 15 | 03-Planificación de CPU/01 - Niveles de planificación y ciclo de ráfagas CPU-IO.md | pendiente | |
| 16 | 03-Planificación de CPU/02 - Clasificación de planificadores y métricas de rendimiento.md | pendiente | |
| 17 | 03-Planificación de CPU/03 - Planificación FCFS y SJF.md | pendiente | |
| 18 | 03-Planificación de CPU/04 - Planificación Round Robin y sistemas interactivos.md | pendiente | |
| 19 | 03-Planificación de CPU/05 - Planificación por prioridad y colas multinivel (MLFQ).md | pendiente | |
| 20 | 04-Señales e IPC/01 - Concepto de señal y ciclo de vida de señales POSIX.md | pendiente | |
| 21 | 04-Señales e IPC/02 - Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT.md | pendiente | |
| – | 04-Señales e IPC/03 - Comunicación entre procesos y manejo de señales en C.md | sin marca | nota modelo |
| 22 | 05-Hilos/01 - Concepto de hilo y recursos compartidos versus privados.md | pendiente | |
| 23 | 05-Hilos/02 - Programación con POSIX Threads y ciclo de vida.md | pendiente | |
| 24 | 05-Hilos/03 - Hilos a nivel de usuario frente a hilos a nivel de kernel.md | pendiente | |
| 25 | 06-Sincronización/01 - Condiciones de carrera y el problema de la sección crítica.md | pendiente | |
| 26 | 06-Sincronización/02 - Soluciones por software y algoritmo de Peterson.md | pendiente | |
| 27 | 06-Sincronización/03 - Sincronización por hardware e instrucciones atómicas.md | pendiente | |
| 28 | 06-Sincronización/04 - Mutex locks y el dilema de busy waiting versus dormir.md | pendiente | |
| 29 | 06-Sincronización/05 - Problema del productor-consumidor y buffer acotado.md | pendiente | |
| 30 | 06-Sincronización/06 - Semáforos de Dijkstra y tipos de semáforos.md | pendiente | |
| 31 | 06-Sincronización/07 - Variables de condición y monitores.md | pendiente | |
| 32 | 06-Sincronización/08 - Problema de los lectores y escritores.md | pendiente | |
| 33 | 06-Sincronización/09 - Problema de los filósofos comelones y deadlocks.md | pendiente | |
| 34 | 07-Administración de memoria/01 - Coordinación de filósofos y manejo de estados con semáforos.md | pendiente | |
| 35 | 07-Administración de memoria/02 - Memoria principal y el desafío de la multiprogramación.md | pendiente | |
| 36 | 07-Administración de memoria/03 - Relocalización, protección de memoria y registros base y límite.md | pendiente | |
| 37 | 07-Administración de memoria/04 - Swapping, fragmentación externa y algoritmos de asignación libre.md | pendiente | |
| 38 | 07-Administración de memoria/05 - Segmentación de memoria y prevención de segmentation fault.md | pendiente | |
| 39 | 07-Administración de memoria/06 - Aritmética de bits y máscara de segmento en traducción de direcciones.md | pendiente | |
| 40 | 08-Paginación y segmentación/01 - Fundamentos de paginación, marcos y tabla de páginas.md | pendiente | |
| 41 | 08-Paginación y segmentación/02 - Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo.md | pendiente | |
| 42 | 08-Paginación y segmentación/03 - Localidad de referencia y gestión de TLB con ASID en cambios de contexto.md | pendiente | |
| 43 | 08-Paginación y segmentación/04 - Sobrecarga de tablas lineales y compromiso de fragmentación interna.md | pendiente | |
| 44 | 08-Paginación y segmentación/05 - Arquitectura de segmentos paginados.md | pendiente | |
| 45 | 08-Paginación y segmentación/06 - Paginación multinivel y tablas de páginas invertidas.md | pendiente | |
| 46 | 08-Paginación y segmentación/07 - Introducción al intercambio por demanda y ciclo de fallos de página.md | pendiente | |
| 47 | 09-Memoria virtual/01 - Fundamentos de memoria virtual y espacio de intercambio (swap).md | pendiente | |
| – | 09-Memoria virtual/02 - Algoritmos de reemplazo FIFO, Óptimo (Belady) y anomalía de Belady.md | sin marca | nota modelo |
| – | 09-Memoria virtual/03 - Algoritmo LRU e implementaciones con hardware y software.md | sin marca | nota modelo |
| – | 09-Memoria virtual/04 - Algoritmo del reloj (Clock) y aproximaciones prácticas de LRU.md | sin marca | nota modelo |
| 48 | 10-Sistemas de archivos/01 - Capas de abstracción de entrada-salida y mecanismos de buffering.md | pendiente | |
| 49 | 10-Sistemas de archivos/02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD).md | pendiente | |
| 50 | 10-Sistemas de archivos/03 - Niveles de formateo y esquemas de particionamiento (MBR y GPT).md | pendiente | |
| 51 | 10-Sistemas de archivos/04 - Algoritmos de planificación de disco (Disk Scheduling).md | pendiente | |
| 52 | 10-Sistemas de archivos/05 - Concepto de archivo, atributos y metadatos.md | pendiente | |
| 53 | 10-Sistemas de archivos/06 - Estructura de directorios y resolución de rutas.md | pendiente | |
| 54 | 11-Implementación de archivos y bloques/01 - Interfaz y llamadas al sistema de archivos y directorios.md | pendiente | |
| 55 | 11-Implementación de archivos y bloques/02 - Enlaces duros (hard links) y enlaces simbólicos (soft links).md | pendiente | |
| 56 | 11-Implementación de archivos y bloques/03 - Montaje de sistemas de archivos y puntos de montaje.md | pendiente | |
| 57 | 11-Implementación de archivos y bloques/04 - Estructuras en disco y en memoria del sistema de archivos virtual (VFS).md | pendiente | |
| 58 | 11-Implementación de archivos y bloques/05 - Métodos de asignación de bloques: asignación contigua y bloques de control.md | pendiente | |
| 59 | 11-Implementación de archivos y bloques/06 - Asignación enlazada y tabla de asignación de archivos (FAT).md | pendiente | |
| 60 | 11-Implementación de archivos y bloques/07 - Asignación indexada y arquitectura de inodos multinivel en Unix.md | pendiente | |
| 61 | 11-Implementación de archivos y bloques/08 - Administración del espacio libre en disco: mapas de bits y listas enlazadas.md | pendiente | |
| 62 | 12-Fundamentos de redes y modelos en capas/01 - Arquitectura de Internet, nodos, enlaces y protocolos.md | pendiente | |
| 63 | 12-Fundamentos de redes y modelos en capas/02 - Redes de acceso y medios físicos de transmisión.md | pendiente | |
| 64 | 12-Fundamentos de redes y modelos en capas/03 - Conmutación de paquetes frente a conmutación de circuitos.md | pendiente | |
| 65 | 12-Fundamentos de redes y modelos en capas/04 - Modelos de capas: modelo de referencia OSI frente al stack TCP-IP.md | pendiente | |
| 66 | 12-Fundamentos de redes y modelos en capas/05 - Capas de transporte, red, enlace y física.md | pendiente | |
| 67 | 12-Fundamentos de redes y modelos en capas/06 - Proceso de encapsulamiento y flujo de datos en la red.md | pendiente | |
| 68 | 13-Capa de aplicación y sockets/01 - Arquitecturas de aplicación y modelos de comunicación.md | pendiente | |
| 69 | 13-Capa de aplicación y sockets/02 - Concepto de socket e identificación por IP y puerto.md | pendiente | |
| 70 | 13-Capa de aplicación y sockets/03 - Sockets UDP y TCP: modelos y llamadas al sistema.md | pendiente | |
| 71 | 13-Capa de aplicación y sockets/04 - Protocolo HTTP, formato de mensajes y estado con cookies.md | pendiente | |
| 72 | 13-Capa de aplicación y sockets/05 - Sistema de nombres de dominio (DNS) y resolución de consultas.md | pendiente | |
| 73 | 13-Capa de aplicación y sockets/06 - Redes Peer-to-Peer (P2P) y distribución con BitTorrent.md | pendiente | |
| 74 | 14-Capa de transporte/01 - Servicios de la capa de transporte y estructura de segmentos.md | pendiente | |
| 75 | 14-Capa de transporte/02 - Multiplexación y desmultiplexación de puertos en UDP y TCP.md | pendiente | |
| 76 | 14-Capa de transporte/03 - Protocolo UDP: datagramas, sobrecarga y checksum.md | pendiente | |
| 77 | 14-Capa de transporte/04 - Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0).md | pendiente | |
| 78 | 14-Capa de transporte/05 - Protocolos de canalización: Go-Back-N y Selective Repeat.md | pendiente | |
| 79 | 14-Capa de transporte/06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa.md | pendiente | |
| 80 | 14-Capa de transporte/07 - Gestión de temporizadores, retransmisión rápida y handshake en TCP.md | pendiente | |
| 81 | 15-Capa de red y direccionamiento/01 - Servicios de la capa de red: enrutamiento y reenvío.md | pendiente | |
| 82 | 15-Capa de red y direccionamiento/02 - Datagrama IPv4: estructura y fragmentación por MTU.md | pendiente | |
| 83 | 15-Capa de red y direccionamiento/03 - Direccionamiento IPv4: subredes, máscaras y notación CIDR.md | pendiente | |
| 84 | 15-Capa de red y direccionamiento/04 - Configuración dinámica con DHCP y traducción de direcciones NAT.md | pendiente | |
| 85 | 15-Capa de red y direccionamiento/05 - Protocolo ICMP y transición a IPv6: dual-stack y tunneling.md | pendiente | |
| 86 | 16-Algoritmos de ruteo/01 - Modelos de grafo y algoritmos Link-State (Dijkstra).md | pendiente | |
| 87 | 16-Algoritmos de ruteo/02 - Algoritmos Distance-Vector (Bellman-Ford) y conteo al infinito.md | pendiente | |
| 88 | 16-Algoritmos de ruteo/03 - Enrutamiento jerárquico y sistemas autónomos (Intra-AS e Inter-AS).md | pendiente | |
| 89 | 17-Capa de enlace y seguridad/01 - Servicios de capa de enlace y control de acceso al medio (MAC).md | pendiente | |
| 90 | 17-Capa de enlace y seguridad/02 - Direcciones MAC, protocolo ARP y trama Ethernet.md | pendiente | |
| 91 | 17-Capa de enlace y seguridad/03 - Conmutación en redes locales (Switches L2, STP) y VLANs.md | pendiente | |
| 92 | 17-Capa de enlace y seguridad/04 - Fundamentos de seguridad en redes: amenazas, ataques y defensas.md | pendiente | |
| 93 | 18-Gestión del curso/01 - Estructura de evaluaciones y preparación del Midterm.md | saltada: no es concepto de estudio (logística/síntesis); decide tú | |
| 94 | 18-Gestión del curso/02 - Síntesis de procesos, hilos y planificación para el Midterm.md | saltada: no es concepto de estudio (logística/síntesis); decide tú | |
| 95 | 18-Gestión del curso/03 - Síntesis de sincronización, memoria y archivos para el Midterm.md | saltada: no es concepto de estudio (logística/síntesis); decide tú | |
| – | 18-Gestión del curso/04 - Mapa conceptual integral del curso de Sistemas Operativos y Redes.md | sin marca | nota modelo |

## Advertencias

- **Piloto:** primero se hacen solo 3 notas, una de cada tipo: 01/06 (conceptual), 01/01 (con imagen) y 02/07 (con código). Después se sigue en orden desde 01/02, saltando las ya reescritas.
- **Commit de estado previo:** no se hizo porque `git add -u` no tenía nada que agregar. Los temas `.obsidian/themes/Catppuccin/` y `Composer/` no se tocaron.
- **`_meta/cache/`** no estaba en `.gitignore` y se agregó. Contiene el texto extraído de los 12 PDFs del ramo con `pdftotext -layout`.
- **`imagenes.json`:** la entrada de `image 70.png` (tema Capa de enlace y seguridad) usaba `origen` en vez de `original` y no tenía `tipo`. Por eso `verificar.py` se caía con `KeyError: 'tipo'` y la prueba 5 nunca corría. Se corrigió solo ese dato; `verificar.py` no se modificó.
- **Línea base del verificador** (después de la corrección): 4 errores previos, todos imágenes `.heic` de RESUMEN MIDTERM SSOO sin destino (tema Gestión del curso). Las notas reescritas no deben sumar errores en las pruebas [1], [2] ni [5]. La prueba [3] (cobertura textual) falla a propósito, porque ya no se copia literal.
- **Mermaid:** se valida con `mermaid.parse` (mermaid + jsdom instalados en el scratchpad de la sesión, fuera del repo).
- **Semáforos en macOS:** `sem_init` (semáforos sin nombre) no funciona en macOS. El código de las notas queda en POSIX estándar; la lógica se prueba una sola vez con una variante para macOS.
- **DUDAS.md:** su encabezado dice "el texto original se conserva tal cual", lo que deja de ser cierto en las notas reescritas. No se cambió; decide tú. Las filas antiguas quedan como historial.
- **`Sistemas Operativos y Redes/_Índice.md`** describe el tag `origen/apuntes`. Al terminar ninguna nota de concepto lo tendrá. No se tocó (regla: no tocar _Índice).
- **Nota modelo 04/03** (sin marca, no se tocó): el ejemplo llama `printf` dentro del handler de `SIGINT`, y su propia pregunta de repaso dice que no se debe.
- **Notas modelo:** citan nombre de PDF y página en las transcripciones. Las notas reescritas no lo hacen.

## Registro por nota

- **01/06 Arranque** (conceptual): 74 líneas, 1 Mermaid (parse ok), 1 tabla. Reincorporados: PC y firmware en ROM/NVRAM, `vmlinuz`, `initramfs`, `grubx64.efi`, GUID, ring 0. Omitido: "ejecutables de 64 bits" (UEFI de 32 bits también existe). Sin dudas nuevas.
- **01/01 Qué es un SO** (con imagen): 84 líneas, 2 imágenes comprobadas (Tanenbaum fig. 1-1 y estructura user/kernel space), 1 Mermaid (parse ok), 1 tabla de roles. Reincorporados: *resource manager*, *extended machine*, SysV init de UNIX. Ignorados: fecha y encabezado "CLASE". El rol de "programa de control" se completó desde el material de clase. Duda nueva 🟡: "manejo de memoria = dónde se guardan las descargas". "Scheduling: elegir quién va a estar en la RAM" calza con el scheduler de largo plazo del material de clase, así que no es duda.
- **02/07 Programación de procesos en C** (con código): 111 líneas, 2 imágenes comprobadas. Código: el programa completo (struct/enum + fork/exit/waitpid) y el fragmento de `exec` (`expr 6 * 7` → 42) compilan sin avisos con `gcc -Wall -pthread` y corren bien; el conteo exponencial (3 `fork` en un for → 8 procesos) también se comprobó. La fork bomb de Bash se documenta pero, a propósito, no se ejecutó. Erratas corregidas sin comentar: `structs`/`Sates`, `argv` descrito como "cantidad de líneas" (ahora `argc`/`argv`), "exec es un archivo .c" (ahora: un ejecutable). Se quitaron los recordatorios "Estudiar", la fecha y las referencias a la tarea. El complemento antiguo atribuía fork bomb y `ulimit` a las diapositivas, pero no aparecen en ellas; se conserva como conocimiento general. Duda nueva 🟡: "el hijo solo ejecuta la línea de comandos".
- **01/02 Modos de operación**: 81 líneas, 1 imagen comprobada, 1 Mermaid (stateDiagram, válido). Se agregó la lista de instrucciones privilegiadas del material de clase. La mnemotecnia arriba/abajo y el ejemplo de copiar un CD quedaron en un callout. El bit 0/1 se presenta como convención de los textos, porque el material de clase no da valores. Sin dudas nuevas.
