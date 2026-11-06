---
ramo: "Arquitectura de Sistemas de Software"
tema: "REST y contratos de API"
tags:
  - arquisis/integracion
  - arquisis/rest
  - origen/complemento
prerrequisitos:
  - "[[04 - Qué no es REST malas prácticas y madurez de Richardson]]"
---

# OpenAPI y límites de REST

Como en la práctica se impuso el nivel 2 de Richardson, lo que reemplazó a la hipermedia es un **contrato escrito**. **OpenAPI** es ese contrato. Esta nota explica por qué el contrato se volvió el artefacto central, y cuáles son las ventajas y las limitaciones de REST que llevan a usar otros mecanismos como gRPC o GraphQL.

## El contrato como artefacto

> [!tip] Contract-first
> **La especificación es el entregable; el servidor es el subproducto.** Primero se escribe y se revisa el contrato, y después se genera código desde él (servidor, clientes, validadores). No al revés.

Qué declara un contrato OpenAPI:
- **recursos** y operaciones;
- **esquemas** de las peticiones y las respuestas;
- **errores** posibles;
- **versionado**;
- **idempotencia** de cada operación.

```yaml
openapi: 3.1.0
info: { title: Catálogo, version: 1.2.0 }
paths:
  /productos/{id}:
    get:
      responses:
        "200":
          content:
            application/json:
              schema: { $ref: "#/components/schemas/Producto" }
        "404": { description: Producto no existe }
components:
  schemas:
    Producto:
      type: object
      required: [id, precio]
      properties:
        id: { type: string }
        precio: { type: integer }
        iva: { type: integer }
```

Por qué importa hoy:
- **Lo que un agente de IA escribe en una hora es el servidor; lo que un humano revisa es el contrato.** Revisar 40 líneas de especificación es más confiable que revisar miles de líneas generadas.
- **Escenario:** un proveedor nuevo se integra **contra el contrato, no contra el código**. Puede generar su cliente, probar contra un servidor simulado y empezar antes de que exista la implementación.
- En el context map, el contrato OpenAPI es el **Published Language** de un Open Host Service, y el contrato versionado de una relación Customer/Supplier.

## Ventajas de REST

- **Las operaciones son estándar**, así que los clientes pueden hacer supuestos seguros: un `GET` no cambia nada y un `PUT` se puede reintentar.
- **El servidor no guarda el estado de la conversación**, lo que permite una **escalabilidad masiva**: cualquier réplica atiende cualquier petición.
- **Las respuestas a `GET` se pueden cachear** en el navegador, los proxies y las CDN.
- Es web-nativo, legible por humanos y tiene herramientas en todos los lenguajes.

## Limitaciones de REST

- **Cada mensaje debe enviar toda la información necesaria** para completar la operación. Eso incluye credenciales o tokens en cada petición, lo que aumenta la superficie de exposición de información sensible.
- **Overfetching y underfetching.** Un endpoint devuelve el recurso completo aunque el cliente necesite dos campos. Para mostrar solo lo necesario hay que crear otro endpoint, o el cliente termina haciendo varias peticiones para armar una pantalla.
- **No hay una descripción estándar obligatoria.** Sin OpenAPI, el cliente depende de convenciones o tiene que "seguir su nariz" (*follow your nose*) navegando links.
- **Pensado para consumo humano** y con **overhead** sobre otros protocolos: texto, headers repetidos y conexiones HTTP. Para comunicación intensa entre servicios, REST es lento.

> [!warning] Cuándo responder "no uses REST"
> Las pautas aceptan reemplazar REST cuando el caso lo justifica:
> - **Alta velocidad o latencia mínima entre módulos** (cámaras que reportan a un servicio central, notificaciones en tiempo real) → **gRPC**, binario y tipado.
> - **Muchos servicios que deben comunicarse sin acoplarse** → **MOM**.
> - **Un frontend que necesita armar vistas con datos de muchos recursos** → **GraphQL**.
> Decir que REST "es malo" no da puntaje: hay que nombrar el atributo afectado (performance, acoplamiento, exposición de datos) y por qué la alternativa lo mejora.

> [!example]- Respuesta modelo: cámaras de un supermercado sin cajeros
> **Enunciado:** la comunicación entre las cámaras y el servicio central es prioritaria, para no perder datos ni detectar tarde los cambios. El equipo dice que REST expone muchos datos por sus endpoints y que HTTP no es lo bastante rápido. ¿Qué medida implementaría?
> **Respuesta:** cambiar el mecanismo de integración a **gRPC**. Usa Protocol Buffers (serialización binaria, más liviana que JSON), contratos estrictamente tipados que exponen solo las funciones definidas, conexiones persistentes sobre HTTP/2 y streaming bidireccional para enviar eventos continuamente. Se puede agregar TLS para la seguridad. La pauta asignaba 2 puntos a la medida y 2 a su justificación.

## Preguntas de repaso

> [!question]- ¿Qué significa que "la especificación es el entregable y el servidor el subproducto"?
> Que en contract-first el artefacto que se diseña, revisa y versiona es el contrato (OpenAPI). El código del servidor y de los clientes se genera o se valida contra él. Así los consumidores pueden integrarse contra el contrato aunque el servidor aún no exista.

> [!question]- Nombre cinco cosas que declara un contrato OpenAPI.
> Recursos y operaciones, esquemas de entrada y salida, errores posibles, versión e idempotencia de cada operación.

> [!question]- ¿Por qué la restricción stateless es a la vez una ventaja y una limitación?
> Es una ventaja porque cualquier réplica atiende cualquier petición, lo que da escalabilidad masiva y tolerancia a fallos. Es una limitación porque cada mensaje debe llevar toda la información necesaria, incluidas las credenciales: los mensajes crecen y se expone más información sensible en cada petición.

> [!question]- Explique overfetching y underfetching con un ejemplo de una app móvil.
> Overfetching: la pantalla de lista solo necesita el nombre y el precio, pero `GET /productos` devuelve descripciones y fotos de cada producto. Underfetching: la pantalla de detalle necesita el producto, el vendedor y las reseñas, y tiene que hacer tres peticiones a tres endpoints.

> [!question]- Mini caso: un sistema debe integrarse con varios sistemas vía API y además notificar en tiempo real. ¿Es REST una buena opción?
> Para las notificaciones en tiempo real, no es la mejor: cada notificación es una petición completa con overhead, y REST no ofrece streaming nativo. Conviene gRPC (streaming y binario) o un MOM con pub/sub. REST sigue siendo válido para las integraciones de consulta, justificándolo por su estándar, sus herramientas y su caché.

> [!question]- V o F: "Con un contrato OpenAPI, una API pasa a ser nivel 3 de Richardson".
> Falso. OpenAPI documenta una API de nivel 2. Es justamente la alternativa que ganó frente a la hipermedia del nivel 3: el cliente conoce el contrato de antemano en vez de descubrir links.

> [!question]- ¿Qué relación del context map formaliza un contrato OpenAPI publicado para cualquier consumidor?
> Open Host Service con Published Language: el upstream publica un protocolo y un lenguaje documentado para todos sus consumidores, y se compromete a mantenerlo estable y versionado.
