---
ramo: "Sistemas Distribuidos"
tema: "Relojes lógicos y estados globales"
tags:
  - sd/estados-globales
  - origen/complemento
prerrequisitos:
  - "[[01 - Relojes lógicos de Lamport]]"
---

# Estados globales y cortes consistentes

A veces hay que sacar una "foto" de todo el sistema: para guardar un respaldo de una base de datos distribuida, detectar un deadlock o depurar un error. En un computador basta con pausar y copiar la memoria. En un sistema distribuido no hay pausa global ni reloj común, y siempre hay mensajes viajando. La pregunta es qué foto parcial es aceptable: la respuesta es el **corte consistente**.

## Qué es un estado global

Un **estado global** (*global snapshot*) está formado por:

- el **estado local** de cada nodo, y
- los **mensajes en tránsito** en los canales de comunicación.

En un solo computador se elige un tiempo $X$ y todos los procesos guardan su estado en ese instante. En un sistema distribuido, determinar esa instantánea es difícil porque:

- casi siempre hay mensajes en tránsito;
- el retraso entre mensajes es inevitable;
- es difícil mantener los nodos sincronizados en todo momento;
- es casi imposible "pausar" todos los nodos en el mismo instante.

Además, la captura debe hacerse **sin detener el sistema** (en paralelo con la operación normal) y sin que los clientes noten nada. Cada nodo guarda su *checkpoint* en un momento distinto, y el objetivo es unificarlos en una foto coherente.

## Para qué sirve

![Usos de un estado global](adjuntos/Usos%20de%20un%20estado%20global.png)

> [!example]- Transcripción de la imagen
> - **Recolección de basura distribuida:** saber si un objeto no tiene referencias en ningún lugar del sistema (por ejemplo, el nodo A referencia un dato que estaría en el nodo B, pero B ya lo eliminó).
> - **Detección de interbloqueos (*deadlocks*):** identificar nodos que esperan recursos indefinidamente.
> - **Depuración de sistemas distribuidos:** entender comportamientos inesperados o violaciones de seguridad transitorias.
> - ***Checkpoints*:** determinar puntos de seguridad para una base de datos distribuida.
> - **Término de algoritmo:** verificar si todos los nodos ya terminaron de ejecutar un algoritmo distribuido.

## Corte consistente

Un **corte** representa un estado global como una "línea" que atraviesa las historias de ejecución de los nodos: lo que queda a la izquierda es el pasado registrado.

> [!tip] Cuándo un corte es consistente
> - Para cada evento incluido, el corte contiene también todos los eventos que lo **precedieron causalmente**.
> - No muestra un **efecto sin causa**: si un mensaje aparece **recibido** antes del corte, también debe aparecer **enviado** antes del corte.

![Corte consistente e inconsistente](adjuntos/Corte%20consistente%20e%20inconsistente.png)

> [!example]- Transcripción de la imagen
> Tres procesos con eventos y mensajes entre ellos, y dos cortes en rojo. El primero (✅) solo deja antes del corte recepciones cuyos envíos también están antes. El segundo (❌) incluye la recepción de un mensaje en el proceso de abajo, pero el envío de ese mensaje, en el proceso de arriba, queda después del corte.

En el corte inválido se registró que llegó un mensaje, pero no que alguien lo envió: es como si el mensaje hubiera aparecido de la nada. Al revés no hay problema: un mensaje enviado antes del corte y recibido después es simplemente un **mensaje en tránsito**, y el estado global debe guardarlo en el canal.

| Situación del mensaje | ¿Consistente? | Qué se registra |
|---|---|---|
| Enviado y recibido antes del corte | Sí | Nada especial |
| Enviado antes, recibido después | Sí | El mensaje, como parte del estado del canal |
| Recibido antes, enviado después | No | Efecto sin causa |

El [[04 - Algoritmo de Chandy-Lamport|algoritmo de Chandy-Lamport]] obtiene un corte consistente de forma distribuida, incluidos los mensajes en tránsito.

> [!warning] Con relojes físicos no basta
> Pedir a todos que guarden su estado "a las 12:00:00" no garantiza consistencia: por la desincronización, un nodo puede guardar después de recibir un mensaje que otro, con el reloj adelantado, envió "después" de su propio guardado.

## Preguntas de repaso

> [!question]- ¿Por qué un estado global incluye los mensajes en tránsito y no solo los estados de los nodos?
> Porque un mensaje enviado y aún no recibido no aparece en ningún estado local. Si no se guarda, al restaurar el sistema desde la foto ese mensaje se pierde.

> [!question]- ¿Qué viola un corte que registra la recepción de un mensaje pero no su envío?
> La causalidad: muestra un efecto sin causa. Ese estado nunca pudo existir en ninguna ejecución real, así que no sirve como punto de restauración.

> [!question]- Nombra dos usos de un estado global y por qué necesitan consistencia.
> Los checkpoints de una base de datos, que deben poder restaurarse a un estado que realmente existió, y la detección de deadlocks, porque un corte inconsistente podría mostrar ciclos de espera que nunca ocurrieron al mismo tiempo.
