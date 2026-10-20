---
ramo: "Sistemas Distribuidos"
tema: "Control de concurrencia distribuido"
tags:
  - sd/concurrencia
  - origen/complemento
prerrequisitos:
  - "[[02 - Control pesimista y optimista]]"
  - "[[05 - Consistencia eventual]]"
---

# Resolución de conflictos concurrentes

Evitar todo conflicto cuesta disponibilidad. Muchos sistemas eligen lo contrario: **dejar que ocurran** y resolverlos después con una política. Esto rompe la serializabilidad de una copia, y la política elegida tiene un impacto directo en la experiencia del usuario y en la complejidad del sistema.

## Características

- No es excluyente con el control de concurrencia: un sistema puede usar ambos en capas distintas. Por ejemplo, cada archivo lo accede un solo nodo a la vez (pesimista), pero varias personas que usan ese nodo lo editan y generan conflictos que hay que resolver.
- Las políticas tampoco son excluyentes: se pueden combinar.

En los ejemplos, dos usuarios cambian a la vez el título de un informe: uno escribe "uwu" y otro "Yo".

## Políticas

| Política | Cómo resuelve | Ejemplo real | Resultado en el informe |
|---|---|---|---|
| **Last write wins** | Gana la versión con el timestamp más reciente | DynamoDB | Queda el último título; el otro se pierde |
| **Versionamiento** | Conserva varias versiones: una actual y otras en el historial, o recursos separados | Dropbox ("copia en conflicto") | Dos informes, "uwu" y "Yo" |
| **Merge manual** | Obliga a un usuario a resolver antes de seguir | Git | "No puedo con ambos; indícame con cuál me quedo" |
| **Merge semántico** | Usa conocimiento de la aplicación, indicado por el usuario o por defecto | `git merge -X ours` / `-X theirs` | "uwu" lo hizo alguien de rol superior: gana "uwu" |
| **Operational Transformation (OT)** | No compara estados: transforma las **operaciones** para que puedan aplicarse en cualquier orden | Google Docs | `Insert("uwu", 0)` e `Insert("Yo", 3)`: queda "uwuYo" |
| **CRDT** (*Conflict-free Replicated Data Types*) | Estructuras diseñadas para converger automáticamente mediante reglas algebraicas | League of Legends (Riak) | Título = {"uwu"} ∪ {"Yo"}: "uwuYo" |

![Comparación de políticas de resolución de conflictos](adjuntos/Comparaci%C3%B3n%20de%20pol%C3%ADticas%20de%20resoluci%C3%B3n%20de%20conflictos.png)

> [!example]- Transcripción de la imagen
> | Protocolo | Cómo resuelve | Pros | Contras |
> |---|---|---|---|
> | Last Write Wins | Se queda con el valor de timestamp mayor | Simple | Pierde datos concurrentes |
> | Versiones | Genera más de un recurso | Simple | Costoso en almacenamiento |
> | Merge manual | Un usuario o proceso decide qué versión conservar | Preciso | Costoso, lento, requiere intervención |
> | Merge semántico | Usa lógica del dominio para combinar versiones | Automatizado y preserva más información | Requiere lógica específica por tipo de dato, complejo de implementar |
> | Operational Transformation | Reescribe operaciones para que puedan aplicarse en cualquier orden | Automatizado y preserva más información | Igual que el anterior |
> | CRDTs | Diseñados para que todas las operaciones concurrentes se combinen sin conflicto | Automatizado y preserva más información | Limitado a tipos de datos específicos |

> [!tip] CRDT en una línea
> Si la operación de combinar es **conmutativa, asociativa e idempotente** (como la unión de conjuntos), no importa en qué orden ni cuántas veces lleguen las actualizaciones: todas las réplicas convergen al mismo valor.

## Ejemplo de aplicación

Un sistema de monitoreo médico recibe datos de muchos sensores (ritmo cardíaco, presión, oxigenación) sobre el mismo paciente. Debe estar **siempre disponible**, aunque nadie lo revise, y **perder datos** por un conflicto puede costar vidas.

- Pesimista u optimista: bloquear o abortar escrituras resta disponibilidad.
- Last write wins: pierde datos.
- Merge manual: requiere que alguien esté revisando.
- **Versionamiento:** conserva todas las versiones sin intervención. Es la estrategia más apropiada.

> [!warning] Last write wins no es inocente
> Depende de relojes sincronizados: si el reloj de un nodo está adelantado, sus escrituras "ganan" siempre, aunque hayan ocurrido antes.

## Preguntas de repaso

> [!question]- ¿Por qué el versionamiento es mejor que last write wins para datos médicos?
> Porque last write wins descarta las escrituras concurrentes, mientras que el versionamiento conserva todas sin necesitar que alguien intervenga.

> [!question]- ¿Qué distingue a Operational Transformation de un merge que compara estados?
> OT no compara los resultados finales: ajusta las operaciones (por ejemplo, la posición de un insert) para que, aplicadas en cualquier orden, produzcan el mismo documento.

> [!question]- ¿Cuál es la limitación principal de los CRDT?
> Solo existen para ciertos tipos de datos (contadores, conjuntos, registros, etc.) cuyas operaciones se pueden combinar algebraicamente sin conflicto.
