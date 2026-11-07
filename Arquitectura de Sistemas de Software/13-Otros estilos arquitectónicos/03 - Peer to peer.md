---
ramo: "Arquitectura de Sistemas de Software"
tema: "Otros estilos arquitectónicos"
tags:
  - arquisis/estilos
  - origen/complemento
prerrequisitos:
  - "[[03 - Máquinas virtuales y cliente-servidor]]"
  - "[[01 - Redes P2P, búsqueda y ataques]]"
---

# Peer to peer

Cliente-servidor tiene un punto único de falla: el servidor. **Peer to peer (P2P)** lo elimina haciendo que **todos sean servidores**. Es el estilo de BitTorrent y Bitcoin, y aparece en las pruebas cuando el enunciado dice "sin servidor central", "nodos idénticos" o "comunicación entre dispositivos cuando no hay conexión".

## Descripción

> [!tip] P2P
> Estilo **totalmente descentralizado**, con **flujos de control y recursos distribuidos entre pares**. Los **peers** son máquinas idénticas que actúan **a la vez como cliente y como servidor**, **sin un componente central**.

- **Componentes:** peers **autoorganizados**, independientes, cada uno con su propio estado y su propio hilo de ejecución.
- **Conectores:** protocolos de red.
- **Datos:** mensajes de red y blobs.
- **Topología:** conexiones de par a par con **interfaces idénticas**. Puede haber redundancia y no hay regulación en la cantidad ni la duración de las conexiones. Es computación descentralizada, se puede componer con otros estilos y admite muchas formas de organizarse.

En UML, cada peer **provee y requiere** las mismas interfaces: puede enviar y recibir.

![Cliente-servidor frente a P2P](adjuntos/Cliente%20servidor%20frente%20a%20P2P.png)

> [!example]- Transcripción de la imagen
> - Arriba a la izquierda, **Client-server**: un nodo central con varios nodos conectados solo a él.
> - Arriba a la derecha, **P2P**: todos los nodos conectados con todos, con la anotación "clientes y servidores a la vez".
> - Abajo, tres **Peer** conectados entre sí, cada uno proveyendo y requiriendo interfaces de los otros.

## Tipos y ejemplos

| Tipo | Ejemplo |
|---|---|
| **No estructurado** | BitTorrent en sus inicios |
| **Estructurado** (topología y organización predeterminadas) | Bitcoin |
| **Híbrido** | BitTorrent con trackers y DHT; versiones iniciales de Spotify y Skype |

Otro ejemplo es Folding@Home, que usa los computadores de voluntarios para simular el plegamiento de proteínas.

## Pros y contras

| Pros | Contras |
|---|---|
| **Redundancia**: beneficia la disponibilidad | **Complejidad**: requiere protocolos para caídas y reinserción de nodos |
| **Tolerancia a la caída de nodos**: si se cae uno, el resto sigue | **Seguridad**: todos los peers tienen acceso a la red; **cada uno puede ser el eslabón más débil** |
| **Escalabilidad**: los nodos entran con facilidad; las tablas de hash distribuidas (DHT) ayudan a encontrar recursos | **Confiabilidad y durabilidad**: en escenarios de escasez (archivos distribuidos) pueden perderse trozos o archivos completos |
| **Performance** | **La consistencia se ve afectada** (es la excepción a la redundancia) |
| En algunos casos, **transparencia y anonimato** | |

> [!example]- Cuándo usarlo en una prueba
> - **Almacenes aislados que deben elegir un HQ local** cuando se cae la red nacional: un componente P2P entre almacenes, con un mecanismo de designación de líder (aleatorio, por votación o por criterio) y uno para evitar dos HQ. La pauta da solo la mitad del puntaje si se predesigna un nodo por región, porque las fallas de red son impredecibles.
> - **Robots o sondas que se comunican entre sí** y se reenvían datos hasta llegar al satélite.
> - **VoltVecino:** nodos idénticos que negocian energía sin servidor central.
> Las pautas lo marcan como **no válido** cuando "todos los sistemas son distintos": P2P exige pares equivalentes.

## Preguntas de repaso

> [!question]- ¿Qué es un peer y en qué se diferencia de un cliente o un servidor?
> Un peer es un nodo idéntico a los demás que actúa a la vez como cliente y como servidor: consume y ofrece recursos. En cliente-servidor los roles son asimétricos y hay un servidor central.

> [!question]- ¿Qué problema de cliente-servidor resuelve P2P y a qué costo?
> Elimina el punto único de falla del servidor central: si cae un peer, el resto sigue funcionando. El costo es la complejidad (protocolos de entrada y salida de nodos), la consistencia (cada peer puede tener un estado distinto) y la seguridad (cada peer es un posible eslabón débil).

> [!question]- Dé un ejemplo de P2P no estructurado, estructurado e híbrido.
> No estructurado: BitTorrent en sus inicios. Estructurado: Bitcoin. Híbrido: BitTorrent con trackers y DHT, o las primeras versiones de Spotify y Skype.

> [!question]- ¿Por qué la consistencia es "la excepción" a la redundancia en P2P?
> Porque los datos replicados en muchos peers dan disponibilidad, pero mantenerlos idénticos es difícil: los peers entran y salen y se comunican sin coordinador, así que distintos peers pueden tener versiones distintas.

> [!question]- Mini caso: una red de almacenes queda aislada del HQ central por fallas de red y debe seguir operando con un HQ local. ¿Qué estilo propone y qué falta especificar?
> P2P entre los almacenes, con el software de HQ instalado en todos los nodos y el estado de la red registrado en cada uno. Falta especificar el mecanismo de elección de líder (votación, criterio o aleatorio) y cómo evitar que existan dos HQ a la vez.

> [!question]- V o F: "P2P es adecuado para conectar un frontend, un sistema de pagos y una base de datos".
> Falso. P2P exige pares equivalentes que compartan el mismo rol. Componentes con funciones distintas no son peers, y las pautas lo marcan como no válido en ese caso.

> [!question]- ¿Qué aporta una DHT a un sistema P2P?
> Permite encontrar en qué peer está un recurso sin un índice central: la tabla de hash se reparte entre los peers, lo que ayuda a escalar.
