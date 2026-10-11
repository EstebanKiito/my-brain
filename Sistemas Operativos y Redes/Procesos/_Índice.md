# Procesos — índice

Concepto de proceso como entidad dinámica en memoria, estructura del espacio de memoria virtual, bloque de control de procesos (PCB), máquina de estados, sobrecarga del cambio de contexto, perfiles CPU-bound vs I/O-bound, jerarquía de procesos y programación en C con llamadas al sistema `fork`, `exec` y `wait`.

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la Clase 3 y Clase 4 de los apuntes de Sistemas Operativos, junto con la Ayudantía 1 (código en C y tareas), complementadas con las diapositivas oficiales de `Contenido_2_Procesos.pdf` y referencias de Arpaci-Dusseau (*OSTEP: Virtualization*).

## Orden de estudio

1. [[01 - Concepto de proceso y espacio de memoria|Concepto de proceso y espacio de memoria]]: definición de proceso frente a programa, segmentos `.text`, `.data`, `heap` y `stack`.
2. [[02 - Bloque de control de procesos y tabla de procesos|Bloque de control de procesos y tabla de procesos]]: representación interna del kernel (PCB / `task_struct`), tabla de procesos e información almacenada.
3. [[03 - Estados de un proceso y ciclo de vida|Estados de un proceso y ciclo de vida]]: máquina de estados (New, Ready, Running, Waiting, Finished) y transiciones por eventos o tiempo.
4. [[04 - Cambio de contexto y tipos de procesos|Cambio de contexto y tipos de procesos]]: mecanismo y costo de conmutación de CPU (*overhead* directo e indirecto), procesos CPU-bound frente a I/O-bound.
5. [[05 - Jerarquía y creación de procesos con fork|Jerarquía y creación de procesos con fork]]: árbol genealógico de procesos, proceso raíz PID 1 (`systemd`), duplicación con `fork()` y optimización *Copy-On-Write*.
6. [[06 - Control de procesos con wait, exec y terminación|Control de procesos con wait, exec y terminación]]: reemplazo de imagen con `execve()`, sincronización con `wait()`, y gestión de procesos zombies y huérfanos.
7. [[07 - Programación de procesos en C y prevención de fork bombs|Programación de procesos en C y prevención de fork bombs]]: implementación práctica en lenguaje C, patrones de bifurcación y defensas contra saturación por *fork bomb*.

