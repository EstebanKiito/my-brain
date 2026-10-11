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

## Memoria virtual
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Sistemas de archivos
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Implementación de archivos y bloques
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Fundamentos de redes y modelos en capas
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Capa de aplicación y sockets
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Capa de transporte
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Capa de red y direccionamiento
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Algoritmos de ruteo
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Capa de enlace y seguridad
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|

## Gestión del curso
| Estado | Nota | Original | Duda / corrección propuesta |
|---|---|---|---|
