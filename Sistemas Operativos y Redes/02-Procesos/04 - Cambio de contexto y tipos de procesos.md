---
ramo: Sistemas Operativos y Redes
tema: Procesos
tags: [so/procesos, origen/complemento]
prerrequisitos: ["[[02 - Bloque de control de procesos y tabla de procesos|Bloque de control de procesos y tabla de procesos]]", "[[03 - Estados de un proceso y ciclo de vida|Estados de un proceso y ciclo de vida]]"]
---
# Cambio de contexto y tipos de procesos

Para que varios procesos compartan una CPU, el sistema operativo tiene que poder detener uno y poner otro en su lugar sin que ninguno lo note. Esa operación, el **cambio de contexto**, es lo que hace posible el multitasking, pero no es gratis. Cuánto conviene alternar depende además de qué tipo de proceso se tenga: uno que calcula sin parar o uno que pasa esperando entrada y salida.

## El cambio de contexto (*context switch*)

Un **cambio de contexto** es cambiar el proceso que está corriendo en la CPU. El SO solo actúa tras una interrupción (una syscall, el *timer* o algún evento), y entonces:

1. Almacena el estado de los registros de P1 en **PCB1**. P1 queda "en pausa".
2. Restaura el estado de los registros de P2 desde **PCB2**: vuelve a cargar los datos y variables que tenía.
3. P2 continúa su ejecución como si nunca se hubiera detenido.

![Secuencia temporal del cambio de contexto](adjuntos/Secuencia%20temporal%20del%20cambio%20de%20contexto.png)

> [!example]- Transcripción de la imagen
> Arriba, los cuatro pasos del multitasking: el SO actúa luego de una interrupción (syscall, timer, evento…), almacena el estado de registros de P1 en PCB1 (P1 queda "en pausa"), restaura el estado de registros desde PCB2, y el proceso P2 continúa su ejecución. Abajo, una línea de tiempo con dos procesos. P1 está en *CPU (running)* en *user space* mientras P2 está *en espera (ready)*. Una **INTERRUPCION** lleva a *CPU (kernel)* en *kernel space*: "Almacena estado de P1 en PCB1 / Restaura estado de P2 desde PCB2". Luego P2 pasa a *running* y P1 queda en espera. Una segunda interrupción hace lo inverso ("Almacena estado de P2 en PCB2 / Restaura estado de P1 desde PCB1") y P1 vuelve a *running*.

Un ejemplo: si tienes un juego abierto y cambias a otra aplicación, el estado del juego queda guardado en su PCB mientras otros procesos usan la CPU. Al volver, el SO lo restaura desde ahí.

> [!warning] Siempre hay *overhead*
> Mientras el kernel guarda y restaura estados, la CPU no avanza en ningún programa de usuario: es tiempo extra que se paga en cada cambio. Además del costo directo (copiar registros, incluidos los de coma flotante y SIMD, cambiar el espacio de direcciones, en x86 el registro `CR3`), hay un **costo indirecto**: las cachés (L1, L2, L3) y la TLB quedan con datos del proceso anterior, así que el nuevo proceso sufre una racha de fallos de caché hasta "calentarlas". Por eso cambiar de contexto demasiado seguido degrada el rendimiento.

## Tipos de procesos según su carga

Los procesos alternan entre dos fases: **uso de CPU** (*CPU burst*) y **espera por I/O** (*I/O burst*). En la mayoría domina una de las dos:

| | **CPU-bound** | **I/O-bound** |
|---|---|---|
| Dominado por | Ráfagas largas de cómputo | Esperas de entrada y salida |
| Interacción | Corre solo, sin interacción humana; es una "caja oscura" que recibe datos y entrega un resultado | Depende constantemente de recibir y entregar datos |
| Ejemplos | Cálculos matemáticos, entrenar un modelo de *machine learning* | WhatsApp (si no hay input, no hay mensaje que enviar), un juego (recibe y entrega datos todo el tiempo) |
| Recursos | Necesita mucha CPU | Usa poca CPU por ráfaga; pasa mucho tiempo en *Waiting* |

Esta distinción importa para la planificación: un proceso I/O-bound necesita la CPU poco rato, pero seguido y rápido (para que la interacción se sienta fluida), mientras que uno CPU-bound aprovecha bloques largos. Se retoma en [[01 - Niveles de planificación y ciclo de ráfagas CPU-IO|ráfagas CPU-I/O]].

## Preguntas de repaso

> [!question]- ¿Qué hace exactamente el SO en un cambio de contexto?
> Tras una interrupción, guarda los registros del proceso actual en su PCB, restaura los del siguiente desde su propio PCB y le devuelve la CPU, para que continúe donde había quedado.

> [!question]- ¿Por qué el cambio de contexto es *overhead* y por qué tiene costos indirectos?
> Mientras ocurre, la CPU no avanza en ningún programa de usuario. Además, al cambiar de proceso las cachés y la TLB quedan con datos del anterior, y el nuevo proceso sufre fallos de caché hasta volver a llenarlas.

> [!question]- ¿Qué diferencia a un proceso CPU-bound de uno I/O-bound? Da un ejemplo de cada uno.
> El CPU-bound pasa la mayor parte del tiempo calculando, como el entrenamiento de un modelo de ML. El I/O-bound pasa la mayor parte del tiempo esperando entrada o salida, como una app de mensajería que espera que el usuario escriba.

> [!question]- ¿Por qué un proceso I/O-bound pasa mucho tiempo en estado Waiting?
> Porque sus ráfagas de CPU son cortas y después de cada una necesita un evento externo (input del usuario, red, disco). Mientras no llega, no puede avanzar.
