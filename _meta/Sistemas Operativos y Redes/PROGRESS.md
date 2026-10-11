# Progreso de la migración — Sistemas Operativos y Redes (IIC2333)

Rama: `migrar/sistemas-operativos-y-redes`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Sistemas Operativos y Redes"` (y la verificación de los otros ramos del vault: Bases de Datos e Ingeniería de Software).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`verificar.py`, `_meta/Sistemas Operativos y Redes/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Estructura de sistemas operativos | `Estructura de sistemas operativos/` | ✅ hecho | 7 + índice | 8 |
| 2 | Procesos | `Procesos/` | ✅ hecho | 7 + índice | 7 |
| 3 | Planificación de CPU | `Planificación de CPU/` | ✅ hecho | 5 + índice | 11 |
| 4 | Señales e IPC | `Señales e IPC/` | ✅ hecho | 3 + índice | 0 |
| 5 | Hilos | `Hilos/` | ✅ hecho | 3 + índice | 3 |
| 6 | Sincronización | `Sincronización/` | ✅ hecho | 9 + índice | 25 |
| 7 | Administración de memoria | `Administración de memoria/` | ✅ hecho | 6 + índice | 16 |
| 8 | Paginación y segmentación | `Paginación y segmentación/` | 🟡 pendiente | – | – |
| 9 | Memoria virtual | `Memoria virtual/` | 🟡 pendiente | – | – |
| 10 | Sistemas de archivos | `Sistemas de archivos/` | 🟡 pendiente | – | – |
| 11 | Implementación de archivos y bloques | `Implementación de archivos y bloques/` | 🟡 pendiente | – | – |
| 12 | Fundamentos de redes y modelos en capas | `Fundamentos de redes y modelos en capas/` | 🟡 pendiente | – | – |
| 13 | Capa de aplicación y sockets | `Capa de aplicación y sockets/` | 🟡 pendiente | – | – |
| 14 | Capa de transporte | `Capa de transporte/` | 🟡 pendiente | – | – |
| 15 | Capa de red y direccionamiento | `Capa de red y direccionamiento/` | 🟡 pendiente | – | – |
| 16 | Algoritmos de ruteo | `Algoritmos de ruteo/` | 🟡 pendiente | – | – |
| 17 | Capa de enlace y seguridad | `Capa de enlace y seguridad/` | 🟡 pendiente | – | – |
| 18 | Gestión del curso + mapa final | `Gestión del curso/` | 🟡 pendiente | – | – |

## Convenciones
- Las mismas de Bases de Datos e Ingeniería de Software: prefijo `NN - ` con orden de estudio por carpeta, wikilinks con alias (`\|` dentro de tablas) e índices enlazados con ruta completa.
- Tags `so/<tema>` + `origen/apuntes` u `origen/complemento`.
- **Slides:** ningún PDF ni PPTX entra al repo. Las slides útiles se convierten a PNG (`pdftoppm -r 110`), van en `adjuntos/` dentro de un callout que cita la clase y se registran en `imagenes.json` con `tipo: "slide"` y `original: …pdf#page=N`.
- **Transcripción de imágenes:** toda imagen lleva un callout plegable `> [!example]- Transcripción de la imagen` con su contenido detallado en texto o código.
- **Dudas y erratas:** el texto original de los apuntes se conserva tal cual; los posibles errores se señalan con callouts `> [!warning] Posible error` y se registran en `DUDAS.md`.

## Registro
- **2026-10-11 — Infraestructura.** Creación de `_meta/Sistemas Operativos y Redes/` (`mapeo.json`, `imagenes.json`, `PROGRESS.md`, `DUDAS.md`). Se definió la arquitectura del curso en 18 temas (11 de Sistemas Operativos, 6 de Redes y Gestión del curso). Verificación multi-ramo en limpio: 0 errores, 0 advertencias.
- **2026-10-11 — Estructura de sistemas operativos.** Fuentes: Clase 1 y Clase 2 completas (108 bloques). 7 notas atómicas + índice. 8 imágenes migradas con sha256 y transcritas. Complementos de `Contenido_1.pdf` y Tanenbaum. Errata marcada en `DUDAS.md` para "MONOLITICO: Falta todo". Verificación: 0 errores, 0 advertencias.
- **2026-10-11 — Procesos.** Fuentes: Clase 3 y Clase 4 de SSOO más Ayudantía 1 (147 bloques totales: 115 de ssoo + 32 de ayudantías). 7 notas atómicas + índice. 7 imágenes migradas con sha256 y transcritas. Complementos de `Contenido_2_Procesos.pdf` y OSTEP. Verificación: 0 errores, 0 advertencias.
- **2026-10-11 — Planificación de CPU.** Fuentes: sección SCHEDULERS de apuntes de SSOO (65 bloques). 5 notas atómicas + índice. 11 imágenes migradas con sha256 y transcritas. Complementos de `Contenido_3_Scheduling.pdf` y OSTEP (métricas, FCFS/SJF convoy effect, RR quantum trade-offs, y 5 reglas de MLFQ). Verificación: 0 errores, 0 advertencias.
- **2026-10-11 — Señales e IPC.** Fuentes: secciones Signals y SEÑALES de SSOO (14 bloques). 3 notas atómicas + índice. Complementos de `Contenido_2_Procesos.pdf` y POSIX (ciclo de señales, diferencias semánticas SIGTERM vs SIGKILL, handlers en C con signal/sigaction, y pipes anónimos). Verificación: 0 errores, 0 advertencias.
- **2026-10-11 — Hilos.** Fuentes: Clase 5 de SSOO (49 bloques). 3 notas atómicas + índice. 3 imágenes migradas con sha256 y transcritas. Complementos de `Contenido_4_Threads.pdf` y POSIX Threads (recursos compartidos vs privados, pthreads en C, y modelos User Space vs Kernel Space vs híbridos M:N). Verificación: 0 errores, 0 advertencias.
- **2026-10-11 — Sincronización.** Fuentes: CONTENIDO 5: SINCRONIZACIÓN de apuntes de SSOO (68 bloques). 9 notas atómicas + índice. 25 imágenes migradas con sha256 y transcritas (incluye diagramas y slides de apoyo). Complementos de `Contenido_5_Sincronizacion.pdf` y Silberschatz (condiciones de carrera, requisitos de sección crítica, Peterson, primitivas atómicas de hardware, mutex vs spinlocks, buffer acotado, semáforos de Dijkstra, variables de condición/monitores, lectores-escritores, filósofos comelones y condiciones de Coffman para deadlock). Verificación: 0 errores, 0 advertencias.
- **2026-10-11 — Administración de memoria.** Fuentes: Clase 6 de apuntes de SSOO (124 bloques). 6 notas atómicas + índice. 16 imágenes migradas con sha256 y transcritas. Complementos de `Contenido_6_Memoria.pdf`, Silberschatz y OSTEP (memoria como arreglo de bytes, multiprogramación, relocalización vs protección, registros base y límite en MMU, swapping, fragmentación externa, algoritmos First Fit / Best Fit / Worst Fit, segmentación y lógica/máscaras de bits). Verificación: 0 errores, 0 advertencias.

