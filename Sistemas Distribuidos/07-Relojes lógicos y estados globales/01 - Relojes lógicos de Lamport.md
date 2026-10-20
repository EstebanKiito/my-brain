---
ramo: "Sistemas Distribuidos"
tema: "Relojes lógicos y estados globales"
tags:
  - sd/relojes
  - origen/complemento
prerrequisitos:
  - "[[02 - Relojes físicos y desincronización]]"
---

# Relojes lógicos de Lamport

Muchas veces no importa **qué hora** era cuando ocurrió algo, sino **qué ocurrió antes de qué**: que una respuesta no aparezca antes que la pregunta, o que un mensaje no "llegue al pasado". Para eso no hace falta sincronizar relojes físicos. Leslie Lamport propuso un **reloj lógico**: un contador de software que ordena los eventos sin depender del hardware.

## Qué es un reloj lógico

Se usa cuando no se necesita la hora real absoluta, sino un mecanismo para **ordenar eventos**. El reloj de Lamport:

- Es un **contador de software** que aumenta monótonamente.
- Cada proceso $P_i$ mantiene su propio reloj lógico, $C(P_i)$.
- Permite inferir el orden de los mensajes **sin relojes físicos sincronizados**.

## La relación "sucedió antes"

Lamport definió la relación **sucedió-antes**, denotada $\rightarrow$:

1. Si $a$ y $z$ ocurren en el mismo proceso y $a$ ocurre antes que $z$, entonces $a \rightarrow z$.
2. Para todo mensaje $m$, el envío ocurre antes que la recepción: $send(m) \rightarrow receive(m)$.

La relación es transitiva: si $a \rightarrow b$ y $b \rightarrow c$, entonces $a \rightarrow c$. Dos eventos que no están relacionados en ningún sentido son **concurrentes**: no se sabe si uno ocurrió antes, después o al mismo tiempo que el otro.

## Reglas del contador

> [!tip] Las dos reglas
> 1. **Evento local o envío:** antes de cada evento en $P_z$, se hace $C(P_z) \mathrel{+}= 1$ y el evento queda registrado con ese valor. Al enviar un mensaje se adjunta el valor actual.
> 2. **Recepción:** si $P_z$ recibe un mensaje de $P_i$ con el valor $C(P_i)$, actualiza $C(P_z) = \max(C(P_i), C(P_z)) + 1$ y registra la recepción con ese valor.

Ejemplo cotidiano: si un proceso envía un mensaje con su contador en 5 y el receptor tiene su contador en 1, el receptor registra la recepción con 6, porque sabe que ocurrió después del envío.

## Ejemplo con tres procesos

![Contadores de Lamport en tres procesos](adjuntos/Contadores%20de%20Lamport%20en%20tres%20procesos.png)

> [!example]- Transcripción de la imagen
> Tres procesos (K, A y T) parten con su contador en 0. K tiene los eventos a=1, b=2, c=3 y d=4; A tiene e=1, f=3 (marcado en naranjo) y g=4; T tiene h=1, i=5 (en naranjo) y j=6. Mensajes: b → f, a → j, h → d y g → i.

![Eventos de tres procesos antes de Lamport](adjuntos/Eventos%20de%20tres%20procesos%20antes%20de%20Lamport.png)

> [!example]- Transcripción de la imagen
> El mismo diagrama al inicio: solo están marcados los primeros eventos de cada proceso (a=1, e=1 y h=1) y los contadores iniciales en 0.

Los valores marcados en naranjo son recepciones:

- $f$: A estaba en 1 y recibe el mensaje de $b$ (2): $\max(2, 1) + 1 = 3$.
- $d$: K estaba en 3 y recibe de $h$ (1): $\max(1, 3) + 1 = 4$.
- $i$: T estaba en 1 y recibe de $g$ (4): $\max(4, 1) + 1 = 5$.
- $j$: T estaba en 5 y recibe de $a$ (1): $\max(1, 5) + 1 = 6$.

Los valores se verificaron con una simulación en Python.

## La garantía es solo en una dirección

Con estas reglas se garantiza que **si $a \rightarrow b$, entonces $C(a) < C(b)$**. Por ejemplo, $b$ ocurre antes que $j$, y efectivamente $2 < 6$. Pero **lo contrario no vale**: si $C(a) < C(b)$, no se puede concluir que $a \rightarrow b$.

![Lamport no permite inferir causalidad](adjuntos/Lamport%20no%20permite%20inferir%20causalidad.png)

> [!example]- Transcripción de la imagen
> "Esta relación **es solo en una dirección. No podemos usar el contador para confiar plenamente en la causalidad.**" El proceso A tiene a=1, b=2 y c=3, y envía un mensaje desde c al proceso T. T tiene d=1 y e=4 (la recepción del mensaje de c).

En el ejemplo de tres procesos, $h$ tiene contador 1, menor que $b$, $c$, $f$ y $g$. Sin embargo, $h$ no ocurrió necesariamente antes que ellos: $h$ podría haber ocurrido justo antes de $i$ y los contadores serían los mismos. En el segundo ejemplo, $d$ tiene 1 aunque pudo ocurrir después de todos los eventos de A: tiene 1 simplemente porque es el primer evento de T.

> [!warning] Orden parcial, no orden real
> Los relojes de Lamport generan un **orden parcial** consistente con la causalidad, pero no garantizan que ese orden refleje la realidad ni detectan eventos concurrentes. Si se confía ciegamente en el contador, "pasan cosas raras". Los [[02 - Relojes vectoriales|relojes vectoriales]] resuelven este problema de unidireccionalidad.

Si se necesita un orden **total** (por ejemplo, para desempatar accesos), se ordena por el par (contador, identificador del proceso), la misma idea del [[06 - Algoritmo de la panadería y deadlock|algoritmo de la panadería]].

## Preguntas de repaso

> [!question]- ¿Por qué al recibir un mensaje se toma el máximo y se suma 1?
> El máximo asegura que la recepción quede después de todo lo que el emisor había vivido al enviar (y de lo que el receptor ya había vivido). El +1 cuenta la recepción como un evento nuevo, estrictamente posterior.

> [!question]- Si $C(x) = 2$ y $C(y) = 7$, ¿se puede afirmar que $x \rightarrow y$?
> No. Lamport solo garantiza que $x \rightarrow y$ implica $C(x) < C(y)$. Un contador menor es compatible tanto con que $x$ ocurriera antes como con que $x$ e $y$ sean concurrentes.

> [!question]- En el ejemplo, ¿por qué $h$ tiene contador 1 si pudo ocurrir después de $b$?
> Porque es el primer evento de T y T no había recibido ningún mensaje antes. El contador solo refleja la información causal que llegó al proceso, no el momento real en que ocurrió el evento.
