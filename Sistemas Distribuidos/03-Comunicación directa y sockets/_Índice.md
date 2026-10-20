# Comunicación directa y sockets — índice

Cómo se comunican los nodos por la red: el vocabulario para clasificar una comunicación (persistencia, sincronía y acoplamiento), los tres paradigmas, los protocolos de transporte y de aplicación que se usan por debajo, y la comunicación directa con sockets en Python y con MPI.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (tipos de comunicación, acoplamiento, paradigmas, protocolos, TCP, UDP, DNS, HTTP, sockets y MPI) y completado con las slides de la clase "Comunicación entre nodos I" (ejemplos de cada tipo, diagramas de TCP y UDP, recorrido DNS, MPI y sus llamadas, y la pregunta de la conferencia por Zoom). El código se ejecutó con Python 3.13 y con mpi4py sobre `mpiexec`.

## Orden de estudio
1. [[01 - Persistencia, sincronía y acoplamiento|Persistencia, sincronía y acoplamiento]]: cómo clasificar una comunicación de red.
2. [[02 - Paradigmas de comunicación|Paradigmas de comunicación]]: directa, indirecta e invocación remota.
3. [[03 - Protocolos de transporte TCP y UDP|Protocolos de transporte TCP y UDP]]: garantías frente a velocidad, y cuándo usar cada uno.
4. [[04 - Protocolos de aplicación DNS y HTTP|Protocolos de aplicación DNS y HTTP]]: resolución de nombres y petición de una página.
5. [[05 - Sockets TCP en Python|Sockets TCP en Python]]: cliente, servidor, protocolo con largo y servidor con threads.
6. [[06 - MPI y el modelo SPMD|MPI y el modelo SPMD]]: comunicación entre procesos de un clúster.

Las imágenes de esta carpeta están en `adjuntos/`.
