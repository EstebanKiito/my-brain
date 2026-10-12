---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/indices, origen/complemento]
prerrequisitos: ["[[10 - Índice hash|Índice hash]]", "[[11 - Índice árbol B+|Índice árbol B+]]"]
---
# Índice hash vs árbol B+

Cuándo conviene cada índice: el **hash** es levemente mejor para igualdades exactas; el **árbol B+** es mucho mejor para rangos y orden, y por eso es el más popular (el default de PostgreSQL).

> [!tip] Complemento — nota nueva (fuente: slides "Clase 9: Almacenamiento y Índices")
> ![Slide - hash vs árbol B+](adjuntos/Slide%20-%20hash%20vs%20árbol%20B+.png)
>
> | Criterio | Hash | Árbol B+ |
> |---|---|---|
> | Búsqueda exacta (`=`) | **levemente más eficiente**, con una función de hash ideal (~1 I/O) | altura h (~2–4 I/O) |
> | Búsqueda por rango (`<`, `>`, `BETWEEN`) | no sirve | **mucho más eficiente** (hojas encadenadas) |
> | `ORDER BY`, `MIN`/`MAX` | no ayuda | sí (orden de las hojas) |
> | Popularidad | menos usado | **más popular** |
>
> En PostgreSQL: `CREATE INDEX … USING btree` (por defecto) o `USING hash`.

> [!note]- Transcripción de la imagen
> **Índices: Hash vs. Árbol B+.** A la izquierda, un hash con la llave k que pasa por h(k) hacia los *primary buckets* 0…N−1, con *overflow pages*: "Levemente más eficiente para búsquedas exactas asumiendo una función de hash ideal". A la derecha, un árbol con *directorios* arriba y *datos* en hojas encadenadas: "Mucho más eficiente para búsquedas por rango" y "Árbol B+ es más popular".

## Preguntas de repaso

1. ¿Cuándo elegirías un índice hash sobre un árbol B+?
> [!question]- Respuesta
> Cuando la columna se consulta solo por igualdad exacta y se quiere el mínimo de I/O.

2. ¿Por qué el árbol B+ es más popular?
> [!question]- Respuesta
> Porque sirve para igualdades con costo bajo (altura pequeña) y además para rangos, ordenamiento y prefijos, que el hash no soporta.

3. ¿Qué índice usa PostgreSQL por defecto?
> [!question]- Respuesta
> Un árbol B (btree).
