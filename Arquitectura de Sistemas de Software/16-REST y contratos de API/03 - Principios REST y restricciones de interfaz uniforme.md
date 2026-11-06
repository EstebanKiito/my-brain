---
ramo: "Arquitectura de Sistemas de Software"
tema: "REST y contratos de API"
tags:
  - arquisis/integracion
  - arquisis/rest
  - origen/complemento
prerrequisitos:
  - "[[01 - REST como estilo derivado de restricciones]]"
---

# Principios REST y restricciones de interfaz uniforme

REST se resume en **nueve principios**. Los primeros cinco vienen de los estilos que lo influencian. Los últimos cuatro son las partes de la **interfaz uniforme**: una sola restricción, la más cara, que en la práctica se divide en cuatro reglas. Estas reglas son las que permiten decir si una API está bien implementada como REST.

## Los nueve principios

| # | Principio | Idea |
|---|---|---|
| 1 | Cliente/servidor | Separar responsabilidades: interfaz y datos evolucionan por separado |
| 2 | Capas | Intermediarios transparentes entre cliente y servidor |
| 3 | Cacheable | Las respuestas indican si se pueden reutilizar |
| 4 | **Stateless** | El servidor no guarda el estado de la conversación |
| 5 | Code on demand | El cliente puede descargar y ejecutar código (opcional) |
| 6 | Recursos identificables | Cada recurso tiene una URI |
| 7 | Manipulación mediante representaciones | Se trabaja con "fotografías" del recurso |
| 8 | Mensajes autodescriptivos | Cada mensaje lleva lo necesario para entenderlo |
| 9 | Hipermedia como motor del estado (HATEOAS) | Las respuestas traen links a lo que se puede hacer |

**Stateless** en detalle: el servidor no almacena información de su conversación con el cliente. Cada petición debe traer todo lo necesario para identificar la respuesta, y el estado de la sesión lo mantiene el cliente (por ejemplo, un token). El servidor sí puede tener estado de los **recursos** (la base de datos): lo prohibido es guardar estado de la **conversación**. Algunos análisis formales de sistemas RESTful (Zuzak, 2012) muestran que el servidor *podría* ser stateful en ciertos casos, pero entonces pierde las ventajas de escala que da esta restricción.

Los **mensajes autodescriptivos** se pueden resolver en el propio servidor o en un **middleware** (un gateway que agrega headers estándar, valida formatos o traduce errores), porque los intermediarios entienden la misma semántica HTTP.

## Recurso y representación

> [!tip] Recurso
> La abstracción clave de la información: **si tiene nombre, puede ser un recurso** (un cliente, un pedido, "las órdenes abiertas de hoy"). Se identifica con una URI, por ejemplo `/apple/1`.

> [!tip] Representación
> Una **"fotografía" del recurso en un momento del tiempo**, en algún formato: texto plano, imagen, JSON, HTML, YAML, XML. Puede ser casi cualquier formato, idealmente estándar.

El ejemplo del curso es el recurso "manzana" `/apple/1`. Puede representarse como un texto en español ("manzana roja, brillante y jugosa"), el mismo texto en ruso, una imagen PNG, un HTML o un JSON. Todas describen el mismo recurso conceptual.

## Las cuatro restricciones de la interfaz uniforme

**1. Los recursos identificables son únicos y opacos.**
- Cada recurso tiene una URI única (`http://ejemplo.com/cliente/bar/orden/1`), y dos recursos distintos no comparten URI.
- **Opaco** significa que el cliente no debe adivinar ni construir la URI: debe recibirla. Así se evita el acoplamiento entre cliente y servidor.
- Hay que evitar el antipatrón `http://{host}/{service}/{id}`, donde el cliente arma URIs con un patrón y queda acoplado a él.
- Si una URI cambia, se usan proxies o redirecciones.

**2. Los recursos son conceptuales y se manipulan mediante (múltiples) representaciones.**
- El formato se **negocia**. El estándar son los *media types* (MIME).
- El cliente indica sus preferencias en orden con el header `Accept`, y el servidor responde indicando el formato con `Content-Type`:

```http
GET /algo HTTP/1.1
Accept: application/json, application/xml

HTTP/1.1 200 OK
Content-Type: application/json
```

**3. Los mensajes son autodescriptivos y estándar.** Se usa una semántica que conocen cliente, servidor e intermediarios:

