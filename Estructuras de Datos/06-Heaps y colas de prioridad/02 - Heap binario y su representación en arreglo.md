---
ramo: "Estructuras de Datos"
tema: "Heaps y colas de prioridad"
tags:
  - edd
  - heap
  - arbol-binario
  - origen/complemento
prerrequisitos:
  - "[[01 - Colas de prioridad]]"
  - "[[01 - Arreglos frente a listas ligadas]]"
---

# Heap binario y su representación en arreglo

El heap es un **árbol binario** con una regla de orden entre padres e hijos. Lo notable es que, aunque se dibuja como árbol, se guarda en un **arreglo** sin punteros: la forma del árbol permite calcular dónde está cada padre e hijo con aritmética.

## Árbol binario

![Definición de árbol binario](adjuntos/Definici%C3%B3n%20de%20%C3%A1rbol%20binario.png)

> [!example]- Transcripción de la imagen
> "Definición". Un **árbol binario (AB)** almacena **llaves** asociándolas mediante punteros con una estrategia recursiva: 1. un AB tiene un **nodo** que contiene una llave; 2. el nodo puede tener hasta dos AB asociados mediante punteros, el hijo izquierdo y el hijo derecho. Así, el árbol $A$ tiene hijos `A.left` y `A.right`, y llave `A.key`.

![Nodo con llave y punteros a sus hijos](adjuntos/Pizarra%20-%20nodo%20con%20llave%20y%20punteros%20a%20sus%20hijos.jpeg)

> [!example]- Transcripción de la imagen
> Foto de pizarra. Un nodo `key` con una flecha `i` (izquierdo) hacia otro nodo `key2`, que a su vez tiene dos flechas hacia sus hijos, y una flecha `d` (derecho) hacia el símbolo de tierra, que representa un puntero `NULL`.

Es la primera **estructura recursiva** del curso. Un árbol binario cualquiera no tiene orden:

![Árbol binario sin orden](adjuntos/%C3%81rbol%20binario%20sin%20orden%20entre%20sus%20elementos.png)

> [!example]- Transcripción de la imagen
> Árbol con raíz 15, hijos 29 y 19; 29 tiene hijos 70 y 23; 19 tiene hijo derecho 170; 70 tiene hijo 3 y 23 tiene hijo 11. "Observemos que no hay un orden a priori entre sus elementos".

## Max heap: la propiedad de heap

![Definición de max heap binario](adjuntos/Definici%C3%B3n%20de%20max%20heap%20binario.png)

> [!example]- Transcripción de la imagen
> "Definición". Un **Max heap binario** $H$ es un árbol binario tal que `H.left` y `H.right` son Max heaps binarios, `H.key > H.left.key` y `H.key > H.right.key`. A estas condiciones se les llama **propiedad de heap**. "Todo hijo tiene llaves menores que el padre… pero entre hermanos no hay ninguna restricción".

![Max heap con nodos de un mismo nivel sin orden](adjuntos/Max%20heap%20con%20nodos%20de%20un%20mismo%20nivel%20sin%20orden.png)

> [!example]- Transcripción de la imagen
> Max heap: raíz 31; hijos 29 y 19; nietos 7 y 23 (de 29) y 13 y 17 (de 19); hojas 5 y 3 (de 7) y 11 (de 23), más un hueco punteado. Los nodos 7, 23, 13 y 17 están resaltados: "Los nodos de un mismo nivel no satisfacen un orden específico".

Como el máximo de cada subárbol está en su raíz, **el máximo de todo el heap está en la raíz**. Un **min heap** es lo mismo con las desigualdades al revés.

## Árboles casi llenos

![Heaps como árboles casi llenos](adjuntos/Heaps%20como%20%C3%A1rboles%20casi%20llenos.png)

