# Control de concurrencia distribuido — índice

Qué hacer cuando varias transacciones tocan los mismos datos a la vez: los tipos de conflicto y sus problemas típicos, las estrategias pesimista y optimista para evitarlos, y las políticas para resolverlos cuando se decide dejarlos ocurrir.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (conflictos, actualización perdida, lecturas inconsistentes, control pesimista con su ejemplo y control optimista) y completado con las slides de la clase "Control de concurrencia" (many readers o single writer, validación forward y backward con su ejemplo, políticas de resolución con casos reales y la pregunta del monitoreo médico). El ejemplo del precio y las dos validaciones se reprodujeron en Python.

## Orden de estudio
1. [[01 - Conflictos por concurrencia|Conflictos por concurrencia]]: lectura-escritura, escritura-escritura y sus problemas.
2. [[02 - Control pesimista y optimista|Control pesimista y optimista]]: locks, deadlocks y validación al commit.
3. [[03 - Resolución de conflictos concurrentes|Resolución de conflictos concurrentes]]: last write wins, versiones, merge, OT y CRDT.

Las imágenes de esta carpeta están en `adjuntos/`.
