# Progreso de la migración — Sistemas Operativos y Redes (IIC2333)

Rama: `migrar/sistemas-operativos-y-redes`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Sistemas Operativos y Redes"` (y la verificación de los otros ramos del vault: Bases de Datos e Ingeniería de Software).

| # | Tema | Carpeta | Estado | Notas | Imágenes (apuntes + slides) |
|---|---|---|---|---|---|
| 0 | Infraestructura (`verificar.py`, `_meta/Sistemas Operativos y Redes/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Estructura de sistemas operativos | `Estructura de sistemas operativos/` | 🟡 pendiente | – | – |
| 2 | Procesos | `Procesos/` | 🟡 pendiente | – | – |
| 3 | Planificación de CPU | `Planificación de CPU/` | 🟡 pendiente | – | – |
| 4 | Señales e IPC | `Señales e IPC/` | 🟡 pendiente | – | – |
| 5 | Hilos | `Hilos/` | 🟡 pendiente | – | – |
| 6 | Sincronización | `Sincronización/` | 🟡 pendiente | – | – |
| 7 | Administración de memoria | `Administración de memoria/` | 🟡 pendiente | – | – |
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

