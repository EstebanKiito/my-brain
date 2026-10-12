---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/inodos
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/06 - Asignación enlazada y tabla de asignación de archivos (FAT)\|06 - Asignación enlazada y tabla de asignación de archivos (FAT)]]"
---

# Asignación indexada y arquitectura de inodos multinivel en Unix

La [[06 - Asignación enlazada y tabla de asignación de archivos (FAT)|asignación enlazada]] obliga a recorrer la cadena para llegar a un bloque. La **asignación indexada** reúne todos los punteros de un archivo en un solo lugar, un **bloque de índices**, que funciona como una tabla: para llegar al bloque $k$ basta mirar la posición $k$. Es la misma idea que las [[06 - Paginación multinivel y tablas de páginas invertidas|tablas de páginas]], aplicada a archivos.

## Asignación indexada

**Cada archivo tiene su propio bloque de índices** (*index block*), y cada entrada de ese bloque apunta a un **bloque de datos**.

![Asignación indexada con bloque de índices](adjuntos/Asignaci%C3%B3n%20indexada%20con%20bloque%20de%20%C3%ADndices.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano: un bloque marcado **BI** (bloque de índices) con varias entradas, de las que salen flechas a tres bloques de datos.

- ✅ **Acceso aleatorio** directo y **sin fragmentación externa**.
- ❌ **Se pierde espacio** por el bloque de índices: los bloques tienen tamaño fijo, así que un archivo pequeño (por ejemplo, de menos de 4 KB) usa un bloque de índices casi vacío, con todas las entradas menos una sin usar.

## ¿Y si el archivo no cabe en un bloque de índices?

Con bloques de 4 KB y punteros de 32 bits, un bloque de índices tiene **1024 punteros**. Para archivos más grandes hay tres opciones:

| Esquema | Idea |
|---|---|
| **Enlazado** | La última entrada del bloque de índices apunta a otro bloque de índices. No es muy útil: vuelve el recorrido secuencial |
| **Índice multinivel** | Como una tabla de páginas multinivel: un bloque de índices apunta a otros bloques de índices, que apuntan a los datos. Con dos niveles, $1024 \times 1024 = 1\,048\,576$ bloques, es decir **4 GB** |
| **Combinado** | Los primeros $p$ punteros apuntan directo a datos, los siguientes a un bloque de índices simple, luego a uno doble, etc. Es el que usa UNIX |

![Estructura de direccionamiento indirecto en inodos](adjuntos/Estructura%20de%20direccionamiento%20indirecto%20en%20inodos.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano de un índice de dos niveles: un bloque de índices cuyas entradas apuntan a otros bloques de índices, que a su vez apuntan a bloques de datos ("etc").

## El inodo de UNIX: esquema combinado

![Asignación combinada multinivel e inodos Unix](adjuntos/Asignaci%C3%B3n%20combinada%20multinivel%20e%20inodos%20Unix.png)

> [!example]- Transcripción de la imagen
> Un inodo con los campos *mode*, *owners (2)*, *timestamps (3)*, *size block count*, luego *direct blocks* (cada uno apunta a un bloque *data*), *single indirect* (apunta a un bloque de punteros a *data*), *double indirect* (a un bloque de punteros a bloques de punteros a *data*) y *triple indirect*.

En los sistemas tipo ext2/ext3, con bloques de 4 KB y punteros de 4 bytes (1024 por bloque):

| Punteros | Bloques que alcanzan | Tamaño |
|---|---|---|
| 12 directos | 12 | 48 KB |
| Indirecto simple: bloque de indirección → bloque índice → datos | $1024$ | 4 MB |
| Indirecto doble | $1024^2$ | 4 GB |
| Indirecto triple | $1024^3$ | 4 TB |

Así, un archivo pequeño se lee con los punteros directos, sin bloques extra, y solo los archivos grandes pagan los niveles de indirección.

```python
BLOQUE, PUNTERO, DIRECTOS = 4096, 4, 12
P = BLOQUE // PUNTERO                          # punteros por bloque índice: 1024
niveles = [DIRECTOS, P, P ** 2, P ** 3]        # directos, simple, doble, triple
print(sum(niveles) * BLOQUE / 2**40, "TiB")    # ≈ 4.0
```

## Preguntas de repaso

> [!question]- ¿Qué ventaja tiene la asignación indexada sobre la enlazada?
> Permite acceso aleatorio directo: la posición $k$ del bloque de índices dice dónde está el bloque $k$, sin recorrer los anteriores. Además, no tiene fragmentación externa.

> [!question]- ¿Cuál es el costo de la asignación indexada para archivos pequeños?
> Cada archivo necesita un bloque de índices completo, aunque use una sola entrada. Ese espacio se pierde.

> [!question]- Con bloques de 4 KB y punteros de 32 bits, ¿cuántos bloques direcciona un índice de dos niveles y qué tamaño es?
> Cada bloque tiene 1024 punteros: $1024 \times 1024 = 1\,048\,576$ bloques de 4 KB, es decir, 4 GB.

> [!question]- ¿Por qué el inodo de UNIX tiene punteros directos además de los indirectos?
> Porque la mayoría de los archivos son pequeños: con los punteros directos se leen sin pasar por bloques de índices, y solo los archivos grandes usan los indirectos.
