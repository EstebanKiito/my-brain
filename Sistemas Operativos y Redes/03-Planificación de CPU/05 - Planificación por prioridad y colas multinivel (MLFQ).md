---
ramo: "Sistemas Operativos y Redes"
tema: "Planificación de CPU"
tags:
  - ssoo
  - scheduling
  - priority
  - starvation
  - aging
  - mlfq
prerrequisitos:
  - "[[03 - Planificación FCFS y SJF]]"
  - "[[04 - Planificación Round Robin y sistemas interactivos]]"
---

# Planificación por prioridad y colas multinivel (MLFQ)

Para satisfacer simultáneamente tiempos de retorno bajos para tareas cortas y tiempos de respuesta ágiles para tareas interactivas sin conocer la duración futura de los procesos, los sistemas operativos emplean **planificación por prioridades** y **colas multinivel con retroalimentación** (*Multilevel Feedback Queue* o MLFQ).

---

## PRORITY SCHEDULING (mis apuntes)

> ![Planificación por prioridad starvation y aging](adjuntos/Planificaci%C3%B3n%20por%20prioridad%20starvation%20y%20aging.png)
> 
> Existen priorida + tiempo de vida → AGING
> - Para eso existe aging, para que cuando pase el tiempo, sumen aging y les de mas prioridad
> 
> STARVATION: Sufren de baja prioridad → Nadie los tomo en cuenta
> 
> PRIORIDADES DE LA COLA
> Colas de multinivel → Se van cambiando de colas con nivels de prioridad
> Me van a atender cuando sea el mas importante de una Cola (A, B o C)
> 
> ![Estructura de colas multinivel con retroalimentación MLFQ](adjuntos/Estructura%20de%20colas%20multinivel%20con%20retroalimentaci%C3%B3n%20MLFQ.png)
> 
> Observacion → No faltar a la clase de paginacion → dado que los videos en youtube son demasiado largos y no sirve tanto verlos → Mejor venir a la clase que es mas densa

> [!warning] Posible error en apuntes
> * *"PRORITY"*: errata por *Priority*.
> * *"priorida"*: errata por "prioridad".
> * *"nivels"*: errata por "niveles".
> * La última observación es un recordatorio personal del estudiante referente al tema posterior de memoria y paginación.

---

> [!example]- Transcripción de la imagen: Planificación por prioridad starvation y aging.png
> **Priority Scheduling:**
> * A cada proceso se le asigna un valor numérico de prioridad.
> * La CPU atiende siempre al proceso listo con mayor prioridad.
> * Desempate entre prioridades iguales: se utiliza FCFS o Round-Robin.
> * **SJF como caso particular:** SJF equivale a un planificador de prioridad donde la prioridad es inversamente proporcional a la duración del *burst* ($p = 1 / \tau$).
> * Las prioridades pueden ser **estáticas** (fijas de por vida) o **dinámicas** (cambian según el comportamiento del proceso o mandatos como `nice` en UNIX).
> * **Inanición (*Starvation*):** Los procesos con baja prioridad pueden quedar postergados indefinidamente ante la llegada continua de procesos de alta prioridad.
> * **Envejecimiento (*Aging*):** Solución que incrementa gradualmente la prioridad de los procesos a medida que acumulan tiempo de espera en la cola *Ready*.

> [!example]- Transcripción de la imagen: Estructura de colas multinivel con retroalimentación MLFQ.png
> **Esquema de colas MLFQ:**
> * Estructura jerárquica con múltiples colas de prioridad:
>   - **Cola superior (Alta prioridad):** Quantum corto (*shorter quantum*), ideal para tareas interactivas / I/O-bound.
>   - **Colas intermedias (Media prioridad):** Quantum moderado.
>   - **Cola inferior (Baja prioridad):** Quantum largo (*longer quantum*) o FCFS para tareas intensivas en CPU (*CPU-bound*).
> * Los procesos que agotan su quantum son expropiados (*preempted*) y degradados al nivel inferior.

---

> [!tip] Complemento: Las 5 Reglas Fundamentales de MLFQ
> El planificador MLFQ (introducido históricamente en sistemas CTSS y base de Windows y macOS) implementa las siguientes reglas:
> 1. **Regla 1:** Si $\text{Prioridad}(A) > \text{Prioridad}(B)$, se ejecuta el proceso $A$.
> 2. **Regla 2:** Si $\text{Prioridad}(A) = \text{Prioridad}(B)$, se ejecutan $A$ y $B$ usando Round-Robin en esa cola.
> 3. **Regla 3:** Cuando un proceso ingresa al sistema, entra en la cola de **máxima prioridad**.
> 4. **Regla 4 (Contabilidad estricta):** Al consumir su cuota de tiempo acumulada en un nivel (incluso si cede la CPU antes de terminar el quantum), su prioridad desciende un nivel. Esto evita que un proceso haga trampa (*gaming the scheduler*) cediendo la CPU deliberadamente al $99\%$ del quantum.
> 5. **Regla 5 (Reinicio periódico / *Priority Boost*):** Tras un intervalo $S$, todos los procesos del sistema se promueven a la cola de máxima prioridad, eliminando la inanición (*starvation*) y permitiendo que procesos que cambiaron de fase recuperen interactividad.

---

## Preguntas de repaso

> [!question]- ¿Qué problema resuelve la técnica de Aging en un planificador por prioridades?
> Resuelve la **inanición** (*starvation*). Al elevar progresivamente la prioridad de un proceso que lleva mucho tiempo esperando en la cola, se garantiza que tarde o temprano alcance una prioridad suficiente para ser ejecutado por la CPU.

> [!question]- ¿Cómo clasifica MLFQ los procesos entre I/O-bound y CPU-bound de forma automática?
> Todos los procesos ingresan en la cola superior. Si un proceso realiza ráfagas cortas de CPU y se bloquea esperando I/O antes de agotar su tiempo, se mantiene en las colas de alta prioridad (favoreciendo la interactividad). Si un proceso monopoliza la CPU agotando su cuota de tiempo, desciende a las colas inferiores (asumiendo que es *CPU-bound*).

> [!question]- ¿Por qué es necesaria la regla del Priority Boost (Regla 5) en MLFQ?
> Porque sin un reinicio periódico, un proceso largo que desciende a la cola inferior podría sufrir inanición si el sistema recibe muchas tareas interactivas nuevas. Además, permite que un proceso que pasa de una fase de cómputo intensivo a una fase interactiva recupere rápidamente una alta prioridad.
