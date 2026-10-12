---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, ingsoft/scrum, origen/complemento]
prerrequisitos: ["[[03 - Velocidad de desarrollo|Velocidad de desarrollo]]"]
---
# Planificación de un release

> [!tip] Complemento — nota nueva (fuente: slides "SCRUM - Planificación y Estimación" y libro del curso, cap. 5.4)
> **Qué es:** un **release** es la entrega de un conjunto de historias de usuario que normalmente se desarrolla a lo largo de **varios sprints**. Planificarlo da la **visión a largo plazo**: cuántas iteraciones se necesitan y qué funcionalidades formarán cada entrega. Por ejemplo, 4 sprints de 2 semanas = un release en 8 semanas.
>
> **Pasos (slides):**
> 1. **Priorizar las historias de usuario**, considerando:
>    - el riesgo de que una historia no se complete como se espera;
>    - el impacto en otras historias si se pospone;
>    - el deseo de la historia por una gran mayoría de usuarios y clientes;
>    - el deseo de la historia por una pequeña pero importante cantidad de clientes o usuarios;
>    - la cohesión de la historia con otras historias.
> 2. **Decidir el período de la iteración y del release** (¿dos semanas?, ¿tres semanas?).
> 3. **Agrupar las historias en sprints y los sprints en releases.**
>
> ![Slide - release plan en el tiempo](../adjuntos/Slide%20-%20release%20plan%20en%20el%20tiempo.png)

> [!example] Ejemplo extra — release plan (slides). Velocidad: 3 puntos/sprint; sprints de 2 semanas.
> | ID | Historia | Estimación | Prioridad |
> |---|---|---|---|
> | 6 | As a general user I want to register a new account. | 3 | 1 |
> | 2 | As a member I want to sign-in my account. | 2 | 2 |
> | 5 | As a member I want to sign-out my account. | 1 | 3 |
> | 10 | As an administrator I want to disallow suspicious registration attempts. | 2 | 4 |
> | 1 | As a member I want to add new items into shopping cart. | 5 | 5 |
> | 3 | As a member I want to checkout shopping cart. | 7 | 6 |
> | 4 | As a member I want to track the delivery. | 2 | 7 |
> | 9 | As a member I want to record delivery addresses. | 1 | 8 |
> | 7 | As a member I want to cancel order. | 1 | 9 |
> | 8 | As an administrator I want to see the list of accounts logged in. | 2 | 10 |
> | | **Total** | **26** | |
>
> Objetivos de cada release y cálculo:
> - **Release 1** (registrarse, iniciar y cerrar sesión): historias 6, 2, 5, 10 = 8 puntos → 8 / 3 = 2,67 → **3 sprints**.
> - **Release 2** (comprar con éxito): historias 1, 3, 4, 9 = 15 puntos → 15 / 3 = **5 sprints**.
> - **Release 3** (resto): historias 7, 8 = 3 puntos → 3 / 3 = **1 sprint**.
>
> Al dividir por la velocidad se **redondea hacia arriba**: no existen "dos tercios de sprint".

## Preguntas de repaso

1. ¿Cuáles son los 3 pasos para planificar un release?
> [!question]- Respuesta
> (1) Priorizar las historias de usuario, (2) decidir la duración de las iteraciones y del release y (3) agrupar las historias en sprints y los sprints en releases.

2. Un release suma 20 puntos y la velocidad es 6. ¿Cuántos sprints necesita?
> [!question]- Respuesta
> 20 / 6 = 3,33 → 4 sprints (se redondea hacia arriba).

3. Nombra dos criterios para priorizar historias al planificar un release.
> [!question]- Respuesta
> El riesgo de que no se complete, su impacto en otras historias si se pospone, cuántos usuarios la desean (o si la piden pocos pero importantes) y su cohesión con otras historias.
