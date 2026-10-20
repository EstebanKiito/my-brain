---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/almacenamiento, bd/costos, origen/apuntes]
prerrequisitos: ["[[03 - Disco, RAM y buffer pool|Disco, RAM y buffer pool]]"]
---
# Modelo de costos de I/O

El costo de una consulta se mide en **I/O**: cuántas páginas hay que traer del disco a la RAM. Una tabla de $|R|$ tuplas con $B$ tuplas por página ocupa $\lceil |R|/B \rceil$ páginas, y recorrerla entera cuesta eso.

## Costo de una consulta

![Cómo se guarda una tabla - 9 tuplas en 3 páginas](adjuntos/Cómo%20se%20guarda%20una%20tabla%20-%209%20tuplas%20en%203%20páginas.png)

- El costo más grande en una base de datos es **traer las páginas del disco duro a la RAM**.
- Objetivo: responder las consultas haciendo la menor cantidad posible de lecturas al disco.
- **Costo I/O:** número de páginas llevadas a memoria para responder una consulta.

### Memorias

![Modelo de costos - memoria principal vs secundaria](adjuntos/Modelo%20de%20costos%20-%20memoria%20principal%20vs%20secundaria.png)

### Costo de lecturas

![Modelo de costos - páginas de una relación](adjuntos/Modelo%20de%20costos%20-%20páginas%20de%20una%20relación.png)

Ejemplo de costo de una consulta:

![Costo de una consulta - SELECT todo de T](adjuntos/Costo%20de%20una%20consulta%20-%20SELECT%20todo%20de%20T.png)

![Costo de una consulta - SELECT T.a](adjuntos/Costo%20de%20una%20consulta%20-%20SELECT%20T.a.png)

![Costo de una consulta - WHERE sobre T.a](adjuntos/Costo%20de%20una%20consulta%20-%20WHERE%20sobre%20T.a.png)

> [!note]- Transcripción de las imágenes
> 1. **Cómo se guarda una tabla:** una tabla T(a int, b text) con 9 tuplas. En el disco duro, Tuplas 1–3 = Página 1, Tuplas 4–6 = Página 2, Tuplas 7–9 = Página 3.
> 2. **Modelo de costos — memoria principal vs. secundaria.** Memoria secundaria: los datos se guardan ahí, la lectura se hace por **páginas** y una página tiene un tamaño de **B** tuplas; *se cuentan los accesos (lectura/escritura) a memoria secundaria*. Memoria principal: los datos son llevados a ella y tiene una capacidad de **M** páginas; *los accesos a memoria principal son despreciables*.
> 3. **Modelo de costos:** ¿cuánto cuesta leer n tuplas de memoria secundaria? $\lceil n/B \rceil$. ¿Cuántas páginas usa una relación R? $\lceil |R|/B \rceil$.
> 4. **Costo de una consulta:** `SELECT * FROM T` → $\lceil |R|/B \rceil = \lceil 9/3 \rceil$. "El costo es 3, porque debo leer las 3 páginas."
> 5. `SELECT T.a FROM T` → $\lceil 9/3 \rceil$. "El costo nuevamente es 3, porque debo leer las 3 páginas."
> 6. ¿Cuál es el costo en I/O de `SELECT * FROM T WHERE T.a = 4` y de `SELECT * FROM T WHERE T.a >= 4`? → $\lceil |R|/B \rceil$.

> [!tip] Complemento (slides "Clase 9")
> - **Respuesta a la última imagen:** sin índice, ambas cuestan **3**, porque hay que leer todas las páginas para saber qué tuplas cumplen la condición. Una tabla sin orden no permite saltarse páginas.
> - **Proyectar menos columnas** (`SELECT T.a`) **no** reduce el I/O: se lee la página completa igual.
> - "¿Podemos hacer esto mejor?" Sí, con **índices**: [[09 - Índices en bases de datos|Índices en bases de datos]].
> - En el modelo, los accesos a RAM se consideran gratis; solo cuentan las páginas leídas o escritas en disco.

## Preguntas de repaso

1. ¿Qué es el costo de I/O de una consulta?
> [!question]- Respuesta
> El número de páginas que hay que traer del disco a la memoria para responderla.

2. Una relación tiene 1.000 tuplas y caben 30 por página. ¿Cuántas páginas usa?
> [!question]- Respuesta
> $\lceil 1000/30 \rceil = 34$ páginas.

3. ¿Por qué `SELECT T.a FROM T` cuesta lo mismo que `SELECT * FROM T`?
> [!question]- Respuesta
> Porque el disco se lee por páginas completas: para obtener solo la columna `a` igual hay que traer las 3 páginas.

4. Sin índice, ¿cuánto cuesta `SELECT * FROM T WHERE T.a = 4`?
> [!question]- Respuesta
> 3 I/O: hay que recorrer todas las páginas, porque no se sabe en cuál está la tupla.
