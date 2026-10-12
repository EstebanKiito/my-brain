---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/vfs
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/03 - Montaje de sistemas de archivos y puntos de montaje\|03 - Montaje de sistemas de archivos y puntos de montaje]]"
---

# Estructuras en disco y en memoria del sistema de archivos virtual (VFS)

Un sistema de archivos permite obtener una **dirección de disco** (un bloque) a partir de datos simbólicos: nombre de archivo, directorio, ruta, links. Para hacerlo necesita dos tipos de estructuras: unas **en disco**, que persisten y describen la partición, y otras **en memoria**, que agilizan el trabajo con los archivos abiertos. El **VFS** es la capa que permite que todo esto funcione igual con cualquier sistema de archivos.

Existen muchos: ISO9660 (CD-ROM), UFS (basado en el Berkeley Fast File System), FAT, FAT32 y NTFS (Windows), ext3 y ext4 (Linux), HFS+ (macOS), además de VFS y FUSE.

## Estructuras en disco

![Estructuras en disco particiones MBR bloques de control y FCB](adjuntos/Estructuras%20en%20disco%20particiones%20MBR%20bloques%20de%20control%20y%20FCB.png)

> [!example]- Transcripción de la imagen
> *Entire disk*: al inicio el **MBR**, con la *Partition table*, y luego varias *Disk partition*. Una partición ampliada contiene, en orden: *Boot block*, *Superblock*, *Free space mgmt*, *I-nodes*, *Root dir* y *Files and directories*. Flechas rojas a mano conectan la tabla de particiones con las particiones y señalan cada bloque.

| Estructura | Qué contiene | En UNIX / en Windows |
|---|---|---|
| **MBR** (sector 0) | La **tabla de particiones** | — |
| **Boot control block** (uno por partición) | Lo necesario para **cargar el SO** desde esa partición | *Boot block* / *Partition Boot Sector* |
| **Volume control block** | **Datos de formato** del sistema de archivos: tipo, número de bloques… | *Superblock* / *Master File Table* |
| **Estructura de directorios** | Los directorios y la organización de los archivos | — |
| Gestión de espacio libre, inodos, archivos | El resto de la partición; cada archivo tiene su bloque de control (FCB), que en UNIX es el **inodo** | — |

## Estructuras en memoria principal

Para no ir al disco en cada operación, el SO mantiene en RAM:

- la **tabla de montajes** (*mount table*): los sistemas de archivos montados;
- los **directorios recientes** (caché);
- la **tabla de archivos abiertos del sistema**;
- la **tabla de archivos abiertos por proceso**;
- los **buffers de bloques de disco**.

## El VFS (*Virtual File System*)

El VFS es una **interfaz común para distintos sistemas de archivos**: el programa llama siempre a `read`, y el VFS llama a la función del sistema de archivos específico que corresponde a ese archivo. **Cualquier sistema de archivos que implemente la interfaz del VFS puede incorporarse al sistema**, y por eso se pueden usar archivos de distintos sistemas de archivos (por ejemplo, un pendrive FAT32 en Linux), e incluso sistemas de archivos remotos, como NFS.

```mermaid
flowchart LR
  P["Tabla del proceso: fd"] --> D["Tabla de archivos abiertos: una entrada por archivo abierto"]
  D --> V["v-node: punto de acceso al archivo"]
  V --> F["Tabla de funciones del sistema de archivos: read, write, open"]
  F --> R["read concreto de ext4, FAT32…"]
```

- La tabla de **archivos abiertos** mantiene los **descriptores de archivo**: estructuras en memoria con información del archivo, con **una entrada única por cada archivo abierto**. Ahí se guarda, entre otras cosas, la posición actual de lectura (el *offset*); por eso un padre y un hijo creado con `fork()` comparten esa posición en los archivos que tenían abiertos.
- Cada entrada apunta a un **v-node** (*virtual node*), el punto de acceso al archivo.
- Cada v-node apunta a una **tabla de funciones** del sistema de archivos concreto, que ejecutan las llamadas (`read`, `write`, …).

![Arquitectura del sistema de archivos virtual VFS y v-nodes](adjuntos/Arquitectura%20del%20sistema%20de%20archivos%20virtual%20VFS%20y%20v-nodes.png)

> [!example]- Transcripción de la imagen
> Dentro de un óvalo **VFS**: la *Process table* (entradas 0, 2, 4) apunta a *File descriptors*, estos a *V-nodes*, y cada v-node a una tabla de *Function pointers* (*write*, *read*, *open*), recuadrada en rojo. Una flecha *Call from VFS into FS 1* lleva a la *Read function* del sistema de archivos **FS 1**, también recuadrada en rojo.

## Preguntas de repaso

> [!question]- ¿Qué guarda el volume control block y cómo se llama en UNIX?
> Los datos de formato del sistema de archivos: su tipo, el número de bloques y otros parámetros. En UNIX se llama *superblock* (en Windows, *Master File Table*).

> [!question]- ¿Para qué sirve el VFS?
> Para ofrecer una interfaz común a todos los sistemas de archivos: el programa usa las mismas llamadas y el VFS las dirige a las funciones del sistema de archivos concreto. Así se puede incorporar cualquier sistema de archivos que implemente esa interfaz.

> [!question]- Describe el camino de un `read(fd, …)` a través del VFS.
> Con el `fd` se busca la entrada en la tabla de archivos abiertos, que apunta a un v-node, que apunta a la tabla de funciones del sistema de archivos concreto. Desde ahí se llama a su función `read`.

> [!question]- ¿Qué estructuras mantiene el SO en memoria para los archivos?
> La tabla de montajes, los directorios recientes, la tabla de archivos abiertos del sistema, la de cada proceso y los buffers de bloques de disco.
