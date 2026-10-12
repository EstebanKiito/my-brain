---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/fat
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/05 - Métodos de asignación de bloques: asignación contigua y bloques de control\|05 - Métodos de asignación de bloques: asignación contigua y bloques de control]]"
---

# Asignación enlazada y tabla de asignación de archivos (FAT)

La [[05 - Métodos de asignación de bloques: asignación contigua y bloques de control|asignación contigua]] sufre fragmentación externa porque exige bloques seguidos. La **asignación enlazada** elimina ese requisito: los bloques de un archivo pueden estar en cualquier parte, y cada uno indica cuál es el siguiente, como una lista ligada. La **FAT** mejora la idea sacando esos punteros a una tabla.

## Asignación enlazada (*linked*)

Cada bloque guarda **un puntero al bloque siguiente**: la mayor parte del bloque es útil para los datos del archivo y una pequeña parte apunta al siguiente. El directorio guarda dónde empieza (y dónde termina) la cadena.

![Asignación enlazada de bloques de archivo](adjuntos/Asignaci%C3%B3n%20enlazada%20de%20bloques%20de%20archivo.png)

> [!example]- Transcripción de la imagen
> Un disco con bloques 0 a 31 y la tabla *directory* (*file / start / end*): *jeep* empieza en 9 y termina en 25. Flechas encadenan los bloques del archivo: 9 → 16 → 1 → 10 → 25, repartidos por todo el disco.

| Ventajas | Desventajas |
|---|---|
| No necesita saber el tamaño inicial: **el archivo puede crecer** tomando cualquier bloque libre | **Acceso solo secuencial**: para leer algo al final del archivo hay que recorrer todos los bloques anteriores, $O(n)$ |
| No hay fragmentación externa | **Se pierde espacio** en cada bloque: de 512 bytes, solo 508 quedan para datos |
| | **Vulnerable**: si falla un bloque, se pierde el resto de la cadena |

Agrupar bloques en *clusters* reduce el espacio perdido en punteros, a cambio de más fragmentación interna. Una lista doblemente enlazada no resuelve el problema: buscar algo en el medio sigue exigiendo recorrer.

## FAT (*File Allocation Table*)

En vez de guardar el puntero dentro de cada bloque de datos, **todos los punteros se guardan en una tabla** al inicio del disco: la entrada $i$ dice cuál es el bloque siguiente al bloque $i$, y el último bloque del archivo se marca con **EOF**. Para seguir la cadena, solo hay que consultar la tabla.

![Asignación enlazada mediante tabla FAT](adjuntos/Asignaci%C3%B3n%20enlazada%20mediante%20tabla%20FAT.png)

> [!example]- Transcripción de la imagen
> *directory entry*: nombre *test*, … , *start block* 217. En la tabla **FAT** (filas 0 a *number of disk blocks* − 1): la entrada 217 contiene 618, la entrada 618 contiene 339 y la entrada 339 marca el fin. La cadena del archivo es 217 → 618 → 339.

```python
EOF_ = -1
FAT = {217: 618, 618: 339, 339: EOF_}        # índice = bloque, valor = bloque siguiente
DIRECTORIO = {"test": 217}                    # el directorio solo guarda el bloque inicial

def bloques(archivo):
    b, cadena = DIRECTORIO[archivo], []
    while b != EOF_:
        cadena.append(b)
        b = FAT[b]                            # se recorre la tabla, no los bloques del disco
    return cadena

print(bloques("test"))   # [217, 618, 339]
```

- **Mejor acceso aleatorio**: la cadena se sigue en la tabla, que se puede tener en memoria, sin leer cada bloque de datos del disco.
- **Limitado por el tamaño de la tabla**: en FAT32, un archivo puede medir a lo más **4 GB** ($2^{32}$ bytes).

> [!tip] Para recordar
> **Enlazada:** el puntero va *dentro* del bloque, y hay que leer el disco bloque a bloque. **FAT:** el puntero va *en una tabla*, y se recorre la tabla.

## Preguntas de repaso

> [!question]- ¿Por qué la asignación enlazada no sufre fragmentación externa?
> Porque los bloques de un archivo no necesitan estar contiguos: cualquier bloque libre puede agregarse a la cadena.

> [!question]- ¿Por qué leer el final de un archivo enlazado es lento?
> Porque cada bloque solo sabe cuál es el siguiente: para llegar al bloque $k$ hay que leer los $k$ anteriores, en orden.

> [!question]- ¿Qué mejora la FAT respecto de la asignación enlazada pura?
> Saca los punteros de los bloques de datos y los reúne en una tabla. Así la cadena se recorre en la tabla (que puede estar en memoria) y no leyendo cada bloque del disco, lo que mejora el acceso aleatorio.

> [!question]- Con la FAT de la figura, ¿qué bloques ocupa el archivo `test`?
> Empieza en 217; la tabla dice 217 → 618 → 339 y luego EOF. Ocupa los bloques 217, 618 y 339.
