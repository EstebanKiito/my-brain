---
ramo: Ingeniería de Software
tema: Historias de usuario
tags: [ingsoft/requisitos, ingsoft/agil, origen/complemento]
prerrequisitos: ["[[05 - Product Backlog|Product Backlog]]"]
---
# Historias de usuario (relatos de usuario)

> [!tip] Complemento — nota nueva (fuente: slides "Historias de Usuario" y libro del curso, cap. 4)
> **Qué es:** una historia de usuario es una **descripción breve, escrita desde la perspectiva del usuario**, de una funcionalidad que le aporta valor. En Scrum son los ítems típicos del [[05 - Product Backlog|Product Backlog]].
>
> **Definición según las slides:**
> - Técnica de captura de requisitos **centrada en el usuario**.
> - Describe los requisitos a partir de los **objetivos del usuario** y de cómo interactúa con el sistema para lograrlos.
> - Es una descripción **concisa y escrita** de un **requisito funcional** que aporta valor al usuario.
> - Pone el énfasis en cumplir los objetivos del usuario y en el valor entregado.
> - Está ligada a los procesos ágiles y al **tratamiento iterativo** de los requisitos.
>
> **Quiénes construyen el Product Backlog inicial:** Product Owner, stakeholders y equipo de desarrollo.

> [!tip] Complemento — por qué historias y no un documento de requisitos (libro, cap. 4.1–4.2)
> - **Requisitos funcionales:** *qué* capacidades tiene el sistema (por ejemplo, consultar el inventario). **No funcionales:** restricciones como rendimiento o usabilidad (por ejemplo, responder en menos de 1 segundo).
> - El documento de requisitos tradicional (un "contrato") tenía dos problemas:
>   1. no se pueden **congelar los requisitos** al inicio del proyecto;
>   2. el lenguaje escrito es **ambiguo**.
>   
>   Lo ágil acepta cambiar requisitos en cada iteración y asume que lo escrito es incompleto.
> - **Ejemplo de ambigüedad:** alguien encarga una torta con la indicación *"escribe 'Hasta pronto Alicia' en morado y coloca estrellas alrededor"*, y el pastelero escribe literalmente esa frase, comillas incluidas.
> - **Un documento compartido no garantiza un entendimiento compartido.** Por eso la historia es una **"promesa de conversación"** con el usuario.
> - *"Las historias de usuario representan los requerimientos del usuario y no así la documentación de los mismos"* (Rachel Davies, 2001).
> - Al principio se escribían en **tarjetas de 3x5 pulgadas**: la tarjeta obliga a ser breve y a conversar el resto.
> - Las historias **no son un nuevo formato de requisitos escritos**, sino un mecanismo para lograr un **entendimiento compartido**. Lo que se busca maximizar es el *outcome* y el impacto, no la cantidad de código.
> - Otro enfoque centrado en el usuario son los **casos de uso**: escenarios más detallados de la interacción usuario-sistema.

> [!tip] Complemento — mapa del tema
> 1. [[02 - Estructura de una historia de usuario|Estructura]]: título, descripción y condiciones de aceptación.
> 2. [[03 - Criterios de aceptación (Dado-Cuando-Entonces)|Criterios de aceptación]]: escenarios Dado / Cuando / Entonces.
> 3. [[04 - Criterio INVEST|INVEST]]: cómo saber si una historia es buena.
> 4. [[05 - Errores comunes en historias de usuario|Errores comunes]].
> 5. [[06 - Épicas, temas e historias|Épicas, temas e historias]]: niveles de granularidad.
> 6. [[07 - Cómo dividir historias de usuario|Cómo dividir historias]].

## Preguntas de repaso

1. ¿Qué es una historia de usuario?
> [!question]- Respuesta
> Una descripción breve y escrita, desde la perspectiva del usuario, de un requisito funcional que le aporta valor. Se centra en el objetivo del usuario y sirve como base para conversar los detalles.

2. ¿Qué significa que una historia sea una "promesa de conversación"?
> [!question]- Respuesta
> Que lo escrito no pretende especificar todo: es un recordatorio de que el equipo y el usuario conversarán los detalles para llegar a un entendimiento compartido.

3. Verdadero o falso: las historias de usuario son un nuevo formato de requerimientos escritos.
> [!question]- Respuesta
> Falso. Son un mecanismo para adquirir un entendimiento compartido, no un formato de documentación.

4. ¿Qué dos problemas del documento de requisitos tradicional resuelve el enfoque ágil?
> [!question]- Respuesta
> Que no se pueden congelar los requisitos al inicio (en ágil se agregan, quitan o modifican en cada iteración) y que lo escrito es ambiguo (se asume incompleto y se complementa conversando).
