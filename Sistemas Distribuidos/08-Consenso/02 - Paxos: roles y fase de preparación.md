---
ramo: "Sistemas Distribuidos"
tema: "Consenso"
tags:
  - sd/consenso
  - origen/complemento
prerrequisitos:
  - "[[01 - Algoritmos de consenso]]"
  - "[[01 - Relojes lógicos de Lamport]]"
---

# Paxos: roles y fase de preparación

**Paxos** es uno de los primeros algoritmos formales de consenso, propuesto por Leslie Lamport. Su idea central es que una operación solo avanza si la respalda una **mayoría** de nodos, y que cualquier propuesta nueva debe "heredar" lo que la mayoría ya pudo haber aceptado. La primera fase, **prepare**, sirve para reservar el turno y descubrir esas aceptaciones previas.

## Un poco de historia

El paper original, *The Part-Time Parliament* (1990), contaba el algoritmo como la historia de un parlamento en una isla griega ficticia llamada Paxos, cuyos miembros eran versiones griegas de científicos reales. El humor no funcionó: nadie entendió el algoritmo, y los revisores pidieron sacar la historia. Años después Lamport publicó una versión "para humanos", *Paxos Made Simple* (2001).

## Roles y fases

| Rol | Qué hace |
|---|---|
| **Proponente** (*proposer*) | Propone una acción para consolidar |
| **Aceptante** (*acceptor*) | Acepta la acción y la guarda localmente |
| **Aprendiz** (*learner*) | Consolida (*commitea*) la acción de forma definitiva |

En la práctica un nodo puede cumplir varios roles, siempre que respete las reglas de cada uno. El algoritmo tiene tres fases: **preparar** (*prepare*), **aceptar** (*accept*) y **aprender** (*learn*).

## Fase 1: preparar

1. El proponente envía `prepare(n)` a cada aceptante. $n$ es un **identificador único** de la propuesta; en las implementaciones suele ser el par (timestamp, id del nodo), para que dos proponentes nunca usen el mismo número.
2. Cada aceptante **activo** responde según su historia:

![Respuestas de los aceptantes a prepare](adjuntos/Respuestas%20de%20los%20aceptantes%20a%20prepare.png)

> [!example]- Transcripción de la imagen
> **Caso 1:** si es su primer `prepare(n)`, responde "ok" y promete no aceptar ningún mensaje con identificador $n_2 < n$. **Caso 2:** si ya recibió un `prepare(n2)`: si $n_2 > n$ rechaza `prepare(n)`; si $n_2 < n$ es un caso especial. En el dibujo, un proponente envía `prepare(5)`: el primer aceptante ("ohh, primer prepare") responde "ok", el segundo ("antes acepté prepare(9)") lo rechaza, y el tercero ("antes acepté prepare(1)") cae en el caso especial.

### El caso especial

![Aceptante que comparte una operación previa](adjuntos/Aceptante%20que%20comparte%20una%20operaci%C3%B3n%20previa.png)

> [!example]- Transcripción de la imagen
> Si un aceptante **ya aceptó una acción** ($A_x$) antes, debe **compartirla** junto con su identificador, y de todas formas responde "ok" y promete no aceptar nada con identificador menor a $n$. En el dibujo, el proponente envió `prepare(5)`. Un aceptante, que antes aceptó `prepare(1)` y su operación $A_1$, responde "Ok, pero acepté $A_1$ con n = 1". Otro, que solo había aceptado `prepare(2)` y nada más, responde "Ok".

El aceptante no oculta lo que ya aceptó: esa información le permitirá al proponente respetar decisiones que quizás ya tenían mayoría.

## Resumen de la fase 1

| Lado | Posibilidades |
|---|---|
| **Proponente** envía `prepare(n)` | Se lo aceptan; se lo rechazan; o se lo aceptan pero le avisan de una operación aceptada antes |
| **Aceptante** recibe `prepare(n)` | Lo acepta y promete no aceptar nada con identificador menor a $n$; lo rechaza o simplemente no responde; si ya había aceptado una operación con identificador menor, la comparte |

## ¿Cuándo sigue el proponente?

![Propuesta rechazada por falta de mayoría](adjuntos/Propuesta%20rechazada%20por%20falta%20de%20mayor%C3%ADa.png)

> [!example]- Transcripción de la imagen
> Un proponente piensa "Me rechazaron": un aceptante respondió "nah", otro respondió "ok", y el tercero está caído.

Si **50 % o menos** de todos los nodos de la red responden "ok", la propuesta **falla** y el proponente vuelve a la fase 1 con un identificador **mayor**. Si **más del 50 %** responde "ok", pasa a la [[03 - Paxos: aceptar y aprender|fase de aceptar]].

> [!tip] Por qué mayoría
> Dos mayorías de un mismo conjunto siempre comparten al menos un nodo. Así, cualquier propuesta nueva con mayoría de "ok" incluye a alguien que vio la propuesta anterior y puede contarle qué se aceptó.

> [!warning] La mayoría es sobre todos los nodos
> El umbral se calcula sobre el total de nodos de la red, no sobre los que respondieron. Un nodo caído cuenta como un "no".

## Preguntas de repaso

> [!question]- ¿Qué promete un aceptante al responder "ok" a `prepare(n)`?
> Que no aceptará ninguna propuesta con identificador menor a $n$. Esa promesa impide que un proponente antiguo consolide algo después de que empezó uno más nuevo.

> [!question]- ¿Por qué el aceptante debe compartir la operación que ya aceptó?
> Porque esa operación pudo haber sido aceptada por una mayoría. Si el nuevo proponente la ignorara, podría consolidar otra operación y romper el acuerdo.

> [!question]- Con 5 nodos, 2 responden "ok", 1 rechaza y 2 están caídos. ¿Qué hace el proponente?
> Vuelve a la fase 1 con un identificador mayor: 2 de 5 no es más del 50 %, y los nodos caídos cuentan dentro del total.
