---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - semaforos
  - dijkstra
  - p-wait
  - v-signal
  - origen/complemento
prerrequisitos:
  - "[[04 - Mutex locks y el dilema de busy waiting versus dormir]]"
  - "[[05 - Problema del productor-consumidor y buffer acotado]]"
---

# Semáforos de Dijkstra y tipos de semáforos

Un mutex deja pasar a un solo thread. Pero a veces se quiere permitir **hasta cierta cantidad** (por ejemplo, $N$ espacios en un buffer), o esperar a que "haya algo" sin perder avisos, como pasaba con `sleep` y `wakeup`. Para eso E. W. Dijkstra propuso en 1965 una nueva primitiva de sincronización, el **semáforo**, que introdujo en Algol 68.

## Definición

Un semáforo **permite un número limitado de threads en una sección crítica**. Un semáforo `S` incluye un **contador** y dos operaciones:

| Operación | Otros nombres | Qué hace |
|---|---|---|
| **P()** (*proberen*) | `wait()`, `down()` | **Intenta decrementar** el contador; si es 0, el thread espera |
| **V()** (*verhogen*) | `signal()`, `up()` | **Incrementa** el contador y despierta a un thread que espere |

> [!tip] Mnemotecnia: Pedir / Votar
> Dijkstra era holandés, pero si no sabes holandés es más fácil recordar **P = Pedir** (decrementa: "pido un permiso") y **V = Votar** (incrementa: "devuelvo un permiso").

El valor inicial define el tipo de semáforo:

- **Binario** (0 o 1): deja pasar a uno a la vez, como un mutex. La diferencia es que el mutex tiene **propietario** (solo quien lo tomó puede liberarlo), mientras que el `V()` de un semáforo lo puede hacer cualquier thread, lo que permite usarlo para avisar entre threads.
- **Contador** (valor inicial $N$): representa $N$ unidades de un recurso, por ejemplo $N$ espacios libres en un buffer.

## Implementación sin busy waiting

Los semáforos tienen una implementación **sin busy waiting**: en vez de girar, el thread que no puede pasar **se va a dormir** en una cola, y `V()` lo despierta.

![Estructura y definición de semáforo de Dijkstra](adjuntos/Estructura%20y%20definici%C3%B3n%20de%20sem%C3%A1foro%20de%20Dijkstra.png)

> [!example]- Transcripción de la imagen
> `struct semaphore { int count; struct Lock l; struct process* slept = NULL; }`.

![Operación P wait o down en semáforos](adjuntos/Operaci%C3%B3n%20P%20wait%20o%20down%20en%20sem%C3%A1foros.png)

> [!example]- Transcripción de la imagen
> `void init(c) { count = c; }` y `void P() { /* wait: put into queue and sleep */ l.acquire(); while(count <= 0) { /* code to add itself to 'slept' */ l.release(); sleep(); l.acquire(); } count--; l.release(); }`.

![Operación V signal o up en semáforos](adjuntos/Operaci%C3%B3n%20V%20signal%20o%20up%20en%20sem%C3%A1foros.png)

> [!example]- Transcripción de la imagen
> `void V(S) { /* signal */ l.acquire(); count++; wakeup(/* first from 'slept' */); // plus, remove from queue  l.release(); }`.

El contador está protegido por un lock interno `l`, así que revisarlo y modificarlo es atómico. En `P()`, mientras no haya permisos, el thread se anota en la cola `slept`, suelta el lock y duerme; al despertar, vuelve a tomar el lock y revisa otra vez. `V()` incrementa y despierta al primero de la cola. Otras implementaciones, pensadas para multiprocesadores, sí usan busy waiting.

## Ejemplo: buffer acotado con semáforos

Los semáforos resuelven el [[05 - Problema del productor-consumidor y buffer acotado|productor-consumidor]] sin busy waiting y sin avisos perdidos: `vacios` cuenta los espacios libres (parte en $N$), `llenos` los elementos (parte en 0) y un mutex protege los índices.

```c
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

#define N 4                          /* tamaño del buffer */
#define ITEMS 20
int buffer[N], in = 0, out = 0;
sem_t vacios, llenos;                /* cuentan espacios libres y elementos */
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void *productor(void *arg) {
    for (int item = 1; item <= ITEMS; item++) {
        sem_wait(&vacios);           /* P: espera un espacio libre */
        pthread_mutex_lock(&mutex);
        buffer[in] = item; in = (in + 1) % N;
        pthread_mutex_unlock(&mutex);
        sem_post(&llenos);           /* V: hay un elemento más */
    }
    return NULL;
}

void *consumidor(void *arg) {
    long suma = 0;
    for (int k = 0; k < ITEMS; k++) {
        sem_wait(&llenos);           /* P: espera un elemento */
        pthread_mutex_lock(&mutex);
        suma += buffer[out]; out = (out + 1) % N;
        pthread_mutex_unlock(&mutex);
        sem_post(&vacios);           /* V: hay un espacio más */
    }
    printf("suma consumida = %ld\n", suma);   /* 1 + 2 + ... + 20 = 210 */
    return NULL;
}

int main(void) {
    sem_init(&vacios, 0, N);         /* N espacios libres al inicio */
    sem_init(&llenos, 0, 0);         /* 0 elementos al inicio */
    pthread_t p, c;
    pthread_create(&p, NULL, productor, NULL);
    pthread_create(&c, NULL, consumidor, NULL);
    pthread_join(p, NULL);
    pthread_join(c, NULL);
    return 0;
}
```

> [!warning] `sem_init` en macOS
> macOS no implementa los semáforos sin nombre (`sem_init`): compila con un aviso de función obsoleta, pero no funcionan. Allí hay que usar semáforos con nombre (`sem_open`). En Linux, el código anterior funciona tal cual.

## Preguntas de repaso

> [!question]- ¿Qué hacen P y V sobre el contador del semáforo?
> P intenta decrementarlo: si no hay permisos (contador en 0), el thread espera. V lo incrementa y despierta a un thread que esté esperando.

> [!question]- Verdadero o falso: los semáforos tienen una implementación sin busy waiting.
> Verdadero. El thread que no puede pasar se anota en una cola y duerme, y V lo despierta. No gasta CPU mientras espera.

> [!question]- ¿Con qué valores se inicializan los semáforos del buffer acotado y por qué?
> `vacios` en $N$, porque al principio todo el buffer está libre, y `llenos` en 0, porque no hay elementos. El productor hace P sobre `vacios` y V sobre `llenos`; el consumidor, al revés.

> [!question]- ¿Por qué la implementación de P suelta el lock antes de dormir?
> Porque si durmiera con el lock tomado, ningún otro thread podría ejecutar V (que también necesita el lock) para despertarlo, y el sistema se trabaría.
