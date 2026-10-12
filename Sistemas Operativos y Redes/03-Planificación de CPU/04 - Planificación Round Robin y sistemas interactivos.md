---
ramo: "Sistemas Operativos y Redes"
tema: "Planificación de CPU"
tags:
  - ssoo
  - scheduling
  - round-robin
  - quantum
  - time-slice
  - interactivo
prerrequisitos:
  - "[[02 - Clasificación de planificadores y métricas de rendimiento]]"
  - "[[03 - Planificación FCFS y SJF]]"
---

# Planificación Round Robin y sistemas interactivos

En sistemas interactivos, el objetivo principal no es minimizar el tiempo total de finalización (*turnaround*), sino brindar una respuesta inmediata al usuario. El algoritmo por excelencia para este propósito es **Round-Robin (RR)**.

---

## ALGORITMOS DE SCHEDULING (mis apuntes)

> ![Métrica de tiempo de respuesta en sistemas interactivos](adjuntos/M%C3%A9trica%20de%20tiempo%20de%20respuesta%20en%20sistemas%20interactivos.png)
> 
> Cada cierto tiempo, para que el tiempo de respuesta sea bajo
> Esta avanzando, pero significa siempre que van a terminar
> Scheduling interactivo → Cree que los programas le dan mucho atencion a cada programa
> 
> ![Planificación Round Robin con quantum unitario](adjuntos/Planificaci%C3%B3n%20Round%20Robin%20con%20quantum%20unitario.png)
> 
> - Asi se ve interactivo, cada ciertos instantes les toca
> - Afecta el turnaround time → Hubieran salido antes con otro FIFO
> - Cambio el tiempo que pasan en el sistema (turnaround) → A cambio de tener un tiempo de respuesta mas bajo

> [!warning] Posible error en apuntes
> * *"Cree que los programas le dan mucho atencion a cada programa"*: redactado de forma confusa; se refiere a que los usuarios perciben que el sistema le presta atención inmediata a cada proceso de forma simultánea (ilusión de paralelismo interactivo).
> * *"mas"*: falta tilde ("más bajo").

---

> [!example]- Transcripción de la imagen: Métrica de tiempo de respuesta en sistemas interactivos.png
> **Métrica: Tiempo de respuesta (*Response Time*):**
> * Definido como el intervalo transcurrido desde la llegada del proceso a la cola hasta su primera ejecución en CPU:
>   $$T_{\text{respuesta}} = T_{\text{inicio ejec.}} - T_{\text{llegada}}$$
> * **Ejemplo comparativo con FCFS:**
>   - $P_1$: Llegada $0$, CPU-burst $5$, Término $5$, Turnaround $5$, Inicio $0$, T. Respuesta $= 0$.
>   - $P_2$: Llegada $1$, CPU-burst $5$, Término $10$, Turnaround $9$, Inicio $5$, T. Respuesta $= 4$.
>   - $P_3$: Llegada $2$, CPU-burst $5$, Término $15$, Turnaround $13$, Inicio $10$, T. Respuesta $= 8$.
> * **Promedios FCFS:** Turnaround promedio $= 9$, Response time promedio $= 4$.

> [!example]- Transcripción de la imagen: Planificación Round Robin con quantum unitario.png
> **Round-Robin con rodaja de tiempo (quantum $q = 1$):**
> * Cada proceso recibe un turno de ejecución de tamaño $q$; al expirar, es expropiado y colocado al final de la cola *Ready*.
> * **Tabla con $q = 1$:**
>   - $P_1$: Llegada $0$, CPU-burst $5$, Término $13$, Turnaround $13$, Inicio $0$, T. Respuesta $= 0$.
>   - $P_2$: Llegada $0.1$, CPU-burst $5$, Término $14$, Turnaround $13.9$, Inicio $1$, T. Respuesta $= 0.9$.
>   - $P_3$: Llegada $0.2$, CPU-burst $5$, Término $15$, Turnaround $14.8$, Inicio $2$, T. Respuesta $= 1.8$.
> * **Promedios Round-Robin:**
>   - Turnaround promedio $= 13.9$ (peor que en FCFS).
>   - Response time promedio $= 0.9$ (drásticamente mejor que los $4$ de FCFS).
> * **Propiedades formales:**
>   - Con $n$ procesos, cada proceso recibe $1/n$ del tiempo de CPU.
>   - Ningún proceso espera más de $(n - 1) \times q$ unidades para volver a ejecutar.

---

> [!tip] Complemento: Dimensionamiento del Quantum ($q$)
> El rendimiento de Round-Robin depende críticamente del tamaño de la rodaja de tiempo $q$ frente al costo del cambio de contexto ($S$):
> 
> ```
> Caso A: Quantum muy grande (q -> inf)
> [                  Proceso P1                  ]
> Degenera en FCFS. Pésimo tiempo de respuesta interactivo.
> 
> Caso B: Quantum muy pequeño (q -> 0)
> [P1][CS][P2][CS][P3][CS][P1][CS]...
> El sistema gasta más tiempo ejecutando cambios de contexto (overhead) que trabajo útil.
> ```
> 
> * **Regla práctica de diseño:** El quantum $q$ debe ser considerablemente mayor que el tiempo de cambio de contexto $S$ (típicamente $q \in [10, 100]\text{ ms}$, con $S < 10\ \mu\text{s}$), de modo que el costo del cambio de contexto represente menos del $1\%$ del tiempo de CPU.

---

## Preguntas de repaso

> [!question]- ¿Cuál es el trade-off fundamental entre FCFS/SJF y Round-Robin?
> Round-Robin prioriza el **tiempo de respuesta** (*response time*) para garantizar interacción fluida, pero empeora el **tiempo de retorno** (*turnaround time*) porque fragmenta la ejecución de todos los procesos al intercalarlos.

> [!question]- ¿Qué ocurre si el quantum $q$ en Round-Robin se define demasiado grande o demasiado pequeño?
> Si $q$ es excesivamente grande, RR degenera en **FCFS**, destruyendo la interactividad. Si $q$ es extremadamente pequeño, el **overhead del cambio de contexto** consume la mayoría de los ciclos de la CPU, degradando severamente el rendimiento del procesador.

> [!question]- En un sistema con $n$ procesos y quantum $q$, ¿cuál es el tiempo máximo que un proceso debe esperar para volver a ejecutar?
> El tiempo máximo de espera entre turnos es $(n - 1) \times q$, asegurando que ningún proceso sufra inanición (*starvation*).
