# Ingeniería de Software (IIC2143) — mapa del curso

Vault de estudio del ramo. Cada nota cubre **un concepto**: no hace falta saber en qué clase se vio, basta con buscar el concepto. Dentro de cada carpeta, el número del archivo indica el orden de lectura.

## Cómo están hechas las notas
- **Frontmatter:** `tema`, `tags` (`origen/apuntes` = parte de mis apuntes; `origen/complemento` = nota nueva) y `prerrequisitos` (lo que conviene leer antes).
- **Cuerpo:** primero mis apuntes; los complementos (slides, libro del curso, conocimiento general) siempre van en callouts `[!tip] Complemento` o `[!example]`.
- **Errores detectados:** van en callouts `[!warning] Posible error` y quedan registrados en `_meta/DUDAS.md`.
- **Cierre:** cada nota termina con **Preguntas de repaso**, con la respuesta oculta.

## Temas
| Tema | Qué cubre |
|---|---|
| [[Ingeniería de Software/Fundamentos/_Índice\|Fundamentos]] | Qué es la IS, problemas del software, calidad |
| [[Ingeniería de Software/Procesos de desarrollo/_Índice\|Procesos de desarrollo]] | Cascada, iterativos (espiral, prototipos, RUP), incrementales, ágil, XP |
| [[Ingeniería de Software/Scrum y gestión ágil/_Índice\|Scrum y gestión ágil]] | Scrum, historias de usuario, planificación y estimación |
| [[Ingeniería de Software/Ruby/_Índice\|Ruby]] | Sintaxis, convenciones, métodos, bloques, colecciones, control, strings |
| [[Ingeniería de Software/Programación orientada a objetos/_Índice\|Programación orientada a objetos]] | Clases, visibilidad, herencia, super, polimorfismo, lookup, self vs super |
| [[Ingeniería de Software/Desarrollo web con Rails/_Índice\|Desarrollo web con Rails]] | HTTP, HTML/CSS, MVC, Active Record, rutas, vistas, API |
| [[Ingeniería de Software/Testing/_Índice\|Testing]] | Unit, integration, fixtures, asserts, cobertura |
| [[Ingeniería de Software/Diseño y UML/_Índice\|Diseño y UML]] | Diagramas de clases y de secuencia, acoplamiento, cohesión, abierto/cerrado |
| [[Ingeniería de Software/Patrones de Diseño/_Índice\|Patrones de Diseño]] | Comportamiento, estructurales, creacionales, comparaciones y ejercicios |
| [[Ingeniería de Software/Arquitectura de software/_Índice\|Arquitectura de software]] | Cliente-servidor, capas, CAP, SOA, microservicios, Docker/Kubernetes |
| [[Ingeniería de Software/Gestión del curso/_Índice\|Gestión del curso]] | Evaluación, checklist de la prueba práctica, proyecto, material |

## Ruta de estudio sugerida
1. **Fundamentos:** por qué existe la ingeniería de software.
2. **Procesos de desarrollo:** qué modelos existen; es la base para entender Scrum.
3. **Scrum y gestión ágil:** Scrum → historias de usuario → planificación y estimación.
4. **Ruby → Programación orientada a objetos:** el lenguaje y luego POO (lookup y self vs super salen en la prueba).
5. **Desarrollo web con Rails → Testing:** fundamentos web, Rails y cómo probarlo.
6. **Diseño y UML → Patrones de Diseño:** UML, principios de diseño, patrones (comportamiento → estructurales → creacionales) y ejercicios de prueba.
7. **Arquitectura de software:** la mirada de alto nivel.

**Para la prueba práctica:** sigue el [[02 - Checklist de la prueba práctica|checklist]] y repasa los [[Ingeniería de Software/Patrones de Diseño/Ejercicios de prueba/_Índice|ejercicios de prueba]].
