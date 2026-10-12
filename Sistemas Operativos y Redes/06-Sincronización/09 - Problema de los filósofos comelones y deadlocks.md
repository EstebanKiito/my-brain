---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - dining-philosophers
  - deadlock
  - interbloqueo
  - origen/complemento
prerrequisitos:
  - "[[06 - Semáforos de Dijkstra y tipos de semáforos]]"
  - "[[08 - Problema de los lectores y escritores]]"
---

# Problema de los filósofos comelones y deadlocks

Hasta ahora cada thread necesitaba un solo recurso protegido. ¿Qué pasa cuando un thread necesita **dos recursos a la vez** y otros compiten por los mismos? El problema de los **filósofos comelones** (*dining philosophers*), propuesto por Dijkstra en 1965, muestra el peligro nuevo que aparece: que todos queden esperándose mutuamente para siempre, un **deadlock** (interbloqueo). Esta nota presenta el problema y por qué la solución ingenua falla. La solución completa con estados y semáforos está en [[01 - Coordinación de filósofos y manejo de estados con semáforos|coordinación de filósofos con estados]].

## El problema

**5 filósofos** se pasan la vida en dos actividades: **comer y pensar**. Están en una mesa redonda con un palillo entre cada par de vecinos.

- Para comer, un filósofo debe tomar **ambos palillos** (el izquierdo y el derecho).
- Solo puede tomar **un palillo a la vez**.

Hay tantos palillos como filósofos, pero cada uno necesita dos, así que **no alcanzan para que todos coman a la vez**: los recursos se comparten y los filósofos tienen que ponerse de acuerdo para sincronizarse.

![Ilustración del problema de la cena de los filósofos](adjuntos/Ilustraci%C3%B3n%20del%20problema%20de%20la%20cena%20de%20los%20fil%C3%B3sofos.png)

> [!example]- Transcripción de la imagen
> "Ilustración del problema de la cena de los filósofos": una mesa redonda con 5 platos de fideos, 5 tenedores (uno entre cada par de platos) y 5 filósofos alrededor.

## La solución ingenua y el deadlock

Lo más directo es un semáforo por palillo, iniciado en 1, y que cada filósofo tome primero el izquierdo y después el derecho:

![Implementación de filósofo con riesgo de deadlock](adjuntos/Implementaci%C3%B3n%20de%20fil%C3%B3sofo%20con%20riesgo%20de%20deadlock.png)

> [!example]- Transcripción de la imagen
> `int left = i; int right = (i+1)%N; // N==5` y `struct semaphore chopstick[N]; // inicializados en 1`. Luego `do { chopstick[left].P(); chopstick[right].P(); /* eat */ chopstick[left].V(); chopstick[right].V(); /* philosophise */ } while ('p');`.

Hay un orden de ejecución que lo arruina: si los 5 filósofos **toman su palillo izquierdo al mismo tiempo**, cada uno queda con uno en la mano esperando el derecho, que tiene su vecino. Nadie suelta lo que tiene y nadie puede avanzar: **deadlock**.

```mermaid
flowchart LR
  F0["F0 tiene p0, espera p1"] --> F1["F1 tiene p1, espera p2"]
  F1 --> F2["F2 tiene p2, espera p3"]
  F2 --> F3["F3 tiene p3, espera p4"]
  F3 --> F4["F4 tiene p4, espera p0"]
  F4 --> F0
```

> [!warning] Deadlock frente a inanición
> En un **deadlock** nadie avanza: el grupo entero queda bloqueado en un ciclo. En la **inanición** el sistema sí avanza, pero algún thread puntual nunca consigue el recurso, por ejemplo un filósofo cuyos vecinos se turnan para comer sin dejarlo nunca.

## Las cuatro condiciones de un deadlock

Un deadlock solo puede ocurrir si se cumplen **las cuatro** condiciones a la vez (condiciones de Coffman):

| Condición | En los filósofos |
|---|---|
| **Exclusión mutua** | Un palillo lo usa un solo filósofo a la vez |
| **Retención y espera** (*hold and wait*) | Cada uno retiene un palillo mientras espera el otro |
| **Sin expropiación** | Nadie le puede quitar el palillo a otro |
| **Espera circular** | F0 espera a F1, que espera a F2… y F4 espera a F0 |

Basta romper **una** para evitar el deadlock. Por ejemplo, que un filósofo tome los palillos en orden inverso rompe la espera circular, y permitir que solo 4 se sienten a la vez garantiza que al menos uno tenga ambos palillos. La solución del curso rompe la **retención y espera**: un filósofo solo pasa a comer cuando **ambos** palillos están libres, así que nunca se queda con uno en la mano esperando el otro.

![Solución con jerarquía de recursos para filósofos](adjuntos/Soluci%C3%B3n%20con%20jerarqu%C3%ADa%20de%20recursos%20para%20fil%C3%B3sofos.png)

> [!example]- Transcripción de la imagen
> "Otra implementación": `enum {PHILOSOPHISE, HUNGRY, EATING} state[N]; /* free / waiting / using */`, un lock `l` y `struct semaphore philosopher[N]; // inicializados en 0`, con las funciones `philosoph`, `take_forks`, `release_forks` y `try_forks`. La transcripción completa y su explicación paso a paso están en [[01 - Coordinación de filósofos y manejo de estados con semáforos|coordinación de filósofos con estados]].

## Preguntas de repaso

> [!question]- ¿Por qué la solución ingenua (izquierdo y luego derecho) puede producir deadlock?
> Porque si los cinco toman su palillo izquierdo a la vez, todos quedan reteniendo uno y esperando el de su vecino. Se forma un ciclo de espera del que nadie sale.

> [!question]- ¿Qué diferencia hay entre deadlock e inanición?
> En el deadlock nadie avanza, porque todos se esperan en ciclo. En la inanición el sistema avanza, pero algún thread puntual nunca obtiene el recurso.

> [!question]- ¿Cuáles son las cuatro condiciones de un deadlock y cuántas hay que romper?
> Exclusión mutua, retención y espera, sin expropiación y espera circular. Basta romper una sola para que el deadlock no pueda ocurrir.

> [!question]- ¿Qué condición rompe la solución con estados del curso?
> La retención y espera: un filósofo solo pasa a comer si ambos vecinos no están comiendo, y toma los dos palillos de una vez, así que nunca retiene uno mientras espera el otro.
