---
ramo: "Estructuras de Datos"
tema: "Quicksort"
tags:
  - edd
  - mediana
  - partition
  - pivote
  - origen/complemento
prerrequisitos:
  - "[[04 - Búsqueda binaria y dividir para conquistar]]"
---

# Mediana y búsqueda por partición

Quicksort nace de un problema que no es ordenar: encontrar la **mediana** sin ordenar todo. La herramienta que lo resuelve es **elegir un pivote y separar** los datos en menores y mayores. Si se aplica repetidamente esa idea, el resultado final es un arreglo ordenado.

## El problema

Para repartir un gran conjunto de puntos 2D entre varias máquinas, se quiere dividir el plano en rectángulos con la **misma cantidad de puntos** cada uno. Hay que cortar por la mediana de $x$, después por la mediana de $y$ en cada mitad, y así sucesivamente. Ordenar por $x$ no sirve para $y$, y los datos llegan al azar.

![Partición de puntos 2D por medianas](adjuntos/Partici%C3%B3n%20de%20puntos%202D%20por%20medianas.png)

> [!example]- Transcripción de la imagen
> Un cuadrado con puntos negros dispersos, dividido por líneas rojas verticales y azules horizontales en rectángulos de distintos tamaños, cada uno con una cantidad parecida de puntos.

![Definición de mediana](adjuntos/Definici%C3%B3n%20de%20mediana.png)

> [!example]- Transcripción de la imagen
> "Definición". Dada una secuencia **ordenada** de $n$ valores $a_0, \dots, a_{n-1}$, la mediana $M_e$ es $a_{\lfloor n/2 \rfloor}$ si $n$ es impar, y $\frac{a_{n/2} + a_{n/2-1}}{2}$ si $n$ es par.

La mediana es el valor con **tantos elementos menores como mayores**. Si los datos estuvieran ordenados, estaría al medio. Pero ordenar cuesta más de lo necesario: basta con *reorganizar*, que no es lo mismo que *reordenar*.

## La estrategia: pivote y partición

Se toma un **pivote** al azar y se separan los demás en **menores** y **mayores**. Así, el pivote queda en su **posición ordenada** y se sabe de qué lado está la mediana, porque estará donde haya más elementos. Se repite solo en ese lado.

![Primer pivote 6](adjuntos/Mediana%20-%20primer%20pivote%206.png)

> [!example]- Transcripción de la imagen
> Secuencia de largo impar: 7, 3, 5, 2, 1, 9, 7, 8, 6, 4, 3 (índices 0 a 10). Pivote aleatorio: 6. Menores: 3, 5, 2, 1, 4, 3. Mayores: 7, 9, 7, 8. Pregunta: "¿es 6 la mediana? ¿dónde se ubica esta?".

![Secuencia reorganizada en torno a 6](adjuntos/Mediana%20-%20secuencia%20reorganizada%20en%20torno%20a%206.png)

> [!example]- Transcripción de la imagen
> 3, 5, 2, 1, 4, 3 (menores, lila), 6 en la posición 6 (gris) y 7, 9, 7, 8 (mayores, amarillo).

![Se revisa el tramo izquierdo](adjuntos/Mediana%20-%20se%20revisa%20el%20tramo%20izquierdo.png)

> [!example]- Transcripción de la imagen
> "Como la posición de la mediana debiera ser $\lfloor 11/2 \rfloor = 5$ y el pivote quedó en la posición 6, revisamos el tramo a la izquierda del pivote". Se marca el tramo de índices 0 a 5.

![Pivote 2 en el tramo izquierdo](adjuntos/Mediana%20-%20pivote%202%20en%20el%20tramo%20izquierdo.png)

> [!example]- Transcripción de la imagen
> Pivote aleatorio 2 en el tramo 3, 5, 2, 1, 4, 3. Menores: 1. Mayores: 3, 5, 4, 3. "Reordenamos el tramo analizado para ver si el pivote es la mediana".

![Se revisa el subtramo derecho](adjuntos/Mediana%20-%20se%20revisa%20el%20subtramo%20derecho.png)

> [!example]- Transcripción de la imagen
> El 2 quedó en la posición 1, así que se sigue en el subtramo derecho, índices 2 a 5: 3, 5, 4, 3.

![Pivote 5 y reubicación](adjuntos/Mediana%20-%20pivote%205%20y%20reubicaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Con pivote 5: menores 3, 4, 3 y mayores ∅. Al reubicar, el tramo queda 3, 4, 3, 5.

![El pivote queda en la posición central](adjuntos/Mediana%20-%20el%20pivote%20queda%20en%20la%20posici%C3%B3n%20central.png)

> [!example]- Transcripción de la imagen
> Arreglo final 1, 2, 3, 4, 3, 5, 6, 7, 9, 7, 8. "Como el pivote está en la posición $\lfloor n/2 \rfloor = \lfloor 11/2 \rfloor = 5$, **es la mediana**".

> [!tip] Idea clave
> Cada partición deja **un** elemento (el pivote) en su posición definitiva y descarta un lado entero. Es la misma lógica de la [[04 - Búsqueda binaria y dividir para conquistar|búsqueda binaria]], pero sobre datos desordenados.

## Preguntas de repaso

> [!question]- ¿Por qué no conviene ordenar el arreglo para encontrar su mediana?
> Porque ordenar cuesta $O(n \log n)$ o más y entrega mucha más información de la necesaria. Para la mediana basta con ubicar un elemento en su posición, cosa que hace la partición.

> [!question]- Tras particionar con un pivote que quedó en la posición 6 de un arreglo de 11, ¿dónde se busca la mediana?
> En el tramo izquierdo (índices 0 a 5), porque la mediana debe quedar en la posición $\lfloor 11/2 \rfloor = 5$, a la izquierda del pivote.

> [!question]- ¿Qué garantiza la partición sobre el pivote?
> Que queda en su posición ordenada: todos los menores a su izquierda y todos los mayores a su derecha, aunque cada lado siga desordenado.
