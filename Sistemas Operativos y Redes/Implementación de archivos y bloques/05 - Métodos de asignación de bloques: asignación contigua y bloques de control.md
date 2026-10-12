---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Implementación de archivos y bloques/04 - Estructuras en disco y en memoria del sistema de archivos virtual (VFS)\|04 - Estructuras en disco y en memoria del sistema de archivos virtual (VFS)]]"
---

# Métodos de asignación de bloques: asignación contigua y bloques de control

La asignación de bloques determina cómo se mapean los bytes lógicos de un archivo a los sectores físicos de almacenamiento secundario mediante estructuras de control de archivos (FCB).

## Bloques y asignación contigua (mis apuntes)

- BLOQUES
- Bloque de directorio
- Read (index)
- Voy a consultar tabla de archivos por procesos
- Luego voy a la tabla de archivos del sistema
- Leer Bloques de datos
- Bytes que son en si el archivo
- Luego voy a consultar a v-nodes para saber que funcion read (segun sistema de archivos) necesito utilizar
- File Control Block (bloque que contiene info para poder leer datos de un archivo)
- Bloques indice
- Bloques Indireccion (Simple, Doble)
- Los archivos no son solo blouqes de datos
- Hay un tamaño real, y un tamaño que ocupa en disco
- Necesito almacenar metadatos, datos extras
- PAra leer un archivo, tengo que cargar y cargar bloques
- La idea es no tener que andar dando tantas vueltas → Cada S.O Tendra una estrategia Distinta
- ESTRATEGIAS
- ASGINACION CONTIGUA
- que los archivos guarden sus bloque de datos de manera contigua
- Es bien sencillo de almacenar y leer
- La compactacion es costoso → queremos evitarlo
- - Problema → No se pueden guardar archivos pequeños → Compactar el archivo

> [!warning] Posible error
> En los apuntes aparecen erratas en `blouqes` (bloques), `ASGINACION` (asignación) y en la afirmación "No se pueden guardar archivos pequeños": en asignación contigua el problema crítico no son los archivos pequeños, sino la **fragmentación externa** del disco y la incapacidad de **crecimiento dinámico** de los archivos sin reubicación o compactación.

> [!tip] Complemento: Mecanismo de asignación contigua
> ![Asignación contigua de bloques de disco](adjuntos/Asignación%20contigua%20de%20bloques%20de%20disco.png)
>
> > [!example]- Transcripción de la imagen
> > **Diagrama de asignación contigua de bloques en disco:**
> > - Un archivo de $n$ bloques ocupa un rango continuo de direcciones físicas en disco: $b, b+1, b+2, \dots, b+n-1$.
> > - La entrada de directorio únicamente requiere registrar dos enteros:
> >   $$\text{Entrada} = (\text{nombre}, \text{bloque inicial } b, \text{longitud } n)$$
> > - **Ventajas:** rendimiento óptimo de lectura secuencial (el brazo no realiza *seek*) y acceso aleatorio instantáneo al bloque $i$ calculando la dirección física directa $b + i$.
> > - **Desventajas:** severa fragmentación externa similar a la de memoria contigua; requiere conocer el tamaño final al crear el archivo o ejecutar costosas compactaciones periódicas (*defragmentación*).

## Preguntas de repaso

> [!question]- ¿Por qué la asignación contigua ofrece el mejor rendimiento de transferencia de entrada/salida?
> Porque al residir todos los bloques del archivo en sectores y pistas consecutivas, el brazo lector del disco magnético solo ejecuta un único movimiento de búsqueda (*seek*) inicial y luego transfiere secuencialmente a velocidad máxima de rotación.

> [!question]- ¿Cómo se calcula la dirección del bloque lógico $k$ de un archivo en asignación contigua si comienza en el bloque $b$?
> La dirección física se calcula de forma directa e instantánea como $b + k$, sin necesidad de consultar tablas auxiliares ni realizar accesos adicionales a disco.

> [!question]- ¿Cuál es la principal limitación de la asignación contigua cuando un archivo necesita incrementar su tamaño?
> Si el bloque físico contiguo adyacente ($b + n$) ya se encuentra ocupado por otro archivo o estructura, el archivo no puede expandirse in situ y el kernel se ve obligado a reubicarlo por completo en un espacio libre mayor o abortar la escritura por falta de espacio contiguo.

