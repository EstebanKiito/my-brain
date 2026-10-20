---
ramo: "Sistemas Distribuidos"
tema: "Protocolos de replicación"
tags:
  - sd/replicacion
  - origen/complemento
prerrequisitos:
  - "[[01 - Protocolos de replicación y gossip]]"
---

# Replicación basada en quórum

No hace falta escribir en todas las réplicas ni leer de todas. Si cada escritura llega a "suficientes" nodos y cada lectura consulta a "suficientes" nodos, toda lectura se cruza con la última escritura en al menos uno. Esa es la idea del **quórum**, la misma que hace funcionar a Paxos y Raft.

## Reglas

![Escritura y lectura con quórum](adjuntos/Escritura%20y%20lectura%20con%20qu%C3%B3rum.png)

> [!example]- Transcripción de la imagen
> Un cliente hace `Write(A) = 5`, que llega a tres de cinco réplicas: quedan con "A=5 (Versión 1)", y las otras dos siguen con "A=NIL (Versión 0)". Otro cliente hace `Read(A)` y consulta a tres réplicas, entre las que hay al menos una con la versión 1.

Sea $N$ la cantidad de nodos, $RQ$ el quórum de lectura y $WQ$ el de escritura:

- Para **leer**, se consulta a $RQ$ nodos y se elige el dato **más reciente** (la versión más alta).
- Para **escribir**, se necesita la aprobación de $WQ$ nodos.
- Si no se logra el quórum, la operación **no se ejecuta**.
- Una réplica que quiere leer puede usar su propio dato, pero igual debe respetar el quórum.

> [!tip] Las dos condiciones
> - $RQ + WQ > N$: todo quórum de lectura se **intersecta** con todo quórum de escritura, así que la lectura siempre incluye a alguien con el dato más reciente.
> - $WQ > N/2$: dos escrituras no pueden tener quórums disjuntos, lo que evita conflictos de escritura.

Una comprobación en Python con $N = 5$ probó todas las combinaciones: con $(RQ, WQ)$ igual a $(3,3)$, $(2,4)$ o $(1,5)$ siempre hay intersección, y con $(2,3)$, donde $RQ + WQ = N$, no.

## Consistencia

Asumiendo $RQ + WQ > N$:

- Se evita leer un dato inconsistente: al menos un nodo participa tanto de la lectura como de la escritura, así que siempre se obtiene el valor más reciente.
- Puede haber réplicas desactualizadas, pero el quórum las "tapa".
- Se garantiza **consistencia secuencial**.

## Ventajas y desventajas

| Ventajas | Desventajas |
|---|---|
| Muy robusto ante particiones: solo la partición que forma quórum sigue operando, lo que evita inconsistencias | Mayor latencia: cada operación espera varias respuestas |
| Tolera muchas fallas de nodos mientras se respete el quórum | Aumenta la probabilidad de no estar disponible (si no hay quórum, no se opera) |

## Variaciones

| Variante | Configuración | Efecto |
|---|---|---|
| **ROWA** (*Read-One Write-All*) | $RQ = 1$, $WQ = N$ | Lectura rapidísima, escritura lenta y frágil |
| **Majority quorum** | $RQ > N/2$ y $WQ > N/2$ | Equilibrio entre lecturas y escrituras |
| **Weighted voting** | Cada nodo tiene un **peso** y el quórum se mide en suma de pesos | Nodos más confiables pesan más |
| **Dynamic voting** | Ajusta $N$, $RQ$ y $WQ$ según los nodos activos | Sigue operando aunque caigan varios |

> [!warning] ROWA y las fallas
> Con $WQ = N$, basta que un solo nodo esté caído para que **ninguna** escritura pueda completarse.

En la práctica, **Google Spanner** usa quórum para escribir, y **Cassandra** y **Amazon Dynamo** lo usan (o una variante) para la consistencia de sus réplicas.

## Preguntas de repaso

> [!question]- ¿Por qué la regla $RQ + WQ > N$ garantiza leer el último valor?
> Porque si la suma supera $N$, ningún conjunto de lectura puede ser disjunto de uno de escritura: por el principio del palomar, comparten al menos un nodo, y ese nodo tiene la versión más reciente.

> [!question]- Con $N = 7$, ¿qué $WQ$ mínimo evita conflictos de escritura y qué $RQ$ necesitas con él?
> $WQ = 4$ (más de la mitad de 7), y $RQ \geq 4$ para que $RQ + WQ > 7$.

> [!question]- ¿Qué gana y qué pierde ROWA?
> Gana lecturas muy rápidas (basta una réplica). Pierde en escritura: hay que escribir en todas, lo que es lento y se bloquea si cualquier réplica está caída.
