---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Implementación de archivos y bloques/01 - Interfaz y llamadas al sistema de archivos y directorios\|01 - Interfaz y llamadas al sistema de archivos y directorios]]"
---

# Enlaces duros (hard links) y enlaces simbólicos (soft links)

Los enlaces permiten compartir un archivo entre múltiples directorios bajo dos paradigmas fundamentales: punteros directos a nivel de inodo (*hard links*) o archivos especiales que almacenan una ruta textual (*soft links*).

## Enlaces duros y simbólicos (mis apuntes)

- LINKS
- Referencias a los procesos/archivos
- Existen 2
- Hardlinks:
- Apuntan directo al ( Inode ) dato en el disco, apunta al archivo real!
- Softlinks:
- Guarda una referencia con el path
- En el dibujo: HARDlink es por ejemplo el puntero de count al nodo (DIRECTO)
- SOFTlink seria por ejemplo el puntero que w apunta a otra ruta (PATH), pero no directamnete al nodo
- → Este se borra cuando se borran todos sus hardlinks
- Por lo tanto el nodo, deberia tener un contador de cuantos lo estan apuntando
- Si borro el hardlink, no necesariamente borro el archivo,
- Cuando borro un archivo original o lo muevo → EL SOFTLINK SE INVALIDA!

> [!warning] Posible error
> En los apuntes dice "Referencias a los procesos/archivos"; los enlaces son referencias exclusivas del sistema de archivos a archivos y directorios, no a procesos del kernel.

> [!tip] Complemento: Comparación arquitectónica de enlaces
> ![Diferencia entre hard links y soft links o enlaces simbólicos](adjuntos/Diferencia%20entre%20hard%20links%20y%20soft%20links%20o%20enlaces%20simbólicos.png)
>
> > [!example]- Transcripción de la imagen
> > **Diagrama conceptual de enlaces en sistemas de archivos:**
> > - **Hard link:** la entrada de directorio apunta directamente al número de inodo (*Inode*). Todos los hard links son indistinguibles entre sí; cada inodo mantiene un contador de referencias (`link_count`).
> > - **Soft link (enlace simbólico):** archivo especial con su propio inodo y tipo `S_IFLNK`, cuyo contenido es la cadena de caracteres de la ruta destino (*pathname*).
> > - **Ciclo de vida:** al invocar `unlink()`, se reduce `link_count`. El espacio en disco y el inodo solo se liberan cuando `link_count == 0` y no existan descriptores de archivo abiertos apuntando a él. Si el destino de un soft link es borrado, el soft link subsiste como enlace roto (*dangling link*).
>
> 1. **Diferencias técnicas cruciales:**
>    - **Fronteras de sistemas de archivos:** un *hard link* solo puede crearse dentro del mismo sistema de archivos físico, pues los números de inodo son únicos únicamente por volumen. Un *soft link* puede atravesar diferentes particiones o sistemas de archivos montados (e incluso recursos de red).
>    - **Enlaces a directorios:** los *hard links* a directorios están prohibidos para usuarios no privilegiados en Unix para evitar ciclos infinitos en el grafo de directorios. Los *soft links* a directorios sí están permitidos.
>    - **Comandos de creación:** `ln archivo_origen enlace_duro` (hard link) frente a `ln -s archivo_origen enlace_simbolico` (soft link).

## Preguntas de repaso

> [!question]- ¿Por qué está prohibido crear enlaces duros (*hard links*) hacia directorios en la mayoría de los sistemas Unix?
> Para impedir la formación de ciclos o grafos cíclicos arbitrarios en la estructura de directorios, lo que provocaría que algoritmos recursivos de búsqueda, conteo o respaldo entren en bucles infinitos y complicaría la detección de directorios huérfanos.

> [!question]- ¿Qué ocurre físicamente con los datos de un archivo en disco si se elimina el archivo original pero existe un enlace duro creado previamente?
> Los datos y el inodo permanecen intactos en el disco. La eliminación simplemente reduce en 1 el contador de referencias (`link_count`) del inodo; mientras el contador sea mayor que cero, el archivo sigue siendo completamente accesible a través del enlace duro restante.

> [!question]- ¿Por qué un enlace simbólico puede quedar roto (*dangling link*) mientras que un enlace duro nunca queda roto?
> Porque el enlace simbólico solo guarda una cadena de texto con la ruta. Si el archivo destino se elimina o se renombra, la ruta deja de apuntar a un objeto existente. Un enlace duro, en cambio, apunta directamente al inodo físico y retiene la existencia del archivo en disco mientras exista el enlace.

