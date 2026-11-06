# Progreso de la migración — Arquitectura de Sistemas de Software (IIC2173)

Rama: `migrar/arquitectura-sistemas-software`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Arquitectura de Sistemas de Software" --tema "<Tema>"` revisando el código de salida (solo este ramo).

Orden de trabajo (pedido del usuario, que prepara la I2): primero los temas 14 a 25 (materia nueva de la I2), después el repaso 01 a 13 y al final 26 a 28. Las carpetas se numeran en el orden del curso.

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Arquitectura de Sistemas de Software/`) | `_meta/Arquitectura de Sistemas de Software/` | ✅ hecho | – | – |
| 1 | Fundamentos de la arquitectura de software | `01-Fundamentos de la arquitectura de software/` | ⏳ pendiente | – | – |
| 2 | Cohesión acoplamiento y connascence | `02-Cohesión acoplamiento y connascence/` | ⏳ pendiente | – | – |
| 3 | Componentes quanta y documentación | `03-Componentes quanta y documentación/` | ⏳ pendiente | – | – |
| 4 | Características arquitectónicas y escenarios | `04-Características arquitectónicas y escenarios/` | ⏳ pendiente | – | – |
| 5 | Atributos estructurales | `05-Atributos estructurales/` | ⏳ pendiente | – | – |
| 6 | Atributos operacionales | `06-Atributos operacionales/` | ⏳ pendiente | – | – |
| 7 | Atributos transversales | `07-Atributos transversales/` | ⏳ pendiente | – | – |
| 8 | DDD estratégico | `08-DDD estratégico/` | ⏳ pendiente | – | – |
| 9 | Diagramación y UML de componentes | `09-Diagramación y UML de componentes/` | ⏳ pendiente | – | – |
| 10 | Estilos jerárquicos y de capas | `10-Estilos jerárquicos y de capas/` | ⏳ pendiente | – | – |
| 11 | Flujo de datos e invocación implícita | `11-Flujo de datos e invocación implícita/` | ⏳ pendiente | – | – |
| 12 | Arquitecturas orientadas a servicios | `12-Arquitecturas orientadas a servicios/` | ⏳ pendiente | – | – |
| 13 | Otros estilos arquitectónicos | `13-Otros estilos arquitectónicos/` | ⏳ pendiente | – | – |
| 14 | Integración y relaciones entre contextos | `14-Integración y relaciones entre contextos/` | ✅ hecho | 6 + `_Índice` | 2 + 1 convertida + 1 slide |
| 15 | Middleware orientado a mensajes | `15-Middleware orientado a mensajes/` | ✅ hecho | 5 + `_Índice` | 1 apuntes + 2 slide |
| 16 | REST y contratos de API | `16-REST y contratos de API/` | ✅ hecho | 5 + `_Índice` | 5 apuntes + 1 convertida + 1 slide |
| 17 | gRPC GraphQL y MCP | `17-gRPC GraphQL y MCP/` | ⏳ pendiente | – | – |
| 18 | DDD táctico | `18-DDD táctico/` | ⏳ pendiente | – | – |
| 19 | Fundamentos de performance | `19-Fundamentos de performance/` | ⏳ pendiente | – | – |
| 20 | Hardware red y performance | `20-Hardware red y performance/` | ⏳ pendiente | – | – |
| 21 | Caché y protocolos web | `21-Caché y protocolos web/` | ⏳ pendiente | – | – |
| 22 | Asincronía y control de demanda | `22-Asincronía y control de demanda/` | ⏳ pendiente | – | – |
| 23 | Medición de escalabilidad | `23-Medición de escalabilidad/` | ⏳ pendiente | – | – |
| 24 | Métodos de escalabilidad | `24-Métodos de escalabilidad/` | ⏳ pendiente | – | – |
| 25 | Escalabilidad de datos | `25-Escalabilidad de datos/` | ⏳ pendiente | – | – |
| 26 | Resolución de casos de diseño | `26-Resolución de casos de diseño/` | ⏳ pendiente | – | – |
| 27 | Infraestructura y despliegue en la nube | `27-Infraestructura y despliegue en la nube/` | ⏳ pendiente | – | – |
| 28 | Gestión del curso | `28-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md) y [`NIVEL-DETALLE.md`](NIVEL-DETALLE.md): detalle alto (hasta 150 líneas) y de 5 a 8 preguntas de repaso plegables. `mapeo.json` fija `"preguntas_repaso": [5, 8]`, que `verificar.py` usa en lugar del rango 3 a 5 de los otros ramos.
- `mapeo.json` lleva `"cobertura": "reescrita"`: la prueba [3] entrega advertencias informativas.
- Sin comas en nombres de carpetas ni de notas; nombres únicos en todo el vault; sin marcas de procedencia en las notas de contenido (las notas de casos y de gestión del curso sí nombran las evaluaciones, porque son su tema).
- Imágenes: las `.png` de Notion se copian con su SHA-256 intacto (`tipo: "apuntes"`); las fotos `.heic` se convierten a `.png` con `sips` y se recortan si hace falta (`tipo: "convertida"`); los diagramas de slides entran con `pdftoppm -r 110` (`tipo: "slide"`, `original: "…pdf#page=N"`).
- Enlaces a otros ramos en vez de duplicar: Sistemas Distribuidos (CAP, consistencia, colas, pub/sub, gRPC, OAuth, líder), Ingeniería de Software (UML de clases y secuencia, patrones de diseño, capas, SOA, microservicios, Docker), Bases de Datos (índices).

## Registro
- **2026-11-06 · Infraestructura.** Se crea la rama y `_meta/Arquitectura de Sistemas de Software/` (`mapeo.json` con los 28 temas, `imagenes.json` vacío, `PROGRESS.md`, `DUDAS.md` y `NIVEL-DETALLE.md`). `verificar.py` acepta `"preguntas_repaso"` por ramo. Temario aprobado por el usuario.
- **2026-11-06 · Tema 14 (piloto).** `14-Integración y relaciones entre contextos`: 6 notas + `_Índice`. Fuentes: sección "Clase 13: Integración" de `Clases I2` (hasta "Recordando el Monolito"), slides 1-24 de Integración v2, AY09, pregunta 2.b de la I2 2026-1, pregunta 1.b del examen 2025-2 y 2.a de la I1 2025-2 (convertidas en preguntas de repaso). Imágenes: 2 PNG de Notion, la foto de la pizarra recortada y la slide 20 (niveles de integración). `_Índice.md` del ramo creado con el tema 14. Pausa para que el usuario revise el piloto.
- **2026-11-06 · Tema 15.** `15-Middleware orientado a mensajes`: 5 notas + `_Índice`. Fuentes: `Clases I2` desde "Recordando el Monolito" hasta "Rest", slides 25-37 de Integración v2, pregunta 1 de la I1 2026-2 y 3.a de la I1 2025-2 (orquestación vs coreografía) y 3.2.b del examen 2025-2 (MOM). Imágenes: 1 PNG de Notion y 2 slides recortadas (29 y 30).
- **2026-11-06 · Tema 16.** `16-REST y contratos de API`: 5 notas + `_Índice`. Fuentes: `Clases I2` desde "Rest" hasta "gRPC" (incluye el flujo de una request y OpenAPI), slides 38-76 de Integración v2, pregunta 4.c del examen 2024-2 y 3.b de la I1 2025-2. Imágenes: 5 PNG de Notion (dos son copias de las slides 58-59), la foto del croquis convertida y la slide 43 (árbol de derivación) recortada.
