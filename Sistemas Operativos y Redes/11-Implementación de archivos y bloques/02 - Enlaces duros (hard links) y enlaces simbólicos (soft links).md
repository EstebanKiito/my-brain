---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/01 - Interfaz y llamadas al sistema de archivos y directorios\|01 - Interfaz y llamadas al sistema de archivos y directorios]]"
---

# Enlaces duros (hard links) y enlaces simbólicos (soft links)

A veces conviene que un mismo archivo aparezca en dos directorios, por ejemplo para compartirlo entre usuarios sin copiarlo. La forma sencilla de hacerlo es con **enlaces** (*links*): referencias a archivos. Hay dos tipos, y la diferencia está en **a qué apunta** cada uno.

## Los dos tipos

| | **Hard link** (`ln`) | **Soft link** o enlace simbólico (`ln -s`) |
|---|---|---|
| Apunta a | **Directo al inodo**: al archivo real en el disco | **Una ruta** (*path*): guarda el nombre del archivo, no el archivo |
| Qué es | Otro par (nombre, inodo) en un directorio, con el mismo inodo que el original | Un archivo especial cuyo contenido es la ruta del destino |
| Si se borra el original | El archivo sigue existiendo mientras quede algún hard link | **El soft link se invalida**: queda roto y hay que borrarlo a mano |
| Si se mueve el original | Sigue funcionando | Se invalida |

Recordando que un [[06 - Estructura de directorios y resolución de rutas|directorio]] es una tabla de pares (nombre → inodo), un hard link es simplemente **otro nombre para el mismo inodo**: todos los nombres son igual de "originales".

![Diferencia entre hard links y soft links o enlaces simbólicos](adjuntos/Diferencia%20entre%20hard%20links%20y%20soft%20links%20o%20enlaces%20simb%C3%B3licos.png)

> [!example]- Transcripción de la imagen
> Grafo de directorios: *root* con dos directorios, **dict** (entradas *list*, *all*, *w*, *count*) y **spell** (entradas *count*, *words*, *list*). La entrada *count* de dict y la *count* de spell apuntan al **mismo** archivo. La entrada *w* de dict y la *words* de spell llevan al mismo subdirectorio (con *list*, *rade*, *w7*). La entrada *all* de dict apunta al archivo *list* de ese subdirectorio.

Leyendo la figura: el *count* compartido es como un **hard link**, un puntero directo al mismo nodo. Una entrada como *w*, que llega a otro lugar a través de una ruta, ilustra la idea de un **soft link**: no apunta al nodo, sino al camino para llegar a él.

## Borrar con enlaces: el contador de referencias

Si un archivo puede tener varios nombres, borrar uno no puede borrar los datos. Por eso **el inodo lleva un contador** de cuántos hard links lo apuntan:

- crear un hard link **aumenta** el contador;
- borrar un nombre (`rm`, es decir, `unlink`) **lo disminuye**;
- el archivo **solo se elimina cuando no quedan referencias** a él (contador en 0) y ningún proceso lo tiene abierto.

Así, borrar un hard link no necesariamente borra el archivo. Los soft links, en cambio, no cuentan: si se borra el archivo original, el soft link sigue existiendo pero apunta a una ruta que ya no existe.

```c
#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>

void mostrar(const char *nombre) {
    struct stat st;
    if (stat(nombre, &st) == 0)          /* stat sigue los soft links hasta el archivo real */
        printf("%-8s -> inodo %llu, %d hard link(s)\n", nombre,
               (unsigned long long)st.st_ino, (int)st.st_nlink);
    else
        printf("%-8s -> no se puede abrir (enlace roto)\n", nombre);
}

int main(void) {
    close(open("original", O_CREAT | O_WRONLY, 0644));
    link("original", "duro");          /* ln original duro   : otro nombre, mismo inodo */
    symlink("original", "blando");     /* ln -s original blando: guarda la ruta "original" */
    mostrar("original"); mostrar("duro"); mostrar("blando");

    unlink("original");                /* rm original */
    printf("-- después de borrar 'original' --\n");
    mostrar("duro"); mostrar("blando");
    unlink("duro"); unlink("blando");
    return 0;
}
```

Al ejecutarlo, los tres nombres muestran el mismo inodo con 2 hard links (`original` y `duro`; `blando` no cuenta). Tras borrar `original`, `duro` sigue funcionando con 1 hard link, y `blando` queda **roto**.

> [!warning] Restricciones de los hard links
> Un hard link solo puede crearse **dentro del mismo sistema de archivos**, porque los números de inodo son únicos solo dentro de cada uno. Además, en UNIX normalmente no se permiten hard links a directorios, para no crear ciclos en el árbol. Los soft links no tienen ninguna de las dos restricciones.

## Preguntas de repaso

> [!question]- ¿A qué apunta un hard link y a qué un soft link?
> El hard link apunta directamente al inodo, el archivo real. El soft link guarda la ruta del archivo, es decir, su nombre.

> [!question]- ¿Qué pasa con los datos si se borra el archivo original pero existe un hard link?
> Nada: el contador de referencias del inodo baja de 2 a 1 y los datos siguen accesibles por el hard link. Solo se borran cuando el contador llega a 0.

> [!question]- ¿Qué pasa con un soft link si se borra o se mueve el archivo original?
> Se invalida: sigue existiendo, pero apunta a una ruta que ya no existe, y hay que borrarlo a mano.

> [!question]- ¿Por qué un hard link no puede apuntar a un archivo de otro sistema de archivos?
> Porque apunta por número de inodo, y ese número solo identifica un archivo dentro de su propio sistema de archivos.
