---
ramo: Ingeniería de Software
tema: Gestión del curso
tags: [ingsoft/curso, ingsoft/requisitos, origen/apuntes]
prerrequisitos: ["[[01 - Historias de usuario|Historias de usuario]]", "[[01 - Scrum|Scrum]]"]
---
# Proyecto del curso

El proyecto semestral era una aplicación web en Ruby on Rails, desarrollada en equipo con Scrum (sprints con entregas parciales). Aquí van mis historias de usuario y su estructura.

## Historias de usuario (mías)
- Obtener/Modificar Info Personal
- Mandar mensajes en un chat
- Dejar Reseñas
- Ver sus solicitudes

## Estructura del proyecto
- **4 sprints** → entregas parciales (40% del proyecto).
- **Entrega final** → 20%.
- **Presentación final** → 20%.
- En mi calendario: Sprint 0 (5 de abril), Sprint 1 (26 de abril), Sprint 2 (26 de mayo).

*(Las páginas "Proyecto - Software" e "Interrogaciones - Examenes - Software" de mi Notion estaban vacías.)*

> [!tip] Complemento — mis historias escritas completas
> Así quedarían con la [[02 - Estructura de una historia de usuario|estructura del curso]] (los roles son una suposición: ajústalos a tu app):
>
> | Título | Descripción | Criterio de aceptación (resumen) |
> |---|---|---|
> | Modificar información personal | Yo, como usuario registrado, necesito ver y modificar mi información personal para mantener mis datos actualizados. | Dado un usuario con sesión iniciada, cuando edita su teléfono y guarda, entonces el perfil muestra el nuevo teléfono. |
> | Enviar mensajes en un chat | Yo, como cliente, necesito enviar mensajes a un proveedor para coordinar el servicio. | Dado un chat abierto, cuando escribo y envío un mensaje, entonces aparece en la conversación de ambos. |
> | Dejar una reseña | Yo, como cliente que recibió un servicio, necesito dejar una reseña para orientar a otros clientes. | Dado un servicio finalizado, cuando ingreso una nota y un comentario, entonces la reseña aparece en el perfil del proveedor. |
> | Ver mis solicitudes | Yo, como usuario, necesito ver mis solicitudes y su estado para hacer seguimiento. | Dado que tengo solicitudes, cuando entro a "Mis solicitudes", entonces veo la lista con su estado. |
>
> Para estimarlas y planificarlas: [[01 - Story points|Story points]] y [[04 - Planificación de una iteración|Planificación de una iteración]].

## Preguntas de repaso

1. Reescribe "Dejar Reseñas" con el formato "Yo, como… necesito… para…".
> [!question]- Respuesta
> Por ejemplo: "Yo, como cliente que recibió un servicio, necesito dejar una reseña con nota y comentario para orientar a otros clientes".

2. ¿Cuánto pesaban las entregas de sprint en la nota de proyecto?
> [!question]- Respuesta
> 40% (4 sprints con entregas parciales).

3. ¿Cómo dividirías "Mandar mensajes en un chat" si fuera muy grande para un sprint?
> [!question]- Respuesta
> Por flujo o por criterio: "enviar un mensaje de texto", "ver el historial de la conversación" y "recibir una notificación de mensaje nuevo".
