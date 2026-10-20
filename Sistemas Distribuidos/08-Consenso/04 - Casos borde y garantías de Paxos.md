---
ramo: "Sistemas Distribuidos"
tema: "Consenso"
tags:
  - sd/consenso
  - origen/complemento
prerrequisitos:
  - "[[03 - Paxos: aceptar y aprender]]"
---

# Casos borde y garantías de Paxos

Las reglas de Paxos se entienden mejor cuando hay **varios proponentes** a la vez o nodos que se caen a mitad de camino. Tres ejemplos muestran qué ocurre: una propuesta interrumpida, una acción aceptada que se sobrescribe y un **livelock**. Después vienen las garantías del algoritmo y su uso en sistemas reales.

En los diagramas, las filas a, b y c son tres aceptantes y cada casilla muestra el identificador prometido o la operación aceptada. Los tres ejemplos se reprodujeron con una simulación en Python que dio los mismos resultados.

## Ejemplo 1: interrumpir a un proponente

![Paxos interrumpe a un proponente](adjuntos/Paxos%20interrumpe%20a%20un%20proponente.png)

> [!example]- Transcripción de la imagen
> Un proponente envía `prepare(1)` y los tres aceptantes prometen 1. Otro proponente envía `prepare(2)` y todos pasan a prometer 2. Cuando llega `accept(A1, 1)`, los tres lo rechazan (señal de prohibido). Luego `accept(A2, 2)` es aceptado por todos, que quedan con $A_2, 2$, y el aprendiz dice "Me quedo con `accept(A2, 2)`".

El primer proponente tenía mayoría, pero antes de enviar su accept apareció un prepare mayor. Como los aceptantes prometieron no aceptar nada menor a 2, su accept no prospera.

## Ejemplo 2: sobrescribir una acción aceptada

![Paxos sobrescribe una acción aceptada](adjuntos/Paxos%20sobrescribe%20una%20acci%C3%B3n%20aceptada.png)

> [!example]- Transcripción de la imagen
> `prepare(1)` llega a a, b y c (todos prometen 1). Cuando llega `prepare(2)`, el nodo a está caído, así que solo b y c pasan a 2. Al volver, a acepta `accept(A1, 1)` (queda con $A_1, 1$) y b y c lo rechazan. Después `accept(A2, 2)` llega a los tres y todos quedan con $A_2, 2$: "Me quedo con `accept(A2, 2)`".

El prepare(1) sí tuvo consenso (los tres prometieron), pero su operación $A_1$ solo la aceptó a, que no supo del prepare(2). Como $A_1$ nunca alcanzó mayoría, el segundo proponente (que no escuchó de a) envió su propia $A_2$, que reemplaza a $A_1$ incluso en a.

> [!tip] Lo que enseña
> Que un **prepare** logre consenso **no asegura** que su operación sea la final. Lo único definitivo es lo que una mayoría **acepta** y los aprendices consolidan.

## Ejemplo 3: livelock

![Livelock en Paxos](adjuntos/Livelock%20en%20Paxos.png)

> [!example]- Transcripción de la imagen
> Dos proponentes se alternan: `prepare(1)`, `prepare(2)`, `accept(A1, 1)` rechazado, `prepare(3)`, `accept(A2, 2)` rechazado, `prepare(4)`, `accept(A1, 3)` rechazado… Los aceptantes pasan de 1 a 2, a 3 y a 4 sin aceptar nunca una operación.

Cada proponente invalida al otro justo antes de su accept. Es un **livelock**: como un deadlock, pero con los nodos **vivos y trabajando**, sin avanzar. Se evita con **timeouts** para llegar a consenso o **retrasando mensajes al azar**, para que un proponente alcance a terminar.

## Garantías

- **Tolerancia a fallos:** con $N$ nodos pueden fallar hasta $\lfloor (N-1)/2 \rfloor$, es decir, menos de la mitad. Con 20 nodos, pueden fallar 9.
- **Tolerancia a particiones:** si la red se divide en dos grupos, el algoritmo sigue funcionando mientras uno de ellos tenga la mayoría.

![Partición de la red en dos grupos](adjuntos/Partici%C3%B3n%20de%20la%20red%20en%20dos%20grupos.png)

> [!example]- Transcripción de la imagen
> Una red de nodos conectados pierde conectividad (*Connectivity Lost*): una línea roja la separa en *Partition A* y *Partition B*, cada una con parte de los nodos.

## Observaciones

- Paxos original acuerda **una sola acción**. Variaciones como **Multi-Paxos** optimizan el proceso para secuencias de acciones.
- El livelock existe, pero se mitiga en la implementación (timeouts, retrasos aleatorios).
- En la vida real: el servicio de bloqueo distribuido **Chubby** de Google usa Paxos para mantener consistentes sus réplicas; **Amazon DynamoDB** lo usa para elegir líderes y lograr consenso; **Apache Cassandra** lo usa solo para sus *Light Weight Transactions* (transacciones condicionales).

> [!warning] Solo caídas, no traiciones
> Paxos no está diseñado, por defecto, para el [[05 - Problema de los generales bizantinos|problema de los generales bizantinos]]. Además, tolera más que caídas: también particiones y mensajes perdidos. Y una operación no queda consolidada cuando la acepta la mayoría, sino cuando los aprendices lo verifican.

## Preguntas de repaso

> [!question]- ¿Qué diferencia un livelock de un deadlock?
> En un deadlock los nodos están bloqueados esperándose. En un livelock siguen activos e intercambian mensajes, pero se anulan mutuamente y nunca progresan.

> [!question]- Con 7 nodos, ¿cuántos pueden fallar sin que Paxos deje de funcionar y por qué?
> 3: los 4 restantes siguen siendo mayoría (más del 50 % de 7). Con 4 caídos, nadie podría reunir mayoría.

> [!question]- Si la red se parte en grupos de 3 y 2 nodos, ¿qué grupo puede seguir decidiendo?
> El de 3, porque tiene la mayoría de los 5 nodos. El de 2 no puede reunir más del 50 %, así que no consolida nada, y eso evita que ambos lados decidan cosas distintas.
