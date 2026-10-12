# Hilos — índice

Concepto de hilo (*thread* o proceso liviano) como unidad fundamental de ejecución en la CPU, disociación entre posesión de recursos y flujo de control, análisis de recursos compartidos (código, variables globales, memoria dinámica, archivos) frente a recursos privados (Thread ID, Program Counter, conjunto de registros de CPU, pila de ejecución privada), ciclo de vida y programación mediante el estándar POSIX Threads (`pthreads`), y modelos arquitectónicos de implementación (hilos en espacio de usuario, hilos en espacio de kernel y modelos híbridos).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la Clase 5 de los apuntes originales de Sistemas Operativos, complementadas con las diapositivas oficiales de `Contenido_4_Threads.pdf` y la especificación estándar de POSIX Threads (IEEE 1003.1c).

## Orden de estudio

1. [[01 - Concepto de hilo y recursos compartidos versus privados|Concepto de hilo y recursos compartidos versus privados]]: definición de hilo frente a proceso, concurrencia frente a paralelismo en hardware multinúcleo, tabla comparativa de recursos compartidos y privados, e introducción a los riesgos de inconsistencia de memoria.
2. [[02 - Programación con POSIX Threads y ciclo de vida|Programación con POSIX Threads y ciclo de vida]]: estándar POSIX Threads (`pthreads`), llamadas fundamentales (`pthread_create`, `pthread_join`, `pthread_exit`, `pthread_yield`), paso de argumentos genéricos y ejemplo práctico en lenguaje C.
3. [[03 - Hilos a nivel de usuario frente a hilos a nivel de kernel|Hilos a nivel de usuario frente a hilos a nivel de kernel]]: arquitectura en espacio de usuario (ULT) y espacio de kernel (KLT), ventajas de escalabilidad y portabilidad, desventajas ante llamadas al sistema bloqueantes, y costo de destrucción de hilos frente a procesos.

