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
| 7 | Fundamentos web | `Desarrollo web con Rails/Fundamentos web/` | ✅ hecho | 4 + índice | 0 |
| 8 | Rails | `Desarrollo web con Rails/Rails/` | ✅ hecho | 15 + índice | 4 |
| 9 | Testing | `Testing/` | ✅ hecho | 9 + índice | 6 |
| 10 | UML | `Diseño y UML/UML/` | ✅ hecho | 7 + índice | 11 |
| 11 | Principios de diseño | `Diseño y UML/Principios de diseño/` | ✅ hecho | 9 + índice | 6 |
| 12 | Patrones de comportamiento | `Patrones de Diseño/Comportamiento/` | ✅ hecho | 6 + 1 general + 1 comparación + 2 ejercicios | 14 |
| 13 | Patrones estructurales | `Patrones de Diseño/Estructurales/` | ✅ hecho | 6 + 1 comparación + 2 ejercicios | 22 |
| 14 | Patrones creacionales | `Patrones de Diseño/Creacionales/` | ✅ hecho | 7 + 1 comparación | 6 |
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
- **2026-10-09 — Fundamentos web.**
  - Fuente: "Resumen Prueba Práctica", §9 HTML + CSS (39 bloques); HTTP es complemento (slides "RoR - First API").
  - Las primeras líneas "html", "css" y "htmlCopiar código" de los bloques de código eran restos de copiar desde ChatGPT: se omitieron y verificar.py las ignora (`RE_ETIQUETA_LENGUAJE`).
  - Verificación: 0 errores, 0 advertencias.
- **2026-10-09 — Rails.**
  - Fuentes: Pt. 1 §2.3 y C1 (Rails/CRUD), Prueba Práctica §10 MVC + Routing (4 imágenes) y la página del ramo (instalación en Mac M1); complementos de las slides First API, Active Record y Rails MVC, y del libro (cap. 11–12).
  - "Vistas ERB" pasaba de 150 líneas: se separó "Parciales en ERB" y se renumeraron las siguientes.
  - Verificación: 0 errores, 0 advertencias (83 bloques: 72 exactos + 11 reformulados).
- **2026-10-09 — Testing.**
  - Fuente: "Resumen Prueba Práctica", §12 Testing (35 bloques, 6 imágenes transcritas); complementos de las slides "Testing".
  - Verificación: 0 errores, 0 advertencias (el verificador detectó y se corrigió una ruta `../adjuntos` mal puesta).
- **2026-10-09 — UML.**
  - Fuente: "Resumen Prueba Práctica", §11 Diseño UML (11 imágenes, transcritas y con versión Mermaid); complementos de las slides "UML" y del libro, cap. 8 (CRC, modelo de dominio, visibilidad `~`, interfaces).
  - Verificación: 0 errores, 0 advertencias.
- **2026-10-09 — Principios de diseño.**
  - Fuente: "Resumen Prueba Práctica", §14 Diseño, acoplamiento y cohesión (42 bloques, 6 imágenes de código transcritas). El bloque de `require_relative` de esta sección está en la nota Ruby/08.
  - Complementos de las slides "Diseño Orientado al Objeto" y del libro, cap. 8.5–8.6 (tipos de acoplamiento y cohesión, analogía del tren).
  - Verificación: 0 errores, 0 advertencias.
- **2026-10-09 — Patrones de comportamiento.**
  - Fuente: "Resumen Prueba Práctica", §15 (76 bloques, 14 imágenes). Cada patrón con código largo se dividió en "Patrón X" (concepto) y "X - implementación en Ruby", para no pasar de 150 líneas.
  - Se crearon "Qué es un patrón de diseño", "Strategy vs Template Method" y los ejercicios de prueba de Strategy (pagos) y Observer (empleados).
  - Verificación: 0 errores, 0 advertencias.
- **2026-10-09 — Patrones estructurales.**
  - Fuente: "Resumen Prueba Práctica", §16 (60 bloques, 22 imágenes). Adapter y Proxy separados en concepto + implementación.
  - Nuevas: "Adapter vs Proxy vs Decorator" y los ejercicios de Decorator (abrigos) y Proxy + Adapter (WeChat).
  - Verificación: 0 errores, 0 advertencias.
- **2026-10-09 — Patrones creacionales.**
  - Fuente: "Resumen Prueba Práctica", §17 hasta el final (43 bloques, 6 imágenes). Abstract Factory, Builder y Factory Method separados en concepto + implementación; Singleton con el ejemplo `MainFolder` de las slides.
  - Nueva: "Factory Method vs Abstract Factory". La tabla de "Qué es un patrón de diseño" quedó enlazada completa.
  - Verificación: 0 errores, 0 advertencias. Con esto, "Resumen Prueba Práctica" queda cubierto completo.
- **Nota técnica:** `.venv` no existe en el repo, así que el verificador usa solo la biblioteca estándar de Python.
