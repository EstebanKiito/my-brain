---
ramo: Ingeniería de Software
tema: Scrum
tags: [ingsoft/scrum, ingsoft/scrum/eventos, origen/apuntes]
prerrequisitos: ["[[01 - Scrum|Scrum]]"]
---
# Sprint

El sprint es la **iteración de Scrum**: un período fijo y corto en el que el equipo desarrolla y produce un incremento del producto.

## Características
- **Período de tiempo fijo y corto**, en el que se lleva a cabo el desarrollo.
- Se crea un **incremento del producto**.

## Sprint Execution
*(En tus apuntes es la actividad 4, solo con el título.)*

> [!tip] Complemento — Sprint Execution (libro del curso, cap. 3.5 y 3.6)
> Es la ejecución de las tareas del [[08 - Sprint Backlog|Sprint Backlog]] **en el orden que el equipo decida**. Nadie le dice al equipo cómo hacer las tareas, y **no existen cosas "casi hechas"**: está hecho o no está hecho. El [[03 - Scrum Master|Scrum Master]] está disponible para guiar y resolver dudas del proceso.

> [!tip] Complemento — qué es un sprint (slides "SCRUM - una introducción rápida" y libro)
> - Es un **"evento de longitud fija"** de **2 a 4 semanas**. Tu imagen de [[01 - Scrum|Scrum]] dice 1 a 4 semanas; la Scrum Guide 2020 dice **un mes o menos**.
> - **Todas las iteraciones tienen el mismo largo.**
> - **Input:**
>   - el **objetivo del sprint**;
>   - los **ítems seleccionados del [[05 - Product Backlog|Product Backlog]]** (por ejemplo, funcionalidades a desarrollar);
>   - el **conjunto de tareas del sprint backlog**.
> - El sprint **termina con un incremento** del producto o con valor agregado al ya existente.
> - El sprint contiene a todos los demás eventos:
>
> ```mermaid
> flowchart LR
>   P[07 Sprint Planning] --> E[Ejecución + Daily Scrum cada día] --> R[10 Sprint Review] --> RE[11 Retrospective]
> ```
>
> Notas relacionadas: [[07 - Sprint Planning|Sprint Planning]], [[09 - Daily Scrum|Daily Scrum]], [[10 - Sprint Review|Sprint Review]], [[11 - Sprint Retrospective|Sprint Retrospective]].

> [!tip] Complemento — "Definition of Done"
> Para saber si algo está "hecho", el equipo acuerda una **Definition of Done (DoD)**: una lista de criterios que todo incremento debe cumplir, por ejemplo "código revisado, tests pasando, desplegado en staging". La slide de Sprint Planning dice que el incremento debe **cumplir la Definition of Done**.

## Preguntas de repaso

1. ¿Qué caracteriza a un sprint?
> [!question]- Respuesta
> Es un período de tiempo fijo y corto (típicamente de 2 a 4 semanas, siempre del mismo largo) en el que se desarrolla y se crea un incremento del producto potencialmente entregable.

2. ¿Cuáles son los inputs de un sprint?
> [!question]- Respuesta
> El objetivo del sprint, los ítems seleccionados del Product Backlog y el conjunto de tareas del Sprint Backlog.

3. ¿Qué significa que en Scrum "no existen cosas casi hechas"?
> [!question]- Respuesta
> Que un ítem cuenta como terminado solo si cumple completamente la Definition of Done. Lo que está a medias no se considera hecho ni suma al incremento.

4. ¿Por qué conviene que todos los sprints tengan la misma duración?
> [!question]- Respuesta
> Porque da un ritmo predecible y permite medir la velocidad del equipo y comparar sprints para planificar.
