---
ramo: "Sistemas Operativos y Redes"
tema: "Hilos"
tags:
  - ssoo
  - threads
  - user-threads
  - kernel-threads
  - escalabilidad
prerrequisitos:
  - "[[01 - Concepto de hilo y recursos compartidos versus privados]]"
  - "[[02 - Programación con POSIX Threads y ciclo de vida]]"
---

# Hilos a nivel de usuario frente a hilos a nivel de kernel

La implementación de hilos difiere según **dónde reside la estructura de control** y **quién realiza la planificación**: en el espacio de usuario gestionados por una biblioteca de soporte (*User-Space Threads*, ULT) o directamente en el núcleo del sistema operativo (*Kernel-Space Threads*, KLT).

---

## THREADS SEGUN SU LOCALIZACION ¿Donde viven? (mis apuntes)

> Existen Threads que están precreados, esperando a ser usados → Pueden estar en espacio de Usuario o en Espacio del Kernell
> - No se pueden crear mas → No escalan
> - No se bloquean, porque pasan directo por abajo, y tienen soporte nativo
> - Son mucho mas RAPIDOS
> - KERNELL THREAD: Si tengo un espacio chico en el Kernell → Tendria un numero limitado de Threads
> - Los threads podrían no funcionar tan bien, porque estan mas lejos del kernell, podrian necesitar permisos, se podrian demorar mas
> - Los procesos que neceisten ser escalables, tienen que vivir en el espacio del Usuario
> - USER SPACE THREAD → Vamos a poder crear mas threads → Si escalan porque hay espacio para poner mas
> 
> No necesariamente tener mas threads, realiza mas rapido las tareas, si divido por ejemplo en muchos threads, voy a demorar mas en crearlos y destruirlos, que lo que me demoro en resolver la tarea
> Crear y eliminar Threads → Es mucho mas FACIL de Crear/Eliminar un proceso (Por el tema de los hijos, liberar recursos etc)
> 
> ELIMINACION
> Eliminarmos Threads → Eliminamos su :
> - mini Stack,
> - su Program Counter y
> - ID
> v/s
> Eliminar procesos → Tiene mucho mas por eliminar
> 
> EJEMPLO DE THREAD IN USER SPACE
> 
> ![Modelos de hilos en espacio de usuario y kernel](adjuntos/Modelos%20de%20hilos%20en%20espacio%20de%20usuario%20y%20kernel.png)
> 
> - Son mas Escalables (en el kernell son limitados)
> - Portable. Implementable en cualquier S.O
> - Context Switch y Scheduling mas rapido
> 
> Pregunta → Describa los beneficios de implementar Threads en el espacio del Usuario
> - Llamadas a syscalls pueden BLOQUEAR el PROCESO
> - Requiere Scheduling cooperativos
> MALO:
> 
> ![Implementación de hilos en espacio de usuario y tablas](adjuntos/Implementaci%C3%B3n%20de%20hilos%20en%20espacio%20de%20usuario%20y%20tablas.png)

> [!warning] Posible error en apuntes
> * *"Kernell"*: errata por "Kernel".
> * *"neceisten"*: errata por "necesiten".
> * *"Eliminarmos"*: errata por "Eliminamos".
> * *"No se bloquean, porque pasan directo por abajo"*: en hilos de kernel, si un hilo invoca una syscall bloqueante (ej. lectura de disco), **ese hilo específico** se bloquea en el kernel, pero el proceso NO se bloquea por completo porque el kernel puede despachar a los demás hilos en otros cores.

---

> [!example]- Transcripción de la imagen: Modelos de hilos en espacio de usuario y kernel.png
> **Comparativa de arquitectura de ejecución:**
> * **User Space Threads (Izquierda):** El kernel solo tiene visibilidad de procesos monohilo (*Process table*). La creación, conmutación y planificación de hilos ocurren enteramente dentro del espacio de usuario en el *Run-time system*.
> * **Kernel Space Threads (Derecha):** El kernel mantiene una tabla de hilos (*Thread table*) nativa. Puede asignar múltiples hilos del mismo proceso a diferentes núcleos físicos de CPU simultáneamente.

> [!example]- Transcripción de la imagen: Implementación de hilos en espacio de usuario y tablas.png
> **Estructuras de tablas en User Space:**
> * El *Run-time system* en el espacio de usuario posee su propia **Thread table** con el Program Counter, stack pointer y estado de cada hilo.
> * El kernel administra únicamente la **Process table** global.

---

> [!tip] Complemento: Comparativa entre User Threads y Kernel Threads
> 
> | Propiedad | Hilos en Espacio de Usuario (ULT) | Hilos en Espacio de Kernel (KLT) |
> | :--- | :--- | :--- |
> | **Administración** | Biblioteca de usuario (*run-time system*) | Núcleo del sistema operativo |
> | **Cambio de contexto** | Ultra rápido (sin trap a modo kernel) | Más lento (requiere cambio de modo y syscall) |
> | **Llamadas bloqueantes** | **Peligro:** Si un hilo se bloquea en I/O, **todo el proceso se congela** | Si un hilo se bloquea, el kernel despacha otro hilo del mismo proceso |
> | **Multiprocesamiento** | No puede utilizar múltiples cores en paralelo | Puede ejecutar hilos en paralelo en múltiples CPUs/cores |
> | **Escalabilidad** | Alta (limitada solo por memoria del proceso) | Moderada (limitada por estructuras del kernel) |
> 
> * **Modelos híbridos (M:N):** Buscan combinar lo mejor de ambos mundos multiplexando $M$ hilos de usuario sobre $N$ hilos de kernel (por ejemplo, los *goroutines* en el runtime de Go).

---

## Preguntas de repaso

> [!question]- ¿Por qué una llamada al sistema bloqueante representa un problema grave para los hilos en espacio de usuario?
> Porque para el núcleo del sistema operativo el proceso es una única entidad. Si un hilo de usuario realiza una syscall bloqueante sincrónica (ej. `read()` esperando el disco), el kernel pone a **todo el proceso** en estado bloqueado, impidiendo que los demás hilos sigan ejecutando aunque tengan trabajo listo.

> [!question]- ¿Por qué cambiar de contexto entre dos hilos a nivel de usuario es más rápido que entre hilos de kernel?
> Porque el cambio de contexto a nivel de usuario no requiere cruzar el límite de protección hacia el modo kernel ni generar una interrupción por software. La biblioteca simplemente guarda y restaura los registros de CPU y el puntero de pila en la tabla del runtime en espacio de usuario.

> [!question]- ¿Por qué crear y destruir hilos es mucho más eficiente que crear y destruir procesos?
> Porque para destruir un hilo solo se liberan su pila privada (*stack*), su identificador y su estructura de registros; todos los recursos pesados del proceso (tabla de páginas, descriptores de archivos, código binario y variables globales) permanecen intactos.

