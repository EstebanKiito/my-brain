---
ramo: "Sistemas Operativos y Redes"
tema: "Implementación de archivos y bloques"
tags:
  - so/archivos
  - so/almacenamiento
  - origen/complemento
prerrequisitos:
  - "[[Sistemas Operativos y Redes/11-Implementación de archivos y bloques/07 - Asignación indexada y arquitectura de inodos multinivel en Unix\|07 - Asignación indexada y arquitectura de inodos multinivel en Unix]]"
---

# Administración del espacio libre en disco: mapas de bits y listas enlazadas

Cada vez que un archivo crece, el sistema de archivos necesita un bloque libre. ¿Cómo encontrarlo rápido sin revisar el disco entero? Hay dos estructuras clásicas para llevar la cuenta del **espacio libre**: el **bitmap** y la **lista enlazada**.

## Bitmap (*bit vector*)

Se usa **un bit por cada bloque** del disco, que indica si el bloque está libre u ocupado.

- ✅ **Sencillo, eficiente e implementable en hardware**: buscar un bloque libre es buscar un bit en un arreglo, y la CPU puede revisar palabras completas de 32 o 64 bits de una vez. También facilita encontrar bloques libres **contiguos**.
- ❌ **No escala tan bien**: el bitmap crece con el disco y conviene tenerlo en memoria.

![Gestión de espacio libre con mapa de bits o bitmap](adjuntos/Gesti%C3%B3n%20de%20espacio%20libre%20con%20mapa%20de%20bits%20o%20bitmap.png)

> [!example]- Transcripción de la imagen
> "¿Cómo encontrar bloques libres? **Bit vector** ó **bitmap** de bloques libres. + Sencillo, eficiente, e implementable en hardware. − No escala tan bien: disco de 1.3 GB, con bloques de 512 byte → 332 KB; disco de 1 TB, con bloques de 4 KB → 256 MB".

El tamaño del bitmap es $\dfrac{\text{tamaño del disco}}{\text{tamaño de bloque}}$ bits:

| Disco | Bloque | Bloques (= bits) | Bitmap |
|---|---|---|---|
| 1,3 GB | 512 B | ≈ 2,7 millones | ≈ **332 KB** |
| 1 TB | 4 KB | $2^{28}$ ≈ 268 millones | el material indica 256 MB; $2^{28}$ bits son **32 MB** |

```python
def primer_libre(bitmap):
    """bitmap[i] == 1 si el bloque i está libre."""
    for i, libre in enumerate(bitmap):
        if libre:
            return i
    return None

bitmap = [0, 0, 1, 1, 0, 1, 0, 0]          # bloques 2, 3 y 5 libres
print(primer_libre(bitmap))                # 2
print(2**40 // 4096 // 8 / 2**20, "MiB")   # bitmap de 1 TiB con bloques de 4 KiB: 32.0
```

## Lista enlazada de bloques libres

Otra estrategia: **cada bloque libre guarda un puntero al siguiente bloque libre**, y el sistema guarda dónde empieza la lista. Los bloques que se liberan se agregan a la lista.

- ✅ No necesita espacio extra: los punteros van dentro de los mismos bloques libres.
- ❌ **Poco eficiente**: recorrerla implica leer bloque por bloque del disco, y es difícil encontrar bloques contiguos.
- **Mejora: agrupar espacios contiguos**. En vez de un puntero por bloque, se guarda un puntero al inicio de cada grupo de bloques libres más el **número de bloques contiguos** del grupo.

![Gestión de espacio libre con lista enlazada de bloques](adjuntos/Gesti%C3%B3n%20de%20espacio%20libre%20con%20lista%20enlazada%20de%20bloques.png)

> [!example]- Transcripción de la imagen
> "Lista Enlazada: punteros a bloques libres; bloques nuevos se agregan a la lista; − poco eficiente; mejora: agrupar espacios contiguos; mantener punteros a espacios libres + número de espacios contiguos". Un disco con bloques 0 a 31; *free-space list head* apunta al bloque 2, y flechas encadenan los bloques libres: 2 → 3 → 4 → 5 → 8 → 9 → 10 → 11 → 12 → 13 → 17 → 18 → 25 → 26 → 27.

> [!tip] Para recordar
> **Bitmap:** 1 bit por bloque, rápido y con costo de memoria proporcional al disco. **Lista enlazada:** sin costo extra, pero lenta; mejor si se guardan grupos (inicio + cantidad).

## Preguntas de repaso

> [!question]- ¿Cómo representa el bitmap el espacio libre y por qué es eficiente?
> Con un bit por bloque que indica si está libre. Buscar un bloque libre es buscar un bit, y el hardware puede revisar muchos bits a la vez.

> [!question]- ¿Por qué se dice que el bitmap no escala tan bien?
> Porque su tamaño crece con el número de bloques del disco, y para que sea rápido conviene tenerlo en memoria. Un disco de 1,3 GB con bloques de 512 B ya necesita unos 332 KB de bitmap.

> [!question]- ¿Qué ventaja y qué desventaja tiene la lista enlazada de bloques libres?
> No usa espacio adicional, porque los punteros van dentro de los bloques libres, pero es poco eficiente: recorrerla requiere leer cada bloque y no sirve para encontrar bloques contiguos.

> [!question]- ¿En qué consiste la mejora de agrupar espacios contiguos?
> En guardar, para cada grupo de bloques libres seguidos, un puntero a su inicio y la cantidad de bloques, en vez de un puntero por cada bloque.