> [!example]- Transcripción de la imagen
> Los heaps se guardan completándolos **por nivel**, es decir, como **árboles binarios casi llenos**. Eso no significa que con $h$ niveles haya $n = 2^h - 1$ nodos; lo que importa es que, antes de agregar un nivel, el último disponible esté completo. "Podremos hacer esto gracias a la propiedad de heap".

![Árbol binario lleno y casi lleno](adjuntos/%C3%81rbol%20binario%20lleno%20y%20casi%20lleno.png)

> [!example]- Transcripción de la imagen
> Arriba, un árbol binario lleno, cuando el número $n$ de nodos cumple $n = 2^d - 1$. Abajo, un árbol binario casi lleno, cuando $2^d \le n < 2^{d+1}$: el último nivel se llena de izquierda a derecha y está incompleto.

Al llenarse por niveles, el árbol queda **balanceado**: tiene $\lfloor \log_2 n \rfloor + 1$ niveles. Por eso recorrer de la raíz a una hoja cuesta $O(\log n)$.

## El arreglo

![Índices de padre e hijos en el arreglo](adjuntos/%C3%8Dndices%20de%20padre%20e%20hijos%20en%20el%20arreglo.png)

> [!example]- Transcripción de la imagen
> La representación permite recorrer descendientes sin punteros: el elemento $H[k]$ es padre de $H[2k+1]$ y $H[2k+2]$, y el padre de $H[k]$ es $H[\lfloor (k-1)/2 \rfloor]$. También permite ubicar los niveles: el primer elemento del nivel $h$ es $A[2^h - 1]$ y los $2^h$ elementos consecutivos corresponden al nivel $h$.

![Max heap y su arreglo](adjuntos/Max%20heap%20y%20su%20arreglo.png)

> [!example]- Transcripción de la imagen
> El max heap anterior con el índice de cada nodo entre corchetes ([0] = 31, [1] = 29, [2] = 19, [3] = 7, [4] = 23, [5] = 13, [6] = 17, [7] = 5, [8] = 3, [9] = 11, [10] vacío) y debajo su arreglo: 31, 29, 19, 7, 23, 13, 17, 5, 3, 11, _.

| Desde la posición $k$ | Índice |
|---|---|
| Hijo izquierdo | $2k + 1$ |
| Hijo derecho | $2k + 2$ |
| Padre | $\lfloor (k-1)/2 \rfloor$ |

> [!warning] Índices desde 0 frente a desde 1
> Con arreglos que empiezan en 0, el padre es $\lfloor (k-1)/2 \rfloor$. La fórmula $\lfloor k/2 \rfloor$ (con hijos en $2k$ y $2k+1$) corresponde a arreglos que empiezan en 1. Mezclar ambas convenciones es un error frecuente al implementar.

## Preguntas de repaso

> [!question]- ¿Qué garantiza la propiedad de heap y qué no garantiza?
> Garantiza que cada padre es mayor que sus hijos (en un max heap), y por lo tanto que el máximo está en la raíz. No garantiza ningún orden entre hermanos ni entre nodos de un mismo nivel.

> [!question]- ¿Por qué un heap se puede guardar en un arreglo sin punteros?
> Porque es un árbol casi lleno que se completa por niveles de izquierda a derecha. Las posiciones de padres e hijos quedan determinadas por fórmulas ($2k+1$, $2k+2$, $\lfloor (k-1)/2 \rfloor$).

> [!question]- En el arreglo 31, 29, 19, 7, 23, 13, 17, 5, 3, 11, ¿quiénes son los hijos de 29 y el padre de 11?
> 29 está en la posición 1, así que sus hijos están en 3 y 4: 7 y 23. 11 está en la posición 9, y su padre está en $\lfloor 8/2 \rfloor = 4$: 23.

> [!question]- ¿Cuántos niveles tiene un heap de $n$ elementos y por qué importa?
> $\lfloor \log_2 n \rfloor + 1$, porque está balanceado. Eso acota en $O(\log n)$ el costo de recorrer de la raíz a una hoja, que es lo que hacen inserción y extracción.
