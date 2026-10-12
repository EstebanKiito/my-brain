---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/vfs
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Implementación de archivos y bloques/03 - Montaje de sistemas de archivos y puntos de montaje\|03 - Montaje de sistemas de archivos y puntos de montaje]]"
---

# Estructuras en disco y en memoria del sistema de archivos virtual (VFS)

Para gestionar archivos de forma eficiente y uniforme, el sistema operativo mantiene estructuras de control persistentes en disco y estructuras transitorias en memoria coordinadas mediante la capa del Sistema de Archivos Virtual (VFS).

## Estructuras de partición y arquitectura VFS (mis apuntes)

- TABLA DE PARTICIONES
- Al inicio tenemos MBR (master boot record), indica partition Table
- Boot control block: Permite cargar el sistema operativo
- Volume Control Block: Datos de formato del sistema de archivos
- Virtual File System, es una interfaz comun para distintos sistemas de archivos
- Llama a sistema de archivos especifico, que utiliza cierto directorio / archivo
- Esto hace archivos tengan compatibilidad entre sistemas operativos
- VFS:
- Tiene una Tabla de archivos de procesos,
- Tiene una entrada unica por cada archivo abierto
- Cada V-Node apunta a una tabla de funciones (funciones que utiliza el archivo en especifico)
- Cada entrada apunta a un virtual node V-Node
- esta apunta a una Tabla Global de archivos abiertos

> [!tip] Complemento: Estructuras en disco frente a estructuras en memoria
> ![Estructuras en disco particiones MBR bloques de control y FCB](adjuntos/Estructuras%20en%20disco%20particiones%20MBR%20bloques%20de%20control%20y%20FCB.png)
>
> > [!example]- Transcripción de la imagen
> > **Estructuras de almacenamiento persistentes en disco:**
> > - **MBR / Partition Table:** ubicado al inicio del almacenamiento físico; describe la división en particiones.
> > - **Boot Control Block:** bloque inicial de una partición (sector de booteo) para cargar el kernel.
> > - **Volume Control Block (Superbloque):** metadatos del volumen: cantidad de bloques, tamaño de bloque, punteros a mapas de bits y tablas de inodos.
> > - **Estructura de directorios:** bloques que organizan la jerarquía de nombres.
> > - **File Control Block (FCB / Inodo):** almacena metadatos del archivo y punteros a bloques de datos.
>
> ![Arquitectura del sistema de archivos virtual VFS y v-nodes](adjuntos/Arquitectura%20del%20sistema%20de%20archivos%20virtual%20VFS%20y%20v-nodes.png)
>
> > [!example]- Transcripción de la imagen
> > **Arquitectura del Sistema de Archivos Virtual (VFS) en memoria:**
> > 1. **Tabla de descriptores por proceso:** cada proceso mantiene una tabla donde cada descriptor ($fd$) apunta a una entrada en la tabla global de archivos abiertos.
> > 2. **Tabla global de archivos abiertos del sistema:** contiene el modo de acceso, el desplazamiento actual (*offset*) y un puntero a la estructura V-Node.
> > 3. **V-Node (*Virtual Node*):** nodo abstracto del VFS independiente del sistema de archivos físico subyacente. Contiene una tabla de punteros a funciones (`vnode operations`: `read`, `write`, `lookup`) y enlaza directamente con el inodo del sistema de archivos real (ext4, NTFS, FAT32 o NFS).
>
> La capa VFS actúa como una interfaz polimórfica: la llamada `read(fd, ...)` invoca `vfs_read()`, la cual despacha a `vnode->v_op->read(...)` según el sistema de archivos montado.

## Preguntas de repaso

> [!question]- ¿Qué ventaja fundamental introduce la capa VFS (*Virtual File System*) en el kernel?
> Proporciona una interfaz orientada a objetos uniforme para las llamadas al sistema del usuario (`open`, `read`, `write`), abstrayendo las diferencias de implementación entre sistemas de archivos locales (ext4, FAT, NTFS) y remotos de red (NFS).

> [!question]- ¿Qué información se mantiene en la tabla global de archivos abiertos del sistema que NO reside en la tabla por proceso?
> El modo de apertura y bloqueo, el contador de referencias de procesos que comparten el archivo, y la posición actual de lectura/escritura (*file offset*), permitiendo que procesos que compartan una entrada (p. ej. tras un `fork()`) compartan el mismo desplazamiento.

> [!question]- ¿Cuál es la diferencia entre un Inodo (*Inode*) en disco y un V-Node en memoria?
> El inodo almacena metadatos y punteros a bloques de forma persistente en un formato propio de ese sistema de archivos. El V-Node es una estructura abstracta transitoria en memoria que unifica la representación del inodo y aloja los punteros a funciones polimórficas del controlador.

