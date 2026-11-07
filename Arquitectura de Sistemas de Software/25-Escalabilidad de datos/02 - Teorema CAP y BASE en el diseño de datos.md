---
ramo: "Arquitectura de Sistemas de Software"
tema: "Escalabilidad de datos"
tags:
  - arquisis/escalabilidad
  - arquisis/datos
  - origen/complemento
prerrequisitos:
  - "[[01 - Índices query tuning y datos por servicio]]"
  - "[[01 - Teorema CAP]]"
  - "[[02 - Teorema PACELC]]"
---

# Teorema CAP y BASE en el diseño de datos

Apenas los datos se reparten entre varias máquinas aparece una pregunta inevitable: si la red se corta entre dos nodos, ¿qué hacemos? El **teorema CAP** formaliza la respuesta, y es una de las preguntas de desarrollo más frecuentes en las pruebas.

## El teorema

> [!tip] CAP
> **Consistency, Availability, Partition tolerance.** En un sistema particionado en red, **solo podemos tener 2 de los 3**. Fue una conjetura de Brewer (2000), demostrada por Gilbert y Lynch (2002).

- **Consistencia (C):** todos los nodos ven el mismo dato al mismo tiempo; una lectura devuelve la última escritura.
- **Disponibilidad (A):** toda petición recibe una respuesta, aunque algún nodo esté caído.
- **Tolerancia a particiones (P):** el sistema sigue funcionando aunque se pierdan mensajes entre nodos.

![Dos nodos A y B separados por una partición, con las tres combinaciones de CAP](adjuntos/Teorema%20CAP%20con%20dos%20nodos%20y%20una%20partición.png)

> [!example]- Transcripción de la imagen
> - Dos nodos, **A** y **B**, unidos por una flecha de replicación cortada por un rayo (una partición). Una estrella escribe en A y una carita lee desde B.
> - Tres frases: *Availability + Partition tolerant = No Consistency*; *Consistency + Partition tolerant = No Available*; *Consistency + Availability = No Partition tolerant*.

**Leyendo la figura:** se escribe en A y se lee en B mientras la red está cortada.
- Si B responde con lo que tiene, el sistema está **disponible** pero puede devolver un dato viejo: **AP**, sin consistencia.
- Si B se niega a responder hasta poder hablar con A, es **consistente** pero **no disponible**: **CP**.
- **CA** solo es posible si no hay particiones, es decir, en un solo nodo o una red que nunca falla. En un sistema distribuido real, **P no se elige**: las particiones ocurren. La decisión real es **C o A durante una partición**.

## CAP doce años después

En 2012 Brewer revisó su propio teorema y señaló sus límites:
- **No considera la latencia.** PACELC lo agrega: si no hay partición, igual hay que elegir entre latencia y consistencia.
- **No considera los mecanismos actuales** para gestionar las particiones.
- **No considera la compensación**: reparar las inconsistencias después de que la partición termina.

## ACID frente a BASE

| | ACID (relacional típico) | BASE (NoSQL típico) |
|---|---|---|
| Significado | Atomicidad, Consistencia, Aislamiento, Durabilidad | ***Basically Available*, *Soft state*, *Eventually consistent*** |
| Prioriza | Consistencia | Disponibilidad y escala |
| Escrituras | Transaccionales: si algo falla, se revierte todo | Rápidas; los nodos convergen después |
| Lecturas | Siempre el último valor confirmado | Pueden ser viejas por un tiempo |
| Riesgo | Menor disponibilidad y escala más difícil | Race conditions y datos desactualizados |

*Soft state* significa que el estado puede cambiar sin nuevas escrituras mientras converge. La caché es un ejemplo de *soft state*.

> [!example]- Respuesta modelo: inventario y transacciones con relacional o NoSQL
> En un e-commerce, el **enfoque relacional** (ACID) mantiene la consistencia: una compra que descuenta stock y registra el pago se guarda completa o se revierte, y se evitan race conditions en las lecturas (nadie compra el último producto dos veces).
> El **enfoque NoSQL** (BASE) permite escrituras más rápidas y disponibilidad alta, pero la información no siempre es consistente. En las transacciones de dinero eso puede producir descuadres, así que para pagos conviene ACID. Para el catálogo o las reseñas, BASE es aceptable.

> [!example]- Respuesta modelo: sensores en una mina con particiones constantes
> **Contexto:** sensores de calidad del aire y de derrumbes en el subsuelo, con particiones de red constantes y prolongadas.
> - **Priorizar C:** los nodos aislados no reportan hasta poder sincronizar. Se evitan datos contradictorios, pero se pierden alertas justo cuando más importan.
> - **Priorizar A:** cada zona sigue registrando y emitiendo alertas localmente, y se reconcilia al reconectar.
> - **Elección:** **AP**, porque una alerta de derrumbe retrasada es peor que un dato temporalmente inconsistente.
> - **Con PACELC, sin partición:** se puede preferir **baja latencia (EL)** para que las alertas lleguen rápido, aceptando consistencia eventual.

## Preguntas de repaso

> [!question]- Enuncie el teorema CAP y explique por qué en la práctica la elección es entre C y A.
> En un sistema distribuido con particiones de red solo se pueden garantizar dos de las tres propiedades: consistencia, disponibilidad y tolerancia a particiones. Como en una red real las particiones ocurren, P es obligatoria, y la decisión es si durante la partición se sacrifica la consistencia (AP) o la disponibilidad (CP).

> [!question]- En la figura de los nodos A y B, ¿qué hace un sistema CP y qué hace uno AP cuando se lee en B durante la partición?
> El CP se niega a responder (o devuelve un error) hasta poder confirmar con A, así que no está disponible pero no entrega datos viejos. El AP responde con el valor que tiene B, quizás desactualizado: sigue disponible pero no es consistente.

> [!question]- ¿Qué críticas hizo Brewer a su propio teorema en 2012?
> Que no considera la latencia, que no considera los mecanismos modernos para manejar las particiones y que no considera la compensación de inconsistencias después de una partición. De ahí surgen PACELC y el diseño con consistencia eventual y reconciliación.

> [!question]- ¿Qué significa BASE y en qué se diferencia de ACID?
> Basically Available, Soft state, Eventually consistent: el sistema prioriza estar disponible, su estado puede cambiar mientras converge y las réplicas se vuelven consistentes con el tiempo. ACID, en cambio, garantiza transacciones atómicas, consistentes, aisladas y durables, a costa de disponibilidad y escala.

> [!question]- ¿Por qué la caché es un ejemplo de "soft state"?
> Porque su contenido puede expirar o invalidarse sin que nadie escriba, y puede no coincidir con la fuente de verdad por un tiempo. Es estado que se reconstruye, no la fuente de verdad.

> [!question]- Mini caso: un banco y una red social deben elegir entre CP y AP para su dato principal. ¿Qué elige cada uno?
> El banco elige CP para los saldos: es preferible rechazar una operación durante una partición antes que permitir un doble gasto. La red social elige AP para el feed y los likes: es preferible mostrar un contador levemente desactualizado antes que no mostrar nada.

> [!question]- V o F: "Un sistema distribuido puede elegir ser CA para tener consistencia y disponibilidad".
> Falso en la práctica. CA solo es posible si no hay particiones, es decir, en un solo nodo o en una red que nunca falla. En un sistema distribuido real las particiones ocurren, así que hay que elegir entre C y A durante ellas.
