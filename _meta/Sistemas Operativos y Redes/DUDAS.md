# Dudas y posibles errores en los apuntes originales — Sistemas Operativos y Redes (IIC2333)

Criterio: el texto original **se conserva tal cual** en la nota. Al lado va un callout `> [!warning] Posible error` con la precisión o corrección, y se registra aquí para revisarlo.

Estados: 🟡 abierta (la tienes que decidir tú) · ✅ resuelta · ℹ️ informativa (no es error tuyo).

## Estructura de sistemas operativos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[03 - Arquitecturas de kernel monolítico y microkernel\|Arquitecturas de kernel monolítico y microkernel]] | "MONOLITICO: Falta todo → Linux (Mas rápido)" | Errata evidente en el texto: un kernel monolítico no le "falta todo", sino que *junta todo* o *contiene todos los servicios* (drivers, IPC, memoria, fs) dentro del mismo espacio de kernel. Se propone corregir la lectura aclarando que empaqueta todos los subsistemas. |
| ℹ️ | [[01 - Qué es un sistema operativo\|Qué es un sistema operativo]] | "(SystemD = System Daemon) → probee funcionalidades basicas" | Errata menor de tipeo ("probee" por "provee") y precisión técnica: Systemd es el init system estándar moderno en GNU/Linux con PID 1, responsable de inicializar el espacio de usuario. |
| ℹ️ | [[03 - Arquitecturas de kernel monolítico y microkernel\|Arquitecturas de kernel monolítico y microkernel]] | "→ Microkernelll:" | Errata tipográfica con triple 'l'. Se preservó intacta en los apuntes. |
| ℹ️ | [[06 - Arranque del sistema computacional\|Arranque del sistema computacional]] | "Este codio tiene dos misions fundamentales" | Erratas tipográficas ("codio" por "código", "misions" por "misiones"). Se conservaron tal cual en la cita textual. |

## Procesos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[03 - Estados de un proceso y ciclo de vida\|Estados de un proceso y ciclo de vida]] | "RUNNING: Corriendo en CPU → CPU Y CORE ES LO MISMO" | Precisión técnica: un zócalo o procesador físico (*CPU*) puede albergar múltiples núcleos independientes (*cores*), cada uno capaz de ejecutar un hilo o proceso en paralelo. En un procesador multinúcleo, la afirmación no es estrictamente cierta a nivel de hardware. |
| ℹ️ | [[03 - Estados de un proceso y ciclo de vida\|Estados de un proceso y ciclo de vida]] | "Schedule FIFO: ... Schedule FCFS: ..." | FIFO (*First-In, First-Out*) y FCFS (*First-Come, First-Served*) son sinónimos exactos para la misma política de planificación no apropiativa. |
| ℹ️ | [[06 - Control de procesos con wait, exec y terminación\|Control de procesos con wait, exec y terminación]] | "Si no se le retorna al padre → Se genera un Proceso Zombie" | Un proceso zombie es un hijo que finalizó su ejecución pero cuyo padre aún no ha invocado `wait()` para leer su estado de salida, manteniendo su entrada en la tabla de procesos. |
| ℹ️ | [[07 - Programación de procesos en C y prevención de fork bombs\|Programación de procesos en C y prevención de fork bombs]] | `structs Process{...} enum Sates{RUNNING, WAI}` | Erratas tipográficas del código de ayudantía (`structs` por `struct`, `Sates` por `States`, `WAI` por `WAITING`). Se conservaron tal cual en el extracto textual. |

## Planificación de CPU
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[03 - Planificación FCFS y SJF\|Planificación FCFS y SJF]] | "0 10 → 10 / 1 10 → 19 / 2 100 → 118" | Los valores corresponden al caso alternativo donde los procesos cortos llegan antes que el largo, invirtiendo el orden de llegada en FCFS y mitigando el efecto convoy. Se documentó la tabla comparativa para evitar confusión. |
| 🟡 | [[02 - Clasificación de planificadores y métricas de rendimiento\|Clasificación de planificadores y métricas de rendimiento]] | "los colaborativos son casi inutiles, mejor expropiar" | Aunque en sistemas multiusuario de escritorio/servidor la falta de expropiación es inaceptable, en sistemas embebidos de bajo costo o esquemas de concurrencia cooperativa (corrutinas) sigue siendo un patrón útil. |
| ℹ️ | [[01 - Niveles de planificación y ciclo de ráfagas CPU-IO\|Niveles de planificación y ciclo de ráfagas CPU-I/O]] | "Regals para elegir... Depende del tipo de schedule" | Erratas tipográficas ("Regals" por "Reglas", "schedule" por "scheduler"). Preservadas intactas en la cita textual. |
| ℹ️ | [[02 - Clasificación de planificadores y métricas de rendimiento\|Clasificación de planificadores y métricas de rendimiento]] | "som los expropiativos... Real tiem... interacutar" | Erratas de tipeo en apuntes ("som" por "son", "Real tiem" por "Real Time", "interacutar" por "interactuar"). |
| ℹ️ | [[05 - Planificación por prioridad y colas multinivel (MLFQ)\|Planificación por prioridad y colas multinivel (MLFQ)]] | "PRORITY SCHEDULING... nivels" | Erratas tipográficas ("PRORITY" por "PRIORITY", "nivels" por "niveles"). |

