---
ramo: "Tecnologías y Aplicaciones Web"
tema: "Almacenamiento en el cliente"
tags:
  - web
  - bases-de-datos
  - nosql
  - origen/complemento
prerrequisitos:
  - "[[04 - Caché, Cache API y CDN]]"
  - "[[04 - Modelos, migraciones y seeds con Sequelize]]"
---

# Almacenamiento en el servidor: SQL y NoSQL

Todo lo que se guarda en el navegador es una copia o un dato local de un usuario. La fuente de verdad de una aplicación vive en el servidor: en sus cachés y, sobre todo, en su **base de datos**. Esta nota ubica las alternativas del lado del servidor, desde las bases relacionales que ya usa el curso hasta las distintas familias NoSQL.

## Del cliente al servidor

| Nivel | Dónde | Ejemplos |
|---|---|---|
| Caché del cliente | Navegador | Caché HTTP, Cache API, Web Storage |
| Caché compartida | Entre el cliente y el origen | CDN, proxy reverso |
| Caché del servidor | Junto a la aplicación | Redis en memoria |
| Persistencia | Servidor | Base de datos SQL o NoSQL |

## Bases de datos SQL

Las bases **relacionales** (PostgreSQL, MySQL, SQLite) organizan los datos en **tablas** con un **esquema fijo**, se consultan con SQL y garantizan transacciones ACID. Son la opción por defecto cuando los datos tienen relaciones claras y la consistencia importa, como en el proyecto del curso con PostgreSQL y Sequelize.

## Bases de datos NoSQL

**NoSQL** significa "no solo SQL": bases que no siguen el modelo relacional. En general:

- tienen **menos restricciones** que un esquema relacional;
- son **schemaless**: cada registro puede tener campos distintos;
- son **fáciles de distribuir** en muchos servidores, lo que facilita escalar.

| Tipo | Modelo | Ejemplo | Uso típico |
|---|---|---|---|
| **Documentos** | Documentos JSON anidados | MongoDB | Catálogos, perfiles, contenido con estructura variable |
| **Key-value** | Una llave apunta a un valor | Redis | Cachés, sesiones, contadores |
| **Vectoriales** | Vectores numéricos (*embeddings*) con búsqueda por similitud | Qdrant | Búsqueda semántica, recomendaciones, IA |
| **Grafos** | Nodos y relaciones | Neo4j | Redes sociales, rutas, recomendaciones |

> [!tip] Elegir por el patrón de acceso
> Si hay muchas relaciones y la consistencia es crítica (pagos, inventario), lo relacional suele ser lo mejor. Si los datos tienen forma variable, se accede siempre por una llave o hay que escalar horizontalmente, una NoSQL puede encajar mejor. Muchas aplicaciones combinan ambas: PostgreSQL como fuente de verdad y Redis como caché.

> [!warning] Schemaless no significa sin estructura
> Que la base no imponga un esquema no elimina la estructura: la tiene que mantener la aplicación. Sin cuidado, la misma colección termina con documentos incompatibles entre sí.

El modelo NoSQL, la consistencia eventual y cada familia se estudian en detalle en Bases de Datos: [[01 - Bases de datos NoSQL|Bases de datos NoSQL]], [[03 - Bases key-value y de grafos|Bases key-value y de grafos]] y [[04 - Bases de documentos y JSON|Bases de documentos y JSON]].

## Preguntas de repaso

> [!question]- ¿Qué significa que una base NoSQL sea schemaless y qué riesgo implica?
> Que la base no exige que todos los registros tengan los mismos campos. Eso da flexibilidad, pero traslada a la aplicación la responsabilidad de mantener datos coherentes.

> [!question]- ¿Para qué sirve una base de datos vectorial?
> Para guardar *embeddings* (vectores que representan textos, imágenes u otros datos) y buscar los más parecidos a uno dado. Es la base de la búsqueda semántica y de muchas aplicaciones de IA.

> [!question]- ¿Por qué una aplicación usaría PostgreSQL y Redis a la vez?
> PostgreSQL guarda los datos de forma consistente y relacional (la fuente de verdad), y Redis, en memoria, responde muy rápido a datos consultados con frecuencia o efímeros, como sesiones o resultados en caché.
