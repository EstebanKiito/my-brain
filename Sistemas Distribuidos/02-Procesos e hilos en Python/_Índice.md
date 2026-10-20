# Procesos e hilos en Python — índice

La base de un sistema distribuido es un computador: cada nodo corre procesos y threads. Este tema repasa qué los distingue, cuánto cuesta cada uno, cómo se comunican y cómo se sincronizan, con ejemplos en Python que se usan en el resto del ramo.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (nodo, paralelismo y concurrencia, costo de un proceso, IPC y paso de mensajes, procesos y threads en Python, locks, panadería, semáforos, eventos, join y deadlock) y completado con las slides de la clase "Base del Sistema Distribuido: un computador" (ejemplos de cada combinación de procesos y threads, mecanismos de IPC, reglas de la panadería y la pregunta de procesos frente a threads). El código se ejecutó con Python 3.13.

## Orden de estudio
1. [[01 - El nodo, procesos y threads|El nodo, procesos y threads]]: qué hace un nodo, combinaciones de procesos y threads, paralelismo frente a concurrencia.
2. [[02 - Procesos y comunicación entre procesos|Procesos y comunicación entre procesos]]: costo del cambio de contexto, IPC y paso de mensajes.
3. [[03 - Procesos en Python con multiprocessing y subprocess|Procesos en Python con multiprocessing y subprocess]]: crear procesos y ejecutar scripts con y sin espera.
4. [[04 - Threads y su programación en Python|Threads y su programación en Python]]: ventajas y riesgos de los threads, `threading.Thread` y árboles de threads.
5. [[05 - Mecanismos de sincronización entre threads|Mecanismos de sincronización entre threads]]: condición de carrera, locks, semáforos, eventos y join.
6. [[06 - Algoritmo de la panadería y deadlock|Algoritmo de la panadería y deadlock]]: exclusión mutua con turnos e interbloqueo.

Las imágenes de esta carpeta están en `adjuntos/`.
