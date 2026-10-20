# Replicación y modelos de consistencia — índice

Por qué se replican los datos y qué puede leer un cliente cuando hay varias copias: los modelos de consistencia fuerte, secuencial, causal y eventual, con ejemplos para distinguirlos.

Volver al [[Sistemas Distribuidos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en los apuntes de clase (por qué replicar, modelos de consistencia, secuencial, fuerte, causal y sus ejemplos) y completado con las slides de la clase "Replicación de datos" (fórmula de disponibilidad, autores y años, valores posibles bajo consistencia causal, consistencia eventual y la pregunta de los cuatro modelos). Las ejecuciones de ejemplo se comprobaron con un verificador de consistencia secuencial por fuerza bruta en Python.

## Orden de estudio
1. [[01 - Replicación de datos y modelos de consistencia|Replicación de datos y modelos de consistencia]]: beneficios de replicar, el problema y la idea de contrato.
2. [[02 - Consistencia secuencial|Consistencia secuencial]]: un mismo orden para todos.
3. [[03 - Consistencia fuerte o linealizable|Consistencia fuerte o linealizable]]: el orden del tiempo real.
4. [[04 - Consistencia causal|Consistencia causal]]: solo lo relacionado causalmente debe ordenarse.
5. [[05 - Consistencia eventual|Consistencia eventual]]: convergencia final y comparación de los cuatro modelos.

Las imágenes de esta carpeta están en `adjuntos/`.
