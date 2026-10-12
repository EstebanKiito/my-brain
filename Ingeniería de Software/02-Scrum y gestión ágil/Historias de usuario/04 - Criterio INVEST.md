---
ramo: Ingeniería de Software
tema: Historias de usuario
tags: [ingsoft/requisitos, origen/complemento]
prerrequisitos: ["[[02 - Estructura de una historia de usuario|Estructura de una historia de usuario]]"]
---
# Criterio INVEST

> [!tip] Complemento — nota nueva (fuente: slides "Historias de Usuario" y libro del curso, cap. 4.5)
> **Qué es:** INVEST es un **criterio de calidad** para historias de usuario. Cada letra es una propiedad que debe cumplir una buena historia.
>
> | Letra | Propiedad | Significado |
> |---|---|---|
> | **I** | Independiente | Independiente de las demás, o débilmente relacionada. Así se puede reordenar según la prioridad. |
> | **N** | Negociable | No es un contrato ni una especificación: es una referencia a una característica que el equipo debe discutir. |
> | **V** | Valiosa | Aporta **valor al usuario** y describe características del sistema. |
> | **E** | Estimable | Tiene suficiente detalle para estimar su costo o tiempo. |
> | **S** | Small (pequeña) | Se puede completar **dentro de un sprint**. |
> | **T** | Testable (verificable) | Tiene suficiente información para comprobar que está completada (condiciones de aceptación). |

> [!example] Ejemplo extra — evaluar una historia con INVEST
> *"Como alumno quiero usar la app"*.
> - **No es valiosa ni testable:** no dice qué ni para qué.
> - **No es estimable ni pequeña:** es toda la app.
>
> Versión mejorada: *"Como alumno necesito ver mis notas del semestre para saber si estoy aprobando"*, con un escenario Dado/Cuando/Entonces. Ahora es pequeña, valiosa, estimable y testable.

> [!tip] Complemento — relación con otras notas
> - Para que sea **Small**, se aplican las técnicas de [[07 - Cómo dividir historias de usuario|cómo dividir historias]].
> - Para que sea **Testable**, se escriben [[03 - Criterios de aceptación (Dado-Cuando-Entonces)|criterios de aceptación]].
> - Si no cumple con la V, suele ser una historia técnica ([[05 - Errores comunes en historias de usuario|error común]]).

## Preguntas de repaso

1. ¿Qué significa cada letra de INVEST?
> [!question]- Respuesta
> Independiente, Negociable, Valiosa, Estimable, Small (pequeña) y Testable (verificable).

2. ¿Por qué una historia debe ser "negociable"?
> [!question]- Respuesta
> Porque no es un contrato cerrado: es una referencia a una necesidad que el equipo y el PO conversan y ajustan.

3. ¿Qué tamaño debe tener una historia según INVEST?
> [!question]- Respuesta
> Debe poder realizarse dentro de un sprint (según el libro, implementable en unos pocos días).

4. ¿Por qué conviene que las historias sean independientes?
> [!question]- Respuesta
> Para poder priorizarlas y reordenarlas libremente y planificar sprints sin bloqueos entre historias.
