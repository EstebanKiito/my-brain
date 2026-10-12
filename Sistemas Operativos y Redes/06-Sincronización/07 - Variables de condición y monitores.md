---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - condition-variables
  - cv
  - monitores
prerrequisitos:
  - "[[04 - Mutex locks y el dilema de busy waiting versus dormir]]"
  - "[[05 - Problema del productor-consumidor y buffer acotado]]"
---

# Variables de condición y monitores

Una **variable de condición** (*Condition Variable*, CV) es una primitiva de sincronización que permite a un hilo suspender su ejecución (*esperar*) dentro de una sección crítica hasta que otro hilo modifique el estado compartido y le notifique que una condición lógica se ha cumplido.

---

## Variables de Condición (mis apuntes)

> ![Concepto y operaciones de variables de condición](adjuntos/Concepto%20y%20operaciones%20de%20variables%20de%20condici%C3%B3n.png)
> 
> IMPLEMENTACION MAS SENCILLA → Con variables
> 
> ![Productor consumidor con variables de condición](adjuntos/Productor%20consumidor%20con%20variables%20de%20condici%C3%B3n.png)
> 
> - No hay nada que consumir → andate a dormir
> - Consumi → Oye despierta → Anda a producir
> - Consumidor → Existe algo para consumir → Anda a consumir
> Implementación bastante bella
> - Estudiar

> [!warning] Posible error en apuntes
> * *"Consumi"* / *"andate"*: redacción informal en apuntes de clase para describir el ciclo de señalización entre el hilo productor y el consumidor al gestionar las colas de espera.

---

> [!example]- Transcripción de la imagen: Concepto y operaciones de variables de condición.png
> **Operaciones fundamentales sobre una Variable de Condición (`cond_t`):**
> * Siempre se utilizan en combinación con un **Mutex Lock**:
>   - **`wait(cond_t *cv, mutex_t *lock)`:**
>     1. Libera atómicamente el cerrojo `lock`.
>     2. Pone al hilo a dormir en la cola de la variable de condición `cv`.
>     3. Al ser despertado, re-adquiere automáticamente el `lock` antes de retornar.
>   - **`signal(cond_t *cv)`:** Despierta al menos a un hilo que esté esperando en `cv`.
>   - **`broadcast(cond_t *cv)`:** Despierta a todos los hilos que estén esperando en `cv`.

> [!example]- Transcripción de la imagen: Productor consumidor con variables de condición.png
> **Patrón canónico Productor-Consumidor:**
> ```c
> mutex_t lock;
> cond_t cv_full, cv_empty;
> int count = 0;
> 
> void producer() {
>     lock.acquire();
>     while (count == N) {
>         wait(&cv_empty, &lock); // Espera espacio libre
>     }
>     put_item();
>     count++;
>     signal(&cv_full);           // Avisa al consumidor
>     lock.release();
> }
> 
> void consumer() {
>     lock.acquire();
>     while (count == 0) {
>         wait(&cv_full, &lock);  // Espera que haya elementos
>     }
>     get_item();
>     count--;
>     signal(&cv_empty);          // Avisa al productor
>     lock.release();
> }
> ```

---

> [!tip] Complemento: Por qué siempre se usa WHILE y no IF al esperar una CV
> En sistemas reales (POSIX Threads con semántica de Mesa), al despertar de un `wait`, la condición puede haber dejado de ser verdadera debido a:
> 1. Otro hilo despertó antes y consumió el recurso.
> 2. Despertares espurios (*spurious wakeups*) generados por el sistema operativo.
> Por esta razón, **siempre** se debe evaluar la condición en un bucle `while (condicion_invalida) wait(&cv, &lock);`.

---

## Preguntas de repaso

> [!question]- ¿Por qué wait() debe liberar el mutex de manera atómica al poner el hilo a dormir?
> Porque si no liberara el cerrojo, el hilo se dormiría reteniendo el lock, impidiendo que el otro hilo (que debe producir el dato y emitir el `signal()`) pueda entrar a la sección crítica, provocando un interbloqueo (*deadlock*) permanente.

> [!question]- ¿Cuál es la diferencia entre cond_signal() y cond_broadcast()?
> `cond_signal()` despierta a uno solo de los hilos que están esperando en la variable de condición (ideal cuando un solo recurso fue añadido), mientras que `cond_broadcast()` despierta a todos los hilos en espera (útil cuando el estado cambió radicalmente o múltiples lectores pueden proceder).

> [!question]- ¿Tienen memoria o estado interno las variables de condición a diferencia de los semáforos?
> No. Las variables de condición son "stateless": si se ejecuta `signal()` en un momento en que ningún hilo está esperando en el `wait()`, la señal se pierde sin dejar rastro en el sistema. Los semáforos, en cambio, incrementan su contador interno y recuerdan el evento.

