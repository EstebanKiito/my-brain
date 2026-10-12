---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - lectores-escritores
  - readers-writers
  - semaforos
  - origen/complemento
prerrequisitos:
  - "[[06 - Semáforos de Dijkstra y tipos de semáforos]]"
---

# Problema de los lectores y escritores

Un mutex trata igual a todos los threads: entra uno y los demás esperan. Pero si la mayoría solo quiere **leer** un dato, hacerlos esperar en fila es un desperdicio, porque leer no cambia nada. El problema de los **lectores y escritores** (*readers-writers*), planteado por Courtois et al. en 1971, modela este caso: el acceso a una base de datos.

## El problema

> [!tip] Regla
> **Permitir el acceso de $n$ lectores simultáneos, pero solamente de 1 escritor.**

Muchos quieren saber el valor de una variable, pero solo uno puede cambiarla a la vez. Puede haber muchos lectores al mismo tiempo, porque leer no bloquea a otros lectores, pero mientras alguien lee **nadie puede escribir**, y mientras alguien escribe nadie puede leer ni escribir.

Esto es muy común en bases de datos. Garantizar que solo uno escriba a la vez, y que nadie lea a medio escribir, es lo que da **consistencia fuerte** (*strongly consistent*). Si se relaja, se gana concurrencia, pero los lectores pueden ver datos erróneos o desactualizados.

## Solución con semáforos

- **Escritor (el caso fácil):** basta un semáforo `rw` compartido entre escritores y lectores.
- **Lectores:** además comparten un semáforo `mutex` que protege el contador `readers`. **El primer lector** que llega toma `rw` en nombre de todos los lectores, y **el último** que sale lo libera.

![Problema de lectores y escritores con semáforos](adjuntos/Problema%20de%20lectores%20y%20escritores%20con%20sem%C3%A1foros.png)

> [!example]- Transcripción de la imagen
> `struct semaphore rw; rw.init(1); struct semaphore mutex; mutex.init(1); int readers = 0; // leen o quieren leer`. Bajo el texto "Escritor (fácil) un semáforo **rw** compartido entre escritores y lectores" aparece el código del **lector**: `while('r') { mutex.P(); readers += 1; if(readers == 1) rw.P(); mutex.V(); /* READ */ mutex.P(); readers -= 1; if(readers == 0) rw.V(); mutex.V(); }`. Bajo "Lectores un semáforo mutex compartido" aparece el del **escritor**: `while('w') { rw.P(); /* WRITE */ rw.V(); }`.

En C con POSIX:

```c
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

sem_t rw;                    /* exclusión entre escritores y el grupo de lectores */
sem_t mutex;                 /* protege readers */
int readers = 0;             /* leen o quieren leer */
int dato = 0;                /* la "base de datos" */

void *lector(void *arg) {
    sem_wait(&mutex);
    if (++readers == 1) sem_wait(&rw);   /* el primer lector bloquea a los escritores */
    sem_post(&mutex);

    printf("leo %d\n", dato);            /* READ: varios lectores a la vez */

    sem_wait(&mutex);
    if (--readers == 0) sem_post(&rw);   /* el último lector deja pasar a los escritores */
    sem_post(&mutex);
    return NULL;
}

void *escritor(void *arg) {
    sem_wait(&rw);
    dato++;                              /* WRITE: solo uno, sin lectores */
    sem_post(&rw);
    return NULL;
}

int main(void) {
    sem_init(&rw, 0, 1);
    sem_init(&mutex, 0, 1);
    pthread_t t[4];
    pthread_create(&t[0], NULL, lector, NULL);
    pthread_create(&t[1], NULL, escritor, NULL);
    pthread_create(&t[2], NULL, lector, NULL);
    pthread_create(&t[3], NULL, lector, NULL);
    for (int k = 0; k < 4; k++) pthread_join(t[k], NULL);
    return 0;
}
```

> [!warning] ¿Por qué `rw` es un semáforo y no un mutex?
> El lector que **toma** `rw` (el primero) no tiene por qué ser el mismo que lo **libera** (el último). Un mutex exige que lo libere quien lo tomó; un semáforo no.

## El costo: inanición de escritores

Esta solución **favorece a los lectores**: mientras haya al menos uno leyendo, los nuevos lectores entran directo y `readers` nunca llega a 0. Si siguen llegando lectores sin pausa, **el escritor espera indefinidamente** (inanición). La variante opuesta da **prioridad a los escritores**: cuando uno quiere escribir, los lectores nuevos esperan a que termine. Así se evita que las actualizaciones se posterguen, aunque ahora el riesgo de esperar mucho lo corren los lectores.

## Preguntas de repaso

> [!question]- ¿Por qué pueden entrar varios lectores a la vez sin romper la exclusión mutua?
> Porque leer no modifica el dato y, por lo tanto, no hay condición de carrera entre lectores. La exclusión solo es necesaria cuando alguien escribe.

> [!question]- ¿Qué hacen el primer y el último lector con el semáforo `rw`?
> El primero (`readers == 1`) hace `P(rw)` para bloquear a los escritores en nombre de todo el grupo. El último (`readers == 0`) hace `V(rw)` para dejarlos pasar.

> [!question]- ¿Qué problema tiene esta solución y cuál es la variante que lo corrige?
> Los escritores pueden sufrir inanición si siempre hay algún lector activo. La variante con prioridad a escritores hace esperar a los lectores nuevos cuando hay un escritor esperando.

> [!question]- ¿Para qué sirve el semáforo `mutex` si los lectores pueden leer juntos?
> Protege el contador `readers`, que todos los lectores modifican. Sin él, dos lectores podrían actualizarlo a la vez y el conteo de "primero" y "último" fallaría.
