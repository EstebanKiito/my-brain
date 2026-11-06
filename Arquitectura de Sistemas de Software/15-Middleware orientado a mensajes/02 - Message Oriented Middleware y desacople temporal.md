---
ramo: "Arquitectura de Sistemas de Software"
tema: "Middleware orientado a mensajes"
tags:
  - arquisis/integracion
  - arquisis/mom
  - origen/complemento
prerrequisitos:
  - "[[01 - Monolito y comunicación indirecta entre contextos]]"
  - "[[02 - Colas de mensajes]]"
---

# Message Oriented Middleware y desacople temporal

El **Message Oriented Middleware (MOM)** fue uno de los primeros métodos de integración entre sistemas, y sigue siendo la respuesta por defecto cuando muchos sistemas deben enviarse información sin acoplarse. Su idea es simple: un middleware que **recibe mensajes y los propaga**, guardándolos en **colas** para que no se pierdan.

## Qué es

> [!tip] MOM
> Un **servidor de colas** entre clientes que toman el rol de **emisor** (*sender*) o **receptor** (*receiver*). La táctica que aplica es **usar un intermediario** para lograr **desacople temporal**: emisor y receptor no necesitan estar activos al mismo tiempo.

![Servidor MOM con colas entre emisores y receptores](adjuntos/Servidor%20MOM%20entre%20emisores%20y%20receptores.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, varios **Senders** apilados. A la derecha, varios **Receivers**.
> - Al centro, el **MOM Server** con dos colas (cilindros con mensajes adentro): los emisores escriben en ellas y los receptores leen de ellas.
> - Dentro del servidor, un **Message Handler Thread Pool**: un conjunto de hilos que procesa y entrega los mensajes.

En notación de componentes, el MOM provee una interfaz a los emisores y otra a los receptores, con multiplicidad de muchos a muchos:

```
S 1..N  —c o—  MOM (cola)  —o >—  R 1..N
```

El emisor trabaja en modo **fire and forget**: deja el mensaje y sigue con lo suyo, sin esperar a que el receptor lo procese. Pero el MOM sí se preocupa de la entrega. Como se trata de comunicación entre sistemas, **le importa saber si se pierde un mensaje**: guarda el mensaje hasta que el receptor confirma que lo recibió (*acknowledgement*). Por debajo funciona como un sistema orientado a eventos, solo que con un manejador de eventos que es una cola y que trata **mensajes** dirigidos a alguien, no eventos anunciados al aire.

**Escenario:** Checkout publica "cobrar pedido 123" en la cola y no espera a Pagos. Si el proveedor de pagos se cae, el mensaje queda guardado y Checkout no se cae con él. Cuando Pagos vuelve, procesa la cola pendiente.

| Prioriza | Cuesta |
|---|---|
| **Escalabilidad:** se agregan receptores que consumen de la misma cola | **Formato de datos acordado:** emisor y receptor deben entender el mismo mensaje |
| **Disponibilidad:** el emisor sigue operando aunque el receptor esté caído | **Complejidad** en el intercambio: reintentos, duplicados, orden, mensajes envenenados |
| **Tolerancia a fallos:** los mensajes persisten hasta que se confirman | Un componente más que operar y que puede fallar |

> [!warning] MOM no es "fire and forget" de punta a punta
> El **emisor** sí dispara y olvida. El **MOM** no: guarda el mensaje y verifica la entrega. Esa es la diferencia con un bus de eventos simple, donde un evento que nadie escucha se pierde. Si la pregunta exige no perder información, hay que nombrar la persistencia y la confirmación de entrega.

## Escalar el MOM: pub/sub, replicación y partición

Un solo servidor de colas es un cuello de botella y un punto único de falla. Para escalarlo se agregan más nodos MOM, pero eso trae los problemas típicos de distribuir:
- **Replicación:** si hay dos nodos, ambos deben manejar la misma cola, así que el contenido se replica.
- **Quórum:** para que los nodos se pongan de acuerdo en cuál es el último estado de la cola, se acepta lo que tiene **la mayoría**. Es la idea de las *quorum queues* de RabbitMQ.
- **Partición:** para escalar ante la distancia, los usuarios de Estados Unidos usan una partición y los de Sudamérica otra, sin mezclar su información.
- **Mensajería pub/sub:** orientación **1-N** (un emisor, muchos suscriptores) y **N-N**, siempre asíncrona.

![Colas de RabbitMQ en tres nodos con una partición de red](adjuntos/Quorum%20queues%20de%20RabbitMQ%20ante%20una%20partición%20de%20red.png)

> [!example]- Transcripción de la imagen
> - Tres nodos: **rabbitmq1** tiene la cola *Master*, **rabbitmq2** una copia *Mirror* y **rabbitmq3** quedó al otro lado de una línea punteada rotulada **Network partition**.
> - Productores (P, azul) y consumidores (C, verde) se conectan a rabbitmq1 y rabbitmq2. Las flechas punteadas muestran que rabbitmq2 reenvía al master.
> - rabbitmq3, aislado, tiene **su propia cola Master** con su propio productor y consumidor: dos masters a la vez, el problema de *split brain*.

Con colas espejo clásicas, el nodo aislado puede declararse master y aceptar escrituras por su cuenta, y al reconectarse hay dos historias distintas. Las **quorum queues** evitan esto con un algoritmo de consenso por mayoría (Raft): solo el lado que tiene la mayoría de los nodos sigue aceptando mensajes.

**Ejemplo de servicio administrado:** **Amazon EventBridge** conecta servicios de AWS, aplicaciones propias y SaaS mediante buses de eventos. Tiene reglas que filtran cada evento y lo envían a destinos como Lambda, SNS o APIs, un **schema registry** con el formato de los eventos y un archivo para **reproducirlos** (*replay*).

## Preguntas de repaso

> [!question]- ¿Qué significa "desacople temporal" y cómo lo logra un MOM?
> Que emisor y receptor no necesitan estar activos al mismo tiempo. El MOM guarda el mensaje en una cola: el emisor lo deja y sigue, y el receptor lo procesa cuando puede. Si el receptor está caído, el mensaje espera.

> [!question]- V o F: "En un MOM, como el emisor hace fire and forget, los mensajes pueden perderse si el receptor está caído".
> Falso. El emisor no espera, pero el MOM persiste el mensaje y solo lo da por entregado cuando el receptor lo confirma. Justamente por eso se usa en comunicación entre sistemas que no pueden perder información.

> [!question]- Nombre tres atributos que el MOM prioriza y dos costos.
> Prioriza escalabilidad (más receptores sobre la misma cola), disponibilidad (el emisor no depende del receptor) y tolerancia a fallos (los mensajes persisten). Cuesta un formato de mensaje acordado y más complejidad en el intercambio (reintentos, duplicados, orden), además de un componente más que operar.

> [!question]- ¿Qué problema muestra la figura de RabbitMQ con una partición de red y cómo lo resuelven las quorum queues?
> Muestra un *split brain*: el nodo aislado se declara master y acepta escrituras por su cuenta, así que al reconectarse hay dos historias distintas de la cola. Las quorum queues usan consenso por mayoría: solo el lado con mayoría de nodos sigue operando, y el nodo aislado deja de aceptar mensajes.

> [!question]- Mini caso: un e-commerce teme que, si el proveedor de pagos se cae, se caiga también Checkout. ¿Qué propone y qué debe mencionar para el puntaje completo?
> Un MOM entre Checkout y Pagos: Checkout encola la orden de cobro y responde al usuario "pago en proceso", y Pagos consume cuando está disponible. Hay que mencionar el desacople temporal, la persistencia con confirmación de entrega, la tolerancia a fallos, y como costos el formato acordado y la asincronía (el usuario no sabe al instante si se cobró).

> [!question]- ¿Por qué particionar un MOM por región (por ejemplo, Estados Unidos y Sudamérica) mejora la escalabilidad?
> Cada partición maneja solo el tráfico de su región, así que la carga se reparte entre nodos, la latencia baja porque el nodo está cerca y los mensajes de una región no compiten con los de otra. El costo es que una consulta que cruce regiones se vuelve más compleja.

> [!question]- Alternativas: ¿qué afirmación sobre MOM es correcta? a) Obliga a que emisor y receptor estén en línea a la vez · b) Reduce las integraciones punto a punto de $N \times M$ a $N + M$ · c) Elimina la necesidad de acordar un formato de mensaje · d) Hace que la comunicación sea sincrónica
> b). a) es justo lo contrario del desacople temporal, c) es falsa porque el formato acordado es uno de sus costos y d) es falsa porque el MOM es asíncrono.
