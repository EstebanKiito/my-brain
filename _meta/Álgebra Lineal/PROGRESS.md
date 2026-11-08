# Progreso de la migración — Álgebra Lineal (MAT1203)

Rama: `migrar/algebra-lineal`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Álgebra Lineal" --tema "<Tema>"` y se reproducen con sympy todos los cálculos de ejemplos y ejercicios. Pausas de revisión: después del tema 2 (piloto), del 6, del 11, del 14 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Álgebra Lineal/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Vectores en Rⁿ | `01-Vectores en Rⁿ/` | ✅ hecho | 5 + índice | 5 |
| 2 | Rectas, planos e hiperplanos | `02-Rectas, planos e hiperplanos/` | ✅ hecho | 4 + índice | 3 |
| 3 | Sistemas de ecuaciones lineales | `03-Sistemas de ecuaciones lineales/` | ✅ hecho | 4 + índice | 2 |
| 4 | Reducción por filas | `04-Reducción por filas/` | ✅ hecho | 4 + índice | 0 |
| 5 | Conjuntos solución e independencia lineal | `05-Conjuntos solución e independencia lineal/` | ✅ hecho | 5 + índice | 4 |
| 6 | Transformaciones lineales | `06-Transformaciones lineales/` | ✅ hecho | 4 + índice | 4 |
| 7 | Álgebra de matrices, inversa y LU | `07-Álgebra de matrices, inversa y LU/` | ✅ hecho | 7 + índice | 2 |
| 8 | Determinantes | `08-Determinantes/` | ✅ hecho | 6 + índice | 4 |
| 9 | Espacios y subespacios vectoriales | `09-Espacios y subespacios vectoriales/` | ✅ hecho | 6 + índice | 3 |
| 10 | Coordenadas, dimensión y rango | `10-Coordenadas, dimensión y rango/` | ✅ hecho | 4 + índice | 1 |
| 11 | Cambio de base | `11-Cambio de base/` | ✅ hecho | 3 + índice | 2 |
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
- Fuentes: slides de clase (41 PDF; su numeración difiere del clase a clase desde la clase 27), clase a clase (indica las secciones del Lay) y el Lay para teoremas y contenidos sin slide (LU).
- Cada tema cierra con una nota **Ejercicios de prueba**: preguntas de interrogaciones y exámenes (banco de Ejercita, 2021-2026; PDF 2013-2019 de respaldo) con desarrollo completo escrito y verificado con sympy. Ejercita solo trae la respuesta final; si no calza con el cálculo, se registra en DUDAS.md.
- Figuras del Lay (vectoriales) recortadas de un render a 200 dpi con `pdftoppm`, registradas con `tipo: "libro"`. Figuras y GIF generados con matplotlib a partir de los ejemplos de las notas; el script queda en `_meta/Álgebra Lineal/figuras/` y se registran con `tipo: "generada"`.
- Figuras de las slides extraídas con `pdfimages` (imagen + máscara alfa sobre fondo blanco), sin los pies de figura del libro, registradas con `tipo: "clase"`.

