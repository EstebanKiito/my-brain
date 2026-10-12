---
ramo: "Sistemas Operativos y Redes"
tema: "Administración de memoria"
tags:
  - so/memoria
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es un sistema operativo]]"
  - "[[01 - Concepto de proceso y espacio de memoria]]"
---

# Memoria principal y el desafío de la multiprogramación

Este capítulo trata de cómo el sistema operativo administra la memoria principal de los procesos que están en ejecución. El punto de partida es simple: la memoria es un gran arreglo de bytes. La dificultad aparece cuando hay que repartirla entre varios procesos a la vez.

## La memoria es un arreglo de bytes

La memoria principal es **un gran arreglo de bytes, cada uno con su propia dirección**. Las unidades son potencias de 2:

| Unidad | Bytes |
|---|---|
| 1 KB | $1024 = 2^{10}$ |
| 1 MB | $2^{20} = 1\,048\,576$ |
| 1 GB | $2^{30}$ |

Una memoria de 256 KB, por ejemplo, tiene direcciones desde `0x000…0` hasta $256 \cdot 2^{10} - 1 = 262\,143$.

![Memoria física compartida con multiprogramación](adjuntos/Memoria%20f%C3%ADsica%20compartida%20con%20multiprogramaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Dibujo a mano: la memoria como una fila de casillas (bytes), con la primera dirección marcada `0x000..0` y la última $256 \cdot 2^{10} - 1$.

## Sin multiprogramación: fácil

¿Cómo se guardan en memoria los procesos, con sus variables y su código? Si hay **un solo proceso**, basta con cargar su espacio completo. La vida del compilador es fácil: **el programa siempre se carga en la misma dirección** y cada variable tiene la misma dirección en cada ejecución.

![Memoria como arreglo lineal de bytes sin multiprogramación](adjuntos/Memoria%20como%20arreglo%20lineal%20de%20bytes%20sin%20multiprogramaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Memoria desde 0 KB hasta *max* (anotado a mano: 256 KB). De 0 KB a 64 KB está el *Operating System (code, data, etc.)*; de 64 KB hasta el final, el *Current Program (code, data, etc.)*.

## Con multiprogramación: dos problemas

Con **varios procesos en memoria**, cada uno puede cargarse en cualquier parte, y eso trae dos problemas:

| Problema | Qué pasa | Requisito |
|---|---|---|
| **1. Relocalización** | Las variables no están siempre en la misma ubicación: dependen de dónde se cargó el proceso | Relocalizar las direcciones |
| **2. Protección** | Un proceso, por error, podría leer y modificar la memoria de otro | Proteger la memoria de cada proceso |

![Problemas de relocalización y protección con multiprogramación](adjuntos/Problemas%20de%20relocalizaci%C3%B3n%20y%20protecci%C3%B3n%20con%20multiprogramaci%C3%B3n.png)

> [!example]- Transcripción de la imagen
> "Con Multiprogramación". La memoria va de 0 KB a 512 KB en bloques de 64 KB: *Operating System* (0-64 KB), *free* (64-128 KB), *Process C* (128-192 KB), *Process B* (192-256 KB), *free* (256-320 KB), *Process A* (320-384 KB) y dos bloques *free* (384-512 KB). Anotaciones a mano: el bloque libre de 64 KB está marcado "PA" con "64·1024", y Process A, tachado, tiene una flecha a "320·1024", es decir, la dirección inicial de A depende de dónde se cargue.

El ejemplo de la figura lo muestra: si el proceso A se carga en 320 KB, su primer byte está en $320 \cdot 1024$. Si la próxima vez cabe en el hueco de 64 KB, empieza en $64 \cdot 1024$. Un programa compilado con la dirección fija $320 \cdot 1024$ escribiría, en el segundo caso, en una zona que no le pertenece.

> [!warning] Direcciones absolutas no sirven con multiprogramación
> Si el SO no se encarga de indicarle al proceso dónde está, el proceso terminará accediendo a direcciones de memoria que no son suyas. Por eso **el compilador y el sistema operativo** trabajan con direcciones **relativas** al inicio del proceso, no absolutas. La dirección real se calcula al ejecutar, según dónde quedó cargado el proceso.

## La solución: espacio de direcciones

Las direcciones que usa un proceso son **virtuales**: no son absolutas, sino direcciones dentro de un **espacio virtual que el SO asigna a cada proceso**. Esa abstracción se llama **espacio de direcciones**, y resuelve a la vez la relocalización y la protección. La primera forma de implementarla, con los registros base y límite, está en [[03 - Relocalización, protección de memoria y registros base y límite|relocalización y registros base y límite]].

## Preguntas de repaso

> [!question]- ¿Por qué con un solo proceso el compilador puede usar direcciones fijas?
> Porque el programa siempre se carga en la misma dirección, así que cada variable queda siempre en el mismo lugar en todas las ejecuciones.

> [!question]- ¿Cuáles son los dos problemas que trae la multiprogramación a la memoria?
> La relocalización (el proceso puede cargarse en cualquier lugar, así que sus direcciones cambian) y la protección (un proceso podría leer o modificar la memoria de otro).

> [!question]- ¿Por qué no sirven las direcciones absolutas con multiprogramación?
> Porque el proceso no se carga siempre en el mismo lugar. Una dirección absoluta fija, válida si se cargó en 320 KB, apuntaría a memoria ajena si esta vez se cargó en 64 KB.

> [!question]- ¿Cuál es la última dirección de una memoria de 256 KB?
> $256 \cdot 2^{10} - 1 = 262\,143$, porque las direcciones van desde 0.
