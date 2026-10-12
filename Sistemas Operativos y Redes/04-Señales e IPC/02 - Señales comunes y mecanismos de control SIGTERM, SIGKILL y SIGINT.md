---
ramo: "Sistemas Operativos y Redes"
tema: "Señales e IPC"
tags:
  - ssoo
  - senales
  - sigterm
  - sigkill
  - sigint
  - sigstop
prerrequisitos:
  - "[[01 - Concepto de señal y ciclo de vida de señales POSIX]]"
---

# Señales comunes y mecanismos de control SIGTERM, SIGKILL y SIGINT

En sistemas tipo UNIX existen señales estándar destinadas al control del ciclo de vida de los procesos, diferenciándose fundamentalmente en su **capacidad de intercepción** y en el **grado de amabilidad** de la terminación.

---

## SEÑALES → Siempre se pregunta (mis apuntes)

> - Aca le preguntar a terminar
> - Sigterm: le avisa que debe terminar
> - El proceso lo terminan sin preguntar
> - SIGKILL: Mata/Termina el proceso
> - SIGINT: Interrumpe → Se interrumpe el proceso (Le puedo mandar cosas) → Es como Esperame un poco
> - SIGSTP: Stop → Detenerlo implica guardar lo que tiene para usarlo después
> - SIGCOM: Continua

> [!warning] Posible error en apuntes
> * *"Aca le preguntar a terminar"*: redacción coloquial para indicar que con `SIGTERM` se solicita amablemente la terminación del proceso, permitiéndole liberar recursos antes de salir.
> * *"SIGSTP"*: se refiere a `SIGTSTP` (señal 20, parada por terminal con `Ctrl+Z`) o `SIGSTOP` (señal 19, detención incondicional por kernel).
> * *"SIGCOM"*: errata evidente por `SIGCONT` (señal 18, reanuda un proceso previamente detenido).

---

> [!tip] Complemento: Comparativa exhaustiva de señales clave
> 
> | Señal | Número | Origen típico | Acción por defecto | ¿Es interceptable / bloqueable? | Propósito y semántica |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | **`SIGINT`** | 2 | Teclado (`Ctrl+C`) | Terminar | **Sí** | Interrupción interactiva. El programa puede capturarla para confirmar salida o guardar cambios. |
> | **`SIGKILL`** | 9 | `kill -9 <pid>` | Terminar forzado | **NO** | Terminación inmediata sin condiciones. La procesa el kernel directamente; el proceso no puede capturarla ni ignorarla. |
> | **`SIGTERM`** | 15 | `kill <pid>` | Terminar | **Sí** | Solicitud formal de término ("aviso educado"). Permite cerrar conexiones, limpiar archivos temporales y liberar memoria. |
> | **`SIGSTOP`** | 19 | `kill -STOP <pid>` | Detener (*Stop*) | **NO** | Pausa incondicional del proceso a nivel de kernel. |
> | **`SIGTSTP`** | 20 | Teclado (`Ctrl+Z`) | Detener (*Stop*) | **Sí** | Suspensión interactiva generada desde la terminal de usuario (*Terminal Stop*). |
> | **`SIGCONT`** | 18 | `kill -CONT`, `fg`, `bg` | Continuar | **Sí** (parcial) | Reanuda la ejecución de un proceso que se encontraba en estado suspendido. |
> | **`SIGSEGV`** | 11 | CPU (Fallo memoria) | Core Dump | **Sí** | Violación de segmento de memoria (acceso a puntero inválido o fuera del espacio virtual). |
> | **`SIGCHLD`** | 17 | Hijo terminado/pausado | Ignorar | **Sí** | Notificación al proceso padre de que un hijo cambió de estado, indicando que debe invocar `wait()`. |

---

> [!tip] Complemento: Terminación suave (SIGTERM) frente a terminación forzada (SIGKILL)
> 1. **La regla de oro de la administración de sistemas:**
>    - Primero se despacha **`SIGTERM` (15)** para permitir un apagado ordenado (*graceful shutdown*).
>    - Si tras un tiempo prudencial el proceso sigue bloqueado o colgado en un recurso, se envía **`SIGKILL` (9)** como último recurso.
> 2. **Peligros de usar `kill -9` (`SIGKILL`) indiscriminadamente:**
>    - El proceso no ejecuta ningún manejador de salida ni las rutinas registradas con `atexit()`.
>    - Puede dejar bases de datos en estado inconsistente, archivos a medio escribir o bloqueos (*locks*) huérfanos en disco.

---

## Preguntas de repaso

> [!question]- ¿Por qué no es posible capturar ni ignorar la señal SIGKILL?
> Porque el sistema operativo debe garantizar que el administrador (root) siempre posea un mecanismo infalible para eliminar cualquier proceso desbocado, malicioso o con un bucle infinito que no responda a solicitudes cooperativas.

> [!question]- ¿Cuál es la diferencia entre SIGINT y SIGTERM?
> `SIGINT` (señal 2) es emitida habitualmente por el usuario desde la consola mediante `Ctrl+C` para interrumpir la tarea actual en primer plano. `SIGTERM` (señal 15) es la señal estándar de terminación que envían scripts o herramientas de administración del sistema para solicitar el cierre voluntario y ordenado de un proceso.

> [!question]- ¿Qué par de señales se utilizan para pausar y reanudar un proceso en segundo plano?
> Se utiliza `SIGSTOP` (o interactivamente `SIGTSTP` con `Ctrl+Z`) para suspender el proceso, y `SIGCONT` para reanudar su ejecución en primer o segundo plano.

