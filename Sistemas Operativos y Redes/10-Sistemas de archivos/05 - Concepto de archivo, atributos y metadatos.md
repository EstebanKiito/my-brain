---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/01 - Capas de abstracción de entrada-salida y mecanismos de buffering\|01 - Capas de abstracción de entrada-salida y mecanismos de buffering]]"
---

# Concepto de archivo, atributos y metadatos

El disco solo sabe de bloques. Al usuario, en cambio, le interesan su tarea, su foto o su programa. El **archivo** es la abstracción que une ambos mundos: el SO presenta los bloques del disco como una unidad con nombre, tipo y permisos, y lleva la cuenta de todo eso en los **metadatos**.

## Qué es un archivo

- Es la **unidad mínima de almacenamiento para el usuario**.
- Es una **agrupación lógica de bytes**, una abstracción. En el disco, sus bloques pueden estar contiguos o enlazados (ver la implementación de bloques).
- Su **significado lo determina la forma en que se usa su contenido**: texto, imagen, código fuente, binario ejecutable…

Conociendo el formato, se sabe cómo interpretar el archivo, y el SO o el usuario saben con qué programa abrirlo.

## Cómo se caracteriza un archivo

| Atributo | Qué guarda |
|---|---|
| **Nombre de bajo nivel** | El identificador que usa el SO: el **número de inodo** (*inode number*) |
| **Nombre simbólico** | El nombre legible para humanos, como `helloworld.py` |
| **Tipo** | Lo **determina el contenido**; la extensión es solo una convención |
| **Ubicación** | Puntero a la dirección en disco de sus datos |
| **Tamaño** | Tamaño actual, en bytes o en bloques; puede incluir un máximo |
| **Protección** | Control de acceso: lectura, escritura, ejecución; en UNIX, `rwx` para el usuario, el grupo y los otros (`rwxrwxrwx`) |
| **Fechas** | Creación, último acceso, última modificación (en UNIX: `atime`, `mtime` y `ctime`, este último el cambio de metadatos) |
| **Usuario** | El propietario |
| **Atributos extendidos** | Más metadatos: codificación, *checksum*, programas asociados |

> [!tip] Dos nombres para lo mismo
> El SO trabaja con el **número de inodo**, un entero fijo y fácil de manejar. El humano usa el **nombre simbólico**. El [[06 - Estructura de directorios y resolución de rutas|directorio]] es justamente la tabla que traduce uno en otro. Gracias a esa separación, un mismo archivo puede tener varios nombres (ver [[02 - Enlaces duros (hard links) y enlaces simbólicos (soft links)|enlaces]]).

> [!warning] La extensión no define el tipo
> Renombrar `foto.png` a `foto.txt` no convierte la imagen en texto. En UNIX, el tipo real se reconoce por el contenido, típicamente por unos bytes fijos al inicio del archivo (*magic numbers*). Por ejemplo, un ejecutable ELF de Linux empieza con los bytes `0x7F 'E' 'L' 'F'`, y un script ejecutable con `#!` seguido de la ruta del intérprete. Además de los archivos regulares, el SO maneja otros tipos de "archivo": directorios, enlaces simbólicos, tuberías con nombre (FIFO) y dispositivos.

## Leer los metadatos de un archivo

La syscall `stat` entrega los metadatos de un archivo:

```c
#include <stdio.h>
#include <sys/stat.h>
#include <time.h>

int main(int argc, char *argv[]) {
    struct stat st;
    if (argc < 2 || stat(argv[1], &st) == -1) { perror("stat"); return 1; }
    printf("nombre de bajo nivel (inodo): %llu\n", (unsigned long long)st.st_ino);
    printf("tipo: %s\n", S_ISDIR(st.st_mode) ? "directorio" : S_ISREG(st.st_mode) ? "archivo regular" : "otro");
    printf("tamaño: %lld bytes en %lld bloques de 512 B\n", (long long)st.st_size, (long long)st.st_blocks);
    printf("permisos: %o\n", st.st_mode & 0777);
    printf("propietario (uid): %d\n", st.st_uid);
    printf("última modificación: %s", ctime(&st.st_mtime));
    return 0;
}
```

Con un archivo de texto de 11 bytes, el resultado muestra un tamaño de **11 bytes** pero **8 bloques de 512 B** (4 KB) ocupados en disco: el sistema de archivos asigna bloques completos, y el resto del bloque queda sin usar (fragmentación interna).

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre el nombre de bajo nivel y el nombre simbólico de un archivo?
> El de bajo nivel es el número de inodo, que usa el SO para identificar el archivo. El simbólico es el nombre legible por humanos, guardado en un directorio que lo asocia con el inodo.

> [!question]- ¿Qué determina el tipo de un archivo?
> Su contenido, es decir, cómo se interpretan sus bytes. La extensión es solo una convención que ayuda a elegir el programa con que abrirlo.

> [!question]- Menciona cinco atributos que guarda el SO de un archivo.
> Nombre de bajo nivel (inodo), tipo, ubicación en disco, tamaño, protección, fechas de creación, acceso y modificación, propietario y atributos extendidos.

> [!question]- ¿Por qué un archivo de 11 bytes puede ocupar 4 KB en disco?
> Porque el sistema de archivos asigna espacio en bloques completos: aunque el contenido mida 11 bytes, se reserva al menos un bloque entero.
