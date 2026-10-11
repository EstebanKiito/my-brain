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
prerrequisitos:
  - "[[03 - Sincronización por hardware e instrucciones atómicas]]"
---

# Mutex locks y el dilema de busy waiting versus dormir

Los **cerrojos de exclusión mutua** (*Mutex Locks*) son primitivas de alto nivel que simplifican el acceso a la sección crítica mediante dos operaciones atómicas fundamentales: **adquirir** (`acquire`) y **liberar** (`release`).

---

## MUTEX LOCKS (mis apuntes)

> Solucion por Software
> Lock::aquite() : Toma el lock
> Lock::realease() : Libera el lock (error si no está tomado)
> Pregunta prueba (V/F) → Los mutex son implementaciones por software
> 
> Hay 2 tipos de espera:
> Bussy Waiting → Thread constantemente revisa si puede entrar a la seccion critica → Constantemente revisando un WHILE por su turno
> Irse a Dormir → Madar a dormir el Thread mientras espera
> 
> EJEMPLOS DE USO
> 
> ![Estructura de mutex lock con acquire y release](adjuntos/Estructura%20de%20mutex%20lock%20con%20acquire%20y%20release.png)
> 
> ![Protección de sección crítica mediante mutex lock](adjuntos/Protecci%C3%B3n%20de%20secci%C3%B3n%20cr%C3%ADtica%20mediante%20mutex%20lock.png)
> 
> Como se elimina el busy waiting → Irse a dormir
> 
> ![Eliminación de busy waiting mediante sleep y wakeup](adjuntos/Eliminaci%C3%B3n%20de%20busy%20waiting%20mediante%20sleep%20y%20wakeup.png)
> 
> Si no hay comida, mandame a dormir, si hay comida, despiertame
> Cuando se genere una comida → Le avisa al Consumidor que hay comida
> Cuando el consumidor consume → Le avisa al Productor

> [!warning] Posible error en apuntes
> * *"aquite"* / *"realease"*: erratas tipográficas por `acquire` y `release`.
> * *"Bussy Waiting"*: errata por *Busy Waiting* (espera activa).
> * *"Madar"*: errata por "Mandar".
> * *"Los mutex son implementaciones por software"*: la interfaz es de software (API POSIX), pero internamente los sistemas operativos y bibliotecas combinan instrucciones atómicas de hardware para el cerrojo rápido con llamadas al kernel para suspender hilos cuando la espera se prolonga.

---

> [!example]- Transcripción de la imagen: Estructura de mutex lock con acquire y release.png y Protección de sección crítica mediante mutex lock.png
> **Definición de interfaz Mutex:**
> ```c
> struct Lock {
>     void acquire(); // Solicita posesión del cerrojo; bloquea si ya está tomado
>     void release(); // Libera el cerrojo; error si quien llama no lo poseía
> };
> ```
> * **Uso estándar:**
> ```c
> struct Lock lock;
> 
> lock.acquire();
> // SECCIÓN CRÍTICA (acceso seguro a memoria compartida)
> lock.release();
> ```

> [!example]- Transcripción de la imagen: Eliminación de busy waiting mediante sleep y wakeup.png
> **Esquema de transición de estados sin desperdicio de CPU:**
> * `sleep()`: El hilo cede voluntariamente la CPU y el planificador lo traslada al estado **Waiting / Blocked** en una cola de espera.
> * `wakeup()`: Cuando el recurso queda disponible, el hilo que libera el cerrojo despierta al hilo dormido, trasladándolo al estado **Ready**.

---

> [!tip] Complemento: Spinlocks versus Mutex con Bloqueo
> 1. **Spinlock (Espera activa / Busy Waiting):**
>    - El hilo ejecuta continuamente un bucle `while (locked);` consumiendo el $100\%$ del núcleo de la CPU.
>    - **Ventaja:** Cero costo de cambio de contexto (*context switch overhead*).
>    - **Uso ideal:** Secciones críticas extremadamente cortas (menos de unos pocos microsegundos) en sistemas multiprocesador.
> 2. **Mutex con Bloqueo (*Sleep-Wakeup*):**
>    - El hilo se suspende en el kernel permitiendo que otros procesos utilicen la CPU.
>    - **Costo:** Involucra dos cambios de contexto (dormir y despertar).
>    - **Uso ideal:** Secciones críticas de duración moderada o larga (I/O, operaciones de red, cálculos pesados).

---

## Preguntas de repaso

> [!question]- ¿Qué problema genera el Busy Waiting en un sistema mono-núcleo?
> Genera un desperdicio total de CPU e inanición: el hilo que espera consume todos los ciclos de reloj ejecutando un bucle vacío, impidiendo que el hilo que posee el cerrojo reciba tiempo de CPU para avanzar y liberarlo.

> [!question]- ¿Cuándo es preferible utilizar un Spinlock en lugar de un Mutex con suspensión (sleep)?
> Cuando el tiempo estimado que el hilo pasará dentro de la sección crítica es inferior al costo temporal de ejecutar dos cambios de contexto (el costo de suspender y despertar el hilo mediante el planificador).

> [!question]- ¿Por qué release() debe arrojar un error si el hilo invocador no posee el cerrojo?
> Porque los mutex poseen semántica de propiedad (*ownership*): únicamente el hilo que tomó exitosamente el cerrojo mediante `acquire()` tiene la autoridad para liberarlo con `release()`. Liberar un lock ajeno rompería la invariante de exclusión mutua.
