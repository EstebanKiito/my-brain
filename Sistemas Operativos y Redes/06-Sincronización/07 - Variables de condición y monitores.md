---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - condition-variables
  - cv
  - monitores
  - origen/complemento
prerrequisitos:
  - "[[04 - Mutex locks y el dilema de busy waiting versus dormir]]"
  - "[[05 - Problema del productor-consumidor y buffer acotado]]"
---

# Variables de condición y monitores

Los semáforos sirven para controlar **cuántos** threads acceden a una región protegida. El mecanismo consiste en bloquearse con `P()` bajo una condición (no quedan permisos) y avisar con `V()` que una condición se cumplió. Pero muchas veces la espera depende de una condición cualquiera ("el buffer está lleno", "no hay escritores") que no se reduce a un contador. Para eso existen las **variables de condición**.

## Qué son

> [!tip] Definición
> Las **variables de condición** permiten **bloquearse bajo condiciones arbitrarias**.
> - `Condition::wait()`: **bloquea siempre** al thread que la llama.
> - `Condition::signal()`: **despierta a un thread bloqueado, si lo hay**.

Además suele existir `broadcast()` (en POSIX, `pthread_cond_broadcast`), que despierta a **todos** los threads bloqueados en esa condición.

![Concepto y operaciones de variables de condición](adjuntos/Concepto%20y%20operaciones%20de%20variables%20de%20condici%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "*Variables de condición permitan bloquearse bajo condiciones arbitrarias.*" · **Condition::wait()** bloquea siempre el thread · **Condition::signal()** despierta a un thread bloqueado, si lo hay.

Una variable de condición **siempre se usa junto a un lock**, y `wait` **libera ese lock antes de bloquearse** (y lo vuelve a tomar al despertar). Esto es lo que evita el aviso perdido de `sleep`/`wakeup`: revisar la condición y dormirse ocurren con el lock tomado, así que nadie puede hacer `signal` entre medio.

## Productor-consumidor con variables de condición

Es la **implementación más sencilla** del [[05 - Problema del productor-consumidor y buffer acotado|buffer acotado]]: un lock y dos condiciones, una para cada lado.

![Productor consumidor con variables de condición](adjuntos/Productor%20consumidor%20con%20variables%20de%20condici%C3%B3n.png)

> [!example]- Transcripción de la imagen
> `struct lock l; struct condition condCons, condProd; int stock = 0; T storage[N];`. **Productor:** `while('p') { item = produce(); l.acquire(); // with mutex  while(stock == N) condProd.wait(l); // wait if full  storage[in] = item; in = ++in%N; stock++; condCons.signal(); // signal new item for consumer  l.release(); }`. **Consumidor:** `while('c') { l.acquire(); while(!stock) condCons.wait(l); // wait if empty  item = storage[out]; out = ++out%N; stock--; condProd.signal(); // signal new slot for producer  l.release(); consume(item); }`.

La lógica se lee casi en lenguaje natural:

- **Consumidor:** si no hay nada que consumir, se va a dormir. Cuando existe algo, lo consume.
- **Al consumir**, le avisa al productor: "despierta, hay espacio, anda a producir".
- **Productor:** si el buffer está lleno, duerme. Al producir, le avisa al consumidor que hay algo.

La misma solución con POSIX threads:

```c
#include <pthread.h>
#include <stdio.h>

#define N 4
#define ITEMS 20
int storage[N], stock = 0, in = 0, out = 0;
pthread_mutex_t l = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t condProd = PTHREAD_COND_INITIALIZER;   /* "hay espacio" */
pthread_cond_t condCons = PTHREAD_COND_INITIALIZER;   /* "hay elementos" */

void *productor(void *arg) {
    for (int item = 1; item <= ITEMS; item++) {
        pthread_mutex_lock(&l);
        while (stock == N)                       /* lleno: dormir */
            pthread_cond_wait(&condProd, &l);    /* suelta l mientras duerme */
        storage[in] = item; in = (in + 1) % N;
        stock++;
        pthread_cond_signal(&condCons);          /* avisar: hay algo que consumir */
        pthread_mutex_unlock(&l);
    }
    return NULL;
}

void *consumidor(void *arg) {
    long suma = 0;
    for (int k = 0; k < ITEMS; k++) {
        pthread_mutex_lock(&l);
        while (stock == 0)                       /* vacío: dormir */
            pthread_cond_wait(&condCons, &l);
        suma += storage[out]; out = (out + 1) % N;
        stock--;
        pthread_cond_signal(&condProd);          /* avisar: hay espacio */
        pthread_mutex_unlock(&l);
    }
    printf("suma consumida = %ld\n", suma);      /* 210 */
    return NULL;
}

int main(void) {
    pthread_t p, c;
    pthread_create(&p, NULL, productor, NULL);
    pthread_create(&c, NULL, consumidor, NULL);
    pthread_join(p, NULL);
    pthread_join(c, NULL);
    return 0;
}
```

> [!warning] `while`, no `if`
> Al despertar de `wait`, la condición podría ya no cumplirse: otro thread pudo adelantarse y tomar el recurso, o el thread pudo despertar sin que nadie hiciera `signal` (*spurious wakeup*). Por eso la condición siempre se vuelve a revisar en un `while`.

> [!tip] Diferencia clave con los semáforos
> Un semáforo **recuerda** los `V()` en su contador. Una variable de condición **no tiene memoria**: un `signal()` sin nadie esperando se pierde. Por eso la condición real se guarda en una variable (`stock`) protegida por el lock.

## Monitores

Un **monitor** lleva esta idea a nivel de lenguaje: agrupa los datos compartidos y los procedimientos que los usan, y garantiza que **solo un thread a la vez ejecute dentro del monitor**, sin que el programador tome el lock a mano. Dentro del monitor se usan variables de condición para esperar. Java es el ejemplo típico: los métodos `synchronized` y las llamadas `wait()`/`notify()` implementan un monitor por objeto.

## Preguntas de repaso

> [!question]- ¿Por qué `wait` debe liberar el lock al bloquearse?
> Porque si durmiera con el lock tomado, el otro thread no podría entrar a cambiar el estado ni a hacer `signal`, y ambos quedarían bloqueados para siempre.

> [!question]- ¿Por qué se revisa la condición con `while` y no con `if`?
> Porque al despertar, otro thread pudo cambiar el estado antes, o el despertar pudo ser espurio. El `while` vuelve a comprobar la condición antes de seguir.

> [!question]- ¿Qué pasa con un `signal()` cuando ningún thread está esperando?
> Se pierde: las variables de condición no guardan memoria, a diferencia de un semáforo, cuyo `V()` queda registrado en el contador.

> [!question]- En el productor-consumidor, ¿a quién avisa cada uno y por qué usan dos condiciones?
> El productor avisa en `condCons` que hay un elemento nuevo y el consumidor avisa en `condProd` que hay un espacio. Al ser dos condiciones distintas, cada `signal` despierta justo al tipo de thread que esperaba ese cambio.
