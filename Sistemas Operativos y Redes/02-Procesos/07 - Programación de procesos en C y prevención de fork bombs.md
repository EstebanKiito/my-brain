---
ramo: Sistemas Operativos y Redes
tema: Procesos
tags: [so/procesos, origen/apuntes]
prerrequisitos: ["[[05 - Jerarquía y creación de procesos con fork|Jerarquía y creación de procesos con fork]]", "[[06 - Control de procesos con wait, exec y terminación|Control de procesos con wait, exec y terminación]]"]
---
# Programación de procesos en C y prevención de fork bombs

Implementar procesos en lenguaje C requiere estructurar rigurosamente las llamadas a `fork()`, `exec()` y `wait()`, cuidando las condiciones de término para prevenir crecimiento descontrolado y ataques de denegación por bomba de bifurcación (*fork bomb*).

## Ayudantía 1 (mis apuntes)
16 / 8 / 2024

Tipos de datos
- Usar double mejor porque acepta mas cosas
- Punteros → Apuntan a direcciones de memoria, para la tarea 0 no se van a necesitar
- strutct
- argv : Cantidad de lineas que se recibe por comando
- enum: define constantes enteras

```c
structs Process{
	int pid,
	char* name,
	int argv
	
}

enum Sates{
	RUNNING
	WAITING
	FINISHED
}
```

Esto para procesos en memoria
- Estudiar : clock
- Estudiar: fork() → Crea procesos con id
- exec : distintos tipos de exec
- cada uno tiene sus argumentos
- wait : → Syscall
- #include sys.types.h
- #includes sys.wait.h

cuidado con fork
LA tarea pide padre hijo padre hijo, y no existe un hijo de un hijo
Podriamos crear hijos de manera exponencial, y el computador pordia fallar y apagarse
Teoricamente
El padre seria el programa principal
Y los hijos serian las funcionalidades por ejemplo

![Uso de fork en lenguaje C](adjuntos/Uso%20de%20fork%20en%20lenguaje%20C.png)

> [!example]- Transcripción de la imagen
> Fragmento de código en C mostrando el flujo de decisión tras `fork()`:
> ```c
> main() {
>     pid = fork();
>     if (pid == 0)
>         ChildProcess();
>     else
>         ParentProcess();
> }
> ```
> En el proceso padre `pid` recibe el PID del hijo (ejemplo: 3456), derivando a `ParentProcess()`; en el proceso hijo `pid` recibe 0, ejecutando `ChildProcess()`.

Fork retorna un id → Si es 0 es el proceso del hijo y si no del padre

![Ciclo de sincronización fork y wait](adjuntos/Ciclo%20de%20sincronización%20fork%20y%20wait.png)

> [!example]- Transcripción de la imagen
> Esquema de bifurcación y sincronización:
> - `fork`: Bifurca en `child program` y `main program (parent)`.
> - El proceso hijo ejecuta sus tareas y realiza `exit`.
> - El proceso padre alcanza la llamada `wait` y aguarda la señal de término del hijo antes de continuar su ejecución (`continue`).

El padre crea al hijo, se hace el exit, y se devuelve al padre, y al padre hay que hacerle un wait, esperando a lo que haga el hijo
Cuidado con los fork bomb, crear un for dentro de un while
Si hacemos fork pero ordenadamente dentro del while, y sabemos que termina todo OK
El hijo es una copia del padre, pero solo ejecuta la linea de comandos
exec es distinto al fork
Reemplaza el path que le damos
exec es un archivo .c que multiplica numeros
el child ya no es el codigo, si no que el archivo .c

> [!warning] Posible error (registrado en `_meta/Sistemas Operativos y Redes/DUDAS.md`)
> En el extracto de código de la ayudantía se conservaron las erratas de sintaxis del apunte original (`structs` por `struct`, `Sates` por `States`, `WAI` por `WAITING`). La sintaxis válida en C requiere `struct Process { ... };` y encabezados `#include <sys/types.h>` y `#include <sys/wait.h>`.

> [!tip] Complemento (slides "Contenido 2: Fork Bomb y ulimit")
> Una **bomba de bifurcación (*Fork Bomb*)** ocurre cuando un proceso genera copias recursivas de sí mismo sin condición de término:
> ```bash
> :(){ :|:& };:   # Fork bomb canónica en Bash
> ```
> Cada llamada genera 2 procesos, luego 4, 8, 16... saturando la tabla de procesos del kernel en milisegundos y congelando el sistema operativo.
>
> **Defensa del sistema:** Los administradores configuran límites con `ulimit -u <máximo_procesos>` o en `/etc/security/limits.conf` para acotar la cantidad máxima de procesos permitidos por usuario.

## Preguntas de repaso

1. ¿Cómo se distingue programáticamente si el código está corriendo en el proceso padre o en el proceso hijo tras un `fork()`?
> [!question]- Respuesta
> Evaluando el valor retornado por `fork()`: si el valor retornado es `0`, el flujo corre en el proceso hijo; si es mayor a cero (el PID del hijo), corre en el proceso padre.

2. ¿Qué ocurre en el sistema operativo durante una *Fork Bomb* y cómo se mitiga?
> [!question]- Respuesta
> Se crean procesos exponencialmente hasta agotar las entradas en la tabla de procesos del kernel y los PIDs disponibles, impidiendo ejecutar cualquier nuevo comando. Se mitiga configurando límites de recursos por usuario mediante `ulimit -u`.

3. ¿Por qué es necesario incluir `<sys/wait.h>` al implementar procesos padres en C?
> [!question]- Respuesta
> Porque declara las firmas de las funciones `wait()` y `waitpid()`, así como las macros para inspeccionar el estado de terminación del hijo (`WIFEXITED`, `WEXITSTATUS`).

4. ¿Cuál es la diferencia entre `fork()` y `exec()` en un programa en C?
> [!question]- Respuesta
> `fork()` crea un nuevo proceso clonando al llamador con un nuevo PID; `exec()` sustituye el código y memoria del proceso actual por un nuevo ejecutable, manteniendo el mismo PID sin crear un proceso adicional.

