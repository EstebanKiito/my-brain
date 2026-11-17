# Progreso de la migración — Matemáticas Discretas (IIC1253)

Rama: `migrar/matematicas-discretas`. Un commit por tema. Antes de cada commit se corre `python3 _meta/verificar.py --ramo "Matemáticas Discretas" --tema "<Tema>"` y se verifican con Python los cálculos de ejemplos y ejercicios. Pausas de revisión: después del tema 4, del 8 y al cierre.

| # | Tema | Carpeta | Estado | Notas | Imágenes |
|---|---|---|---|---|---|
| 0 | Infraestructura (`_meta/Matemáticas Discretas/`) | `_meta/` | ✅ hecho | – | – |
| 1 | Inducción simple, fuerte y estructural | `01-Inducción simple, fuerte y estructural/` | ⏳ pendiente | – | – |
| 2 | Lógica proposicional y equivalencia | `02-Lógica proposicional y equivalencia/` | ⏳ pendiente | – | – |
| 3 | Satisfacibilidad, consecuencia y resolución | `03-Satisfacibilidad, consecuencia y resolución/` | ⏳ pendiente | – | – |
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
