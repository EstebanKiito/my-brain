---
ramo: "Sistemas Distribuidos"
tema: "Fundamentos de sistemas distribuidos"
tags:
  - sd/fundamentos
  - origen/complemento
prerrequisitos:
  - "[[01 - Qué es un sistema distribuido]]"
---

# Desafíos de los sistemas distribuidos

Repartir un sistema entre muchas máquinas trae fiabilidad y escalabilidad, pero también problemas que no existen dentro de un solo computador. El curso los agrupa en cuatro desafíos; casi todos los algoritmos que vienen después (relojes, consenso, replicación) son respuestas a alguno de ellos.

## 1. Complejidad inherente

Con dos o más computadores **no hay memoria compartida**: cada nodo tiene su memoria local y solo conoce a los demás por los mensajes que recibe. De ahí salen dos dificultades:

- **Establecer un estado global es complejo.** Ningún nodo ve el sistema completo en un instante; cada uno tiene una foto parcial y desfasada.
- **No se puede asegurar un tiempo global.** Cada máquina tiene su propio reloj, y los relojes se desvían. No hay forma directa de saber qué evento ocurrió primero en dos nodos distintos.

En un solo computador, en cambio, los procesos comparten memoria y reloj, y la sincronización se resuelve con herramientas como [[04 - Mutex locks y el dilema de busy waiting versus dormir|mutex]] o [[06 - Semáforos de Dijkstra y tipos de semáforos|semáforos]].

## 2. Gestión de fallos parciales

En un computador, una falla grave suele botarlo entero. En un sistema distribuido falla **una parte** y el resto sigue: un nodo se cae, un enlace se corta, un disco se llena. El desafío es **enmascarar** esas fallas y recuperarse de ellas para que pasen desapercibidas para usuarios y aplicaciones.

## 3. Latencia y ancho de banda

Los mensajes tardan y la red tiene capacidad limitada. La consecuencia más seria es sutil: en un sistema asíncrono es **imposible distinguir un nodo caído de uno que solo responde muy lento**. Si un nodo no contesta, esperar más puede ser inútil y declararlo muerto puede ser un error.

> [!warning] Caído o lento
> Un *timeout* no prueba que el otro nodo falló, solo que no respondió a tiempo. Muchos errores de diseño vienen de tratar el silencio como una falla segura.

## 4. Pitfalls de diseño

Son **supuestos falsos** que el diseñador asume sin darse cuenta y que el sistema real no cumple. Las slides mencionan:

- La red es segura.
- La red es homogénea.
- La latencia es bajísima.
- El ancho de banda alcanza para todo.
- Hay un único administrador.

Esta lista corresponde a las clásicas **falacias de la computación distribuida** (Deutsch y Gosling), que además incluyen que la red es confiable, que la topología no cambia y que transportar datos no cuesta nada.

## Ejemplo: identificar objetivo y desafío

Una empresa ofrece *streaming* de conciertos 24/7: si un servidor se cae, el usuario se redirige a otro. Para lograrlo confía en que la comunicación entre servidores será tan rápida que, al caer uno, alcanzará a enviar el concierto a otro.

- El **objetivo** que persigue es la **confiabilidad** (seguir funcionando ante fallas parciales).
- El **problema** que ilustra es un **pitfall de diseño**: asume que la latencia es bajísima. Un servidor que se cae tampoco "alcanza" a enviar nada.

```mermaid
flowchart LR
    A[Supuesto: la red es rapidísima] --> B[Al caer, el servidor envía el concierto a otro]
    B --> C{¿Se cumple el supuesto?}
    C -- No --> D[El usuario pierde la transmisión]
```

## Preguntas de repaso

> [!question]- ¿Por qué la falta de memoria compartida impide conocer el estado global?
> Porque cada nodo solo sabe lo que tiene en su memoria y lo que le llega por mensajes, que tardan. Cuando un mensaje llega, el estado del emisor ya puede haber cambiado, así que nadie tiene una foto simultánea del sistema completo.

> [!question]- ¿Qué consecuencia tiene no poder distinguir un nodo caído de uno lento?
> El sistema debe decidir con información incompleta: si espera de más se bloquea, y si declara la falla antes de tiempo puede tener dos nodos actuando a la vez. Los algoritmos de consenso y de detección de fallas existen para lidiar con esa incertidumbre.

> [!question]- En el ejemplo del *streaming*, ¿por qué la respuesta no es "confiabilidad con problemas de latencia"?
> Porque el escenario no describe una red lenta, sino un diseño que **asume** que la red será rapidísima. El error está en el supuesto, y eso es un pitfall de diseño.
