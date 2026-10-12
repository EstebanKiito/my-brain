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
  - origen/complemento
prerrequisitos:
  - "[[02 - Clasificación de planificadores y métricas de rendimiento]]"
---

# Planificación FCFS y SJF

Los dos algoritmos más simples para sistemas *batch* responden a la pregunta "¿quién sigue?" de formas opuestas: **FCFS** atiende por orden de llegada, mientras que **SJF** atiende primero al más corto. Compararlos muestra por qué el orden importa tanto para el *turnaround*, la métrica que más interesa en batch.

## FCFS: orden de llegada

**FCFS** (*First-Come, First-Served*), también llamado **FIFO**, atiende a los procesos en el orden en que llegan, con una cola FIFO. Es **no expropiativo** y **simple**, pero **poco predecible**, porque el resultado depende de quién llegó primero.

El turnaround de cada proceso es *el instante en que salió menos el instante en que llegó*. Con un proceso largo adelante:

| Proceso | Llegada | CPU-burst | Término | Turnaround |
|---|---|---|---|---|
| P1 | 0 | 100 | 100 | $100 - 0 = 100$ |
| P2 | 1 | 10 | 110 | $110 - 1 = 109$ |
| P3 | 2 | 10 | 120 | $120 - 2 = 118$ |

El promedio es **109**. Los procesos cortos esperan detrás del largo, igual que autos detrás de un camión en una carretera de un carril: es el **efecto convoy** (*convoy effect*). Además, mientras el proceso largo acapara la CPU, los procesos cortos que harían I/O no la piden, y los dispositivos quedan ociosos. Si P2 hubiera llegado en $t=0$ y P1 en $t=1$, el promedio bajaría a **79**. Y si los dos cortos llegan antes que el largo (llegadas 0, 1 y 2 con ráfagas 10, 10 y 100), los turnaround son 10, 19 y 118, con promedio **49**.

![Planificación FCFS y efecto convoy](adjuntos/Planificaci%C3%B3n%20FCFS%20y%20efecto%20convoy.png)

> [!example]- Transcripción de la imagen
> "Orden de llegada. Cola FIFO." La tabla P1/P2/P3 de arriba (llegadas 0, 1, 2; ráfagas 100, 10, 10; término 100, 110, 120; turnaround 100, 109, 118) y un diagrama de Gantt: P1 de 0 a 100, P2 de 100 a 110, P3 de 110 a 120. "Turnaround time promedio: **109**. Si P2 hubiese llegado en t=0, y P1 hubiese llegado en t=1, entonces turnaround time promedio → 79". Non-Preemptive · Simple · Poco predecible. Convoy effect.

## SJF: el más corto primero

La lección de FCFS es que conviene poner primero al más corto. **SJF** (*Shortest Job First*) lo hace de forma sistemática: cuando la CPU se libera, elige el proceso listo con la ráfaga de CPU más corta.

| Proceso | Llegada | CPU-burst | Término | Turnaround |
|---|---|---|---|---|
| P1 | 0 | 10 | 10 | 10 |
| P2 | 2 | 10 | 20 | 18 |
| P3 | 1 | 100 | 120 | 119 |

En $t=0$ solo está P1. Cuando termina, en $t=10$, compiten P2 y P3, y gana P2 por ser más corto. El promedio es **49**.

![Planificación SJF y cálculo de turnaround](adjuntos/Planificaci%C3%B3n%20SJF%20y%20c%C3%A1lculo%20de%20turnaround.png)

> [!example]- Transcripción de la imagen
> "El más corto primero." Tabla con P1 (llegada 0, ráfaga 10, término 10, turnaround 10), P2 (2, 10, 20, 18) y P3 (1, 100, 120, 119). Gantt: P1 de 0 a 10, P2 de 10 a 20, P3 de 20 a 120. "Turnaround time promedio: **49**". Versión preemptive: Shortest Remaining Time Next, que elige al que le queda menos tiempo · No sabemos cuánto demora cada CPU-burst · Óptimo · Potencial inanición (*starvation*) de procesos largos.

Propiedades de SJF:

- **Es óptimo** para minimizar el turnaround promedio.
- Su versión expropiativa es **SRTN** (*Shortest Remaining Time Next*, también llamada STCF, *Shortest Time-to-Completion First*): si llega un proceso al que le queda menos tiempo que al actual, lo desaloja.
- **No sabemos cuánto demora cada CPU-burst**, así que en la práctica solo se puede estimar.

> [!warning] Inanición (*starvation*)
> Con SJF, un proceso largo puede quedarse **sin ser atendido por mucho tiempo**, "pasando hambre", si siguen llegando procesos cortos. Y ese proceso largo puede ser importante: SJF no considera la importancia, solo la duración.

## Simulación

```python
def planificar(procesos, sjf=False):
    """procesos: lista de (nombre, llegada, rafaga). No expropiativo."""
    pendientes, t, turnaround = list(procesos), 0, {}
    while pendientes:
        listos = [p for p in pendientes if p[1] <= t] or [min(pendientes, key=lambda p: p[1])]
        elegido = min(listos, key=lambda p: (p[2], p[1]) if sjf else (p[1],))
        t = max(t, elegido[1]) + elegido[2]          # corre hasta terminar
        turnaround[elegido[0]] = t - elegido[1]
        pendientes.remove(elegido)
    return turnaround, sum(turnaround.values()) / len(turnaround)

print(planificar([("P1", 0, 100), ("P2", 1, 10), ("P3", 2, 10)]))            # promedio 109.0
print(planificar([("P1", 0, 10), ("P2", 2, 10), ("P3", 1, 100)], sjf=True))  # promedio 49.0
```

## Preguntas de repaso

> [!question]- ¿Qué es el efecto convoy y por qué afecta a FCFS?
> Es cuando procesos cortos quedan esperando detrás de uno largo que llegó antes. FCFS no reordena, así que el turnaround promedio sube mucho: 109 en el ejemplo, contra 49 si los cortos van primero.

> [!question]- ¿Por qué SJF no se puede implementar tal cual en un SO de propósito general?
> Porque el SO no sabe de antemano cuánto durará la próxima ráfaga de CPU de un proceso. Solo puede estimarla a partir del comportamiento pasado.

> [!question]- ¿Qué hace SRTN distinto de SJF?
> Es expropiativo: si llega un proceso al que le queda menos tiempo que al que está corriendo, lo desaloja. SJF, en cambio, deja terminar al proceso actual.

> [!question]- Calcula el turnaround promedio con FCFS para llegadas 0, 1, 2 y ráfagas 10, 10, 100.
> Terminan en 10, 20 y 120. Los turnaround son 10, 19 y 118, y el promedio es $147/3 = 49$.