| Método | Semántica | Safe | Idempotente |
|---|---|---|---|
| `GET` | Leer (cacheable) | Sí | Sí |
| `POST` | Crear una entidad sin conocer su ID | No | No |
| `PUT` | Actualizar o reemplazar la entidad | No | Sí |
| `PATCH` | Modificación parcial | No | No necesariamente |
| `DELETE` | Borrar | No | Sí |

Los códigos de estado: `1xx` informativos, `2xx` éxito (`200 OK`, `201 Created`), `3xx` redirección, `4xx` **error del cliente**, `5xx` **error del servidor**. Para describir errores existe el formato estándar *problem details* (RFC 9457).

**4. HATEOAS** (*Hypertext As The Engine Of Application State*). Las representaciones contienen los **links** necesarios para navegar y descubrir otros recursos, y los **controles** para cambiar su estado:

```xml
<orden self="http://ejemplo.com/orden/101230">
  <cliente ref="http://ejemplo.com/cliente/bar"/>
  <producto ref="http://ejemplo.com/producto/21034"/>
  <cantidad valor="1"/>
</orden>
```

## El patrón contenedor-ítem (CRUD)

| Operación | Petición |
|---|---|
| Listar | `GET /contenedor` |
| Añadir | `POST /contenedor` (ítem en el body; la URI del nuevo ítem vuelve en el header `Location`) |
| Leer | `GET /contenedor/item` |
| Modificar | `PUT /contenedor/item` |
| Borrar | `DELETE /contenedor/item` |

Aquí vive casi toda API en producción, en el nivel 2 de madurez de Richardson. Ver [[04 - Qué no es REST malas prácticas y madurez de Richardson]].

> [!warning] Idempotente no es lo mismo que safe
> **Safe** significa que no cambia el estado del recurso (`GET`). **Idempotente** significa que repetirla tiene el mismo efecto que hacerla una vez (`PUT`, `DELETE`). `DELETE` cambia el estado, así que no es safe, pero borrar dos veces deja el mismo resultado, así que es idempotente. `POST` no es ninguna de las dos: dos `POST` crean dos recursos.

## Preguntas de repaso

> [!question]- ¿Qué significa que el servidor sea stateless si igual tiene una base de datos?
> Que no guarda el estado de la conversación con cada cliente (en qué paso va, qué pidió antes). Cada petición trae todo lo necesario. El estado de los recursos sí vive en el servidor. Gracias a esto, cualquier réplica puede atender cualquier petición.

> [!question]- ¿Por qué se dice que una URI debe ser opaca y qué antipatrón lo viola?
> El cliente no debe deducir ni armar URIs: debe recibirlas del servidor. Así el servidor puede reorganizarlas sin romper a los clientes. El antipatrón `http://{host}/{service}/{id}` obliga al cliente a construir la URI con un patrón, y queda acoplado a esa estructura.

> [!question]- Un cliente prefiere JSON pero acepta XML. ¿Cómo lo comunica y cómo sabe qué recibió?
> Envía el header `Accept: application/json, application/xml`, en orden de preferencia. El servidor elige un formato y lo indica en el header `Content-Type` de la respuesta.

> [!question]- Clasifique como safe o idempotente: GET, POST, PUT y DELETE.
> GET es safe e idempotente. POST no es ninguna de las dos. PUT es idempotente pero no safe. DELETE es idempotente pero no safe.

> [!question]- ¿Qué códigos devuelve el patrón contenedor-ítem al crear un ítem y dónde va su URI?
> `POST /contenedor` responde `201 Created`, y la URI del nuevo ítem va en el header `Location`.

> [!question]- V o F: "HATEOAS significa que las respuestas deben ser HTML".
> Falso. Significa que las representaciones, en cualquier formato (XML, JSON, HTML), incluyen links y controles para navegar a otros recursos y cambiar su estado, de modo que el cliente descubre las acciones posibles en vez de conocerlas de antemano.

> [!question]- Un error de validación del body, ¿debe ser 4xx o 5xx? ¿Por qué importa la diferencia?
> 4xx (por ejemplo, 400 o 422), porque el error es del cliente. Importa porque es un mensaje autodescriptivo: el cliente sabe que reintentar igual no sirve, mientras que ante un 5xx puede reintentar, y los intermediarios y el monitoreo distinguen fallas propias de errores de uso.
