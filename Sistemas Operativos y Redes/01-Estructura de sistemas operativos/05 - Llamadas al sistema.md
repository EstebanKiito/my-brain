---
ramo: Sistemas Operativos y Redes
tema: Estructura de sistemas operativos
tags: [so/estructura-so, origen/complemento]
prerrequisitos: ["[[02 - Modos de operación y anillos de protección|Modos de operación y anillos de protección]]", "[[04 - Interrupciones y excepciones|Interrupciones y excepciones]]"]
---
# Llamadas al sistema

Un programa en modo usuario no puede leer el disco ni crear procesos por su cuenta: tiene que pedírselo al sistema operativo. Las **llamadas al sistema** (*system calls* o *syscalls*) son la forma precisa de hacer ese pedido: una lista definida de operaciones que el SO ofrece, cada una con un punto de entrada controlado al kernel.

## Qué son y cómo se usan

Una syscall equivale a decir "por favor, sistema operativo, haz esto por mí". Operaciones como leer (`read`), escribir (`write`) o copiar un archivo terminan siempre en syscalls, aunque se lancen desde la línea de comandos o desde una interfaz gráfica.

- **Cada SO tiene su propio conjunto de syscalls**, y una **biblioteca** (estática o dinámica, en C) que las invoca. El programador llama a una función normal como `read(fd, buf, n)` y la biblioteca se encarga del resto.
- Una syscall es un **trap**: la biblioteca pone el número de la llamada y sus argumentos en registros de la CPU (en Linux x86-64, el número en `%rax` y los argumentos en `%rdi`, `%rsi`, `%rdx`…) y ejecuta la instrucción especial que pasa a modo kernel. El kernel ubica el código correspondiente en su tabla de syscalls y verifica los argumentos, por ejemplo que los punteros apunten a memoria del propio proceso. Luego ejecuta el servicio y devuelve el resultado, o un código de error en `errno`.
- En la ejecución participan el proceso de usuario, la biblioteca, el **vector de interrupciones** que el SO configuró en el hardware y el código de syscalls del kernel (ver [[04 - Interrupciones y excepciones|interrupciones]]).

> [!warning] Implementar una syscall es otra cosa
> *Usar* una syscall es seguro: el kernel valida cada pedido. *Escribir* una nueva requiere modificar código que corre con permisos de kernel, y un error ahí puede romper el sistema completo.

## Ejemplo: copiar un archivo

Detrás de `cp source.txt dest.txt` pasan muchas cosas:

1. Abrir el origen (`stat`, `open`). El SO verifica si existe y si hay permiso de lectura.
2. Leer el origen hacia una región de memoria (`mmap` o `read`).
3. Escribir desde memoria hacia el destino (`write`).
4. Liberar la memoria y cerrar los archivos (`munmap`, `close`).

Todas estas acciones requieren syscalls. Para verlas en Linux: `strace cp source.txt dest.txt`.

![Llamadas al sistema al copiar un archivo](adjuntos/Llamadas%20al%20sistema%20al%20copiar%20un%20archivo.png)

> [!example]- Transcripción de la imagen
> El comando `cp source.txt dest.txt` corre en *user space* como una sucesión de bloques cortos. Cada uno cruza la franja **Syscalls** hacia *kernel space*, donde aparecen en orden `stat`, `open`, `mmap`, `read`, `write`, `munmap` y `close`, y luego vuelve a *user space*.

Una versión mínima de `cp` escrita solo con syscalls:

```c
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc != 3) { fprintf(stderr, "uso: %s origen destino\n", argv[0]); return 1; }
    int in = open(argv[1], O_RDONLY);                            /* ¿existe? ¿puedo leerlo? */
    if (in < 0) { perror("open origen"); return 1; }
    int out = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (out < 0) { perror("open destino"); return 1; }
    char buf[4096];
    ssize_t n;
    while ((n = read(in, buf, sizeof buf)) > 0)                  /* disco -> memoria */
        write(out, buf, n);                                      /* memoria -> disco */
    close(in);
    close(out);
    return 0;
}
```

## Catálogo y portabilidad

![Clasificación de syscalls en UNIX](adjuntos/Clasificación%20de%20syscalls%20en%20UNIX.png)

> [!example]- Transcripción de la imagen
> Cuatro tablas de syscalls POSIX:
> - **Process management:** `fork()` (crea un hijo idéntico al padre), `waitpid(pid, &statloc, options)` (espera que un hijo termine), `execve(name, argv, environp)` (reemplaza la imagen del proceso) y `exit(status)` (termina y retorna el estado).
> - **File management:** `open`, `close`, `read`, `write`, `lseek` (mueve el puntero del archivo) y `stat` (información del archivo).
> - **Directory and file-system management:** `mkdir`, `rmdir` (borra un directorio vacío), `link`, `unlink`, `mount` y `umount`.
> - **Miscellaneous:** `chdir`, `chmod` (bits de protección), `kill` (envía una señal) y `time` (segundos desde el 1 de enero de 1970).

![Syscalls UNIX versus Win32](adjuntos/Syscalls%20UNIX%20versus%20Win32.png)

> [!example]- Transcripción de la imagen
> Equivalencias UNIX → Win32: `fork` → `CreateProcess`, `waitpid` → `WaitForSingleObject`, `execve` → *(none)*, porque `CreateProcess` = `fork` + `execve`; `exit` → `ExitProcess`, `open` → `CreateFile`, `close` → `CloseHandle`, `read` → `ReadFile`, `write` → `WriteFile`.

Definir una interfaz estándar ayuda a la **portabilidad**: un programa escrito contra ella compila en cualquier SO que la implemente.

- **POSIX** (*Portable Operating System Interface*, estándar IEEE 1003.1) define la interfaz entre las aplicaciones y los sistemas tipo UNIX.
- En Linux, la **SCI** (*System Call Interface*) más su implementación en glibc forman la API del kernel.
- En Windows está la *Native API* de NT (en `ntdll.dll`) y, sobre ella, la **Win32 API** (`kernel32.dll`, `advapi32.dll`, `user32.dll`).

## Preguntas de repaso

> [!question]- ¿Por qué los programas usan funciones de biblioteca en vez de ejecutar directamente la instrucción de syscall?
> Porque la biblioteca oculta los detalles de cada arquitectura (qué registros usar, qué instrucción ejecutar) y ofrece una interfaz estándar en C, como POSIX, que hace portable el programa.

> [!question]- ¿Qué verifica el SO cuando un programa intenta abrir un archivo para copiarlo?
> Que el archivo exista y que el proceso tenga permiso de lectura. También que los argumentos sean válidos, por ejemplo que los punteros apunten a memoria del propio proceso.

> [!question]- ¿Qué diferencia de diseño hay entre crear un proceso en UNIX y en Win32?
> UNIX separa la duplicación del proceso (`fork`) de la carga de otro programa (`execve`). Win32 hace ambas cosas en una sola llamada, `CreateProcess`.

> [!question]- ¿Por qué usar una syscall es seguro, pero escribir una nueva es peligroso?
> Al usarla, el kernel valida el pedido antes de ejecutarlo. Escribir una nueva implica agregar código que corre en modo kernel, sin esa protección, y un error ahí puede botar todo el sistema.
