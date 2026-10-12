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
  - origen/complemento
prerrequisitos:
  - "[[02 - Clasificación de planificadores y métricas de rendimiento]]"
  - "[[03 - Planificación FCFS y SJF]]"
---

# Planificación Round Robin y sistemas interactivos

En un sistema interactivo hay una persona esperando. No le importa tanto cuándo *termina* su programa como cuándo *empieza a responder*. Por eso la métrica que manda es el **tiempo de respuesta**, y el algoritmo diseñado para minimizarlo es **Round Robin** (RR).

## La métrica: tiempo de respuesta

El **tiempo de respuesta** (*response time*) es el tiempo **desde la llegada a la cola hasta la primera ejecución**: $T_{\text{respuesta}} = T_{\text{inicio}} - T_{\text{llegada}}$.

Con FCFS, tres procesos de 5 unidades que llegan en 0, 1 y 2 se atienden uno tras otro:

| Proceso | Llegada | CPU-burst | Término | Turnaround | Inicio | Respuesta |
|---|---|---|---|---|---|---|
| P1 | 0 | 5 | 5 | 5 | 0 | 0 |
| P2 | 1 | 5 | 10 | 9 | 5 | 4 |
| P3 | 2 | 5 | 15 | 13 | 10 | 8 |

Turnaround promedio **9**, respuesta promedio **4**. El último en llegar espera 8 unidades sin recibir ni un instante de CPU, y para un usuario eso se siente como un programa colgado.

![Métrica de tiempo de respuesta en sistemas interactivos](adjuntos/M%C3%A9trica%20de%20tiempo%20de%20respuesta%20en%20sistemas%20interactivos.png)

> [!example]- Transcripción de la imagen
> "Métrica: tiempo de respuesta (response time). Tiempo desde llegada (a la cola) hasta primera ejecución." La tabla de arriba (P1, P2, P3 con llegadas 0, 1, 2, ráfagas de 5, términos 5, 10, 15, turnaround 5, 9, 13, inicio 0, 5, 10, respuesta 0, 4, 8) y un Gantt con P1 de 0 a 5, P2 de 5 a 10 y P3 de 10 a 15. Turnaround time promedio: 9. Response time promedio: 4.

## Round Robin: un turno para cada uno

RR da a cada proceso un **turno** (*quantum* o *time slice*) de largo $q$. Cuando se acaba, el *timer* lo interrumpe y el proceso pasa al **final de la cola Ready**. Así, cada cierto tiempo a cada proceso le toca: todos avanzan un poco y el usuario percibe que el sistema le presta atención a cada programa a la vez. Como todos avanzan, todos van a terminar: nadie queda sin CPU.

Con $q = 1$ y tres procesos de 5 unidades que llegan casi juntos (0; 0,1; 0,2):

| Proceso | Llegada | Término | Turnaround | Inicio | Respuesta |
|---|---|---|---|---|---|
| P1 | 0 | 13 | 13 | 0 | 0 |
| P2 | 0,1 | 14 | 13,9 | 1 | 0,9 |
| P3 | 0,2 | 15 | 14,8 | 2 | 1,8 |

La respuesta promedio baja a **0,9**, pero el turnaround promedio sube a **13,9**: con FIFO habrían salido antes. RR **cambia tiempo en el sistema por un tiempo de respuesta más bajo**.

![Planificación Round Robin con quantum unitario](adjuntos/Planificaci%C3%B3n%20Round%20Robin%20con%20quantum%20unitario.png)

> [!example]- Transcripción de la imagen
> "Un turno (quantum, time slice) para cada uno. Ejemplo con q=1". La tabla de arriba y un Gantt que alterna P1, P2, P3 en franjas de 1 unidad hasta t=15. Turnaround time promedio: 13.9. Response time promedio: 0.9. Con *n* procesos, cada uno recibe $1/n$ de CPU (*Fair!*). Ningún proceso espera más de $(n-1) \times q$ para ejecutar. Altamente dependiente de la elección de *q* (¿qué pasa si *q* es muy pequeño o muy grande?).

Propiedades:

- Con $n$ procesos, **cada uno recibe $1/n$ de la CPU**: es justo (*fair*).
- **Ningún proceso espera más de $(n-1) \times q$** para volver a ejecutar.
- El comportamiento depende mucho de la elección de $q$.

> [!warning] Elegir el quantum
> - **$q$ muy grande:** ningún proceso alcanza a agotar su turno y RR **degenera en FCFS**, con mal tiempo de respuesta.
> - **$q$ muy pequeño:** se cambia de contexto todo el tiempo y el *overhead* se come la CPU.
>
> $q$ debe ser bastante mayor que el costo de un cambio de contexto, pero lo bastante corto para que la interacción se sienta inmediata.

## Simulación

```python
from collections import deque

def round_robin(procesos, q):
    """procesos: lista de (nombre, llegada, rafaga) ordenada por llegada."""
    restante = {n: r for n, _, r in procesos}
    llegada = {n: a for n, a, _ in procesos}
    cola, t, i, inicio, fin = deque(), 0.0, 0, {}, {}
    while len(fin) < len(procesos):
        while i < len(procesos) and procesos[i][1] <= t:   # admitir a los que llegaron
            cola.append(procesos[i][0]); i += 1
        if not cola:
            t = procesos[i][1]; continue
        p = cola.popleft()
        inicio.setdefault(p, t)
        corre = min(q, restante[p])
        t += corre; restante[p] -= corre
        while i < len(procesos) and procesos[i][1] <= t:   # llegadas durante el turno
            cola.append(procesos[i][0]); i += 1
        if restante[p] > 0:
            cola.append(p)                                 # vuelve al final de la cola
        else:
            fin[p] = t
    n = len(procesos)
    turnaround = sum(fin[p] - llegada[p] for p in fin) / n
    respuesta = sum(inicio[p] - llegada[p] for p in inicio) / n
    return round(turnaround, 2), round(respuesta, 2)

print(round_robin([("P1", 0, 5), ("P2", 0.1, 5), ("P3", 0.2, 5)], q=1))    # (13.9, 0.9)
print(round_robin([("P1", 0, 5), ("P2", 0.1, 5), ("P3", 0.2, 5)], q=100))  # (9.9, 4.9): como FCFS
```

## Preguntas de repaso

> [!question]- ¿Qué gana y qué pierde Round Robin frente a FCFS?
> Gana tiempo de respuesta, porque todos reciben CPU pronto: 0,9 contra 4 en los ejemplos. Pierde turnaround, porque al intercalarlos todos terminan más tarde: 13,9 contra 9.

> [!question]- ¿Qué pasa si el quantum es muy grande o muy pequeño?
> Si es muy grande, RR se comporta como FCFS y la interactividad se pierde. Si es muy pequeño, la CPU pasa la mayor parte del tiempo haciendo cambios de contexto.

> [!question]- Con 4 procesos y $q = 20$ ms, ¿cuánto puede esperar como máximo un proceso para volver a ejecutar?
> $(n-1) \times q = 3 \times 20 = 60$ ms.

> [!question]- ¿Por qué Round Robin no produce inanición?
> Porque la cola es circular: cada proceso que agota su turno vuelve al final y todos los que están delante también reciben solo un turno. Así, cada proceso vuelve a ejecutar en a lo más $(n-1) \times q$.
