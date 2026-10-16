# Árboles balanceados — índice

Cómo garantizar altura $O(\log n)$ en un árbol de búsqueda: los AVL, que rebalancean con rotaciones; los árboles 2-3, que nunca se desbalancean gracias a los nodos múltiples y al split; y los rojo-negro, que representan un 2-4 dentro de un árbol binario.

Volver al [[Estructuras de Datos/_Índice|mapa del ramo]].

> [!note] Origen
> Basado en mis apuntes de las clases de AVL, árboles 2-3 y rojo-negro (definiciones, rotaciones simples y dobles, ejemplo de inserciones en AVL, inserciones con split en 2-3, equivalencia rojo-negro/2-4; 37 imágenes). El ejemplo de inserciones en AVL se recalculó con una implementación en Python, y la recurrencia de nodos mínimos se verificó numéricamente.

## Orden de estudio
1. [[01 - Árboles AVL y propiedad de balance|Árboles AVL y propiedad de balance]]: definición, balance $\pm 1$, por qué basta corregir el primer desbalance y altura tipo Fibonacci.
2. [[02 - Rotaciones simples y dobles en AVL|Rotaciones simples y dobles en AVL]]: X, Y, Z, el caso exterior y el cambio de dirección, y el ejemplo M, D, H, B, A, C, S, K, I.
3. [[03 - Árboles 2-3|Árboles 2-3]]: nodos 2 y 3, búsqueda, inserción con split y crecimiento desde la raíz.
4. [[04 - Árboles rojo-negro|Árboles rojo-negro]]: representación de nodos múltiples con colores, las 4 propiedades, la equivalencia con 2-4 y la inserción.

Las imágenes de esta carpeta están en `adjuntos/`.
