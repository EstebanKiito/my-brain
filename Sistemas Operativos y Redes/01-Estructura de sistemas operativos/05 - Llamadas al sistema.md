---
ramo: Sistemas Operativos y Redes
tema: Estructura de sistemas operativos
tags: [so/estructura-so, origen/apuntes]
prerrequisitos: ["[[02 - Modos de operación y anillos de protección|Modos de operación y anillos de protección]]", "[[04 - Interrupciones y excepciones|Interrupciones y excepciones]]"]
---
# Llamadas al sistema

Las llamadas al sistema (*system calls* o *syscalls*) constituyen la interfaz programática controlada mediante la cual los programas de usuario solicitan servicios al núcleo del sistema operativo.

## Comunicación con el sistema operativo (mis apuntes)
Para esto se usan las SYSCALL
SYSCALL
- Read
- Write
- Copiar
Tabla definida de opciones de operaciones para el S.O → guias de llamadas al systema
Son llamadas que se hacen al sistema
****— IMPORTANTE PARA LA TAREA 1 —*****
Se pueden llamar desde linea comandos, interfaz, etc

SYSCALLS
Interfaz de Llamadas al sistema
→ Cada S.O tiene su LIBRERIA para invocar Syscalls
Ejemplo
Al copiar un archivo → Pasan cosas por detras
- Verificar si existe el archivo
- Si tengo permisos para leerlo
- Si puede escribir en memoria

SYSCALL
Es una librería, serie de instrucciones para llamar al sistema
Cada sistema tiene la suya
→ LISTA
- Necesitamos de las syscalls para por ej: copiar un archivo
EJEMPLO DE SYSCALL (Copiar)
Para escribir una syscall, necesitamos permisos de kernell, y esto es peligroso, podria romper nuestro sistema

![Syscalls UNIX versus Win32](adjuntos/Syscalls%20UNIX%20versus%20Win32.png)

> [!example]- Transcripción de la imagen
> Comparativa de llamadas al sistema entre UNIX y la API Win32 de Windows:
> | Operación | UNIX | Win32 | Descripción |
> |---|---|---|---|
> | Crear proceso | `fork` | `CreateProcess` | Crea un nuevo proceso hijo |
> | Esperar proceso | `waitpid` | `WaitForSingleObject` | Espera que un proceso termine |
> | Cargar ejecutable | `execve` | *(none: CreateProcess = fork + execve)* | Reemplaza la imagen de memoria del proceso |
> | Terminar proceso | `exit` | `ExitProcess` | Termina la ejecución y retorna estado |
> | Abrir archivo | `open` | `CreateFile` | Abre un archivo existente o crea uno nuevo |
> | Cerrar archivo | `close` | `CloseHandle` | Cierra el descriptor o handle de archivo |
> | Leer datos | `read` | `ReadFile` | Lee datos desde el archivo hacia un buffer |
> | Escribir datos | `write` | `WriteFile` | Escribe datos de un buffer hacia el archivo |

![Clasificación de syscalls en UNIX](adjuntos/Clasificación%20de%20syscalls%20en%20UNIX.png)

> [!example]- Transcripción de la imagen
> Clasificación estándar de llamadas al sistema en UNIX:
> - **Process management:** `fork()`, `waitpid()`, `execve()`, `exit()`.
> - **File management:** `open()`, `close()`, `read()`, `write()`, `lseek()`, `stat()`.
> - **Directory and file-system management:** `mkdir()`, `rmdir()`, `link()`, `unlink()`, `mount()`, `umount()`.
> - **Miscellaneous:** `chdir()`, `chmod()`, `kill()`, `time()`.

![Llamadas al sistema al copiar un archivo](adjuntos/Llamadas%20al%20sistema%20al%20copiar%20un%20archivo.png)

> [!example]- Transcripción de la imagen
> Secuencia de syscalls ejecutadas por el comando `cp source.txt dest.txt`:
> 1. El proceso en *user space* invoca `stat` para verificar atributos y tamaño del origen.
> 2. Llama a `open` para abrir `source.txt` en modo lectura y `dest.txt` en modo escritura.
> 3. Emplea `mmap` o bucles sucesivos de `read` y `write` transfiriendo bloques de datos a través de memoria intermedia.
> 4. Al finalizar la transferencia, ejecuta `munmap` y `close` para liberar los descriptores de archivo.

> [!tip] Complemento (slides "Contenido 1: Invocación de Syscalls")
> Las aplicaciones rara vez ejecutan directamente la instrucción de máquina `syscall`. En su lugar, invocan la biblioteca estándar de C (`libc` / glibc):
> 1. El programa llama a una función envoltorio (*wrapper*) como `read(fd, buf, n)`.
> 2. La biblioteca coloca el identificador numérico de la llamada en un registro de CPU (por ejemplo, `%rax` en x86_64) y los argumentos en registros designados (`%rdi`, `%rsi`, `%rdx`).
> 3. Ejecuta la instrucción `syscall`, provocando el cambio a Ring 0 y saltando al dispatcher del kernel.
> 4. El kernel busca el número en la tabla de despacho (*syscall table*), valida los punteros del usuario, ejecuta la rutina interna y almacena el resultado o código de error (`errno`).

## Preguntas de repaso

1. ¿Por qué las aplicaciones de usuario utilizan funciones wrapper de bibliotecas (como `libc`) en lugar de invocar `syscall` directamente?
> [!question]- Respuesta
> Porque los wrappers ofrecen una API portable estándar (POSIX) en C, ocultando las particularidades de arquitectura y registros de máquina de cada procesador.

2. ¿Cómo valida el kernel la seguridad de los parámetros enviados en una syscall?
> [!question]- Respuesta
> Verifica que los punteros proporcionados pertenezcan al espacio de direcciones del proceso y no apunten a memoria protegida del kernel, y valida que el tamaño del buffer y los descriptores de archivo sean válidos.

3. ¿Qué llamadas al sistema intervienen para copiar un archivo (`cp origen destino`)?
> [!question]- Respuesta
> `open` para abrir origen y crear destino, `read` para transferir datos al buffer de memoria, `write` para vaciar el buffer al disco, y `close` para cerrar ambos descriptores.

4. ¿Qué diferencia de diseño existe entre la creación de procesos en UNIX y en Win32?
> [!question]- Respuesta
> UNIX separa la duplicación del proceso (`fork`) de la carga de un nuevo ejecutable (`execve`), mientras que Win32 combina ambas operaciones en una sola llamada de alto nivel (`CreateProcess`).

