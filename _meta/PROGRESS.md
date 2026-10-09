# Progreso de la migración — Ingeniería de Software (IIC2143)

Rama: `migrar/software-v2`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py`.

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`verificar.py`, mapeo, índices) | `_meta/` | ✅ hecho | – | – |
| 1 | Procesos de desarrollo | `Procesos de desarrollo/` | ✅ hecho | 12 + índice | 9 + 4 |
| 2 | Scrum | `Scrum y gestión ágil/Scrum/` | ✅ hecho | 11 + índice | 1 + 8 |
| 3 | Historias de usuario | `Scrum y gestión ágil/Historias de usuario/` | ✅ hecho | 7 + índice | 0 |
| 4 | Planificación y estimación | `Scrum y gestión ágil/Planificación y estimación/` | ✅ hecho | 10 + índice | 0 + 6 |
| 5 | Ruby | `Ruby/` | ✅ hecho | 8 + índice | 0 |
| 6 | Programación orientada a objetos | `Programación orientada a objetos/` | ✅ hecho | 13 + índice | 0 |
| 7 | Fundamentos web | `Desarrollo web con Rails/Fundamentos web/` | ⏳ pendiente | | |
| 8 | Rails | `Desarrollo web con Rails/Rails/` | ⏳ pendiente | | |
| 9 | Testing | `Testing/` | ⏳ pendiente | | |
| 10 | UML | `Diseño y UML/UML/` | ⏳ pendiente | | |
| 11 | Principios de diseño | `Diseño y UML/Principios de diseño/` | ⏳ pendiente | | |
| 12 | Patrones de comportamiento | `Patrones de Diseño/Comportamiento/` | ⏳ pendiente | | |
| 13 | Patrones estructurales | `Patrones de Diseño/Estructurales/` | ⏳ pendiente | | |
| 14 | Patrones creacionales | `Patrones de Diseño/Creacionales/` | ⏳ pendiente | | |
| 15 | Arquitectura de software | `Arquitectura de software/` | ⏳ pendiente | | |
| 16 | Fundamentos + Gestión del curso + mapa final | `Fundamentos/`, `Gestión del curso/` | ⏳ pendiente | | |

## Convenciones
- Cada nota lleva un prefijo `NN - ` con su orden de estudio dentro de la carpeta (`01 - …`, `02 - …`). El `_Índice.md` de la carpeta lista las notas en ese mismo orden.
- Los wikilinks usan el nombre real y el título como alias: `[[02 - Modelo en cascada|Modelo en cascada]]`. Dentro de tablas el alias va escapado: `\|`.

## Registro
- **2026-10-09 — Procesos de desarrollo.**
  - Fuente: "Resumen Software Pt 1", §4 Procesos (81 bloques, 9 imágenes); complementos de las slides "Procesos de Desarrollo de Software" y del libro del curso, cap. 2.
  - Verificación: 0 errores, 0 advertencias. Cobertura: 66 bloques exactos + 15 reformulados, 0 sin cubrir.
- **2026-10-09 — Orden de estudio.** Se renumeraron las 12 notas de Procesos con prefijo `NN - ` y se actualizaron todos los wikilinks.
- **2026-10-09 — Scrum.**
  - Fuente: "Resumen Software Pt 1", §5 SCRUM (46 bloques, 1 imagen); complementos de las slides "SCRUM - una introducción rápida", el libro del curso (cap. 3) y la Scrum Guide 2020.
  - Las imágenes de `Scrum y gestión ágil/` se comparten en `Scrum y gestión ágil/adjuntos/` (`"adjuntos"` en mapeo.json).
  - Verificación: 0 errores, 0 advertencias. Cobertura: 37 exactos + 9 reformulados, 0 sin cubrir.
- **2026-10-09 — Historias de usuario.**
  - Fuente: "Resumen Software Pt 1", §7 Relatos de usuario (13 bloques, sin imágenes); complementos de las slides "Historias de Usuario" y del libro del curso, cap. 4.
  - Las "Historias de usuario (mías)" de la página del ramo quedan para el tema Gestión del curso, como estaba planificado.
  - Verificación: 0 errores, 0 advertencias. Cobertura: 9 exactos + 4 reformulados.
  - verificar.py: un encabezado original también cuenta como cubierto si todas sus palabras (con tolerancia a erratas) están en el título o en un encabezado de alguna nota.
- **2026-10-09 — Planificación y estimación.**
  - Fuente: "Resumen Software Pt 1", §8 Estimaciones, que solo tiene el título: las 10 notas son complemento (slides 8 y 9 y libro, cap. 5 y 7).
  - Se transcribieron como tablas los ejemplos de las slides (velocidad, release plan, tareas, AccSellerator → Triad).
  - Verificación: 0 errores, 0 advertencias.
- **2026-10-09 — Ruby.**
  - Fuentes: "Resumen Software Pt 1", §1 RUBY, y la parte RUBY de "C1 Software" (idéntica); complementos de las slides "Ruby" y del libro, cap. 10.
  - "require_relative" (de Resumen Prueba Práctica §14) se dejó como nota en Ruby; se verificará con el tema Principios de diseño.
  - verificar.py: secciones delimitadas por texto (`por_texto`) para páginas sin encabezados; desempate de ventanas por similitud.
  - Verificación: 0 errores, 0 advertencias.
- **2026-10-09 — Programación orientada a objetos.**
  - Fuente: "Resumen Prueba Práctica", §13 Polimorfismo y Lookup (67 bloques: todo el código copiado y, donde no corre, con versión corregida al lado); complementos de las slides "Object Oriented Programming" y "Ruby".
  - Verificación: 0 errores, 0 advertencias (58 exactos + 9 reformulados).
- **Nota técnica:** `.venv` no existe en el repo, así que el verificador usa solo la biblioteca estándar de Python.
