---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - mutex
  - spinlock
  - busy-waiting
  - sleep-wakeup
  - origen/complemento
prerrequisitos:
  - "[[03 - Sincronización por hardware e instrucciones atómicas]]"
---

# Mutex locks y el dilema de busy waiting versus dormir

Las instrucciones atómicas resuelven la exclusión mutua, pero son incómodas de usar y obligan a girar en un `while` mientras se espera. Por eso, sobre ellas se construyen **primitivas de software**, más cómodas. La más simple es el **mutex lock** (*MUTual EXclusion lock*). Al diseñarlo aparece la pregunta central de este capítulo: mientras un thread espera, ¿conviene que siga revisando o que se vaya a dormir?

## El mutex: acquire y release

Un mutex ofrece dos operaciones:

- `Lock::acquire()`: **toma** el lock. Si está tomado, espera hasta que se libere.
- `Lock::release()`: **libera** el lock (es un error si no está tomado).

Es una **solución por software**: una abstracción que se implementa usando una instrucción atómica del hardware por debajo.

![Estructura de mutex lock con acquire y release](adjuntos/Estructura%20de%20mutex%20lock%20con%20acquire%20y%20release.png)

> [!example]- Transcripción de la imagen
> `struct Lock { bool value = false; // false==free, true==busy }`. "Implementación sin (mucho) busy waiting": `void acquire() { while(test_and_set(&value)) thread_yield(); // otras implementaciones usan sleep() y colas de espera }` y `void release() { value = false; }`.

Para proteger una sección crítica basta con encerrarla entre `acquire` y `release`:

![Protección de sección crítica mediante mutex lock](adjuntos/Protecci%C3%B3n%20de%20secci%C3%B3n%20cr%C3%ADtica%20mediante%20mutex%20lock.png)

> [!example]- Transcripción de la imagen
> "Solución a Sección Crítica": `while(true) { ... lock.acquire(); /* SC */ lock.release(); /* Out of SC */ }`. "Contador con acceso exclusivo": `struct Lock l; // compartido` y `for(int i=0; i<max; i++) { l.acquire(); counter = counter + 1; l.release(); }`.

En C con POSIX, el mismo contador queda así, y llega siempre a 2.000.000, a diferencia del ejemplo sin protección de [[01 - Condiciones de carrera y el problema de la sección crítica|condiciones de carrera]]:

```c
#include <pthread.h>
#include <stdio.h>

#define VECES 1000000
long contador = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;   /* compartido */

void *incrementar(void *arg) {
    for (int i = 0; i < VECES; i++) {
        pthread_mutex_lock(&lock);       /* acquire: si está tomado, el thread duerme */
        contador = contador + 1;         /* sección crítica */
        pthread_mutex_unlock(&lock);     /* release */
    }
    return NULL;
}

int main(void) {
    pthread_t a, b;
    pthread_create(&a, NULL, incrementar, NULL);
    pthread_create(&b, NULL, incrementar, NULL);
    pthread_join(a, NULL);
    pthread_join(b, NULL);
    printf("contador = %ld\n", contador);   /* siempre 2000000 */
    return 0;
}
```

## Dos formas de esperar

| | **Busy waiting** (espera activa; un lock así se llama *spinlock*) | **Irse a dormir** (*sleep*) |
|---|---|---|
| Qué hace el thread | Revisa constantemente, en un `while`, si ya puede entrar a la SC | Se bloquea en una cola de espera y no usa CPU |
| Costo | Gasta CPU mientras espera | Dos cambios de contexto: dormir y despertar |
| Conviene cuando | La espera es muy corta y hay varios núcleos | La espera puede ser larga |

La implementación de la figura es un punto intermedio: si el lock está tomado, el thread no gira sin parar, sino que **cede la CPU** con `thread_yield()`. Para eliminar el busy waiting del todo, el thread **se va a dormir**:

- `sleep()`: el thread se bloquea en la **cola waiting** (pasa a estado *Waiting*).
- `wakeup(t)`: saca al thread `t` de la cola waiting, si está ahí, y lo deja en *Ready*.

![Eliminación de busy waiting mediante sleep y wakeup](adjuntos/Eliminaci%C3%B3n%20de%20busy%20waiting%20mediante%20sleep%20y%20wakeup.png)

> [!example]- Transcripción de la imagen
> "sleep() se bloquea en cola waiting · wakeup(t) saca a t de la cola waiting (si está)". **Productor:** `while('p') { item = produce(); while (stock == N) sleep(); // Storage full  storage[in] = item; in = ++in%N; lock.acquire(); stock++; lock.release(); if(stock == 1) wakeup(consumer); }`. **Consumidor:** `while('c') { while(!stock) sleep(); // Wait for new items  item = storage[out]; out = ++out%N; lock.acquire(); stock--; lock.release(); if(stock == N-1) wakeup(producer); consume(item); }`.

La idea, aplicada al [[05 - Problema del productor-consumidor y buffer acotado|productor-consumidor]], es: *"si no hay comida, mándame a dormir; si hay comida, despiértame"*. Cuando el productor genera algo, le avisa al consumidor que hay comida; cuando el consumidor consume, le avisa al productor que hay espacio.

## Preguntas de repaso

> [!question]- Verdadero o falso: los mutex son implementaciones por software.
> Verdadero. El mutex es una primitiva de software (con `acquire` y `release`) construida sobre una instrucción atómica del hardware, como `test_and_set`.

> [!question]- ¿Qué es busy waiting y por qué es un problema?
> Es esperar revisando constantemente en un ciclo si ya se puede entrar. Gasta CPU sin avanzar, y en un sistema de un solo núcleo le quita tiempo justo al thread que tiene el lock y debe liberarlo.

> [!question]- ¿Cuándo conviene esperar activamente en vez de dormir?
> Cuando se espera que el lock se libere muy pronto y hay otros núcleos: dormir y despertar cuesta dos cambios de contexto, y si la espera es más corta que eso, girar sale más barato.

> [!question]- ¿Qué hacen `sleep()` y `wakeup(t)`?
> `sleep()` bloquea al thread que la llama en la cola waiting, sin consumir CPU. `wakeup(t)` saca al thread `t` de esa cola para que vuelva a estar listo.
