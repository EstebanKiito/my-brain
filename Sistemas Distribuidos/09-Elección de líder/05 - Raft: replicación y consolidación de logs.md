---
ramo: "Sistemas Distribuidos"
tema: "Elección de líder"
tags:
  - sd/eleccion-de-lider
  - sd/consenso
  - origen/complemento
prerrequisitos:
  - "[[03 - Raft: estados y elección del líder]]"
---

# Raft: replicación y consolidación de logs

Una vez elegido el líder, Raft logra el consenso sobre una **secuencia** de acciones: el líder las registra en su **log** y lo copia a los seguidores. La pregunta difícil es cuándo una acción queda **consolidada**, es decir, cuándo ya no puede perderse aunque cambie el líder. La respuesta de Raft es sutil: no basta con que la mayoría la tenga.

## Logs y replicación

- Un **log** es una lista de tuplas: cada una tiene la operación y el **term** en que se creó.
- El líder recibe las operaciones y las guarda en su log. Si un seguidor recibe una operación, la **redirige al líder**.
- El líder intenta replicar su log en los seguidores. Si en una posición hay **conflicto** entre la tupla del líder y la del seguidor, **gana la del líder**.

![Raft replica el log del líder](adjuntos/Raft%20replica%20el%20log%20del%20l%C3%ADder.png)

> [!example]- Transcripción de la imagen
> El líder, con log $[(A_1,1),(A_2,1),(A_3,2)]$, dice "¡Vamos a replicar mis logs!". Un seguidor con $[(A_1,1),(A_2,1),(A_4,2),(A_5,2)]$ queda con $[(A_1,1),(A_2,1),(A_3,2)]$: $A_4$ y $A_5$ se reemplazan. Otro seguidor con $[(A_1,1)]$ queda con $[(A_1,1),(A_2,1),(A_3,2)]$.

## Consolidación directa

> [!tip] Regla
> Una acción se consolida **directamente** solo si fue replicada a la **mayoría** de los nodos **en el mismo term en que fue creada**.

Por ejemplo, si en el term 1 el líder y un seguidor tienen $A_1$ y $A_2$ (2 de 3 nodos, con uno caído), ambas quedan consolidadas.

El ejemplo de las slides muestra por qué hace falta la condición del term. Hay 5 nodos, A a E, con timeouts 1, 5, 4, 3 y 2:

1. **Term 1:** A es líder (menor timeout), crea $(A_1, 1)$ y lo replica solo a B. Luego A cae.
2. **Term 2:** E es líder con los votos de C y D, y crea $(A_2, 2)$. Luego E cae.
3. **Term 3:** A vuelve, recupera el liderazgo y replica $A_1$ a C. Ahora A, B y C tienen $A_1$: es mayoría… pero se creó en el term 1, no en el 3, así que **no** se consolida.
4. **Term 4:** A cae y E vuelve a ser líder (su último log es del term 2, el más reciente). Replica su log, y $(A_2, 2)$ reemplaza a $A_1$ en B y C.

![Raft A2 en mayoría pero no consolidada](adjuntos/Raft%20A2%20en%20mayor%C3%ADa%20pero%20no%20consolidada.png)

> [!example]- Transcripción de la imagen
> Tabla de terms 1 a 4 para A-1 (caído), B-5, C-4, D-3 y E-2 (líder). En el term 4, B, C, D y E tienen $(A_2,2)$; A conserva $(A_1,1)$. Texto: "E replica sus logs a todos los nodos activos. Ahora $A_1$ ni siquiera está en la mayoría. Pero $A_2$ ahora sí está en mayoría, ¿debería ser consolidado?… No".

$A_2$ tampoco se consolida, porque se creó en el term 2 y llegó a la mayoría en el term 4. Y con razón: si en el term 3 A hubiera creado $(A_3, 3)$, al volver podría ganar la elección con un log del term 3 y sobrescribir $A_2$.

![Raft puede sobrescribir A2](adjuntos/Raft%20puede%20sobrescribir%20A2.png)

> [!example]- Transcripción de la imagen
> Variante en que A creó $(A_3, 3)$ en el term 3. En el term 4, B, C, D y E tienen $(A_2,2)$ y A tiene $(A_1,1)(A_3,3)$. "Si A vuelve y E se cae, el último log de A tiene un term mayor a todos. A es líder y puede hacer que $A_2$ se sobrescriba."

## Consolidación indirecta

> [!tip] Regla
> Una acción se consolida **indirectamente** si en el log existe una acción **posterior** que fue consolidada directamente.

![Raft consolidación indirecta](adjuntos/Raft%20consolidaci%C3%B3n%20indirecta.png)

> [!example]- Transcripción de la imagen
> En el term 3, A replica $(A_1,1)(A_3,3)$ a C y D. "$A_3$ fue consolidada directamente. Por lo tanto, $A_1$ fue consolidada indirectamente. Mientras exista mayoría de nodos (requisito del algoritmo), el líder será A, C o D, que tienen $A_1$ y $A_3$."

Como $A_3$ se creó y llegó a la mayoría en el mismo term 3, queda consolidada, y con ella todo lo anterior en el log, incluida $A_1$. Así, una acción que no se consolidó en su term **sí puede consolidarse** en un term posterior, de forma indirecta.

## Garantías y uso real

- Las mismas que Paxos: pueden fallar $\lfloor (N-1)/2 \rfloor$ nodos, y si la red se parte, sigue funcionando el lado con mayoría.
- **etcd** (base de datos clave-valor que usan Kubernetes y Docker Swarm) gestiona su log replicado con Raft; **Neo4j** (grafos, usada por eBay) y **ScyllaDB** (NoSQL, usada por Discord y Disney+) también lo usan.

> [!warning] Afirmaciones falsas típicas
> - "Una operación que no se consolidó en su term nunca podrá consolidarse": **falso**, puede consolidarse indirectamente.
> - "Si una operación llega a la mayoría tras varios terms, queda consolidada": **falso**, como muestra $A_2$.
> - En cambio, sí es cierto que se consolida si llega a la mayoría en su mismo term, y que en un term se pueden consolidar varias operaciones.

## Preguntas de repaso

> [!question]- ¿Por qué Raft exige que la acción llegue a la mayoría en el mismo term en que se creó?
> Porque una acción de un term antiguo puede estar en la mayoría y aun así ser sobrescrita por un líder futuro cuyo último log es de un term más reciente. Solo si llegó a la mayoría en su propio term se garantiza que cualquier líder futuro la tendrá.

> [!question]- ¿Qué pasa con el log de un seguidor que tiene tuplas distintas a las del líder?
> En las posiciones en conflicto gana el líder: las tuplas del seguidor se reemplazan por las del líder.

> [!question]- ¿Cómo queda consolidada $A_1$ si nunca se consolidó en el term 1?
> Indirectamente: cuando $A_3$, posterior en el log, se consolida directamente en el term 3, todo lo anterior a ella en ese log queda consolidado también.
