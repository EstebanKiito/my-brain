# Consenso — índice

Cómo logran varios nodos acordar una misma operación aunque algunos fallen: las propiedades de un algoritmo de consenso, Paxos fase por fase con sus casos borde y garantías, y el problema de los generales bizantinos, en que algunos nodos mienten.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (propiedades, algoritmos, Paxos con sus fases, casos borde y garantías, generales bizantinos con mensajes orales y firmados) y completado con las slides de la clase "Consenso" (historia de Paxos, ejemplos paso a paso, uso real de Paxos, pBFT, Proof of Work, Proof of Stake y la pregunta sobre Paxos). Los ejemplos de Paxos y de mensajes orales se reprodujeron con simulaciones en Python.

## Orden de estudio
1. [[01 - Algoritmos de consenso|Algoritmos de consenso]]: el problema, propiedades deseables y algoritmos conocidos.
2. [[02 - Paxos: roles y fase de preparación|Paxos: roles y fase de preparación]]: proponentes, aceptantes y aprendices, y la fase prepare.
3. [[03 - Paxos: aceptar y aprender|Paxos: aceptar y aprender]]: qué operación se envía y cuándo se consolida.
4. [[04 - Casos borde y garantías de Paxos|Casos borde y garantías de Paxos]]: interrupción, sobrescritura, livelock, fallas y particiones.
5. [[05 - Problema de los generales bizantinos|Problema de los generales bizantinos]]: nodos traidores, mensajes orales y firmados, y casos reales.

Las imágenes de esta carpeta están en `adjuntos/`.
