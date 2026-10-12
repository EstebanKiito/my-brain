---
ramo: Sistemas Operativos y Redes
tema: Procesos
tags: [so/procesos, origen/complemento]
prerrequisitos: ["[[01 - Concepto de proceso y espacio de memoria|Concepto de proceso y espacio de memoria]]"]
---
# Bloque de control de procesos y tabla de procesos

Para poder sacar un proceso de la CPU y luego retomarlo exactamente donde quedó, el sistema operativo necesita guardar todo lo que lo describe en algún lugar. Ese lugar es el **PCB** (*Process Control Block*), y todos los PCB se organizan en una única **tabla de procesos**.

## El PCB: la ficha de cada proceso

El PCB **almacena toda la información de un proceso**. Una buena analogía es el **registro civil**: así como ahí está tu ficha (identidad, padres, domicilio), en el PCB está la del proceso. Y como esa ficha, su contenido va cambiando durante la vida del proceso.

Según el material del curso, el PCB guarda:

| Campo | Para qué sirve |
|---|---|
| **Estado** | Si el proceso está *new*, *ready*, *running*, *waiting*… |
| **PID** y **PPID** | Su propio identificador y el de su padre |
| **Program Counter** (PC) | La próxima instrucción a ejecutar |
| **Registros de CPU** (`eax`, `ebx`, `sbp`, `sp`…) | El estado exacto de ejecución |
| **Información de memoria** | Límites, tablas de páginas o segmentos: dónde está su código y sus datos |
| **Información de scheduling** | Prioridad, tipo de cola |
| **Archivos y dispositivos abiertos** | Los recursos de I/O que tiene asignados |
| **Ejecutable** | El binario que se está corriendo |
| **Contabilidad** (*accounting*) | Tiempo de CPU usado, entre otros datos |

## Ciclo de vida del PCB

- **Al crear un proceso se crea su PCB**: hay un PCB por cada proceso que existe, incluidos todos los hijos.
- **Todo está en la misma tabla**: el SO mantiene una sola **tabla de procesos** para todos ellos, en su propia zona de memoria. Cada entrada apunta al PCB de un proceso.
- **Al terminar, el PCB no desaparece de inmediato.** Queda hasta que el padre recoge el estado de salida del hijo con `wait()`, y entonces se libera la entrada. Mientras tanto, el proceso es un *zombie* (ver [[06 - Control de procesos con wait, exec y terminación|wait y terminación]]).

![Tabla de procesos y estructura del PCB](adjuntos/Tabla%20de%20procesos%20y%20estructura%20del%20PCB.png)

> [!example]- Transcripción de la imagen
> A la izquierda, la memoria: el **Sistema Operativo** abajo (0x000-0x300) y encima los procesos 1, 2 y 3. Desde la zona del SO sale la **Tabla de procesos**, un arreglo con entradas numeradas de 1 a 255. Algunas entradas (3, 4, una intermedia y la 254) apuntan con flechas a un **PCB**. Cada PCB tiene los campos Estado, Parent Process ID (PPID), Program Counter (PC), Registros (`eax`, `ebx`, `sbp`, `sp`, …), Límites de memoria, Archivos abiertos, Ejecutable (binario), Prioridad y "…".

## Para qué sirve: sacar y reanudar

Si el SO saca un proceso de la CPU, tiene que **guardar su estado** (PC y registros) en el PCB. Cuando quiera reanudarlo, **carga en la CPU** esos mismos datos desde el PCB, y el proceso continúa como si nada hubiera pasado. Este es el [[04 - Cambio de contexto y tipos de procesos|cambio de contexto]].

> [!warning] El PCB no es una tabla de stacks
> El PCB describe y controla al proceso, pero **no administra su stack**. El stack vive en la memoria del proceso; el PCB solo guarda el *stack pointer* (`sp`) y el `sbp` entre sus registros, para poder restaurarlo.

## En Linux

En Linux, el PCB es la estructura `struct task_struct` (definida en `include/linux/sched.h`), que contiene entre otros:

- identificadores (`pid`, `tgid`) y credenciales (`uid`, `gid`);
- punteros a `parent`, `children` y `sibling`, que forman el árbol de procesos;
- los registros guardados en el cambio de contexto (`thread_struct`);
- un puntero a `mm_struct`, que describe la memoria del proceso;
- un puntero a `files_struct`, con la tabla de descriptores de archivos abiertos.

## Preguntas de repaso

> [!question]- ¿Por qué se compara el PCB con el registro civil?
> Porque es la ficha de identidad del proceso que mantiene el SO: su PID y el de su padre, su estado, su PC, sus registros y los recursos asignados. Su contenido se actualiza a lo largo de la vida del proceso.

> [!question]- ¿Qué se guarda en el PCB cuando un proceso sale de la CPU y para qué?
> El Program Counter y los registros de CPU. Así, al reanudarlo, el SO los vuelve a cargar y el proceso sigue en la instrucción exacta donde quedó.

> [!question]- ¿Es correcto decir que el PCB es una tabla que maneja los stacks?
> No. El stack está en la memoria del proceso y el PCB solo guarda el *stack pointer* entre sus registros. El PCB controla y describe al proceso, no administra su stack.

> [!question]- ¿Cuántas tablas de procesos hay y cuándo se libera un PCB?
> Una sola tabla para todos los procesos, con un PCB por proceso. El PCB de un proceso terminado se libera cuando su padre recoge el estado de salida con `wait()`.
