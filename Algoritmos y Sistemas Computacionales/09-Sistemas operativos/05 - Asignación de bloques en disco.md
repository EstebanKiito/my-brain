---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Sistemas operativos"
tags:
  - algoritmos/sistemas-operativos
  - algoritmos/archivos
  - origen/complemento
prerrequisitos:
  - "[[04 - Archivos y directorios|Archivos y directorios]]"
---

# Asignación de bloques en disco

Un archivo se guarda en uno o más **bloques** del disco. La forma de asignarlos afecta la velocidad de acceso, el espacio desperdiciado y la facilidad para hacer crecer un archivo. Esta nota compara las estrategias clásicas: asignación contigua, FAT, bloque de índice y índice multinivel.

## Asignación contigua

El archivo ocupa $n$ bloques consecutivos a partir de un bloque inicial $b$: $b, b+1, \dots, b+n-1$. El directorio guarda el bloque inicial y el largo.

- **Ventaja:** acceder al bloque siguiente es inmediato; la lectura secuencial es muy rápida.
- **Problema:** **fragmentación externa**. Al borrar archivos quedan huecos entre bloques ocupados; un archivo nuevo puede no caber aunque haya espacio total suficiente.
- **Solución parcial:** compactación o defragmentación, que mueve los bloques para juntar el espacio libre.

## FAT (File Allocation Table)

La **FAT** es una tabla al inicio del disco con una entrada por bloque. El directorio guarda el nombre y el bloque inicial; cada entrada de la tabla apunta al siguiente bloque del archivo, y el último marca **EOF** (*end of file*).

- **Ventaja:** mejor acceso aleatorio que la asignación contigua, porque se puede seguir la cadena.
- **Problema:** el tamaño de la tabla limita el disco; en FAT32, un archivo no puede superar los 4 GB.

## Bloque de índice

El archivo tiene un **bloque de índice** que contiene la lista de bloques que lo forman.

- **Ventaja:** acceso aleatorio sin fragmentación externa; los bloques pueden estar dispersos.
- **Problema:** se pierde espacio en el bloque de índice, sobre todo en archivos muy pequeños.

## Índice multinivel

Si el archivo es muy grande, un solo bloque de índice no alcanza. La última entrada del índice apunta a otro bloque de índice, formando varios niveles, igual que una tabla de páginas multinivel.

Con bloques de 4 KB y punteros de 32 bits caben 1024 punteros por bloque. Dos niveles permiten direccionar $1024^2 = 1\,048\,576$ bloques, es decir, alrededor de 4 GB.

El **esquema combinado** usa los primeros $p$ punteros como bloques directos, los siguientes como índice simple, luego doble y triple. Así los archivos pequeños se acceden rápido y los grandes no pierden la capacidad de crecer.

> [!tip] La idea central
> No hay una estrategia perfecta: la asignación contigua es rápida pero fragmenta; la FAT es flexible pero limita el tamaño; el índice evita la fragmentación pero gasta espacio; el multinivel permite archivos grandes a costa de más accesos.

> [!warning] El bloque de índice no guarda los datos
> Guarda las **direcciones** de los bloques que contienen los datos. Es una tabla de contenido, no el contenido mismo.

## Preguntas de repaso

> [!question]- ¿Cuál es el problema principal de la asignación contigua?
> La fragmentación externa: al borrar archivos quedan huecos y un archivo nuevo puede no encontrar $n$ bloques consecutivos aunque haya espacio libre total.

> [!question]- ¿Cómo encuentra la FAT el siguiente bloque de un archivo?
> La entrada del bloque actual en la tabla apunta al siguiente bloque. La cadena termina cuando se llega a EOF.

> [!question]- ¿Qué ventaja tiene el bloque de índice frente a la FAT?
> Permite acceso aleatorio sin fragmentación externa: el índice tiene todas las direcciones de los bloques del archivo.

> [!question]- ¿Para qué sirve el índice multinivel?
> Para direccionar archivos más grandes que los que caben en un solo bloque de índice, encadenando bloques de índice.
