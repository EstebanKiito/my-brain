# Protocolos de replicación — índice

Cómo se replican en la práctica las escrituras entre réplicas: gossip, quórum, replicación basada en primario y replicación activa, qué consistencia logra cada uno y qué sistemas reales los usan.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Los apuntes de esta clase quedaron vacíos, así que el tema se construyó con las slides de la clase "Replicación de datos II" (los cuatro protocolos, su consistencia, ventajas, desventajas, variaciones de quórum, uso en la industria y la pregunta sobre operaciones no deterministas). La intersección de quórums y la propagación de gossip se comprobaron con simulaciones en Python.

## Orden de estudio
1. [[01 - Protocolos de replicación y gossip|Protocolos de replicación y gossip]]: qué es un protocolo de replicación y el protocolo epidémico.
2. [[02 - Replicación basada en quórum|Replicación basada en quórum]]: reglas $RQ + WQ > N$ y $WQ > N/2$, y variantes.
3. [[03 - Replicación primaria y replicación activa|Replicación primaria y replicación activa]]: un primario frente a todos activos, y uso en la industria.

Las imágenes de esta carpeta están en `adjuntos/`.
