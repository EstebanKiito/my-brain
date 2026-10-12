---
ramo: "Sistemas Operativos y Redes"
tema: "Planificación de CPU"
tags:
  - ssoo
  - scheduling
  - preemptive
  - batch
  - metricas
  - origen/complemento
prerrequisitos:
  - "[[01 - Niveles de planificación y ciclo de ráfagas CPU-IO]]"
---

# Clasificación de planificadores y métricas de rendimiento

Existen muchos schedulers, y para compararlos conviene clasificarlos con dos preguntas: **¿puede el SO quitarle la CPU a un proceso?** y **¿qué se quiere optimizar?** La respuesta a la segunda pregunta define las **métricas** con que se mide si un algoritmo es bueno.

## Por tipo de interrupción: expropiativo o colaborativo

| | **Preemptive** (expropiativo) | **Non-preemptive** (colaborativo o no expropiativo) |
|---|---|---|
| Cómo se libera la CPU | El SO usa interrupciones, por ejemplo del **timer**, para decidir cuándo sacar a un proceso | El proceso ejecuta hasta que **deja voluntariamente** la CPU (por ejemplo, con `yield`), **se bloquea** en I/O o **termina** |
| Riesgo | Más cambios de contexto (*overhead*) | Un proceso que nunca cede la CPU la monopoliza |

Los más usados son los **expropiativos**: es mejor que el SO pueda expropiar la CPU que depender de que cada proceso la suelte por su cuenta. Con un scheduler colaborativo, un programa con un ciclo infinito (`while (1);`) congelaría al resto.

![Clasificación de planificadores expropiativos y colaborativos](adjuntos/Clasificaci%C3%B3n%20de%20planificadores%20expropiativos%20y%20colaborativos.png)

> [!example]- Transcripción de la imagen
> "Por tipo de interrupción". **Preemptive (expropiativo):** utiliza interrupciones (ej: de reloj (timer)) para decidir cuándo sacar a un proceso de ejecución. **Non-Preemptive (colaborativo o no-expropiativo):** permite que un proceso ejecute hasta que el proceso deja voluntariamente la CPU, se bloquea en I/O o termina.

## Por objetivo: batch, interactivo o tiempo real

| Tipo | Idea | Objetivos | Ejemplo |
|---|---|---|---|
| **Batch** (por lotes) | Sin interacción; el trabajo se procesa más tarde | CPU lo más ocupada posible, minimizar *turnaround*, maximizar *throughput* | Esperar a la noche y transcribir de una vez un lote de 40 llamadas; una compra cuyo pedido se procesa y despacha días después |
| **Interactivo** | Hay un usuario esperando; mezcla de ambos extremos | Minimizar el **tiempo de respuesta**, satisfacer a los usuarios | Un escritorio o un navegador |
| **Tiempo real** (*real time*) | Se procesa en el momento en que llega | Tiempo de respuesta **predecible**, cumplir **deadlines** | Transcribir una llamada apenas termina; urgencias en un hospital; el pago de una compra (redirección a Webpay), que debe resolverse en el momento |

![Objetivos de planificación batch interactiva y tiempo real](adjuntos/Objetivos%20de%20planificaci%C3%B3n%20batch%20interactiva%20y%20tiempo%20real.png)

> [!example]- Transcripción de la imagen
> "Por Objetivo". **Batch:** trabajo por lotes, sin interacción; mantener la CPU lo más ocupada posible; minimizar *turnaround time* (tiempo desde envío hasta término); maximizar *throughput* (número de trabajos por hora). **Interactive:** minimizar tiempo de respuesta; satisfacer usuarios. **Real Time:** tiempo de respuesta debe ser predecible; alcanzar *deadlines*.

## Métricas

![Conceptos y métricas clave de planificación](adjuntos/Conceptos%20y%20m%C3%A9tricas%20clave%20de%20planificaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> **BATCH** = un proceso batch es sin ninguna interacción. **Turnaround** = tiempo que el proceso permanece en el sistema. **Throughput** = cantidad de procesos terminados por unidad de tiempo.

| Métrica | Definición | Se busca |
|---|---|---|
| **Turnaround time** | $T_{\text{término}} - T_{\text{llegada}}$: todo el tiempo que el proceso está en el sistema | Minimizar |
| **Response time** | $T_{\text{primera ejecución}} - T_{\text{llegada}}$: cuánto espera hasta tocar la CPU por primera vez | Minimizar |
| **Waiting time** | $T_{\text{turnaround}} - T_{\text{CPU}}$: tiempo total en la cola Ready | Minimizar |
| **Throughput** | $\frac{\text{procesos terminados}}{\text{tiempo}}$, en general por segundo | Maximizar |
| **Utilización de CPU** | Fracción del tiempo en que la CPU hace trabajo útil | Maximizar |

**Ejemplo.** A llega en $t=0$ y necesita 5 unidades de CPU; B llega en $t=1$ y necesita 3. Si se atienden por orden de llegada, A corre de 0 a 5 y B de 5 a 8:

| Proceso | Turnaround | Response | Waiting |
|---|---|---|---|
| A | $5 - 0 = 5$ | $0$ | $0$ |
| B | $8 - 1 = 7$ | $5 - 1 = 4$ | $7 - 3 = 4$ |

El throughput es 2 procesos en 8 unidades, es decir 0,25 procesos por unidad de tiempo.

## Preguntas de repaso

> [!question]- ¿Por qué los SO de propósito general usan schedulers expropiativos?
> Porque con uno colaborativo la CPU solo se libera cuando el proceso la cede, se bloquea o termina, y un proceso en un ciclo infinito la monopolizaría. Con el timer, el SO siempre recupera el control.

> [!question]- ¿Qué diferencia hay entre turnaround time y response time?
> El turnaround mide todo el tiempo en el sistema, desde la llegada hasta el término. El response time mide solo cuánto tarda en recibir la CPU por primera vez, que es lo que percibe un usuario interactivo.

> [!question]- ¿Por qué un sistema batch y uno interactivo optimizan cosas distintas?
> En batch nadie está esperando una respuesta, así que importa terminar muchos trabajos (throughput) y rápido en total (turnaround). En un sistema interactivo hay un usuario esperando, así que lo que importa es responder pronto aunque el total tarde un poco más.

> [!question]- ¿Qué exige un sistema de tiempo real que no exigen los otros?
> Que el tiempo de respuesta sea predecible y que se cumplan los plazos (*deadlines*). No basta con ser rápido en promedio.
