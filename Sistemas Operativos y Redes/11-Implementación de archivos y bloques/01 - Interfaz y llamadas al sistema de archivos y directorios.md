---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/syscalls
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/05 - Concepto de archivo, atributos y metadatos\|05 - Concepto de archivo, atributos y metadatos]]"
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/06 - Estructura de directorios y resolución de rutas\|06 - Estructura de directorios y resolución de rutas]]"
---

# Interfaz y llamadas al sistema de archivos y directorios

El sistema operativo expone una API estandarizada de llamadas al sistema que permite a las aplicaciones crear, manipular, posicionar y sincronizar archivos y estructuras de directorios.

## API de archivos y directorios (mis apuntes)

- Clase 11
- 2/10/24
- Tablas que tengan punteros a otros directorios y/o otros archivos
- Directorios en bajo nivel:
- API de sistema de archivos
- Creacion: Open
- Lectura/Escritura: read, write
- Lectura/Escritura (no secuencial): lseek
- escritura inmediata : fsync
- renaming mv
- eliminar rm
- DIRECTORIOS
- Creacion: mkdir
- Lectura: opendir, readdir, closedir
- eliminacion rmdir

> [!warning] Posible error
> En los apuntes se listan `mv` y `rm` como funciones de la API; en realidad son comandos de usuario del shell que internamente invocan las llamadas al sistema POSIX `rename()` y `unlink()`.

> [!tip] Complemento: Semántica de las llamadas al sistema POSIX
> 1. **Operaciones sobre archivos:**
>    - `open(pathname, flags, mode)`: abre o crea un archivo. Retorna un descriptor de archivo entero no negativo ($fd$).
>    - `read(fd, buf, count)` y `write(fd, buf, count)`: transfieren bytes entre el espacio de usuario y el búfer del archivo. Avanzan implícitamente el puntero de posición (*offset*).
>    - `lseek(fd, offset, whence)`: reposiciona el puntero de lectura/escritura sin realizar operaciones de E/S físicas. Permite accesos aleatorios y la creación de archivos dispersos (*sparse files*).
>    - `fsync(fd)`: fuerza la escritura inmediata a disco de todos los bloques de datos y metadatos modificados retenidos en la caché de páginas del kernel (*page cache*).
> 2. **Operaciones sobre directorios:**
>    - `mkdir(pathname, mode)` y `rmdir(pathname)`: crean y eliminan directorios (el directorio a eliminar debe estar completamente vacío salvo por `.` y `..`).
>    - `opendir()`, `readdir()`, `closedir()`: funciones de la biblioteca estándar de C (`dirent.h`) que iteran secuencialmente sobre las entradas de directorio (`struct dirent`, conteniendo `d_ino` y `d_name`).

## Preguntas de repaso

> [!question]- ¿Por qué es necesaria la llamada al sistema `fsync()` tras realizar una operación de escritura crítica con `write()`?
> Porque `write()` retorna con éxito apenas los datos son copiados al búfer en memoria (*page cache*) del kernel. Si el sistema sufre un corte de energía antes de que el kernel descargue los datos al disco, la información se pierde; `fsync()` bloquea el proceso hasta que los bloques se graben físicamente en el almacenamiento secundario.

> [!question]- ¿Cómo permite `lseek()` optimizar el almacenamiento mediante archivos dispersos (*sparse files*)?
> Permite desplazar el puntero de posición más allá del final actual del archivo sin escribir ceros intermedios. El sistema de archivos no asigna bloques físicos de disco a los huecos vacíos, reservando bloques solo cuando se escriban datos reales.

> [!question]- ¿Qué llamada al sistema subyacente ejecuta el comando de terminal `rm` para eliminar un archivo?
> Ejecuta la llamada al sistema `unlink()`, la cual elimina la entrada de directorio especificada y decrementa el contador de enlaces duros del inodo asociado.

