---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/06 - Estructura de directorios y resolución de rutas|06 - Estructura de directorios y resolución de rutas]]"
---

# Montaje de sistemas de archivos y puntos de montaje

Un computador puede tener varios discos y particiones, cada uno con su propio sistema de archivos: el disco interno con ext4, un pendrive con FAT32, un disco externo con NTFS. **Montar** es incorporar uno de esos dispositivos nuevos al árbol de directorios que ya se está usando, para acceder a sus archivos como a cualquier otro.

## Montar un sistema de archivos

El sistema puede manejar **múltiples sistemas de archivos** en distintos discos (dispositivos de bloques). Para acceder a uno se necesita un **punto de montaje** (*mountpoint*): un directorio del árbol actual donde el SO "cuelga" la raíz del sistema de archivos nuevo, usando `mount`.

```bash
mount /dev/sda1 /home/users     # el contenido de la partición sda1 aparece en /home/users
```

Por convención, los volúmenes que se montan a mano suelen ir bajo `/mnt`. Por ejemplo, al montar una memoria USB, sus archivos aparecen como si fueran una carpeta más.

![Montaje de sistemas de archivos y tabla de monturas](adjuntos/Montaje%20de%20sistemas%20de%20archivos%20y%20tabla%20de%20monturas.png)

> [!example]- Transcripción de la imagen
> A la izquierda, un árbol con raíz y los directorios *bin*, *dev*, *lib*, *mnt* y *usr*; *mnt* está marcado en rojo. A la derecha, el mismo árbol después de montar: bajo *mnt* aparece un subárbol completo. Trazos a mano marcan en rojo el árbol principal y una parte del subárbol, y en azul otra parte, para indicar que distintas zonas del árbol pertenecen a sistemas de archivos diferentes.

## Distintos sistemas de archivos en un mismo árbol

Cada dispositivo puede tener un sistema de archivos distinto:

| Sistema | Uso típico |
|---|---|
| **ext4** | Linux |
| **NTFS** | Windows |
| **FAT32** | Memorias USB, por su compatibilidad |

En la figura, la parte roja podría ser NTFS y la azul FAT32: el usuario ve un solo árbol, pero por debajo hay sistemas de archivos distintos. Por eso **el SO debe tener una tabla** (la **tabla de montajes**) que registre, para cada punto de montaje, qué dispositivo y qué sistema de archivos hay ahí, y así saber cómo atender cada acceso. La capa que permite tratar a todos por igual es el **VFS** (*virtual file system*), que se ve en [[04 - Estructuras en disco y en memoria del sistema de archivos virtual (VFS)|estructuras del sistema de archivos]].

> [!warning] Lo que había en el punto de montaje se oculta
> Si el directorio usado como punto de montaje ya tenía archivos, quedan **ocultos** mientras dure el montaje (no se borran). Al desmontar con `umount`, vuelven a aparecer.

## UNIX frente a Windows

- En **UNIX/Linux** hay un **único árbol** con raíz `/`: cada disco o partición se monta en algún directorio de ese árbol.
- En **Windows**, cada unidad tiene tradicionalmente su propia letra (`C:\`, `D:\`), con árboles separados.

## Preguntas de repaso

> [!question]- ¿Qué es un punto de montaje?
> Un directorio del árbol actual donde el SO integra la raíz de otro sistema de archivos, para que sus archivos se accedan como parte del mismo árbol.

> [!question]- ¿Por qué el SO necesita una tabla de montajes?
> Porque en un mismo árbol conviven sistemas de archivos distintos (ext4, NTFS, FAT32…). La tabla dice qué dispositivo y qué sistema de archivos hay en cada punto de montaje, para usar el código correcto en cada acceso.

> [!question]- ¿Qué pasa con los archivos que había en un directorio cuando se monta algo sobre él?
> Quedan ocultos mientras dure el montaje y reaparecen intactos al desmontar.

> [!question]- ¿Qué hace `mount /dev/sda1 /home/users`?
> Integra el sistema de archivos de la partición `/dev/sda1` en el directorio `/home/users`, de modo que su contenido aparece ahí.