## Registro
- **2026-11-07 · Vectores en Rⁿ (piloto).** Fuentes: slides 1-3 (vectores, combinaciones lineales, Gen, producto punto, norma, distancia, Cauchy-Schwarz, ángulo, ortogonalidad, Pitágoras) y Lay 1.3. Se agregaron el patrón de demostración con productos punto, la no linealidad de la norma y la no transitividad de la ortogonalidad. Ejercicios: 7 (Ejercita 2021-2026 y PDF 2018-2019), uno con datos imposibles registrado en DUDAS. 5 notas; 5 figuras de clase.
- **2026-11-07 · Rectas, planos e hiperplanos (piloto).** Fuentes: slides 3-4 (rectas, planos, ángulo entre planos, hiperplanos, tablas resumen). Se agregaron el producto cruz y la distancia punto-plano (no están en las slides pero se usan en las interrogaciones), el diagrama de posición relativa de dos rectas y las rectas alabeadas. Ejercicios: 8 (Ejercita). 4 notas; 3 figuras de clase.
- **2026-11-07 · Sistemas de ecuaciones lineales.** Fuentes: slides 5-7 (intersección de planos, SEL, matrices, operaciones de fila, Ax, equivalencias) y Lay 1.1, 1.3 y 1.4 (teorema de existencia con pivote en cada fila). Las dos figuras son composiciones de las figuras de planos de la slide 5 (páginas 3 y 8-10). Ejercicios: 8 (Ejercita). 4 notas; 2 figuras de clase.
- **2026-11-07 · Reducción por filas.** Fuentes: slides 8-10 (formas escalonadas, pivotes, algoritmo, bacterias, variables libres, criterio de consistencia, sistema con parámetro $a$) y Lay 1.2. Se agregaron el diagrama del algoritmo, la lectura de relaciones entre columnas en la FER y los errores típicos. Ejercicios: 8 (Ejercita). 4 notas; sin imágenes (las slides son texto).
- **2026-11-07 · Conjuntos solución e independencia lineal.** Fuentes: slides 11-12 (sistemas homogéneos, traslación, varios lados derechos, construir un sistema a partir de su solución, independencia lineal y casos simples) y Lay 1.5 y 1.7. Ejercicios: 16 en dos notas (Ejercita). 5 notas; 1 figura de clase.
- **2026-11-07 · Transformaciones lineales.** Fuentes: slides 13-14 (transformación matricial, linealidad, propiedades, matriz estándar, rotación, sobre e inyectiva) y Lay 1.8-1.9, incluidas las tablas de las págs. 73-75 (escritas como tabla) y los ejercicios 19 (pág. 69) y 35 (pág. 79) del clase a clase. Ejercicios: 8 (Ejercita); se verificó que la respuesta de 2022-1-i1-8 (entrada 11/15) es correcta, aunque no se usó por requerir inversa. 4 notas; 1 figura de clase.
- **2026-11-07 · Figuras para temas 05 y 06 (a pedido del usuario).** Tema 05: tres figuras de Lay 1.7 (dos vectores LD/LI en R², tres vectores en R³ según si w está en Gen{u, v}, tres vectores en R² siempre LD). Tema 06: lámina del cuadrado unitario bajo ocho transformaciones del catálogo y dos GIF (trasquilado y rotación), generados con `figuras/transformaciones_del_plano.py`.
- **2026-11-07 · Álgebra de matrices, inversa y LU.** Fuentes: slides 15-17 (operaciones, producto, transpuesta, inversa, matrices elementales, algoritmo de la inversa, teorema de la matriz invertible) y Lay 2.1-2.3; la factorización LU (Lay 2.5) no tiene slide, pero se incluyó porque aparece en casi todas las I2. Ejercicios: 16 en dos notas (Ejercita); el ejercicio LU de 4 × 4 de la I2 2022-1 es el ejemplo 1 de Lay 2.5. 7 notas; 1 figura de clase y 1 del Lay.
- **2026-11-07 · Determinantes.** Fuentes: slides 18-21 (cofactores, propiedades, invertibilidad, det AB, linealidad por columnas, Cramer, adjunta, área y volumen, elipse) y Lay 3.1-3.3. El ejemplo de 5 × 5 de la slide 18 se tomó del Lay (el texto extraído de la slide estaba desordenado). Se agregaron det(adj A) = (det A)^(n-1), que aparece en las pruebas, y un GIF generado sobre área y orientación. Ejercicios: 16 en dos notas (Ejercita). 6 notas; 3 figuras de clase y 1 generada.
- **2026-11-07 · Espacios y subespacios vectoriales.** Fuentes: slides 22-24 (espacio vectorial, subespacios, Gen, LI y bases, teorema del conjunto generador, Nul, Col, núcleo y rango) y Lay 4.1-4.3. Tres figuras recortadas del Lay (las slides no traen figuras). Ejercicios: 16 en dos notas (Ejercita; las de núcleo y rango en P2 estaban clasificadas como transformaciones). 6 notas; 3 figuras del libro.
- **2026-11-07 · Coordenadas, dimensión y rango.** Fuentes: slides 25-26 (coordenadas, isomorfismo, dimensión, teorema de la base, espacio fila, teorema del rango, continuación del teorema de la matriz invertible) y Lay 4.4-4.6. Ejercicios: 8 (Ejercita), algunos agrupando V o F relacionados. 4 notas; 1 figura de clase.
- **2026-11-07 · Cambio de base.** Fuentes: slide 27 (cambio de base, P C←B, inversa, cambio en Rⁿ y a la base estándar) y Lay 4.7. Ejercicios: 7 (Ejercita). 3 notas; 2 figuras de clase (a la primera se le quitó el pie de figura).
