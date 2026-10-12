---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/syscalls
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/05 - Concepto de archivo, atributos y metadatos\|05 - Concepto de archivo, atributos y metadatos]]"
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/06 - Estructura de directorios y resolución de rutas\|06 - Estructura de directorios y resolución de rutas]]"
---

# Interfaz y llamadas al sistema de archivos y directorios

El sistema de archivos se usa a través de una **API** (en UNIX, la del estándar POSIX): un conjunto de [[05 - Llamadas al sistema|llamadas al sistema]] para crear, leer, escribir y borrar archivos y directorios. Por debajo, los directorios son tablas con punteros a otros directorios o a archivos, pero el programa nunca las toca directamente: siempre pasa por esta API.

## Archivos

| Operación | Llamada | Qué hace |
|---|---|---|
| Creación y apertura | `open` | Abre (o crea) un archivo y devuelve un **descriptor de archivo** (`fd`), un entero que identifica el archivo abierto |
| Lectura y escritura | `read`, `write` | Transfieren bytes y **avanzan la posición** (el *offset*) en el archivo |
| Acceso no secuencial | `lseek` | Mueve la posición a cualquier byte, sin leer ni escribir; si se mueve más allá del final y se escribe ahí, queda un archivo disperso (*sparse*) cuyo hueco no ocupa bloques |
| Escritura inmediata | `fsync` | Obliga a escribir en disco lo que está en los buffers del kernel |
| Renombrar | `rename` (lo que usa el comando `mv`) | Cambia el nombre o la ubicación |
| Estado | `stat` | Entrega los metadatos del archivo |
| Eliminación | `unlink` (lo que usa el comando `rm`) | Quita la entrada del directorio |

> [!warning] `write` no significa "ya está en el disco"
> `write` retorna apenas los datos se copian a los buffers del kernel; el disco se actualiza después. Si se corta la luz antes, se pierden. Cuando importa (por ejemplo, en una base de datos), se llama a `fsync`, que bloquea hasta que los datos estén escritos.

## Directorios

| Operación | Llamada |
|---|---|
| Creación | `mkdir` |
| Lectura | `opendir`, `readdir`, `closedir` (recorren los pares nombre → inodo) |
| Eliminación | `rmdir` (solo si el directorio está vacío) |

## Ejemplo completo

```c
#include <dirent.h>
#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>

int main(void) {
    mkdir("carpeta", 0755);                                   /* crear directorio */
    int fd = open("carpeta/nota.txt", O_CREAT | O_RDWR | O_TRUNC, 0644);
    write(fd, "hola mundo", 10);                              /* escribe y avanza el offset */
    fsync(fd);                                                /* fuerza la escritura a disco */
    lseek(fd, 5, SEEK_SET);                                   /* salto no secuencial al byte 5 */
    char buf[6] = {0};
    read(fd, buf, 5);                                         /* lee "mundo" */
    printf("leído desde el byte 5: %s\n", buf);
    close(fd);

    rename("carpeta/nota.txt", "carpeta/nueva.txt");          /* lo que hace mv */
    struct stat st;
    stat("carpeta/nueva.txt", &st);
    printf("tamaño tras renombrar: %lld bytes\n", (long long)st.st_size);

    DIR *d = opendir("carpeta");                              /* recorrer el directorio */
    struct dirent *e;
    while ((e = readdir(d)) != NULL)
        printf("entrada: %-10s inodo %llu\n", e->d_name, (unsigned long long)e->d_ino);
    closedir(d);

    unlink("carpeta/nueva.txt");                              /* lo que hace rm */
    rmdir("carpeta");                                         /* solo si está vacío */
    return 0;
}
```

Al ejecutarlo se lee `mundo` desde el byte 5, y `readdir` lista las entradas `.`, `..` y `nueva.txt`, cada una con su número de inodo. Al final no queda nada: `unlink` borró el archivo y `rmdir` la carpeta ya vacía.

## Preguntas de repaso

> [!question]- ¿Qué llamada permite leer un archivo de forma no secuencial y cómo?
> `lseek`, que mueve la posición de lectura o escritura a cualquier byte del archivo sin transferir datos; el siguiente `read` o `write` actúa desde ahí.

> [!question]- ¿Por qué existe `fsync` si ya se llamó a `write`?
> Porque `write` deja los datos en buffers del kernel y retorna antes de que lleguen al disco. `fsync` espera a que queden escritos, para que no se pierdan ante un corte.

> [!question]- ¿Qué llamadas al sistema usan los comandos `mv` y `rm`?
> `mv` usa `rename`, que cambia el nombre o la ubicación, y `rm` usa `unlink`, que quita la entrada del directorio.

> [!question]- ¿Qué entrega `readdir` al recorrer un directorio?
> Una entrada por vez, cada una con el nombre y el número de inodo; incluye siempre `.` y `..`.
