# Administración de memoria — índice

Conceptos fundamentales de gestión de memoria principal (RAM) en sistemas operativos modernos. Análisis de la memoria como arreglo lineal de bytes, el impacto de la multiprogramación y la inviabilidad de las direcciones absolutas frente a las relativas. Formulación de los dos desafíos clave: relocalización dinámica y protección de memoria frente a accesos indebidos (*Segmentation Fault*). Mecanismo clásico de registros Base y Límite implementado en la MMU (*Memory Management Unit*). Técnicas de sobrecarga de memoria mediante intercambio (*swapping*) con almacenamiento secundario, caracterización de la fragmentación externa y algoritmos de asignación libre de particiones contiguas (First Fit, Best Fit, Worst Fit) versus compactación. Introducción a la segmentación del espacio de direcciones (código, heap, stack), validación de límites, prevención de desbordes y cálculo de direcciones mediante aritmética y máscaras de bits.

Volver al [[Sistemas Operativos y Redes/_Índice|mapa del ramo]].

> [!note] Origen
> Notas elaboradas a partir de la Clase 6 de los apuntes originales de Sistemas Operativos, complementadas con las diapositivas oficiales de `Contenido_6_Memoria.pdf` y la literatura estándar de sistemas operativos (Silberschatz et al., OSTEP).

## Orden de estudio

1. [[01 - Coordinación de filósofos y manejo de estados con semáforos|Coordinación de filósofos y manejo de estados con semáforos]]: repaso de primitivas de sincronización y análisis detallado de la solución con estados (`THINKING`, `HUNGRY`, `EATING`) y semáforos privados para evitar inanición y deadlocks.
2. [[02 - Memoria principal y el desafío de la multiprogramación|Memoria principal y el desafío de la multiprogramación]]: estructura de la RAM como arreglo lineal de bytes, unidades de medida ($2^{10}$ B = 1 KB, $2^{20}$ B = 1 MB, $2^{30}$ B = 1 GB), y por qué las direcciones absolutas fallan al ejecutar múltiples procesos simultáneos.
3. [[03 - Relocalización, protección de memoria y registros base y límite|Relocalización, protección de memoria y registros base y límite]]: problemas duales de relocalización y aislamiento, direcciones virtuales vs. físicas, arquitectura de registros Base y Límite en la MMU y detección de desbordes (*Segmentation Fault*).
4. [[04 - Swapping, fragmentación externa y algoritmos de asignación libre|Swapping, fragmentación externa y algoritmos de asignación libre]]: mecanismo de intercambio (*swap-in* / *swap-out*) gestionado por el planificador de mediano plazo, generación de huecos de memoria, inviabilidad de la compactación y políticas de colocación contigua (First Fit, Best Fit, Worst Fit).
5. [[05 - Segmentación de memoria y prevención de segmentation fault|Segmentación de memoria y prevención de segmentation fault]]: descomposición del espacio lógico en segmentos autónomos (código, heap, stack), estructura de la tabla de segmentos con bases y límites, y cálculo del desplazamiento relativo para evitar desbordes.
6. [[06 - Aritmética de bits y máscara de segmento en traducción de direcciones|Aritmética de bits y máscara de segmento en traducción de direcciones]]: división binaria de la dirección virtual en selector de segmento y offset, evaluación de capacidades de direccionamiento, y uso de máscaras a nivel de bits con operadores AND y desplazamiento a la derecha.

