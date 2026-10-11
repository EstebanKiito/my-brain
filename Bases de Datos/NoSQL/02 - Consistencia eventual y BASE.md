---
ramo: Bases de Datos
tema: NoSQL
tags: [bd/nosql, origen/complemento]
prerrequisitos: ["[[01 - Bases de datos NoSQL|Bases de datos NoSQL]]", "[[04 - Escalamiento y teorema CAP|Escalamiento y teorema CAP]]"]
---
# Consistencia eventual y BASE

En una base distribuida no se puede tener a la vez consistencia, disponibilidad y tolerancia a particiones (**CAP**). Como las particiones de red pasan igual, se elige entre un sistema **CP** y uno **AP**. Muchos NoSQL eligen AP con **consistencia eventual** (paradigma **BASE**).

> [!note] El teorema CAP ya está en Ingeniería de Software
> La definición general está en [[04 - Escalamiento y teorema CAP|Escalamiento y teorema CAP]]. Aquí va el enfoque de la clase de bases de datos: los ejemplos AP vs CP y BASE.

> [!tip] Complemento — nota nueva (fuente: slides "Clase 14: NoSQL")
> **Tres propiedades fundamentales en un entorno distribuido:**
> - **Consistency:** todos los usuarios ven lo mismo. A "¿cuántos userID empiezan con 'A'?", las tres réplicas responden 128.
> - **Availability:** todas las consultas siempre reciben una respuesta, aunque sea errónea ("130, quizás").
> - **Partition tolerance:** el sistema funciona bien aunque esté físicamente dividido (un "problema en la red" separa las réplicas).
>
> **Teorema CAP:** en una base de datos distribuida es imposible mantener las tres al mismo tiempo. Como **P es un hecho** en cualquier sistema distribuido, hay que elegir entre C y A: sistemas **CP** o **AP**.
>
> **Ejemplo:** hay 38 userID que empiezan con "Z". Se corta la red entre las réplicas y en un lado se agrega el usuario "Z123".
> | Sistema | Al consultar en la réplica aislada | Prioriza |
> |---|---|---|
> | **AP** | responde **38** (dato viejo, pero responde) | disponibilidad |
> | **CP** | responde **error** (no puede garantizar el valor correcto) | consistencia |

> [!tip] Complemento — BASE y consistencia eventual (slides "Clase 14")
> En la práctica, los sistemas distribuidos fijan la P y **balancean** entre C y A, sin elegir uno de forma exclusiva. Es el paradigma **BASE**:
> - **B**asically **A**vailable: casi siempre responde.
> - **S**oft state: el estado puede cambiar aunque no haya escrituras, porque se están propagando.
> - **E**ventually consistent: si dejan de llegar escrituras, todas las réplicas **terminan** convergiendo.
>
> **Consistencia eventual, paso a paso:** durante la partición se agrega Z123 en una réplica, y por un rato una dice 38 y otra 37. Cuando la red se recupera, el cambio se propaga y ambas dicen 38.
>
> ```mermaid
> sequenceDiagram
>   participant A as Réplica 1
>   participant B as Réplica 2
>   Note over A,B: problema en la red
>   A->>A: + Z123 (38 usuarios Z)
>   Note over B: todavía 37
>   Note over A,B: se recupera la red
>   A->>B: propaga + Z123
>   Note over A,B: ambas: 38
> ```
>
> | ACID (relacional) | BASE (NoSQL) |
> |---|---|
> | consistencia fuerte, inmediata | consistencia eventual |
> | prioriza la corrección | prioriza la disponibilidad y la escala |

## Preguntas de repaso

1. ¿Qué dice el teorema CAP y por qué en la práctica se elige entre C y A?
> [!question]- Respuesta
> Que una base distribuida no puede garantizar a la vez consistencia, disponibilidad y tolerancia a particiones. Como las particiones de red ocurren igual (P es un hecho), hay que sacrificar C o A durante una partición.

2. Durante una partición, ¿qué responde un sistema AP y qué responde uno CP?
> [!question]- Respuesta
> El AP responde con el dato que tiene, aunque pueda estar desactualizado. El CP responde error si no puede garantizar el valor correcto.

3. ¿Qué significa BASE?
> [!question]- Respuesta
> Basically Available, Soft state, Eventually consistent: casi siempre disponible, con estado que cambia mientras se propagan los datos, y consistente cuando las réplicas convergen.

4. ¿Qué es la consistencia eventual?
> [!question]- Respuesta
> La garantía de que, si no llegan más escrituras, todas las réplicas terminan con el mismo valor. Mientras tanto, pueden responder valores distintos.
