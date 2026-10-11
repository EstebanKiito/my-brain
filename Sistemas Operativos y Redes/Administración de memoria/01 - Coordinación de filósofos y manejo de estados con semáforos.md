---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - so/sincronizacion
  - origen/apuntes
prerrequisitos:
  - "[[09 - Problema de los filósofos comelones y deadlocks]]"
  - "[[06 - Semáforos de Dijkstra y tipos de semáforos]]"
---

# Coordinación de filósofos y manejo de estados con semáforos

En la sesión inicial del módulo de memoria se repasaron las primitivas de sincronización y se analizó la implementación concreta del problema clásico de los cinco filósofos empleando una máquina de estados por filósofo y semáforos privados para evitar la inanición y el interbloqueo.

## Sincronización y cena de los filósofos (mis apuntes)

> [!note] Apuntes de clase
> **Clase 6 (Online) → Mauro Quintana**
> **MEMORIA**
> 2/09/24
>
> **Resumen:**
> - Mutex Lock: Aquire() - Realease()
> - Semaforos: V() - P()
> - Varaibles de condicion: singal() - wait()
> - Primitivas de Software
> - Exclusion mutua
> - Progreso
> - Espera Acotada
> - Propiedades de la Sincronizacion (Seccion Critica
>
> **Problema visto en clases → Problema de los 5 filósofos**
> Cada filosofo tendre un semaforo que va a empezar en 1
> Los filosofos van a tener 3 estados posibles:
> - Estado filosofal → Tiene palillo
> - Estado hungry → Tiene intenciones de utilizar el palillo
> - Estado eating → Esta usando el
>
> **POSIBLES CASOS DE LOS THREADS**
> Intento tomar los palillos:
> Entro a try forks
> Compruebo el estado de los comesales a la derecha y izquierda
> - Happy path → irse a take_forks : Y se ejecuta a la primera, aquire el lock
>
> Dentro de try forks:
> Nunca accedi a philoshoppher[i}.V() → Por lo tanto el contador sigue en 0
> Y se va a bloquear en la instruccion philosopher[i].P() → Porque el contador sigue en 0
> No pude decrementar en el contador
> El de la izquierda o la derecha esta comiendo
> Por lo tanto ese ejecuto take_force
> va a comer eat()
> y va a soltar los palillos
> en realease forks → Cambia de estado a filosofando
> Y le avisa al de la izquierda → Intenta tomar los palillos
> Ahora en nuestro principal si cumple, aumenta el contador → Vuelve a estar en 1
> Dentro de la funcion, desperte al proceso de la cola de dormidos
> El que estaba durmiendo era philosopher[i].P() para decrementar el contador
> Se levanta y hace lo que debia
> Finalmente en este caso, es otro thread el que nos avisa que podemos continuar (realese_forks)
> - Unhappy path → Alguno esta usando los palillos

> [!warning] Posible error
> En los apuntes se indica "Estado filosofal → Tiene palillo". En la formulación estándar (Tanenbaum), en el estado *THINKING* (pensando/filosofando) el proceso no retiene ningún recurso; los palillos se adquieren exclusivamente al transicionar a *EATING*. Asimismo, figuran erratas tipográficas menores: "Aquire() - Realease()", "singal()", "philoshoppher[i}.V()", "take_force" y "realese_forks".

![Coordinación de filósofos con estados y semáforos](adjuntos/Coordinaci%C3%B3n%20de%20fil%C3%B3sofos%20con%20estados%20y%20sem%C3%A1foros.png)

> [!example]- Transcripción de la imagen
> Diagrama y pseudocódigo en C de la solución de Tanenbaum al problema de los filósofos comelones:
> - Vector de estados `state[N]` con valores `THINKING`, `HUNGRY`, `EATING`.
> - Mutex `mutex` para proteger la evaluación y actualización de estados.
> - Arreglo de semáforos `s[N]` (inicializados en 0) donde se bloquea cada filósofo si sus vecinos comen.
> - Función `test(i)`: verifica si `state[i] == HUNGRY && state[LEFT] != EATING && state[RIGHT] != EATING`. Si se cumple, cambia a `state[i] = EATING` y ejecuta `V(s[i])`.
> - `take_forks(i)`: adquiere mutex, fija `state[i] = HUNGRY`, ejecuta `test(i)`, suelta mutex y ejecuta `P(s[i])`.
> - `put_forks(i)`: adquiere mutex, fija `state[i] = THINKING`, prueba `test(LEFT)` y `test(RIGHT)`, y suelta mutex.

> [!tip] Complemento: Mecanismo de señalización cruzada
> La clave de este diseño radica en que cuando un filósofo no puede comer inmediatamente en `take_forks()`, no entra a la sección crítica de comer y queda suspendido en su semáforo privado (`P(s[i])`). Cuando sus vecinos terminan de comer en `put_forks()`, evalúan `test()` sobre sus adyacentes y ejecutan `V(s[vecino])`, despertándolo de la cola de bloqueados del kernel.

## Preguntas de repaso

> [!question]- ¿Por qué cada filósofo requiere un semáforo privado inicializado en 0 en lugar de bloquearse sobre un mutex global?
> Si se bloqueara sobre el mutex global, impediría que cualquier otro filósofo verifique o cambie de estado. El semáforo privado permite suspender selectivamente solo al filósofo que no tiene ambos palillos disponibles, manteniendo la concurrencia en la mesa.

> [!question]- ¿Qué rol cumple la función `test(i)` durante la ejecución de `put_forks()`?
> Al terminar de comer y soltar los palillos, el filósofo invoca `test()` para su vecino izquierdo y derecho. Si alguno estaba en estado `HUNGRY` esperando palillos y ahora ambos vecinos están libres, `test()` transiciona su estado a `EATING` y realiza un `signal` (`V`) sobre su semáforo privado para despertarlo.

> [!question]- ¿Cómo garantiza esta solución que no ocurra deadlock?
> El interbloqueo se elimina porque ningún filósofo toma un solo palillo y espera pasivamente con él en mano: solo se adquiere permiso para comer si ambos vecinos están libres simultáneamente, rompiendo la condición de retención y espera (*hold and wait*).

