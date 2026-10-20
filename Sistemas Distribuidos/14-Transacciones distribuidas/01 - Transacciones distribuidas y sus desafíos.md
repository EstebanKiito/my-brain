---
ramo: "Sistemas Distribuidos"
tema: "Transacciones distribuidas"
tags:
  - sd/transacciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Transacciones]]"
  - "[[01 - Replicación de datos y modelos de consistencia]]"
---

# Transacciones distribuidas y sus desafíos

Una transferencia bancaria resta dinero de una cuenta y lo suma en otra: si solo ocurre una de las dos partes, el sistema queda inconsistente. Las **transacciones** agrupan operaciones para que ocurran todas o ninguna. Cuando esas operaciones están en **servidores distintos**, aparecen todos los problemas de un sistema distribuido: fallas parciales, latencia y concurrencia entre nodos.

## Transacción

Una **transacción** es una secuencia de operaciones que un cliente solicita a un servidor, diseñada para ejecutarse como una **unidad indivisible**. Busca asegurar la consistencia y la durabilidad de los datos frente a la concurrencia y las fallas.

En una transferencia de A a B hay que restar en A y sumar en B: si solo se completa una parte, el sistema queda inconsistente. Y si varios usuarios depositan a la vez en B, B debe ver la suma total, sin que un depósito se pierda por concurrencia. La versión centralizada está en [[01 - Transacciones|Transacciones]].

| Comando | Qué hace |
|---|---|
| `BEGIN` | Inicia la transacción |
| `READ` | Lee un valor |
| `WRITE` | Escribe (también actualizar o eliminar) |
| `COMMIT` | Consolida los cambios de forma permanente |
| `ABORT` o `ROLLBACK` | Deshace todos los cambios de la transacción |

## Transacción distribuida

Es una transacción gestionada por **múltiples servidores** en distintos computadores. Debe cumplir las mismas propiedades, pero además:

- todos los servidores involucrados **confirman** la transacción, o todos la **cancelan**;
- todos quedan en un estado **consistente**.

Ejemplo: una gran cadena de supermercados mueve dinero entre servidores que ni siquiera están en la misma red, mientras miles de clientes compran o piden devoluciones al mismo tiempo.

## Desafíos

- **Fallas parciales:** un servidor puede caer en medio de la transacción.
- **Heterogeneidad** de la red: componentes de distintos tipos interactúan.
- **Latencia** de comunicación.
- **Concurrencia:** cada recurso debe ser seguro ante solicitudes simultáneas.
- **Interbloqueos distribuidos.**

> [!tip] Serializabilidad de una copia
> Las transacciones distribuidas deben cumplir la **serializabilidad de una copia** (*one-copy serializability*):
> - **Serializabilidad:** el resultado final es el mismo que si las transacciones se hubieran ejecutado una tras otra, en algún orden serial (ver [[05 - Schedules serial y serializable|schedules serializables]]).
> - **De una copia:** aunque haya varias copias de los datos, el comportamiento debe ser el mismo que si existiera una sola.

Para lograrlo, los sistemas suelen usar **locks** que ordenan las transacciones. Pero distintos servidores pueden imponer órdenes distintos y crear **dependencias cíclicas**: el servidor 1 espera que termine T2, el 2 espera a T3 y el 3 espera a T1. Es un **deadlock distribuido**, que se detecta con un **grafo global de espera** (*wait-for graph*), la versión distribuida del [[07 - Grafo de precedencia|grafo de precedencia]].

## Transacciones planas y anidadas

![Transacción plana y anidada de un viaje](adjuntos/Transacci%C3%B3n%20plana%20y%20anidada%20de%20un%20viaje.png)

> [!example]- Transcripción de la imagen
> **Plana:** "¡Me voy de vacaciones!" se divide en T1 (pasaje de ida y vuelta), T2 (estadía en hotel) y T3 (transporte al hotel), todas al mismo nivel. **Anidada:** "Usaré puntos para ahorrar en el paquete de viaje": T0 (paquete de viaje) contiene T1 (pasajes) y T2 (hotel); T1 contiene T3 (pasaje de ida), T4 (pasaje de vuelta) y T5 (puntos); T2 contiene T5 (puntos), T6 (estadía) y T7 (transporte).

En una transacción **anidada**, una transacción contiene sub-transacciones en varios niveles. Ejemplo: pagar los sueldos del mes (nivel 0) se divide en pagar a cada departamento (nivel 1), que se divide en transferir a cada empleado (nivel 2).

- Las sub-transacciones de un mismo nivel pueden ejecutarse **en paralelo**, incluso en servidores distintos.
- Pueden **fallar independientemente**, y la transacción padre puede optar por una alternativa, lo que mejora la recuperación y la flexibilidad.

> [!warning] El commit de una sub-transacción no es definitivo
> Solo cuando la transacción del nivel **superior** hace commit se garantiza que toda la operación perdure.

## Preguntas de repaso

> [!question]- ¿Qué agrega "de una copia" a la serializabilidad?
> Exige que, aunque los datos estén replicados, el resultado sea el mismo que con una sola copia: ningún cliente debe notar que hay réplicas.

> [!question]- ¿Cómo se produce un deadlock distribuido aunque cada servidor ordene bien sus propias transacciones?
> Si cada servidor impone un orden distinto, las esperas entre servidores pueden formar un ciclo (T1 espera a T2, T2 a T3 y T3 a T1). Ningún servidor lo ve completo; hace falta el grafo global de espera.

> [!question]- ¿Qué ventaja tiene una transacción anidada frente a una plana?
> Sus sub-transacciones pueden ejecutarse en paralelo y fallar por separado; la transacción padre puede buscar una alternativa en vez de abortar todo.
