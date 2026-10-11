---
ramo: Bases de Datos
tema: Evaluación de consultas
tags: [bd/evaluacion, origen/complemento]
prerrequisitos: ["[[01 - Algoritmos en un DBMS e iteradores|Algoritmos en un DBMS e iteradores]]", "[[09 - Índices en bases de datos|Índices en bases de datos]]"]
---
# Selección y proyección

La **selección** (σ) recorre toda la tabla salvo que haya un índice sobre el atributo de la condición. La **proyección** (π) siempre recorre toda la tabla y solo recorta columnas.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 10: Evaluación de consultas")
> El algoritmo de selección cambia según la consulta sea de **igualdad** (=) o de **rango** (<, >), y según el atributo esté **indexado** o no.
>
> **Selección sin índice:**
> ```
> open():  R.open()
> next():  t := R.next()
>          while t != null do
>              if t satisface condición then return t
>              t := R.next()
>          return null
> close(): R.close()
> ```
> Necesariamente hay que **recorrer todo R**: costo $\lceil |R|/B \rceil$.
>
> **Selección con índice I y consulta de igualdad:**
> ```
> open():  I.open(); I.search(Atributo = valor)
> next():  t := I.next(); if t != null return t; return null
> close(): I.close()
> ```
> - Solo se leen las páginas que satisfacen la condición (más I/O si muchas tuplas la cumplen).
> - Cambia según el índice sea **clustered o unclustered**: en el unclustered, cada tupla puede estar en una página distinta. Ver [[12 - Índices clustered y unclustered|Índices clustered y unclustered]].
> - Si el atributo es **llave primaria**, la operación cuesta prácticamente **~1 I/O**.
>
> **Selección con índice y consulta de rango:** "existe un índice especial para esto": el [[11 - Índice árbol B+|árbol B+]], que baja hasta el inicio del rango y recorre las hojas.
>
> **Proyección:** algoritmo muy sencillo:
> ```
> next():  t := R.next()
>          if t != null return project(t, atributos)
>          return null
> ```
> Necesariamente recorre todo R. Si además se pide `DISTINCT`, hay que eliminar duplicados ordenando o con hash, lo que es más caro.

## Preguntas de repaso

1. ¿Cuánto cuesta una selección sin índice?
> [!question]- Respuesta
> Leer toda la relación: $\lceil |R|/B \rceil$ páginas, porque hay que revisar cada tupla.

2. ¿Cuánto cuesta una selección por igualdad sobre la llave primaria indexada?
> [!question]- Respuesta
> Prácticamente ~1 I/O (más la altura del índice si no está en memoria).

3. ¿Qué índice conviene para una selección por rango?
> [!question]- Respuesta
> Un árbol B+, porque las hojas están ordenadas y encadenadas.

4. ¿Por qué la proyección no se beneficia de un índice sobre las tuplas?
> [!question]- Respuesta
> Porque necesita todas las tuplas de R (solo descarta columnas), así que igual recorre toda la relación.
