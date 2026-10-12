---
ramo: "Sistemas Operativos y Redes"
tema: "Hilos"
tags:
  - ssoo
  - threads
  - hilos
  - concurrencia
  - paralelismo
  - origen/complemento
prerrequisitos:
  - "[[01 - Concepto de proceso y espacio de memoria]]"
  - "[[04 - Cambio de contexto y tipos de procesos]]"
---

# Concepto de hilo y recursos compartidos versus privados

Un proceso tiene su código, sus archivos y su estado, pero hace una sola cosa a la vez. Si dentro de él hay tareas distintas que no tienen por qué ejecutarse una después de otra, conviene poder correrlas en paralelo sin crear procesos completos. Para eso existen los **threads** (hilos): los procesos tienen threads adentro.

## Qué es un thread

Un **thread** es *como un proceso, pero más liviano* (*lightweight process*): es la **unidad básica de uso de CPU**. Los threads surgen de **separar dos conceptos** que el proceso tenía juntos:

- el **proceso** agrupa los **recursos** (memoria, archivos, etc.);
- el **thread** es solo una **unidad de ejecución**.

Un proceso puede tener uno (*single-threading*) o varios threads (*multi-threading*).

¿Para qué sirven?

- **Paralelizar o distribuir tareas**: si hay tareas que se pueden hacer en paralelo, se usa un thread para cada una.
- **Simplificar el código**: cada thread puede ejecutar una parte distinta del programa, lo que encaja bien con la programación guiada por eventos (por ejemplo, un servidor web con un thread por cliente).
- **Ahorrar costo**: crear y destruir un thread es sustancialmente más liviano que hacerlo con un proceso.

> [!warning] Threads no implica paralelismo
> Los threads no necesariamente se ejecutan al mismo tiempo. Solo con varios núcleos puede haber paralelismo real; con uno solo se turnan (concurrencia, por ejemplo con [[04 - Planificación Round Robin y sistemas interactivos|Round Robin]]). Por eso un programa con varios threads incluso podría ser **más lento**, por el costo de coordinarlos.

## Qué comparten y qué no

| **No comparten** (ejecución) | **Comparten** (recursos) |
|---|---|
| Thread ID (`tid`) | Espacio de memoria: código, variables globales (`.data`) y heap (lo pedido con `malloc()`) |
| Program Counter | Archivos abiertos |
| Registros | Procesos hijos |
| Stack | Señales y manejadores de señales |
| Estado | Alarmas pendientes e información de contabilidad |

> [!tip] Regla para recordarlo
> **Lo privado tiene que ver con la ejecución; lo compartido tiene que ver con los recursos.**
> - Cada thread tiene su propio id, igual que los procesos, y no lo puede compartir.
> - Tampoco comparten el PC, porque cada uno va en una línea distinta del código, haciendo cosas distintas.
> - Y cada uno necesita su propio stack para sus propias llamadas a función.

```c
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

int global = 0;                                   /* .data: compartida por todos los threads */

void *trabajo(void *arg) {
    int local = *(int *)arg;                      /* stack: privada de cada thread */
    printf("thread %d: &local=%p  &global=%p\n", local, (void *)&local, (void *)&global);
    sleep(1);                                     /* seguir vivo mientras corre el otro */
    return NULL;
}

int main(void) {
    pthread_t t1, t2;
    int id1 = 1, id2 = 2;
    pthread_create(&t1, NULL, trabajo, &id1);
    pthread_create(&t2, NULL, trabajo, &id2);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    return 0;
}
```

Al ejecutarlo, los dos threads imprimen **la misma dirección para `global`** y **direcciones distintas para `local`**: la global está en la memoria compartida, mientras que cada `local` vive en el stack de su thread.

## El costo de compartir

Compartir recursos es lo que hace livianos a los threads, pero también lo que los hace peligrosos. Si dos threads intentan, por ejemplo, abrir y escribir el mismo archivo Excel al mismo tiempo, uno puede escribir la mitad y el otro la otra mitad, y el archivo queda incompleto o mezclado. Es un **problema de sincronización**: una [[01 - Condiciones de carrera y el problema de la sección crítica|condición de carrera]]. Se estudia en el capítulo de sincronización.

## Preguntas de repaso

> [!question]- ¿Qué tiene cada thread de forma privada y por qué?
> Su thread ID, su Program Counter, sus registros, su stack y su estado. Todo eso describe la ejecución de cada thread, que avanza por líneas y llamadas distintas.

> [!question]- Verdadero o falso: los threads no comparten id, pero sí comparten recursos como los archivos abiertos.
> Verdadero. El id es propio de cada thread, mientras que los recursos del proceso (archivos, memoria, hijos, señales) son comunes a todos sus threads.

> [!question]- ¿Por qué un programa con varios threads podría ser más lento que uno con un solo thread?
> Porque los threads solo corren en paralelo si hay varios núcleos. Con uno solo se turnan, y el costo de cambiarlos y coordinarlos puede superar lo que se gana.

> [!question]- ¿Por qué compartir memoria entre threads puede corromper datos?
> Porque dos threads pueden modificar la misma variable o el mismo archivo intercalando sus operaciones. Sin sincronización, el resultado depende del orden en que se ejecutan y puede quedar mezclado o incompleto.
