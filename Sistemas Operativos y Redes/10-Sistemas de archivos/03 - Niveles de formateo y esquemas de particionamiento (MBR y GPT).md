---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - so/almacenamiento
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)\|02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)]]"
---

# Niveles de formateo y esquemas de particionamiento (MBR y GPT)

Para que un dispositivo de almacenamiento secundario pueda ser utilizado por el sistema operativo, debe atravesar tres niveles sucesivos de estructuración: formateo de bajo nivel, particionamiento y formateo lógico.

## Niveles de formateo y particionamiento (mis apuntes)

- FORMATEO
- Dejar la memoria secundaria en un formato listo para hacer algo
- Podemos hacer formateos a distintos niveles
- FORMATEO BAJO NIVEL
- Formateo de fabrica : ESTRUCTURA : header + data + trailer
- PARTICIONAMIENTO
- Formateo que permite tener varias particiones
- Un espacio para administrar las particiones, y luego las particiones, donde se pueden hacer unidades independientes por ejemplo, instalar un S.O alternativo, etc
- Sistemas antiguos utilizan MBR (master boot record)
- Sistemas modernos usan GPT (Guide partition table)
- → Permite tener una cantidad mayor de particiones (sigue siendo limitada)
- FORMATEO LOGICO
- El que se encarga de hacer el sistema de archivos
- Divido memoria en bloques, y a cada uno le doy una interpretacion
- Por ejemplo, un bloque es un directorio, otro es un archivo, etc

> [!warning] Posible error
> En los apuntes se menciona `GPT (Guide partition table)`. El acrónimo estándar de la industria es **GUID Partition Table** (tabla de particiones basada en identificadores únicos globales, *Globally Unique Identifier*).

> [!tip] Complemento: Las tres fases de preparación del almacenamiento
> 1. **Formateo de bajo nivel (*Low-level formatting* o físico):**
>    - Realizado típicamente en fábrica por el fabricante del disco.
>    - Escribe en la superficie magnética la estructura básica de los sectores:
>      - **Header:** número de sector, número de cilindro y bandera de sincronización.
>      - **Data:** área útil de carga (típicamente $512\text{ B}$ o $4096\text{ B}$).
>      - **Trailer:** código de redundancia cíclica o de corrección de errores (ECC, *Error-Correcting Code*).
> 2. **Particionamiento de disco:**
>    - Divide el almacenamiento físico en una o más regiones lógicas tratadas como unidades independientes por el kernel.
>    - **MBR (*Master Boot Record*):**
>      - Ubicado en el sector 0 del disco ($512\text{ bytes}$).
>      - Contiene el cargador de arranque primario ($446\text{ B}$), la tabla de 4 particiones primarias ($64\text{ B}$) y la firma mágica `0x55AA` ($2\text{ B}$).
>      - Límite de direccionamiento: campos LBA de 32 bits, lo que restringe el tamaño máximo del disco a $2^{32} \times 512\text{ B} = 2\text{ TB}$.
>    - **GPT (*GUID Partition Table*):**
>      - Estándar de la arquitectura UEFI. Direccionamiento LBA de 64 bits (capacidad de hasta $9.4\text{ ZB}$).
>      - Soporta hasta 128 particiones primarias en Windows/Linux por omisión.
>      - Incluye redundancia mediante una copia de respaldo de la cabecera y tabla de particiones al final físico del disco, verificadas con CRC32.
> 3. **Formateo lógico (*High-level formatting* o creación de FS):**
>    - Crea las estructuras de datos del sistema de archivos en una partición dada (p. ej., ext4, NTFS, APFS).
>    - Inicializa el superbloque, las tablas de inodos o tablas de asignación (FAT), mapas de bits de espacio libre y el directorio raíz (`/`).

## Preguntas de repaso

> [!question]- ¿Por qué el esquema de particionamiento MBR impone un límite de tamaño de disco de 2 TB para sectores de 512 bytes?
> Porque la tabla de particiones en el MBR reserva exactamente 32 bits para el número de sectores lógicos direccionables ($2^{32}$ sectores). Multiplicado por $512\text{ bytes/sector}$, la capacidad máxima direccionable es $2^{32} \times 512\text{ B} = 2\text{ TiB}$.

> [!question]- ¿Qué información crucial contiene el trailer de un sector físico en un disco formateado a bajo nivel?
> Contiene el código de corrección de errores (ECC). Cuando la cabeza lee el sector, el controlador calcula el ECC de los datos leídos; si difiere del trailer, detecta y corrige automáticamente errores de lectura menores sin involucrar al sistema operativo.

> [!question]- ¿Qué ventaja de fiabilidad ofrece GPT frente a MBR ante fallas o corrupción de sectores?
> GPT almacena una copia íntegra de respaldo de su cabecera y tabla de particiones en los últimos sectores físicos del disco y utiliza sumas de verificación CRC32 para detectar corrupción y auto-reparar la tabla desde la réplica.

