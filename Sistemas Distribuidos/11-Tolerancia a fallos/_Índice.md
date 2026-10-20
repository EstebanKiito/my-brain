# Tolerancia a fallos — índice

Abre la unidad de fiabilidad: qué significa que un sistema sea confiable, cómo se encadenan fallo, error y fracaso, cómo se detectan y enmascaran las fallas con redundancia, qué límite impone el teorema FLP al consenso y qué garantías puede ofrecer un RPC cuando algo falla.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (confiabilidad y sus propiedades, métricas, fallo, error y fracaso, tipos de fracasos, detección, redundancia, teorema FLP y semánticas de RPC) y completado con las slides de la clase "Tolerancia a fallos" (ejemplo de disponibilidad con réplicas, ejemplos de fallos transitorios, intermitentes y permanentes, tipos de respuesta incorrecta, premio Dijkstra, fallos de RPC y la pregunta sobre tolerancia a fallos). Los ejemplos de disponibilidad, TMR, Hamming y semánticas de RPC se ejecutaron en Python.

## Orden de estudio
1. [[01 - Confiabilidad y sus propiedades|Confiabilidad y sus propiedades]]: disponibilidad, fiabilidad, seguridad, mantenibilidad y métricas.
2. [[02 - Fallo, error y fracaso|Fallo, error y fracaso]]: la cadena de causalidad y los tipos de fallos y fracasos.
3. [[03 - Detección de fallos y redundancia|Detección de fallos y redundancia]]: sondas, latidos y timeouts; redundancia de hardware, información, tiempo y software.
4. [[04 - Teorema de imposibilidad FLP|Teorema de imposibilidad FLP]]: por qué no se puede garantizar consenso en un sistema asíncrono.
5. [[05 - Semánticas de RPC ante fallos|Semánticas de RPC ante fallos]]: maybe, at-least-once, at-most-once y exactly-once.

Las imágenes de esta carpeta están en `adjuntos/`.
