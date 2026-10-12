---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/fat
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/05 - Métodos de asignación de bloques: asignación contigua y bloques de control\|05 - Métodos de asignación de bloques: asignación contigua y bloques de control]]"
---

# Asignación enlazada y tabla de asignación de archivos (FAT)

La asignación enlazada elimina la fragmentación externa conectando los bloques de un archivo como una lista ligada, cuya optimización centralizada en memoria dio origen a la Tabla de Asignación de Archivos (FAT).

## Asignación enlazada y FAT (mis apuntes)

- ASIGNACION ENLAZADA (LINKED)
- Almacena punteros a bloque siguiente
- Una parte de bloque es util para el dato (del archivo)
- Y una pequeña parte apunta al siguiente bloque
- - Problema O(n): Si quiero leer algo al final del archivo, al ser lista ligada, tengo que recorrer todos los bloques anteriores!!!
- Solucion: Lista Doblemente enlazada, pero igual para busquedas entremedios el mismo problema
- ASIGNACION LINKED FAT
- FAT: File allocation table
- Cada entrada de la tabla me apunta hacia otro bloque
- No tengo la referencia dentro del bloque de datos → Lo tengo dentro de una tabla
- Ahora solo me dirijo a la tabla para buscar cierto puntero, asociar un bloque con otro
- - Problema : Limitado por tamaño de tabla → Para FAT32 : 4GB por archivo
- direcciones 4 bytes → 32 bits : 2**32 = 4GB

> [!tip] Complemento: De la lista enlazada pura a la arquitectura FAT
> 1. **Asignación enlazada básica (*Linked Allocation*):**
>    ![Asignación enlazada de bloques de archivo](adjuntos/Asignación%20enlazada%20de%20bloques%20de%20archivo.png)
>    > [!example]- Transcripción de la imagen
>    > **Diagrama de asignación enlazada pura:**
>    > - Cada bloque físico contiene los datos útiles del archivo y un puntero de disco (p. ej. de 4 bytes) al bloque siguiente.
>    > - La entrada de directorio solo guarda el puntero al bloque inicial (*start*) y al bloque final (*end*).
>    > - **Ventajas:** sin fragmentación externa; cualquier bloque libre del disco puede anexarse al vuelo.
>    > - **Inconvenientes:** acceso aleatorio $O(n)$ sumamente costoso (para leer el bloque $k$ deben leerse los $k-1$ bloques anteriores de disco) y pérdida de alineación binaria de potencia de dos ($508\text{ B}$ de datos útiles en sectores de $512\text{ B}$).
>
> 2. **File Allocation Table (FAT):**
>    ![Asignación enlazada mediante tabla FAT](adjuntos/Asignación%20enlazada%20mediante%20tabla%20FAT.png)
>    > [!example]- Transcripción de la imagen
>    > **Estructura de la tabla FAT:**
>    > - Todos los punteros de enlace se extraen de los bloques de datos y se consolidan en una tabla contigua al inicio del volumen (*FAT*).
>    > - El índice de la tabla coincide con el número de bloque de datos en disco. El valor de la celda contiene el número del siguiente bloque o un valor centinela de fin de archivo (`EOF`).
>    > - La tabla FAT completa se almacena en memoria RAM, por lo que recorrer la cadena de punteros para acceso aleatorio se efectúa en microsegundos en RAM antes de leer el bloque final en disco.
>    > - **Límite de FAT32:** el campo de tamaño de archivo en la entrada de directorio ocupa exactamente 32 bits, limitando el tamaño máximo por archivo a $2^{32} - 1\text{ bytes} \approx 4\text{ GiB}$.

## Preguntas de repaso

> [!question]- ¿Por qué la búsqueda aleatoria en asignación enlazada pura es ineficiente frente a FAT?
> Porque en la asignación pura cada puntero está incrustado dentro del bloque en el disco, obligando a realizar $k$ lecturas físicas completas de disco para alcanzar el bloque $k$. En FAT la tabla reside en memoria RAM, por lo que el recorrido de punteros se resuelve instantáneamente en RAM y solo se ejecuta una lectura física al bloque de destino.

> [!question]- ¿Por qué un archivo en el sistema FAT32 no puede superar los 4 GB de tamaño?
> Porque la especificación de FAT32 define el campo de longitud del archivo en la entrada de directorio con un entero sin signo de 32 bits ($2^{32} - 1\text{ bytes} = 4\text{ GiB} - 1\text{ byte}$).

> [!question]- ¿Qué ocurre si se corrompe un único bloque intermedio en un sistema con asignación enlazada pura?
> Se pierde el puntero al bloque siguiente, desconectando el resto de la cadena y haciendo irrecuperables todos los bloques subsecuentes del archivo a menos que existan copias de respaldo o herramientas forenses de escaneo sectorial.

