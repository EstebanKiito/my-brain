# Threading — índice

Conceptos y herramientas de concurrencia mediante hilos en Python: distinción entre procesos e hilos, creación y control con el módulo estándar `threading`, sincronización y espera con `join()`, ciclo de vida de hilos de soporte *daemon*, exclusión mutua para evitar condiciones de carrera mediante `Lock`, prevención de interbloqueos (*deadlocks*), coordinación mediante señales con `Event`, desacoplamiento mediante colas seguras para hilos con `queue.Queue` y temporizadores asíncronos con `Timer`, y el impacto arquitectónico del *Global Interpreter Lock* (GIL) en tareas I/O-bound y CPU-bound.

Volver al [[Programación Avanzada/_Índice|mapa del ramo]].

> [!note] Origen
> Reescrito a partir de los tres notebooks de la octava semana del curso (introducción a threading, concurrencia y consecuencias, y ejemplos y aplicaciones prácticas), complementado con las diapositivas de clases.

## Orden de estudio
1. [[01 - Hilos y procesos: el módulo threading|Hilos y procesos: el módulo threading]]: procesos vs hilos, memoria compartida, creación con funciones objetivo (`target`) y subclases de `Thread`, y ciclo de vida básico con `start()` y `run()`.
2. [[02 - Sincronización con join y ciclo de vida de hilos daemon|Sincronización con join y ciclo de vida de hilos daemon]]: espera y coordinación con `join()`, tiempos límite con `timeout`, consulta de estado con `is_alive()`, y ciclo de vida de hilos daemon frente a no daemon.
3. [[03 - Concurrencia condiciones de carrera y locks|Concurrencia, condiciones de carrera y locks]]: acceso concurrente a memoria compartida, condiciones de carrera (*race conditions*), exclusión mutua con `threading.Lock` y uso seguro con context manager `with lock:`.
4. [[04 - Deadlocks y coordinación de hilos con Event|Deadlocks y coordinación de hilos con Event]]: causas y prevención de interbloqueos (*deadlocks*), ruptura de dependencias circulares, y señalización eficiente entre hilos con `threading.Event`.
5. [[05 - Colas sincronizadas y el patrón productor-consumidor|Colas sincronizadas y el patrón productor-consumidor]]: desacoplamiento con el patrón productor-consumidor, estructura `queue.Queue` thread-safe nativa sin espera activa (*busy waiting*), y temporizadores asíncronos con `threading.Timer`.
6. [[06 - El GIL de Python: concurrencia IO-bound frente a CPU-bound|El GIL de Python: concurrencia IO-bound frente a CPU-bound]]: el cerrojo global del intérprete (GIL) de CPython, diferencias entre concurrencia y paralelismo, rendimiento en tareas I/O-bound vs CPU-bound, y cuándo recurrir a `multiprocessing`.
