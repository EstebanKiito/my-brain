---
ramo: "Tecnologías y Aplicaciones Web"
tema: "APIs web y REST"
tags:
  - web
  - api
  - rest
  - crud
  - origen/complemento
prerrequisitos:
  - "[[01 - APIs y APIs web]]"
---

# CRUD y principios REST

Casi toda aplicación hace lo mismo con sus datos: crearlos, leerlos, modificarlos y borrarlos. Para que distintas APIs se parezcan entre sí y sean fáciles de usar, existe un estilo que dice cómo exponer esas operaciones sobre HTTP: **REST**. Una API que lo sigue es predecible: con ver un endpoint se puede adivinar cómo son los demás.

## CRUD

**CRUD** son las cuatro operaciones que se pueden hacer sobre un recurso: **C**reate, **R**ead, **U**pdate y **D**elete. En la web se traducen a métodos HTTP sobre rutas:

| CRUD | Método | Ruta | Acción |
|---|---|---|---|
| R | `GET` | `/users` | Obtener la colección de recursos |
| C | `POST` | `/users` | Agregar un recurso a la colección |
| R | `GET` | `/users/2` | Obtener un recurso |
| U | `PUT` | `/users/2` | Definir (reemplazar) los atributos de un recurso |
| U | `PATCH` | `/users/2` | Modificar algunos atributos de un recurso |
| D | `DELETE` | `/users/2` | Eliminar un recurso |

Por ejemplo, en Instagram se **crean** posts o historias (`POST /stories`), se **lee** el timeline (`GET /stories`, `GET /posts/1`), se **edita** un post propio (`PUT` o `PATCH /posts/2`) y se **elimina** un post propio (`DELETE /posts/2`).

> [!tip] `PUT` frente a `PATCH`
> `PUT` envía la representación **completa** del recurso y la reemplaza; lo que no se envía se pierde. `PATCH` envía **solo los campos** que cambian.

## REST

**REST** (*REpresentational State Transfer*) es un **estilo arquitectónico**: un conjunto de principios (o restricciones) que debe cumplir un servicio web para ser escalable y fácil de usar. Lo definió Roy Fielding en su tesis de doctorado, el año 2000. Trabaja con los conceptos de **recursos** y **representaciones** de recursos, y se apoya en los métodos HTTP para indicar las acciones.

Un servicio que cumple todos estos principios se llama **RESTful**:

| Principio | Qué exige |
|---|---|
| **Client-server** | Cliente y servidor separados, que pueden evolucionar de forma independiente |
| **Stateless** | Cada request trae toda la información necesaria para completarla; el servidor no recuerda requests anteriores |
| **Cacheable** | Cada respuesta indica si se puede cachear o no |
| **Uniform interface** | Cada recurso se identifica de forma única (*resource-based*); se manipula a través de representaciones uniformes; cada mensaje es autodescriptivo; y mediante hipervínculos el cliente puede llegar a todos los recursos (*HATEOAS*) |
| **Layered system** | El cliente no distingue si hay capas intermedias (proxies, balanceadores): son transparentes |
| **Code on demand** (opcional) | El servidor puede enviar scripts al cliente para indicarle cómo ejecutar una acción |

## Cómo se ve un servicio RESTful

REST se apoya fuertemente en HTTP, y cada parte de la request tiene un rol:

- el **alcance** va en el path (el endpoint): `/repos/{owner}/{repo}/issues`;
- la **acción** va en el método HTTP: `POST`;
- los **datos** van en el body (*payload*), y los metadatos en los headers.

Además:

- cada endpoint es **independiente** del resto;
- no hay redirecciones entre pantallas, porque la API no tiene pantallas;
- un caso de uso puede requerir consumir **varios** endpoints.

> [!warning] CRUD no es lo mismo que REST
> CRUD es el conjunto de operaciones sobre datos; existe en cualquier sistema, incluso sin web. REST es un estilo para diseñar servicios web, con principios como la ausencia de estado o las respuestas cacheables. Una API RESTful suele exponer operaciones CRUD, pero cumplir REST exige mucho más que mapear CRUD a métodos HTTP.

La versión de este mapeo en Rails, con `resources`, está en [[02 - CRUD|CRUD]] y [[10 - Rutas en Rails|Rutas en Rails]].

## Preguntas de repaso

> [!question]- ¿Qué implica que una API REST sea stateless?
> Que el servidor no guarda contexto de la conversación con el cliente: cada request tiene que incluir todo lo necesario, incluida la identificación del usuario (por ejemplo, un token). A cambio, cualquier servidor puede atender cualquier request, lo que facilita escalar.

> [!question]- ¿Cuándo conviene `PATCH` en vez de `PUT`?
> Cuando se modifican solo algunos campos: `PATCH` envía únicamente lo que cambia. Con `PUT` habría que enviar el recurso completo, y lo omitido se perdería.

> [!question]- En `POST /posts/2/comments` con un JSON en el body, ¿dónde está el alcance, la acción y los datos?
> El alcance está en el path (los comentarios del post 2), la acción en el método (`POST`: crear) y los datos en el body (el contenido del comentario).
