---
ramo: "Arquitectura de Sistemas de Software"
tema: "Flujo de datos e invocación implícita"
tags:
  - arquisis/estilos
  - arquisis/eventos
  - origen/complemento
prerrequisitos:
  - "[[02 - Invocación implícita y arquitectura orientada a eventos]]"
  - "[[03 - Sistemas publish-subscribe]]"
---

# Topologías mediator y broker y el estilo pub sub

EDA se puede organizar de dos formas: con un **mediador** que dirige el flujo (**orquestación**) o con un **broker** que solo transporta eventos y deja que cada componente sepa su parte (**coreografía**). **Pub/sub** es la variante más simple: publicar mensajes a quien le interese. Saber cuál usar y qué cuesta cada una es pregunta segura.

## Topología mediator (orquestación)

- Un **ente centralizado** capaz de movilizar un proceso: toma los eventos y los **mueve entre los procesadores de eventos**.
- Se usa **cuando se necesita control del flujo**: una orquesta necesita un director.
- **Puede tener comportamiento síncrono**: el mediador espera a que un consumidor termine para seguir con el siguiente paso.
- **Efecto secundario interesante: trazabilidad simplificada**, porque todo pasa por él.
- Cuando se habla de un mediator, se habla de un **bus de eventos**.

**Ejemplos:** Apache Camel, Temporal, Apache Airflow, Django signals, AWS Step Functions y el patrón SAGA.

> [!example]- El mediator hoy: el bus de eventos gestionado
> El ESB de SOA no desapareció: **se descompuso en piezas gestionadas**, cada una "tonta" por separado.
> - **Router de eventos:** AWS EventBridge, Azure Event Grid, Google Eventarc. Reglas por atributos, fan-out, schema registry, archivo y replay.
> - **Broker:** Azure Service Bus, Amazon SQS/SNS, Google Pub/Sub, RabbitMQ. Transporta y entrega.
> - **Orquestador:** Step Functions, Logic Apps, Google Workflows, Temporal. El proceso queda **fuera del bus**, y es opcional.
> - **Transformación:** EventBridge Pipes, input transformers. Cambian la forma del sobre, no el dominio.
> Son las mismas capacidades que el ESB, pero con la lógica en los **endpoints**, no en el medio. **Regla:** enrutar por **atributos** del evento es un *dumb pipe*; decidir por el **significado** del evento es lógica de negocio y va en un servicio.

## Topología broker (coreografía)

- Una **entidad dedicada a enviar mensajes y cumplir las entregas**. **No orquesta** los eventos, **solo los mueve**.
- Es el intermediario necesario para sostener muchas arquitecturas de eventos. **Ojo con el SPOF.**
- Puede usar un protocolo (AMQP, XMPP).
- En la coreografía **todos se saben la coreografía**: cada consumidor sabe qué hacer y **puede convertirse en productor** del siguiente evento. Los pasos pueden ejecutarse en paralelo.

**Ejemplos:** RabbitMQ (muchos productores generan mensajes a muchos canales que llegan a suscriptores específicos), Mosquitto, Redis, ejabberd y AWS SNS.

![Topología broker con canales de eventos y procesadores](adjuntos/Topología%20broker%20de%20EDA%20con%20canales%20de%20eventos.png)

> [!example]- Transcripción de la imagen
> - Un **Initiating Event** entra a un **Event Channel** del broker (la columna central con varios canales).
> - Cada canal entrega a un **Event Processor** (con varios componentes internos). El procesador, al terminar, emite un **Processing Event** a otro canal, que lo entrega a otro procesador, y así sucesivamente.

| | Mediator | Broker |
|---|---|---|
| Control del flujo | Centralizado | Distribuido entre los consumidores |
| Trazabilidad | Simple | Difícil |
| Acoplamiento | Todos dependen del mediador | Bajo |
| Riesgo | SPOF y cuello de botella | Pérdida de visibilidad; el broker también puede ser un SPOF |
| Quantas | Tiende a 1 (si cae el mediador, cae el flujo) | **N**: fire and forget, cada uno funciona aunque otro caiga |

## Pub/sub

> [!tip] Publisher/subscriber
> Variante de EDA: los **publishers envían mensajes sin apuntar a suscriptores específicos**, y los **suscriptores escuchan** solo lo que les interesa. Se puede organizar en **tópicos**, y los mensajes se envían de forma **indirecta**.

