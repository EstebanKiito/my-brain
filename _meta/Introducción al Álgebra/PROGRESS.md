# Progreso de la migración — Introducción al Álgebra (MAT1207)

Rama: `migrar/intros-matematicos`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Introducción al Álgebra" --tema "<Tema>"` y se reproducen con sympy los cálculos de ejemplos y ejercicios. Pausas de revisión: después del tema 2 (piloto), del 7, del 11 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Introducción al Álgebra/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Lógica proposicional | `01-Lógica proposicional/` | ⏳ pendiente | – | – |
| 2 | Técnicas de demostración e inducción | `02-Técnicas de demostración e inducción/` | ⏳ pendiente | – | – |
| 3 | Conjuntos y operaciones | `03-Conjuntos y operaciones/` | ⏳ pendiente | – | – |
| 4 | Cuantificadores y negación | `04-Cuantificadores y negación/` | ⏳ pendiente | – | – |
| 5 | Polinomios: división y algoritmo de Euclides | `05-Polinomios: división y algoritmo de Euclides/` | ⏳ pendiente | – | – |
| 6 | Polinomios: raíces y gráfica | `06-Polinomios: raíces y gráfica/` | ⏳ pendiente | – | – |
| 7 | Trigonometría: razones y resolución de triángulos | `07-Trigonometría: razones y resolución de triángulos/` | ⏳ pendiente | – | – |
| 8 | Funciones trigonométricas e identidades | `08-Funciones trigonométricas e identidades/` | ⏳ pendiente | – | – |
| 9 | Números complejos, inversas y ecuaciones trigonométricas | `09-Números complejos, inversas y ecuaciones trigonométricas/` | ⏳ pendiente | – | – |
| 10 | Geometría analítica: distancia, circunferencia y división de segmentos | `10-Geometría analítica: distancia, circunferencia y división de segmentos/` | ⏳ pendiente | – | – |
| 11 | Cónicas: parábola, elipse e hipérbola | `11-Cónicas: parábola, elipse e hipérbola/` | ⏳ pendiente | – | – |
| 12 | Geometría vectorial: componentes, producto punto y cruz | `12-Geometría vectorial: componentes, producto punto y cruz/` | ⏳ pendiente | – | – |
| 13 | Gestión del curso | `13-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md): un concepto por nota, de 60 a 120 líneas (máximo 150), prosa explicativa, definiciones y teoremas en `[!tip]`, LaTeX y preguntas de repaso plegables.
- Fuentes: las clases semanales (`Clases 2022/SemanaN.pdf`) son la fuente principal; el libro de precálculo (Mickenberg) y los apuntes de demostraciones (Linero, Lógica proposicional) aportan teoremas y demostraciones que las clases citan sin desarrollar.
- Cada tema cierra con una nota **Ejercicios de prueba**: preguntas de las interrogaciones, tareas y exámenes de `Pruebas/` (2022–2026, con pauta), con desarrollo completo escrito y verificado con sympy. Si la pauta no calza con el cálculo, se registra en `DUDAS.md`.
- Figuras de las clases extraídas con `pdftoppm`/`pdfimages`, registradas con `tipo: "clase"`. Diagramas generados con matplotlib cuando aclaren; el script queda en `_meta/Introducción al Álgebra/figuras/` y se registran con `tipo: "generada"`.

## Registro
- **2026-11-07 · Infraestructura.** Se creó `_meta/Introducción al Álgebra/` con `mapeo.json`, `imagenes.json`, `PROGRESS.md` y `DUDAS.md`. Temario de 12 temas de contenido + Gestión del curso, propuesto y aprobado por el usuario.
