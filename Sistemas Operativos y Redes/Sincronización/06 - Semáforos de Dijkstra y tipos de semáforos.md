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
prerrequisitos:
  - "[[04 - Mutex locks y el dilema de busy waiting versus dormir]]"
  - "[[05 - Problema del productor-consumidor y buffer acotado]]"
---

# Semáforos de Dijkstra y tipos de semáforos

Un **semáforo** es una variable entera especial introducida por Edsger Dijkstra en 1965 que, además de su inicialización, solo puede manipularse mediante dos operaciones atómicas indivisibles: **P** (*wait* / *down*) y **V** (*signal* / *up*).

---

## SEMAFOROS (mis apuntes)

> Primitiva de sincronización que invento Dijkstra → De P dercrementa y V Aumenta
> Un semáforo S incluye un contador y dos operaciones:
> - proberen P() ó wait() ó down(). Intenta decrementar el valor.
> - verhogen V() ó signal() ó up(). Incrementa el valor.
> 
> ![Estructura y definición de semáforo de Dijkstra](adjuntos/Estructura%20y%20definici%C3%B3n%20de%20sem%C3%A1foro%20de%20Dijkstra.png)
> 
> ![Operación P wait o down en semáforos](adjuntos/Operaci%C3%B3n%20P%20wait%20o%20down%20en%20sem%C3%A1foros.png)
> 
> ![Operación V signal o up en semáforos](adjuntos/Operaci%C3%B3n%20V%20signal%20o%20up%20en%20sem%C3%A1foros.png)
> 
> Implementan una version sin Bussy Waiting
> Los semaforos se pueden arreglar mucho haciendo usando sleep
> Pregunta prueba → Semaforos tiene una implementacion sin Bussy Waiting

> [!warning] Posible error en apuntes
> * *"dercrementa"*: errata por "decrementa".
> * *"Bussy Waiting"*: errata por *Busy Waiting*.
> * Nombres históricos en holandés: *Proberen* (probar/intentar) y *Verhogen* (incrementar/elevar).

---

> [!example]- Transcripción de la imagen: Estructura y definición de semáforo de Dijkstra.png y Operaciones P y V
> **Definición clásica con Busy Waiting:**
> ```c
> struct semaphore {
>     int count;
> };
> 
> void wait(semaphore *S) {     // P(S) o down(S)
>     while (S->count <= 0);    // Espera activa
>     S->count--;
> }
> 
> void signal(semaphore *S) {   // V(S) o up(S)
>     S->count++;
> }
> ```
> 
> **Implementación robusta del Sistema Operativo (Sin Busy Waiting):**
> ```c
> struct semaphore {
>     int value;
>     Queue<PCB*> waiting_queue;
> };
> 
> void wait(semaphore *S) {
>     S->value--;
>     if (S->value < 0) {
>         // Añadir este proceso a S->waiting_queue
>         sleep(); // Suspende el hilo en la cola del SO
>     }
> }
> 
> void signal(semaphore *S) {
>     S->value++;
>     if (S->value <= 0) {
>         // Remover un proceso P de S->waiting_queue
>         wakeup(P); // Pasa P al estado Ready
>     }
> }
> ```
> * **Propiedad del contador negativo:** Si `value < 0`, su magnitud absoluta $|value|$ representa exactamente el número de procesos actualmente bloqueados esperando el semáforo.

---

> [!tip] Complemento: Tipos de Semáforos
> 1. **Semáforo Binario (*Binary Semaphore*):**
>    - Su valor solo puede ser 0 o 1.
>    - Opera de forma muy similar a un Mutex (utilizado comúnmente para exclusión mutua simple).
> 2. **Semáforo Contador (*Counting Semaphore*):**
>    - Su valor inicial se establece en $N \ge 0$, representando la cantidad de unidades disponibles de un conjunto de recursos compartidos (ejemplo: $N$ slots en un buffer o $N$ conexiones a una base de datos).

---

## Preguntas de repaso

> [!question]- ¿Qué significa el valor negativo del contador en la implementación de semáforos sin espera activa?
> En una implementación con cola de bloqueo, si el contador de un semáforo es negativo (ej. $-k$), indica que no hay recursos disponibles y que existen exactamente $k$ procesos suspendidos en la cola de espera de ese semáforo.

> [!question]- ¿Cuál es la diferencia entre un Semáforo Binario y un Mutex?
> Aunque ambos restringen el acceso a un solo hilo (valores 0 y 1), un Mutex tiene concepto estricto de **propiedad** (*ownership*: solo quien lo adquiere puede liberarlo), mientras que un semáforo puede ser señalado (`signal`) por un hilo diferente al que ejecutó el `wait` (permitiendo sincronización y señalización entre hilos).

> [!question]- ¿Por qué las operaciones wait() y signal() deben ejecutarse de forma atómica?
> Porque si dos hilos decrementaran o incrementaran concurrentemente el contador sin exclusión mutua, se produciría una condición de carrera sobre la variable entera interna, pudiendo admitir a más hilos de los permitidos en la sección crítica.
