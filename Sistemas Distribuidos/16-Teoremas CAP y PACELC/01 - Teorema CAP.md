---
ramo: "Sistemas Distribuidos"
tema: "Teoremas CAP y PACELC"
tags:
  - sd/cap
  - origen/complemento
prerrequisitos:
  - "[[03 - Consistencia fuerte o linealizable]]"
  - "[[02 - Replicación basada en quórum]]"
---

# Teorema CAP

Compras una entrada para el cine y, al llegar, otra persona tiene un ticket para el mismo asiento. ¿Qué pasó? Probablemente dos réplicas del sistema de ventas no se pudieron comunicar y ambas vendieron el asiento, porque el sistema prefirió seguir vendiendo antes que esperar. El **teorema CAP** dice que, cuando la red se parte, esa elección es inevitable.

## Enunciado

Eric **Brewer** lo propuso en **2000**, y **Gilbert y Lynch** lo formalizaron:

> [!tip] Teorema CAP
> En una red sujeta a fallas de comunicación, es imposible que un servicio web implemente una memoria compartida de lectura y escritura atómica que garantice una respuesta a cada solicitud. Dicho simple: **ante una partición de red (P), un sistema distribuido debe elegir entre consistencia (C) y disponibilidad (A)**; no puede garantizar ambas.

| Letra | Propiedad | Significado en CAP |
|---|---|---|
| **C** | Consistencia (*consistency*) | Todas las réplicas tienen el mismo valor y toda lectura devuelve el más reciente (**consistencia fuerte**) |
| **A** | Disponibilidad (*availability*) | Toda solicitud recibe una respuesta (éxito o falla), sin garantía de que sea la versión más reciente |
| **P** | Tolerancia a particiones (*partition tolerance*) | El sistema sigue funcionando pese a mensajes perdidos o partes caídas, es decir, a una partición de red |

La versión introductoria del teorema, desde la arquitectura de software, está en [[04 - Escalamiento y teorema CAP|Escalamiento y teorema CAP]].

## Las tres combinaciones

- **CA:** sin partición, la red responde siempre y los nodos se coordinan para tener los datos al día. Solo es posible mientras la red no se divide.
- **CP:** ante una partición, el nodo aislado **deja de atender** para no entregar datos inconsistentes: uno o más nodos dejan de estar disponibles. Ejemplo: [[02 - Replicación basada en quórum|quórum]].
- **AP:** ante una partición, el nodo aislado **sigue atendiendo**, aunque entregue datos obsoletos. Ejemplo: [[01 - Protocolos de replicación y gossip|gossip]].

![Sistema CP ante una partición](adjuntos/Sistema%20CP%20ante%20una%20partici%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Tres nodos parten con $n=1$. (1) Un cliente lee $n=1$. (2) Un nodo queda aislado y otro cliente escribe $n=0$ en el resto. (3) El nodo aislado (con $n=1$) rechaza la lectura (señal de prohibido). (4) Restaurada la red, todos tienen $n=0$ y la lectura devuelve 0.

![Sistema AP ante una partición](adjuntos/Sistema%20AP%20ante%20una%20partici%C3%B3n.png)

> [!example]- Transcripción de la imagen
> Mismo escenario, pero en (3) el nodo aislado sigue respondiendo y devuelve $n=1$, un valor obsoleto. Al restaurarse la red, todos convergen a $n=0$.

> [!warning] P no es opcional
> En un sistema distribuido real las particiones **van a ocurrir**. "Elegir CA" solo describe el comportamiento mientras la red funciona; la decisión real es qué sacrificar cuando se parte: C o A.

## Críticas

1. **Solo habla de particiones.** En la práctica las particiones son raras. ¿Qué se elige el resto del tiempo? CAP no ayuda a pensarlo.
2. **El "todo o nada" es irreal.** CAP es binario (hay consistencia o no), pero existen gradientes: consistencia causal, lecturas y escrituras por quórum, timeouts variables.
3. **No distingue latencia de disponibilidad.** Para Gilbert y Lynch, un nodo que no responde en tiempo finito no está disponible. Pero un sistema que tarda 10 s y otro que tarda 50 ms, ¿son igual de "disponibles"?

CAP es muy útil para entender el **límite** de un sistema distribuido, pero no basta para **diseñarlo**: no considera los compromisos cuando todo funciona normal. Para eso está [[02 - Teorema PACELC|PACELC]].

## Preguntas de repaso

> [!question]- En el problema del asiento duplicado, ¿qué eligió el sistema durante la partición?
> Disponibilidad: cada réplica siguió vendiendo sin poder coordinarse con la otra, a costa de la consistencia (dos ventas del mismo asiento).

> [!question]- ¿Por qué un sistema basado en quórum es CP?
> Porque el lado de la partición que no logra quórum deja de aceptar operaciones: prefiere no responder antes que responder con datos inconsistentes.

> [!question]- ¿Por qué se dice que un sistema distribuido no puede elegir "CA"?
> Porque no puede evitar que ocurran particiones. Cuando ocurre una, tiene que decidir entre seguir respondiendo (A) o mantener la consistencia (C).
