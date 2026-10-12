---
ramo: Bases de Datos
tema: Almacenamiento e índices
tags: [bd/indices, origen/complemento]
prerrequisitos: ["[[04 - Modelo de costos de IO|Modelo de costos de IO]]", "[[07 - Diccionarios|Diccionarios]]"]
---
# Índices en bases de datos

Un índice es una estructura auxiliar (un diccionario en disco) que, dado un valor o un rango de un atributo, encuentra rápido las tuplas que cumplen la condición, **sin recorrer toda la tabla**.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 9: Almacenamiento y Índices")
> **Índice:** herramienta que optimiza el acceso a los datos para una consulta o un conjunto de consultas en particular. Se le indica que queremos las tuplas con cierto valor en un atributo (o con un valor en cierto rango) y encuentra rápido las que cumplen la condición. Idealmente, un índice debe **caber en RAM**.
>
> **Consultas a optimizar:**
> ```sql
> -- por valor
> SELECT * FROM Table WHERE Table.value = 'value';
> -- por rango
> SELECT * FROM Table WHERE Table.value >= 'value';
> ```
>
> **En SQL:**
> ```sql
> CREATE INDEX <nombre_indice> ON <tabla> (<atributo>);
> CREATE INDEX idx_usuarios_edad ON Usuarios (edad);   -- ejemplo
> ```
> **Las llaves primarias están indexadas por defecto** (y también las columnas `UNIQUE`).
>
> **Flujo:** con `Usuarios(uid int PRIMARY KEY, nombre text, edad int)`, la consulta `SELECT * FROM Usuarios WHERE uid = 104` se resuelve con el índice de `uid` y se evita recorrer toda la tabla.
>
> **Definiciones:**
> - **Search key:** el valor con que se busca en el índice (por ejemplo, el `uid`).
> - **Data entry:** lo que devuelve el índice para esa search key: la tupla misma o un puntero a ella (ver [[12 - Índices clustered y unclustered|clustered vs unclustered]]).

> [!tip] Complemento — tipos y costos
> | Índice | Búsqueda por igualdad | Búsqueda por rango |
> |---|---|---|
> | Sin índice (scan) | $\lceil \lvert R \rvert/B \rceil$ | $\lceil \lvert R \rvert/B \rceil$ |
> | [[10 - Índice hash\|Hash]] | ≈ 1 I/O | no sirve |
> | [[11 - Índice árbol B+\|Árbol B+]] | altura $h$ | $h$ + páginas con resultados |
>
> **Costo de un índice:** ocupa espacio y **cada `INSERT`, `UPDATE` o `DELETE` debe actualizarlo**. Por eso no se indexa todo: solo las columnas que se usan seguido en `WHERE`, `JOIN` u `ORDER BY`. En PostgreSQL, `EXPLAIN SELECT …` muestra si la consulta usa un índice (*Index Scan*) o recorre la tabla (*Seq Scan*).

## Preguntas de repaso

1. ¿Para qué sirve un índice?
> [!question]- Respuesta
> Para encontrar rápido las tuplas con cierto valor (o rango) en un atributo, con menos I/O que recorrer toda la tabla.

2. ¿Qué atributos están indexados por defecto?
> [!question]- Respuesta
> La llave primaria (y en PostgreSQL también las columnas con restricción `UNIQUE`).

3. ¿Qué es la search key y qué es el data entry?
> [!question]- Respuesta
> La search key es el valor por el que se busca. El data entry es lo que devuelve el índice: la tupla o un puntero a ella.

4. ¿Por qué no conviene indexar todas las columnas?
> [!question]- Respuesta
> Porque cada índice ocupa espacio y vuelve más lentas las escrituras, ya que hay que actualizarlo en cada INSERT, UPDATE o DELETE.
