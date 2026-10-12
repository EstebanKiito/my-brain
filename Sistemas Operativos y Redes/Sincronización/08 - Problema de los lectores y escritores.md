---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - lectores-escritores
  - readers-writers
  - semaforos
prerrequisitos:
  - "[[06 - Semáforos de Dijkstra y tipos de semáforos]]"
---

# Problema de los lectores y escritores

El problema de los **Lectores y Escritores** (*Readers-Writers Problem*) modela el acceso concurrente a una base de datos o estructura de datos donde coexisten dos tipos de procesos: los **lectores**, que únicamente consultan la información sin alterarla, y los **escritores**, que modifican los datos.

---

## PROBLEMA LECTOR-ESCRITOR (mis apuntes)

> “Permitir acceso de n lectores simultáneos, pero solamente 1 escritor”
> → Muchos quieren saber el valor de una variable → Pero solo 1 puede cambiarla
> 
> ![Problema de lectores y escritores con semáforos](adjuntos/Problema%20de%20lectores%20y%20escritores%20con%20sem%C3%A1foros.png)
> 
> Pueden haber muchos readers, pero leer no necesariamente bloquea, pero NO pueden ESCRIBIR
> Esto es comun en la base de datos
> Strongly consistent → Solo uno escribe a la vez
> No strongly consistent → Pueden tener errores

---

> [!example]- Transcripción de la imagen: Problema de lectores y escritores con semáforos.png
> **Solución clásica con Semáforos (Prioridad a Lectores):**
> ```c
> struct semaphore rw;    // Controla acceso exclusivo a la base de datos (init: 1)
> struct semaphore mutex; // Protege la variable de conteo read_count (init: 1)
> int read_count = 0;
> 
> // Código del Escritor (Writer):
> void writer() {
>     rw.wait();          // Solicita acceso exclusivo total
>     write_data();       // Solo 1 escritor modifica a la vez
>     rw.signal();
> }
> 
> // Código del Lector (Reader):
> void reader() {
>     mutex.wait();
>     read_count++;
>     if (read_count == 1) {
>         rw.wait();      // El primer lector toma rw para bloquear a los escritores
>     }
>     mutex.signal();
> 
>     read_data();        // Múltiples lectores leen en paralelo
> 
>     mutex.wait();
>     read_count--;
>     if (read_count == 0) {
>         rw.signal();    // El último lector libera rw para los escritores
>     }
>     mutex.signal();
> }
> ```

---

> [!tip] Complemento: Variantes y riesgo de inanición (Starvation)
> 1. **Primera variante (Prioridad a lectores):**
>    - Ningún lector espera si la base de datos ya está abierta para lectura.
>    - **Riesgo:** Si siguen llegando nuevos lectores continuamente, el escritor sufrirá **inanición indefinida** (*writer starvation*).
> 2. **Segunda variante (Prioridad a escritores):**
>    - Si un escritor manifiesta su deseo de escribir, los nuevos lectores entrantes quedan suspendidos hasta que el escritor termine.
>    - Evita que las actualizaciones críticas queden postergadas.
> 3. **Consistencia fuerte (*Strong consistency*):**
>    - En motores de bases de datos, los bloqueos compartidos (*shared locks*) para lectura y exclusivos (*exclusive locks*) para escritura garantizan aislamiento estricto y evitan lecturas sucias (*dirty reads*).

---

## Preguntas de repaso

> [!question]- ¿Por qué múltiples lectores pueden acceder simultáneamente sin violar la exclusión mutua?
> Porque las operaciones de lectura no alteran el estado ni los bytes en memoria. Dado que la lectura es idempotente y no genera condiciones de carrera, restringir a un solo lector degradaría innecesariamente el rendimiento del sistema.

> [!question]- ¿Qué rol cumple la variable read_count y qué hilo se encarga de tomar el semáforo rw?
> `read_count` cuenta cuántos lectores se encuentran actualmente en la sección de lectura. El **primer lector** (`read_count == 1`) es quien toma el semáforo `rw` para bloquear a cualquier posible escritor; y el **último lector** en salir (`read_count == 0`) es el responsable de liberar `rw`.

> [!question]- ¿Qué problema sufre la solución básica que prioriza a los lectores?
> Sufre el riesgo de **inanición de escritores**: si hay un flujo ininterrumpido de lectores donde siempre hay al menos uno activo, `read_count` nunca baja a 0, impidiendo que los escritores puedan tomar `rw` y actualizar los datos.