A diferencia del broker de EDA, en pub/sub no se envían eventos a los que un consumidor reacciona para continuar un flujo: el publicador **publica desinteresado** y los suscriptores hacen algo con el mensaje. Es el estilo más simplificado de EDA.

**Ejemplos:** RSS, chats y juegos (XMPP), IoT (**MQTT**), e-commerce (eventos críticos, stock), envío de correos y notificaciones.

**MQTT** (*MQ Telemetry Transport*): fácil de escalar, de configuración mínima, conexión simple y ligera, con soporte de QoS, sobre TCP/IP. Es el estándar en IoT. En el proyecto del curso, más de 150 suscriptores se conectan al broker y pueden publicar en los canales permitidos.

**Funcionamiento con confirmaciones:** el publicador envía un mensaje y el broker responde con un *ack*; el broker reenvía al suscriptor y este responde con su *ack*. Todo sigue siendo asíncrono, y el ack le sirve al broker para continuar.

| Pros | Contras |
|---|---|
| Ventajas de EDA: **desacoplamiento** (cualquiera puede entrar a un tópico) | **Mensajería confiable**: ¿cómo asegurar que llegue? Hace falta **QoS** (al menos una vez, exactamente una vez) |
| **Asincronía**: fire and forget, aunque el suscriptor puede esperar un evento | **Seguridad**: sin control de acceso (RBAC, CBAC), cualquiera podría escuchar |
| **Escalable**: aprovecha el broadcasting | **Complejidad**: los tópicos y contenidos pueden enredarse |

> [!example]- V/F de prueba: "Características de pub/sub"
> - "Los suscriptores siempre responden al publicador" → **Falso**: un logger, por ejemplo, no responde a cada mensaje.
> - "No tiene límites de escalabilidad al usar un broker" → **Falso**: un solo broker puede no bastar y necesitar clustering.
> - "Es posible que se pierdan mensajes" → **Verdadero**: depende de la QoS.
> - "Los mensajes deben ser muy detallados y pesados" → **Falso**: se privilegian mensajes pequeños y ligeros, como en MQTT.
> - "Es muy flexible a cambios de estructura de los mensajes" → **Falso**: cambiar la estructura obliga a actualizar a todos los clientes.

## Preguntas de repaso

> [!question]- ¿Qué gana y qué pierde EDA con topología mediator frente a broker?
> Con mediator gana control del flujo y trazabilidad simple, pero el mediador es un SPOF y un cuello de botella, y todos dependen de él. Con broker gana desacople, escalabilidad y N quantas, pero pierde visibilidad: es difícil saber dónde falló un flujo.

> [!question]- ¿Qué distingue a pub/sub del broker de EDA?
> En pub/sub, el publicador emite mensajes por tópico sin esperar que alguien continúe un flujo, y los suscriptores interesados solo los consumen (notificaciones, IoT). En el broker de EDA, los eventos encadenan procesamiento: cada consumidor reacciona y puede emitir el siguiente evento.

> [!question]- Nombre tres ejemplos de mediator y tres de broker.
> Mediator: Apache Camel, Temporal, AWS Step Functions (también Airflow y SAGA). Broker: RabbitMQ, Mosquitto y AWS SNS (también Redis y ejabberd).

> [!question]- ¿Qué regla separa un "dumb pipe" de la lógica de negocio en un bus de eventos moderno?
> Enrutar por atributos del evento (tipo, región) es un dumb pipe aceptable en el bus. Decidir según el significado del evento (si un pedido requiere revisión) es lógica de negocio y debe ir en un servicio.

> [!question]- V o F: "En pub/sub nunca se pierden mensajes porque el broker los gestiona".
> Falso. Según la implementación y la QoS configurada, los mensajes pueden perderse (por ejemplo, con QoS 0 en MQTT o si nadie está suscrito).

> [!question]- ¿Por qué EDA con broker suele tener N quantas?
> Porque el productor hace fire and forget y cada consumidor funciona de forma independiente: si un consumidor cae, el productor y los demás siguen operando.

> [!question]- Mini caso: miles de sensores IoT reportan lecturas y varios sistemas las consumen. ¿Qué estilo y protocolo propone?
> Pub/sub con MQTT: los sensores publican por tópico, los sistemas interesados se suscriben, el protocolo es liviano y soporta QoS. Hay que considerar un broker en cluster para escalar y control de acceso a los tópicos por seguridad.
