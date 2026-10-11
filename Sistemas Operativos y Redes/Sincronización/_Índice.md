# Sincronización — índice

Fundamentos y mecanismos de coordinación y sincronización entre procesos e hilos concurrentes que comparten memoria y recursos en el sistema operativo. Análisis de condiciones de carrera (*race conditions*), formulación del problema de la sección crítica y sus tres requisitos formales (exclusión mutua, progreso, espera acotada). Soluciones algorítmicas por software (algoritmo de Peterson), primitivas de hardware atómicas (`TestAndSet`, `CompareAndSwap`), bloqueos de exclusión mutua (*mutex locks* / *spinlocks*), semáforos de Dijkstra, variables de condición y monitores. Estudio detallado de los problemas clásicos de concurrencia: productor-consumidor con buffer acotado, lectores y escritores, y el dilema de los filósofos comelones, junto con las condiciones y prevención de bloqueos mutuos (*deadlocks*).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir del CONTENIDO 5: SINCRONIZACIÓN de los apuntes originales de Sistemas Operativos, complementadas con las diapositivas oficiales de `Contenido_5_Sincronizacion.pdf` y la literatura estándar de sistemas operativos (Silberschatz et al.).

## Orden de estudio

1. [[01 - Condiciones de carrera y el problema de la sección crítica|Condiciones de carrera y el problema de la sección crítica]]: naturaleza no determinista de la concurrencia, condiciones de carrera (*race conditions*), formulación matemática de la sección crítica y los tres requisitos formales (exclusión mutua, progreso y espera acotada).
2. [[02 - Soluciones por software y algoritmo de Peterson|Soluciones por software y algoritmo de Peterson]]: evolución histórica de soluciones puramente algorítmicas por software, turnos y banderas de intención, algoritmo de Peterson para 2 procesos y límites ante reordenamiento de instrucciones en CPUs modernas.
3. [[03 - Sincronización por hardware e instrucciones atómicas|Sincronización por hardware e instrucciones atómicas]]: primitivas de hardware a nivel de procesador, deshabilitación de interrupciones e instrucciones atómicas indivisibles `TestAndSet` y `CompareAndSwap` (CAS).
4. [[04 - Mutex locks y el dilema de busy waiting versus dormir|Mutex locks y el dilema de busy waiting versus dormir]]: cerrojos de exclusión mutua (`mutex`), operaciones `acquire()` y `release()`, compromiso entre espera activa (*spinlocks*) y suspensión en colas de espera (*sleep*).
5. [[05 - Problema del productor-consumidor y buffer acotado|Problema del productor-consumidor y buffer acotado]]: coordinación de flujo entre procesos productores y consumidores sobre un buffer de capacidad finita, uso de contadores y punteros circulares.
6. [[06 - Semáforos de Dijkstra y tipos de semáforos|Semáforos de Dijkstra y tipos de semáforos]]: estructura y semántica de semáforos de Dijkstra, operaciones atómicas `wait` ($P$) y `signal` ($V$), semáforos binarios y contadores, y eliminación de espera activa mediante colas de bloqueo del kernel.
7. [[07 - Variables de condición y monitores|Variables de condición y monitores]]: abstracciones de sincronización estructuradas en lenguajes de alto nivel, semántica de monitores, variables de condición (`cond_wait`, `cond_signal`, `cond_broadcast`) y el patrón de verificación en ciclo `while`.
8. [[08 - Problema de los lectores y escritores|Problema de los lectores y escritores]]: sincronización con acceso asimétrico a datos compartidos (lectura concurrente vs. escritura exclusiva), inanición (*starvation*) y variantes de prioridad.
9. [[09 - Problema de los filósofos comelones y deadlocks|Problema de los filósofos comelones y deadlocks]]: dilema clásico de asignación de recursos circulares, caracterización de interbloqueos (*deadlocks*), las 4 condiciones de Coffman y algoritmos de prevención.
