---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/04 - Estructuras en disco y en memoria del sistema de archivos virtual (VFS)|04 - Estructuras en disco y en memoria del sistema de archivos virtual (VFS)]]"
---

# Métodos de asignación de bloques: asignación contigua y bloques de control

Cada archivo necesita bloques de disco, y cómo se eligen esos bloques determina qué tan rápido se puede leer el archivo. Una mala asignación provoca demoras en los tiempos de acceso. Esta nota presenta qué bloques necesita un archivo y la estrategia más simple: la **asignación contigua**.

## Un archivo no es solo sus datos

Un archivo ocupa más que los bytes de su contenido. Tiene un **tamaño real** (sus bytes) y un **tamaño en disco** (los bloques que ocupa), y además necesita metadatos:

| Tipo de bloque | Para qué sirve |
|---|---|
| **Bloques de datos** | Los bytes que son, en sí, el archivo |
| **Bloque de directorio** | Asocia el nombre del archivo con su información |
| **File Control Block** (FCB) | Contiene la información para poder leer los datos del archivo: metadatos y dónde están sus bloques |
| **Bloques índice** y **de indirección** (simple, doble) | En algunas estrategias, guardan las direcciones de los bloques de datos ([[07 - Asignación indexada y arquitectura de inodos multinivel en Unix|asignación indexada]]) |

Para leer un archivo, el SO recorre varias estructuras: consulta la **tabla de archivos del proceso**, luego la **tabla de archivos del sistema**, luego el **v-node** para saber qué función `read` usar según el sistema de archivos, y recién entonces lee los **bloques de datos** (ver [[04 - Estructuras en disco y en memoria del sistema de archivos virtual (VFS)|VFS]]). La idea de cada estrategia de asignación es no tener que dar tantas vueltas para encontrar los bloques, y cada SO tiene la suya.

## Asignación contigua

Los **bloques de datos de cada archivo se guardan de forma contigua**: un archivo de $n$ bloques que empieza en el bloque $b$ ocupa $b, b+1, \dots, b+n-1$. El directorio solo necesita guardar el **inicio** y el **largo**.

![Asignación contigua de bloques de disco](adjuntos/Asignaci%C3%B3n%20contigua%20de%20bloques%20de%20disco.png)

> [!example]- Transcripción de la imagen
> "Asignación contigua. Archivo de n bloques: b, b+1, …, b+n−1. Fácil de acceder a siguiente bloque. Problema: fragmentación externa. Require operaciones de compactación (defragmentación)." Un disco con bloques 0 a 31 y la tabla *directory* (*file / start / length*): *count* 0 2, *tr* 14 3, *mail* 19 6, *list* 28 4, *f* 6 2.

| Ventajas | Desventajas |
|---|---|
| **Muy sencilla** de almacenar y leer | **Fragmentación externa**: quedan huecos entre archivos, como con la memoria contigua |
| **Fácil acceder al siguiente bloque**, y al bloque $k$ directamente: $b + k$ | Hay que saber el tamaño al crear el archivo, y crecer es difícil si el bloque siguiente está ocupado |
| Lectura secuencial rapidísima en un HDD (casi sin *seek*) | Arreglarlo requiere **compactar** (desfragmentar), lo que es costoso y se quiere evitar |

```python
DIRECTORIO = {"count": (0, 2), "tr": (14, 3), "mail": (19, 6), "list": (28, 4), "f": (6, 2)}  # (inicio, largo)

def bloque_fisico(archivo, k):
    inicio, largo = DIRECTORIO[archivo]
    if not 0 <= k < largo:
        raise IndexError("bloque fuera del archivo")
    return inicio + k                                # acceso directo: b + k

print(bloque_fisico("mail", 3))                      # 22
```

Con la tabla de la figura, en los 32 bloques quedan **15 libres**, repartidos en huecos de 4, 6, 2 y 3 bloques. Un archivo de **7 bloques no cabe**, aunque sobre espacio: eso es la fragmentación externa.

## Preguntas de repaso

> [!question]- ¿Qué guarda el directorio para un archivo con asignación contigua?
> El bloque de inicio y el largo, en bloques. Con eso se puede calcular la ubicación de cualquier bloque del archivo.

> [!question]- ¿Dónde está el bloque 3 del archivo `mail` de la figura?
> `mail` empieza en el bloque 19, así que su bloque 3 está en $19 + 3 = 22$.

> [!question]- ¿Cuál es el problema principal de la asignación contigua?
> La fragmentación externa: entre archivos quedan huecos que, sumados, alcanzarían para un archivo nuevo, pero ninguno basta por sí solo. Resolverlo exige compactar, lo que es costoso.

> [!question]- ¿Qué es el File Control Block?
> El bloque con la información necesaria para leer un archivo: sus metadatos y la ubicación de sus bloques de datos. En UNIX corresponde al inodo.
