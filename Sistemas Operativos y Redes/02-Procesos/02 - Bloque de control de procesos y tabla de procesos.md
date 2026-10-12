---
ramo: Sistemas Operativos y Redes
tema: Procesos
tags: [so/procesos, origen/apuntes]
prerrequisitos: ["[[01 - Concepto de proceso y espacio de memoria|Concepto de proceso y espacio de memoria]]"]
---
# Bloque de control de procesos y tabla de procesos

El Bloque de Control de Procesos (*Process Control Block* o PCB) es la estructura de datos central que el sistema operativo utiliza para representar, identificar y gestionar el ciclo de vida completo de cada proceso en el sistema.

## PCB y tabla de procesos (mis apuntes)
PCB → Guarda informacion del proceso
Process Control Block
- Donde esta el codigo
- Program Counter
- Estados y Anchos
- Almacena toda la informacion de un Proceso
Puede cambiar
Es como la informacion tuya en el registro civil
Si un programa esta finished, luego de un tiempo se va limpiando por temas de espacio
Guarda Id del hijo y de si misma
Cuando se crea un proceso se crea una PCB
Hay una PCB por cada hijo (cada proceso que existe)
Todo esta en la misma tabla → El SO tiene solo 1 tabla para todos los procesos

ESQUEMA

![Tabla de procesos y estructura del PCB](adjuntos/Tabla%20de%20procesos%20y%20estructura%20del%20PCB.png)

> [!example]- Transcripción de la imagen
> Arquitectura de la tabla de procesos y composición del PCB:
> - **Memoria física:** Muestra procesos en ejecución (proceso 1, 2, 3) y la región del sistema operativo.
> - **Tabla de procesos del SO:** Arreglo central indexado (entradas 1 a 255...) donde cada entrada contiene un puntero a la estructura PCB de un proceso activo.
> - **Contenido del PCB:**
>   - Estado actual del proceso (Ready, Running, Waiting...).
>   - Parent Process ID (PPID) y Process ID (PID).
>   - Program Counter (PC): dirección de la próxima instrucción a ejecutar.
>   - Registros de CPU (`eax`, `ebx`, `sbp`, `sp`...).
>   - Límites y punteros de memoria (registros base y límite / tablas de páginas).
>   - Tabla de descriptores de archivos abiertos.
>   - Ruta y nombre del archivo binario ejecutable.
>   - Prioridad y estadísticas de scheduling.

Pregunta → El pcb controla los procesos → verdadero
Es una tabla que maneja los stacks → Falso!
Si saco un proceso de la CPU
Tengo que guardar su estado donde estaba
Pero quiero reanudarlo y quiero cargar en la Cpu los datos del procesos

> [!tip] Complemento (slides "Contenido 2: Estructuras del Kernel")
> En sistemas UNIX / Linux, la tabla de procesos se implementa en el kernel como una lista enlazada circular o un árbol jerárquico de estructuras `struct task_struct` (definida en `<linux/sched.h>`).
>
> **Campos fundamentales de `task_struct`:**
> - **Identificadores:** `pid` (identificador único del proceso), `tgid` (thread group ID), `uid`/`gid` (credenciales de seguridad del usuario).
> - **Relaciones genealógicas:** punteros a `parent`, `children` y `sibling`.
> - **Contexto de procesador:** estructura `thread_struct` con los registros guardados durante un cambio de contexto.
> - **Gestor de memoria:** puntero a `struct mm_struct` que describe la tabla de páginas y regiones de memoria virtual.
> - **Gestor de archivos:** puntero a `struct files_struct` con la tabla de descriptores de archivos abiertos (`fd`).

## Preguntas de repaso

1. ¿Qué es el Process Control Block (PCB) y por qué se compara con un "registro civil" del proceso?
> [!question]- Respuesta
> Porque es la ficha de identidad completa que mantiene el kernel para cada proceso, conteniendo su identificador único (PID), el de su padre (PPID), estado actual, registros de hardware y recursos asignados.

2. ¿Por qué es falso afirmar que el PCB "es una tabla que maneja los stacks"?
> [!question]- Respuesta
> Porque el PCB no administra el contenido de las pilas de llamadas (las cuales residen en el espacio de memoria virtual del proceso o en la pila de kernel); el PCB solo guarda el puntero de pila (Stack Pointer) para restaurar la ejecución.

3. ¿Qué información vital del PCB se guarda cuando un proceso es desalojado de la CPU?
> [!question]- Respuesta
> El Program Counter (dirección de la próxima instrucción) y el valor de todos los registros de propósito general y control de la CPU, permitiendo reanudar el proceso más tarde en el punto exacto donde fue pausado.

4. ¿Cuándo se elimina definitivamente el PCB de un proceso terminado de la tabla de procesos?
> [!question]- Respuesta
> Cuando el proceso padre invoca la llamada al sistema `wait()` o `waitpid()`, recogiendo el código de terminación del hijo y liberando su entrada (evitando que quede en estado zombie).

