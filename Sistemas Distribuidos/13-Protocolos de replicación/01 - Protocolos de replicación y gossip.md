---
ramo: "Sistemas Distribuidos"
tema: "Protocolos de replicación"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[05 - Consistencia eventual]]"
---

# Protocolos de replicación y gossip

Los modelos de consistencia dicen **qué** se promete; los **protocolos de replicación** dicen **cómo** se cumple: qué reglas siguen los nodos para propagar las escrituras y responder lecturas. El más simple y robusto es **gossip**, que copia la forma en que se esparce un rumor (o una epidemia).

## Protocolos de replicación

Un protocolo de replicación es un conjunto de reglas que define cómo se replica la información e incluso cómo se comunican los nodos. Algunos **no son excluyentes**: se combinan para obtener ciertos beneficios. El curso estudia cuatro:

| Protocolo | Idea | Consistencia típica |
|---|---|---|
| **Gossip** | Cada nodo contagia la novedad a algunos vecinos | Eventual (causal con FIFO y vectores) |
| [[02 - Replicación basada en quórum\|Quórum]] | Leer y escribir requiere los votos de un subconjunto | Secuencial |
| [[03 - Replicación primaria y replicación activa\|Basado en primario]] | Un nodo recibe todo y propaga | Fuerte (si todo pasa por el primario) |
| [[03 - Replicación primaria y replicación activa\|Replicación activa]] | Todos procesan todo, en un orden total | Secuencial |

## Gossip

![Gossip propaga una escritura entre vecinos](adjuntos/Gossip%20propaga%20una%20escritura%20entre%20vecinos.png)

> [!example]- Transcripción de la imagen
> Una red de nodos, cada uno con su base de datos. Un cliente hace `Write(A) = 5` en un nodo de un extremo, y la escritura viaja de vecino en vecino. En el otro extremo, otro cliente hace `Read(A)` en un nodo al que la novedad quizás aún no llegó.

- También se llama **protocolo epidémico**: un nodo "infectado" con datos nuevos los propaga a sus vecinos directos, y ellos a los suyos.
- Es un enfoque **lazy** (perezoso): las réplicas intercambian periódicamente sus actualizaciones más recientes con un **subconjunto** de vecinos, no con todos.

Una simulación en Python, donde cada nodo infectado contacta a un vecino al azar por ronda, mostró que las rondas crecen de forma logarítmica: unas 8 con 16 nodos, 13 con 128 y 18 con 1024. Por eso gossip escala tan bien.

## Consistencia

- Todas las réplicas terminan con la misma información, pero sin garantías de **cuándo** ni en qué **orden**: **consistencia eventual**.
- Si los mensajes respetan **FIFO** entre nodos y se usan **relojes vectoriales**, se puede asegurar **consistencia causal**: un nodo no aplica una actualización hasta haber aplicado todas las que la causaron.

> [!example] Por qué hacen falta los vectores
> K escribe $W_K(x)=1$. F lee $x\rightarrow 1$ y escribe $W_F(x)=2$ y luego $W_F(z)=1$. S lee $z\rightarrow 1$, y después lee $x$, que debería ser 2. Pero si el $W_K(x)=1$ de K le llega a S **después** de las escrituras de F (por otro camino del gossip), S leería 1: un valor anterior a una causa que ya vio. Con relojes vectoriales, S detecta que esa escritura es anterior a lo que ya aplicó.

## Ventajas y desventajas

| Ventajas | Desventajas |
|---|---|
| Extremadamente robusto: tolera fallas de nodos | No sirve si se necesita consistencia estricta e inmediata (por ejemplo, transacciones financieras) |
| Escala a sistemas muy grandes y dinámicos | La convergencia puede tardar más de lo deseado |
| No requiere un coordinador central | Mucha redundancia de mensajes: un nodo recibe la misma novedad varias veces |
| Muy simple de implementar | |

> [!tip] Dónde se usa
> **Cassandra** y **Amazon Dynamo** usan gossip para comunicar el estado de los nodos, y **Consul** usa una variante (SWIM) para administrar los servicios de la red.

## Preguntas de repaso

> [!question]- ¿Por qué gossip escala bien a miles de nodos?
> Porque cada nodo solo habla con unos pocos vecinos por ronda, y como la cantidad de infectados se multiplica en cada ronda, la novedad llega a todos en un número logarítmico de rondas.

> [!question]- ¿Qué se necesita para que gossip ofrezca consistencia causal y no solo eventual?
> Canales FIFO entre nodos y relojes vectoriales, para que cada nodo aplique una actualización solo después de las que la causaron.

> [!question]- ¿Por qué gossip no sirve para un sistema de transferencias bancarias?
> Porque no garantiza cuándo ni en qué orden se ven las escrituras: dos réplicas podrían aceptar retiros que juntos dejan el saldo negativo antes de enterarse una de la otra.
