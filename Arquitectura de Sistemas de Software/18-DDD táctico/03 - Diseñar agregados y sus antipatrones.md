---
ramo: "Arquitectura de Sistemas de Software"
tema: "DDD táctico"
tags:
  - arquisis/ddd
  - origen/complemento
prerrequisitos:
  - "[[02 - Agregados y raíz del agregado]]"
---

# Diseñar agregados y sus antipatrones

Dibujar agregados es fácil; dibujarlos del **tamaño correcto** es lo difícil. Si son demasiado grandes, se bloquean y se cargan enteros sin necesidad. Si no tienen comportamiento, las reglas terminan en cualquier parte. La mala modelación produce **modelos sin borde, caros de mantener y acoplados**.

## La regla: agregados chicos

> [!tip] Tamaño de un agregado
> Un agregado contiene **lo que debe ser cierto a la vez, y nada más**.
> **Test:** ¿estos dos datos cambian en la misma transacción para que una regla se cumpla?
> - **Sí** → van en el mismo agregado.
> - **No** → se dividen, y se coordinan por id y eventos.

Aplicado a Checkout:
- *¿El total y las líneas del pedido deben coincidir siempre?* Sí → mismo agregado (Pedido).
- *¿Un pedido nuevo debe actualizar al cliente en la misma transacción?* No → Cliente es otro agregado y el pedido guarda `clienteId`.
- *¿Confirmar un pedido debe descontar stock en la misma transacción?* Normalmente no: se acepta un instante de inconsistencia y Stock reacciona al evento. Si el negocio no tolera sobreventa ni por un segundo, la reserva de stock se modela con su propia regla (reservar antes de confirmar).

## Antipatrones

![Agregado gigante de Cliente con todos sus pedidos y modelo anémico con PedidoService](adjuntos/Antipatrones%20agregado%20gigante%20y%20modelo%20anémico.png)

> [!example]- Transcripción de la imagen
> - **Agregado gigante:** un recuadro **Cliente** que contiene una grilla de 18 cajas "Pedido" y la nota "+ 82 pedidos más".
> - **Modelo anémico:** un **PedidoService** con `confirmar()`, `cancelar()` y `calcularTotal()`, que hace `set` sobre un **Pedido** cuyas propiedades son `Estado { get; set; }`, `Total { get; set; }` y `Lineas { get; set; }`, con la anotación "sin comportamiento".

**1. El agregado gigante.** Cliente contiene todos sus pedidos. Para agregar un pedido hay que **cargar los 100 pedidos** del cliente. Dos compras simultáneas del mismo cliente **se bloquean** entre sí, aunque no tengan nada que ver. El agregado crece sin límite. *Solución:* Pedido es su propio agregado y guarda `clienteId`.

**2. El modelo anémico.** Las entidades son bolsas de datos con getters y setters, y las reglas viven en un `PedidoService`. Cualquier código puede hacer `pedido.Total = 0` y saltarse el invariante. Las reglas se duplican en varios servicios. *Solución:* mover el comportamiento a la entidad (`pedido.confirmar()`, `pedido.agregarLinea()`), y que los setters desaparezcan.

## Señales de un sistema que no considera DDD táctico

- **Un servicio por tabla**, con entidades de puros getters y setters, y **la regla en ninguna parte**.
- **Una transacción que toca tres agregados**: falta una frontera o falta un evento.
- **Infraestructura importada desde el dominio**: la entidad conoce el ORM, HTTP o el framework.
- No poder responder **"¿qué debe ser cierto a la vez?"**.

**Ejercicio sugerido:** tomar el código de un proyecto propio y buscar el **invariante que ningún agregado protege**. Por ejemplo, "una oferta no puede comprarse más veces que su stock" puede no estar protegido si dos peticiones concurrentes leen el mismo stock.

> [!warning] Un agregado no es una tabla
> El agregado se define por **invariantes y transacciones**, no por la estructura de la base de datos. Un agregado puede ocupar varias tablas (Pedido y LíneaPedido), y dos tablas con llave foránea pueden pertenecer a agregados distintos (Pedido y Cliente). En bases de documentos, la frontera del agregado suele coincidir con la frontera del documento.

| Diseño | Síntoma | Costo |
|---|---|---|
| Agregado gigante | Cargar o bloquear cientos de objetos para cambiar uno | Performance, concurrencia |
| Modelo anémico | Setters públicos y reglas en servicios | Invariantes rotos, reglas duplicadas |
| Agregado demasiado fino | Una regla que requiere cambiar dos agregados a la vez | Inconsistencias o transacciones múltiples |
| Agregados chicos con eventos | Una transacción por agregado | Consistencia eventual entre ellos |

## Preguntas de repaso

> [!question]- Enuncie el test para decidir si dos cosas van en el mismo agregado.
> ¿Deben cambiar en la misma transacción para que una regla se cumpla? Si la respuesta es sí, van juntas. Si es no, se separan en agregados distintos que se referencian por id y se coordinan con eventos.

> [!question]- ¿Qué problemas concretos tiene que Cliente contenga a todos sus pedidos?
> Para agregar un pedido hay que cargar todos los anteriores, dos compras simultáneas del mismo cliente se bloquean entre sí y el agregado crece sin límite. Es un problema de performance y de concurrencia sin ninguna regla que lo justifique.

> [!question]- ¿Qué es un modelo anémico y por qué rompe invariantes?
> Es un modelo donde las entidades solo tienen datos con getters y setters, y la lógica vive en servicios. Como cualquier código puede llamar a los setters, nada impide dejar el total distinto de la suma de líneas. Además, la regla se termina duplicando en varios servicios.

> [!question]- V o F: "Cada tabla de la base de datos corresponde a un agregado".
> Falso. Los agregados se definen por invariantes y transacciones. Pedido y LíneaPedido son dos tablas en un mismo agregado, mientras que Pedido y Cliente son tablas con llave foránea que pertenecen a agregados distintos.

> [!question]- Una transacción de "confirmar pedido" actualiza el pedido, el stock y los puntos del cliente. ¿Qué señal es y cómo se corrige?
> Es la señal de una transacción que toca tres agregados. Se corrige dejando que la transacción solo confirme el pedido y emita `PedidoConfirmado`. Stock y Puntos reaccionan al evento en sus propias transacciones, con consistencia eventual.

> [!question]- ¿Por qué "infraestructura importada desde el dominio" es un antipatrón?
> Porque acopla las reglas de negocio a detalles técnicos (ORM, HTTP, framework): cambiar la base de datos o el framework obliga a tocar el dominio, y probar las reglas exige levantar infraestructura. El dominio debe depender solo de sí mismo.

> [!question]- Mini caso: una tienda no puede vender más unidades de las que hay en stock, ni siquiera por un segundo. ¿Cómo afecta esto al diseño de agregados?
> La regla "stock ≥ 0" debe protegerse transaccionalmente. Una opción es que la reserva del stock sea parte de la operación del agregado Stock (reservar con verificación atómica antes de confirmar el pedido). Otra es modelar una Reserva como agregado propio. No sirve dejarlo a consistencia eventual, porque permitiría sobreventa.
