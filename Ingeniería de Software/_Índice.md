# Ingeniería de Software (IIC2143) — mapa del curso

Vault de estudio del ramo. Cada nota cubre **un concepto**: no hace falta saber en qué clase se vio, basta con buscar el concepto.

## Cómo están hechas las notas
- **Frontmatter:** `tema`, `tags` y `prerrequisitos` (lo que conviene leer antes).
- **Cuerpo:** primero mis apuntes; los complementos (slides, libro del curso, conocimiento general) siempre van en callouts `[!tip] Complemento` o `[!example]`.
- **Errores detectados:** van en callouts `[!warning] Posible error` y quedan registrados en `_meta/DUDAS.md`.
- **Cierre:** cada nota termina con **Preguntas de repaso**, con la respuesta oculta.

## Temas
| Tema | Qué cubre | Estado |
|---|---|---|
| [[Ingeniería de Software/Procesos de desarrollo/_Índice\|Procesos de desarrollo]] | Cascada, iterativos (espiral, prototipos, RUP), incrementales, ágil, XP | ✅ |
| [[Ingeniería de Software/Scrum y gestión ágil/_Índice\|Scrum y gestión ágil]] | Scrum, historias de usuario, planificación y estimación | ✅ |
| [[Ingeniería de Software/Ruby/_Índice\|Ruby]] | Sintaxis, convenciones, métodos, bloques, colecciones, control, strings | ✅ |
| [[Ingeniería de Software/Programación orientada a objetos/_Índice\|Programación orientada a objetos]] | Clases, visibilidad, herencia, super, polimorfismo, lookup, self vs super | ✅ |
| [[Ingeniería de Software/Desarrollo web con Rails/_Índice\|Desarrollo web con Rails]] | HTTP, HTML/CSS, MVC, Active Record, rutas, vistas, API | ✅ |
| [[Ingeniería de Software/Testing/_Índice\|Testing]] | Unit, integration, fixtures, asserts, cobertura | ✅ |
| [[Ingeniería de Software/Diseño y UML/_Índice\|Diseño y UML]] | Diagramas de clases y de secuencia, acoplamiento, cohesión, abierto/cerrado | ✅ |
| [[Ingeniería de Software/Patrones de Diseño/_Índice\|Patrones de Diseño]] | Comportamiento, estructurales, creacionales, comparaciones y ejercicios de prueba | ✅ |
| Arquitectura de software | Cliente-servidor, capas, microservicios | ⏳ pendiente |
| Fundamentos y gestión del curso | Qué es la IS, evaluación, checklist de la prueba práctica | ⏳ pendiente |

## Ruta de estudio sugerida
1. **Procesos de desarrollo:** por qué hace falta un proceso y qué modelos existen. Es la base para entender Scrum.
2. **Scrum y gestión ágil:** Scrum aplica las ideas ágiles → historias de usuario → planificación y estimación.
3. **Ruby → Programación orientada a objetos:** el lenguaje y luego POO (lookup y self vs super salen en la prueba).
4. **Desarrollo web con Rails → Testing.**
5. **Diseño y UML → Patrones de Diseño:** primero comportamiento (Strategy, Template Method, Observer), luego estructurales y creacionales; cierra con los ejercicios de prueba.
6. Arquitectura de software *(pendiente)*.

Esta ruta se completa a medida que se migran los temas (ver `_meta/PROGRESS.md`).
