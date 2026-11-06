---
ramo: "Arquitectura de Sistemas de Software"
tema: "Flujo de datos e invocación implícita"
tags:
  - arquisis/estilos
  - arquisis/eventos
  - origen/complemento
prerrequisitos:
  - "[[01 - Flujo de datos por lotes y pipe and filter]]"
---

# Invocación implícita y arquitectura orientada a eventos

En vez de que un componente **llame** a otro, **anuncia** que algo pasó, y quienes estén interesados reaccionan. Esa es la **invocación implícita**, y su forma principal es la **Event-Driven Architecture (EDA)**. Es el estilo que más aparece en las soluciones de prueba, porque da desacople, escalabilidad y asincronía, y también el que más costos ocultos tiene.

## Qué es

> [!tip] Invocación implícita / EDA
> **Anuncio de eventos en lugar de invocación de métodos**, con **asincronía implícita**. El sistema **reacciona a una situación particular** y actúa según el evento. Ejemplo: enviar una oferta en una subasta online.

**Componentes clave:**
- **Listeners** (*subscribers*, *consumers*): registran su interés en algún componente y asocian métodos a eventos.
- **Producers** (*publishers*): producen contenido.
- **Canales:** transmiten la información entre productores y consumidores.
- Los listeners se registran de manera **implícita** y los métodos, de manera **explícita** en los consumidores. Las interfaces de los componentes son **métodos y eventos**.

**Conectores:** invocación explícita e implícita en respuesta a eventos.

![Producer, Event Handler y Consumer en EDA](adjuntos/Productor%20manejador%20de%20eventos%20y%20consumidor.png)

> [!example]- Transcripción de la imagen
> - Croquis "Invocación Implícita": **Producer** → **Event Handler** → **Consumer**, unidos por interfaces.
> - Debajo: "EDA (event driven arc)".

La **asincronía está del lado del productor**: el producer sigue funcionando aunque los consumidores (por ejemplo, workers) estén trabajando, y el event handler sigue reaccionando a los clientes.

## Invariantes del estilo

- **Los publicadores no conocen los efectos de sus eventos.**
- **No se asume cómo se procesará** la respuesta a un evento.
- **No se responde necesariamente a todo.**
- ***Fire and forget***.

**Datos:** suscripciones, notificaciones, *push* y *pull*. Los elementos transferidos siguen un contrato y **llevan toda la data necesaria**. **Topologías:** red, **broker** y **mediator**.

## Workers: el patrón típico del proyecto

![Productor, cola y workers que devuelven un id de trabajo](adjuntos/Productor%20cola%20y%20workers.png)

> [!example]- Transcripción de la imagen
> - Croquis "Sistema Workers": **Prod** → **Queue** → **Workers** (varios apilados).
> - Prod envía un `job` a la cola y recibe un `job_id`. Los workers preguntan "hay job" y la cola les entrega el `job id` disponible.

El productor envía el trabajo a la cola, que **devuelve un id** para consultar después el resultado. Los workers piden tareas y la cola les asigna las disponibles. El productor no espera: consulta luego por el id.

## Pros y contras

| Pros | Contras |
|---|---|
| **Reuso de componentes y evolución**: puede pasar de una app pequeña a un gran sistema | **Estructura poco intuitiva**: ¿quién le habla a quién? |
| **Reducción del acoplamiento**: flexible, modularizable, compatible con agilidad y con microservicios | **Latencia**: los eventos complejos pueden elevarla |
| **Escalabilidad y distribución elevadas**, **alto performance** | **Consistencia eventual**: hay que olvidarse de ACID entre componentes |
| **Sin integración punto a punto**: agregar consumidores es muy sencillo | **Soporte y mantenibilidad**: debugging y búsqueda de problemas difíciles |
| **Muy compatible con tiempo real**; se puede agregar request-reply y colas | **No se conoce la respuesta de los componentes** ni su orden; la entrega no está garantizada (IoT) |
| | Los componentes no permiten controlar el sistema: se necesitarían intermediarios caros y es difícil restaurar la operación |

**Problemas por la asincronía:** si se cae un consumidor, hace falta algún mecanismo de **rollback** o de reintento. Si se cae el productor, hay que ver cómo seguir consumiendo.

## Consideraciones para implementarlo

- **Establecer buenos contratos** (el esquema de cada evento).
- **Monitorear** los eventos lo más posible.
- **Idempotencia**: manejar eventos **duplicados o desordenados** sin efectos dobles.
- **Manejar errores**: responder y notificar.

> [!warning] EDA no es "más rápido" en todo
> EDA mejora el throughput y la escalabilidad, pero un flujo de varios eventos encadenados puede tener **más latencia** que una llamada directa, y es **eventualmente consistente**. Si el enunciado exige consistencia fuerte inmediata (un saldo bancario), EDA debe justificarse con cuidado.

## Preguntas de repaso

> [!question]- ¿Qué diferencia la invocación implícita de la explícita?
> En la explícita, un componente llama directamente a un método de otro. En la implícita, anuncia un evento y los componentes interesados, registrados de antemano, reaccionan sin que el emisor sepa quiénes son.

> [!question]- Nombre los cuatro invariantes de EDA.
> Los publicadores no conocen los efectos de sus eventos, no se asume cómo se procesará la respuesta, no se responde necesariamente a todo y se trabaja con fire and forget.

> [!question]- ¿Por qué la idempotencia es una consideración central en EDA?
> Porque los eventos pueden llegar duplicados (por reintentos) o desordenados. Si procesar dos veces el mismo evento tiene efectos dobles, como cobrar dos veces, el sistema queda inconsistente. Los consumidores deben producir el mismo resultado aunque reciban el evento varias veces.

> [!question]- Nombre tres ventajas y tres desventajas de EDA.
> Ventajas: bajo acoplamiento, alta escalabilidad y lo fácil que es agregar consumidores. Desventajas: estructura poco intuitiva y difícil de depurar, consistencia eventual, y desconocimiento del resultado y del orden de las respuestas.

> [!question]- ¿Cómo funciona un sistema de workers con cola?
> El productor envía el trabajo a la cola y recibe un id. Los workers toman los trabajos disponibles y los procesan. El productor consulta el resultado después con el id, sin quedarse bloqueado esperando.

> [!question]- V o F: "En EDA, el productor espera la confirmación de que el consumidor procesó el evento".
> Falso. El productor hace fire and forget: publica y sigue. No conoce el efecto del evento ni espera el procesamiento (aunque el broker pueda confirmar la recepción).

> [!question]- Mini caso: un e-commerce quiere que al confirmar una compra se actualicen inventario, puntos, correo y analítica. ¿Por qué EDA?
> Porque Checkout publica `CompraConfirmada` y cada contexto reacciona por su cuenta: se agregan consumidores sin modificar Checkout, la compra no espera a los demás y la falla de uno no bloquea al resto. El costo es la consistencia eventual y la necesidad de consumidores idempotentes y de monitoreo.
