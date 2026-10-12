---
ramo: Sistemas Operativos y Redes
tema: Procesos
tags: [so/procesos, origen/apuntes]
prerrequisitos: ["[[02 - Bloque de control de procesos y tabla de procesos|Bloque de control de procesos y tabla de procesos]]"]
---
# Estados de un proceso y ciclo de vida

Durante su ciclo de vida, un proceso transita por diversos estados controlados por el planificador del sistema operativo, respondiendo a eventos de entrada/salida, interrupciones del temporizador y solicitudes de sincronización.

## Estados del proceso (mis apuntes)
Estados Proceso
- RUNNING: Corriendo en CPU → CPU Y CORE ES LO MISMO
- READY: listo para entrar en la CPU → LISTO PARA EJECUTAR, tiene TODO lo que necesita
- ej: Proceso de copiar archivos, en que carpeta? → necesito que el usuario ingrese un input para saber donde buscar
- Leer archivo en memoria → Cuando reciba lo que falta
- WAITING: Esperando I/O o bloqueado(esperando) → LE FALTA ALGO PARA CORRER
- FINISHED: Terminado
Ready → Running → Finished ———> Waiting….. → Ready → …..

> [!warning] Posible error (registrado en `_meta/Sistemas Operativos y Redes/DUDAS.md`)
> En la afirmación "CPU Y CORE ES LO MISMO", cabe notar que técnicamente una CPU física (*socket*) puede contener múltiples núcleos (*cores*) independientes. Además, las siglas FIFO (*First-In, First-Out*) y FCFS (*First-Come, First-Served*) denotan exactamente la misma estrategia de planificación.

![Diagrama de estados de un proceso](adjuntos/Diagrama%20de%20estados%20de%20un%20proceso.png)

> [!example]- Transcripción de la imagen
> Máquina de estados del ciclo de vida de un proceso:
> - **New:** Proceso recién creado mediante `fork()`, aún cargándose en memoria principal.
> - **Ready:** Proceso admitido en memoria, con todos sus recursos listos; espera en la cola de listos a que el *scheduler* lo asigne a una CPU.
> - **Running:** Proceso en ejecución activa sobre un núcleo de CPU.
>   - Transición a **Ready:** Ocurre por interrupción del temporizador (*timer interrupt*) cuando expira su cuanto de tiempo.
>   - Transición a **Waiting:** Ocurre cuando el proceso solicita una operación bloqueante (ejemplo: lectura/escritura de disco, entrada de usuario o `wait`).
>   - Transición a **Finished:** Ocurre al terminar su ejecución normal (`exit`) o al ser cancelado forzosamente (`kill`).
> - **Waiting (Blocked / Sleeping):** El proceso espera un evento externo o fin de I/O. Al cumplirse el evento, pasa a **Ready** (nunca salta directo a Running).
> - **Finished (Terminated):** Ejecución concluida, pendiente de limpieza de su PCB por el padre.

Quien eleije que entra en la CPU
Es una SCHEDULING
- Ready es una cola de procesos
- Existen de varios tipos
- Algunos ekigen
- Otro sacan de la cola Ready
Schedule FIFO: Primero que entra primero en ejecutarse
Schedule FCFS: Primero que entra → Primero que sale
Etc…
Se asignan tiempo → Ej: Se ejecutan en 5 segundos, si no sale y espera volver a ejecutarse, se pone en la cola READY

> [!tip] Complemento (slides "Contenido 2: Modelo de 5 y 7 Estados")
> En sistemas avanzados con gestión de memoria virtual existen estados adicionales con procesos suspendidos en disco (memoria de intercambio o swap):
> - **Ready Suspended (Listo y suspendido):** Proceso listo pero cuyo espacio de direcciones fue transferido al swap por falta de memoria RAM.
> - **Blocked Suspended (Bloqueado y suspendido):** Proceso esperando un evento de I/O y también movido a swap.

## Preguntas de repaso

1. ¿Por qué un proceso que termina una operación de I/O pasa al estado *Ready* y no directamente a *Running*?
> [!question]- Respuesta
> Porque la CPU puede estar ocupada atendiendo a otro proceso en ese instante. El proceso debe incorporarse a la cola de listos para que el planificador (*scheduler*) decida el orden equitativo de acceso al procesador.

2. ¿Cuál es la diferencia sustancial entre los estados *Ready* y *Waiting*?
> [!question]- Respuesta
> Un proceso en *Ready* tiene todo lo necesario para ejecutar de inmediato y solo espera turno de CPU; un proceso en *Waiting* no puede ejecutar aunque la CPU esté ociosa, porque depende de un evento externo (disco, red o usuario).

3. ¿Qué provoca la transición de un proceso de *Running* a *Ready* en un sistema multitarea?
> [!question]- Respuesta
> Una interrupción por temporizador de hardware (*timer interrupt*) generada al agotarse el cuanto de tiempo asignado (*quantum*), provocando el desalojo voluntario del procesador por planificación apropiativa.

4. ¿En qué estado permanece un proceso zombie?
> [!question]- Respuesta
> Se encuentra en el estado *Finished* (terminado): ya liberó su memoria y recursos, pero su PCB permanece en la tabla del kernel hasta que su proceso padre lea su estado de salida.