## Señales e IPC
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[02 - Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT\|Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT]] | "SIGCOM: Continua" | Errata evidente por `SIGCONT` (señal POSIX número 18), encargada de reanudar un proceso suspendido. |
| ℹ️ | [[01 - Concepto de señal y ciclo de vida de señales POSIX\|Concepto de señal y ciclo de vida de señales POSIX]] | "SigStopy" | Errata tipográfica por `SIGSTOP` o `SIGTSTP`. Preservada intacta en la cita textual. |
| ℹ️ | [[02 - Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT\|Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT]] | "SIGSTP: Stop" | Errata tipográfica por `SIGTSTP` / `SIGSTOP`. Preservada en la cita textual. |

## Hilos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[03 - Hilos a nivel de usuario frente a hilos a nivel de kernel\|Hilos a nivel de usuario frente a hilos a nivel de kernel]] | "No se bloquean, porque pasan directo por abajo" | Precisión técnica: en hilos de kernel, si un hilo realiza una llamada bloqueante (I/O), ese hilo específico sí se bloquea, pero el resto de los hilos del proceso pueden continuar su ejecución en paralelo en otros núcleos. |
| ℹ️ | [[01 - Concepto de hilo y recursos compartidos versus privados\|Concepto de hilo y recursos compartidos versus privados]] | "parelizarlo... qusiera" | Erratas tipográficas ("parelizarlo" por "paralelizarlo", "qusiera" por "quisiera"). Preservadas intactas en la cita textual. |
| ℹ️ | [[03 - Hilos a nivel de usuario frente a hilos a nivel de kernel\|Hilos a nivel de usuario frente a hilos a nivel de kernel]] | "Kernell... neceisten... Eliminarmos" | Erratas tipográficas ("Kernell" por "Kernel", "neceisten" por "necesiten", "Eliminarmos" por "Eliminamos"). |

## Sincronización
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[01 - Condiciones de carrera y el problema de la sección crítica\|Condiciones de carrera y el problema de la sección crítica]] | "Espera Agotada" | Errata en el tercer criterio formal de la sección crítica: el término estándar es *Espera Acotada* (*Bounded Waiting*), que garantiza un límite finito a la cantidad de accesos concedidos a otros procesos antes de admitir al solicitante. |
| ℹ️ | [[04 - Mutex locks y el dilema de busy waiting versus dormir\|Mutex locks y el dilema de busy waiting versus dormir]] | "aquite() y realease()" | Erratas tipográficas por las operaciones canónicas `acquire()` y `release()` de cerrojos de exclusión mutua. |
| ℹ️ | [[05 - Problema del productor-consumidor y buffer acotado\|Problema del productor-consumidor y buffer acotado]] | "PRODUCTO-CONSUMIDOR" | Errata tipográfica ("PRODUCTO" por "PRODUCTOR"). Preservada en la cita textual. |
| ℹ️ | [[06 - Semáforos de Dijkstra y tipos de semáforos\|Semáforos de Dijkstra y tipos de semáforos]] | "dercrementa" | Errata tipográfica en la definición de la operación `wait()`. Preservada en la cita textual. |

