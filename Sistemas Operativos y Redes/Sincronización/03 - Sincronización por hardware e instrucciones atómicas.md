---
ramo: "Sistemas Operativos y Redes"
tema: "Sincronización"
tags:
  - ssoo
  - sincronizacion
  - hardware
  - atomic-instructions
  - test-and-set
  - compare-and-swap
prerrequisitos:
  - "[[02 - Soluciones por software y algoritmo de Peterson]]"
---

# Sincronización por hardware e instrucciones atómicas

Para garantizar exclusión mutua de forma eficiente y segura en sistemas multiprocesador modernos, las CPUs implementan **instrucciones atómicas de hardware**. Una operación atómica se ejecuta como una unidad indivisible en un solo ciclo de bus o mediante bloqueo de línea de caché (*cache lock*), sin posibilidad de ser interrumpida.

---

## Sincronizaciones por Hardware (mis apuntes)

> Dependen de que existan Instrucciones Atomicas
> - Cada computador trae estas, que se ejcutan en el hardware, como Locks que se ejecutan en hardware
> - Guardo por ejemplo una varibale que esta bloqueada
> - Y que otro thread no puede acceder
> 
> Hay varias Sincronizaciones por hardware → Solo se van a usar si se trabaja con sistemas operativos (ej: Microsoft)
> - test_and_set() : Ejecucion que tiene un booleano, que lo que hace es cambiar su valor, toma su valor lo cambia y lo retorna
> 
> ![Instrucción atómica hardware test and set](adjuntos/Instrucci%C3%B3n%20at%C3%B3mica%20hardware%20test%20and%20set.png)
> 
> ![Semántica equivalente de test and set](adjuntos/Sem%C3%A1ntica%20equivalente%20de%20test%20and%20set.png)
> 
> Esto es basicamente lo que hace
> Existen muchas formas de implementarla
> IMPLEMENTACION INGENUA
> 
> ![Implementación básica de lock con test and set](adjuntos/Implementaci%C3%B3n%20b%C3%A1sica%20de%20lock%20con%20test%20and%20set.png)
> 
> Ingenua porque es la mas facil
> Un Thread a la vez (Por hardware) a diferencia de Por software que pueden entrar mas de uno a la vez
> - Compare_and_swap()
> 
> ![Semántica equivalente de compare and swap](adjuntos/Sem%C3%A1ntica%20equivalente%20de%20compare%20and%20swap.png)
> 
> Recordar que siempre que esta vacio es falso
> No usamos directamente, estas instrucciones atomicas → Si no que usamos Instrucciones Primitivas (Por Software)
> EJEMPLO
> 
> ![Implementación de lock con compare and swap](adjuntos/Implementaci%C3%B3n%20de%20lock%20con%20compare%20and%20swap.png)

> [!warning] Posible error en apuntes
> * *"Solo se van a usar si se trabaja con sistemas operativos"*: las instrucciones atómicas forman la base de todas las bibliotecas de concurrencia y runtime de lenguajes modernos (ej. `std::atomic` en C++, Go, Java, Rust), no exclusivamente del código del kernel.
> * *"Un Thread a la vez (Por hardware) a diferencia de Por software..."*: tanto por software como por hardware, el objetivo de la sección crítica es que ingrese exactamente **un hilo a la vez** (exclusión mutua). La diferencia radica en que el hardware garantiza indivisibilidad física sin depender de variables adicionales en RAM.

---

> [!example]- Transcripción de la imagen: Instrucción atómica hardware test and set.png y Semántica equivalente de test and set.png
> **Semántica conceptual de `test_and_set` (TSL en x86):**
> ```c
> bool test_and_set(bool *target) {
>     bool rv = *target;   // Lee el valor actual
>     *target = true;      // Escribe incondicionalmente true
>     return rv;           // Retorna el valor previo de forma atómica
> }
> ```
> * **Implementación de un Spinlock simple:**
> ```c
> bool lock = false;
> 
> while (test_and_set(&lock)); // Espera activa mientras retorne true (ocupado)
> // SECCIÓN CRÍTICA
> lock = false;                // Libera el cerrojo
> ```

> [!example]- Transcripción de la imagen: Semántica equivalente de compare and swap.png y Implementación de lock con compare and swap.png
> **Semántica conceptual de `compare_and_swap` (CAS / CMPXCHG en x86):**
> ```c
> int compare_and_swap(int *value, int expected, int new_value) {
>     int prev = *value;
>     if (prev == expected) {
>         *value = new_value;
>     }
>     return prev;
> }
> ```
> * Permite construir algoritmos sin bloqueos (*lock-free*) verificando si el valor en memoria coincide con el valor esperado antes de actualizarlo.

---

## Preguntas de repaso

> [!question]- ¿Qué significa que una instrucción de CPU sea "atómica"?
> Significa que su ejecución es completamente indivisible: se ejecuta de principio a fin sin que ninguna interrupción, cambio de contexto u otro núcleo del procesador pueda observar un estado intermedio o modificar los datos involucrados durante la operación.

> [!question]- ¿Cómo logra test_and_set implementar un cerrojo (spinlock)?
> Inicialmente `lock = false`. El primer hilo ejecuta `test_and_set(&lock)`, que atómicamente pone `lock = true` y devuelve `false`, saliendo del `while` hacia la sección crítica. Cualquier hilo subsiguiente ejecutará la instrucción, pondrá `lock = true` y recibirá `true`, quedando atrapado en el bucle `while` hasta que el primero ponga `lock = false`.

> [!question]- ¿Cuál es la ventaja de compare_and_swap frente a test_and_set?
> `compare_and_swap` opera sobre enteros o punteros arbitrarios en lugar de solo booleanos, y solo realiza la escritura si el valor actual coincide exactamente con un valor esperado. Esto habilita estructuras de datos concurrentes avanzadas y libres de cerrojos (*lock-free data structures*).
