---
ramo: "Arquitectura de Sistemas de Software"
tema: "gRPC GraphQL y MCP"
tags:
  - arquisis/integracion
  - arquisis/contratos
  - origen/complemento
prerrequisitos:
  - "[[05 - OpenAPI y límites de REST]]"
  - "[[03 - Partnership Shared Kernel y Customer Supplier]]"
---

# Evolución de contratos tests de contrato y outbox

Elegir REST, gRPC, GraphQL o eventos es solo el principio. Lo difícil es **cambiar** el contrato sin romper a los consumidores. La pregunta que guía esta nota es: *si el proveedor cambia su contrato, ¿cuántos contextos se enteran?* La respuesta ideal es ninguno, y se logra con reglas de evolución, tests automáticos y publicación confiable de eventos.

## Reglas para que un contrato evolucione

1. **Cambios aditivos solamente.** Se pueden agregar campos u operaciones, pero nunca cambiar el significado o el tipo de uno existente ni quitarlo.
2. **Lector tolerante.** El consumidor ignora los campos que no conoce. Así, un campo nuevo no lo rompe.
3. **Deprecar con ventana y fecha.** Antes de quitar algo, se anuncia, se da un plazo y se monitorea quién lo sigue usando.
4. **Versionar solo cuando se rompe.** Si un cambio incompatible es inevitable, se publica una nueva versión (en el header o en el path, como `/v2/`) y se mantienen ambas durante la transición.

Estas reglas dan **compatibilidad hacia atrás** (los clientes viejos funcionan con el servidor nuevo) y **hacia adelante** (los clientes nuevos toleran respuestas de un servidor viejo). Son **la misma regla en OpenAPI, protobuf y esquemas de eventos**: en protobuf, por ejemplo, nunca se reutiliza el número de un campo borrado.

| Cambio | ¿Compatible? |
|---|---|
| Agregar el campo opcional `iva` a `Producto` | ✔ Aditivo |
| Renombrar `precio` a `price` | ✘ Rompe a quien lee `precio` |
| Cambiar `precio` de entero a string | ✘ Cambia el tipo |
| Hacer obligatorio un campo de la petición que antes era opcional | ✘ Rompe a los clientes que no lo envían |
| Agregar un valor nuevo a un enum de estados | ⚠ Solo si los consumidores son lectores tolerantes |

## Tests de contrato dirigidos por el consumidor

Con **Pact** u otras herramientas similares:
- **El consumidor declara qué usa** del contrato (qué endpoints, qué campos, qué respuestas espera).
- **El productor corre esas expectativas en su CI.**
- Si un cambio del productor **rompe el contrato, falla el build de quien lo rompe, antes de llegar a producción.**

Es el mecanismo natural de una relación **Customer/Supplier**: el cliente tiene voz y la expresa como tests ejecutables.

## Outbox: publicar eventos sin perderlos

Cuando un servicio guarda un dato y además publica un evento (por ejemplo, guarda el pedido y publica `PedidoCreado`), hay un problema de **escritura doble**:
- si guarda el dato y se cae antes de publicar, **el evento se pierde**;
- si publica primero y falla al guardar, **el evento anuncia algo que no existe**.

El **patrón outbox** lo resuelve:

```mermaid
sequenceDiagram
    participant S as Servicio de pedidos
    participant DB as Base de datos
    participant R as Relay
    participant B as Broker o log
    S->>DB: BEGIN; INSERT pedido; INSERT outbox(PedidoCreado); COMMIT
    R->>DB: lee filas nuevas de outbox
    R->>B: publica PedidoCreado
    R->>DB: marca la fila como publicada
```

El evento se escribe **en la misma transacción que el dato**, en una tabla `outbox`. Un proceso aparte, el **relay**, lee esa tabla y publica los eventos. Como la transacción es atómica, o se guardan ambos o ninguno. Si el relay se cae, reintenta, así que **los consumidores deben ser idempotentes** porque pueden recibir un evento dos veces.

## De la relación al contrato

| Relación del context map | Mecanismo | Contrato | Cómo evoluciona |
|---|---|---|---|
| Customer/Supplier | API síncrona | OpenAPI, gRPC | Negociado, con tests de contrato |
| Conformist + ACL | Cliente del API ajeno + adaptador | El de ellos | Se sufre; la ACL absorbe el cambio |
| OHS + Published Language | API pública, eventos, log | OpenAPI, AsyncAPI, esquema con registro | Aditivo, con deprecación con ventana |
| Shared Kernel | Librería, esquema compartido, `.proto` | El código compartido | Por acuerdo; releases acoplados |
| Partnership | Orquestación | Co-diseñado | Juntos |
| Separate Ways | Ninguno | Ninguno | No aplica |

## Preguntas de repaso

> [!question]- ¿Qué es un lector tolerante y por qué hace posible agregar campos sin romper a nadie?
> Es un consumidor que ignora los campos que no conoce, en vez de fallar. Si todos los consumidores son tolerantes, el productor puede agregar campos nuevos: los viejos simplemente no los leen.

> [!question]- Clasifique como compatible o incompatible: a) agregar un campo opcional · b) renombrar un campo · c) quitar un endpoint deprecado hace seis meses y sin uso.
> a) Compatible, es aditivo. b) Incompatible, rompe a quien lee el nombre antiguo. c) Es un cambio que rompe, pero aceptable si se anunció con ventana y fecha y el monitoreo muestra que nadie lo usa.

> [!question]- ¿Cómo funciona un test de contrato dirigido por el consumidor y quién falla cuando se rompe?
> El consumidor declara qué partes del contrato usa. El productor corre esas expectativas en su CI. Si un cambio del productor rompe lo que algún consumidor usa, falla el build del productor, antes de producción.

> [!question]- Explique el problema de la escritura doble y cómo lo resuelve el outbox.
> Guardar un dato y publicar su evento son dos operaciones en sistemas distintos. Si falla una de las dos, se pierde el evento o se publica uno falso. El outbox escribe el evento en una tabla de la misma base de datos, dentro de la misma transacción que el dato, y un relay lo publica después. O se guardan ambos o ninguno.

> [!question]- ¿Por qué los consumidores de un outbox deben ser idempotentes?
> Porque el relay puede publicar un evento y caerse antes de marcarlo como publicado. Al reiniciar lo publica de nuevo, así que un consumidor puede recibir el mismo evento dos veces y debe producir el mismo resultado.

> [!question]- ¿Qué relación del context map evoluciona "sufriendo el cambio" y qué componente lo absorbe?
> Conformist con ACL frente a un proveedor que no controlamos. El contrato es el del proveedor y sus cambios llegan sin negociación. La ACL absorbe el cambio, así que solo se modifica la capa de traducción y no el dominio.

> [!question]- V o F: "Para no romper clientes, cada cambio del contrato debe publicarse como una versión nueva (/v2, /v3…)".
> Falso. Se versiona solo cuando un cambio rompe la compatibilidad. Los cambios aditivos con lectores tolerantes no necesitan versión nueva, y versionar todo multiplica las versiones que hay que mantener.
