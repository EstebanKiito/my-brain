---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Sistemas de archivos/01 - Capas de abstracción de entrada-salida y mecanismos de buffering\|01 - Capas de abstracción de entrada-salida y mecanismos de buffering]]"
---

# Concepto de archivo, atributos y metadatos

Un archivo constituye la unidad lógica elemental de almacenamiento persistente ofrecida al usuario, encapsulando una secuencia lineal de bytes junto con un conjunto estructurado de metadatos y atributos de control.

## Concepto de archivos y atributos (mis apuntes)

- ARCHIVOS
- Los archivos son la unidad minima de almacenamiento para el usuario
- Simplemente es una agrupacion de bytes (tiene que estar continua o linkeadas (los frames))
- Con el formato, sabemos como interpretar un archivo → El s.o sabra con que abrir el archivo
- Nombre → Low level (para el S.O)
- Nombre → Simbolico, leible para el humano “hellowoeld.py”
- tipo
- ubicacion
- tamaño
- proteccion
- etc
- Tienen datos:

> [!warning] Posible error
> En los apuntes aparece `“hellowoeld.py”` (error tipográfico por `helloworld.py`).

> [!tip] Complemento: Atributos y metadatos de un archivo
> 1. **Doble identificación de un archivo:**
>    - **Nombre simbólico (*human-readable*):** cadena de caracteres almacenada en la estructura del directorio que lo contiene.
>    - **Nombre de bajo nivel (*low-level name*):** número entero unívoco dentro del sistema de archivos, conocido como **número de inodo** (*inode number*) en entornos Unix/Linux.
> 2. **Metadatos esenciales (estructura de control o inodo):**
>    - **Tipo:** archivo regular, directorio, enlace simbólico, socket, tubería nombrada (FIFO) o archivo especial de dispositivo.
>    - **Ubicación:** punteros directos e indirectos a los bloques físicos en el almacenamiento.
>    - **Tamaño:** longitud actual en bytes y cantidad de bloques asignados en disco.
>    - **Protección y permisos:** bits de control de acceso (lectura, escritura, ejecución) para usuario, grupo y otros (`rwxrwxrwx`), además de bits especiales (SUID, SGID, Sticky).
>    - **Marcas de tiempo (*timestamps*):** fecha y hora de último acceso (`atime`), última modificación de datos (`mtime`) y último cambio de metadatos (`ctime`).
> 3. **Determinación del tipo de archivo:**
>    - En Unix, la extensión del archivo (p. ej. `.py`, `.c`, `.png`) es solo una convención de conveniencia para aplicaciones o usuarios. El kernel no impone semántica a la extensión.
>    - Herramientas y bibliotecas determinan el tipo real inspeccionando los **números mágicos** (*magic numbers*), que son secuencias de bytes fijas al inicio del contenido del archivo (cabecera).

## Preguntas de repaso

> [!question]- ¿Por qué el sistema de archivos separa el nombre legible del archivo de su identificador de bajo nivel (número de inodo)?
> Porque permite que múltiples nombres o enlaces de directorios distintos apunten al mismo archivo físico en disco (hard links) y simplifica la gestión interna del kernel, que opera con índices numéricos fijos en memoria y tablas de inodos en vez de manipular cadenas de longitud variable.

> [!question]- ¿Cómo determina un sistema tipo Unix el tipo real de un archivo ejecutable o script si el usuario cambia su extensión?
> El sistema analiza los primeros bytes del archivo (números mágicos o cabecera). Por ejemplo, un ejecutable ELF comienza con `0x7F 'E' 'L' 'F'`, y un script ejecutable comienza con el *shebang* `#!` seguido de la ruta al intérprete.

> [!question]- ¿Cuál es la diferencia entre el tamaño lógico de un archivo y el espacio físico que ocupa en disco?
> El tamaño lógico es la cantidad exacta de bytes útiles que contiene el archivo. El espacio físico en disco es siempre un múltiplo entero del tamaño de bloque del sistema de archivos (p. ej., bloques de 4 KB), pudiendo generar fragmentación interna en el último bloque asignado.
