---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - so/almacenamiento
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)|02 - Discos duros magnéticos (HDD) y discos de estado sólido (SSD)]]"
---

# Niveles de formateo y esquemas de particionamiento (MBR y GPT)

Un disco recién fabricado es solo una superficie capaz de guardar bits. **Formatear** es dejar la memoria secundaria en un formato listo para usarse, y se hace en **tres niveles**, cada uno sobre el anterior: primero sectores físicos, después particiones y al final un sistema de archivos.

```mermaid
flowchart LR
  A["Bajo nivel: sectores con header, data y trailer"] --> B["Particionamiento: MBR o GPT"]
  B --> C["Formateo lógico: sistema de archivos en cada partición"]
```

## 1. Formateo de bajo nivel

Crea la **estructura de los sectores**: cada uno queda como **header + data + trailer**.

- **Header:** información para ubicar el sector (su número, entre otros datos).
- **Data:** los datos útiles (por ejemplo, 512 bytes).
- **Trailer:** incluye un código de corrección de errores (**ECC**), que permite detectar y corregir errores al leer el sector.

Se ejecuta **en fábrica**. Hacer un *low-level formatting* equivale a regresar el disco a sus valores de fábrica.

## 2. Particionamiento

Permite tener **varias particiones**: agrupaciones de sectores que el sistema **trata como discos separados**. Hay un espacio para administrar las particiones (la tabla de particiones) y luego las particiones mismas, que funcionan como unidades independientes; por ejemplo, para instalar un SO alternativo en otra partición.

| | **MBR** (*Master Boot Record*) | **GPT** (*GUID Partition Table*) |
|---|---|---|
| Uso | Sistemas antiguos (BIOS) | Sistemas modernos (UEFI) |
| Dónde está la tabla | En el primer sector del disco (512 B), junto al código de arranque | En los primeros sectores, con una **copia de respaldo al final** del disco |
| Direccionamiento | **32 bits** para direccionar bloques de 512 B | 64 bits |
| Tamaño máximo de disco | $2^{32} \times 512\text{ B} = 2$ TiB | Prácticamente sin límite actual |
| Particiones | 4 primarias | Muchas más (128 por defecto), aunque sigue habiendo un límite |

El sector del MBR reparte sus 512 bytes en 446 de código de arranque, 64 de tabla (4 entradas de 16) y 2 de firma (`0x55AA`). El límite viene directo de sus 32 bits: las direcciones de bloque (LBA, *logical block address*) no pueden nombrar más de $2^{32}$ bloques de 512 bytes. GPT, además, protege su tabla con sumas de verificación (CRC32) y con la copia del final, de modo que si una se corrompe, se recupera de la otra. La relación con el arranque se ve en [[06 - Arranque del sistema computacional|arranque del sistema]].

## 3. Formateo lógico

Es el que **crea el sistema de archivos** en una partición: divide la partición en **bloques** y le da a cada uno una interpretación. Por ejemplo, un bloque guarda un directorio, otro el contenido de un archivo, otro los metadatos. Distintos sistemas de archivos (FAT, ext4, NTFS, APFS) organizan esos bloques de forma distinta. Así nacen, entre otras, las estructuras que se ven en [[05 - Concepto de archivo, atributos y metadatos|archivos y metadatos]] y en la implementación de bloques e inodos.

> [!tip] Para recordar
> **Bajo nivel → sectores** (en fábrica). **Particionamiento → discos lógicos** (MBR/GPT). **Lógico → sistema de archivos** (bloques con significado).

## Preguntas de repaso

> [!question]- ¿Qué estructura deja el formateo de bajo nivel en cada sector?
> Header + data + trailer: la cabecera con información del sector, los datos útiles y un trailer con el código de corrección de errores (ECC).

> [!question]- ¿Por qué MBR no puede manejar discos de más de 2 TiB?
> Porque usa 32 bits para direccionar bloques de 512 bytes: a lo más $2^{32}$ bloques, es decir, $2^{32} \times 512\text{ B} = 2$ TiB.

> [!question]- ¿Qué ventajas tiene GPT sobre MBR?
> Direcciona con 64 bits, así que admite discos muchísimo más grandes. Permite muchas más particiones. Y guarda una copia de respaldo de la tabla al final del disco, con sumas de verificación para detectar corrupción.

> [!question]- ¿Qué hace el formateo lógico?
> Crea el sistema de archivos en una partición: divide el espacio en bloques y define qué representa cada uno (directorios, archivos, metadatos, espacio libre).
