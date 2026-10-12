---
ramo: "Sistemas Operativos y Redes"
tema: "Gestión del curso"
tags:
  - sistemas-operativos
  - gestion-curso
  - procesos
  - hilos
  - scheduling
  - pcb
prerrequisitos:
  - "[[18-Gestión del curso/01 - Estructura de evaluaciones y preparación del Midterm|01 - Estructura de evaluaciones y preparación del Midterm]]"
---

# Síntesis de procesos, hilos y planificación para el Midterm

Esta nota recopila los conceptos clave sobre la arquitectura del sistema operativo, el modelo de procesos e hilos, llamadas al sistema esenciales (`fork`, `exec`, `wait`), señales y políticas de planificación de CPU (**scheduling**), tal como fueron sintetizados en la pizarra de repaso y en las preguntas tipo examen del Midterm.

---

## Núcleo, procesos y concurrencia en pizarra (mis apuntes)

Resumen Clase Lunes 28/10/24: Profe Lesly Reyes
S.O → Kernell + Programas
Kernell → Programa que siempre esta ejecutando
- Provee las funcionalidades minimas
SO
- Nos abstrae del hardware
- Permite compartir Recursos
- Nos ofrece servicios
SO → Compusto por
→ Sistema de archivos
→ Proteccion/Seguridad
→ Control I/O
→ Drivers
Tipos de Kernells
→ Complejo/grande
→ Rapido
- Monolitico:
→ Pequeño/modular
→ Aislado a fallos
- MicroKernell:
Acceso
→ Kernell Mode
→ User Mode
Syscalls
Llaman al S.O
Proceso
Codigo + Recursos
Memoria Archivos
Sockets
CPU atiende “Simultaneamente” mas de un Proceso: Multitasking
Proceso
→ Codigo
→ Datos
→ Heap
→ Stack
PCB
Estado, ID
Estados de un proceso → New / Running / Ready / Terminated
Context Switch
Espacio de Swap
Threads = Procesos mas livianos

![Pizarra de repaso 1: Arquitectura del núcleo, llamadas al sistema y modelo de procesos](adjuntos/IMG_1083.heic)

> [!example]- Transcripción de la imagen
> Registro de pizarra (panel izquierdo): SO = kernel + programas; kernel permanente que abstrae hardware, ofrece servicios y comparte recursos. Subsistemas: archivos, protección, I/O y drivers. Kernels monolíticos (grandes, rápidos) vs microkernels (modulares, aislados a fallos). Modo Kernel vs Usuario. Procesos (código, datos, heap, stack), PCB (estado, PID, PC), estados (New, Running, Ready, Waiting, Terminated), context switch, swap y threads como procesos livianos.

Syscalls
- Fork: Creacion de nuevo proceso
→ Reemplaza el codigo de quien lo llamo
- Exec: Carga el binario en memoria
Señales
Sigterm / Sigkill / Sigint
Wait → Espero del termino del proceso hijo
Proceso Huerfano: Cuando un padre termine (exit) o muere y sus hijos quedan huerfanos ()
Proceso Zombie: cuando un proceso termina y su padre no hace wait
Scheduling
Long Term (cola Ready) / Medium term (Swapping) / Short Term (selecciona ejecuta)
- Preemptie (expropiativo) : Saca el procesos de ejecucion
- Batch : Se ejecuta por lotes
- Interactivo : Minimiza el tiempo de respuesta
- FCFS
- SJF
- RR (round robin)

![Pizarra de repaso 2: Llamadas fork/exec/wait, estados de procesos y niveles de scheduling](adjuntos/IMG_1084.heic)

> [!example]- Transcripción de la imagen
> Registro de pizarra (panel central): Syscalls fork() (creación de hijo), exec() (reemplazo de código y carga de binario) y wait() (espera del hijo). Procesos huérfanos (padre muere antes; adoptado por PID 1) y zombies (hijo termina y padre no hace wait). Señales SIGTERM, SIGKILL y SIGINT. Planificadores Long-Term (cola ready), Medium-Term (swapping) y Short-Term (despacho a CPU). Algoritmos cooperativos vs expropiativos, batch vs interactivos, y FCFS, SJF y Round Robin.

