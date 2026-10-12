---
ramo: "Sistemas Operativos y Redes"
tema: "Sistemas de archivos"
tags:
  - so/archivos
  - origen/apuntes
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/10-Sistemas de archivos/05 - Concepto de archivo, atributos y metadatos\|05 - Concepto de archivo, atributos y metadatos]]"
---

# Estructura de directorios y resolución de rutas

Los directorios organizan los archivos del sistema en una estructura jerárquica de árbol, funcionando internamente como tablas de correspondencia entre nombres legibles y números de inodo.

## Directorios y rutas (mis apuntes)

- DIRECTORIOS
- Contenedores de archivos o otro directorios (de manera de alto nivel (para usuarios))
- Lista de pares (nombre leible, low-level nombre)
- Jerarquia empieza con : (la raiz): “/”
- Usa separador /
- Unidades son Subdirectorios
- Otros directiors : Jerarqui o arboles de directorios
- Puede contener:
- Rutas absolutas : Partencon desde la raiz (con / ) → UNICAS
- v/s Rutas relativas: Parten desde el directorio donde nos encontremos

> [!warning] Posible error
> En los apuntes aparecen erratas en `directiors` (directorios), `Jerarqui` (jerarquía) y `Partencon` (parten con).

> [!tip] Complemento: Implementación de directorios y resolución de rutas
> 1. **Estructura interna de un directorio:**
>    - En sistemas tipo Unix, un directorio es un archivo cuyo contenido es gestionado exclusivamente por el kernel.
>    - Consiste en una lista de entradas de directorio (*dentries*), donde cada entrada vincula:
>      $$\text{Entrada} = (\text{nombre legible por el usuario}, \text{número de inodo})$$
>    - Todo directorio contiene siempre dos entradas iniciales obligatorias:
>      - `.` : apunta al inodo del directorio actual.
>      - `..` : apunta al inodo del directorio padre (en la raíz `/`, tanto `.` como `..` apuntan al mismo inodo raíz, típicamente el inodo 2 en ext4).
> 2. **Tipos de rutas y resolución por el kernel:**
>    - **Ruta absoluta:** comienza con `/` (raíz). Identifica un único nodo en el árbol de forma absoluta e independiente del estado de ejecución del proceso (p. ej. `/home/user/documentos/archivo.txt`).
>    - **Ruta relativa:** no comienza con `/`. Su resolución depende del directorio de trabajo actual (*Current Working Directory* o CWD) almacenado en el bloque de control del proceso (PCB).
> 3. **Proceso de resolución de nombres (*Path traversal*):**
>    - El kernel lee el inodo raíz, busca en su bloque de datos la entrada del primer componente de la ruta, obtiene su inodo, verifica permisos de ejecución (`+x`), y repite recursivamente hasta alcanzar el archivo o subdirectorio final.

## Preguntas de repaso

> [!question]- ¿Por qué un proceso requiere permiso de ejecución (`x`) y no solo de lectura (`r`) sobre un directorio para acceder a sus archivos?
> Porque el permiso de lectura (`r`) solo autoriza a listar los nombres de los archivos contenidos en el directorio (con `ls`). El permiso de ejecución (`x`) autoriza al kernel a atravesar (*traverse*) el directorio y resolver sus nombres de inodo para abrir o acceder a los archivos internos.

> [!question]- ¿Qué representan las entradas especiales `.` y `..` y a qué apuntan en el directorio raíz `/`?
> Representan el directorio actual (`.`) y el directorio contenedor padre (`..`). En el directorio raíz `/`, dado que no existe un contenedor superior, ambas entradas apuntan al mismo inodo raíz.

> [!question]- ¿Dónde reside físicamente el nombre de un archivo en un sistema de archivos Unix?
> El nombre reside en los bloques de datos del directorio que lo contiene, emparejado con su número de inodo. El inodo del archivo en sí mismo no almacena su nombre legible.

