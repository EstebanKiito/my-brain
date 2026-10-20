# Exclusión mutua distribuida — índice

Cómo garantizar que un solo nodo use un recurso compartido cuando no hay memoria común: los requisitos de safety, liveness y ordering, y tres algoritmos con distintos compromisos: servidor central, Token Ring y el multicast de Ricart y Agrawala.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (requisitos, servidor central, Token Ring y el resumen de la unidad) y completado con las slides de la clase "Exclusión mutua distribuida" y de la sesión de repaso (diagramas de cada algoritmo, Ricart y Agrawala completo, que en los apuntes quedó sin desarrollar, y la pregunta de los sensores de humo). El ejemplo de Ricart y Agrawala se reprodujo con una simulación en Python.

## Orden de estudio
1. [[01 - Exclusión mutua distribuida y servidor central|Exclusión mutua distribuida y servidor central]]: requisitos y el algoritmo con un coordinador.
2. [[02 - Algoritmo Token Ring|Algoritmo Token Ring]]: un token que circula por un anillo.
3. [[03 - Multicast de Ricart y Agrawala|Multicast de Ricart y Agrawala]]: permisos de todos ordenados por reloj lógico, y comparación de los tres.

Las imágenes de esta carpeta están en `adjuntos/`.