## Administración de memoria
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[01 - Coordinación de filósofos y manejo de estados con semáforos\|Coordinación de filósofos y manejo de estados con semáforos]] | "Estado filosofal → Tiene palillo" | En la formulación estándar (Dijkstra/Tanenbaum), en el estado *THINKING* (filosofando) el filósofo no retiene recursos; ambos palillos se adquieren exclusivamente al pasar a *EATING*. |
| ℹ️ | [[02 - Memoria principal y el desafío de la multiprogramación\|Memoria principal y el desafío de la multiprogramación]] | "DIRECCIONES ABSOLUTAS EN MULTIPGROMACION" | Errata tipográfica ("MULTIPGROMACION" por multiprogramación). Preservada intacta en la cita textual. |
| ℹ️ | [[03 - Relocalización, protección de memoria y registros base y límite\|Relocalización, protección de memoria y registros base y límite]] | "realocalizada ... Memory Managment Unit" | Erratas tipográficas ("realocalizada" por relocalizada, "Managment" por Management). Preservadas en la cita textual. |
| ℹ️ | [[04 - Swapping, fragmentación externa y algoritmos de asignación libre\|Swapping, fragmentación externa y algoritmos de asignación libre]] | "memoria secundaria que usaremos como memoria secundaria" | Redundancia textual en la explicación de memoria swap. Preservada en la cita textual. |
| ℹ️ | [[05 - Segmentación de memoria y prevención de segmentation fault\|Segmentación de memoria y prevención de segmentation fault]] | "SEGMENTION FAULT" | Errata tipográfica por *Segmentation Fault* (`SIGSEGV`). Preservada en la cita textual. |
| ℹ️ | [[06 - Aritmética de bits y máscara de segmento en traducción de direcciones\|Aritmética de bits y máscara de segmento en traducción de direcciones]] | "aritmetrica" | Errata tipográfica por aritmética. Preservada en la cita textual. |

## Paginación y segmentación
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[01 - Fundamentos de paginación, marcos y tabla de páginas\|Fundamentos de paginación, marcos y tabla de páginas]] | "framse ... 64b de direcciones ... 16 bits de desplazamiento" | Errata tipográfica ("framse" por frames) y uso de unidades: 64b y 16 bits corresponden a 64 Bytes de espacio de direcciones y 16 Bytes de desplazamiento por página. |
| ℹ️ | [[02 - Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo\|Translation Lookaside Buffer (TLB) y tiempo de acceso efectivo]] | "TIEMPO ACCESOO PROMEDIO" | Errata tipográfica con doble 'o'. Preservada en la cita textual. |
| ℹ️ | [[03 - Localidad de referencia y gestión de TLB con ASID en cambios de contexto\|Localidad de referencia y gestión de TLB con ASID en cambios de contexto]] | "cercena ... Adress Space Identifier" | Erratas tipográficas ("cercena" por cercana, "Adress" por *Address*). Preservadas en la cita textual. |
| ℹ️ | [[04 - Sobrecarga de tablas lineales y compromiso de fragmentación interna\|Sobrecarga de tablas lineales y compromiso de fragmentación interna]] | "2*20 x 2**2B" | Errata de notación en el exponente: se pretendía calcular $2^{20} \times 2^2\text{ B} = 4\text{ MB}$. |
| ℹ️ | [[05 - Arquitectura de segmentos paginados\|Arquitectura de segmentos paginados]] | "ESPACIO VIRUTAL" | Errata tipográfica por Espacio Virtual. Preservada en la cita textual. |
| ℹ️ | [[06 - Paginación multinivel y tablas de páginas invertidas\|Paginación multinivel y tablas de páginas invertidas]] | "sitemas ... pagiunas" | Erratas tipográficas ("sitemas" por sistemas, "pagiunas" por páginas). Preservadas en la cita textual. |
| ℹ️ | [[07 - Introducción al intercambio por demanda y ciclo de fallos de página\|Introducción al intercambio por demanda y ciclo de fallos de página]] | "realmente te" | Frase inconclusa al cierre del párrafo ("realmente tenemos"). Preservada en la cita textual. |

## Memoria virtual
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| ℹ️ | [[01 - Fundamentos de memoria virtual y espacio de intercambio (swap)\|Fundamentos de memoria virtual y espacio de intercambio (swap)]] | "ecnuentren ... reemplazen" | Erratas tipográficas ("ecnuentren" por encuentren, "reemplazen" por reemplacen). Preservadas en la cita textual. |

