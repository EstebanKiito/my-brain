---
ramo: "Sistemas Operativos y Redes"
tema: "Planificación de CPU"
tags:
  - ssoo
  - scheduling
  - fcfs
  - sjf
  - convoy-effect
  - starvation
prerrequisitos:
  - "[[02 - Clasificación de planificadores y métricas de rendimiento]]"
---

# Planificación FCFS y SJF

Los algoritmos de planificación básicos para procesamiento por lotes (*batch*) organizan los procesos según su orden de llegada (**FCFS**) o según la duración estimada de su ráfaga (**SJF**).

---

## ORDEN DE LLEGADA (mis apuntes)

> FIFO
> FCFS
> 
> ![Planificación FCFS y efecto convoy](adjuntos/Planificaci%C3%B3n%20FCFS%20y%20efecto%20convoy.png)
> 
> El segundo en el que sali - El segundo en el que llegue
> 100 + 10 - 1 → Llegue en 1 = 109
> 110+ 10 - 2 → Llegue en 2 = 118
> 0 10 → 10
> 1 10 → 19
> 2 100 → 118
> 
> Siempre generalmente se pone el mas corto primero
> SJF
> 
> ![Planificación SJF y cálculo de turnaround](adjuntos/Planificaci%C3%B3n%20SJF%20y%20c%C3%A1lculo%20de%20turnaround.png)
> 
> PROBLEMA : No atender un proceso por mucho tiempo → (Pasa hambre)
> Puede haber uno que es largo, pero es importante → Y no lo estariamos ejecutando todavia

> [!warning] Posible confusión en apuntes: Caso alternativo en FCFS
> Las líneas `0 10 → 10`, `1 10 → 19`, `2 100 → 118` corresponden al caso inverso donde los trabajos cortos llegan primero:
> * Proceso corto $A$ llega en $t=0$ con duración 10: termina en 10 ($10 - 0 = 10$).
> * Proceso corto $B$ llega en $t=1$ con duración 10: termina en 20 ($20 - 1 = 19$).
> * Proceso largo $C$ llega en $t=2$ con duración 100: termina en 120 ($120 - 2 = 118$).
> El *turnaround* promedio baja drásticamente de $109$ a $(10 + 19 + 118)/3 = 49$ (o 79 según la variación de arribos), demostrando la alta sensibilidad de FCFS al orden de llegada.

---

> [!example]- Transcripción de la imagen: Planificación FCFS y efecto convoy.png
> **First-Come, First-Served (FCFS):**
> * Orden de llegada estricto mediante cola FIFO no expropiativa (*non-preemptive*).
> * **Tabla de ejecución:**
>   - $P_1$: Llegada $0$, CPU-burst $100$, Término $100$, Turnaround $= 100 - 0 = 100$.
>   - $P_2$: Llegada $1$, CPU-burst $10$, Término $110$, Turnaround $= 110 - 1 = 109$.
>   - $P_3$: Llegada $2$, CPU-burst $10$, Término $120$, Turnaround $= 120 - 2 = 118$.
> * **Turnaround promedio:** $(100 + 109 + 118) / 3 = 109$.
> * Si $P_2$ y $P_3$ hubiesen llegado antes que $P_1$, el turnaround promedio se reduciría notablemente.
> * **Características:** Simple de implementar, pero produce el **efecto convoy** (*convoy effect*), donde procesos cortos esperan tras un proceso masivo.

> [!example]- Transcripción de la imagen: Planificación SJF y cálculo de turnaround.png
> **Shortest Job First (SJF):**
> * Selecciona el proceso con la ráfaga de CPU (*CPU-burst*) más corta.
> * **Tabla con orden por duración:**
>   - $P_1$: Llegada $0$, CPU-burst $10$, Término $10$, Turnaround $= 10$.
>   - $P_2$: Llegada $2$, CPU-burst $10$, Término $20$, Turnaround $= 18$.
>   - $P_3$: Llegada $1$, CPU-burst $100$, Término $120$, Turnaround $= 119$.
> * **Turnaround promedio:** $(10 + 18 + 119) / 3 = 49$.
> * **Propiedades:**
>   - Teóricamente **óptimo** para minimizar el tiempo de retorno promedio.
>   - Versión preemptive: *Shortest Remaining Time Next* (SRTN / STCF).
>   - **Desventaja:** Requiere conocer la duración del CPU-burst de antemano y genera riesgo de **inanición** (*starvation*) para procesos largos si siguen llegando trabajos cortos.

---

> [!tip] Complemento: Comparativa analítica entre FCFS y SJF/SRTN
> 
> ```
> Diagrama de Gantt - Efecto Convoy (FCFS):
> [        P1 (100)        ][ P2 (10) ][ P3 (10) ]
> 0                       100        110        120
> 
> Diagrama de Gantt - SJF (Óptimo en Turnaround):
> [ P1 (10) ][ P2 (10) ][        P3 (100)        ]
> 0         10         20                       120
> ```
> 
> * **Efecto convoy (*Convoy Effect*):** Análogo a autos rápidos atascados detrás de un camión lento en una carretera de un solo carril. Los dispositivos de I/O quedan ociosos mientras el proceso CPU-bound acapara el procesador.
> * **Inanición (*Starvation* / Pasa hambre):** Ocurre cuando un proceso listo nunca recibe CPU porque el algoritmo siempre favorece procesos con ráfagas menores.

---

## Preguntas de repaso

> [!question]- ¿Qué es el efecto convoy y por qué afecta negativamente a FCFS?
> Ocurre cuando un proceso largo con alto uso de CPU se ubica al frente de la cola FIFO, obligando a todos los procesos cortos a esperar. Esto aumenta drásticamente el tiempo de retorno promedio y deja los dispositivos de entrada/salida subutilizados.

> [!question]- ¿Por qué no es posible implementar un SJF puro en sistemas de propósito general?
> Porque el sistema operativo no puede conocer con exactitud la duración del próximo ciclo de CPU (*CPU-burst*) de un programa arbitrario antes de ejecutarlo. Solo se pueden hacer estimaciones estadísticas (por ejemplo, mediante medias móviles exponenciales).

> [!question]- ¿Cuál es la variante expropiativa de SJF y cómo funciona?
> Es **SRTN** (*Shortest Remaining Time Next*) o **STCF** (*Shortest Time-to-Completion First*). Si llega un nuevo proceso cuya ráfaga restante es menor que el tiempo que le queda al proceso en ejecución, el planificador desaloja al proceso actual para atender al nuevo.
