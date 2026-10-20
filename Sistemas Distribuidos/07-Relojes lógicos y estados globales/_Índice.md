# Relojes lógicos y estados globales — índice

Ordenar eventos sin relojes físicos y sacar una foto consistente del sistema sin detenerlo: relojes de Lamport, relojes vectoriales, estados globales con cortes consistentes y el algoritmo de Chandy-Lamport con un ejemplo completo.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (reloj lógico de Lamport con sus reglas y su ejemplo, relojes vectoriales, estados globales, corte consistente y Chandy-Lamport) y completado con las slides de las clases "Coordinación y sincronización" y "Vectores lógicos y estados globales" (paso a paso de los ejemplos, usos de un estado global, supuestos y Apache Flink). Los contadores y vectores de los ejemplos se verificaron con una simulación en Python.

## Orden de estudio
1. [[01 - Relojes lógicos de Lamport|Relojes lógicos de Lamport]]: relación "sucedió antes", reglas del contador y su límite.
2. [[02 - Relojes vectoriales|Relojes vectoriales]]: un contador por proceso, comparación y detección de concurrencia.
3. [[03 - Estados globales y cortes consistentes|Estados globales y cortes consistentes]]: para qué sirven y cuándo una foto es válida.
4. [[04 - Algoritmo de Chandy-Lamport|Algoritmo de Chandy-Lamport]]: marcadores, fases y supuestos.
5. [[05 - Ejemplo de Chandy-Lamport|Ejemplo de Chandy-Lamport]]: tres nodos, paso a paso, con mensajes en tránsito.

Las imágenes de esta carpeta están en `adjuntos/`.
