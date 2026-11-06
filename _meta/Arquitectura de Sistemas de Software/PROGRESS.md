# Progreso de la migración — Arquitectura de Sistemas de Software (IIC2173)

Rama: `migrar/arquitectura-sistemas-software`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Arquitectura de Sistemas de Software" --tema "<Tema>"` revisando el código de salida (solo este ramo).

Orden de trabajo (pedido del usuario, que prepara la I2): primero los temas 14 a 25 (materia nueva de la I2), después el repaso 01 a 13 y al final 26 a 28. Las carpetas se numeran en el orden del curso.

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Arquitectura de Sistemas de Software/`) | `_meta/Arquitectura de Sistemas de Software/` | ✅ hecho | – | – |
| 1 | Fundamentos de la arquitectura de software | `01-Fundamentos de la arquitectura de software/` | ✅ hecho | 3 + `_Índice` | 4 apuntes + 0 slide |
| 2 | Cohesión acoplamiento y connascence | `02-Cohesión acoplamiento y connascence/` | ✅ hecho | 3 + `_Índice` | 4 apuntes + 3 convertida + 0 slide |
| 3 | Componentes quanta y documentación | `03-Componentes quanta y documentación/` | ✅ hecho | 2 + `_Índice` | 1 apuntes + 2 convertida + 0 slide |
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
| 17 | gRPC GraphQL y MCP | `17-gRPC GraphQL y MCP/` | ✅ hecho | 5 + `_Índice` | 1 apuntes + 0 slide |
| 18 | DDD táctico | `18-DDD táctico/` | ✅ hecho | 6 + `_Índice` | 0 apuntes + 5 slide |
| 19 | Fundamentos de performance | `19-Fundamentos de performance/` | ✅ hecho | 3 + `_Índice` | 0 apuntes + 2 slide |
| 20 | Hardware red y performance | `20-Hardware red y performance/` | ✅ hecho | 3 + `_Índice` | 0 apuntes + 2 slide |
| 21 | Caché y protocolos web | `21-Caché y protocolos web/` | ✅ hecho | 3 + `_Índice` | 0 apuntes + 5 slide |
| 22 | Asincronía y control de demanda | `22-Asincronía y control de demanda/` | ✅ hecho | 3 + `_Índice` | 0 apuntes + 3 slide |
| 23 | Medición de escalabilidad | `23-Medición de escalabilidad/` | ✅ hecho | 3 + `_Índice` | 0 apuntes + 2 slide |
| 24 | Métodos de escalabilidad | `24-Métodos de escalabilidad/` | ✅ hecho | 3 + `_Índice` | 0 apuntes + 3 slide |
| 25 | Escalabilidad de datos | `25-Escalabilidad de datos/` | ✅ hecho | 5 + `_Índice` | 0 apuntes + 3 slide |
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
- **2026-11-06 · Tema 17.** `17-gRPC GraphQL y MCP`: 5 notas + `_Índice`. Fuentes: `Clases I2` desde "gRPC" hasta el final, slides 77-90 de Integración v2, alternativa 2.b del examen 2025-2, AY09 (caso del satélite del examen 2024-2) y pregunta 2.b de la I2 2026-1. Imágenes: 1 PNG de Notion.
- **2026-11-06 · Tema 18.** `18-DDD táctico`: 6 notas + `_Índice`. No hay apuntes de Notion de este tema: fuente única las 15 slides de `19ab - bloque-ddd-tactico.pdf` (con el código de Sairyss/domain-driven-hexagon, MIT, reescrito y comentado). AY07 y AY08 tratan DDD estratégico y quedan para el tema 08. Imágenes: 5 slides recortadas (4, 6, 10, 11 y 12).
- **2026-11-06 · Tema 19.** `19-Fundamentos de performance`: 3 notas + `_Índice`. Fuentes: slides 1-14 y 54 de Performance, la sección "Clase 16: Performance" de `Syllabus/I2/Apuntes_I2.pdf` (export más nuevo que el HTML de Notion, que llega solo hasta MCP), AY09 (escenario del dashboard), pregunta 3.2.b y alternativa 2.a de la pauta I2 2025-2. Cálculos M/M/1 y percentiles comprobados con python3.
- **2026-11-06 · Tema 20.** `20-Hardware red y performance`: 3 notas + `_Índice`. Fuentes: slides 15-35 de Performance, pregunta 1.a de la pauta I2 2025-2 (combinar dos problemas de la red) y 1.b de la pauta I2 2025-1 (latencia de las sondas). Imágenes: slides 15 y 27 recortadas.
- **2026-11-06 · Tema 21.** `21-Caché y protocolos web`: 3 notas + `_Índice`. Fuentes: slides 37-54 de Performance; preguntas de caché de la pauta I2 2024-2 (1.a, alternativas y caso News Hunter), examen 2025-1 (2.a), I2 2025-2 (2.c), compilado I2 (caché por tienda y caso 2026-1 donde la caché no conviene). Imágenes: 5 slides recortadas.
- **2026-11-06 · Tema 22.** `22-Asincronía y control de demanda`: 3 notas + `_Índice`. Fuentes: slides 55-79 de Performance y AY09 (pregunta del robot EVA y la asincronía). Imágenes: slides 58, 65 y 72 recortadas. Errata de la slide de NodeJS registrada en DUDAS.
- **2026-11-06 · Tema 23.** `23-Medición de escalabilidad`: 3 notas + `_Índice`. Fuentes: slides 1-16 de Escalabilidad. Ejemplos numéricos de Little, Amdahl (tabla para p = 50, 75, 90 y 95%) y Gustafson comprobados con python3. Imágenes: slides 14 y 15 recortadas.
- **2026-11-06 · Tema 24.** `24-Métodos de escalabilidad`: 3 notas + `_Índice`. Fuentes: slides 17-39 de Escalabilidad y la sección de horizontal vs vertical de `Apuntes_I2.pdf`. Imágenes: slides 22, 23 y 33.
- **2026-11-06 · Tema 25.** `25-Escalabilidad de datos`: 5 notas + `_Índice`. Fuentes: slides 40-77 de Escalabilidad; pregunta 1.b y alternativas 2.a de la I2 2026-1 (CAP en una mina, leader-follower, sharding y particionado vertical), 1.b de la pauta I2 2025-2 (relacional frente a NoSQL) y 1.a y 1.c de la pauta I2 2024-2 (bases por sección y sharding). Imágenes: slides 46, 61 y 65. **Cierre del bloque I2 (temas 14-25)**: pausa para que el usuario revise.
- **2026-11-06 · Tema 01.** `01-Fundamentos de la arquitectura de software`: 3 notas + `_Índice`. Fuentes: `Clases i1` (Clase 1 hasta "Plan del Curso" y de "Facts clave" a "Cohesión"), slides 1-34 y 50-56 de Introducción, alternativa 2.a del examen 2025-2. Imágenes: 4 PNG de Notion.
- **2026-11-06 · Tema 02.** `02-Cohesión acoplamiento y connascence`: 3 notas + `_Índice`. Fuentes: `Clases i1` desde "Cohesión" hasta "Clase 3", slides 57-66 de Introducción, pregunta 1.a del examen 2025-1 (big ball of mud). Imágenes: 4 PNG de Notion y 3 fotos convertidas.
- **2026-11-06 · Tema 03.** `03-Componentes quanta y documentación`: 2 notas + `_Índice`. Fuentes: `Clases i1` desde "Clase 3" hasta "Clase 4" y slides 67-78 de Introducción. Imágenes: 1 PNG de Notion y 2 fotos convertidas.
