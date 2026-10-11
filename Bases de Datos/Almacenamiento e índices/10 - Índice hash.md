---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/indices, origen/complemento]
prerrequisitos: ["[[08 - Tablas de hash|Tablas de hash]]", "[[09 - Índices en bases de datos|Índices en bases de datos]]"]
---
# Índice hash

Un índice hash es una tabla de hash en disco: cada casillero es una **página**, con páginas de *overflow* encadenadas si se llena. Encuentra un valor exacto en ~1 I/O, pero **no sirve para rangos**.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 9: Almacenamiento y Índices")
> La idea es replicar las tablas de hash en una base de datos. Ahora **los casilleros son páginas del disco**, y en cada página caben muchas tuplas. Objetivo: resolver consultas de igualdad (`SELECT * FROM Artistas A WHERE A.aid = 12`) con la menor cantidad de I/O.
>
> **Estructura**, para una relación R y un atributo A:
> - N páginas de disco sirven de buckets.
> - Cada bucket tiene una **lista ligada de overflow pages**.
> - Una función de hash $h: dominio(A) \to [0, \dots, N-1]$ indica a qué bucket va cada valor.
>
> ![Slide - hash index con overflow page](adjuntos/Slide%20-%20hash%20index%20con%20overflow%20page.png)

> [!note]- Transcripción de la imagen
> Hash Index, ejemplo con 5 buckets: 0 → (5, Bernini) · 1 → (1, Leonardo), (11, Brunelleschi) → **overflow page** con (16, Giotto) · 2 → (12, Botticelli) · 3 → (8, Michelangelo) · 4 → vacío. El bucket 1 se llenó (caben 2 tuplas por página), así que Giotto ($16 \bmod 5 = 1$) va a una página de overflow.

> [!tip] Complemento — costo (slides "Clase 9")
> **Buscar** una search key k:
> 1. Calcular $h(k)$: costo $O(1)$, en RAM.
> 2. Acceder al bucket correspondiente.
> 3. Buscar el elemento en esa página o en sus overflow pages.
>
> - **Caso ideal:** 1 I/O (la página del bucket). En la slide aparece "costo 0" si el directorio ya está en memoria y solo se cuenta el overhead del índice.
> - **Peor caso:** $O(\lceil |R|/B \rceil)$, cuando **todo va a un casillero** y hay que recorrer toda la cadena de overflow.
>
> **¿Cuándo no conviene?** Con rangos: `SELECT * FROM Artistas A WHERE A.aid > 12`. El hash desordena los valores, así que no hay forma de saber en qué buckets están los mayores que 12: hay que revisarlos todos.

## Preguntas de repaso

1. ¿Qué son los buckets en un índice hash de una base de datos?
> [!question]- Respuesta
> Páginas de disco. Cada una guarda las tuplas (o punteros) cuyas llaves caen en ese casillero según la función de hash.

2. ¿Qué es una overflow page?
> [!question]- Respuesta
> Una página adicional, encadenada al bucket, que se usa cuando el bucket se llena.

3. ¿Cuál es el costo de buscar una igualdad en el mejor y en el peor caso?
> [!question]- Respuesta
> En el mejor caso, ~1 I/O (la página del bucket). En el peor, si todo cae en el mismo bucket, $\lceil |R|/B \rceil$, como recorrer la tabla.

4. ¿Por qué un índice hash no sirve para `WHERE aid > 12`?
> [!question]- Respuesta
> Porque la función de hash no preserva el orden: los valores mayores que 12 están repartidos en cualquier bucket.
