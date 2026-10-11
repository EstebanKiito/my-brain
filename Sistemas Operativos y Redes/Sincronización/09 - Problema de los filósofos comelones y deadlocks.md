---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - dining-philosophers
  - deadlock
  - interbloqueo
prerrequisitos:
  - "[[06 - Semáforos de Dijkstra y tipos de semáforos]]"
  - "[[08 - Problema de los lectores y escritores]]"
---

# Problema de los filósofos comelones y deadlocks

El problema de la **Cena de los Filósofos** (*Dining Philosophers Problem*), formulado por Edsger Dijkstra en 1965, es el paradigma clásico para modelar la asignación de recursos limitados entre múltiples procesos sin caer en **interbloqueos** (*deadlocks*) ni **inanición** (*starvation*).

---

## PROBLEMA FILOSOFICO (mis apuntes)

> Menos palillos que personas → Y hay que compartir
> 5 filósofos se pasan la vida en dos actividades: comer y pensar - Para comer deben tomar ambos palillos - Sólo pueden tomar un palillo a la vez
> ej 4 palillos 4 comensales:
> 
> ![Ilustración del problema de la cena de los filósofos](adjuntos/Ilustraci%C3%B3n%20del%20problema%20de%20la%20cena%20de%20los%20fil%C3%B3sofos.png)
> 
> Se tienen que poner de acuerdo para sincronizarse
> Código para filósofo i
> 
> ![Implementación de filósofo con riesgo de deadlock](adjuntos/Implementaci%C3%B3n%20de%20fil%C3%B3sofo%20con%20riesgo%20de%20deadlock.png)
> 
> Otra implementacion
> 
> ![Solución con jerarquía de recursos para filósofos](adjuntos/Soluci%C3%B3n%20con%20jerarqu%C3%ADa%20de%20recursos%20para%20fil%C3%B3sofos.png)

---

> [!example]- Transcripción de la imagen: Ilustración del problema de la cena de los filósofos.png
> **Disposición en la mesa redonda:**
> * $N = 5$ filósofos sentados alrededor de una mesa con un plato central de fideos.
> * Hay exactamente 5 palillos en total (uno entre cada par de filósofos adyacentes).
> * Para comer, un filósofo necesita obligatoriamente **ambos palillos** (izquierdo y derecho: `chopstick[i]` y `chopstick[(i+1)%5]`).

> [!example]- Transcripción de la imagen: Implementación de filósofo con riesgo de deadlock.png
> **Implementación ingenua con Semáforos (VULNERABLE A DEADLOCK):**
> ```c
> semaphore chopstick[5]; // Inicializados en 1
> 
> void philosopher(int i) {
>     while (1) {
>         think();
>         wait(chopstick[i]);              // Toma el palillo izquierdo
>         wait(chopstick[(i + 1) % 5]);    // Toma el palillo derecho
>         eat();
>         signal(chopstick[i]);
>         signal(chopstick[(i + 1) % 5]);
>     }
> }
> ```
> * **Riesgo mortal de Interbloqueo (*Deadlock*):** Si todos los 5 filósofos se sientan simultáneamente y toman su palillo izquierdo al mismo tiempo, todos tendrán un palillo en la mano izquierda y quedarán eternamente bloqueados esperando el palillo derecho. El sistema colapsa.

> [!example]- Transcripción de la imagen: Solución con jerarquía de recursos para filósofos.png
> **Solución Asimétrica (Jerarquía de Recursos):**
> * Rompe la condición de espera circular:
>   - Filósofos pares (0, 2, 4): Toman primero el palillo izquierdo `i`, luego el derecho `(i+1)%5`.
>   - Filósofos impares (1, 3): Toman primero el palillo derecho `(i+1)%5`, luego el izquierdo `i`.
> * Al menos un filósofo siempre podrá tomar ambos palillos y comer, liberándolos al terminar y garantizando progreso global.

---

> [!tip] Complemento: Las 4 Condiciones de Coffman para un Deadlock
> Un interbloqueo (*deadlock*) solo puede ocurrir si se cumplen simultáneamente cuatro condiciones:
> 1. **Exclusión Mutua:** Los recursos no son compartibles (cada palillo solo lo usa un filósofo).
> 2. **Retención y Espera (*Hold and Wait*):** Un proceso retiene un recurso mientras espera por otros.
> 3. **Sin Expropiación (*No Preemption*):** Los recursos no pueden ser arrebatados forzosamente.
> 4. **Espera Circular (*Circular Wait*):** Existe una cadena cíclica de procesos donde cada uno espera un recurso retenido por el siguiente. La solución asimétrica elimina esta cuarta condición.

---

## Preguntas de repaso

> [!question]- ¿Por qué la solución ingenua donde todos toman su palillo izquierdo primero produce un deadlock?
> Porque si todos los filósofos toman su palillo izquierdo simultáneamente, cada uno retiene un recurso y espera el palillo derecho (retenido por su vecino). Se forma un ciclo cerrado de espera (*circular wait*) del que ningún proceso puede salir por sí mismo.

> [!question]- ¿Cómo resuelve la técnica asimétrica el problema del interbloqueo?
> Al forzar a los filósofos impares a tomar sus palillos en orden inverso (derecho y luego izquierdo), se destruye la simetría y se previene la espera circular. Al menos dos filósofos competirán por el mismo palillo inicial, garantizando que otro pueda tomar ambos palillos contiguos y comer.

> [!question]- ¿Qué otra estrategia existe para evitar que los filósofos caigan en deadlock sin cambiar el orden de toma?
> Limitar el número máximo de comensales sentados a la mesa simultáneamente a $N-1$ (mediante un semáforo contador inicializado en 4). Si solo 4 filósofos intentan comer con 5 palillos disponibles, por el principio del palomar al menos uno tendrá acceso a dos palillos.

