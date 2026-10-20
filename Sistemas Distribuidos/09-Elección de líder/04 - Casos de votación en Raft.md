---
ramo: "Sistemas Distribuidos"
tema: "Elección de líder"
tags:
  - sd/eleccion-de-lider
  - origen/complemento
prerrequisitos:
  - "[[03 - Raft: estados y elección del líder]]"
---

# Casos de votación en Raft

Las reglas de votación de Raft se aplican igual en todos los casos, pero el resultado cambia según **quién** se postula primero. En estos cuatro casos hay cuatro nodos, y cada log es una lista de tuplas $(A_x, N)$: la acción $x$ registrada durante el term $N$. Con 4 nodos, la mayoría es 3 votos (el candidato vota por sí mismo).

Los cuatro casos se verificaron con una implementación en Python de las reglas de votación.

## Caso 1: el más actualizado se postula

![Raft caso 1 con el candidato más actualizado](adjuntos/Raft%20caso%201%20con%20el%20candidato%20m%C3%A1s%20actualizado.png)

> [!example]- Transcripción de la imagen
> El candidato (con corona) tiene el log $[(A_1,1),(A_2,1),(A_3,2)]$, term 2 y timeout 150, y dice "Voten por mí". Un nodo con $[(A_1,1),(A_2,1)]$ y term 2 responde "Tu último registro está en term 2 vs el mío que es term 1. ¡Voto por ti!". Uno sin logs (term 0) dice "No tengo logs. ¡Voto por ti!". Otro con $[(A_1,1),(A_2,1)]$ y term 1 también vota a favor por la misma razón.

Su último log es del term 2 y el de los demás es del term 1 o no existe: recibe los 4 votos y es líder.

## Caso 2: el menos actualizado se postula

![Raft caso 2 con el candidato menos actualizado](adjuntos/Raft%20caso%202%20con%20el%20candidato%20menos%20actualizado.png)

> [!example]- Transcripción de la imagen
> El nodo sin logs (term 0, timeout 150) se postula: "Voten por mí". Los otros tres (con terms 2, 2 y 1 en el dibujo) responden "Tu term actual es menor al mío. ¡Rechazado!".

Al postularse sube su term a 1. Los votantes con term 2 lo rechazan por la regla 1; el que tiene term 1 no puede rechazarlo por term, pero sí por la regla 3c, porque el candidato no tiene logs y él sí. No logra mayoría y esperará otro timeout.

## Caso 3: solo el term actualizado

![Raft caso 3 con solo el term actualizado](adjuntos/Raft%20caso%203%20con%20solo%20el%20term%20actualizado.png)

> [!example]- Transcripción de la imagen
> Se postula el nodo con $[(A_1,1),(A_2,1)]$, term 2 y timeout 150. El nodo con $[(A_1,1),(A_2,1),(A_3,2)]$ responde "Tu último log tiene un term menor al mío. ¡Rechazado!". El nodo sin logs vota a favor, y el otro nodo con $[(A_1,1),(A_2,1)]$ dice "Nuestro último log es igual en term. El largo es el mismo. ¡Voto por ti!".

Su term (3 tras postularse) es el más alto, pero su log no es el más actualizado: lo rechaza quien tiene $(A_3, 2)$. Aun así reúne 3 votos (el suyo y dos más) y **gana**. $A_3$ no estaba consolidada (solo la tenía un nodo), así que se puede perder sin violar nada.

## Caso 4: term y logs no tan actualizados

![Raft caso 4 con term y logs no tan actualizados](adjuntos/Raft%20caso%204%20con%20term%20y%20logs%20no%20tan%20actualizados.png)

> [!example]- Transcripción de la imagen
> Se postula el nodo con $[(A_1,1),(A_2,1)]$, term 1 y timeout 150. El nodo con $[(A_1,1),(A_2,1),(A_3,2)]$ y term 2 responde "Tu term actual es menor al mío. ¡Rechazado!". El otro nodo con $[(A_1,1),(A_2,1)]$ y term 1 dice "Nuestro último log es igual en term. El largo es el mismo. ¡Voto por ti!". El nodo sin logs vota a favor.

También gana con 3 de 4 votos. El rechazo del nodo con $(A_3, 2)$ se explica en cualquier caso por la regla 3c: el último log del candidato es del term 1, menor que el suyo.

## Resumen

| Caso | Candidato | Votos | ¿Líder? |
|---|---|---|---|
| 1 | El de log más actualizado | 4 de 4 | Sí |
| 2 | El nodo sin logs y con term 0 | 1 de 4 | No |
| 3 | Log del term 1, term alto | 3 de 4 | Sí |
| 4 | Log del term 1, term 1 | 3 de 4 | Sí |

> [!tip] Lo que muestran los casos
> Gana cualquier candidato que esté **al menos tan actualizado como una mayoría**, no necesariamente el más actualizado de todos. Lo que no puede pasar es que gane alguien al que le falte una acción **consolidada**.

> [!warning] Rechazo por term o por log
> Un votante con term mayor rechaza por la regla 1 antes de mirar los logs. Si los terms empatan, decide la comparación de logs. Para predecir el resultado conviene revisar ambas reglas en orden.

## Preguntas de repaso

> [!question]- En el caso 3, ¿por qué se puede elegir un líder que no tiene $(A_3, 2)$?
> Porque $A_3$ estaba solo en un nodo, así que no estaba consolidada. Raft solo garantiza conservar las acciones consolidadas; el resto puede sobrescribirse.

> [!question]- ¿Por qué el nodo sin logs del caso 2 no gana aunque todos podrían votar por él según la regla 2?
> La regla 2 la aplica el **votante** cuando el votante no tiene logs. Aquí los votantes sí tienen logs y además un term mayor que el del candidato, así que lo rechazan por la regla 1.

> [!question]- Con 5 nodos, ¿cuántos votos necesita un candidato?
> 3, contando el suyo: más de la mitad de 5.
