---
ramo: Ingeniería de Software
tema: Planificación y estimación
tags: [ingsoft/estimacion, ingsoft/scrum, origen/complemento]
prerrequisitos: ["[[03 - Velocidad de desarrollo|Velocidad de desarrollo]]", "[[07 - Sprint Planning|Sprint Planning]]"]
---
# Planificación de una iteración

> [!tip] Complemento — nota nueva (fuente: slides "SCRUM - Planificación y Estimación" y libro del curso, cap. 5.3)
> **Qué es:** el detalle táctico del [[07 - Sprint Planning|Sprint Planning]]. Las historias elegidas según la [[03 - Velocidad de desarrollo|velocidad]] se desglosan en **tareas** estimadas en **horas**.
>
> **Pasos (slides):**
> 1. Discutir las historias a considerar.
> 2. **Desagregar las historias en tareas.**
> 3. Un desarrollador **acepta la responsabilidad** de una tarea.
> 4. Se termina cuando todas las historias fueron discutidas y todas las tareas aceptadas.
>
> **Ejemplo de tablero (slides)**
> | Tarea | Quién | Estimación (h) |
> |---|---|---|
> | Code basic search screen | Susan | 6 |
> | Code advanced search screen | Susan | 8 |
> | Code results screen | Jay | 6 |
> | Write and tune SQL to query the database for basic searches | Susan | 4 |
> | Write and tune SQL to query the database for advanced searches | Susan | 8 |
> | Document new functionality in help system and user's guide | Shannon | 2 |

> [!example] Ejemplo extra — desglose de una historia (libro, cap. 5.3)
> Historia: *"Crear una página de inicio de sesión para los usuarios"* (Rails).
> | Tarea | Horas |
> |---|---|
> | Diseñar la interfaz de la página de inicio de sesión | 4 |
> | Configurar el controlador de sesiones en Ruby on Rails | 2 |
> | Crear una vista para el formulario de inicio de sesión | 3 |
> | Implementar la lógica de autenticación en el controlador | 6 |
> | Establecer las rutas necesarias | 1 |
> | Agregar validaciones de entrada y manejo de errores | 3 |
> | Crear pruebas unitarias | 5 |
> | Integrar estilos CSS | 2 |
> | Configurar sesiones de usuario y almacenamiento seguro de contraseñas | 4 |
> | Pruebas de integración del flujo de inicio de sesión | 4 |
> | **Total** | **34** |
>
> Las **historias** se estiman en puntos (relativos) y las **tareas** en horas (concretas, porque ya son pequeñas).

## Preguntas de repaso

1. ¿En qué unidades se estiman las historias y en cuáles las tareas?
> [!question]- Respuesta
> Las historias en story points (unidad relativa); las tareas en horas o días, porque son pequeñas y concretas.

2. ¿Quién decide qué tarea toma cada desarrollador?
> [!question]- Respuesta
> El propio desarrollador acepta la responsabilidad de la tarea; el trabajo no se asigna desde afuera.

3. ¿Cuándo termina la planificación de la iteración?
> [!question]- Respuesta
> Cuando todas las historias consideradas fueron discutidas y todas sus tareas fueron aceptadas por algún miembro del equipo.
