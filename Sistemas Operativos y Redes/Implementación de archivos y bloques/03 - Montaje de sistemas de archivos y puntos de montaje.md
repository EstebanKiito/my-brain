---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Sistemas de archivos/06 - Estructura de directorios y resolución de rutas\|06 - Estructura de directorios y resolución de rutas]]"
---

# Montaje de sistemas de archivos y puntos de montaje

El mecanismo de montaje (*mount*) permite integrar volúmenes de almacenamiento secundarios y diversos tipos de sistemas de archivos dentro de una jerarquía de directorios única y unificada.

## Montaje de sistemas de archivos (mis apuntes)

- MONTURA SISTEMA DE ARCHIVOS
- Incorporar un dispositivo nuevo a nuestro sistema archivos, EJ: Montar memoria USB
```bash
mount /dev/sda1 /home/users
```
- En Windows → NTFS
- En un USB podriamos usar FAT32
- En Linux → ext4
- VFS (virtual file system) → Lo veremos mas adelante!
- Cuando yo monto un volumen nuevo, se hace en la carpeta MNT
- El S.O Debe tener una tabla, para saber que sistema de archivos se esta usando en cada directorio
- El rojo podria ser NTFS y azul FAT32

> [!tip] Complemento: Arquitectura de montaje y tabla de monturas
> ![Montaje de sistemas de archivos y tabla de monturas](adjuntos/Montaje%20de%20sistemas%20de%20archivos%20y%20tabla%20de%20monturas.png)
>
> > [!example]- Transcripción de la imagen
> > **Diagrama de montaje de sistemas de archivos y tabla de monturas (*Mount Table*):**
> > - El árbol de directorios global unifica diferentes dispositivos de bloques.
> > - Un directorio existente en el árbol (p. ej., `/mnt` o `/home/users`) se designa como **punto de montaje** (*mount point*).
> > - El comando `mount /dev/sda1 /home/users` asocia el dispositivo de bloques `/dev/sda1` al punto `/home/users`.
> > - **Tabla de monturas (*Mount Table*):** estructura mantenida en memoria por el kernel que registra cada punto de montaje, el dispositivo asociado, y el tipo de sistema de archivos (ext4, NTFS, FAT32).
>
> 1. **Efecto de enmascaramiento (*Shadowing*):**
>    - Si el directorio utilizado como punto de montaje contenía archivos o subdirectorios previos antes del montaje, estos quedan temporalmente ocultos e inaccesibles mientras dure la montura. Al desmontar el volumen con `umount`, los contenidos originales reaparecen intactos.
> 2. **Diferencias entre plataformas:**
>    - **Unix / Linux:** espacio de nombres unificado con una sola raíz global (`/`). Todos los discos y particiones se montan en algún subdirectorio del árbol común.
>    - **Windows:** espacio de nombres particionado mediante letras de unidad (`C:\`, `D:\`), aunque soporta también puntos de montaje NTFS sobre carpetas vacías.

## Preguntas de repaso

> [!question]- ¿Qué ocurre con los archivos previamente existentes en un directorio cuando se monta sobre él un nuevo sistema de archivos?
> Quedan temporalmente enmascarados (*shadowed*): el kernel redirige todas las operaciones de acceso al directorio raíz del nuevo sistema de archivos montado. Los archivos originales no se borran ni modifican y vuelven a ser visibles al ejecutar `umount`.

> [!question]- ¿Cuál es el propósito de la tabla de monturas (*Mount Table*) mantenida por el sistema operativo?
> Registrar la correspondencia entre los puntos de montaje activos en el árbol de directorios, el dispositivo físico de bloques asociado y el controlador o tipo de sistema de archivos (ext4, FAT, NTFS, etc.) necesario para traducir las llamadas de E/S.

> [!question]- ¿Cómo difiere el modelo de organización de unidades de almacenamiento entre Windows y sistemas tipo Unix?
> Unix unifica todos los dispositivos en un único árbol jerárquico bajo la raíz `/`, donde cada dispositivo se monta en un subdirectorio. Windows históricamente asigna letras de unidad independientes (`C:`, `D:`) a cada partición o dispositivo, creando árboles separados.

