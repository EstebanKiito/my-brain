# Elección de líder — índice

Cómo un grupo de nodos acuerda quién asume un rol especial y cómo lo reemplaza si cae: los algoritmos Bully y Ring-based, y Raft, que elige un líder democráticamente para luego lograr consenso replicando un log.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (propiedades de safety y liveness, Bully, Raft con estados, term, elección, sus cuatro casos, heartbeats, replicación y consolidación) y completado con las slides de la clase "Elección de líder" (Bully paso a paso y su costo, Ring-based, ejemplo de consolidación directa e indirecta con 5 nodos, uso real de Raft y la pregunta sobre consolidación). Las reglas de votación de Raft y los conteos de mensajes se verificaron en Python.

## Orden de estudio
1. [[01 - Elección de líder y algoritmo Bully|Elección de líder y algoritmo Bully]]: propiedades de una elección y el algoritmo del "matón".
2. [[02 - Algoritmo Ring-based|Algoritmo Ring-based]]: elección en un anillo donde cada nodo conoce solo a su vecino.
3. [[03 - Raft: estados y elección del líder|Raft: estados y elección del líder]]: seguidor, candidato y líder, term, postulación, votación y heartbeats.
4. [[04 - Casos de votación en Raft|Casos de votación en Raft]]: cuatro elecciones paso a paso.
5. [[05 - Raft: replicación y consolidación de logs|Raft: replicación y consolidación de logs]]: replicación, consolidación directa e indirecta, y garantías.

Las imágenes de esta carpeta están en `adjuntos/`.
