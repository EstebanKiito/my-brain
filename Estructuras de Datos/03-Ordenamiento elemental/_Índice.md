# Ordenamiento elemental — índice

Los algoritmos de ordenación cuadráticos que atacan el problema de frente: selection sort e insertion sort, el análisis exacto de insertion sort con inversiones y las propiedades (estabilidad, in place, adaptatividad) con las que se comparan todos los algoritmos de ordenación.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes de las clases de selection e insertion sort (con 9 imágenes y animaciones) y en la parte de sorting de la primera ayudantía (versiones in place, ejercicio de sublistas y 2 fotos de la pizarra, giradas para que se lean). Se completó con las slides de selection sort e insertion sort, y la demostración del caso promedio y el ejemplo de estabilidad se verificaron en Python.

## Orden de estudio
1. [[01 - Ordenar para buscar y selection sort|Ordenar para buscar y selection sort]]: por qué ordenar, la versión in place y su costo $\Theta(n^2)$.
2. [[02 - Insertion sort|Insertion sort]]: insertar en la parte ordenada, el costo de insertar y la versión in place.
3. [[03 - Inversiones y análisis de casos de insertion sort|Inversiones y análisis de casos de insertion sort]]: $O(n + k)$, mejor, peor y caso promedio, y el ejercicio de las $n/k$ sublistas.
4. [[04 - Propiedades de los algoritmos de ordenación|Propiedades de los algoritmos de ordenación]]: estable, in place, adaptativo, online, y cuándo usar cada algoritmo.

Las imágenes de esta carpeta están en `adjuntos/`.
