# Progreso de la migración — Introducción al Álgebra (MAT1207)

Rama: `migrar/intros-matematicos`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Introducción al Álgebra" --tema "<Tema>"` y se reproducen con sympy los cálculos de ejemplos y ejercicios. Pausas de revisión: después del tema 2 (piloto), del 7, del 11 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Introducción al Álgebra/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Lógica proposicional | `01-Lógica proposicional/` | ✅ hecho | 7 + índice | 0 |
| 2 | Técnicas de demostración e inducción | `02-Técnicas de demostración e inducción/` | ✅ hecho | 6 + índice | 0 |
| 3 | Conjuntos y operaciones | `03-Conjuntos y operaciones/` | ✅ hecho | 8 + índice | 2 |
| 4 | Cuantificadores y negación | `04-Cuantificadores y negación/` | ✅ hecho | 5 + índice | 0 |
| 5 | Polinomios: división y algoritmo de Euclides | `05-Polinomios: división y algoritmo de Euclides/` | ✅ hecho | 4 + índice | 0 |
| 6 | Polinomios: raíces y gráfica | `06-Polinomios: raíces y gráfica/` | ✅ hecho | 6 + índice | 0 |
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
- **2026-11-07 · Lógica proposicional (piloto).** Fuentes: clase Semana 1 (proposiciones, conectivos, tautologías, leyes, técnicas de demostración) y los apuntes de lógica proposicional (auxiliar MA1101). Se reconstruyó la negación, que en los PDF se pierde (se usa barra sobre la letra). Ejercicios: 7 (guía del curso y tarea 1), con dos erratas de la guía registradas en DUDAS. 7 notas; sin imágenes (las fuentes son texto).
- **2026-11-07 · Técnicas de demostración e inducción (piloto).** Fuentes: clase Semana 2 (principio de inducción, plantilla, cambio de caso base, definiciones por inducción) y los apuntes de Linero sobre la demostración (método directo y contraejemplos). Ejercicios: 6 (guía del curso y tarea 1), incluida una suma telescópica con potencias de $2$. 6 notas; sin imágenes (las fuentes son texto).
- **2026-11-07 · Conjuntos y operaciones.** Fuentes: clase Semana 3 (conjuntos, pertenencia, notación, igualdad, vacío, universo, cardinalidad, subconjuntos, unión, intersección, diferencia, complemento, De Morgan, álgebra de conjuntos y aplicaciones a encuestas). Los diagramas de Venn son vectoriales en la clase y se regeneraron con `figuras/venn.py` (2 PNG, `tipo: "generada"`). Ejercicios: 6 (guía del curso). 8 notas; 2 figuras.
- **2026-11-07 · Cuantificadores y negación.** Fuentes: clase Semana 4 (funciones proposicionales, cuantificadores $\forall$, $\exists$, $\exists!$, demostración con cuantificadores, orden de cuantificadores y negación). Ejercicios: 5 (guía del curso). 5 notas; sin imágenes (las fuentes son texto).
- **2026-11-07 · Polinomios: división y algoritmo de Euclides.** Fuentes: clase Semana 5 (funciones polinomiales, grado, coeficientes, $\mathbb{K}[x]$, igualdad, grado de suma y producto, algoritmo de la división y teorema del resto). Ejercicios: 5 (guía del curso y tarea 2), incluido hallar $c$ para que $x^2+c$ divida a $2x^3-x^2+6x-3$. 4 notas; sin imágenes (las fuentes son texto).
- **2026-11-07 · Polinomios: raíces y gráfica.** Fuentes: clase de polinomios semana 6 (raíces, teorema del factor, ceros racionales, irreducibles, factorización en $\mathbb{R}$, teorema fundamental del álgebra, raíces conjugadas y gráfica/comportamiento final). El comportamiento final se tabuló (la clase lo da en gráficas vectoriales). Ejercicios: 5 (guía del curso). 6 notas; sin imágenes.
