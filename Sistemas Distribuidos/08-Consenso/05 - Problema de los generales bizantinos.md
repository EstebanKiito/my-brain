---
ramo: "Sistemas Distribuidos"
tema: "Consenso"
tags:
  - sd/consenso
  - origen/complemento
prerrequisitos:
  - "[[04 - Casos borde y garantías de Paxos]]"
---

# Problema de los generales bizantinos

Paxos supone que un nodo puede caerse, pero que si responde, dice la verdad. ¿Y si un nodo **miente**? El **problema de los generales bizantinos** describe un ejército cuyos generales deben decidir juntos si atacan o se retiran, sabiendo que algunos pueden ser traidores. Es el modelo de un sistema con nodos maliciosos o defectuosos, como una red de criptomonedas abierta a cualquiera.

## El problema

- Uno o más nodos se comportan de forma **impredecible o maliciosa** respecto del protocolo: envían mensajes contradictorios, omiten pasos o actúan arbitrariamente.
- Muchos algoritmos (como Paxos) asumen caídas de nodos o particiones de red, pero **no** que un nodo entregue un valor distinto al que indica el protocolo.
- Con 1 coordinador (líder) y 2 seguidores, basta **un traidor** para que no se logre consenso.

![Seguidor traidor y coordinador traidor](adjuntos/Seguidor%20traidor%20y%20coordinador%20traidor.png)

> [!example]- Transcripción de la imagen
> **Seguidor traidor:** el líder (con corona) ordena "¡Ataquen!" a sus dos seguidores. El seguidor leal le reenvía "¡Ataquen!" al otro, pero el traidor le dice "Retirada", y el leal queda dudando ("¿?"). **Coordinador traidor:** el líder traidor ordena "¡Ataquen!" a un seguidor y "Retirada" al otro; los seguidores se reenvían lo que recibieron y ambos quedan dudando.

En ambos casos, el seguidor leal ve exactamente lo mismo: una orden del líder y una contraria del otro seguidor. No puede saber quién miente, así que con 3 nodos no hay solución.

## Solución 1: mensajes orales (OM)

> [!tip] Regla
> Al recibir el mensaje del líder, cada nodo lo **propaga a todos** y se queda con el **mensaje más repetido**; ante un empate, se aplica una regla determinista. Si hay $n$ traidores, se necesitan **$3n + 1$ nodos** en total.

![Mensajes orales con un seguidor traidor](adjuntos/Mensajes%20orales%20con%20un%20seguidor%20traidor.png)

> [!example]- Transcripción de la imagen
> El líder ordena "¡Ataquen!" a tres seguidores. Los seguidores leales se reenvían "¡Ataquen!", mientras que el traidor (al centro) les dice "Retirada" a ambos. Cada leal recibe dos "¡Ataquen!" y una "Retirada", y piensa "Ataco".

![Mensajes orales con el líder traidor](adjuntos/Mensajes%20orales%20con%20el%20l%C3%ADder%20traidor.png)

> [!example]- Transcripción de la imagen
> El líder traidor ordena "Ataquen" a dos seguidores y "retirada" al del centro. Los seguidores se reenvían lo que recibieron: el del centro dice "Retirada" y los otros dicen "¡Ataquen!". Los seguidores de los extremos reciben dos "Ataquen" y una "Retirada", y piensan "Ataco".

Con 4 nodos y 1 traidor, los leales siempre terminan con la misma decisión. Una simulación en Python lo confirmó en ambos casos; con 3 nodos, en cambio, el leal queda con un empate 1 a 1 que no puede resolver con certeza.

## Solución 2: mensajes firmados (SM)

> [!tip] Regla
> El líder **firma** su mensaje; los demás copian el mensaje, lo firman y envían **ambos** (el original y la copia). Se asume que la firma **no se puede falsificar**. Si hay $n$ traidores, se necesitan **$2n + 1$ nodos** en total.

![Mensajes firmados con un seguidor traidor](adjuntos/Mensajes%20firmados%20con%20un%20seguidor%20traidor.png)

> [!example]- Transcripción de la imagen
> El líder ordena "¡Ataquen!" a ambos seguidores. El leal reenvía "Com: Atacar / Yo: Atacar". El traidor reenvía "Com: Atacar / Yo: Retirada": no puede falsificar la orden firmada del comandante. El leal piensa "Ataco porque el otro nodo es traidor".

![Mensajes firmados con el líder traidor](adjuntos/Mensajes%20firmados%20con%20el%20l%C3%ADder%20traidor.png)

> [!example]- Transcripción de la imagen
> El líder traidor envía "¡Ataquen!" a un seguidor y "Retirada" al otro, ambos firmados. Los seguidores se reenvían "Com: Atacar / Yo: Atacar" y "Com: Retirada / Yo: Retirada". Ambos piensan "El líder es el traidor. Debemos elegir nuevo líder".

La firma cambia el juego: un traidor ya no puede inventar lo que dijo el líder, y un líder traidor queda expuesto al mostrar dos órdenes firmadas distintas.

| Solución | Supuesto | Nodos necesarios con $n$ traidores |
|---|---|---|
| Mensajes orales (OM) | Los mensajes se pueden alterar al reenviarlos | $3n + 1$ |
| Mensajes firmados (SM) | Las firmas no se pueden falsificar | $2n + 1$ |

## En la vida real

- **pBFT** (*Practical Byzantine Fault Tolerance*): algoritmo de los años 90 que tolera fallas bizantinas; usa firma de mensajes, pero exige al menos $3n + 1$ nodos para $n$ fallas.
- **Proof of Work** (PoW): los nodos compiten resolviendo un problema matemático costoso, y el primero que lo resuelve crea el bloque. Un traidor necesitaría gastar demasiados recursos, o controlar el **51 %** de la red, para que aceptaran su solución.
- **Proof of Stake** (PoS): los participantes **apuestan** criptomonedas para proponer un bloque, y se elige a uno de ellos. Los demás validadores verifican el bloque con votos firmados. Si un validador hace trampa, los demás lo detectan, rechazan el bloque y el tramposo pierde parte o todo lo apostado.

> [!warning] Lo bizantino es caro
> Tolerar mentiras exige más nodos ($3n + 1$ frente a los $2n + 1$ que bastan para tolerar caídas en Paxos), más mensajes y criptografía. Por eso los sistemas internos de una empresa, donde los nodos son confiables, usan Paxos o Raft.

## Preguntas de repaso

> [!question]- ¿Por qué con 3 nodos y un traidor no hay consenso con mensajes orales?
> Porque el seguidor leal recibe una orden del líder y otra contraria del otro seguidor, y no puede distinguir si miente el líder o el seguidor. Ambos escenarios le resultan idénticos.

> [!question]- ¿Por qué las firmas bajan el requisito de $3n + 1$ a $2n + 1$ nodos?
> Porque un traidor no puede alterar lo que firmó otro. Los leales comparan directamente las órdenes firmadas del líder y descubren las contradicciones sin depender de una votación por mayoría.

> [!question]- ¿Qué hace costoso atacar una red con Proof of Work?
> Para imponer un bloque falso hay que resolver el problema más rápido que el resto de la red, lo que en la práctica exige controlar cerca del 51 % del poder de cómputo total.
