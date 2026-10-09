---
ramo: Ingeniería de Software
tema: Fundamentos
tags: [ingsoft/fundamentos, origen/complemento]
prerrequisitos: ["[[01 - Qué es la ingeniería de software|Qué es la ingeniería de software]]"]
---
# Calidad de software

> [!tip] Complemento — nota nueva (fuente: slides de presentación del curso y "Procesos de Desarrollo de Software")
> **Qué es:** el software de calidad no solo **funciona**: también es mantenible, extensible, legible y responde a lo que el usuario necesita, dentro de plazo y presupuesto.
>
> *"No es suficiente escribir un código que funcione. Lo más importante es escribir código de calidad: mantenible, extensible, legible…"* (slides del curso)
>
> **Lo aprendido hasta ahora** (aspectos funcionales y de programación): funciones, variables, estructuras de datos, objetos, polimorfismo y herencia.
>
> **Otros aspectos de la calidad:**
> - extensibilidad, mantenibilidad, escalabilidad y rendimiento;
> - además, en un proyecto real: el **cliente**, la **usabilidad**, los **requisitos**, el **cronograma**, el **diseño**, la **documentación**, el **presupuesto** y el **equipo de trabajo**.
>
> **Expectativas actuales** (slides, "2023"):
> - **Portable:** se ejecuta en distintos sistemas operativos y hardware (celulares).
> - **Performance:** soporta múltiples usuarios y transacciones en tiempo real.
> - **Confiable:** los servicios nunca dejan de funcionar y los datos no se pierden.
> - **Extensible, modificable, escalable** en el tiempo.
> - **Tiempo y presupuesto.**
>
> **Calidad vs. costo:** *"…in software development this is absolute nonsense, because poor quality is the major contributor to the soaring costs of software development."* (Dijkstra, EWD690). Hablar de un *trade-off* entre costo y calidad no tiene sentido en software: **la mala calidad es lo que más encarece el desarrollo**. Por eso [[06 - Ajustes de la planificación|la calidad no se negocia]].
>
> **Dónde se trabaja la calidad en el curso:** [[01 - Buen diseño de software|buen diseño]] (acoplamiento, cohesión), [[01 - Qué es el testing de software|testing]] y [[01 - Qué es un patrón de diseño|patrones de diseño]].

## Preguntas de repaso

1. ¿Por qué "que funcione" no basta para que un software sea de calidad?
> [!question]- Respuesta
> Porque además debe ser mantenible, extensible, legible, escalable y confiable, y responder a los usuarios dentro de plazo y presupuesto. Un código que funciona pero es inmantenible se vuelve caro de cambiar.

2. ¿Qué dice Dijkstra sobre el *trade-off* entre costo y calidad?
> [!question]- Respuesta
> Que en software no tiene sentido: la mala calidad es la principal causa del aumento de los costos.

3. Nombra tres expectativas actuales sobre el software.
> [!question]- Respuesta
> Portabilidad, rendimiento (muchos usuarios en tiempo real), confiabilidad (24/7, sin pérdida de datos) y extensibilidad, además de cumplir tiempo y presupuesto.
