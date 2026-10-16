---
ramo: "Estructuras de Datos"
tema: "Estructuras lineales"
tags:
  - edd
  - arreglos
  - listas-ligadas
  - complejidad
  - origen/complemento
prerrequisitos:
  - "[[03 - Notación asintótica O, Omega y Theta]]"
  - "[[03 - Aritmética de punteros y arreglos]]"
---

# Arreglos frente a listas ligadas

Las dos formas básicas de guardar una secuencia en memoria son el **arreglo** y la **lista ligada**. Casi todas las estructuras del curso se construyen sobre una de ellas, y cada una es rápida justo en lo que a la otra le cuesta. Elegir bien entre ambas es la primera decisión de diseño de cualquier algoritmo.

## Arreglo: celdas contiguas

Un **arreglo** es una secuencia de celdas de **largo fijo**, todas del mismo tamaño y tipo, guardadas de forma **contigua** en memoria. Como la celda $i$ está en la dirección $A + i \cdot \text{tamaño}$, se accede a cualquier índice en **$O(1)$** (es la [[03 - Aritmética de punteros y arreglos|aritmética de punteros]] de C).

![Arreglo contiguo en memoria](adjuntos/Slide%20-%20arreglo%20contiguo%20en%20memoria.png)

> [!example]- Transcripción de la imagen
> Slide "Arreglos". Un arreglo es una secuencia de celdas de largo fijo; cada celda es del mismo tamaño y almacena valores del mismo tipo. Se guarda en memoria de manera contigua, lo que permite acceso por índice en tiempo $\mathcal{O}(1)$. A la derecha, la memoria con `A` apuntando a cuatro celdas seguidas: $A_0 = 2.47$, $A_1 = 3.76$, $A_2 = 0.35$, $A_3 = -2.0$.

El costo está en **cambiar su forma**. Insertar en medio obliga a correr todos los elementos siguientes ($O(n)$), y si el arreglo se llena hay que pedir uno más grande y copiarlo todo.

## Lista ligada: celdas enlazadas

Una **lista ligada** es una secuencia de **largo variable** formada por **nodos**: cada uno guarda un valor y un **puntero al siguiente**. Los nodos quedan **dispersos** en memoria, donde haya espacio, y el último apunta a `NULL`.

![Lista ligada en memoria](adjuntos/Slide%20-%20lista%20ligada%20en%20memoria.png)

> [!example]- Transcripción de la imagen
> Slide "Listas ligadas". Una lista ligada es una secuencia de celdas de largo variable, cada celda del mismo tamaño. Se guarda en memoria de manera aleatoria, usando punteros, y por eso no permite acceso eficiente por índice. A la derecha, `L` apunta a $L_0 = 2.47$, que está en el medio de la memoria. Flechas curvas llevan a $L_1 = 3.76$ (más arriba), $L_2 = 0.35$ (más abajo) y $L_3 = -2.0$, en un orden distinto al de sus posiciones físicas.

Para llegar al nodo $i$ hay que seguir $i$ punteros desde la cabeza: **$O(n)$**. A cambio, insertar o borrar junto a un nodo que ya se tiene es **$O(1)$**, porque solo se cambian punteros:

![Inserción en una lista ligada](adjuntos/Slide%20-%20inserci%C3%B3n%20en%20una%20lista%20ligada.png)

> [!example]- Transcripción de la imagen
> La lista 2.47 → 3.76 → 0.35 → −2.0 (el último con una X, es decir, `NULL`), ahora con un nodo 4.0 insertado entre 3.76 y 0.35: 2.47 → 3.76 → 4.0 → 0.35 → −2.0. Ningún otro nodo se movió.

## Comparación

| Operación | Arreglo | Lista ligada |
|---|---|---|
| Acceder al índice $i$ | $O(1)$ | $O(n)$ |
| Insertar o borrar al inicio | $O(n)$ (correr todo) | $O(1)$ |
| Insertar al final | $O(1)$ si hay espacio | $O(1)$ **con puntero al último**, $O(n)$ sin él |
| Insertar en medio (ya ubicado) | $O(n)$ | $O(1)$ |
| Buscar un valor | $O(n)$, o $O(\log n)$ si está ordenado ([[04 - Búsqueda binaria y dividir para conquistar\|búsqueda binaria]]) | $O(n)$ siempre |
| Memoria extra | Ninguna | Un puntero por nodo |

> [!tip] Guardar un puntero al final
> Mantener un puntero al último elemento (en una lista) o el índice de la primera celda libre (en un arreglo) convierte "agregar al final" en $O(1)$, sin tener que recorrer la estructura. Es una optimización barata que muchos algoritmos del curso dan por supuesta.

> [!warning] La búsqueda binaria no sirve en listas
> Aunque la lista esté ordenada, llegar al elemento del medio cuesta $O(n)$, así que la búsqueda binaria pierde su ventaja. Las estructuras que buscan rápido sin arreglos (árboles de búsqueda) se ven más adelante en el curso.

El mismo tema, visto desde el almacenamiento de una base de datos, está en [[06 - Arreglos y listas ligadas|Arreglos y listas ligadas (Bases de Datos)]].

## Preguntas de repaso

> [!question]- ¿Por qué un arreglo permite acceso por índice en $O(1)$ y una lista ligada no?
> En el arreglo las celdas son contiguas y del mismo tamaño, así que la dirección del elemento $i$ se calcula con una suma. En la lista los nodos están dispersos y la única forma de llegar al $i$-ésimo es seguir $i$ punteros.

> [!question]- ¿Por qué insertar en medio de una lista ligada es $O(1)$, pero en un arreglo es $O(n)$?
> En la lista basta con reasignar dos punteros (el del nodo nuevo y el del anterior). En el arreglo hay que correr una posición todos los elementos que van después, que pueden ser $n$.

> [!question]- ¿Qué se necesita para insertar al final de una lista ligada en $O(1)$?
> Un puntero al último nodo (*tail*). Sin él, hay que recorrer toda la lista para encontrar el final.

> [!question]- Si un programa hace muchos accesos por índice y casi ninguna inserción, ¿qué estructura conviene?
> Un arreglo: su acceso es $O(1)$, y su desventaja (insertar en medio) casi no se usa.
