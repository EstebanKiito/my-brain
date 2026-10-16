---
ramo: "Estructuras de Datos"
tema: "Heaps y colas de prioridad"
tags:
  - edd
  - colas-de-prioridad
  - heap
  - origen/complemento
prerrequisitos:
  - "[[03 - Pilas y colas]]"
---

# Colas de prioridad

En una [[03 - Pilas y colas|cola FIFO]], la prioridad es el orden de llegada. Pero muchas veces lo que importa es un **atributo del dato**: el avión con menos combustible aterriza primero, el paciente más grave se atiende primero y el sistema operativo ejecuta el proceso más prioritario. Los datos llegan en cualquier orden, así que no basta con ponerlos en fila.

> [!tip] Definición
> Una **cola de prioridad** (de máxima o de mínima prioridad) es una estructura de datos que permite **insertar** un dato con su prioridad, **extraer** el de mayor prioridad y, eventualmente, **cambiar** la prioridad de un dato.

## Las soluciones ingenuas son lineales

![Costos de cola de prioridad en arreglos](adjuntos/Costos%20de%20cola%20de%20prioridad%20en%20arreglos.png)

> [!example]- Transcripción de la imagen
> **Arreglo sin orden**: inserción al final, $\mathcal{O}(1)$; extracción buscando el máximo, $\mathcal{O}(n)$. **Arreglo ordenado por valor**: inserción en la posición correcta, $\mathcal{O}(n)$; extracción del último elemento, $\mathcal{O}(1)$.

| Implementación | Insertar | Extraer el más prioritario |
|---|---|---|
| Arreglo sin orden | $O(1)$ | $O(n)$: hay que recorrerlo |
| Arreglo ordenado (insertion sort) | $O(n)$ | $O(1)$ |
| **Heap** | $O(\log n)$ | $O(\log n)$ |

Las dos primeras pagan $O(n)$ en alguna operación. La salida es **descomponer** el problema: no hace falta tener los datos totalmente ordenados, basta con un **orden parcial** que garantice dónde está el más prioritario.

## La idea del heap

Un **heap** es una estructura **jerárquica** con orden parcial: los elementos de más arriba tienen más prioridad que los de más abajo. Así, el más prioritario está siempre en la cima y se lee en $O(1)$. Como la estructura es un árbol balanceado, insertar y extraer cuestan $O(\log n)$: menos que lineal, porque los datos están "medio ordenados".

> [!warning] Un heap no sirve para buscar
> El heap solo sabe cuál es el **máximo** (o el mínimo). Para encontrar cualquier otro valor hay que recorrerlo entero, en $O(n)$. Para buscar están los árboles de búsqueda, que se ven más adelante en el curso.

Comparado con una cola FIFO, que inserta y extrae en $O(1)$, el heap es más lento ($O(\log n)$). Ese es el precio de ordenar por prioridad en vez de por llegada.

## Preguntas de repaso

> [!question]- ¿Qué diferencia una cola de prioridad de una cola FIFO?
> En la FIFO sale el que lleva más tiempo esperando. En la cola de prioridad sale el que tiene mayor prioridad según un atributo del dato, sin importar cuándo llegó.

> [!question]- ¿Por qué un arreglo ordenado no es una buena cola de prioridad?
> Porque, aunque extraer el máximo es $O(1)$, cada inserción debe ubicar el dato en su lugar y correr los demás, lo que cuesta $O(n)$.

> [!question]- ¿Qué gana el heap con un orden solo parcial?
> Mantener un orden total cuesta caro. El heap solo garantiza que cada nodo es más prioritario que sus descendientes, y eso basta para tener el máximo en la cima con operaciones $O(\log n)$.

> [!question]- Dar dos ejemplos de problemas que necesitan una cola de prioridad.
> Elegir el siguiente proceso a ejecutar en un sistema operativo y decidir qué avión aterriza primero según su combustible.
