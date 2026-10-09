---
ramo: Ingeniería de Software
tema: Testing
tags: [ingsoft/testing, origen/complemento]
prerrequisitos: ["[[01 - Qué es el testing de software|Qué es el testing de software]]"]
---
# Error, defecto y falla

> [!tip] Complemento — nota nueva (fuente: slides "Testing")
> **Qué es:** la clasificación inicial de los problemas del software.
>
> | Término | Definición |
> |---|---|
> | **Error** | **acción humana** que produce un resultado incorrecto |
> | **Defecto** (bug) | presencia de una **imperfección** en el software que puede ocasionar fallas |
> | **Falla** | **comportamiento observable incorrecto** con respecto a los requisitos |
>
> **¿Están relacionados?** Sí: un **error** introduce un **defecto** en el software, que se manifiesta a través de una **falla** en las pruebas o en el uso.
>
> ```mermaid
> flowchart LR
>   E["Error (persona)"] --> D["Defecto (en el código)"] --> F["Falla (comportamiento observable)"]
> ```
>
> **Qué puede salir mal** (slides): errores en la especificación, el diseño o la implementación; errores en el uso del sistema; condiciones del ambiente; daño intencional; entre otros.

> [!example] Ejemplo extra
> Una programadora confunde `<` con `<=` (**error**). El código queda con la condición `if edad < 18` en vez de `<= 17`… o al revés (**defecto**). Una persona de 18 años no puede registrarse (**falla**). Un defecto puede existir sin producir fallas mientras no se ejecute esa línea con ese dato.

## Preguntas de repaso

1. Define error, defecto y falla.
> [!question]- Respuesta
> Error: acción humana equivocada. Defecto: la imperfección que queda en el software. Falla: el comportamiento incorrecto observable respecto de los requisitos.

2. ¿Cómo se relacionan?
> [!question]- Respuesta
> Un error introduce un defecto, y el defecto se manifiesta como una falla cuando se ejecuta esa parte del código.

3. ¿Puede existir un defecto sin que haya una falla?
> [!question]- Respuesta
> Sí. Si el código defectuoso nunca se ejecuta, o nunca con los datos que lo gatillan, la falla no se observa.
