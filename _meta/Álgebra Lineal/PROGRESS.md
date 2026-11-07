# Progreso de la migración — Álgebra Lineal (MAT1203)

Rama: `migrar/algebra-lineal`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Álgebra Lineal" --tema "<Tema>"` y se reproducen con sympy todos los cálculos de ejemplos y ejercicios. Pausas de revisión: después del tema 2 (piloto), del 6, del 11, del 14 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Álgebra Lineal/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Vectores en Rⁿ | `01-Vectores en Rⁿ/` | ✅ hecho | 5 + índice | 5 |
| 2 | Rectas, planos e hiperplanos | `02-Rectas, planos e hiperplanos/` | ✅ hecho | 4 + índice | 3 |
| 3 | Sistemas de ecuaciones lineales | `03-Sistemas de ecuaciones lineales/` | ⏳ pendiente | – | – |
| 4 | Reducción por filas | `04-Reducción por filas/` | ⏳ pendiente | – | – |
| 5 | Conjuntos solución e independencia lineal | `05-Conjuntos solución e independencia lineal/` | ⏳ pendiente | – | – |
| 6 | Transformaciones lineales | `06-Transformaciones lineales/` | ⏳ pendiente | – | – |
| 7 | Álgebra de matrices, inversa y LU | `07-Álgebra de matrices, inversa y LU/` | ⏳ pendiente | – | – |
| 8 | Determinantes | `08-Determinantes/` | ⏳ pendiente | – | – |
| 9 | Espacios y subespacios vectoriales | `09-Espacios y subespacios vectoriales/` | ⏳ pendiente | – | – |
| 10 | Coordenadas, dimensión y rango | `10-Coordenadas, dimensión y rango/` | ⏳ pendiente | – | – |
| 11 | Cambio de base | `11-Cambio de base/` | ⏳ pendiente | – | – |
| 12 | Valores y vectores propios | `12-Valores y vectores propios/` | ⏳ pendiente | – | – |
| 13 | Diagonalización | `13-Diagonalización/` | ⏳ pendiente | – | – |
| 14 | Valores propios complejos | `14-Valores propios complejos/` | ⏳ pendiente | – | – |
| 15 | Ortogonalidad y complemento ortogonal | `15-Ortogonalidad y complemento ortogonal/` | ⏳ pendiente | – | – |
| 16 | Proyecciones y Gram-Schmidt | `16-Proyecciones y Gram-Schmidt/` | ⏳ pendiente | – | – |
| 17 | Mínimos cuadrados | `17-Mínimos cuadrados/` | ⏳ pendiente | – | – |
| 18 | Matrices simétricas y formas cuadráticas | `18-Matrices simétricas y formas cuadráticas/` | ⏳ pendiente | – | – |
| 19 | Cholesky y descomposición en valores singulares | `19-Cholesky y descomposición en valores singulares/` | ⏳ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md) con detalle alto (hasta ~150 líneas): definiciones y teoremas en `[!tip]`, intuición geométrica, demostraciones cortas cuando aclaran y ejemplos resueltos paso a paso. Todo en LaTeX.
- Fuentes: slides de clase (41 PDF; su numeración difiere del clase a clase desde la clase 27), clase a clase (indica las secciones del Lay) y el Lay para teoremas y contenidos sin slide (rango, LU).
- Cada tema cierra con una nota **Ejercicios de prueba**: preguntas de interrogaciones y exámenes (banco de Ejercita, 2021-2026; PDF 2013-2019 de respaldo) con desarrollo completo escrito y verificado con sympy. Ejercita solo trae la respuesta final; si no calza con el cálculo, se registra en DUDAS.md.
- Figuras de las slides extraídas con `pdfimages` (imagen + máscara alfa sobre fondo blanco), sin los pies de figura del libro, registradas con `tipo: "clase"`.

## Registro
- **2026-11-07 · Vectores en Rⁿ (piloto).** Fuentes: slides 1-3 (vectores, combinaciones lineales, Gen, producto punto, norma, distancia, Cauchy-Schwarz, ángulo, ortogonalidad, Pitágoras) y Lay 1.3. Se agregaron el patrón de demostración con productos punto, la no linealidad de la norma y la no transitividad de la ortogonalidad. Ejercicios: 7 (Ejercita 2021-2026 y PDF 2018-2019), uno con datos imposibles registrado en DUDAS. 5 notas; 5 figuras de clase.
- **2026-11-07 · Rectas, planos e hiperplanos (piloto).** Fuentes: slides 3-4 (rectas, planos, ángulo entre planos, hiperplanos, tablas resumen). Se agregaron el producto cruz y la distancia punto-plano (no están en las slides pero se usan en las interrogaciones), el diagrama de posición relativa de dos rectas y las rectas alabeadas. Ejercicios: 8 (Ejercita). 4 notas; 3 figuras de clase.
