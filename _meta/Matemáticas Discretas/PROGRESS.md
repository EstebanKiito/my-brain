# Progreso de la migración — Matemáticas Discretas (IIC1253)

Rama: `migrar/matematicas-discretas`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Matemáticas Discretas" --tema "<Tema>"` y se verifican con Python los cálculos de ejemplos y ejercicios. Pausas de revisión: después del tema 4, del 8 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Matemáticas Discretas/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Inducción simple, fuerte y estructural | `01-Inducción simple, fuerte y estructural/` | ✅ hecho | 8 + índice | 1 |
| 2 | Lógica proposicional y equivalencia | `02-Lógica proposicional y equivalencia/` | ✅ hecho | 9 + índice | 4 |
| 3 | Satisfacibilidad, consecuencia y resolución | `03-Satisfacibilidad, consecuencia y resolución/` | ✅ hecho | 9 + índice | 3 |
| 4 | Lógica de predicados y métodos de demostración | `04-Lógica de predicados y métodos de demostración/` | ⏳ pendiente | – | – |
| 5 | Teoría de conjuntos | `05-Teoría de conjuntos/` | ⏳ pendiente | – | – |
| 6 | Relaciones y relaciones de equivalencia | `06-Relaciones y relaciones de equivalencia/` | ⏳ pendiente | – | – |
| 7 | Conjunto cuociente, órdenes y elementos extremos | `07-Conjunto cuociente, órdenes y elementos extremos/` | ⏳ pendiente | – | – |
| 8 | Funciones y cardinalidad | `08-Funciones y cardinalidad/` | ⏳ pendiente | – | – |
| 9 | Algoritmos y complejidad | `09-Algoritmos y complejidad/` | ⏳ pendiente | – | – |
| 10 | Grafos, caminos y ciclos | `10-Grafos, caminos y ciclos/` | ⏳ pendiente | – | – |
| 11 | Árboles | `11-Árboles/` | ⏳ pendiente | – | – |
| 12 | Aritmética modular y criptografía | `12-Aritmética modular y criptografía/` | ⏳ pendiente | – | – |
| 13 | Gestión del curso | `13-Gestión del curso/` | ⏳ pendiente | – | – |

## Convenciones
- Notas según [`_meta/ESTANDAR-NOTAS.md`](../ESTANDAR-NOTAS.md): un concepto por nota, de 60 a 120 líneas (máximo 150), prosa explicativa, definiciones y teoremas en `[!tip]`, LaTeX y preguntas de repaso plegables (3 a 8).
- Fuentes: las clases (`Clases/00..27`, Sebastián Bugedo) son la fuente principal; los apuntes de Jorge Pérez y de Luis Dissett y el libro complementan demostraciones y figuras.
- Cada tema cierra con una nota **Ejercicios de ayudantías y tareas** y otra **Ejercicios de prueba**: selección curada (8-12 preguntas, todos los tipos) del banco de ejercicios de licc-cursos-app y de las pautas de `Pruebas/`, con solución reescrita y verificada.
- Figuras: se recortan de las clases (render a 200 dpi con `pdftoppm`, `tipo: "clase"`); si no están en clase, de los apuntes o del libro (`tipo: "libro"`) o de los enunciados (`tipo: "clase"`). No se generan figuras propias.
- Nombres de nota únicos en todo el vault (se revisan colisiones con Álgebra, Cálculo, EDD, Algoritmos…): si el concepto ya existe en otro ramo, se enlaza.

## Registro
- **2026-11-17 · Inducción simple, fuerte y estructural (piloto).** Fuentes: clases 1 y 2 (buen orden, PIS, PICV, equivalencia, definiciones inductivas, listas $L_\mathbb{N}$, inducción estructural), ayudantía de inducción (5 ejercicios, con la figura de las regiones del plano) y 9 preguntas de I1, I3 y Examen 2015-2 a 2020-1 del banco de ejercicios. Verificadas numéricamente con Python las fórmulas (suma de cuadrados, $n! > 2^n$, $F_n \le 2^n$, $G_n \le 3^n$, $2p + 7q$, Fibonacci mod 5 y paridad). 8 notas + índice; las clases no traen figuras en este tema.
- **2026-11-17 · Satisfacibilidad, consecuencia y resolución.** Fuentes: clases de satisfacibilidad y consecuencia y de consecuencia y resolución, ayudantías 3 y 4 (parte proposicional), banco de ejercicios de lógica proposicional (I1/examen 2015-2 a 2026-1). Verificaciones con Python (fuerza bruta de valuaciones): modus ponens, modus tollens, demostración por partes, inconsistencia de los conjuntos de las trazas, CNF/DNF de (p∧q)→(r∧¬q), redundancia de {p,q,p↔q}, consecuencia de 10 variables (1024 valuaciones), contraejemplos de uniones y consecuencia débil, equivalencia α⊨β ⇔ α≡α∧β y propiedades de consecuencia (modelado como conjuntos de mundos), cláusulas conjuntivas, 3-coloreo (triángulo sí, K4 no) y fórmula de jaulas contra conteo directo.
- **2026-11-17 · Lógica proposicional y equivalencia.** **Estado (PROGRESS):** Lógica proposicional y equivalencia: 7 notas de teoría + 2 de ejercicios + índice, 4 imágenes.

**Registro:** Fuentes: clases de lógica proposicional y de equivalencia lógica, ayudantía de lógica proposicional, banco de ejercicios (11 preguntas de prueba: 2015-2 a 2026-1) y figuras de enunciados 2018-2-i1-3 y 2026-1-i1-2. Verificaciones: con Python se recalcularon todas las leyes de equivalencia, la tabla de φ (≡ q↔r) y su DNF/CNF, NAND, traducciones a {¬,→}, Superman (64 valuaciones), tabla EQ, la equivalencia larga, el dual, CNF/DNF/mayoría 2024-2, CNF 2025-2, tautología 2026-1, δ (CNF, DNF, NOR), contraejemplos de 2019-1 (n=3..6), bicondicionales recursivos (k=1..4), paridad de modelos de XOR.

- ℹ️ **Anidamiento de implicaciones 2019-1 (n=1).** La pauta dice "solo n=1,2", pero γ_1 es una conjunción vacía (sin implicaciones); en la nota se afirma solo n=2.
- ℹ️ **Ayudantía de lógica proposicional.** El PDF de soluciones repite el encabezado "Ayudantía 1 - Inducción" en cada página; se usó el contenido (dual, Superman, EQ, equivalencia larga) y se omitió el ejercicio de palíndromos (pertenece al tema de inducción).
- ℹ️ **Formas normales.** La clase no define DNF/CNF por nombre (solo la construcción desde la tabla); los términos "literal", "cláusula", DNF y CNF se tomaron de las pruebas y el banco de ejercicios.
- ℹ️ **2022-1-i1-4.** El máximo real de fórmulas no equivalentes y satisfacibles es 2^(2^n−1), mayor que lo pedido 2^(2^(n−1)); la nota usa lo correcto.
