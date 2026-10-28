# Progreso de la migración — Algoritmos y Sistemas Computacionales (IIC1001)

Rama: `migrar/algoritmos-sistemas-computacionales`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Algoritmos y Sistemas Computacionales" --tema "<Tema>"` revisando el código de salida, y también se verifican los demás ramos porque el grafo es del vault completo. Pausas de revisión: después del tema 2 (piloto), del tema 6 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Algoritmos y Sistemas Computacionales/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Introducción a los sistemas computacionales | `01-Introducción a los sistemas computacionales/` | ⬜ pendiente | – | – |
| 2 | Representación numérica | `02-Representación numérica/` | ⬜ pendiente | – | – |
| 3 | Operaciones binarias y complemento a dos | `03-Operaciones binarias y complemento a dos/` | ⬜ pendiente | – | – |
| 4 | Codificación de caracteres | `04-Codificación de caracteres/` | ⬜ pendiente | – | – |
| 5 | Compuertas lógicas y lógica proposicional | `05-Compuertas lógicas y lógica proposicional/` | ⬜ pendiente | – | – |
| 6 | Circuitos sumadores | `06-Circuitos sumadores/` | ⬜ pendiente | – | – |
| 7 | Multiplexores y demultiplexores | `07-Multiplexores y demultiplexores/` | ⬜ pendiente | – | – |
| 8 | Programabilidad de circuitos digitales | `08-Programabilidad de circuitos digitales/` | ⬜ pendiente | – | – |
| 9 | Sistemas operativos | `09-Sistemas operativos/` | ⬜ pendiente | – | – |
| 10 | Complejidad algorítmica | `10-Complejidad algorítmica/` | ⬜ pendiente | – | – |
| 11 | Grafos | `11-Grafos/` | ⬜ pendiente | – | – |
| 12 | Gestión del curso | `12-Gestión del curso/` | ⬜ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md), con detalle medio-alto y lenguaje para primer año: cada concepto parte de un problema concreto, sin tecnicismo elevado.
- No hay export de Notion ni apuntes propios. Fuentes: PDF de clase (`Clases/`), pruebas y actividades con sus soluciones (`Pruebas/`, `Actividades/`) y ayudantía (`Extra/`).
- Los contenidos de los PDF se reescriben dentro de las notas; los PDF y las slides no se suben al repo. Solo las figuras útiles van como PNG en `adjuntos/`, registradas con `tipo: "clase"`.
- Solape con otros ramos: se escribe la versión de primer año y se enlaza la nota avanzada en vez de duplicar. Sistemas operativos → `Sistemas Operativos y Redes`; complejidad → `Estructuras de Datos/01-Análisis de algoritmos`; grafos → `Estructuras de Datos/15-Grafos y DFS` y `17-Caminos más cortos`; algoritmo → `Introducción a la Programación/01-Algoritmos y pensamiento computacional`.

## Pendientes por falta de material
El curso original tiene clases que no vienen en el export de PDFs (faltan las clases 10, 11, 13, 19, 20, 21, 22, 24, 25 y 26). Por eso **no se migran** los siguientes temas del programa, y quedan registrados aquí y en `DUDAS.md`:
- Funcionamiento de Internet.
- Herramientas computacionales: GitHub y LaTeX.
- Estructuras secuenciales.
- Algoritmos de ordenamiento (la clase 23 anuncia "Martes 9-junio: algoritmos de ordenamiento", pero el PDF no está).
- Árboles (el programa menciona "grafos y árboles"; solo hay PDF de grafos).

Si más adelante aparecen esos PDFs, se agregan al `mapeo.json` y se migran como temas nuevos.

## Registro
- **2026-10-28 · Infraestructura.** Se crea la rama `migrar/algoritmos-sistemas-computacionales` y `_meta/Algoritmos y Sistemas Computacionales/` (`mapeo.json` con 12 temas y `pdfs` informativos, `imagenes.json` vacío, `PROGRESS.md` y `DUDAS.md`). Se verifican los 21 PDF de clase, las 5 actividades con solución, las 2 pruebas con solución y la ayudantía. Temario aprobado por el usuario. Sin dudas.
