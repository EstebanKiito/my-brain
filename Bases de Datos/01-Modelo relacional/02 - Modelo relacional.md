---
ramo: Bases de Datos
tema: Modelo relacional
tags: [bd/modelo-relacional, origen/complemento]
prerrequisitos: ["[[01 - Sistemas de bases de datos y DBMS|Sistemas de bases de datos y DBMS]]"]
---
# Modelo relacional

El modelo relacional guarda los datos en **tablas (relaciones)** con columnas tipadas (**atributos**) y filas (**tuplas**). Es la base sobre la que funcionan SQL y el álgebra relacional.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 1: Motivación" y "Clase 3: Repaso de llaves + SQL")
> El modelo de las bases de datos relacionales se basa en:
> - **Tablas** (relaciones).
> - **Columnas** de las tablas (atributos con sus tipos).
> - **Filas** de las tablas (tuplas), que contienen los datos.

## Ejemplo: la relación Películas

| ID Película | Nombre Película | Año | Categoría | Calificación (IMDB) |
|---|---|---|---|---|
| 1 | Interstellar | 2014 | Fantasía | 8.6 |
| 2 | The Revenant | 2015 | Drama | 8.1 |
| 3 | The Imitation Game | 2014 | Biografía | 8.1 |
| 4 | The Theory of Everything | 2014 | Biografía | 7.7 |

> [!tip] Complemento — vocabulario (slides "Clase 1" y "Clase 3")
> | Término | Qué es | En el ejemplo |
> |---|---|---|
> | **Relación** | cada tabla | `Películas` |
> | **Atributo** | cada columna | id, nombre, año, categoría, calificación |
> | **Tupla** | cada fila | `(1, Interstellar, 2014, Fantasía, 8.6)` |
> | **Esquema** | conjunto de relaciones con sus atributos | `Películas(id, nombre, año, categoría, calificación)` |
> | **Dominio** | tipo de dato de cada atributo | `Películas(id:int, nombre:string, año:int, categoría:string, calificación:float)` |
> | **Instancia** | conjunto de tuplas para cada relación del esquema | las 4 filas de la tabla |
>
> - **Una relación es un conjunto de tuplas:** no hay filas repetidas. Si la fila 4 aparece dos veces, ya no es una relación válida.
> - **Esquema vs instancia:** el esquema dice el nombre de la tabla y sus atributos (es fijo); la instancia son los datos de un momento (cambian con cada INSERT, UPDATE o DELETE).
> - Un esquema de varias relaciones: `Películas(id, nombre, año, categoría, calificación)`, `Actor(id, nombre, edad)`, `Actuó_en(id_actor, id_película)`.
> - Aunque las tablas parecen arreglos o listas de Python, hay diferencias: se asume que están **en disco y no en memoria**, y se manipulan con SQL y álgebra relacional.

> [!tip] Complemento — restricciones de integridad (slides "Clase 1" y "Clase 3")
> Son restricciones que imponemos a un esquema y que **todas las instancias deben satisfacer**. La más importante son las **llaves**: un conjunto de atributos que identifica de manera única a cada tupla. En el esquema, la llave primaria se subraya. Los tipos de llave están en [[03 - Superllaves, claves candidatas y clave primaria|Superllaves, claves candidatas y clave primaria]].

## Otros modelos de datos

> [!tip] Complemento — modelos de datos (slides "Clase 1")
> Un **modelo de datos** es una notación para escribir datos. En el curso se ven dos en detalle: el **relacional** (el más usado en producción) y los **semiestructurados** (key-value, grafos), cuya necesidad ha ido aumentando.
>
> Los mismos datos de películas en un modelo semiestructurado (key-value / JSON), con estructura jerárquica año → tipo → películas:
> ```json
> {
>   "2014": {
>     "Biografía": [
>       { "nombre": "The Imitation Game", "calificación": 8.1 },
>       { "nombre": "The Theory of Everything", "calificación": 7.7 }
>     ],
>     "SciFi": [ { "nombre": "Interstellar", "calificación": 8.6 } ]
>   },
>   "2015": { "Drama": [ { "nombre": "The Revenant", "calificación": 8.1 } ] }
> }
> ```
> En la slide también aparece en XML (`<Películas><Año valor="2014"><Tipo valor="Biografía"><Película …/>`).
>
> | | Relacional | Semiestructurado (XML, JSON) |
> |---|---|---|
> | Almacena datos y es versátil para modelar | sí | sí |
> | Lenguaje de consultas | sí (SQL) | sí |
> | Esquema | **definido por un esquema** | flexible, no está separado por un esquema |
> | Consecuencia | más simple, pero más limitado | más flexible |
>
> Otros modelos: orientados a objetos, columnares, de grafos. "Tenemos que aprender las diferencias y cuándo usar qué."

## Preguntas de repaso

1. ¿Qué es una relación, un atributo y una tupla?
> [!question]- Respuesta
> Una relación es una tabla; un atributo es una columna (con su dominio o tipo), y una tupla es una fila con datos.

2. ¿Cuál es la diferencia entre esquema e instancia?
> [!question]- Respuesta
> El esquema es la estructura: nombre de cada relación y sus atributos, por ejemplo `Películas(id, nombre, año, categoría, calificación)`. La instancia es el conjunto concreto de tuplas que tiene cada relación en un momento dado.

3. ¿Por qué no puede haber dos filas idénticas en una relación?
> [!question]- Respuesta
> Porque una relación es un conjunto de tuplas, y un conjunto no tiene elementos repetidos.

4. ¿Qué es una restricción de integridad y cuál es la más importante?
> [!question]- Respuesta
> Una condición impuesta al esquema que toda instancia debe cumplir. La más importante es la llave, que identifica de forma única cada tupla.

5. ¿En qué se diferencia el modelo relacional de uno semiestructurado como JSON?
> [!question]- Respuesta
> El relacional está definido por un esquema fijo, lo que lo hace más simple pero más limitado. El semiestructurado es jerárquico y flexible, sin un esquema separado.
