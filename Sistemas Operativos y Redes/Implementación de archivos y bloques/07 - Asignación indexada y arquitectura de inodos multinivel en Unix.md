---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/inodos
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/Implementación de archivos y bloques/06 - Asignación enlazada y tabla de asignación de archivos (FAT)\|06 - Asignación enlazada y tabla de asignación de archivos (FAT)]]"
---

# Asignación indexada y arquitectura de inodos multinivel en Unix

La asignación indexada concentra los punteros a bloques de datos en bloques de índices dedicados, permitiendo acceso aleatorio directo sin fragmentación externa y escalando a archivos multiterabyte mediante la arquitectura combinada de inodos de Unix.

## Asignación indexada y bloques de indirección (mis apuntes)

- ASIGNACION INDEXADA
- Punteros (bloques de indices) hacia Bloque de datos
- Cada archivo presenta su propio bloque de indices (se puede interpretar como una tabla)
- Cada bloque de indice → Apunta a un BLOQUE DE DATOS
- Se pierde espacio por tamaño de index block
- Puede haber sobreasignacion dado que los bloques tienen tamaños constantes → y si un archivo por ejemplo pesa menos de 4kb cae dentro de un bloque de indice, sobran n-1
- ESQUEMA ENLZADO: Ultimo bloque de indice, apunta a la siguiente tabla de bloques de indices → No muy util → Mejor tener :
- INDICE MUTINIVEL!!!!
- ASGINACION COMBINADA (BLOQUES DE INDIRECCION)
- Bloques indirectos → Apuntas a bloques de indices → Apuntan a bloques de datos
- Ej: Direccion simple → Como se ve en la figura : Bloque indireccion simple → Bloque indice → Bloque de datos
- Tamaño posible: 1024*1024*32KB = 4 TB !!!

> [!warning] Posible error
> En los apuntes aparecen erratas en `ENLZADO` (enlazado), `MUTINIVEL` (multinivel), `ASGINACION` (asignación) y `Direccion simple` (indirección simple). Además, en el cálculo de capacidad `1024*1024*32KB = 4 TB`, para bloques de 4 KB con punteros de 4 bytes (1024 punteros/bloque), 4 TB corresponde al límite del nivel de indirección triple ($1024^3 \times 4\text{ KB} = 4\text{ TB}$).

> [!tip] Complemento: Arquitectura de inodos combinados multinivel (Unix FFS / ext)
> 1. **Asignación indexada pura:**
>    ![Asignación indexada con bloque de índices](adjuntos/Asignación%20indexada%20con%20bloque%20de%20índices.png)
>    > [!example]- Transcripción de la imagen
>    > **Diagrama de asignación indexada:**
>    > - El inodo o directorio contiene un único puntero al bloque de índices (*index block*).
>    > - El bloque de índices contiene un arreglo ordenado de punteros a los bloques de datos físicos.
>    > - Provee acceso aleatorio directo en $O(1)$, pero desperdicia espacio en archivos muy pequeños al requerir un bloque completo de índices.
>
> 2. **Esquema combinado multinivel de inodos en Unix:**
>    ![Asignación combinada multinivel e inodos Unix](adjuntos/Asignación%20combinada%20multinivel%20e%20inodos%20Unix.png)
>    ![Estructura de direccionamiento indirecto en inodos](adjuntos/Estructura%20de%20direccionamiento%20indirecto%20en%20inodos.png)
>    > [!example]- Transcripción de las imágenes
>    > **Estructura jerárquica del Inodo Unix (bloques de 4 KB y punteros de 4 bytes = 1024 entradas por bloque):**
>    > - **12 Punteros directos:** apuntan directamente a bloques de datos ($12 \times 4\text{ KB} = 48\text{ KB}$). Cubren eficientemente la gran mayoría de archivos pequeños sin accesos extra a disco.
>    > - **1 Puntero indirecto simple:** apunta a un bloque de índices con 1024 punteros a datos ($1024 \times 4\text{ KB} = 4\text{ MB}$).
>    > - **1 Puntero indirecto doble:** apunta a un bloque que apunta a 1024 bloques de índices ($1024^2 \times 4\text{ KB} = 4\text{ GB}$).
>    > - **1 Puntero indirecto triple:** añade tres niveles de indirección ($1024^3 \times 4\text{ KB} = 4\text{ TB}$).

## Preguntas de repaso

> [!question]- ¿Por qué la mayoría de los sistemas Unix reservan 12 punteros directos en el inodo antes de recurrir a la indirección?
> Porque los estudios empíricos demuestran que la gran mayoría de los archivos en sistemas reales son pequeños ($\le 48\text{ KB}$). Los punteros directos permiten acceder a esos archivos sin sobrecarga de lecturas adicionales a bloques de índices.

> [!question]- ¿Cuántos accesos a disco se requieren para leer un byte ubicado en el rango de un puntero indirecto doble si ninguna estructura está en caché?
> Se requieren 3 lecturas de disco: primero leer el bloque de indirección doble, luego leer el bloque de índices de segundo nivel correspondiente, y finalmente leer el bloque de datos físico.

> [!question]- ¿Qué ventaja ofrece el esquema multinivel de Unix frente a un esquema puramente enlazado de bloques de índices?
> El esquema multinivel minimiza drásticamente la cantidad de bloques de índices asignados para archivos pequeños o medianos y permite un acceso directo rápido calculando el nivel de indirección aritméticamente, a diferencia del recorrido secuencial en esquemas enlazados.

