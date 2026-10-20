---
ramo: "Sistemas Distribuidos"
tema: "Consenso"
tags:
  - sd/consenso
  - origen/complemento
prerrequisitos:
  - "[[01 - Coordinación en sistemas distribuidos]]"
---

# Algoritmos de consenso

Una base de datos replicada debe decidir si una escritura se aplica o no, y todas las réplicas deben tomar **la misma** decisión, aunque algunas estén caídas o los mensajes lleguen tarde, duplicados o contradictorios. Si cada nodo decide por su cuenta, el sistema se divide en versiones incompatibles. Los **algoritmos de consenso** resuelven exactamente eso.

## El problema

Varios nodos deben acordar una decisión común: un valor, una modificación o la eliminación de un dato. Lo dificultan:

- fallas de red y nodos caídos;
- mensajes duplicados, perdidos o contradictorios;
- varios nodos que proponen cosas distintas al mismo tiempo.

![Consenso fallido entre tres proponentes](adjuntos/Consenso%20fallido%20entre%20tres%20proponentes.png)

> [!example]- Transcripción de la imagen
> Una red de nodos interconectados en la que tres participantes proponen cosas distintas ("I propose A", "I propose B", "I propose C"), y al centro un cartel rojo: **CONSENSUS FAILED**.

## Definición

Un **algoritmo de consenso** es un protocolo (una secuencia de mensajes) que permite a varios nodos acordar una **operación o acción** común, aun en presencia de fallos. Los protocolos sirven para acordar cualquier decisión; por simplicidad se habla de acordar una "operación" en vez de un "valor".

> [!tip] Propiedades deseables
> - **Acuerdo** (*agreement*): todos los nodos activos aceptan la **misma** operación.
> - **Terminación** (*termination*): todos los nodos activos **eventualmente** aceptan una operación.
> - **Tolerancia a fallos** (*fault tolerance*): funciona aunque algunos nodos no respondan.

La terminación no es trivial: un algoritmo que nunca decide nada cumple el acuerdo, pero no sirve.

## Algoritmos conocidos

| Algoritmo | Idea | Dónde se usa |
|---|---|---|
| **Paxos** | Uno de los primeros, de Leslie Lamport; acuerdo por mayoría de aceptantes | Chubby de Google, DynamoDB, transacciones livianas de Cassandra |
| **Raft** | Variación más sencilla y "democrática" de Paxos, basada en un líder | etcd, Consul y bases de datos distribuidas |
| **Proof of Work** | Los nodos compiten resolviendo un problema computacional (consenso Nakamoto) | Bitcoin |
| **Proof of Stake** | Los participantes apuestan monedas para proponer bloques; más eficiente en energía | Ethereum |

Las criptomonedas han originado muchas variaciones más. Este tema estudia [[02 - Paxos: roles y fase de preparación|Paxos]] y el [[05 - Problema de los generales bizantinos|problema de los generales bizantinos]]; Raft se estudia junto con la elección de líder.

> [!warning] Fallar no es lo mismo que mentir
> Paxos y Raft toleran nodos que **se caen** o mensajes que **se pierden**. No toleran nodos que **mienten** o envían valores distintos a los que dicta el protocolo: ese es el escenario bizantino, que exige otras técnicas.

## Preguntas de repaso

> [!question]- ¿Por qué no basta con la propiedad de acuerdo para que un algoritmo de consenso sea útil?
> Porque un algoritmo que nunca decide también cumple el acuerdo, ya que nadie acepta algo distinto. Por eso se exige terminación: todos los nodos activos deben eventualmente aceptar una operación.

> [!question]- ¿Qué tipo de falla no considera Paxos?
> Las fallas bizantinas: nodos que envían mensajes contradictorios o maliciosos. Paxos supone que los nodos pueden caerse o no responder, pero que si responden siguen el protocolo.

> [!question]- ¿Qué tienen en común un sistema de réplicas de base de datos y una criptomoneda desde el punto de vista del consenso?
> Ambos necesitan que muchos nodos acuerden el mismo orden de operaciones (escrituras o transacciones) sin un árbitro central confiable y tolerando nodos que fallan.
