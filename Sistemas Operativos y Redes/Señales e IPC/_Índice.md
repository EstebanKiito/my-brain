# Señales e IPC — índice

Mecanismos de comunicación y control entre procesos (**IPC**, *Inter-Process Communication*): concepto de señal como interrupción por software, ciclo de vida de señales POSIX (generación, estado pendiente y entrega), diferenciación semántica entre terminación suave (`SIGTERM`) e inmediata (`SIGKILL`), interrupción por teclado (`SIGINT`), suspensión y reanudación (`SIGSTOP`/`SIGTSTP` y `SIGCONT`), y programación en lenguaje C con manejadores de señales (`signal`/`sigaction`) y tuberías anónimas (*pipes*).

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de las secciones de señales de los apuntes originales de Sistemas Operativos, complementadas con las diapositivas oficiales (`Contenido_2_Procesos.pdf`), manuales POSIX y fundamentos de programación de sistemas UNIX.

## Orden de estudio

1. [[01 - Concepto de señal y ciclo de vida de señales POSIX|Concepto de señal y ciclo de vida de señales POSIX]]: naturaleza asíncrona, interrupciones por software, etapas de vida (generación, pendiente, entrega), llamadas al sistema `kill()` y utilidades `kill -l` y `killall`.
2. [[02 - Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT|Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT]]: semántica de señales clave, apagado ordenado (*graceful shutdown*), diferencias de interceptabilidad entre `SIGTERM` y `SIGKILL`, y suspensión con `SIGSTOP` / `SIGCONT`.
3. [[03 - Comunicación entre procesos y manejo de señales en C|Comunicación entre procesos y manejo de señales en C]]: paradigmas de IPC, registro de *signal handlers* con `signal()` y `sigaction()`, funciones seguras ante señales asíncronas y comunicación mediante *pipes* unidireccionales.

