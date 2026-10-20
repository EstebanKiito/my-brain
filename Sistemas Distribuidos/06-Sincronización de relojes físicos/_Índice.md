# Sincronización de relojes físicos — índice

Abre la unidad de coordinación: qué significa coordinar nodos, por qué los relojes físicos se desincronizan y cómo se corrigen con tres algoritmos de complejidad creciente: Cristian (preguntar a un reloj mejor), Berkeley (promediar entre todos) y NTP (jerarquía de servidores con medición de retraso y desfase).

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (coordinación y sus tipos, sincronización de relojes, relojes físicos, Cristian, Berkeley y NTP) y completado con las slides de la clase "Coordinación y sincronización" y de la sesión de repaso de la unidad (paso a paso del ejemplo de Berkeley con su comprobación, los tres ejemplos de NTP y la pregunta sobre UTC). Los cálculos de los ejemplos se verificaron en Python.

## Orden de estudio
1. [[01 - Coordinación en sistemas distribuidos|Coordinación en sistemas distribuidos]]: los cuatro tipos de coordinación y los algoritmos que los combinan.
2. [[02 - Relojes físicos y desincronización|Relojes físicos y desincronización]]: deriva del cuarzo, relojes atómicos y por qué no se retrocede un reloj.
3. [[03 - Método de Cristian|Método de Cristian]]: estimar la hora de un servidor con el *round trip*.
4. [[04 - Algoritmo de Berkeley|Algoritmo de Berkeley]]: un líder promedia las horas de todos y envía diferencias.
5. [[05 - Protocolo NTP|Protocolo NTP]]: estratos, retraso, desfase y elección de la mejor medición.

Las imágenes de esta carpeta están en `adjuntos/`.