## Sistemas de archivos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[03 - Niveles de formateo y esquemas de particionamiento (MBR y GPT)\|Niveles de formateo y esquemas de particionamiento (MBR y GPT)]] | "GPT (Guide partition table)" | Errata en el acrónimo: GPT corresponde a GUID Partition Table (*Globally Unique Identifier Partition Table*), no Guide. |
| ℹ️ | [[01 - Capas de abstracción de entrada-salida y mecanismos de buffering\|Capas de abstracción de entrada-salida y mecanismos de buffering]] | "Buffer en el espacio KERNELL" | Errata tipográfica en "KERNELL" con doble 'L'. |
| ℹ️ | [[02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)\|Discos duros magnéticos (HDD) y discos de estado sólido (SSD)]] | "Memoira Secundaria" | Errata tipográfica por Memoria Secundaria. |
| ℹ️ | [[04 - Algoritmos de planificación de disco (Disk Scheduling)\|Algoritmos de planificación de disco (Disk Scheduling)]] | "Schedulling ... Numeros de secotres" | Erratas tipográficas ("Schedulling" por Scheduling y "secotres" por sectores). |
| ℹ️ | [[05 - Concepto de archivo, atributos y metadatos\|Concepto de archivo, atributos y metadatos]] | "“hellowoeld.py”" | Errata tipográfica por "helloworld.py". |
| ℹ️ | [[06 - Estructura de directorios y resolución de rutas\|Estructura de directorios y resolución de rutas]] | "directiors ... Jerarqui ... Partencon" | Erratas tipográficas ("directiors" por directorios, "Jerarqui" por jerarquía, "Partencon" por parten con). |

## Implementación de archivos y bloques
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[01 - Interfaz y llamadas al sistema de archivos y directorios\|Interfaz y llamadas al sistema de archivos y directorios]] | "renaming mv ... eliminar rm" | `mv` y `rm` son utilidades de espacio de usuario; las llamadas al sistema POSIX reales son `rename()` y `unlink()`. |
| 🟡 | [[05 - Métodos de asignación de bloques: asignación contigua y bloques de control\|Métodos de asignación de bloques: asignación contigua y bloques de control]] | "Problema → No se pueden guardar archivos pequeños" | Precisión conceptual: en asignación contigua el desafío no radica en archivos pequeños, sino en la fragmentación externa y la imposibilidad de expandir archivos sin compactación. |
| ℹ️ | [[02 - Enlaces duros (hard links) y enlaces simbólicos (soft links)\|Enlaces duros (hard links) y enlaces simbólicos (soft links)]] | "Referencias a los procesos/archivos" | Los enlaces son referencias exclusivas a archivos o directorios en disco, no a procesos del sistema operativo. |
| ℹ️ | [[05 - Métodos de asignación de bloques: asignación contigua y bloques de control\|Métodos de asignación de bloques: asignación contigua y bloques de control]] | "blouqes ... PAra ... ASGINACION" | Erratas tipográficas ("blouqes" por bloques, "ASGINACION" por asignación). |
| ℹ️ | [[07 - Asignación indexada y arquitectura de inodos multinivel en Unix\|Asignación indexada y arquitectura de inodos multinivel en Unix]] | "ENLZADO ... MUTINIVEL ... ASGINACION ... Direccion simple" | Erratas de tipeo por enlazado, multinivel, asignación e indirección simple. |

## Fundamentos de redes y modelos en capas
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[01 - Arquitectura de Internet, nodos, enlaces y protocolos\|Arquitectura de Internet, nodos, enlaces y protocolos]] | "TCP: Transport control protocol" | El acrónimo estándar de IETF para TCP es *Transmission Control Protocol* (Protocolo de Control de Transmisión). |
| 🟡 | [[03 - Conmutación de paquetes frente a conmutación de circuitos\|Conmutación de paquetes frente a conmutación de circuitos]] | "red de INTERCAMBIO DE CIRCUITOS" | El término técnico formal en telecomunicaciones y redes es *conmutación de circuitos* (*Circuit Switching*). |
| ℹ️ | [[01 - Arquitectura de Internet, nodos, enlaces y protocolos\|Arquitectura de Internet, nodos, enlaces y protocolos]] | "PROVEDORES ... Elemenots ... atravez" | Erratas tipográficas ("PROVEDORES" por proveedores, "Elemenots" por elementos, "atravez" por a través). |
| ℹ️ | [[02 - Redes de acceso y medios físicos de transmisión\|Redes de acceso y medios físicos de transmisión]] | "acutan ... Comuncacion ... wirless ... Porpagacion" | Erratas tipográficas ("acutan" por actúan, "Comuncacion" por comunicación, "wirless" por wireless, "Porpagacion" por propagación). |
| ℹ️ | [[03 - Conmutación de paquetes frente a conmutación de circuitos\|Conmutación de paquetes frente a conmutación de circuitos]] | "trasnmicion ... packetes ... congesiton" | Erratas tipográficas ("trasnmicion" por transmisión, "packetes" por paquetes, "congesiton" por congestión). |
| ℹ️ | [[05 - Capas de transporte, red, enlace y física\|Capas de transporte, red, enlace y física]] | "ORGIN Y DESTINY ... Sevicion ... gratiza ... SWITCHS" | Erratas tipográficas en nombres y conceptos ("ORGIN Y DESTINY" por origen y destino, "Sevicion" por servicio, "gratiza" por garantiza, "SWITCHS" por switches). |
| ℹ️ | [[06 - Proceso de encapsulamiento y flujo de datos en la red\|Proceso de encapsulamiento y flujo de datos en la red]] | "trasnporte ... dispoisitvo" | Erratas de tipeo por transporte y dispositivo. |

