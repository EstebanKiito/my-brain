---
ramo: "Arquitectura de Sistemas de Software"
tema: "DDD táctico"
tags:
  - arquisis/ddd
  - arquisis/eventos
  - origen/complemento
prerrequisitos:
  - "[[02 - Agregados y raíz del agregado]]"
  - "[[04 - Evolución de contratos tests de contrato y outbox]]"
---

# Eventos de dominio y eventos de integración

Si cada transacción toca un solo agregado, ¿cómo se entera el stock de que se confirmó un pedido? Con **eventos**. Hay dos tipos, y confundirlos es un error frecuente: el **evento de dominio** es parte del modelo interno de un contexto, y el **evento de integración** es un contrato público hacia otros contextos.

## Eventos de dominio

> [!tip] Evento de dominio
> **Algo que pasó**, nombrado **en pasado** y en el **lenguaje ubicuo** del contexto: `UserCreated`, `PedidoConfirmado`, `PagoRechazado`.

- **Lo emite el agregado cuando cambia de estado.** En `UserEntity`, cada cambio hace `addEvent(...)`.
- **Se maneja dentro del mismo contexto**: otros agregados reaccionan **después**, en su propia transacción.
- El consumo es **1-n**: varios manejadores pueden reaccionar al mismo evento. Suele implementarse con un pub/sub interno.
- **Es lo que permite tener agregados chicos**: en vez de un agregado gigante que cambia todo junto, cada uno cambia lo suyo y avisa.

```typescript
export class UserCreatedDomainEvent extends DomainEvent {
  readonly email: string;
  readonly country: string;
}

@Injectable()
export class CreateWalletWhenUserIsCreatedDomainEventHandler {
  @OnEvent(UserCreatedDomainEvent.name, { async: true, promisify: true })
  async handle(event: UserCreatedDomainEvent): Promise<void> {
    const wallet = WalletEntity.create({ userId: event.aggregateId });
    await this.walletRepo.insert(wallet);
  }
}
```

El nombre del manejador cuenta la regla del negocio: **"crear la billetera cuando se crea el usuario"**. Usuario y Billetera son agregados distintos y cada uno se guarda en su propia transacción.

## Eventos de integración

> [!tip] Evento de integración
> **El evento de dominio es modelo; el evento de integración es contrato** (un *published language*). Se publica hacia **otros contextos**, con un **esquema propio y versionado**.

![Evento de dominio traducido a evento de integración y publicado con outbox](adjuntos/Evento%20de%20dominio%20traducido%20a%20evento%20de%20integración%20con%20outbox.png)

> [!example]- Transcripción de la imagen
> - Dentro de un recuadro punteado **Contexto Pedidos**: **PedidoConfirmado** (evento de dominio) → **Traductor** (mapea al esquema público) → **Outbox** (se guarda con el pedido).
> - Desde el Outbox, una flecha "publica" hacia **PedidoConfirmado v1**, el evento de integración, resaltado fuera del contexto.
> - De ahí salen flechas hacia **Envío** e **Inventario**, los contextos consumidores.

Reglas:
- **Se traduce: nunca se expone el evento interno tal cual.** Si se publicara el evento de dominio, cualquier refactor interno rompería a los demás contextos.
- Se **versiona** (`PedidoConfirmado v1`) y evoluciona con las reglas de los contratos: cambios aditivos, lector tolerante y deprecación con ventana.
- Se publica con **outbox**: el evento se escribe en la misma transacción que el dato y un relay lo publica después.

| | Evento de dominio | Evento de integración |
|---|---|---|
| Naturaleza | Parte del modelo | Contrato público |
| Alcance | Dentro del bounded context | Entre contextos |
| Esquema | Libre, cambia con el modelo | Propio, versionado y estable |
| Transporte | Pub/sub en memoria o interno | Broker o log, con outbox |
| Ejemplo | `PedidoConfirmado` con objetos internos | `PedidoConfirmado v1` con id, total y fecha |

> [!warning] Publicar el evento interno hacia afuera
> Exponer el evento de dominio directamente a otros contextos los vuelve **Conformist** del modelo interno: cualquier cambio de nombres o estructura los rompe. El traductor es el Published Language del contexto, y protege tanto al emisor (puede refactorizar) como a los consumidores.

## Preguntas de repaso

> [!question]- ¿Cómo se nombran los eventos de dominio y por qué?
> En pasado y en el lenguaje ubicuo (`PedidoConfirmado`, `UserCreated`), porque describen un hecho que ya ocurrió en el negocio y que no se puede deshacer, no una orden.

> [!question]- ¿Por qué se dice que los eventos de dominio "permiten agregados chicos"?
> Porque un cambio que afecta a varios agregados no necesita una transacción que los toque a todos. El agregado que cambia emite un evento y los demás reaccionan después, cada uno en su transacción. Así no hace falta agrupar todo en un agregado gigante.

> [!question]- ¿Cuál es la diferencia principal entre un evento de dominio y uno de integración?
> El de dominio es parte del modelo interno y vive dentro del contexto. El de integración es un contrato público hacia otros contextos, con un esquema propio, versionado y estable, y se obtiene traduciendo el de dominio.

> [!question]- ¿Qué problema evita el traductor entre el evento de dominio y el de integración?
> Que los otros contextos se acoplen al modelo interno. Sin traductor, cada refactor interno (renombrar un campo, cambiar una estructura) rompería a los consumidores. Con traductor, el contrato público se mantiene estable.

> [!question]- ¿Por qué los eventos de integración se publican con outbox?
> Para evitar la escritura doble: si el pedido se guarda pero el evento no se publica, Envío nunca se entera, y si se publica sin guardar, se anuncia algo que no existe. El outbox guarda el evento en la misma transacción que el dato, y un relay lo publica después.

> [!question]- En el ejemplo de la billetera, ¿por qué no se crea la billetera dentro de `UserEntity.create`?
> Porque Usuario y Billetera son agregados distintos, y crear ambos en la misma operación rompería la regla de una transacción por agregado. El usuario emite `UserCreated` y un manejador crea la billetera después, en su propia transacción.

> [!question]- V o F: "Un evento de integración debe incluir el agregado completo serializado para que los consumidores tengan toda la información".
> Falso. Debe incluir solo lo que el contrato público define, con un esquema propio y estable. Serializar el agregado completo expone el modelo interno y acopla a los consumidores a su estructura.
