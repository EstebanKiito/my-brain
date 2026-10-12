---
ramo: Bases de Datos
tema: NoSQL
tags: [bd/nosql, origen/complemento]
prerrequisitos: ["[[02 - Modelo relacional|Modelo relacional]]", "[[02 - Propiedades ACID|Propiedades ACID]]"]
---
# Bases de datos NoSQL

"NoSQL" agrupa a las bases de datos con **menos esquema y menos garantías** que las relacionales, a cambio de **distribuirse** bien entre muchos servidores. Nacen de sistemas como la web, Google o Twitter, donde un solo servidor no alcanza.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 14: NoSQL")
> | | Relacionales (SQL) | NoSQL |
> |---|---|---|
> | Estructura | mucha (un **esquema fijo**) | menos restricciones, menos esquema |
> | Garantías | muchas (**ACID**) | menos garantías de consistencia |
> | Distribución | generalmente **centralizadas** (viven en un servidor) | más adecuadas para la distribución |
>
> **¿Por qué NoSQL?** Los sistemas relacionales no están pensados para un entorno **altamente distribuido** (la web, Google, Twitter, Instagram, etc.).
>
> **Sistemas distribuidos: dos problemas fundamentales**
> | Problema | Solución |
> |---|---|
> | Los datos **no caben** en un computador | **Fragmentación** (*sharding*): repartir los datos. Ej.: usuarios de Twitter de la A a la M en un servidor y de la N a la Z en otro |
> | Los servidores **pueden fallar** | **Replicación**: varias copias de los datos en distintos servidores |
>
> Al replicar aparece el dilema de qué garantías se pueden mantener: [[02 - Consistencia eventual y BASE|CAP, consistencia eventual y BASE]].

> [!tip] Complemento — sabores de NoSQL (slides "Clase 14")
> Los más populares hoy son:
> | Tipo | Idea | Ejemplos | Nota |
> |---|---|---|---|
> | **Key-value** | pares llave → valor | Amazon Dynamo, Redis | [[03 - Bases key-value y de grafos\|key-value y grafos]] |
> | **Documentos** | el valor es un documento JSON | MongoDB, CouchDB | [[04 - Bases de documentos y JSON\|documentos y JSON]] |
> | **Grafos** | nodos y relaciones | Neo4J, Virtuoso, Jena, Blazegraph | [[03 - Bases key-value y de grafos\|key-value y grafos]] |
>
> En la slide se ordenan así: key-value (más **volumen de datos**, menos complejidad) → documentos → grafos (más **complejidad**, menos volumen).

## Preguntas de repaso

1. ¿Qué entrega un sistema relacional que un NoSQL típicamente relaja?
> [!question]- Respuesta
> Un esquema fijo y garantías ACID. Los NoSQL tienen menos esquema y menos garantías de consistencia, a cambio de distribuirse mejor.

2. ¿Cuáles son los dos problemas fundamentales de un sistema distribuido y cómo se enfrentan?
> [!question]- Respuesta
> Que los datos no caben en un computador (fragmentación) y que los servidores fallan (replicación).

3. Nombra los tres sabores de NoSQL más populares y un ejemplo de cada uno.
> [!question]- Respuesta
> Key-value (Redis, Amazon Dynamo), documentos (MongoDB, CouchDB) y grafos (Neo4J).
