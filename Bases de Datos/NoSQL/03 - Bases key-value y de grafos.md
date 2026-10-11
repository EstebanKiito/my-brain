---
ramo: Bases de Datos
tema: NoSQL
tags: [bd/nosql, origen/complemento]
prerrequisitos: ["[[01 - Bases de datos NoSQL|Bases de datos NoSQL]]", "[[08 - Tablas de hash|Tablas de hash]]"]
---
# Bases key-value y de grafos

Dos sabores de NoSQL en extremos opuestos. Las **key-value** son grandes tablas de hash persistentes: simples y muy escalables. Las de **grafos** están especializadas en guardar y recorrer **relaciones**.

## Bases key-value

> [!tip] Complemento — nota nueva (fuente: slides "Clase 14: NoSQL")
> - Son independientes del esquema: almacenan la información en **pares**, y cada par tiene una **llave** (identificador) y un **valor**.
> - **Operaciones cruciales:** `put(key, value)`, `get(key)` y `delete(key)`.
>
> | Key | Value |
> |---|---|
> | Chile | Santiago |
> | Inglaterra | Londres |
> | Escocia | Edinburgo |
> | Francia | Paris |
> | Alemania | Berlin |
>
> - Son **grandes tablas de hash persistentes** (ver [[08 - Tablas de hash|Tablas de hash]]). La categoría es difusa, porque muchas bases de otros tipos usan key-value y hashing hasta cierto punto.
> - Ejemplo más importante: **Amazon Dynamo**; otro es **Redis**.
> - El valor puede representar **cualquier cosa**, por ejemplo un carro de compras:
>
> | cartID | value |
> |---|---|
> | 11789 | usrID: "Juan", ítem: "Magic the Gathering Deck", value: … |
> | 12309 | usrID: "Domagoj", item: "APEX XTX50 regulator set", value: … |
>
> Uso típico: caché, sesiones de usuario, carros de compra; todo lo que se busca **solo por llave**.

## Bases de grafos y RDF

> [!tip] Complemento — nota nueva (fuente: slides "Clase 14: NoSQL")
> - Especializadas en guardar **relaciones**.
> - En general almacenan sus datos como **property graphs**: nodos y aristas, ambos con propiedades.
> - Ejemplos: **Neo4J**, Virtuoso, Jena, Blazegraph (estos tres últimos para RDF, la Web Semántica).

> [!example] Ejemplo extra — "amigos de mis amigos" (Neo4J, lenguaje Cypher)
> ```
> MATCH (yo:Usuario {nombre: "Adrian"})-[:SIGUE]->()-[:SIGUE]->(sugerido)
> RETURN DISTINCT sugerido.nombre
> ```
> En SQL esto es un join de `Sigue` consigo misma por cada nivel de profundidad. En una base de grafos se recorren las aristas directamente, lo que conviene para redes sociales, recomendaciones y rutas.

## Preguntas de repaso

1. ¿Cuáles son las operaciones básicas de una base key-value?
> [!question]- Respuesta
> `put(key, value)`, `get(key)` y `delete(key)`.

2. ¿Por qué se dice que una base key-value es una tabla de hash persistente?
> [!question]- Respuesta
> Porque guarda pares llave-valor y accede a ellos por llave mediante hashing, igual que una tabla de hash, pero guardando los datos de forma persistente (y distribuida).

3. ¿Para qué problemas conviene una base de grafos?
> [!question]- Respuesta
> Para datos dominados por relaciones que se recorren a varios niveles: redes sociales, recomendaciones o rutas. En SQL requerirían muchos joins encadenados.
