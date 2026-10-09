---
ramo: Ingeniería de Software
tema: Scrum
tags: [ingsoft/scrum, ingsoft/scrum/artefactos, origen/complemento]
prerrequisitos: ["[[01 - Scrum|Scrum]]", "[[02 - Product Owner|Product Owner]]"]
---
# Product Backlog

> [!tip] Complemento — nota nueva (fuente: slides "SCRUM - una introducción rápida", "Historias de Usuario" y libro del curso, cap. 3.5)
> **Qué es:** el Product Backlog es la **lista priorizada de todo lo que hay que hacer** en el producto. La mantiene el [[02 - Product Owner|Product Owner]] y es la fuente de la que se alimenta cada sprint.
>
> **Qué contiene** (slides "Historias de Usuario"):
> - **Producto nuevo:** nuevas funcionalidades y requerimientos no funcionales.
> - **Producto existente:** mejoras, corrección de defectos y cambios de infraestructura.
>
> **Características:**
> - Está **priorizado**: arriba lo más valioso y lo mejor detallado. El PO lo revisa y lo reprioriza constantemente.
> - Es **vivo**: el PO puede agregar o ajustar elementos en cualquier momento según el feedback ("Add/Take from Product Backlog").
> - Cada ítem tiene una **estimación** de esfuerzo, por ejemplo en story points.
> - En el backlog inicial participan el **Product Owner, los stakeholders y el equipo de desarrollo**.
> - Sus ítems suelen escribirse como **historias de usuario**.

> [!example] Ejemplo extra — Product Backlog de un sistema de reservas de hotel (slides)
> | Backlog item | Estimación |
> |---|---|
> | Allow a guest to make a reservation | 3 |
> | As a guest, I want to cancel a reservation. | 5 |
> | As a guest, I want to change the dates of a reservation. | 3 |
> | As a hotel employee, I can run RevPAR reports (revenue-per-available-room) | 8 |
> | Improve exception handling | 8 |
> | … | 30 |
> | … | 50 |
>
> Los ítems de abajo tienen estimaciones grandes (30, 50) porque todavía no se refinan: son demasiado grandes para un sprint y se dividirán más adelante.

> [!tip] Complemento — refinamiento del backlog (slides)
> ![Slide - refinamiento del backlog](../adjuntos/Slide%20-%20refinamiento%20del%20backlog.png)
>
> La slide muestra con humor lo que hay en un backlog real:
> - cosas para el siguiente sprint;
> - cosas para el siguiente semestre;
> - cosas que creemos que llegarán algún día;
> - cosas que están para hacernos parecer ocupados;
> - cosas que activamente están ahí para engañar al cliente;
> - cosas que los investigadores no saben por qué siguen ahí.
>
> El **refinamiento** consiste en revisar el backlog seguido: detallar y dividir los ítems de arriba, reestimar, repriorizar y **eliminar lo que ya no aporta**.

## Preguntas de repaso

1. ¿Qué es el Product Backlog y quién es responsable de él?
> [!question]- Respuesta
> Es la lista priorizada de todo lo que necesita el producto (funcionalidades, mejoras, correcciones, cambios de infraestructura). El responsable es el Product Owner, que la mantiene y prioriza.

2. ¿Por qué los ítems de arriba están más detallados que los de abajo?
> [!question]- Respuesta
> Porque son los próximos en desarrollarse: deben estar refinados y ser pequeños para caber en un sprint. Los de abajo pueden ser grandes y vagos hasta que se acerque su turno.

3. Diferencia entre Product Backlog y Sprint Backlog.
> [!question]- Respuesta
> El Product Backlog es la lista de todo el producto, priorizada por el PO y en cambio constante. El Sprint Backlog es el subconjunto que el equipo eligió para un sprint, dividido en tareas, junto con el plan para completarlas.
