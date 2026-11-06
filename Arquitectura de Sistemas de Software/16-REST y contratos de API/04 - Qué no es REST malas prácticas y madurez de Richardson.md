---
ramo: "Arquitectura de Sistemas de Software"
tema: "REST y contratos de API"
tags:
  - arquisis/integracion
  - arquisis/rest
  - origen/complemento
prerrequisitos:
  - "[[03 - Principios REST y restricciones de interfaz uniforme]]"
---

# Qué no es REST malas prácticas y madurez de Richardson

"API REST" se usa para casi cualquier API sobre HTTP. Esta nota separa lo que REST exige de lo que solo es costumbre, muestra las malas prácticas típicas y ordena las APIs según el **modelo de madurez de Richardson**. Termina resolviendo una contradicción entre dos reglas del propio curso.

## Lo que REST no es

- **No es un estándar de APIs web.** Es un estilo arquitectónico: un conjunto de restricciones.
- **No son APIs que retornan JSON.** Una representación puede tener muchos formatos.
- **No es un estándar para nombrar o formar URIs.** No promueve URIs anidadas ni índices incrementales.
- **No es lo mismo que CRUD.** CRUD es un patrón que REST permite (contenedor-ítem), pero un recurso puede ser un proceso, una búsqueda o un cálculo.
- **No está ligado a HTTP.** HTTP es su implementación más conocida, pero las restricciones se pueden aplicar con otros protocolos.

## Malas prácticas

| Mala práctica | Ejemplo | Por qué está mal |
|---|---|---|
| Método en la URI | `/servicio/v1/recurso?method=get`, `/servicio/v1/get_recurso` | Duplica la semántica que ya dan los verbos HTTP; los intermediarios no pueden cachear ni reintentar correctamente |
| Formato en la URI | `/servicio/v1/recurso.json` | El formato se negocia con `Accept`; la URI debe identificar el recurso, no una representación |
| URIs no opacas (URI-template) | `/servicio/v1/{id}`, `/servicio/v1/1` | El cliente construye URIs y queda acoplado. Con ids correlativos, además, cualquiera puede recorrer recursos probando números |

## El modelo de madurez de Richardson

Propuesto por Richardson (2008) y difundido por Fowler (2010). El ejemplo es una clínica donde un paciente reserva hora con un doctor.

**Nivel 0, el pantano de POX (*Plain Old XML*). No es REST.** Hay un único endpoint que escucha todas las operaciones. El intercambio depende del contenido del mensaje, los verbos se usan mal (todo es `POST`) y no hay recursos distintos. Es RPC disfrazado.

**Nivel 1, recursos. No es REST.** Los recursos se identifican con URIs separadas (`/doctors/jones`, `/slots/1234`), pero casi no se usan los verbos: se sigue mandando todo por `POST` y respondiendo `200` aunque falle.

**Nivel 2, verbos HTTP. Todavía no es REST completo.** Hay recursos con URI, verbos con su semántica y códigos de respuesta:

```http
GET /doctors/jones/slots?date=20100104&status=open HTTP/1.1
→ 200 OK  <openSlotList> slots 1234 y 5678 </openSlotList>

POST /slots/1234 HTTP/1.1
<appointmentRequest><patient id="jsmith"/></appointmentRequest>
→ 201 Created   Location: slots/1234/appointment
→ 409 Conflict  (si otro paciente tomó la hora; devuelve los slots aún libres)
```

**Nivel 3, controles hipermediales. Es REST.** Las respuestas incluyen **links** con `rel` (el tipo de acción, una URI si la define el usuario, o valores predeterminados como `self`) y `href` (la URI a seguir). Después de reservar, la respuesta dice qué se puede hacer ahora:

```xml
<appointment>
  <slot id="1234" doctor="jones" start="14" end="15"/>
  <patient id="jsmith"/>
  <link rel="/linkrels/appointment/cancel"  href="/slots/1234/appointment"/>
  <link rel="/linkrels/appointment/addTest" href="/slots/1234/appointment/tests"/>
  <link rel="self"                          href="/slots/1234/appointment"/>
</appointment>
```