Proceso:
- Codigo
- Heap
- Datos
- Stack
PCB: Guarda estado, Guarda el id (donde esta el codigo, cuanto tiempo a corrido, en que parte esta el program counter)
Siempre se pregunta como
La pcb permite guardar el estado : V
La pcb permite guardar el id: V
La pcb permite guardar estado del disco: F
Estados: New/ Running/ Waiting/ Ready/ Terminated
Context Switch: Correr el programa desde donde estaba (no partir desde el inicio)
Spacio de Swap: Donde van los programas que no se han estado usando por tiempo (ej: Si deje abierto el correo y no se ha usado en tiempo)
Espacio en memoria secundaria (disco), donde van los procesos que salen de la CPU
PREGUNTA SI O SI
Threads → ¿Que Comparten y que no comparten?
Fork
Exec
Pregunta: Definicion
Que es un proceso zombie?
Que es un proceos Huerfano?
Señales a saberse:
Sigterm (terminar en buena onda) / Sigkill (matarlo) / Sigint (interrupcion)
Pregunta si o si de schedulling
Ej: Hay 3 schedulling corriendose (long medium y short term)
Que hace el long → Escoge que procesos poner en la cola ready
Short term: Selecciono el que se va a ejecutar
Short term: Hace swapping: Saca de la Cpu
Distintos tipos de schedulers
Colaborativos → Sal cuando quieras → Los proecsos siempre querran terminar todo → Por ellos nunca salen
Expropiativos → Sacan los procesos de ejecucion → (Con un timer) , Estos son mas usados
Batch: Por lotes, y corre por ejemplo por las noches, en CPU BURST : Alto computo
Interactivo: Interactivo con el usario (I/O)
Schedullers: tenemos que sabernos las definiciones
Los ejemplos son solo como los de la ayudantia → Aprenderselos

> [!tip] Complemento de clase: Resumen de preguntas críticas de examen
> 1. **Diferencia Zombie vs Huérfano**:
>    - **Zombie**: Proceso que ejecutó `exit()`, liberó su memoria pero sigue ocupando una entrada en la tabla de procesos porque su padre aún no recoge su código de salida con `wait()`.
>    - **Huérfano**: Proceso cuyo padre finalizó sin esperar su término; el sistema operativo lo reasigna al proceso raíz `init` (PID 1) o `systemd`, el cual ejecuta `wait()` periódicamente para prevenir que se convierta en zombie permanente.
> 2. **Hilos (Threads)**:
>    - *Comparten*: Espacio de direcciones completo (código, datos globales, heap), descriptores de archivos abiertos, sockets y señales.
>    - *No comparten (privado)*: Stack (pila de llamadas local), registros de CPU (incluyendo Program Counter) y Thread ID (TID).

---

## Preguntas de repaso

> [!question]- ¿Por qué es fundamental que un planificador sea expropiativo (*preemptive*) en un sistema multiusuario interactivo?
> Porque en un planificador cooperativo un proceso con un bucle infinito o intensivo en CPU podría monopolizar el procesador indefinidamente sin ceder el control. La expropiación mediante interrupciones periódicas de reloj (*timer interrupts*) garantiza el reparto equitativo del tiempo de CPU.

> [!question]- ¿Qué información crucial restaura el sistema operativo durante un cambio de contexto (*context switch*)?
> Guarda los registros de la CPU del proceso saliente en su respectivo PCB y carga en los registros del procesador el estado del nuevo proceso seleccionado (incluyendo el contador de programa `PC`, el puntero de pila `SP` y la tabla de traducción de memoria en la MMU).

> [!question]- ¿Cuál es la diferencia operativa entre las señales SIGTERM y SIGKILL?
> SIGTERM (señal 15) es una solicitud de terminación que el proceso puede interceptar para limpiar recursos, cerrar sockets y guardar archivos antes de salir. SIGKILL (señal 9) es interceptada directamente por el kernel y destruye el proceso de manera inmediata e incondicional sin darle oportunidad de ejecutar manejadores.
