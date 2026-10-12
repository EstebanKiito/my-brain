# Planificación de CPU — índice

Mecanismos y algoritmos del sistema operativo para la asignación eficiente y equitativa del tiempo de procesador entre múltiples procesos en estado listo (*ready*): niveles de planificación (largo, mediano y corto plazo), alternancia de ráfagas CPU e I/O, taxonomía por expropiación y entorno, métricas de desempeño (*turnaround*, tiempo de respuesta, *throughput*, utilización), algoritmos por lotes (FCFS y SJF/SRTN), planificación interactiva (Round-Robin y dimensionamiento del quantum), y sistemas por prioridades con colas multinivel con retroalimentación (MLFQ).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la sección de planificación de CPU de los apuntes originales de Sistemas Operativos, complementadas con las diapositivas oficiales del curso (`Contenido_3_Scheduling.pdf`) y fundamentos del libro de Arpaci-Dusseau (*Operating Systems: Three Easy Pieces - CPU Scheduling*).

## Orden de estudio

1. [[01 - Niveles de planificación y ciclo de ráfagas CPU-IO|Niveles de planificación y ciclo de ráfagas CPU-I/O]]: planificador a largo, mediano y corto plazo (*dispatcher*), gestión de multiprogramación, *swapping* y alternancia entre ráfagas de cómputo y espera por periféricos.
2. [[02 - Clasificación de planificadores y métricas de rendimiento|Clasificación de planificadores y métricas de rendimiento]]: políticas expropiativas (*preemptive*) frente a cooperativas, entornos *batch*, interactivo y tiempo real, y formalización de métricas (*turnaround*, *response time*, *throughput*, utilización).
3. [[03 - Planificación FCFS y SJF|Planificación FCFS y SJF]]: algoritmos basados en orden de llegada y duración de ráfaga, cálculo de tiempos de retorno, efecto convoy (*convoy effect*) e inanición (*starvation*).
4. [[04 - Planificación Round Robin y sistemas interactivos|Planificación Round Robin y sistemas interactivos]]: asignación equitativa por rodajas de tiempo (*quantum*), optimización del tiempo de respuesta interactivo y compromiso frente a la sobrecarga del cambio de contexto.
5. [[05 - Planificación por prioridad y colas multinivel (MLFQ)|Planificación por prioridad y colas multinivel (MLFQ)]]: asignación estática y dinámica de prioridades, técnica de envejecimiento (*aging*), y arquitectura de colas con retroalimentación basadas en las 5 reglas clásicas de MLFQ.

