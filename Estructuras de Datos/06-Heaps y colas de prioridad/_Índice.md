# Heaps y colas de prioridad — índice

Cómo atender por prioridad y no por orden de llegada: colas de prioridad, el heap binario guardado en un arreglo, sus operaciones en $O(\log n)$ (una de ellas implementada en C) y heapsort.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes de las clases de heaps y heapsort (colas de prioridad, árbol binario, max heap, indexación, extracción e inserción, BuildHeap y heapsort; 17 imágenes, una animación y una foto de pizarra) y en el min heap en C de la tercera ayudantía, completado con inserción y extracción. El código C se compiló y probó (0 leaks) y el Python se verificó.

## Orden de estudio
1. [[01 - Colas de prioridad|Colas de prioridad]]: el problema, las soluciones lineales y la idea de orden parcial.
2. [[02 - Heap binario y su representación en arreglo|Heap binario y su representación en arreglo]]: árbol binario, propiedad de heap, árboles casi llenos e índices $2k+1$, $2k+2$, $\lfloor (k-1)/2 \rfloor$.
3. [[03 - Inserción y extracción en un heap|Inserción y extracción en un heap]]: SiftUp, SiftDown y un min heap en C.
4. [[04 - BuildHeap y heapsort|BuildHeap y heapsort]]: construir el heap en $O(n)$, heapsort y sus propiedades.

Las imágenes de esta carpeta están en `adjuntos/`.
