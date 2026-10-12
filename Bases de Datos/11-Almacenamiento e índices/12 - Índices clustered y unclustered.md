---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/indices, origen/complemento]
prerrequisitos: ["[[10 - Índice hash|Índice hash]]", "[[11 - Índice árbol B+|Índice árbol B+]]"]
---
# Índices clustered y unclustered

Un índice **clustered** (primario) guarda o devuelve **la tupla misma**, con los datos ordenados u organizados según el índice. Uno **unclustered** (secundario) devuelve un **puntero** a la página donde está la tupla, así que cuesta un I/O extra por cada tupla.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 9: Almacenamiento y Índices")
> Un índice puede retornar la tupla buscada o un puntero (o lista de punteros) a las páginas del disco que la tienen.
> | | Clustered | Unclustered |
> |---|---|---|
> | Data entry | la tupla misma | puntero a la página con la tupla |
> | También llamado | índice **primario** | índice **secundario** |
> | Típicamente sobre | la primary key (`id` de Empleados) | otro atributo (`edad`, para ordenar más rápido por edad) |
> | Cuántos por tabla | uno (los datos se ordenan de una sola forma) | varios |
>
> **Costos de los ejemplos de la clase** (R(a,b,c), índice sobre a):
> | Búsqueda | Hash clustered | Hash unclustered | B+ clustered | B+ unclustered |
> |---|---|---|---|---|
> | `a = 5` | **1** (el bucket es la página con la tupla) | **2** (bucket + página de datos) | **h** (los datos están en las hojas) | **h + 1** |
> | `a > 5` | — (no sirve) | — | $h + B_m$ (páginas con tuplas que calzan) | $h + n/P + n$ (un I/O por cada tupla) |
>
> donde n es el número de tuplas que calzan y P la cantidad de punteros por página. Como un puntero (8 bytes) es mucho más chico que una tupla (~160 bytes), en una página caben más punteros que tuplas: $P > B$.

> [!example] Ejemplo extra — ejercicio de la clase
> R(a, b, c) con 1M de tuplas, `a` uniforme en [0, 1.000.000] y llave, B+ tree **unclustered** de altura h, P > B punteros por página (hojas al 100%).
>
> `SELECT * FROM R WHERE a < 21`:
> 1. Bajar hasta a = 21 → **h**.
> 2. Por uniformidad, hay 21 tuplas que calzan, con 21 punteros. Recorrer las hojas hacia la izquierda → **21/P − 1** páginas más.
> 3. Unclustered: por cada puntero hay que traer la página de la tupla → **21**.
>
> **Costo = h + (21/P − 1) + 21.** Con un índice clustered serían solo $h + \lceil 21/B \rceil$, porque las 21 tuplas están juntas.
>
> Por eso, para rangos grandes con un índice unclustered, a veces conviene más **recorrer la tabla** que usar el índice. El optimizador lo decide.

## Preguntas de repaso

1. ¿Qué diferencia a un índice clustered de uno unclustered?
> [!question]- Respuesta
> El clustered devuelve (y almacena en orden) la tupla misma. El unclustered devuelve un puntero a la página donde está la tupla.

2. ¿Por qué una búsqueda `a = 5` cuesta 1 en un hash clustered y 2 en uno unclustered?
> [!question]- Respuesta
> En el clustered, la página del bucket tiene la tupla. En el unclustered, el bucket solo tiene el puntero y hace falta otro I/O para traer la página de datos.

3. ¿Cuánto cuesta `a < 21` con un B+ unclustered sobre 1M tuplas uniformes?
> [!question]- Respuesta
> h + (21/P − 1) + 21: bajar el árbol, recorrer las hojas con los 21 punteros y un I/O por cada tupla.

4. ¿Cuántos índices clustered puede tener una tabla?
> [!question]- Respuesta
> Uno, porque los datos físicos solo se pueden ordenar de una forma. Los secundarios (unclustered) pueden ser varios.
