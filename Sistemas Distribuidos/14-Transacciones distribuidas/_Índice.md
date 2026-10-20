# Transacciones distribuidas — índice

Transacciones que abarcan varios servidores: qué son, sus desafíos (fallas parciales, concurrencia, deadlocks distribuidos), cómo se cumplen las propiedades ACID entre nodos y los protocolos de commit de dos y tres fases.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (definición, ejemplo de transferencias y comandos) y completado con las slides de la clase "Transacciones distribuidas", ya que los apuntes quedaron incompletos (desafíos, serializabilidad de una copia, transacciones anidadas, ACID y cómo cada comando puede violarlas, 2PC, 3PC y la pregunta sobre los protocolos). Los escenarios de 2PC y 3PC se simularon en Python.

## Orden de estudio
1. [[01 - Transacciones distribuidas y sus desafíos|Transacciones distribuidas y sus desafíos]]: comandos, desafíos, serializabilidad de una copia y transacciones anidadas.
2. [[02 - Propiedades ACID en transacciones distribuidas|Propiedades ACID en transacciones distribuidas]]: cada propiedad entre nodos y cómo se viola.
3. [[03 - Commit de dos fases|Commit de dos fases]]: votación, consolidación y el estado incierto.
4. [[04 - Commit de tres fases|Commit de tres fases]]: pre-commit, decisión entre participantes y comparación con 2PC.

Las imágenes de esta carpeta están en `adjuntos/`.
