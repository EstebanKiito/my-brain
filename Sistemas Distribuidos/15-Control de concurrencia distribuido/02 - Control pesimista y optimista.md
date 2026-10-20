---
ramo: "Sistemas Distribuidos"
tema: "Control de concurrencia distribuido"
tags:
  - sd/concurrencia
  - origen/complemento
prerrequisitos:
  - "[[01 - Conflictos por concurrencia]]"
---

# Control pesimista y optimista

Los protocolos de **control de concurrencia** gestionan el acceso simultáneo de varios usuarios o procesos a los mismos datos, para evitar conflictos y mantener la integridad. Hay dos actitudes opuestas: el **pesimista** no confía en nadie y bloquea antes de tocar un dato; el **optimista** supone que los choques son raros, deja avanzar a todos y solo revisa al momento del commit.

## Control pesimista

Evita los conflictos **a medida que ocurren** las operaciones, con exclusión mutua que ordena las transacciones que acceden a un mismo recurso.

- Lo usual es **many readers o single writer**: varias lecturas concurrentes, o una sola escritura.
  - Si hay lecturas en curso, se admiten otras lecturas, pero ninguna escritura hasta que terminen todas.
  - Si hay una escritura, no se admite ninguna otra operación sobre ese dato hasta que termine.
- **Exclusión jerárquica:** distintas granularidades de bloqueo: la base completa, una tabla o una fila.

Es la idea del [[08 - Strict 2PL|Strict 2PL]] y de los [[11 - Locks y registros fantasma|locks]] de las bases de datos.

![Ejemplo de control pesimista con locks](adjuntos/Ejemplo%20de%20control%20pesimista%20con%20locks.png)

> [!example]- Transcripción de la imagen
> T1: Begin, read X, Commit. T2: Begin, write Z, Commit. T3: Begin, write X, write Z, Commit.
> 1. T3 hace write X y bloquea X. 2. T1 quiere read X y espera. 3. T2 hace write Z y bloquea Z. 4. T3 quiere write Z y espera. 5. T2 hace commit y libera Z (la imagen dice "Lock" Z, pero el paso 6 muestra que se liberó). 6. T3 hace write Z, lo bloquea, hace commit y libera Z y X. 7. T1 hace read X, lo bloquea, hace commit y libera X.

> [!warning] Deadlocks distribuidos
> Con exclusión mutua, dos transacciones pueden bloquear cada una un dato que la otra necesita. Soluciones:
> - **Timeout:** la transacción bloqueada aborta tras cierto tiempo y rompe la cadena de espera.
> - **Detección** (la más usada): buscar ciclos en el **grafo de espera** y abortar alguna transacción del ciclo según una heurística.

## Control optimista

"Dale, y después vemos qué pasó." Las transacciones avanzan aisladas hasta que quieren hacer commit; entonces una **fase de validación** busca conflictos. Si los hay, la transacción no hace commit: queda en espera o se aborta, según el sistema. Conviene cuando los conflictos son **poco probables** (por ejemplo, dos transferencias simultáneas a la misma persona común).

![Control optimista con validación al commit](adjuntos/Control%20optimista%20con%20validaci%C3%B3n%20al%20commit.png)

> [!example]- Transcripción de la imagen
> Permite que las transacciones avancen aisladas hasta el commit. Antes de terminar se valida si hay conflictos; si los hay, no se permite el commit (stand-by o aborto). La validación puede usar **timestamps** (comparar la última modificación consolidada con la hora en que empezó la transacción) o **versiones** (cada recurso tiene un contador, y la transacción espera que la versión que vio al empezar siga igual al terminar).

### Validación hacia adelante y hacia atrás

| | Forward validation | Backward validation |
|---|---|---|
| La transacción $T_v$ se compara con | Las transacciones **activas** | Las transacciones **ya consolidadas** durante su vida |
| Se revisan | Las **escrituras** de $T_v$ contra las lecturas de las otras | Las **lecturas** de $T_v$ contra las escrituras de las otras |
| Intención | No invalidar lecturas futuras ("mira adelante") | Asegurar que lo leído siga vigente ("mira atrás") |
| Costo | Seguir las transacciones activas | Guardar el historial de commits |

Con el mismo ejemplo, si los commits se intentan en el orden T3, T1, T2:

- **Forward:** T3 no puede, porque T1 (activa) leyó X, que T3 escribió. T1 sí (no escribió nada) y T2 también (ya no hay activas).
- **Backward:** T3 sí (no hay commits previos). T1 aborta, porque leyó X y T3 lo escribió. T2 sí (no leyó nada).

Ambas validaciones se reprodujeron en Python. Por defecto se validan conflictos lectura-escritura, pero se pueden extender a escritura-escritura.

| | Pesimista | Optimista |
|---|---|---|
| Cuándo actúa | Antes de cada operación | Al commit |
| Costo | Esperas y riesgo de deadlock | Trabajo perdido al abortar |
| Conviene si | Los conflictos son frecuentes | Los conflictos son raros |

## Preguntas de repaso

> [!question]- ¿Por qué el control optimista conviene cuando los conflictos son raros?
> Porque evita el costo de bloquear en cada operación. Si casi nunca hay conflictos, casi nunca se aborta, y el trabajo perdido es poco.

> [!question]- ¿Qué diferencia a la validación forward de la backward?
> Forward compara las escrituras de la transacción con las lecturas de las transacciones aún activas; backward compara sus lecturas con las escrituras de las transacciones que ya hicieron commit mientras ella corría.

> [!question]- ¿Cómo rompe un timeout un deadlock distribuido?
> La transacción que lleva demasiado esperando aborta y libera sus locks; las demás del ciclo pueden avanzar.
