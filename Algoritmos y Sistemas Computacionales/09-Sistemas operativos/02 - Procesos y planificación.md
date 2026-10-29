---
ramo: "Algoritmos y Sistemas Computacionales"
tema: "Sistemas operativos"
tags:
  - algoritmos/sistemas-operativos
  - algoritmos/procesos
  - origen/complemento
prerrequisitos:
  - "[[01 - El sistema operativo como intermediario|El sistema operativo como intermediario]]"
---

# Procesos y planificación

Un **proceso** es un programa en ejecución. No basta con el código: mientras corre, el proceso necesita registros, una pila, datos y memoria dinámica. El sistema operativo administra esos recursos y decide qué proceso usa la CPU en cada momento.

## Qué hay dentro de un proceso

| Parte | Qué guarda |
|---|---|
| **Código** (*text*) | Las instrucciones del programa; es información estática |
| **Program Counter y registros** | La actividad actual: en qué instrucción va y con qué valores |
| **Stack** | Datos temporales: parámetros de funciones, direcciones de retorno y variables locales |
| **Datos** (*data*) | Variables globales |
| **Heap** | Memoria asignada dinámicamente en tiempo de ejecución |

![Diseño de la memoria de un proceso: stack, heap, data y text](adjuntos/Dise%C3%B1o%20de%20la%20memoria%20de%20un%20proceso.png)

> [!example]- Transcripción de la imagen
> - La memoria se dibuja como un rectángulo que va de 0 (abajo) a `max` (arriba).
> - Desde abajo: `text` (código), `data` (variables globales), `heap` (memoria dinámica).
> - Arriba, el `stack`, que crece hacia abajo.
> - El espacio entre el stack y el heap es la memoria libre disponible.

> [!tip] La idea central
> El código es igual para todas las ejecuciones de un programa, pero cada proceso tiene su propio PC, registros, stack y heap. Por eso dos ejecuciones del mismo programa son procesos distintos.

## Muchos procesos quieren la CPU

La CPU ejecuta una instrucción a la vez (por núcleo), pero puede haber muchos procesos listos. El sistema operativo los organiza en colas:

- **Ready queue:** procesos listos para ejecutarse, esperando su turno.
- **CPU:** el proceso que está corriendo en este momento.
- **I/O queue:** procesos que esperan una operación de entrada/salida.

Un proceso se mueve entre estas colas: cuando se le acaba el **time slice** vuelve a la cola de listos; cuando pide una operación de E/S pasa a la cola de E/S; cuando la operación termina, vuelve a la cola de listos.

> [!warning] La ilusión de simultaneidad
> Un solo núcleo no ejecuta dos procesos al mismo tiempo: los alterna muy rápido. El **time slice** es el tiempo que le toca a cada uno antes de que el SO decida si sigue o cambia.

## Planificación

El criterio para elegir el siguiente proceso se llama **planificación** (*scheduling*). Distintos algoritmos priorizan cosas distintas: terminar rápido, repartir el tiempo equitativamente, atender primero lo urgente o maximizar el uso de la CPU. En este curso solo se presenta la idea; los algoritmos se ven en el ramo de Sistemas Operativos.

## Preguntas de repaso

> [!question]- ¿Qué diferencia hay entre un programa y un proceso?
> El programa es el código estático; el proceso es ese programa en ejecución, con su PC, registros, stack, datos y heap.

> [!question]- ¿Qué guarda el stack de un proceso?
> Los datos temporales de las funciones: parámetros, direcciones de retorno y variables locales.

> [!question]- ¿Qué pasa cuando a un proceso se le acaba el time slice?
> Vuelve a la cola de listos para que el sistema operativo elija otro proceso. No termina: solo deja la CPU por un momento.

> [!question]- ¿Para qué sirve la cola de E/S?
> Para organizar los procesos que están esperando una operación de entrada/salida, como leer un archivo o recibir datos del teclado.
