---
ramo: "Arquitectura de Sistemas de Software"
tema: "Resolución de casos de diseño"
tags:
  - arquisis/casos
  - origen/complemento
prerrequisitos:
  - "[[01 - Método para resolver un caso de prueba]]"
  - "[[03 - Peer to peer]]"
  - "[[02 - Teorema CAP y BASE en el diseño de datos]]"
---

# Casos O.J.O.N. y FakeIFA con P2P y consenso

Dos casos donde la clave es reconocer que **no puede haber un servidor central confiable todo el tiempo**: almacenes que quedan aislados por fallas de red (O.J.O.N., I2 2025-2) y un álbum de láminas que valida intercambios entre dispositivos por consenso (FakeIFA, I2 2026-1). Ambos piden **P2P**, **elección de líder o consenso** y **reconciliación** de estados.

## Caso O.J.O.N.: reservas de comida ante desastres

**Resumen:** unos **700 almacenes** con bodegas manejadas por robots y un inventario local. Un **HQ en la capital** autoriza las reposiciones (10 a 15 por semana por almacén). Hay un módulo de voz para llamar a las autoridades ante saqueos. Si fallan las telecomunicaciones y una región queda aislada, **debe seguir operando** y establecer **un HQ local** lo antes posible. **No puede haber 2 HQ en una red.** Los almacenes tienen conexión inalámbrica regional y siempre intentan conectarse al mayor número de almacenes posible.

**3.1.a) ¿Cómo declarar un HQ en una red aislada?**
- Un componente **P2P entre almacenes**, con el software de HQ instalado en **todos los nodos**. Cada almacén registra el estado y la ubicación de los demás.
- Al perder contacto con el HQ, un mecanismo de **elección de líder** (aleatorio, por votación o por un criterio, que hay que especificar) y un mecanismo para **evitar dos HQ**.
- **Predesignar un nodo por región da solo la mitad del puntaje**, porque las fallas de red son impredecibles: también puede fallar justo ese nodo.

**3.1.b) Datos para analítica y trazabilidad.** Una **base analítica separada de la operacional**, idealmente NewSQL o NoSQL (columnar o documental), justificada: sus necesidades de velocidad y operación son muy distintas a las de la base del día a día.

**3.1.c) Reconciliar al reconectar** (el HQ local y el central tomaron decisiones distintas).
- Estrategias: **event sourcing** (se guardan todos los eventos y se reproducen) o un sistema **tipo Git** (se detectan los conflictos y se resuelven).
- Hay que registrar las inconsistencias y **especificar cómo se resuelven** los conflictos, por ejemplo con un *overwrite* desde el HQ central.
- **Tradeoff:** se pierde disponibilidad durante el período de resolución, y la resolución de errores es compleja.

**d)** Escalabilidad, seguridad, mantenibilidad (detección de fallos) y confiabilidad. **No:** integrabilidad (los sistemas son propios e idénticos), usabilidad, portabilidad, flexibilidad.
**e)** P2P, SOA, EDA, pub/sub, pipe & filter y capas. **No:** código móvil, pizarra.

## Caso FakeIFA: álbum digital sin falsificaciones

**Resumen:** una app móvil para **comprar láminas** (pago externo y registro central en el backend), con notificaciones en tiempo real. Los **intercambios** se hacen **punto a punto** entre dispositivos, con proximidad física la primera vez y llaves para cifrado de extremo a extremo. Cada intercambio se notifica a un **subconjunto de las conexiones previas**, que lo guardan localmente **sellado con un hash**. Cada hora, un **cronjob con workers** pide esos historiales a los dispositivos y valida por **consenso de la mayoría**. Si es consistente, se guarda y se revisa si se completó el álbum; si no, se anula como fraude.

| Pregunta | Respuesta esperada |
|---|---|
| **a)** 2 medidas de escalabilidad en el backend | **Replicación** de servicios, **separación de responsabilidades** (servicios distintos para compras, notificaciones y validación) y elasticidad. 2 puntos por medida justificada |
| **b)** Registro de intercambios validados con formatos que varían según la versión de cada dispositivo: ¿base de documentos? | **Sí, es buena opción**: tolera esquemas distintos por versión. También suman alternativas como **adaptadores por versión** |
| **c)** Caché para las requests del servidor a cada dispositivo durante la validación | **NO es buena opción.** La validación necesita información **fidedigna y actual** de cada dispositivo, que puede diferir, y cachearla rompe el consenso. Alternativa: un **broker de mensajería** que reciba los mensajes de los dispositivos frente a un gatillante. 2 + 2 puntos |
| **d)** Características | Escalabilidad, disponibilidad, integrabilidad, confiabilidad, seguridad. **No:** mantenibilidad, flexibilidad, usabilidad, soporte |
| **e)** Estilos | **P2P**, EDA, pub/sub, microservicios, SOA, pipe & filter, **pizarra** (para el análisis de intercambios), bien justificados. **No:** main y subrutinas, **código móvil (no por ser app móvil)**, lotes secuenciales |

> [!tip] El patrón de estos casos
> "Sin servidor central", "nodos idénticos", "mayoría", "no pueden haber 2…" son señales de **P2P con elección de líder o consenso** (como Raft o Bully, vistos en Sistemas Distribuidos). Y cuando la red se parte, hay que hablar de **reconciliación** y del tradeoff **disponibilidad o consistencia** (CAP).

## Preguntas de repaso

> [!question]- ¿Por qué predesignar un HQ por región da solo la mitad del puntaje en O.J.O.N.?
> Porque las fallas de red son impredecibles: el nodo predesignado puede quedar aislado o fallar justo cuando se necesita. Una elección de líder dinámica entre los nodos alcanzables es más resiliente.

> [!question]- ¿Qué dos mecanismos debe tener la solución P2P de O.J.O.N.?
> Un mecanismo de elección del HQ local entre los almacenes conectados (aleatorio, votación o criterio explícito) y un mecanismo que evite que existan dos HQ en la misma red.

> [!question]- ¿Por qué la analítica va en una base separada de la operacional?
> Porque las consultas analíticas (agregaciones sobre mucha historia, trazabilidad) tienen patrones y necesidades distintos a las operaciones del día a día, y mezclarlas degradaría la base operacional. Una base columnar o NoSQL se adapta mejor a ese uso.

> [!question]- Describa una estrategia de reconciliación al reconectar y su tradeoff.
> Event sourcing: cada HQ registra eventos, y al reconectar se combinan, se detectan los conflictos y se resuelven con una regla explícita (por ejemplo, prevalece el HQ central). El tradeoff es menos disponibilidad durante la resolución y una lógica de conflictos compleja.

> [!question]- ¿Por qué la caché no sirve para la validación de intercambios en FakeIFA?
> Porque la validación por consenso necesita la información actual y fidedigna que reporta cada dispositivo. Cachear respuestas haría que el servidor validara con datos viejos o repetidos y podría aceptar fraudes. Conviene un broker que reciba los reportes ante un gatillante.

> [!question]- ¿Por qué código móvil no suma en FakeIFA aunque sea una app móvil?
> Porque el estilo código móvil implica transferir y ejecutar código en otros nodos, y aquí lo que viaja entre dispositivos son datos (láminas y registros), no código. Que la app corra en un celular no lo justifica.
