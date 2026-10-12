---
ramo: "Sistemas Operativos y Redes"
tema: "Planificación de CPU"
tags:
  - ssoo
  - scheduling
  - cpu
  - dispatcher
  - swapping
  - origen/complemento
prerrequisitos:
  - "[[03 - Estados de un proceso y ciclo de vida]]"
  - "[[04 - Cambio de contexto y tipos de procesos]]"
---

# Niveles de planificación y ciclo de ráfagas CPU-I/O

Con muchos procesos en memoria y una CPU que atiende solo uno a la vez, el sistema operativo debe decidir constantemente **quién corre a continuación**. Esa decisión es el **scheduling** (planificación), y la toma el **scheduler** (planificador). En realidad no es una sola decisión, sino tres, que se toman a distintas escalas de tiempo.

## Tres niveles de scheduler

El scheduler aplica **reglas para elegir qué proceso entra a la CPU** (a un núcleo), es decir, cuál es el mejor candidato de la cola *Ready*. En un computador funcionan siempre tres planificadores:

| Nivel | Qué hace | Verbo clave |
|---|---|---|
| **Largo plazo** (*long-term*) | Admite procesos en la cola *Ready* y así determina el **grado de multiprogramación** (cuántos procesos hay en memoria) | **Pone** procesos en Ready |
| **Mediano plazo** (*medium-term*) | Modifica temporalmente el grado de multiprogramación haciendo **swapping**: copia procesos de RAM a disco y de disco a RAM | **Saca** procesos de memoria |
| **Corto plazo** (*short-term*, o *dispatcher*) | **Elige** qué proceso de la cola *Ready* se ejecuta y realiza el **cambio de contexto** | **Elige** quién corre |

La cola *Ready* vive en la **RAM** (memoria principal). El **disco** (memoria secundaria) es adonde el planificador de mediano plazo envía los procesos que saca de memoria: al final, el que saca lo que no se está usando es el de mediano plazo.

El de corto plazo actúa con muchísima frecuencia (en cada interrupción del *timer*, cada pocos milisegundos), así que debe ser muy rápido. El de largo plazo actúa con mucha menor frecuencia.

![Niveles de scheduling y colas del sistema operativo](adjuntos/Niveles%20de%20scheduling%20y%20colas%20del%20sistema%20operativo.png)

> [!example]- Transcripción de la imagen
> Los *Incoming jobs* llegan a una cola y pasan por el **Long term scheduling** hacia la **Ready queue**. Desde ahí, el **Short term scheduling** los lleva a la **CPU**, de donde salen por *Release* (terminan), por *Time out* (vuelven a la Ready queue) o por *Event wait* (van a la **Blocked queue**). Desde la Blocked queue, *Event occurs* los devuelve a Ready. El **Medium term scheduling** mueve procesos hacia y desde dos colas en disco: **Ready, suspend queue** y **Blocked, suspend queue**.

> [!warning] Scheduling es *overhead*
> Planificar y cambiar de contexto no avanza ningún programa. Si el scheduler o el cambio de contexto toman más tiempo que el propio proceso, o si se le asigna muy poco tiempo a cada uno, el sistema pasa más tiempo administrando que trabajando. Y si hay demasiados procesos compitiendo por memoria (un trabajo del largo plazo), la contención se manifiesta como ***thrashing***.

## Ráfagas de CPU y de I/O

No todos los procesos se comportan igual. Todos alternan entre dos fases, **uso de CPU** (*CPU burst*) y **espera por I/O** (*I/O burst*), pero suelen estar dominados por una de ellas:

- **CPU-bound:** ráfagas de CPU largas y pocas esperas.
- **I/O-bound:** ráfagas de CPU cortas, separadas por esperas frecuentes de I/O.

![Alternancia entre ráfagas de CPU y de entrada y salida](adjuntos/Alternancia%20entre%20r%C3%A1fagas%20de%20CPU%20y%20de%20entrada%20y%20salida.png)

> [!example]- Transcripción de la imagen
> "No todos los procesos se comportan igual. Alternan entre dos fases: uso de CPU (CPU-burst) y espera por I/O (I/O-burst). Procesos suelen estar dominados por una u otra etapa". Abajo, dos líneas de tiempo. La de arriba tiene barras largas (*Long CPU burst*) separadas por esperas breves. La de abajo tiene barras muy cortas (*Short CPU burst*) separadas por esperas largas (*Waiting for I/O*).

## Utilización de CPU con multiprogramación

El tiempo que los procesos pasan esperando I/O deja la CPU ociosa, y **una CPU bajo el 100% está subutilizada**. Si cada proceso pasa una fracción $p$ de su tiempo esperando I/O, la probabilidad de que los $n$ procesos en memoria estén esperando **todos a la vez** es $p^n$. Por lo tanto:

$$\text{Utilización de CPU} = 1 - p^n$$

Con procesos I/O-bound que esperan el 80% del tiempo ($p = 0{,}8$):

| $n$ procesos | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Utilización | 20% | 36% | 48,8% | 59% | 67,2% |

Esto explica la multiprogramación: con más procesos en memoria, es menos probable que todos estén esperando al mismo tiempo. Pero cada proceso adicional ocupa memoria, y ese equilibrio es justamente el que administran los planificadores de largo y mediano plazo.

## Preguntas de repaso

> [!question]- ¿Qué decide cada uno de los tres planificadores?
> El de largo plazo decide qué procesos se admiten en memoria (el grado de multiprogramación). El de mediano plazo saca procesos a disco o los trae de vuelta (swapping). El de corto plazo elige qué proceso de la cola Ready usa la CPU y hace el cambio de contexto.

> [!question]- ¿Por qué el planificador de corto plazo tiene que ser muy rápido?
> Porque se ejecuta en cada cambio de contexto, muchas veces por segundo, y todo su tiempo es *overhead*: no avanza ningún programa de usuario.

> [!question]- Si $p = 0{,}5$, ¿cuál es la utilización de CPU con 3 procesos en memoria?
> $1 - 0{,}5^3 = 1 - 0{,}125 = 0{,}875$, es decir, 87,5%.

> [!question]- ¿Qué es el thrashing y qué nivel de planificación ayuda a evitarlo?
> Es la contención por memoria cuando hay demasiados procesos: el sistema pasa más tiempo moviendo datos entre RAM y disco que ejecutando. Lo controlan los planificadores de largo plazo (admitiendo menos procesos) y de mediano plazo (sacando procesos a disco).
