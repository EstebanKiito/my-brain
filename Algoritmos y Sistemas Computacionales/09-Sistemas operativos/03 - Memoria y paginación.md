---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Sistemas operativos"
tags:
  - algoritmos/sistemas-operativos
  - algoritmos/memoria
  - origen/complemento
prerrequisitos:
  - "[[02 - Procesos y planificación|Procesos y planificación]]"
---

# Memoria y paginación

La memoria principal es un gran arreglo de bytes, cada uno con su dirección. El procesador lee instrucciones y datos desde ahí, y escribe los resultados. Para repartirla entre varios procesos, el sistema operativo usa **paginación** y **memoria virtual**.

## La memoria como arreglo

Cada byte tiene una **dirección**. El PC lee la instrucción desde una dirección, la instrucción puede pedir operandos en otras direcciones y el resultado se guarda en otra. Sin un mecanismo que traduzca direcciones, un proceso podría leer o escribir la memoria de otro.

## Paginación

La **paginación** divide la memoria en unidades de tamaño fijo:

- La memoria física se divide en **marcos** (*frames*).
- La memoria lógica de cada proceso se divide en **páginas**.
- Una dirección paginada se escribe como `(número de página, offset)`.

La **tabla de páginas** indica en qué marco físico está cada página lógica. El offset no cambia: solo se traduce el número de página.

![Paginación: páginas lógicas, tabla de páginas y marcos físicos](adjuntos/Paginaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> - A la izquierda, la memoria lógica con las páginas 0, 1, 2 y 3.
> - Al centro, la tabla de páginas: 0→1, 1→4, 2→3, 3→7.
> - A la derecha, la memoria física con ocho marcos (0 a 7).
> - La página 0 está en el marco 1, la página 1 en el marco 4, la página 2 en el marco 3 y la página 3 en el marco 7.

> [!tip] La idea central
> Las páginas de un proceso no necesitan estar contiguas en la memoria física. La tabla de páginas se encarga de que el proceso vea una memoria ordenada aunque por dentro esté repartida.

## Memoria virtual

La **memoria virtual** aumenta la separación entre la memoria que ve el programador y la memoria física real. Cada proceso recibe un espacio de direcciones propio; el sistema operativo traduce esas direcciones virtuales a marcos físicos mediante el **mapa de memoria**.

Eso permite, entre otras cosas, que un proceso use más memoria que la RAM disponible: las páginas que no se están usando pueden quedar en disco y traerse cuando se necesiten.

> [!warning] La memoria virtual no es memoria infinita
> Si los procesos usan más memoria de la que cabe y el disco no alcanza, el sistema se vuelve lento o falla. La memoria virtual da la ilusión de más espacio, pero el respaldo físico sigue siendo finito.

## Preguntas de repaso

> [!question]- ¿Qué es un marco y qué es una página?
> Un marco es una unidad de tamaño fijo en la memoria física; una página es una unidad del mismo tamaño en la memoria lógica de un proceso. La tabla de páginas relaciona ambas.

> [!question]- ¿Qué parte de la dirección no cambia al traducir?
> El offset. Solo se traduce el número de página; el desplazamiento dentro de la página es el mismo en la memoria lógica y en la física.

> [!question]- ¿Por qué la paginación evita la fragmentación externa?
> Porque los marcos son de tamaño fijo y cualquier página libre puede usarse, sin necesidad de que estén contiguas. No quedan huecos entre bloques de distinto tamaño.

> [!question]- ¿Qué ventaja da la memoria virtual a cada proceso?
> Le da la ilusión de tener un espacio de memoria propio, grande y ordenado, aunque la memoria física esté compartida y repartida.
