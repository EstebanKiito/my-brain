---
ramo: "Sistemas Distribuidos"
tema: "Transacciones distribuidas"
tags:
  - sd/transacciones
  - origen/complemento
prerrequisitos:
  - "[[01 - Transacciones distribuidas y sus desafíos]]"
  - "[[02 - Propiedades ACID]]"
---

# Propiedades ACID en transacciones distribuidas

Las propiedades **ACID** son los pilares de la fiabilidad de una transacción. En una base de datos centralizada (ver [[02 - Propiedades ACID|Propiedades ACID]]) las garantiza un solo motor; en una transacción distribuida, cada propiedad debe cumplirse **en todos los nodos a la vez**, y eso es lo que vuelve necesarios protocolos como el commit de dos fases.

## Las cuatro propiedades

**A, atomicidad:** la transacción es indivisible: todas sus operaciones se completan o ninguna. Si algo falla (por ejemplo, un servidor), se borran todos sus efectos. Una vez terminada (commit o abort), la transacción queda cerrada y no admite más operaciones. En un sistema distribuido, además, **todos los nodos participantes la aceptan o ninguno**.

**C, consistencia:** una transacción exitosa lleva el sistema de un estado consistente a otro, sin violar reglas ni invariantes. Por ejemplo, no aceptar un pago que supera el cupo de la tarjeta, ni sacar dinero de una cuenta bloqueada. Muchas veces es responsabilidad de quien programa el servidor.

**I, aislamiento:** cada transacción se ejecuta sin interferencia de las concurrentes. Sus efectos intermedios no son visibles hasta el commit. Evita:

- **Lecturas sucias** (*dirty reads*): leer un valor escrito por otra transacción que aún no hace commit. Si esa transacción aborta, se leyó un dato que nunca existió. Ver [[04 - Lecturas sucias, no repetibles y actualización perdida|lecturas sucias]].
- **Escrituras prematuras** (*premature writes*): escribir en la base antes de garantizar el commit. Si se resta dinero de una cuenta y el sistema falla antes del commit, la transacción no ocurrió, pero la base ya cambió.

**D, durabilidad:** tras un commit exitoso, los efectos quedan en almacenamiento permanente y sobreviven a cualquier falla del servidor. En transacciones anidadas, solo el commit del **nivel superior** garantiza que todo perdure.

## Cómo puede violar ACID cada comando

| Comando | Viola atomicidad si… | Viola consistencia si… | Viola aislamiento o durabilidad si… |
|---|---|---|---|
| `WRITE` | Se ejecuta después de un commit o abort | Escribe un valor que no corresponde al sistema | Modifica la base visible para todos antes del commit (escritura prematura) |
| `READ` | Se ejecuta después de un commit o abort | Lee una variable que no existe | Lee un valor de otra transacción no consolidado (lectura sucia) |
| `COMMIT` | No logra completarse en todos los nodos involucrados | Consolida aunque una operación ya violó alguna propiedad | – |
| `ABORT` | – | – | Intenta abortar una transacción ya consolidada (viola durabilidad) |

> [!tip] El punto crítico distribuido
> La atomicidad es la más difícil de mantener entre nodos: un `COMMIT` que solo algunos servidores alcanzan a aplicar deja el sistema partido. Coordinar ese momento es el trabajo de los protocolos de commit.

> [!warning] Consistencia ACID no es consistencia de réplicas
> La "C" de ACID habla de respetar las reglas del negocio. Los modelos de consistencia de la replicación (fuerte, secuencial, eventual) hablan de qué valor ve cada réplica. Son conceptos distintos con el mismo nombre.

## Preguntas de repaso

> [!question]- ¿Qué agrega la atomicidad en una transacción distribuida respecto de una local?
> Que la decisión sea la misma en todos los nodos: o todos los servidores aplican la transacción o ninguno, aunque alguno falle a mitad de camino.

> [!question]- ¿Por qué una escritura prematura viola el aislamiento?
> Porque deja visible en la base un efecto intermedio antes del commit. Otras transacciones pueden leerlo, y si la transacción falla, la base queda con un cambio que nunca debió ocurrir.

> [!question]- ¿Qué propiedad viola un `ABORT` sobre una transacción ya consolidada?
> La durabilidad: un commit exitoso garantiza que sus efectos permanecen, y deshacerlo contradice esa promesa.
