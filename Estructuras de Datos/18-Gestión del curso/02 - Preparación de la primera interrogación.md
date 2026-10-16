---
ramo: "Estructuras de Datos"
tema: "Gestión del curso"
tags:
  - edd
  - gestion-del-curso
  - repaso
  - origen/complemento
prerrequisitos:
  - "[[04 - BuildHeap y heapsort]]"
  - "[[04 - Árboles rojo-negro]]"
---

# Preparación de la primera interrogación

La primera interrogación cubre **algoritmos de ordenación, heaps, ordenamiento lineal y árboles de búsqueda**. Las preguntas rara vez piden recitar un algoritmo: piden **modificar** uno existente, **mejorarlo**, **diseñar** uno nuevo con las ideas vistas, decir **qué hace**, o demostrar su **correctitud** y **complejidad**. Por eso hay que entender el pseudocódigo, no memorizarlo.

> [!tip] Objetivos evaluados
> Comprender y comparar los algoritmos clásicos de ordenación; modificarlos para resolver problemas; diseñar algoritmos con las técnicas estudiadas; demostrar correctitud y complejidad; y comprender y comparar estructuras basadas en árboles.

## Ordenación: la idea de cada algoritmo

| Algoritmo | Mnemotecnia | Lo que suelen preguntar |
|---|---|---|
| [[01 - Ordenar para buscar y selection sort\|Selection sort]] | "Selecciona ordenado": busca el menor y lo pone en la salida | No distingue un arreglo ya ordenado: siempre $O(n^2)$. Sirve sin memoria adicional |
| [[02 - Insertion sort\|Insertion sort]] | "Inserta ordenado": toma un elemento y busca su lugar hacia atrás | Mejor caso $O(n)$; el costo depende de las inversiones |
| [[02 - Mergesort y su recurrencia\|Mergesort]] | Mezcla mitades ordenadas recursivamente | Corrige varias inversiones a la vez; hay que dominar la **ecuación de recurrencia** (suelen dar un algoritmo "perversamente parecido") |
| [[03 - Quicksort\|Quicksort]] | Ordena haciendo que todos sean pivotes | Peor caso $O(n^2)$; mejoras: insertion sort para $n \le 20$, mediana de 3, partición en 3 (con dos pivotes) |
| [[04 - BuildHeap y heapsort\|Heapsort]] | Selection sort con un heap | $O(n \log n)$ siempre, no estable |
| [[02 - Radix sort LSD y MSD\|Counting y radix]] | Categorizar en vez de comparar | Requieren un rango acotado; si el rango supera mucho a $n$, dejan de ser lineales. Atención a cuál es el dígito más o menos significativo |

> [!warning] Restricciones del enunciado
> Si el enunciado dice que **no hay memoria adicional**, mergesort deja de ser eficiente (el merge in place es $O(n^2)$). Leer las restricciones decide qué algoritmo conviene.

## Heaps: las preguntas típicas

- Casi siempre aparecen como **cola de prioridad**: pacientes por gravedad, aviones por combustible.
- Para no duplicar datos, conviene un **heap de índices** que apunte a los datos originales.
- **Convertir un max heap en un min heap en menos de $O(n \log n)$**: basta con **BuildHeap**, que es $O(n)$ y funciona sobre cualquier arreglo.
- ¿Se puede modificar un heap para que maneje **dos prioridades**? ¿Y hacer **estable** un algoritmo, por ejemplo para usarlo dentro de radix sort? Son variaciones frecuentes.
- Frente a una cola FIFO, el heap es más lento ($O(\log n)$ en vez de $O(1)$). No sirve para ordenar por llegada.

## Árboles

- [[03 - Eliminación en un ABB|ABB]]: búsqueda, inserción y eliminación en $O(h)$; el peor caso es una lista.
- [[02 - Rotaciones simples y dobles en AVL|AVL]]: insertar una secuencia y aplicar las rotaciones. Es pregunta de prueba frecuente.
- [[03 - Árboles 2-3|2-3]]: lo fácil es insertar un nodo; lo difícil, escribir el pseudocódigo de la inserción. Para listar sus nodos en orden, el in-order cambia solo con un `if` para el 3-nodo.
- [[04 - Árboles rojo-negro|Rojo-negro]]: revisar si un árbol dado cumple las propiedades y corregirlo; pasar de rojo-negro a 2-4 y viceversa.

> [!example] Para el informe o "torpedo"
> Tener a mano los pseudocódigos para poder modificarlos, junto con las estrategias para demostrar correctitud (que termina y que hace lo pedido) y para calcular complejidad.

## Preguntas de repaso

> [!question]- ¿Cómo se convierte un max heap en un min heap en $O(n)$?
> Aplicando BuildHeap con la comparación de mínimos sobre el mismo arreglo: funciona sobre cualquier arreglo de entrada y cuesta $O(n)$.

> [!question]- ¿Por qué mergesort deja de ser buena opción si no hay memoria adicional?
> Porque su merge eficiente necesita una secuencia auxiliar $O(n)$. La versión in place cuesta $O(n^2)$ por merge.

> [!question]- Nombrar tres mejoras de quicksort y qué resuelve cada una.
> Usar insertion sort en tramos pequeños (evita el costo de la recursión), elegir el pivote como mediana de 3 (evita pivotes extremos y el envenenamiento) y particionar en menores, iguales y mayores (maneja bien los elementos repetidos).
