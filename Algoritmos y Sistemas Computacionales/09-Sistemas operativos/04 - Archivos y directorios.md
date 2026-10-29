---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Sistemas operativos"
tags:
  - algoritmos/sistemas-operativos
  - algoritmos/archivos
  - origen/complemento
prerrequisitos:
  - "[[03 - Memoria y paginación|Memoria y paginación]]"
---

# Archivos y directorios

Los datos que deben sobrevivir al término de un programa se guardan en el disco, y el sistema operativo los organiza en **archivos** y **directorios**. El sistema de archivos es la parte del SO que traduce un nombre simbólico, como `informe.pdf`, a una dirección física en el disco.

## Qué es un archivo

Un **archivo** es una colección de información en almacenamiento secundario. Es la unidad de almacenamiento que ve el usuario y una agrupación lógica de bytes.

Su contenido puede ser cualquier cosa: texto, una imagen, código fuente o un ejecutable. El significado no lo pone el sistema operativo, sino la aplicación que lo usa: los mismos bytes pueden ser una foto para un programa y basura para otro.

> [!tip] La idea central
> El archivo tiene un nombre para las personas, pero el disco solo entiende bloques y direcciones. El sistema de archivos hace la traducción.

## Directorios y rutas

Los **directorios** organizan los archivos en forma de árbol. El sistema de archivos mantiene listas de archivos y sus ubicaciones, y permite encontrar un archivo siguiendo un **camino** (*path*).

- **Ruta absoluta:** parte desde la raíz. Por ejemplo, `/spell/mail/exp`.
- **Ruta relativa:** parte del directorio actual. Por ejemplo, `p/list` solo existe si el directorio actual es `/programs/`.
- **Directorio actual:** el que se usa como base para las rutas relativas; se consulta con `pwd`.

## Sistemas de archivos

Un **sistema de archivos** permite obtener una dirección de disco a partir de un nombre simbólico, un directorio, una ruta o un link. Algunos ejemplos:

| Sistema | Dónde se usa |
|---|---|
| ISO9660 | CD-ROM |
| UFS | Unix (basado en Berkeley FFS) |
| FAT, FAT32, NTFS | Windows |
| ext3, ext4 | Linux |
| GFS, FUSE | Sistemas distribuidos y en espacio de usuario |

> [!warning] El nombre no garantiza el contenido
> Cambiar la extensión de un archivo no cambia su contenido. Un `.txt` renombrado a `.jpg` sigue siendo texto; la aplicación que lo abre decide si puede interpretarlo.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre una ruta absoluta y una relativa?
> La absoluta parte desde la raíz del sistema (`/spell/mail/exp`); la relativa parte del directorio actual (`p/list`).

> [!question]- ¿Qué hace el sistema de archivos?
> Traduce nombres simbólicos, directorios y rutas a direcciones de bloques en el disco, y mantiene la organización de los archivos.

> [!question]- ¿El sistema operativo interpreta el contenido de un archivo?
> No. Solo lo almacena y lo entrega. El significado lo determina la aplicación que lo usa.

> [!question]- ¿Para qué sirve el directorio actual?
> Para resolver las rutas relativas. Si el directorio actual cambia, la misma ruta relativa puede apuntar a otro archivo.
