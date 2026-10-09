---
ramo: Ingeniería de Software
tema: Fundamentos
tags: [ingsoft/fundamentos, origen/complemento]
prerrequisitos: ["[[01 - Qué es la ingeniería de software|Qué es la ingeniería de software]]"]
---
# Problemas del desarrollo de software (CHAOS report)

> [!tip] Complemento — nota nueva (fuente: slides "Ingeniería de Software: Introducción")
> **Qué es:** evidencia de que desarrollar software es difícil. Muchos proyectos fracasan o no cumplen las expectativas.
>
> ## ¿En verdad es tan complejo? — CHAOS report 2015
> Muestra de **25.000 proyectos** entre 2011 y 2015:
>
> ![Slide - CHAOS report 2015](adjuntos/Slide%20-%20CHAOS%20report%202015.png)
>
> | Indicador | Sí | No |
> |---|---|---|
> | Proyectos considerados **valiosos** | 59% | 41% |
> | Proyectos **on goal** (cumplieron su objetivo) | 38% | 62% |
> | Proyectos considerados **satisfactorios** | 56% | 44% |
>
> **Clasificación de proyectos:**
> - **Succeeded:** completado con un presupuesto razonable según lo estimado y con un resultado satisfactorio (buen número de funcionalidades presentadas).
> - **Challenged:** completado, pero no a tiempo o con más presupuesto del esperado.
> - **Failed:** no completado.
>
> **¿Qué tan grandes o complejos eran los proyectos?** La tasa de éxito baja mucho a medida que crecen el tamaño y la complejidad:
>
> ![Slide - éxito según tamaño y complejidad](adjuntos/Slide%20-%20éxito%20según%20tamaño%20y%20complejidad.png)
>
> ## Otros problemas relacionados
> - software que a menudo **no hace lo que los usuarios quieren**;
> - software muy caro;
> - software que no es suficientemente rápido;
> - software difícil de usar;
> - software que no puede ser portado;
> - software muy caro de mantener;
> - software poco confiable;
> - proyectos de software que se atrasan.
>
> ## ¿En serio no es fácil responder a las necesidades de los usuarios?
> ![Slide - uso de las funcionalidades solicitadas](adjuntos/Slide%20-%20uso%20de%20las%20funcionalidades%20solicitadas.png)
>
> Porcentaje de funcionalidades solicitadas:
> - entregadas pero **no utilizadas**: 47%;
> - pagadas pero no entregadas: 29%;
> - abandonadas o rehechas: 19%;
> - utilizadas, pero después de varios cambios: 3%;
> - utilizadas tal como se entregaron: 2%.
>
> ## Otro problema importante es la comunicación
> ![Slide - problema de comunicación](adjuntos/Slide%20-%20problema%20de%20comunicación.png)
>
> La clásica caricatura del columpio en un árbol: lo que pidió el cliente, lo que entendió el líder de proyecto, lo que diseñó el analista, lo que programó el programador, lo que se documentó… y lo que el cliente realmente necesitaba (un simple neumático colgado). Por eso existen las [[01 - Historias de usuario|historias de usuario]] y los procesos [[09 - Metodologías ágiles y manifiesto ágil|ágiles]], con feedback frecuente.

## Preguntas de repaso

1. ¿Qué diferencia hay entre un proyecto "challenged" y uno "failed" según el CHAOS report?
> [!question]- Respuesta
> El challenged se completó, pero tarde o con más presupuesto del esperado. El failed no se completó.

2. Según las slides, ¿qué porcentaje de las funcionalidades solicitadas se entrega pero no se usa?
> [!question]- Respuesta
> Cerca del 47%, el grupo más grande. Muestra lo difícil que es entender qué necesitan realmente los usuarios.

3. ¿Qué relación hay entre el tamaño y la complejidad de un proyecto y su tasa de éxito?
> [!question]- Respuesta
> Mientras más grande y complejo es el proyecto, menor es la probabilidad de éxito y mayor la de fracaso.