| Nivel | Recursos con URI | Verbos HTTP | Códigos de estado | Hipermedia |
|---|---|---|---|---|
| 0 | – | – | – | – |
| 1 | ✔ | – | – | – |
| 2 | ✔ | ✔ | ✔ | – |
| 3 | ✔ | ✔ | ✔ | ✔ |

## El veredicto: ganó el nivel 2 con contrato

> [!tip] Nivel 3 no ganó
> En la práctica ganó el **nivel 2 más un contrato escrito** (OpenAPI). Los clientes que son programas prefieren un **esquema** conocido de antemano antes que descubrir links en ejecución. HATEOAS reaparece donde el cliente es un modelo de IA que lee en ejecución qué herramientas puede usar.

**Escenario:** si el requisito es que un proveedor nuevo se integre en poco tiempo, el nivel 2 con OpenAPI cumple la medida, y el nivel 3 también la cumple, pero cuesta más.

## La contradicción resuelta

El curso tiene dos reglas que parecen opuestas: "un recurso debe tener una URI como ID: `thing`, `thing/1`" y "mala práctica: URIs no opacas como `…/{id}` o `…/1`". **Las dos tienen razón, en niveles distintos:**
- `thing/1` es **nivel 2**: el cliente construye la URI siguiendo una **convención**, no una restricción.
- La opacidad es **nivel 3**: el cliente **recibe** la URI en un link. Es una restricción de la hipermedia.

Elegir el nivel es una decisión con costo, y un **nivel 2 bien documentado es defendible**. También es defendible romper REST cuando conviene: gRPC para comunicación interna o endpoints con forma de RPC.

> [!warning] "Es REST" en una prueba
> Si una pregunta afirma que una API "es REST" porque usa JSON y verbos HTTP, lo preciso es decir que está en el nivel 2 de Richardson. Según Fielding, sin hipermedia no es REST completo. Igual hay que aclarar que el nivel 2 es lo que se usa en la industria.

## Preguntas de repaso

> [!question]- Nombre cinco cosas que REST NO es.
> No es un estándar de APIs web, no son APIs que devuelven JSON, no es un estándar para nombrar URIs, no es lo mismo que CRUD y no está ligado a HTTP.

> [!question]- ¿Qué tiene de malo `GET /api/v1/productos.json`?
> Pone el formato en la URI. En REST, la URI identifica el recurso, y el formato de la representación se negocia con el header `Accept` y se informa con `Content-Type`. Con el formato en la URI, un mismo recurso termina con varias URIs.

> [!question]- Además del acoplamiento, ¿qué riesgo tienen las URIs con ids correlativos como `/usuarios/1`, `/usuarios/2`?
> Que cualquiera puede enumerar recursos probando números y descubrir cuántos hay o acceder a ellos si la autorización falla. Los ids opacos (UUID) o los links entregados por el servidor reducen ese riesgo.

> [!question]- Una API tiene un solo endpoint `/api` que recibe un XML con la operación y responde siempre 200. ¿En qué nivel de Richardson está?
> Nivel 0, el pantano de POX: un único endpoint para todo, los verbos y los códigos no se usan y no hay recursos separados.

> [!question]- ¿Qué agrega el nivel 3 sobre el nivel 2 y por qué no se impuso en la industria?
> Agrega hipermedia: las respuestas traen links (`rel`, `href`) con las acciones posibles, y el cliente descubre el flujo en ejecución. No se impuso porque los clientes que son programas prefieren un contrato explícito (OpenAPI) conocido de antemano, que además permite generar código.

> [!question]- Resuelva la contradicción entre "`thing/1` como ID" y "`/{id}` es mala práctica".
> `thing/1` es una convención del nivel 2: el cliente arma la URI. La opacidad es una restricción del nivel 3: el cliente recibe la URI en un link y no la construye. Ambas reglas son correctas para su nivel, y elegir el nivel 2 documentado es una decisión defendible.

> [!question]- V o F: "Una API que usa GET, POST, PUT y DELETE con sus códigos de estado correctos está en el nivel 3 de madurez".
> Falso. Eso es el nivel 2. El nivel 3 exige además controles hipermediales: links en las representaciones que indican qué se puede hacer a continuación.
