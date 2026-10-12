---
ramo: "Sistemas Operativos y Redes"
tema: "Hilos"
tags:
  - ssoo
  - threads
  - user-threads
  - kernel-threads
  - escalabilidad
  - origen/complemento
prerrequisitos:
  - "[[01 - Concepto de hilo y recursos compartidos versus privados]]"
  - "[[02 - Programación con POSIX Threads y ciclo de vida]]"
---

# Hilos a nivel de usuario frente a hilos a nivel de kernel

Los threads pueden "vivir" en dos lugares: en el **espacio de usuario**, administrados por una biblioteca sin que el kernel sepa que existen, o en el **espacio del kernel**, como entidades que el SO conoce y planifica. La elección cambia qué pasa cuando un thread se bloquea, cuánto cuesta cambiar de thread y cuántos threads se pueden tener.

![Modelos de hilos en espacio de usuario y kernel](adjuntos/Modelos%20de%20hilos%20en%20espacio%20de%20usuario%20y%20kernel.png)

> [!example]- Transcripción de la imagen
> Dos cuadros, cada uno con *User space* arriba y *Kernel space* (Kernel) abajo. A la izquierda hay tres procesos (*Process 1, 2, 3*), cada uno con **un solo thread**. A la derecha hay **un proceso** con **tres threads**. Muestra la diferencia entre tener varios procesos de un thread y un proceso con varios threads.

## Threads en espacio de usuario (ULT)

Los implementa y maneja una **biblioteca de usuario** (el *run-time system*). Cada proceso guarda su propia **tabla de threads**, y el **kernel no ve threads**: solo ve procesos de un único thread.

![Implementación de hilos en espacio de usuario y tablas](adjuntos/Implementaci%C3%B3n%20de%20hilos%20en%20espacio%20de%20usuario%20y%20tablas.png)

> [!example]- Transcripción de la imagen
> Dos procesos en *user space*, cada uno con varios threads y, abajo dentro del proceso, su **Run-time system** con su **Thread table**. En *kernel space*, el Kernel solo tiene la **Process table**.

| Lo bueno | Lo malo |
|---|---|
| **Portable:** se puede implementar en cualquier SO | Una **syscall bloqueante** (por ejemplo, un `read()` que espera al disco) **bloquea todo el proceso**: el kernel no sabe que hay otros threads listos |
| **Cambio de contexto y scheduling más rápidos:** no hay que entrar al kernel | **Requiere scheduling cooperativo:** no hay timers que interrumpan a un thread que no cede la CPU |
| **Más escalable:** usa la memoria del proceso, así que hay espacio para crear muchos threads | |

Para mitigar el bloqueo, estas implementaciones usan variantes **no bloqueantes** de algunas syscalls. Piensa en un servidor web multithread: si atender a un cliente bloquea el proceso entero, todos los demás clientes esperan.

## Threads en espacio de kernel (KLT)

Los implementa y maneja **nativamente el kernel**, con sus propias estructuras, sin bibliotecas de usuario.

| Lo bueno | Lo malo |
|---|---|
| **Soporte nativo**, sin bibliotecas | **Syscalls más costosas:** cada operación de threads requiere llamar al kernel |
| **Las syscalls no bloquean el proceso:** si un thread espera I/O, el kernel puede ejecutar otro thread del mismo proceso | **Escalabilidad limitada por el SO:** el espacio del kernel es acotado, así que hay un número limitado de threads |
| Pueden correr en paralelo en distintos núcleos | Semántica poco clara de `fork()` y de las señales (¿se copian todos los threads?, ¿cuál recibe la señal?) |

Como crear y destruir threads del kernel tiene costo, las implementaciones evitan hacerlo: mantienen **thread pools**, conjuntos de threads ya creados que esperan a ser usados, y reutilizan sus estructuras.

> [!tip] Resumen para recordar
> **Usuario:** rápido, portable y escalable, pero una syscall bloqueante congela todo el proceso. **Kernel:** robusto ante bloqueos y con paralelismo real, pero más caro y limitado en cantidad. Un proceso que necesita ser muy escalable (miles de threads) favorece threads de usuario.

## Implementación híbrida

Una tercera opción **multiplexa** varios threads de usuario sobre unos pocos threads de kernel (modelo M:N). El kernel solo ve los threads de kernel. Así se obtienen threads livianos de crear, escalables como los de usuario y cuyas syscalls no bloquean el proceso.

## Más threads no siempre es más rápido

Crear y eliminar un thread es mucho más fácil que hacerlo con un proceso. Al eliminar un thread solo se libera su pequeño stack, su PC (con sus registros) y su ID. Un proceso, en cambio, tiene mucho más que liberar: memoria, archivos, hijos. Aun así, crear threads no es gratis: si una tarea se divide en demasiados threads, se puede demorar más en crearlos y destruirlos que en resolver la tarea.

## Preguntas de repaso

> [!question]- Describe los beneficios de implementar threads en espacio de usuario.
> Son portables, porque basta una biblioteca y no requieren soporte del SO. El cambio de contexto y el scheduling son más rápidos, porque no entran al kernel. Y son más escalables, porque usan la memoria del proceso.

> [!question]- ¿Por qué una syscall bloqueante es un problema para los threads de usuario y no para los de kernel?
> Con threads de usuario, el kernel solo ve un proceso de un thread: si ese "único" thread se bloquea, el kernel bloquea el proceso completo. Con threads de kernel, el SO sabe que hay otros threads del proceso listos y puede ejecutarlos.

> [!question]- ¿Por qué los threads de kernel escalan peor?
> Porque cada uno ocupa estructuras dentro del kernel, cuyo espacio es limitado, y cada operación sobre ellos es una syscall con su costo.

> [!question]- ¿Qué se libera al eliminar un thread y por qué es más barato que eliminar un proceso?
> Solo su stack, sus registros (incluido el PC) y su ID. Los recursos pesados (memoria, archivos, hijos) son del proceso y siguen intactos para los demás threads.
