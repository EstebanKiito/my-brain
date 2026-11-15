# Progreso de la migración — Introducción al Cálculo (MAT1107)

Rama: `migrar/introduccion-calculo`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Introducción al Cálculo" --tema "<Tema>"` y se reproducen con sympy los cálculos de ejemplos y ejercicios. Pausas de revisión: después del tema 2 (piloto), del 6, del 9 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Introducción al Cálculo/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Números reales: axiomas de cuerpo y de orden | `01-Números reales: axiomas de cuerpo y de orden/` | ✅ hecho | 7 + índice | 0 |
| 2 | Valor absoluto y raíces | `02-Valor absoluto y raíces/` | ⏳ pendiente | – | – |
| 3 | Inecuaciones | `03-Inecuaciones/` | ⏳ pendiente | – | – |
| 4 | Funciones reales: gráficas y transformaciones | `04-Funciones reales: gráficas y transformaciones/` | ⏳ pendiente | – | – |
| 5 | Polinomios y funciones racionales | `05-Polinomios y funciones racionales/` | ⏳ pendiente | – | – |
| 6 | Composición, inversa y biyecciones | `06-Composición, inversa y biyecciones/` | ⏳ pendiente | – | – |
| 7 | Exponencial y logaritmo | `07-Exponencial y logaritmo/` | ⏳ pendiente | – | – |
| 8 | Sucesiones, monotonía y axioma del supremo | `08-Sucesiones, monotonía y axioma del supremo/` | ⏳ pendiente | – | – |
| 9 | Sumas finitas, binomio y aplicaciones financieras | `09-Sumas finitas, binomio y aplicaciones financieras/` | ⏳ pendiente | – | – |
| 10 | Límites de sucesiones y álgebra de límites | `10-Límites de sucesiones y álgebra de límites/` | ⏳ pendiente | – | – |
| 11 | Cálculo de límites y límites infinitos | `11-Cálculo de límites y límites infinitos/` | ⏳ pendiente | – | – |
| 12 | Gestión del curso | `12-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md): un concepto por nota, de 60 a 120 líneas (máximo 150), prosa explicativa, definiciones y teoremas en `[!tip]`, LaTeX y preguntas de repaso plegables (3 a 8).
- Fuentes: las clases (`Clases/clase1..25.pdf`, 2022-1) son la fuente principal; el libro de precálculo (Mickenberg; Stewart de respaldo) aporta teoremas y demostraciones que las clases citan sin desarrollar (polinomios, sucesiones, axioma del supremo, límites).
- Cada tema cierra con una nota **Ejercicios de la guía de …** (guías 1-10 de 2023) y otra **Ejercicios de prueba de …**: preguntas de las interrogaciones, tareas y exámenes de `PRUEBAS/` (2020-2026), con desarrollo completo escrito y verificado con sympy. Si la pauta no calza con el cálculo, se registra en `DUDAS.md`.
- Figuras: las clases las dibujan como gráficos vectoriales, así que se recortan de un render a 200 dpi de la página (`pdftoppm`), registradas con `tipo: "clase"`. Si la clase no tiene la figura, se recorta del Mickenberg (`tipo: "libro"`) o de la pauta (`tipo: "clase"`). No se generan figuras propias.
- Nombres de nota únicos en todo el vault: se revisan las colisiones con Introducción al Álgebra y Álgebra Lineal; si el concepto ya existe allí, se enlaza en vez de duplicar.

## Registro
- **2026-11-15 · Infraestructura.** Se creó `_meta/Introducción al Cálculo/` con `mapeo.json`, `imagenes.json`, `PROGRESS.md` y `DUDAS.md`. Temario de 11 temas de contenido + Gestión del curso, propuesto en el plan y aprobado por el usuario. Fuentes inventariadas: 25 clases (la clase 24 tiene una segunda versión, `clase24 (1).pdf`, por comparar), Mickenberg, Stewart, 10 guías, ~75 pruebas 2020-1 a 2026-1 (con pauta en 2022-1, 2023-2, 2024-2, 2025-2, parte de 2026-1 y la tarea), ayudantías 2022-1 a 2024-1 y el cuaderno manuscrito (sin texto, solo contraste).
- **2026-11-15 · Números reales: axiomas de cuerpo y de orden (piloto).** Fuentes: clases 1 a 3 (axiomas de cuerpo, consecuencias, axiomas de orden, $\mathbb{R}^+$, cuadrados e inversos, ejemplos de desigualdades) y Guía 1. Ejercicios de prueba: 9 preguntas de I0, I1 e I2 de 2020-1, 2022-1, 2022-2, 2023-1, 2023-2, 2024-1, 2025-1, 2025-2 y 2026-1, con identidades verificadas con sympy y desigualdades muestreadas numéricamente. Para $a<b \Rightarrow a^3<b^3$ (I1 2025-2) se da una prueba sin casos, además del método de la pauta. 7 notas; sin imágenes (las clases no traen figuras en este tema).