## Capa de aplicación y sockets
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[01 - Arquitecturas de aplicación y modelos de comunicación\|Arquitecturas de aplicación y modelos de comunicación]] | "Es ICP Friendly" | El término técnico formal es *ISP-friendly* (amigable con el Proveedor de Servicios de Internet / Internet Service Provider). |
| 🟡 | [[03 - Sockets UDP y TCP: modelos y llamadas al sistema\|Sockets UDP y TCP: modelos y llamadas al sistema]] | "Por cada cliente → Un puerto" y "TCP: Conexion única (un puerto por cada conexion)" | El servidor mantiene el mismo puerto local (ej. 80); lo que se crea para cada cliente conectado es un nuevo descriptor de socket, diferenciado por la 4-tupla `(IP_src, Port_src, IP_dst, Port_dst)`. |
| ℹ️ | [[01 - Arquitecturas de aplicación y modelos de comunicación\|Arquitecturas de aplicación y modelos de comunicación]] | "RECPETORES ... ciuertas ... fekear ip" | Erratas tipográficas ("RECPETORES" por receptores, "ciuertas" por ciertas, "fekear ip" por IP spoofing). |
| ℹ️ | [[04 - Protocolo HTTP, formato de mensajes y estado con cookies\|Protocolo HTTP, formato de mensajes y estado con cookies]] | "CLOUDFORM ... Filezile" | Erratas tipográficas por Cloudflare / CloudFront y FileZilla. |

## Capa de transporte
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[06 - Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa\|Protocolo TCP: estructura del segmento, MSS y confirmación acumulativa]] | "Posee 20 Bits" y "7 bites" | El encabezado base de TCP mide 20 bytes (160 bits), no 20 bits. Asimismo, los caracteres ASCII son bytes, no bits. |
| ℹ️ | [[04 - Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)\|Principios de transferencia confiable de datos (rdt 1.0 a rdt 3.0)]] | "Cheksum ... Acnolagment ... SEQUENCIA" | Erratas tipográficas ("Cheksum" por checksum, "Acnolagment" por acknowledgment, "SEQUENCIA" por secuencia). |
| ℹ️ | [[07 - Gestión de temporizadores, retransmisión rápida y handshake en TCP\|Gestión de temporizadores, retransmisión rápida y handshake en TCP]] | "retrasnmitir ... dubplicado" | Erratas tipográficas por retransmitir y duplicado. |

## Capa de red y direccionamiento
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
| 🟡 | [[02 - Datagrama IPv4: estructura y fragmentación por MTU\|Datagrama IPv4: estructura y fragmentación por MTU]] | "Router del otro extremos lo reensambla" | En la arquitectura de Internet (IPv4), los routers intermedios nunca reensamblan fragmentos; el reensamblado se realiza exclusivamente en el host destinatario final. |
| 🟡 | [[03 - Direccionamiento IPv4: subredes, máscaras y notación CIDR\|Direccionamiento IPv4: subredes, máscaras y notación CIDR]] | "IPV6: 6 Bytes → 128 bits" | Una dirección IPv6 de 128 bits mide exactamente 16 bytes ($128/8 = 16$), no 6 bytes. |
| 🟡 | [[04 - Configuración dinámica con DHCP y traducción de direcciones NAT\|Configuración dinámica con DHCP y traducción de direcciones NAT]] | "NAT tiene distractores" | La palabra correcta es detractores (*detractors*), en alusión a las críticas arquitectónicas por violar el principio de extremo a extremo. |
| ℹ️ | [[04 - Configuración dinámica con DHCP y traducción de direcciones NAT\|Configuración dinámica con DHCP y traducción de direcciones NAT]] | "hacia el destino 128.76.29.7" | En el flujo de retorno se tipeó 128.76.29.7 en vez de la IP pública 138.76.29.7 usada en el ejemplo. |

## Algoritmos de ruteo
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Capa de enlace y seguridad
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Gestión del curso
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
