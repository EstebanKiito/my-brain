---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, ingsoft/scrum, origen/complemento]
prerrequisitos: ["[[01 - Story points|Story points]]", "[[06 - Sprint|Sprint]]"]
---
# Velocidad de desarrollo

> [!tip] Complemento — nota nueva (fuente: slides "SCRUM - Planificación y Estimación" y libro del curso, cap. 5.2)
> **Qué es:** la velocidad es el **número de story points que un equipo puede completar en un sprint**. Responde a: ¿cuántos puntos puedo manejar en un sprint?
>
> **Cómo se calcula:**
> 1. En cada sprint pasado se **suman los puntos de las historias terminadas**. **No se incluyen las historias hechas a la mitad.**
> 2. Se **promedia** sobre los sprints anteriores.
>
> **Ejemplo 1: un sprint (slides)**
> | Historia | Story points |
> |---|---|
> | A user can… | 4 |
> | A user can… | 3 |
> | A user can… | 5 |
> | A user can… | 3 |
> | A user can… | 2 |
> | A user can… | 4 |
> | A user can… | 2 |
> | **Velocidad** | **23** |
>
> **Ejemplo 2: promedio de varios sprints (slides)**
> | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 | Sprint 5 | Sprint 6 | Sprint 7 |
> |---|---|---|---|---|---|---|
> | 80 | 70 | 95 | 105 | 130 | 110 | 120 |
>
> Promedio = 710 / 7 ≈ 101 → **velocidad ≈ 100** puntos por sprint.
>
> **¿Y si es mi primer sprint?** Es difícil adivinar cuántos puntos se podrán manejar. Una estrategia es decidir en equipo qué historias se **intentarán** terminar en el sprint 1, **sin el compromiso** de acabarlas todas. Desde el sprint 2 ya hay historia para calcular la velocidad.

> [!tip] Complemento — usar la velocidad para elegir historias (libro, cap. 5.2)
> En el [[07 - Sprint Planning|Sprint Planning]] se eligen historias de **alta prioridad** cuya suma de puntos **se acerque a la velocidad**.
>
> Ejemplo: backlog en orden de prioridad A (4), B (8), C (2), D (12), E (4), F (16), con **velocidad 12**. En el próximo sprint conviene tomar **A y B** (4 + 8 = 12). C ya no cabe.

> [!warning] Error común
> Usar la velocidad para **comparar equipos** o como meta de productividad ("este sprint hay que subir a 30"). Los puntos son relativos a cada equipo, y presionar la velocidad solo infla las estimaciones.

## Preguntas de repaso

1. ¿Cómo se calcula la velocidad de un equipo?
> [!question]- Respuesta
> Se suman los story points de las historias completadas al 100% en cada sprint anterior y se promedian esos totales.

2. Un equipo terminó historias de 5, 3, 8 y dejó a medias una de 5. ¿Cuál fue la velocidad de ese sprint?
> [!question]- Respuesta
> 16 puntos (5 + 3 + 8). La historia a medias no cuenta.

3. ¿Qué se hace en el primer sprint, cuando aún no hay velocidad?
> [!question]- Respuesta
> El equipo decide en conjunto qué historias intentará terminar, sin comprometerse a acabarlas todas. A partir del segundo sprint usa lo ocurrido para calcular la velocidad.

4. Con velocidad 10 y un backlog priorizado A (3), B (5), C (5), D (2), ¿qué historias entran al sprint?
> [!question]- Respuesta
> A y B (8 puntos). C ya excede la velocidad (13). Respetando la prioridad, D podría evaluarse para completar 10, pero solo si el PO acepta adelantarla a C.
