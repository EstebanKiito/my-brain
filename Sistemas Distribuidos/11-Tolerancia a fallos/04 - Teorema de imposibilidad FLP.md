---
ramo: "Sistemas Distribuidos"
tema: "Tolerancia a fallos"
tags:
  - sd/tolerancia-a-fallos
  - sd/consenso
  - origen/complemento
prerrequisitos:
  - "[[03 - Detección de fallos y redundancia]]"
  - "[[01 - Algoritmos de consenso]]"
---

# Teorema de imposibilidad FLP

Paxos y Raft funcionan bien en la práctica, pero ¿existe un algoritmo de consenso que **siempre** termine y **nunca** se equivoque, aun si un nodo puede fallar? En 1985, Fischer, Lynch y Paterson demostraron que, en un sistema completamente asíncrono, **no**. El teorema no dice que el consenso sea inútil, sino qué supuestos hacen falta para lograrlo.

## El teorema

- Demostrado en **1985** por **Michael J. Fischer, Nancy A. Lynch y Michael S. Paterson** (*Impossibility of Distributed Consensus with One Faulty Process*).
- Es un resultado fundamental de la teoría de los sistemas distribuidos y ganó el **premio Dijkstra** en 2001, que reconoce trabajos cuyo impacto en la computación distribuida ha sido evidente durante al menos una década.

> [!tip] Enunciado
> En un sistema **completamente asíncrono**, es **imposible garantizar el consenso** si incluso **un solo proceso** puede fallar.

- **La razón:** no se puede distinguir entre un proceso **muy lento** y uno que se **bloqueó**. Esperar al lento puede ser esperar para siempre; ignorarlo puede significar decidir sin él cuando su voto era clave.
- **La implicación:** en un sistema asíncrono es imposible **garantizar** la tolerancia a fallos del consenso.

"Completamente asíncrono" significa que no hay cota para el tiempo que tarda un mensaje ni para la velocidad de un proceso. Es el mismo dilema de los timeouts de la [[03 - Detección de fallos y redundancia|detección de fallos]], llevado al límite.

## Qué significa en la práctica

El teorema fija una **cota superior** para los algoritmos de consenso tolerantes a fallas: ningún algoritmo puede superarla. Por eso hay que ser riguroso con los supuestos de cada algoritmo distribuido. Afirmar que se garantiza consenso total en un sistema asíncrono sería mentir.

## Estrategias para vivir con el teorema

| Estrategia | Idea | Ejemplo |
|---|---|---|
| **Asumir sincronía parcial** | Agregar límites de tiempo al sistema asíncrono | Timeouts en Bully o en el election timeout de Raft |
| **Consenso parcialmente correcto** | Decidir con un **quórum** (mayoría) | Paxos y Raft avanzan con más del 50 % de los nodos |
| **Relajar las garantías** | En vez de "garantizar el consenso", lograrlo "con alta probabilidad" | Timeouts aleatorios de Raft, Proof of Work |

> [!warning] Paxos no contradice FLP
> Paxos nunca decide algo incorrecto (safety), pero no garantiza terminar: el livelock de [[04 - Casos borde y garantías de Paxos|los casos borde]] es exactamente el escenario que el teorema dice que no se puede eliminar del todo. Los timeouts y retrasos aleatorios lo vuelven improbable, no imposible.

## Preguntas de repaso

> [!question]- ¿Por qué el teorema necesita que el sistema sea completamente asíncrono?
> Porque si hay una cota conocida para los retrasos, un timeout permite distinguir un proceso caído de uno lento. Sin esa cota, cualquier espera puede ser insuficiente y el algoritmo no puede decidir con certeza.

> [!question]- ¿Qué propiedad sacrifican en la práctica algoritmos como Paxos frente a FLP?
> La terminación garantizada: mantienen siempre el acuerdo, pero en escenarios adversos (como un livelock) podrían no terminar. Se mitiga con timeouts y aleatoriedad.

> [!question]- ¿Por qué el teorema habla de un solo proceso propenso a fallos?
> Para mostrar lo fuerte del resultado: basta con que uno solo pueda fallar, aunque nunca lo haga, para que ningún algoritmo pueda garantizar el consenso en un sistema asíncrono.
